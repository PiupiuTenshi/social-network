# PH01-FE-FOUNDATION-02 — Implementation and test evidence

- Task: `PH01-FE-FOUNDATION-02`
- Goal: HTTP, auth and realtime adapters with error handling and lifecycle control.
- Recorded: 2026-09-11 UTC
- Environment: Windows PowerShell; Node v22.19.0; npm 11.6.0; Angular 21 locked workspace.
- Baseline: local workspace; no Git commit, remote, deployment, migration, or dependency installation was performed.

## Delivered

- `frontend/scripts/generate-p0-types.mjs` generates all P0 OpenAPI schemas as TypeScript and formats the generated file with the locked Prettier configuration.
- `AccessTokenStore` retains only the access token in memory. `AuthRefreshCoordinator` shares one in-flight refresh operation and clears that memory state after `refresh_invalid` or `refresh_reused`.
- `P0ApiClient` preserves the original request body and `Idempotency-Key` for one post-refresh retry, uses cookie credentials, maps failures, and cancels an obsolete keyed request.
- `BrowserRefreshTransport` binds refresh to the configured API base path and forwards `AbortSignal`.
- `problem-details.ts` maps the P0 error envelope and Problem Details, including 412 and 429.
- `SignalRRealtimeAdapter` defines connection, subscribe and disconnect lifecycle through an injected SignalR boundary. `LiveKitAdapter` remains a separate interface.

## Acceptance mapping

| Acceptance | Evidence and result |
|---|---|
| AC01 | Generated P0 types, memory-only token store, single-flight coordinator and adapter harness prove concurrent refresh produces one rotation; no token is placed in URL or persistent storage. |
| AC02 | P0 client preserves body/idempotency on retry; harness covers terminal refresh, 412 mapping, cancellation and realtime lifecycle. Test doubles are confined to `frontend/tests`. |

## Commands actually run

| Command | Exit | Result |
|---|---:|---|
| `npm.cmd --prefix frontend run generate:p0-types` | 0 | Generated 10 P0 contract types. |
| `npm.cmd --prefix frontend run lint` | 0 | All frontend source files match Prettier. |
| `npm.cmd --prefix frontend run test:adapters` | 0 | Refresh, retry, failure, cancellation and realtime lifecycle harness passed. |
| `npm.cmd --prefix frontend run typecheck` | 0 | Angular application TypeScript check passed. |
| `npm.cmd --prefix frontend run build` | 0 | Angular production build passed. |
| `python -X utf8 scripts/validate_p0_contracts.py` | 0 | 30 operations, 7 messages, 11 API fixtures and 4 event fixtures validated. |
| `python -X utf8 -m py_compile scripts/task_gate.py` | 0 | Gate implementation compiled. |
| `python -X utf8 scripts/task_gate.py validate` | 0 | 318-subtask plan and state validated. |

## Gate mechanism correction

The earlier receipt algorithm revalidated the current hash of every old completion artifact. Adding this task's scripts to the shared frontend package therefore made the already accepted Foundation-01 receipt stale. `scripts/task_gate.py` now verifies all artifact hashes at submit/accept, then treats completion/review manifests as immutable handover snapshots. Later source/contract changes continue to invalidate through `source_hashes`; downstream compatibility continues to use `impact` and `dependency_scopes`. The evidence file itself remains hash-pinned in `state.json`, and each artifact must still exist and be nonempty.

## Limits and risks

- The locked workspace has no approved SignalR JavaScript dependency. This task provides the typed lifecycle boundary and does not claim a live SignalR wire connection.
- Browser refresh behavior is proven against P0 contract fixtures and the adapter harness. Account-service integration and browser end-to-end authentication remain owned by their later feature tasks.
- Two initial formatting/build attempts encountered a transient Windows `EPERM` file lock. After the lock cleared, formatting, harness, typecheck and build were rerun successfully as recorded above.
