# Definition of Ready — PH02-DATA-ACC-P0-01

- TASK_ID: PH02-DATA-ACC-P0-01
- Owner: Account / `account_db`.
- Scope: Account P0 schema design only: `account`, `profile`, `refresh_token`, `account_setting`, constraints, indexes, migration and retention rationale.

| DoR | Result | Evidence |
| --- | --- | --- |
| Scope and acceptance | PASS | Prompt, P0 data blueprint and current Account persistence boundary define the four tables and required token/session fields. |
| Ownership and boundaries | PASS | `Account` is sole owner of `account_db`; no external FK or cross-database query is introduced. |
| Contract and security | PASS | P0 API defines account credentials/session behavior; refresh credentials are hash-only and browser refresh uses the approved cookie policy. |
| Verification | PASS | `validate_p0_data_blueprint.py` and the migration harness are available. |
| Migration and recovery | PASS | Expand/backfill/switch/contract strategy, one-runner policy and P0 RPO/RTO are documented. |

No destructive migration, production action, dependency addition or external credential is needed for this design task.
