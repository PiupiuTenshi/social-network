# Quy trình lập trình với trợ lý AI

## Mục tiêu

Trợ lý AI hỗ trợ khảo sát, triển khai và rà soát dựa trên bằng chứng; không phải nguồn sự thật. Mỗi kết quả phải đủ để người hoặc trợ lý khác tiếp tục mà không cần toàn bộ lịch sử trò chuyện.

## Quy trình tám bước

1. **Chuẩn hóa đầu vào** bằng `FEATURE_BRIEF`, `BUG_REPORT` hoặc `PROMPT_INPUT`.
2. **Chốt hợp đồng nhiệm vụ:** một kết quả chính, lý do nghiệp vụ, phạm vi, tiêu chí chấp nhận và rủi ro.
3. **Ghép bối cảnh tối thiểu** bằng `scripts/build_context.py`.
4. **Sinh bộ prompt** bằng `$build-project-prompts` hoặc `scripts/generate_prompt_pack.py`.
5. **Chạy prompt khảo sát/kế hoạch** trước prompt triển khai.
6. **Triển khai và kiểm thử theo từng công việc nhỏ;** dùng bản bàn giao gần nhất làm đầu vào cho bước sau.
7. **Chạy prompt rà soát chuyên biệt** về mã, bảo mật hoặc hiệu năng khi có rủi ro tương ứng.
8. **Đồng bộ tài liệu và mở pull request** kèm bằng chứng.

Ví dụ lệnh cho chức năng, lỗi, API, Kafka và nhiệm vụ chỉ đọc nằm trong [`PROMPT_USAGE_EXAMPLES.md`](PROMPT_USAGE_EXAMPLES.md). Khi tách việc cho nhiều trợ lý, bắt buộc áp dụng [`PARALLEL_AGENT_WORKFLOW.md`](PARALLEL_AGENT_WORKFLOW.md).

## Không làm

- Dán toàn bộ kho mã vào một prompt.
- Yêu cầu “làm hết dự án” trong một prompt.
- Chấp nhận mã không có kiểm thử hoặc không có kết quả lệnh thật.
- Để trợ lý tự chọn ownership, API hoặc lược đồ khi nguồn sự thật chưa rõ.
- Cho phép tự commit, push hoặc deploy chỉ vì mã đã được sinh.

## Bàn giao chuẩn

Dùng `templates/IMPLEMENTATION_REPORT.md`. Công việc tiếp theo chỉ cần bối cảnh dự án ổn định, hợp đồng nhiệm vụ và bản bàn giao gần nhất.
