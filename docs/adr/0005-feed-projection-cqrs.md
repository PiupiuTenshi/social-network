# ADR-005 - Bảng tin dùng bản chiếu theo CQRS

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Tạo bảng tin bằng cách gọi đồng bộ nhiều dịch vụ hoặc nối dữ liệu xuyên cơ sở dữ liệu gây N+1, độ trễ cao và coupling mạnh.

## Quyết định

Feed Service duy trì `FeedEntry`, `FeedPostSummary` và `FeedUserSummary` từ sự kiện của Tài khoản và Mạng xã hội. Luồng đọc dùng bản chiếu và cache cục bộ; dữ liệu có thể dựng lại từ nguồn và phần sự kiện phát sinh sau checkpoint.

## Lý do

Bản chiếu tối ưu access pattern đọc, giữ quyền sở hữu dữ liệu nguồn và cho phép xử lý tải đọc độc lập.

## Hệ quả

- Chấp nhận độ trễ nhất quán cuối cùng.
- Cần xử lý sự kiện trùng, đảo thứ tự, xóa và cập nhật phiên bản.
- Phải có quy trình rebuild, checkpoint, invalidation và đối soát.

## Ràng buộc thực thi

- Lọc quyền riêng tư và block là điều kiện bắt buộc trước khi trả kết quả.
- Bản chiếu chỉ chứa trường tối thiểu cần cho Feed.
- Feed không trở thành nguồn sự thật cho dữ liệu Social hoặc Account.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
