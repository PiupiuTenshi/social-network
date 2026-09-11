# Danh mục prompt

Đã có [318 prompt theo subtask ID](../docs/execution/README.md) cho kế hoạch toàn dự án. Với ID đã đăng ký, dùng `python -X utf8 scripts/task_gate.py prompt ID` để lấy prompt sau kiểm READY; `--preview` chỉ xem. Prompt chung dưới đây hỗ trợ chuẩn bị bối cảnh và không cấp quyền bỏ qua dependencies.

Mỗi prompt dùng cấu trúc: bối cảnh -> vai trò -> hành động -> yêu cầu -> đầu ra -> kiểm chứng. Trước khi dùng, thay `{{...}}` bằng dữ liệu nhiệm vụ hoặc giữ rõ `CHƯA XÁC MINH`; không tự bịa phiên bản, đường dẫn, lệnh hoặc hành vi.

Trình tự thông thường:

1. `$build-project-prompts.md` hoặc `00-master-orchestrator.md`.
2. `03-feature-spec-to-plan.md` để chia việc.
3. Prompt triển khai chuyên biệt từ `04` đến `10`, `13` hoặc `17`.
4. `11-generate-tests.md` để bổ sung kiểm thử, hoặc `23-test-evidence-review.md` cho nhiệm vụ chỉ đọc.
5. `14-code-review.md` và prompt rủi ro chuyên biệt khi cần.
6. `19-documentation-sync.md`.
7. `22-pr-review.md`.

Lỗi dùng `12-fix-bug.md`; sự cố vận hành dùng `20-incident-debug.md`; thay đổi hợp đồng liên dịch vụ dùng `21-contract-change.md`.

`23-test-evidence-review.md` dùng khi chỉ cần đánh giá độ phủ và bằng chứng kiểm thử mà không chỉnh mã.
## UI/UX và Frontend

- `24-uiux-review.md`: rà soát bản thiết kế, contract, state, responsive và accessibility.
- `25-uiux-to-frontend.md`: triển khai màn hình từ `design/design.md` đã khóa.
