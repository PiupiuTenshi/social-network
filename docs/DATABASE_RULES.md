# Quy tắc dữ liệu và di trú cơ sở dữ liệu

## Quyền sở hữu

- Mỗi dịch vụ có cơ sở dữ liệu logic riêng.
- Không truy vấn, ghi hoặc tạo khóa ngoại xuyên dịch vụ.
- Định danh ngoài chỉ là UUID hoặc tham chiếu; không suy ra sự tồn tại hoặc quyền nếu chưa kiểm tra qua hợp đồng hoặc bản chiếu.

## Lược đồ

- Ràng buộc unique bảo vệ các bất biến như theo dõi, chặn, phản ứng, `clientMessageId` và khóa xử lý lặp.
- Chỉ mục phải gắn với mẫu truy cập và được kiểm chứng bằng kế hoạch truy vấn hoặc metric.
- Aggregate có khả năng tranh chấp dùng cột `version` cho optimistic concurrency.
- Xóa mềm phải có bộ lọc và chỉ mục phù hợp, đồng thời không làm lộ dữ liệu đã ẩn.

## Di trú an toàn

1. Mở rộng lược đồ theo cách tương thích.
2. Deploy mã đọc được cả cấu trúc cũ và mới.
3. Backfill theo lô, có checkpoint, metric và khả năng tiếp tục.
4. Chuyển đọc/ghi bằng cờ chức năng hoặc triển khai có kiểm soát.
5. Chỉ thu hẹp sau ít nhất một chu kỳ phát hành và có bằng chứng không còn bên sử dụng cũ.

Không chạy di trú phá hủy nếu chưa có sao lưu, đánh giá tương thích và phương án quay lui hoặc tiến tới.

## EF Core

- Di trú thuộc đúng dịch vụ sở hữu.
- Không để nhiều bản sao tự chạy di trú lúc khởi động.
- Truy vấn đọc dùng projection và `AsNoTracking` khi phù hợp.
- Giao dịch ngắn; không giữ khóa qua lời gọi mạng.
- Chiến lược thử lại phải kết hợp xử lý lặp an toàn để không nhân đôi tác dụng phụ.

Xem `docs/reference/DATA_MODEL.md`.
