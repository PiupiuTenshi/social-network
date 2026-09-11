# PH03-DATA-CHT-P0-03 — Kiểm chứng dữ liệu CHT P0

## Mục tiêu và phạm vi

- Phase: PH03 | Nhóm: DATA | Ưu tiên: P0 | Task cha: PH03-DATA-CHT-P0.
- Mục tiêu duy nhất: Kiểm chứng dữ liệu CHT P0.
- Miền: chat | Chức năng: nền tảng/quy trình.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH03-DATA-CHT-P0-03`; chưa được tạo chỉ vì có trong prompt.
- conversation, conversation_member, message, message_reaction, notification; unique clientMessageId và read cursor tăng

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH03-DATA-CHT-P0-03
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH03-DATA-CHT-P0-02`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `docs/reference/DATA_MODEL.md`
- `docs/reference/SERVICE_OWNERSHIP.md`
- `docs/DATABASE_RULES.md`
- `docs/reference/OPERATIONS_BASELINE.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Chạy constraint/race/permission/query-plan tests và đối soát fixture.
2. Ghi bằng chứng restore/rebuild, backfill resume, metadata/object consistency khi liên quan.

## Tiêu chí chấp nhận

- **AC01**: Test chứng minh bất biến của conversation, conversation_member, message, message_reaction, notification; unique clientMessageId và read cursor tăng; không có truy vấn chéo DB.
- **AC02**: Bằng chứng migration/query/index và kế hoạch recovery được bàn giao cho Backend, không chỉ ảnh ERD.

## Kiểm chứng và bằng chứng

- Khám phá lệnh thật trong solution/package scripts/CI. Nếu chưa có, ghi blocker hoặc tạo harness đúng phạm vi; không ghi lệnh đoán là đã chạy.
- Kiểm thử mục tiêu → unit/integration/contract/architecture phù hợp → format/analyzer/build → review diff/tài liệu.
- Với planning, kiểm nguồn/decision/contract bằng validator và review thay cho giả build sản phẩm.
- Lưu lệnh, exit code, thời gian UTC, môi trường, artifact và SHA-256; ánh xạ đủ AC. Thiếu/skip một AC bắt buộc không được DONE.

## Điều kiện dừng

- Nguồn mâu thuẫn, API/data/ownership/quyền chưa khóa; dependency hoặc bằng chứng thay đổi; kiểm thử thất bại.
- Không tự thêm thư viện, chạy migration phá hủy, thay production hoặc nới điều kiện READY.
- Không commit, push, merge, tag, deploy hoặc gửi thông tin cho người khác nếu chưa có ủy quyền rõ cho thao tác đó.

## Bàn giao

Ghi `TASK_ID=PH03-DATA-CHT-P0-03`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
