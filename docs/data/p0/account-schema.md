# Account P0 schema decision

`Account` exclusively owns `account_db`. The mapping in
[`account-schema.json`](account-schema.json) is the PH02 refinement of the
PH00 data blueprint; it does not amend the PH00 baseline. Every relational FK
is local to `account_db`. Other services use the Account identity contract or
their local projections and have no foreign key or query into this database.

`email` and `username` are supplied in their approved canonical form before a
write. Their unique constraints are the final concurrency protection and map a
collision to the P0 `409` contract. Raw refresh credentials are never stored,
logged or exported: only `token_hash` is persisted.

The Account migration uses `expand -> backfill -> switch -> contract` with one
approved Account migration runner. Application replicas never migrate at
startup. Migration implementation and fixtures belong to
`PH02-DATA-ACC-P0-02`; this task creates no database objects.

Refresh-token rows are retained until expiry plus the approved security
retention window. Account lifecycle records follow the Account retention
policy. Backup/restore targets remain RPO <= 24 hours and RTO <= 4 hours.
