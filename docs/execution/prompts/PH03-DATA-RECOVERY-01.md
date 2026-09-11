# PH03-DATA-RECOVERY-01 — Khôi phục P0 và rebuild Feed

## Mục tiêu và phạm vi

- Phase: PH03 | Nhóm: DATA | Ưu tiên: P0 | Task cha: PH03-DATA-RECOVERY.
- Mục tiêu duy nhất: Khôi phục P0 và rebuild Feed.
- Miền: deploy | Chức năng: nền tảng/quy trình.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH03-DATA-RECOVERY-01`; chưa được tạo chỉ vì có trong prompt.
- Bản kế hoạch không chứng minh mã ứng dụng đã tồn tại.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH03-DATA-RECOVERY-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH03-BE-FED-02-02`
- `PH03-BE-CHT-08-02`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `docs/reference/OPERATIONS_BASELINE.md`
- `docs/INCIDENT_RUNBOOK.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Backup mỗi DB, tách khỏi volume/máy chạy; restore vào môi trường riêng, kiểm checksum.
2. Rebuild Feed từ source export + checkpoint + Kafka delta; duplicate/out-of-order và thay quyền không rò dữ liệu.
3. Đo RPO/RTO và smoke Account/Post/Chat sau restart/restore.

## Tiêu chí chấp nhận

- **AC01**: RPO <=24h, RTO P0 <=4h có timestamps và dữ liệu đối soát.
- **AC02**: Rebuild không cần FK/query chéo DB, không phát email/thanh toán lặp.
- **AC03**: Kafka/Valkey/DB outage có runbook/alert và bằng chứng không mất dữ liệu commit.

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

Ghi `TASK_ID=PH03-DATA-RECOVERY-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
