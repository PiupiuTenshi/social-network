# Bắt đầu làm việc với dự án

Với kế hoạch triển khai toàn dự án, mở [execution/README.md](execution/README.md), chọn ID trong backlog Backend/Data/Frontend và làm theo [READY_GATE.md](execution/READY_GATE.md). Mỗi subtask phải có DoR và tiền nhiệm DONE trước khi bắt đầu; task kế tiếp không tự READY. [Git playbook](execution/GIT_PLAYBOOK.md) có lệnh từ khởi tạo repository đến phát hành.

## Sáu câu hỏi phải trả lời trước khi viết mã

1. Nhiệm vụ thuộc mã chức năng hoặc issue nào?
2. Dịch vụ nào sở hữu dữ liệu và bất biến?
3. Hợp đồng đầu vào/đầu ra nào bị ảnh hưởng?
4. Phân quyền, xử lý đồng thời, xử lý lặp an toàn và chế độ lỗi nào áp dụng?
5. Kiểm thử và bằng chứng nào chứng minh hoàn thành?
6. Tài liệu hoặc hợp đồng nào phải đồng bộ?

## Luồng một nhiệm vụ

```text
Ý tưởng hoặc lỗi
  -> Mô tả chức năng hoặc báo cáo lỗi
  -> Điều kiện sẵn sàng triển khai
  -> Bối cảnh tối thiểu
  -> Bộ prompt
  -> Khảo sát mã
  -> Kế hoạch
  -> Triển khai
  -> Kiểm thử và rà soát
  -> Đồng bộ tài liệu
  -> Pull request có bằng chứng
  -> Định nghĩa hoàn thành
```

## Tài liệu cần đọc theo loại việc

- Frontend/UI: `FRONTEND_START_HERE.md`, `design/design.md`, màn hình liên quan, OpenAPI/AsyncAPI và `prompts/25-uiux-to-frontend.md`.

- Chức năng: `PROJECT_CONTEXT`, `SERVICE_BOUNDARIES`, đặc tả chức năng và `TESTING_STRATEGY`.
- API: thêm `API_RULES` và `reference/API_CATALOG`.
- Kafka: thêm `EVENT_RULES`, `reference/EVENT_CATALOG` và `reference/TOPIC_CATALOG`.
- Cơ sở dữ liệu: thêm `DATABASE_RULES` và `reference/DATA_MODEL`.
- Thời gian thực/RTC: thêm `REALTIME_RULES` và `reference/SIGNALR_CATALOG`.
- Lỗi: thêm `FAILURE_HANDLING` và `prompts/12-fix-bug.md`.
- Bảo mật: thêm `SECURITY_RULES` và mô hình đe dọa.
- Phát hành: thêm `RELEASE_CHECKLIST`, `reference/OPERATIONS_BASELINE`, `GIT_FLOW` và `GIT_COMMANDS`.
- Dùng prompt lần đầu: đọc `PROMPT_USAGE_EXAMPLES`.
- Chạy nhiều trợ lý hoặc nhiều worktree: đọc `PARALLEL_AGENT_WORKFLOW` trước khi tách việc.

Ánh xạ đầy đủ nằm trong `.ai/context-map.yaml`. Các đường dẫn trong danh sách trên đều nằm trong thư mục `docs/`, trừ khi đã ghi rõ thư mục khác.
