# Chiến lược kiểm thử

## Các cấp độ

- **Đơn vị:** bất biến, chuyển trạng thái, xác thực dữ liệu và chính sách thuần.
- **Tích hợp:** API, cơ sở dữ liệu, giao dịch và adapter container.
- **Hợp đồng:** OpenAPI, lược đồ sự kiện và tính tương thích.
- **Kiến trúc:** hướng phụ thuộc, không truy vấn chéo, API không dùng `DbContext` trực tiếp.
- **Xuyên suốt:** các luồng nghiệm thu chọn lọc.
- **Tải, lỗi và bảo mật:** theo NFR và danh mục rủi ro.

## Trường hợp bắt buộc

### API và chức năng

Luồng thành công, dữ liệu sai, chưa xác thực, không đủ quyền, không tìm thấy hoặc được ẩn, xung đột, hủy yêu cầu và lỗi phụ thuộc.

### Xử lý đồng thời và lặp an toàn

- `ETag` cũ;
- yêu cầu HTTP lặp;
- sự kiện Kafka lặp;
- hai người mua tranh chấp một đơn vị tồn kho;
- `clientMessageId` lặp;
- tiến trình chết sau khi Kafka đã nhận nhưng trước khi Outbox được đánh dấu.

### Nhất quán cuối

Dùng polling có giới hạn thời gian và tín hiệu quan sát được. Không dùng thời gian chờ cố định dài để che tính không xác định.

### Sửa lỗi

Tạo kiểm thử hồi quy thất bại trước bản sửa khi thực tế cho phép; chứng minh nguyên nhân gốc thay vì chỉ kiểm tra vị trí ném exception.

## Thứ tự chạy

1. Kiểm thử mới hoặc kiểm thử mục tiêu.
2. Bộ kiểm thử của module hoặc dịch vụ liên quan.
3. Định dạng, analyzer và biên dịch.
4. Kiểm thử tích hợp, hợp đồng và kiến trúc liên quan.
5. Bộ kiểm thử rộng hơn trước pull request hoặc hợp nhất.

Không ghi “đạt” cho lệnh chưa chạy. Lưu bằng chứng theo `templates/TEST_EVIDENCE.md`.
