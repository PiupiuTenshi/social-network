# Danh mục topic và vận hành sự kiện

## Topic cơ sở

| Topic | Khóa | Phân vùng | Lưu giữ | Nhóm sự kiện |
| --- | --- | --- | --- | --- |
| account.user.v1 | UserId/AccountId | 3 | 7 ngày | Đăng ký, hồ sơ, mật khẩu, xóa tài khoản |
| social.relationship.v1 | ActorId | 3 | 7 ngày | Theo dõi, chặn |
| social.post.v1 | PostId | 6 | 7 ngày | Bài viết, bình luận, tương tác, chia sẻ |
| social.moderation.v1 | ReportId/TargetId | 3 | 30 ngày | Báo cáo và hành động điều hành |
| community.lifecycle.v1 | CommunityId | 3 | 7 ngày | Cộng đồng, thành viên, vai trò, kênh |
| chat.message.v1 | ConversationId | 6 | 7 ngày | Hội thoại và tin nhắn |
| media.asset.v1 | MediaId | 3 | 7 ngày | Tải lên, xử lý, xóa phương tiện |
| commerce.order.v1 | OrderId | 3 | 14 ngày | Đơn hàng, thanh toán và trạng thái |
| commerce.listing.v1 | ListingId | 3 | 7 ngày | Tin đăng và tồn kho |
| ai.job.v1 | EntityId/RequestId | 3 | 7 ngày | Embedding, tóm tắt, transcript |

## Retry và DLQ

| Loại lỗi | Xử lý | Khoảng chờ | Quy tắc |
| --- | --- | --- | --- |
| Lỗi tạm thời ngắn | Thử lại cục bộ tối đa 3 lần | 200 ms, 500 ms, 1 giây có jitter | Không commit offset trước khi giao dịch thành công. |
| Lỗi phụ thuộc kéo dài | Chuyển sang topic retry | .retry.1m -> .retry.10m -> .retry.1h | Giữ eventId/correlationId; giới hạn tổng thời gian 24 giờ. |
| Lỗi dữ liệu/schema vĩnh viễn | Không thử lại vô hạn | Chuyển .dlq ngay hoặc sau số lần hữu hạn | Lưu reason, stack đã làm sạch, consumer, offset và schema version. |
| Lỗi nghiệp vụ dự kiến | Đánh dấu rejected | Không xem là lỗi hạ tầng | Phát sự kiện kết quả khi luồng cần biết; không gây vòng lặp retry. |
| Phát lại DLQ | Dùng công cụ quản trị được bảo vệ | Dry-run -> batch nhỏ -> theo dõi metric | Bắt buộc audit; không phát lại trực tiếp vào hệ thống khi chưa sửa nguyên nhân. |

## Phiên bản, thứ tự và replay

| Chủ đề | Quy tắc bắt buộc |
| --- | --- |
| Tương thích cùng phiên bản lớn | Chỉ thêm trường tùy chọn; không đổi ý nghĩa, kiểu hoặc xóa trường bắt buộc; consumer phải bỏ qua trường chưa biết. |
| Thay đổi phá vỡ | Tăng major trong topic/schema; chạy song song producer/consumer trong thời gian chuyển đổi và có kế hoạch kết thúc phiên bản cũ. |
| Thứ tự | Chỉ cam kết trong một partition; chọn partition key theo aggregate và so sánh aggregateVersion khi có thể nhận sự kiện cũ. |
| Kích thước | Event <= 256 KB; không chứa tệp, transcript dài hoặc dữ liệu nhạy cảm không cần thiết; dùng object/reference. |
| Phát lại | Consumer group riêng; bắt đầu từ checkpoint; giới hạn tốc độ; luôn dùng Inbox; tác dụng phụ ngoài như email/thanh toán bị tắt trừ khi bật rõ ràng. |
| Outbox không chắc chắn | Nếu Kafka đã nhận nhưng worker chết trước khi cập nhật published_at, cùng eventId sẽ được phát lại và consumer phải bỏ qua tác dụng phụ trùng. |
| Schema registry | Lưu JSON Schema/Protobuf contract trong kho mã; CI kiểm tra tương thích và sinh AsyncAPI. Registry dịch vụ bên ngoài là tùy chọn. |
