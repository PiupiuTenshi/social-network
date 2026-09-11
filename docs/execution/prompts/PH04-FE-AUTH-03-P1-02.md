# PH04-FE-AUTH-03-P1-02 — QA AUTH-03 P1 trên Desktop/Mobile

## Mục tiêu và phạm vi

- Phase: PH04 | Nhóm: FE | Ưu tiên: P1 | Task cha: PH04-FE-AUTH-03-P1.
- Mục tiêu duy nhất: QA AUTH-03 P1 trên Desktop/Mobile.
- Miền: cross-cutting | Chức năng: ACC-10.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH04-FE-AUTH-03-P1-02`; chưa được tạo chỉ vì có trong prompt.
- Route: /dang-ky. Vai trò: Khách. Chỉ bật ACC-10 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH04-FE-AUTH-03-P1-02
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH04-FE-AUTH-03-P1-01`

## Nguồn phải đọc

- `AGENTS.md`
- `RULES.md`
- `docs/START_HERE.md`
- `.ai/context-map.yaml`
- `docs/PROJECT_CONTEXT.md`
- `docs/SERVICE_BOUNDARIES.md`
- `docs/DEFINITION_OF_READY.md`
- `docs/DEFINITION_OF_DONE.md`
- `design/screens/auth/auth-03-dang-ky.md`
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

1. Kiểm E2E luồng chính/lỗi/quyền/retry với Backend thật; đọc mục tiêu, hành động, component và AC UI trong screen.
2. Đối chiếu SVG/PNG tại 320/390/768/1024/1440 px; keyboard, focus, screen reader, 200% zoom/reflow, contrast/reduced motion.
3. Chạy lint/type/build/test và bàn giao ảnh, video hoặc report; không gọi screen complete nếu capability bắt buộc còn thiếu.

## Tiêu chí chấp nhận

- **AC01**: AUTH-03 P1 có mapping design → code/test, ảnh Desktop/Mobile và sai khác có lý do.
- **AC02**: E2E thật qua auth, quyền, state và duplicate/reconnect phù hợp; không lộ dữ liệu hoặc side effect trùng.
- **AC03**: Touch target >=44x44; focus/name/contrast AA đạt; mọi check bắt buộc có artifact và kết quả thật.

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

Ghi `TASK_ID=PH04-FE-AUTH-03-P1-02`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
