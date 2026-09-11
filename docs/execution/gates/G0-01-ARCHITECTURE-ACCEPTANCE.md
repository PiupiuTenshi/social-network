# G0-01 — Nghiệm thu kiến trúc trước nghiệp vụ

- Quyết định: **PASS cho P0 foundation**.
- Ngày: `2026-09-08`
- Phạm vi: chỉ xác nhận đầu vào và harness nền tảng cho các task sau G0; không
  nghiệm thu tính năng nghiệp vụ hay môi trường production.

## Kết luận theo tiêu chí G0

| Tiêu chí | Kết luận | Artifact đã rà soát |
| --- | --- | --- |
| Ownership | PASS | ADR-0012 và `docs/data/p0/data-blueprint.json`: 4 logical DB, 27 bảng P0, một owner cho mỗi bảng; validator chặn FK xuyên DB. |
| Schema P0 | PASS | Blueprint, Chat/Feed schema, indexes theo access pattern, outbox/inbox, checkpoint/export/rebuild; P0 text-only. |
| API/error | PASS | ADR-0011, OpenAPI P0 và fixtures: 30 operations, permissions, DTO/error envelope, cursor, ETag/412, idempotency/409, and the cookie-bound refresh operation. |
| Event/privacy | PASS | AsyncAPI 7 message và fixtures: partition key, aggregate version, actor/scope, replay correlation, fail-closed policy propagation. |
| Dependency direction | PASS | Solution has Api → Application → Domain; architecture harness passed against Account.Domain project and compiled assembly. |
| Migration evidence | PASS | `InitialEmpty` has empty `Up`/`Down`; migration harness applied it to a disposable SQLite database. |
| Toolchain/build | PASS | Pinned .NET/EF/Node/Angular/container metadata, NuGet/npm locks; .NET build and Angular build completed successfully. |

## Blocker disposition

| Blocker | G0 disposition |
| --- | --- |
| BL-01 | Closed by canonical `AGENTS.md` audit evidence. |
| BL-02 … BL-06 | Closed for P0 by ADR-0011, OpenAPI/AsyncAPI and contract fixtures. |
| BL-17 | Closed for the harness prerequisite by PH00-BE-TOOLCHAIN-01. |
| BL-07 … BL-16 | Remain planned P1/P2 decisions; not P0 capability and not enabled. |
| BL-18 | Remains PH01 CI/remote-readiness work; no remote or protected-branch claim is made. |

## Constraints carried forward

- Docker daemon was unavailable during PH00. The PostgreSQL compose pin exists but
  was not started; only the disposable SQLite migration test is accepted here.
- P0 blueprint/contracts are implementation inputs, not deployed services or applied
  production schemas.
- Every successor remains subject to its own `task_gate.py check`, DoR, contract/data
  scope and evidence. This PASS does not make a downstream task automatically READY.
