# Twight Light — Bộ tài liệu Vibe Coding và Frontend Design

Bộ này kết hợp **Thiết kế hệ thống chi tiết v3.0**, quy tắc/prompt Vibe Coding và **UI/UX 1.2 Final** để triển khai Backend .NET, hạ tầng và Frontend theo cùng một nguồn truy vết.

## Bắt đầu nhanh

Kế hoạch triển khai chi tiết nằm tại [docs/execution/README.md](docs/execution/README.md): **9 phase, 158 task, 318 subtask và prompt theo ID**, chia Backend/Data/Frontend, có cổng READY và Git playbook. Dùng điểm vào này để chọn công việc; sinh prompt chung không thay thế kiểm tra READY.

1. Đọc `AGENTS.md` và `RULES.md`.
2. Đọc `docs/START_HERE.md` cho luồng phát triển chung.
3. Với Frontend, đọc `FRONTEND_START_HERE.md` rồi `design.md`.
4. Với Backend, dùng `docs/reference/`, OpenAPI/AsyncAPI thực tế và prompt phù hợp trong `prompts/`.
5. Không triển khai tính năng được đánh dấu `contract-gap` trước khi hợp đồng được duyệt.

## Thành phần

- `design.md`: tài liệu UI/UX cuối, bản tiện dụng ở thư mục gốc.
- `design/`: 47 màn hình Desktop/Mobile, SVG/PNG, token, nguồn Markdown và gallery độc lập.
- `docs/`: kiến trúc, ranh giới dịch vụ, Git flow, kiểm thử, bảo mật, vận hành và danh mục tham chiếu.
- `prompts/`: prompt theo chức năng, lỗi, API, cơ sở dữ liệu, Kafka, SignalR, LiveKit, CI/CD và UI/UX.
- `templates/`: biểu mẫu ADR, task, bug, API/event contract, PR và bằng chứng kiểm thử.
- `scripts/`: sinh prompt, kiểm tra tài liệu và đồng bộ thiết kế.
- `source-documents/`: DOCX/PDF thiết kế hệ thống v3.0 dùng để truy vết.

## Sinh bộ prompt

```bash
python scripts/generate_prompt_pack.py \
  --task-id ACC-01-register \
  --task-type backend-feature \
  --domain account \
  --function-id ACC-01 \
  --description "Triển khai đăng ký tài khoản theo ACC-01"
```

## Kiểm tra toàn bộ

```bash
python scripts/validate_vibe_kit.py
python scripts/validate_all.py
```

## Nguồn sự thật

1. ADR mới hơn đã được chấp thuận.
2. Thiết kế hệ thống v3.0 và `docs/reference/`.
3. OpenAPI/AsyncAPI/schema/migration trong kho mã.
4. `design/design.md` cho UI/UX đã khóa.
5. Kiểm thử chấp nhận và mã nguồn hiện tại.

Khi các nguồn mâu thuẫn về hợp đồng, dữ liệu, bảo mật hoặc kiến trúc, dừng và tạo nhiệm vụ làm rõ/ADR; không tự sửa một phía.
