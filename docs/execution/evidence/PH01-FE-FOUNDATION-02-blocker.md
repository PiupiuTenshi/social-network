# Blocker resolution — PH01-FE-FOUNDATION-02

- Original blocker: missing P0 refresh endpoint and browser transport policy.
- Resolution: ADR-0014 and `docs/contracts/p0/openapi.json` now define `POST /auth/refresh`, an HttpOnly refresh cookie, memory-only Session access token, and terminal 401 behavior. Fixtures cover refresh success and reuse.
- Remaining scope limit: the locked workspace has no SignalR client package. The task will expose a typed SignalR adapter boundary only; actual protocol transport is deferred until a dependency is approved in its owning task.
- Result: DoR can be prepared; no backend contract or production behavior is inferred.
