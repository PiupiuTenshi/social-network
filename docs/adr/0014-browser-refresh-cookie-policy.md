# ADR-0014: Browser refresh session policy

- Status: Accepted
- Date: 2026-09-11
- Decision owner: Project owner
- Supersedes: the absence of a browser refresh contract in ADR-0011 P0 inputs

## Decision

The browser receives a short-lived access token only in the JSON `Session` response
and keeps it in application memory. It never stores an access or refresh token in a
URL, log, `localStorage`, `sessionStorage`, IndexedDB, or persistent client cache.

`POST /auth/refresh` rotates the opaque refresh credential carried only in a
`HttpOnly`, `Secure` (outside local development), `SameSite=Lax`, path-scoped refresh
cookie. Its successful response is a new `Session`; the response does not contain a
refresh token. The Account service invalidates the previous token family member on
rotation and treats reuse as session-family compromise.

The refresh operation is anonymous at the access-token layer but requires the refresh
cookie. The service validates `Origin` for browser requests and rejects unsafe
cross-origin refresh attempts. Credentialed CORS, if deployed, is restricted to the
configured exact frontend origins; wildcard origins are prohibited. Logout revokes the
refresh family and clears the cookie. `401 refresh_invalid` and `401 refresh_reused`
are terminal: the frontend clears its in-memory access token and does not retry refresh.

## Consequences

Frontend sends at most one refresh request at a time, retries the original request once
after a successful refresh, preserves its body and `Idempotency-Key`, and never retries
the refresh endpoint itself. Server implementation, Account migration, rotation/reuse
tests and origin/CORS enforcement belong to Account tasks. This decision adds the P0
OpenAPI operation and fixtures required for PH01-FE-FOUNDATION-02.
