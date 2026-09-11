# PH03-BE-SOC-07-01 — Triển khai SOC-07: Bình luận và trả lời

## Mục tiêu và phạm vi

- Phase: PH03 | Nhóm: BE | Ưu tiên: P0 | Task cha: PH03-BE-SOC-07.
- Mục tiêu duy nhất: Triển khai SOC-07: Bình luận và trả lời.
- Miền: social | Chức năng: SOC-07.
- Chế độ: implementation. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.
- Nhánh đề xuất: `feat/PH03-BE-SOC-07-01`; chưa được tạo chỉ vì có trong prompt.
- Owner: Mạng xã hội. Hợp đồng tham chiếu: POST /posts/{id}/comments. Dữ liệu: comment. Sự kiện: CommentCreated.

## Cổng bắt buộc trước khi thực hiện

```powershell
python -X utf8 scripts/task_gate.py check PH03-BE-SOC-07-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }
```

Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.
READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.

## Phụ thuộc phải DONE có bằng chứng

- `PH03-DATA-SOC-P0-03`
- `PH01-BE-PLATFORM-01`
- `PH01-BE-CI-01`
- `PH03-BE-SOC-06-02`
- `PH02-GATE-ACCOUNT-01`

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

1. Theo hợp đồng đã khóa: Tạo bình luận hoặc trả lời và ghi Outbox CommentCreated.
2. Thực thi: Parent cùng bài; độ sâu; rate limit.
3. Khảo sát src/Services/Social, tests và hợp đồng thực tế; bổ sung log/metric/trace, cancellation, test ngay cùng mã.

## Tiêu chí chấp nhận

- **AC01**: Given điều kiện trước của SOC-07, when thực hiện hợp lệ, then Tạo bình luận hoặc trả lời và ghi Outbox CommentCreated.
- **AC02**: Kiểm soát được chứng minh: Parent cùng bài; độ sâu; rate limit.
- **AC03**: Ca tối thiểu chạy thật: Parent sai; private/blocked.

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

Ghi `TASK_ID=PH03-BE-SOC-07-01`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.
Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.
