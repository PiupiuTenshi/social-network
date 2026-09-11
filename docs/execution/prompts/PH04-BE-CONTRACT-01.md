# PH04-BE-CONTRACT-01 — Khóa bổ sung hợp đồng P1

## Mục tiêu và phạm vi

- Phase: PH04 | Nhóm: BE | Ưu tiên: P1 | Task cha: PH04-BE-CONTRACT.
- Mục tiêu duy nhất: Khóa bổ sung hợp đồng P1.
- Miền: cross-cutting | Chức năng: nền tảng/quy trình.
- Chế độ: planning. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `docs/PH04-BE-CONTRACT-01`; chưa được tạo chỉ vì có trong prompt.
- Bản kế hoạch không chứng minh mã ứng dụng đã tồn tại.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH04-BE-CONTRACT-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `G1-01`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `docs/reference/API_CATALOG.md`
- `docs/reference/SECURITY_THREAT_MODEL.md`
- `design/sources/18-backend-contract-gaps.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Giải quyết BL-07/08/09/10 và API đọc P1: OTP, deletion/cancel/ack, video status, moderation/reopen, permission revocation/RTC.
2. Khóa API/schema/ERD P1 và cập nhật test contract; mỗi gap UI nâng cao có quyết định dùng baseline hoặc mở rộng.

## Tiêu chí chấp nhận

- **AC01**: Không còn API/trạng thái/owner chưa rõ trong P1 đã chọn; các quyết định có bằng chứng chấp thuận.
- **AC02**: P2 consumer chưa triển khai không gây deadlock deletion; xác định danh sách participant theo release và quy trình backfill khi bật sau.

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

Ghi `TASK_ID=PH04-BE-CONTRACT-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
