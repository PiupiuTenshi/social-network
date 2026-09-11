# Toolchain selection record — 2026-09-08

| Component | Pinned selection | Basis |
| --- | --- | --- |
| .NET SDK | 10.0.204 | Installed SDK selected by `global.json`; .NET 10 is an LTS release. |
| .NET runtime / EF Core | 10.0.8 | Installed shared runtime; central package management keeps EF Core aligned. |
| SQLite native transitive | 2.1.13 | Explicit central pin; replaces vulnerable 2.1.11 reported by restore. |
| Node | 22.19.0 | Installed version and Angular 21 compatible range. |
| Angular CLI | 21.2.23 | Latest 21.x version returned by npm Registry during this task. |
| Angular framework | 21.2.22 | Latest 21.x core version returned by npm Registry during this task. |
| PostgreSQL image | `postgres:17-alpine` plus SHA-256 manifest digest | Docker Official Image pin in compose; not started because no daemon was reachable. |

The frontend lockfile is the authoritative complete npm dependency graph. The .NET
restore lockfiles are the authoritative NuGet dependency graph. Update versions only
through a reviewed toolchain task, then regenerate both locks and rerun the harnesses.
