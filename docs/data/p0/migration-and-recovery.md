# P0 migration and recovery plan

## Accountable roles and targets

| Activity | Accountable role | Target / acceptance evidence |
| --- | --- | --- |
| Generate/review one service script | Service owner + database reviewer | Script is idempotent where supported; checksum and compatibility review recorded. |
| Execute migration | Release operator | One runner lock per logical database; migration ledger reports the expected version. |
| Seed test data | Test-data owner | Isolated test database, deterministic manifest, synthetic data only. |
| Backup/restore drill | Operations owner | P0 RPO <= 24h and RTO <= 4h; restore to isolated instance and smoke-check account, post and message. |
| Projection rebuild | Feed owner | Export manifest, source watermarks, checkpoint, count/checksum and authorization samples pass before promotion. |

## From empty database

1. Create separate logical databases and least-privilege migration identities for
   Account, Social, Chat and Feed.
2. Generate a reviewed migration artifact per owner and record its checksum.
3. Apply each artifact once under the service migration lock, then verify the
   migration ledger and schema checksum.
4. Seed only a test environment from the checked-in synthetic seed manifest.
   Seeds use stable IDs, do not contain real credentials/PII, and exercise a
   relation, a block, a text post, a comment, a conversation and a message.
5. Start consumers only after their inbox/projection tables and source schema are
   present; seed events use the same outbox path as normal writes.

## Upgrade and rollback strategy

| Stage | Required control |
| --- | --- |
| Expand | Add nullable/default-safe structures and compatible indexes. Old and new binaries can read the schema. |
| Backfill | Batch with a persisted checkpoint, metric, throttle and resumable idempotency. Compare count and hash before switching. |
| Switch | Change reads/writes through a controlled flag; measure errors, lock time and latency. |
| Contract | Remove old structure only after a release cycle, consumer inventory and backup verification. |
| Roll back | Roll back code only while schema remains compatible; otherwise roll forward with a corrective migration. |

No migration runs at application startup. A destructive operation needs a verified
backup, restore plan, compatibility decision and release operator approval.

## Commands to verify in the real environment

The repository has no runtime solution, migration project, database URL or CI
runner. The following are **not executed evidence**; the named role must replace
placeholders and record command output, UTC time, artifact checksum and database
identity in the later migration task.

```powershell
# Service owner: generate reviewed, idempotent script
dotnet ef migrations script --idempotent --project <service-infrastructure-project> --startup-project <service-api-project> --output <approved-script.sql>

# Release operator: record current version before and after applying an approved script
psql "$env:TARGET_DATABASE_URL" --command "select migration_id from schema_migrations order by applied_at desc"
psql "$env:TARGET_DATABASE_URL" --file <approved-script.sql>

# Operations owner: create and test an isolated backup/restore artifact
pg_dump --format=custom --file <backup-file.dump> "$env:SOURCE_DATABASE_URL"
pg_restore --dbname "$env:ISOLATED_RESTORE_DATABASE_URL" --clean --if-exists <backup-file.dump>
```

`pg_restore --clean` is only for the isolated restore target, never an assumed
production command. Restore acceptance is migration-ledger/schema checksum match,
synthetic smoke reads, and measured elapsed time within the RTO target.

## Projection export, checkpoint and rebuild

Each Feed projection checkpoint records source name, source export id, source
high-water mark, consumer position, schema version, row count, content hash,
policy-version range, timestamp and status. The export manifest is durable with
the source backup. A rebuild run records the target namespace, input manifests,
start/finish UTC, validation result and promotion time.

When a consumer is behind Kafka retention:

1. Freeze promotion, create `rebuild_run`, and preserve the failed checkpoint.
2. Obtain authorized Account/Social/Chat source exports and their transaction or
   outbox high-water marks; do not infer missing records from Kafka.
3. Build a fresh Feed target from those exports. Apply privacy/block policy while
   loading; omit data whose policy cannot be verified.
4. Replay source outbox records after each captured high-water mark with inbox
   idempotency. Kafka may accelerate delivery only where offsets remain available.
5. Compare row counts and deterministic content hashes, sample access authorization,
   and ensure lag/checkpoint reaches the captured watermarks before atomic promotion.
6. Retain the old projection until promotion evidence passes; failed runs stay
   diagnosable and are not partially exposed.

Kafka configuration/schema is backed up, but Kafka event retention is not a backup
strategy. Source database backup plus authorized source export is the rebuild base.

