# ADR-004 - Tách mặt phẳng SignalR và LiveKit

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Thông điệp ứng dụng thời gian thực và gói media có yêu cầu vận chuyển, độ trễ, băng thông và khả năng khôi phục khác nhau.

## Quyết định

SignalR vận chuyển thông điệp ứng dụng như tin nhắn, trạng thái gõ, hiện diện, thông báo và token AI. LiveKit cùng coturn vận chuyển âm thanh, video và chia sẻ màn hình. Kafka chỉ mang metadata hoặc sự kiện vòng đời, không mang gói media.

## Lý do

Tách hai mặt phẳng giúp mỗi công nghệ xử lý đúng loại tải và bảo đảm trò chuyện văn bản vẫn hoạt động khi RTC gặp lỗi.

## Hệ quả

- Phải vận hành, quan sát và kiểm thử hai mặt phẳng riêng.
- Client cần xử lý kết nối lại SignalR và vòng đời phòng LiveKit độc lập.
- RTC có thể suy giảm mà không làm hỏng luồng chat bền vững.

## Ràng buộc thực thi

- Community kiểm tra thành viên và quyền trước khi cấp token LiveKit.
- Token RTC ngắn hạn và chỉ chứa capability cần thiết.
- Không đưa media bytes qua SignalR, Kafka hoặc API backend.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
