# PH03-FE-NOTI-01-P0-01 — Triển khai NOTI-01 P0: Thông báo

## Mục tiêu và phạm vi

- Phase: PH03 | Nhóm: FE | Ưu tiên: P0 | Task cha: PH03-FE-NOTI-01-P0.
- Mục tiêu duy nhất: Triển khai NOTI-01 P0: Thông báo.
- Miền: cross-cutting | Chức năng: CHT-08.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH03-FE-NOTI-01-P0-01`; chưa được tạo chỉ vì có trong prompt.
- Route: /thong-bao. Vai trò: Người dùng. Chỉ bật CHT-08 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH03-FE-NOTI-01-P0-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH01-FE-FOUNDATION-02`
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
- `design/screens/notifications/noti-01-thong-bao.md`
- `design/design.md`
- `design/tokens/design-tokens.json`
- `design/sources/11-state-matrix.md`
- `design/sources/18-backend-contract-gaps.md`
- `design/sources/19-frontend-contract-readiness.md`
- `docs/UIUX_WORKFLOW.md`
- `docs/reference/API_CATALOG.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Mục tiêu screen: Hiển thị hộp thông báo theo con trỏ, đánh dấu đã đọc và điều hướng đến đối tượng liên quan.
2. Đối chiếu tất cả hành động/API đọc với OpenAPI thực tế, ghi capability matrix baseline/gap/tắt; không suy ra endpoint từ route.
3. Tạo route/component/state/adapter/tests cho capability trong phạm vi; giữ desktop/mobile, token và accessibility.

## Tiêu chí chấp nhận

- **AC01**: Màn hình NOTI-01 tại /thong-bao thực hiện đúng quyền Người dùng và capability CHT-08.
- **AC02**: Trạng thái riêng được kiểm chứng: - Có thông báo mới; - Rỗng; - Đang tải; - Ngoại tuyến; - Đối tượng đích đã bị xóa; ; Ngoài các trạng thái trên, áp dụng trạng thái dùng chung trong `sources/11-state-matrix.md`.
- **AC03**: Loading/empty/error/401/403/404/409/412/422/429/503, offline/reconnect liên quan đều có đường xử lý; giữ dữ liệu khi retry.
- **AC04**: Tất cả hành động thiếu hợp đồng có quyết định hoặc bị tắt đúng policy; không có mock/API bịa trên đường release.

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

Ghi `TASK_ID=PH03-FE-NOTI-01-P0-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
