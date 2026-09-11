# PH04-FE-SET-02-P1-01 — Triển khai SET-02 P1: Bảo mật tài khoản

## Mục tiêu và phạm vi

- Phase: PH04 | Nhóm: FE | Ưu tiên: P1 | Task cha: PH04-FE-SET-02-P1.
- Mục tiêu duy nhất: Triển khai SET-02 P1: Bảo mật tài khoản.
- Miền: cross-cutting | Chức năng: ACC-09, ACC-08.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH04-FE-SET-02-P1-01`; chưa được tạo chỉ vì có trong prompt.
- Route: /thiet-lap/bao-mat. Vai trò: Người dùng. Chỉ bật ACC-09, ACC-08 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH04-FE-SET-02-P1-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH01-FE-FOUNDATION-02`
- `PH04-BE-ACC-09-02`
- `PH04-BE-ACC-08-02`
- `G1-01`
- `PH04-BE-CONTRACT-01`
- `PH03-FE-SET-02-P0-02`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `design/screens/settings/set-02-bao-mat-tai-khoan.md`
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

1. Mục tiêu screen: Đổi mật khẩu, đăng xuất phiên hiện tại hoặc mọi phiên và xem thông tin bảo mật cơ bản.
2. Đối chiếu tất cả hành động/API đọc với OpenAPI thực tế, ghi capability matrix baseline/gap/tắt; không suy ra endpoint từ route.
3. Tạo route/component/state/adapter/tests cho capability trong phạm vi; giữ desktop/mobile, token và accessibility.

## Tiêu chí chấp nhận

- **AC01**: Màn hình SET-02 tại /thiet-lap/bao-mat thực hiện đúng quyền Người dùng và capability ACC-09, ACC-08.
- **AC02**: Trạng thái riêng được kiểm chứng: - Mặc định; - Đang xử lý; - Xác thực lại; - Thành công; - Thất bại; ; Ngoài các trạng thái trên, áp dụng trạng thái dùng chung trong `sources/11-state-matrix.md`.
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

Ghi `TASK_ID=PH04-FE-SET-02-P1-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
