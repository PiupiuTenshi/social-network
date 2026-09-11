# Kế hoạch thực thi Twight Light

Đây là điểm vào cho yêu cầu **phase → backend/data/frontend → task → subtask → prompt theo ID/mục tiêu → cổng READY → Git flow**. Kế hoạch dựa trên thiết kế v3.0, ADR, tài liệu quy tắc và UI/UX 1.2 Final; không thay thế các nguồn đó.

## Trạng thái bàn giao ngày 07/09/2026

- Có **9 phase, 158 task, 318 subtask**, mỗi subtask một prompt riêng.
- Bao phủ **66 mã chức năng** và **47 màn hình**; màn hình có nhiều mức ưu tiên được chia thành các lát cắt P0/P1/P2.
- Kho ban đầu là bộ tài liệu, chưa có solution .NET, ứng dụng Angular, OpenAPI/AsyncAPI triển khai, migration sản phẩm hoặc `.git`.
- **Chưa có subtask sản phẩm nào được READY/DONE, chưa có G0–G4 đạt.** Tạo kế hoạch không đồng nghĩa đã triển khai dự án.
- Các quyết định còn thiếu có trong [BLOCKERS.md](BLOCKERS.md). Thứ tự ưu tiên của ADR-010 được giữ: G1 trước P1; G2 trước P2.

## Đọc theo nhu cầu

| Tài liệu | Nội dung |
|---|---|
| [ROADMAP.md](ROADMAP.md) | Mục tiêu phase, ba luồng BE/DATA/FE, đầu vào/đầu ra, thứ tự và kế hoạch 24 tuần |
| [BACKEND.md](BACKEND.md) | Task/subtask theo 8 dịch vụ, Gateway, BuildingBlocks, hợp đồng và tích hợp |
| [DATA.md](DATA.md) | Ownership, lược đồ, migration/fixture, constraint/race, projection, retention và khôi phục |
| [FRONTEND.md](FRONTEND.md) | App shell và từng lát cắt của 47 màn hình; route, quyền, integration và QA |
| [PROMPT_ORDER.md](PROMPT_ORDER.md) | Thứ tự đọc/thực hiện đề nghị của toàn bộ 318 prompt, nhóm theo các đợt dependency |
| [GOVERNANCE.md](GOVERNANCE.md) | Khảo sát, gia cố, bằng chứng và bàn giao |
| [QUALITY_GATES.md](QUALITY_GATES.md) | Nhiệm vụ nghiệm thu G0–G4 và kiểm Account trước Mạng xã hội |
| [TRACEABILITY.md](TRACEABILITY.md) | Ánh xạ function ID ↔ task ↔ screen; tránh nhầm ID UI và Backend |
| [READY_GATE.md](READY_GATE.md) | State machine, lệnh theo ID, mẫu bằng chứng, điều kiện dừng và phục hồi task |
| [GIT_PLAYBOOK.md](GIT_PLAYBOOK.md) | Từ khởi tạo Git đến branch, commit, push, PR, merge, tag, hotfix và rollback |
| [DOCUMENT_AUDIT.md](DOCUMENT_AUDIT.md) | Phạm vi đọc/đối chiếu, baseline và giới hạn kiểm tra |
| [VALIDATION_REPORT.md](VALIDATION_REPORT.md) | Lệnh đã chạy và kết quả kiểm chứng công cụ/kế hoạch |
| [BLOCKERS.md](BLOCKERS.md) | Các mâu thuẫn/chỗ trống cần giải quyết trước mã liên quan |
| [plan.json](plan.json) | Danh mục máy đọc được: mục tiêu, actions, acceptance, dependencies, sources, hashes |
| [state.json](state.json) | Trạng thái thực thi và lịch sử chuyển trạng thái; không sửa tay để vượt cổng |

## Bắt đầu bằng một ID

Chạy tại thư mục gốc bằng PowerShell. `-X utf8` tránh lỗi tiếng Việt trên Windows.

```powershell
python -X utf8 scripts/task_gate.py next
python -X utf8 scripts/task_gate.py check PH00-GOV-AUDIT-01
```

Lệnh `check` ban đầu trả `NOT_READY` vì chưa có hồ sơ DoR. Xem mục tiêu mà không cấp quyền chạy:

```powershell
python -X utf8 scripts/task_gate.py prompt PH00-GOV-AUDIT-01 --preview
```

Chuẩn bị hồ sơ theo [READY_GATE.md](READY_GATE.md). Prompt đầu tiên: [PH00-GOV-AUDIT-01](prompts/PH00-GOV-AUDIT-01.md). Việc đầu tiên là xác nhận nguồn, đường vào quy tắc, phạm vi và cơ chế duyệt; **chưa viết nghiệp vụ**.

Khi đã có bằng chứng READY:

```powershell
python -X utf8 scripts/task_gate.py check PH00-GOV-AUDIT-01
if ($LASTEXITCODE -ne 0) { throw 'NOT_READY' }
python -X utf8 scripts/task_gate.py start PH00-GOV-AUDIT-01
if ($LASTEXITCODE -ne 0) { throw 'Không thể bắt đầu' }
python -X utf8 scripts/task_gate.py prompt PH00-GOV-AUDIT-01
```

Có thể giao trợ lý câu sau, đổi đúng ID:

```text
Thực hiện subtask PH00-GOV-AUDIT-01 theo docs/execution/plan.json.
Đọc prompt tương ứng và chạy task_gate.py check trước khi làm.
Nếu chưa READY, chỉ nêu blocker và chuẩn bị phần bằng chứng trong phạm vi được phép;
không tự ghi PASS, không triển khai task sau. Nếu READY, start đúng ID, thực hiện
mục tiêu/acceptance và bàn giao bằng chứng thật. Không tự commit/push/tag/deploy.
```

## Cập nhật kế hoạch

Gate/bộ sinh chỉ cần Python chuẩn (đã kiểm trên Python 3.11.9). Riêng `validate_all.py` còn chạy validator UI/UX, cần các dependency đã khai báo trong `design/requirements.txt`. Khi máy chưa có, chuẩn bị môi trường riêng rồi dùng interpreter đó; không coi thiếu thư viện là kiểm tra đã đạt:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r design/requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Chưa cài đủ dependency kiểm thiết kế' }
.\.venv\Scripts\python.exe -X utf8 scripts/validate_all.py
```

Trong lần bàn giao này, Pillow được cài riêng vào `work/document-audit/python-deps` và truyền `PYTHONPATH` cho tiến trình kiểm chứng; không đổi Python toàn máy. Chi tiết môi trường nằm trong VALIDATION_REPORT.

Nguồn sinh nằm trong [build_execution_plan.py](../../scripts/build_execution_plan.py); dữ liệu nghiệp vụ được đọc từ FUNCTION_SPECIFICATIONS/TRACEABILITY_MATRIX và screen inventory/spec. Quyết định phân chia/phụ thuộc nằm trong bộ sinh để tái tạo nhất quán.

```powershell
python -X utf8 scripts/build_execution_plan.py --check
python -X utf8 scripts/task_gate.py validate
python -X utf8 scripts/test_task_gate.py
python -X utf8 scripts/validate_all.py
```

Khi đổi nguồn/phạm vi: ghi quyết định, sửa bộ sinh có review, chạy không có `--check` để sinh lại, rà soát diff và bằng chứng bị STALE. Bộ sinh **không ghi đè state/evidence**. Không renumber ID đã dùng; nếu phải thay task, tạo ID mới và ghi liên kết thay thế.

Đồng bộ MANIFEST/checksums bằng `python -X utf8 scripts/refresh_kit_inventory.py` sau thay đổi tệp. Công cụ này chỉ cập nhật danh mục/hash, không chứng minh tài liệu đúng nghiệp vụ hoặc test đã đạt.
