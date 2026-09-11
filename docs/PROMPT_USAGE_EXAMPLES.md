# Ví dụ sử dụng bộ prompt

Các ví dụ dưới đây chỉ minh họa cách tạo bộ prompt. Trước khi triển khai mã, vẫn phải khảo sát kho mã và thay nội dung `CHƯA XÁC MINH` bằng bằng chứng thật.

## 1. Chức năng Backend .NET

```bash
python scripts/generate_prompt_pack.py \
  --task-id ACC-01-register \
  --task-type backend-feature \
  --domain account \
  --function-id ACC-01 \
  --description "Triển khai đăng ký tài khoản và phát UserRegistered" \
  --evidence "Thiết kế ACC-01, API catalog và data model" \
  --constraints "Không thay đổi đường dẫn /api/v1/auth/register" \
  --acceptance-criteria "Given email và username chưa tồn tại, when đăng ký hợp lệ, then tạo Account/Profile/Outbox trong một giao dịch và không trả password hash."
```

Thực hiện theo thứ tự các tệp được sinh:

1. `02-plan.md`
2. `03-implementation-prompt.md`
3. `04-test-prompt.md`
4. `05-review-prompt.md`
5. `06-docs-sync-prompt.md`
6. `07-handoff-template.md`

## 2. Sửa lỗi

```bash
python scripts/generate_prompt_pack.py \
  --task-id BUG-CHT-duplicate-message \
  --task-type bug-fix \
  --domain chat \
  --function-id CHT-02 \
  --description "Điều tra tin nhắn bị tạo trùng khi máy khách gửi lại sau mất kết nối" \
  --evidence "Hai Message có cùng conversationId, senderId và clientMessageId" \
  --constraints "Không thay đổi hợp đồng MessageCreated" \
  --acceptance-criteria "Cùng clientMessageId chỉ tạo một Message và trả lại kết quả đã có."
```

Prompt sửa lỗi bắt buộc tách triệu chứng, vị trí biểu hiện, nguyên nhân gốc và yếu tố góp phần. Không chấp nhận bản vá chỉ thêm `catch`, kiểm tra `null` hoặc thử lại để che triệu chứng.

## 3. Thay đổi API

```bash
python scripts/generate_prompt_pack.py \
  --task-id API-SOC-04-etag \
  --task-type api \
  --domain social \
  --function-id SOC-04 \
  --description "Bổ sung ETag và If-Match cho chỉnh sửa bài viết" \
  --evidence "Post có version và tài liệu yêu cầu trả 412 khi phiên bản cũ" \
  --constraints "Giữ tương thích phản hồi thành công hiện tại" \
  --acceptance-criteria "If-Match khớp thì cập nhật và tăng version; không khớp trả Problem Details 412."
```

## 4. Sự kiện Kafka

```bash
python scripts/generate_prompt_pack.py \
  --task-id EVT-SOC-post-created \
  --task-type kafka \
  --domain social \
  --function-id SOC-03 \
  --description "Triển khai PostCreated v1 qua Transactional Outbox" \
  --evidence "Event catalog quy định key PostId; Feed và AI/Search là bên nhận" \
  --constraints "Không phát sự kiện trước khi giao dịch tạo bài viết commit" \
  --acceptance-criteria "Kafka gián đoạn không làm mất PostCreated; phát lặp cùng eventId không tạo FeedEntry trùng."
```

## 5. Nhiệm vụ chỉ rà soát

```bash
python scripts/generate_prompt_pack.py \
  --task-id REVIEW-PR-142 \
  --task-type pr-review \
  --domain cross-cutting \
  --function-id CHT-02 \
  --description "Rà soát pull request 142 trước khi hợp nhất" \
  --evidence "Issue, diff và kết quả CI của pull request" \
  --constraints "Chỉ đọc; không sửa tệp hoặc thay đổi trạng thái pull request" \
  --acceptance-criteria "Mọi tiêu chí có trạng thái Đạt, Không đạt hoặc Chưa xác minh và mọi lỗi chặn có bằng chứng."
```

Với nhiệm vụ chỉ đọc, `04-test-prompt.md` sẽ dùng prompt rà soát bằng chứng kiểm thử thay vì yêu cầu chỉnh mã kiểm thử.

## 6. Tạo lại bộ prompt

Bộ sinh không ghi đè thư mục đã có. Chỉ dùng `--force` khi đã lưu hoặc không còn cần bản bàn giao cũ:

```bash
python scripts/generate_prompt_pack.py \
  --task-id ACC-01-register \
  --task-type backend-feature \
  --domain account \
  --function-id ACC-01 \
  --description "Triển khai đăng ký tài khoản" \
  --force
```

## 7. Nhúng nội dung tài liệu

Mặc định `01-context.md` chỉ chứa bản đồ tệp để tránh ngữ cảnh dài và lỗi thời. Chỉ nhúng khi agent không thể đọc trực tiếp kho mã:

```bash
python scripts/generate_prompt_pack.py \
  --task-id ACC-01-register \
  --task-type backend-feature \
  --domain account \
  --function-id ACC-01 \
  --description "Triển khai đăng ký tài khoản" \
  --embed-context \
  --max-context-chars 60000
```
