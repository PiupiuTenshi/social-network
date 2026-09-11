# PH06-BE-MKT-06-01 — Triển khai MKT-06: Trạng thái đơn hàng và Saga đơn giản hóa

## Mục tiêu và phạm vi

- Phase: PH06 | Nhóm: BE | Ưu tiên: P2 | Task cha: PH06-BE-MKT-06.
- Mục tiêu duy nhất: Triển khai MKT-06: Trạng thái đơn hàng và Saga đơn giản hóa.
- Miền: commerce | Chức năng: MKT-06.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH06-BE-MKT-06-01`; chưa được tạo chỉ vì có trong prompt.
- Owner: Thương mại. Hợp đồng tham chiếu: State transition/cancel. Dữ liệu: order, status_history. Sự kiện: OrderStatusChanged.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH06-BE-MKT-06-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH06-DATA-MKT-P2-03`
- `PH01-BE-PLATFORM-01`
- `PH01-BE-CI-01`
- `PH06-BE-MKT-04-02`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `docs/reference/FUNCTION_SPECIFICATIONS.md`
- `docs/reference/TRACEABILITY_MATRIX.md`
- `docs/reference/API_CATALOG.md`
- `docs/reference/EVENT_CATALOG.md`
- `docs/reference/DATA_MODEL.md`
- `docs/TESTING_STRATEGY.md`
- `docs/SECURITY_RULES.md`
- `docs/REALTIME_RULES.md`
- `docs/reference/SIGNALR_CATALOG.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Theo hợp đồng đã khóa: Áp dụng máy trạng thái: Pending, AwaitingPayment, Paid, Processing, Completed và Cancelled.
2. Thực thi: Transition whitelist; compensation.
3. Khảo sát src/Services/Commerce, tests và hợp đồng thực tế; bổ sung log/metric/trace, cancellation, test ngay cùng mã.

## Tiêu chí chấp nhận

- **AC01**: Given điều kiện trước của MKT-06, when thực hiện hợp lệ, then Áp dụng máy trạng thái: Pending, AwaitingPayment, Paid, Processing, Completed và Cancelled.
- **AC02**: Kiểm soát được chứng minh: Transition whitelist; compensation.
- **AC03**: Ca tối thiểu chạy thật: Invalid transition; release once.

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

Ghi `TASK_ID=PH06-BE-MKT-06-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
