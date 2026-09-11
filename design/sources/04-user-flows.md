# 04. Luồng người dùng

Các sơ đồ chỉnh sửa được nằm trong `assets/editable/flows/`.

## Luồng P0

- Đăng ký -> đăng nhập -> bảng tin.
- Tạo bài viết -> Outbox -> xuất hiện trên bảng tin.
- Theo dõi/chặn -> cập nhật UI và bản chiếu.
- Tạo hội thoại -> gửi tin -> nhận realtime -> đánh dấu đã đọc.
- Mở thông báo -> điều hướng đến tài nguyên hợp lệ.

## Luồng P1

- Quên mật khẩu -> OTP -> đặt lại -> thu hồi phiên.
- Tạo cộng đồng -> vai trò/kênh mặc định -> mời/tham gia.
- Tải phương tiện -> xác minh -> xử lý -> gắn vào bài/tin nhắn.
- Tham gia phòng -> cấp token -> LiveKit -> fallback TURN.
- Báo cáo -> hàng đợi -> hành động -> đóng/audit.
- Yêu cầu xóa tài khoản -> ân hạn -> hủy hoặc hoàn tất.

## Luồng P2

- Duyệt tin đăng -> tạo đơn -> giữ tồn kho -> thanh toán giả lập -> theo dõi trạng thái.
- Hỏi AI -> truy xuất theo quyền -> stream -> mở nguồn.
- Tóm tắt/phiên âm -> job -> kết quả hoặc fallback.
