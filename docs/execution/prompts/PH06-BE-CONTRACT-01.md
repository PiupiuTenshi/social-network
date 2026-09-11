# PH06-BE-CONTRACT-01 — Quyết định phạm vi và hợp đồng P2

## Mục tiêu và phạm vi

- Phase: PH06 | Nhóm: BE | Ưu tiên: P2 | Task cha: PH06-BE-CONTRACT.
- Mục tiêu duy nhất: Quyết định phạm vi và hợp đồng P2.
- Miền: cross-cutting | Chức năng: nền tảng/quy trình.
- Chế độ: planning. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `docs/PH06-BE-CONTRACT-01`; chưa được tạo chỉ vì có trong prompt.
- Bản kế hoạch không chứng minh mã ứng dụng đã tồn tại.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH06-BE-CONTRACT-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `G2-01`

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
- `design/sources/18-backend-contract-gaps.md`
- `docs/reference/NFR.md`
- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.
- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.

## Các bước trong subtask

1. Giải quyết BL-11/12: mock payment đối lập seller QR, variants, job AI/PDF, tài nguyên và model.
2. Chốt từng năng lực P2 nhận triển khai; OpenSearch optional mặc định tắt; không đổi nguồn thanh toán khi chưa ADR.
3. Khóa nguồn export/RAG ACL, cancellation, invalidation/deletion và NFR/cost từng khả năng.

## Tiêu chí chấp nhận

- **AC01**: Danh sách P2 đưa vào release và phần hoãn được chủ dự án quyết định; cập nhật kế hoạch trước thực thi nếu cắt.
- **AC02**: OpenAPI/AsyncAPI/data model và UI thống nhất; không nối UI QR vào MockPaymentProvider.
- **AC03**: Từng P2 có giới hạn tài nguyên, fallback và test không làm hỏng P0/P1.

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

Ghi `TASK_ID=PH06-BE-CONTRACT-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
