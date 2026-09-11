# Definition of Ready report — PH01-DATA-INFRA-01

- TASK_ID: `PH01-DATA-INFRA-01`
- Recorded: `2026-09-09T00:52:53+07:00`
- Scope: local Docker Compose infrastructure for PostgreSQL, Kafka, Valkey and
  SeaweedFS; per-service database credentials; a manually invoked migration runner;
  health, persistence, restart and isolated restore checks.
- Excluded: product services/features, P1 capabilities, host-published broker/DB
  ports, production/staging deployment, application auto-migration, Git and remote
  operations.

## Inputs and decisions

G0-01 is DONE. ADR-0012 requires four logical databases with separate credentials,
no cross-database foreign keys, one migration runner per database and no migration at
application startup. OPERATIONS_BASELINE requires environment separation, fail-fast
configuration, secret isolation, resource limits, Kafka retention and a minimal
backup/restore drill.

The existing compose file is an intentionally superseded PH00 probe: it has only a
public PostgreSQL port and a hard-coded development password. This task will replace
it rather than carry either unsafe property forward. Docker Desktop was started and
verified at implementation time: Server `28.4.0`, storage driver `overlayfs`, Compose
`v2.39.4-desktop.1`.

The accepted implementation shape is an internal-only Compose network, named volumes,
healthchecks and resource limits. Compose variables use required-value interpolation;
an ignored local `.env` contains randomly generated development secrets, while
tracked examples contain only names/placeholders. `account_db`, `social_db`,
`chat_db`, and `feed_db` receive separate login roles and CONNECT grants. The Kafka
topic prefix and Compose project name are environment-specific. A profile-gated
migration-runner accepts one target database, obtains a transaction advisory lock and
records only an infrastructure bootstrap ledger; it is never started with application
replicas.

## Verification and stop conditions

The task will validate Compose interpolation and syntax, bring the local stack up,
wait for all healthchecks, verify no host-published ports, verify failed cross-database
access with a service credential, run the migration runner twice plus a concurrent-lock
probe, then write/check a marker through PostgreSQL restart and restore it to a fresh
isolated database. Tests use synthetic marker data only and do not run a product or
destructive migration.

The task stops if image/configuration compatibility fails, a service is unhealthy,
credentials can connect across databases, a host port is published, the runner fails
to reject concurrency, persistence/restore fails, or any P0 owner/schema decision
changes. Docker daemon availability is now evidenced; no remaining external
dependency blocks this bounded local implementation.
