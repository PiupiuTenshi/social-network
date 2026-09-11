# PH01 local core infrastructure

`deploy/compose/compose.infrastructure.yml` is the local P0 infrastructure entry
point. It supersedes the PH00 PostgreSQL-only compose probe, which remains unchanged
as predecessor evidence.

## Environment isolation and secrets

Each environment uses a separate Compose project, named volumes, credentials and Kafka
prefix. Examples are in `deploy/compose/.env.example` and `deploy/compose/env/`.
Create a local, ignored development secret file:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/infra/new-local-secrets.ps1 -Environment dev
```

The tracked compose file requires every secret and identifier with `${VAR:?message}`.
It has no `ports:` mappings; PostgreSQL, Kafka, Valkey and SeaweedFS are available only
on the internal Compose network. Do not copy the generated dev `.env` to test or
staging.

## Start and verify

```powershell
# Requires Docker Desktop and a running Docker daemon.
powershell -ExecutionPolicy Bypass -File scripts/infra/infrastructure.ps1 -Action up
powershell -ExecutionPolicy Bypass -File scripts/infra/verify-infrastructure.ps1
```

The first command creates/starts the stack and waits for healthchecks. The verification
checks missing-config failure, host-port absence, account credential isolation,
profile-gated migration locking, PostgreSQL restart, and restore to a newly created
isolated probe database. It also verifies a namespaced Kafka topic survives restart.

## Migration runner

`migration-runner` has the `migrate` profile and is excluded from normal `up`. Invoke
it explicitly for exactly one logical database:

```powershell
docker compose --env-file deploy/compose/.env -f deploy/compose/compose.infrastructure.yml run --rm --no-deps -e TARGET_DATABASE=account_db migration-runner
```

The current runner records only an idempotent infrastructure ledger protected by one
transaction advisory lock per logical database. It is not an EF runner and does not
permit application replicas to migrate at startup. Service schema migrations remain
the responsibility of later per-service data tasks.
