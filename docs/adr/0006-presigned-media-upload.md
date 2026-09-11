# ADR-006 - Tải phương tiện trực tiếp bằng URL ký trước

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Chuyển file qua API backend làm tăng băng thông, bộ nhớ và rủi ro quá tải của dịch vụ ứng dụng.

## Quyết định

Media Service tạo `UploadSession`, object key do máy chủ sinh và URL ký trước có TTL ngắn. Client PUT trực tiếp lên SeaweedFS. Bước hoàn tất dùng HEAD/stat để xác minh object, sau đó worker kiểm tra magic bytes và xử lý media.

## Lý do

Cách này giảm tải backend, giữ kiểm soát metadata và vẫn cho phép xác minh tệp trước khi công bố.

## Hệ quả

- Cần dọn session hết hạn và object mồ côi.
- Trạng thái upload và xử lý media là bất đồng bộ.
- Client phải xử lý hết hạn URL và gọi complete lặp an toàn.

## Ràng buộc thực thi

- Không tin MIME, kích thước hoặc trạng thái thành công do client tự khai.
- Object key không do client tùy ý chọn.
- Bucket không public; truy cập tải xuống nhạy cảm cũng dùng URL ký trước.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
