# Definition of Ready — PH01-FE-FOUNDATION-02

- TASK_ID: `PH01-FE-FOUNDATION-02`
- Scope: Angular HTTP/auth/realtime client adapters and generated P0 TypeScript types only.
- Owner boundary: Account owns refresh-token rotation and authorization. This frontend code holds only an access token in memory and never implements server authorization or refresh persistence.

## Inputs reviewed

- PH01-FE-FOUNDATION-01 is `DONE` with the locked Angular workspace, shell and feature-flag foundation.
- ADR-0014 and `POST /auth/refresh` define cookie transport, refresh rotation behavior visible to the client, and terminal `refresh_invalid`/`refresh_reused` behavior.
- P0 OpenAPI/fixtures define the `Session` response, error response shape, 412/429 cases, and cookie-bound refresh operation.
- SignalR remains an application realtime channel; LiveKit remains separate RTC transport. No SignalR JavaScript package is present in the locked workspace, so the deliverable is a typed adapter seam and lifecycle contract, not an invented wire-protocol implementation.

## Delivery and verification

The implementation will generate TypeScript contract types from P0 OpenAPI with a repository script; provide a single-flight refresh coordinator; map Problem Details, 412 and 429; preserve request body and Idempotency-Key across one post-refresh retry; support AbortSignal and latest-response control; and provide a transport-agnostic realtime adapter interface.

Tests will run through a dependency-free TypeScript-to-JavaScript harness for concurrency, terminal refresh, retry, cancellation, stale response and realtime lifecycle behavior, followed by Angular typecheck, formatting and production build. No persistent token storage, token logging, mock release transport, new dependency, backend change, migration, Git or deployment is in scope.
