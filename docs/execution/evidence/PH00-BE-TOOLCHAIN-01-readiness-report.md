# Definition of Ready report — PH00-BE-TOOLCHAIN-01

- TASK_ID: `PH00-BE-TOOLCHAIN-01`
- Recorded: `2026-09-08T05:27:41+07:00`
- Baseline: working-tree snapshot; `git rev-parse --is-inside-work-tree` returned
  exit code 128 because this repository has not been initialized as a Git worktree.
- Scope: create a minimal .NET/Angular toolchain, architecture harness, and an empty
  EF Core migration. No domain behaviour, product feature, production configuration,
  Git initialization, remote, branch, commit, push, tag, or deployment is included.

## Inputs, decisions, and dependencies

`PH00-DATA-BOUNDARY-01` is DONE with valid readiness, completion, and review receipts.
The required project rules, service boundaries, coding conventions, source structure,
and predecessor handoff were read before this report. The P0 contracts and data
boundary lock the dependency surface needed by a framework-only skeleton.

The implementation target is .NET 10 with the locally installed SDK `10.0.204` and
runtime `10.0.8`; EF Core packages will be centrally pinned to `10.0.8`, matching that
runtime. Node `22.19.0` is locally installed and satisfies Angular 21's supported Node
range. Angular CLI `21.2.23` and Angular core `21.2.22` were verified from npm; the
generated lockfile is the final dependency receipt. PostgreSQL is pinned in compose by
tag and manifest digest; it is a configuration artifact only because Docker's daemon
is unavailable on this workstation.

The skeleton has one framework-free Domain project, with the permitted dependency path
`Api -> Application -> Domain`; Infrastructure carries EF Core. An architecture console
harness will inspect the Domain project and compiled assembly references. An integration
console harness will apply a deliberately empty EF Core migration to a disposable local
SQLite file. This provides an executable migration test without pretending a Docker
database ran.

## Verification plan and stop conditions

The implementation will use `dotnet restore`, `dotnet build`, the architecture harness,
the SQLite migration harness, and `npm.cmd ci`/Angular build where the registry and
filesystem permit. Exact commands, exit codes, timestamps, versions, and hashes will be
recorded in the completion report. Docker compose validation is explicitly deferred:
the Docker client reported that its daemon pipe is unavailable. Any conflict in the P0
contract/data boundary, a package restore failure, a non-empty migration, a framework
reference in Domain, or a migration test failure stops the subtask.

## DoR conclusion

All seven Definition-of-Ready checks are satisfied for this bounded foundation task:
the output and acceptance criteria are observable; ownership, contracts and P0 data
boundaries are inherited from reviewed predecessors; the only persistent data action is
a disposable SQLite test migration; and the executor may create repository-local files
but has no authorization to perform Git or remote operations. The unavailable Docker
daemon is documented as an environment limitation, not hidden as a successful test.
