# Quy tắc API

## Hợp đồng chung

- Đường dẫn cơ sở: `/api/v1`.
- DTO giao thức tách khỏi entity và mô hình miền.
- JSON dùng `camelCase`; định danh ưu tiên UUIDv7; thời gian dùng UTC ISO 8601.
- Lỗi dùng Problem Details, có `traceId`, mã lỗi ổn định và lỗi theo trường khi phù hợp.
- Không trả stack trace, SQL, secret, token hoặc chi tiết xác thực nhạy cảm.

## Mã trạng thái

- `200`: đọc hoặc cập nhật thành công.
- `201`: tạo thành công, có `Location`.
- `202`: tác vụ bất đồng bộ đã được nhận, có `requestId` hoặc `jobId`.
- `204`: thành công và không có nội dung trả về.
- `400`: yêu cầu không phân tích được hoặc sai định dạng giao thức.
- `401`: chưa xác thực hoặc token không hợp lệ.
- `403`: đã xác thực nhưng không đủ quyền.
- `404`: tài nguyên không tồn tại hoặc được cố ý ẩn để tránh lộ thông tin.
- `409`: xung đột nghiệp vụ hoặc dùng lại khóa lặp với nội dung khác.
- `412`: `If-Match` không còn khớp phiên bản.
- `422`: dữ liệu hợp lệ về định dạng nhưng vi phạm quy tắc nghiệp vụ.
- `429`: vượt giới hạn; trả `Retry-After` khi có thể.
- `503`: phụ thuộc tạm thời không sẵn sàng và không thể suy giảm an toàn.

## Xử lý đồng thời và lặp an toàn

- Aggregate có `version` trả `ETag`.
- Cập nhật hoặc xóa gửi `If-Match`; câu lệnh cơ sở dữ liệu phải kèm điều kiện phiên bản.
- `Idempotency-Key` được lưu cùng băm nội dung yêu cầu và phản hồi trong thời gian sống quy định.
- Cùng khóa và cùng nội dung trả phản hồi cũ; cùng khóa nhưng nội dung khác trả `409`.

## Phân trang

- Cursor do máy chủ tạo, Base64URL và không để máy khách suy diễn nội dung.
- Mặc định 20, tối đa 50 trừ khi hợp đồng quy định khác.
- Thứ tự phải ổn định và có khóa phụ `id`.
- Không dùng offset trên đường nóng của Bảng tin hoặc lịch sử tin nhắn khi hợp đồng đã dùng cursor.

## Kiểm thử hợp đồng

Mọi điểm cuối thay đổi phải cập nhật OpenAPI, ví dụ và kiểm thử hợp đồng. Danh mục chuẩn nằm trong `docs/reference/API_CATALOG.md`.
