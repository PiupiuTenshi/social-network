# ADR-0012: P0 data boundary, projection rebuild and recovery

- Status: Accepted
- Date: 2026-09-07
- Decision owner: project owner, delegated to PH00-DATA-BOUNDARY-01
- Depends on: ADR-0011

## Context

The reference data model assigns service ownership but summarizes Chat and Feed,
and does not make an executable P0 schema or rebuild procedure explicit. P0 also
requires text-only posts while the reference model includes a future video type.
Kafka retains data for a bounded period and cannot be a database backup.

## Decisions

1. `account_db`, `social_db`, `chat_db`, and `feed_db` are separate logical
   databases and separate migration/credential accounts even when an early
   environment shares a PostgreSQL instance. Each aggregate and table in the P0
   blueprint has one owner. No foreign key or query crosses a database boundary;
   external identifiers are opaque values verified by an API or an authorized
   projection.
2. The P0 physical table blueprint is
   [`../data/p0/data-blueprint.json`](../data/p0/data-blueprint.json). It makes
   Chat conversations, membership, messages, read cursor and notifications, and
   Feed entries, user summaries, post summaries, checkpoints and rebuild runs
   concrete. It also states version, unique and access-pattern indexes.
3. Every source-owning service writes its state change and immutable outbox record
   in one local transaction. Consumers record `(consumer_name, event_id)` in a
   local inbox or use an equivalent unique idempotency record in the same local
   transaction as the projection change. Delivery is at-least-once.
4. P0 `post.content` is text; `post.type` is fixed to `content` and no P0
   `post_media_ref` write exists. Video/media remains disabled reference work,
   consistent with ADR-0011.
5. Feed is a derived read model. It stores a source aggregate id and policy
   version, reauthorizes/withholds stale data, exports checkpoint manifests, and
   can be rebuilt from authorized source exports plus the outbox/event delta after
   the captured high-water mark. Kafka is transport with at least seven-day
   retention, never the recovery source of truth.
6. When the required Kafka offset is older than retention, the rebuild owner opens
   a `rebuild_run`, takes source export high-water marks, rebuilds in an isolated
   target, replays only the post-watermark delta, validates counts/checksums and
   authorization samples, then atomically promotes the new projection. A failed
   run is retained with its checkpoint and is never partially promoted.
7. Migrations are run only by an approved per-service migration runner, never by
   application startup and never concurrently. They follow expand/backfill/switch/
   contract. Backup verification applies before destructive changes. P0 targets are
   RPO <= 24 hours and RTO <= 4 hours, inherited from OPERATIONS_BASELINE.

## Consequences

The new blueprint and runbook are the accepted P0 data implementation inputs. The
legacy reference model remains audit evidence and must be synchronized in a later,
explicitly scoped task. Commands in the runbook are environment-verification
templates; no database, backup, restore, or migration is claimed to have run here.

