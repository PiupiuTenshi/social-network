# Implementation report - PH01-BE-PLATFORM-01

- TASK_ID: PH01-BE-PLATFORM-01
- Objective: BuildingBlocks, Gateway and baseline observability.
- Revalidated: 2026-09-11 on Windows PowerShell with .NET SDK 10.0.204.
- Scope: ADR-0013, accepted by the project owner.

## Acceptance mapping

| AC | Result in the accepted Platform scope | Evidence |
| --- | --- | --- |
| AC01 | PASS | The versioned envelope and Account Outbox/Inbox/idempotency records form the platform contract. The SQLite harness processes an event once and rejects its duplicate without a repeated side effect. |
| AC02 | PASS | The publisher marks an Outbox record only after Kafka acknowledgement. The harness begins a database transaction, writes an Outbox candidate, simulates failure before commit, and proves no persisted candidate remains. |
| AC03 | PASS | Gateway exposes Problem Details, JWT boundary configuration, CORS allowlist, rate limiting and protected proxy routes. The Account API sets and returns correlation IDs. Platform metrics define Outbox, Inbox duplicate, DLQ and lag contracts. The architecture harness proves the Domain boundary. |

## Commands executed

All commands completed with exit code 0.

| Command | Result |
| --- | --- |
| dotnet build TwightLight.slnx --no-restore | 8 projects built; 0 warnings and 0 errors. |
| dotnet run --project tests/Architecture/Architecture.Harness/Architecture.Harness.csproj --no-build | Account.Domain is framework-free. |
| dotnet run --project tests/Integration/Migration.Harness/Migration.Harness.csproj --no-build | Empty migration, Inbox idempotency and rolled-back Outbox checks passed. |

## Scope and remaining service evidence

Per ADR-0013, this task does not claim resource BOLA, production Kafka principal/ACL,
production JWT issuer/key, hosted consumer runtime, broker-down/crash-after-publish, or
end-to-end service contract tests. Account, Social, Chat and Feed must prove those items
against their own schema, endpoints and identities before their tasks are accepted.
