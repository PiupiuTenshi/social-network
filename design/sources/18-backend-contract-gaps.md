# Khoảng trống hợp đồng phát sinh từ vòng duyệt 2

Các mục dưới đây là yêu cầu UI/UX mới, chưa mặc nhiên được backend v3.0 hỗ trợ. Cần ADR hoặc cập nhật đặc tả trước khi triển khai.

## Tài khoản và hồ sơ

- Biệt danh, ảnh bìa, tâm trạng, bài hát Spotify, thông tin chi tiết hồ sơ và cửa hàng người bán.
- Số điện thoại bắt buộc khi sửa hồ sơ; khả năng tìm bằng email/số điện thoại.
- Đăng xuất một thiết bị bằng OTP và danh sách phiên nhiều thiết bị.
- Lý do chặn; cảnh báo khi gặp người đã chặn trong cộng đồng chung.
- Dùng lại email trong thời gian chờ xóa và quy tắc hòa giải giữa tài khoản mới/cũ.

## Bài viết, video và thông báo

- Định dạng rich text, font/kích thước/đậm nhạt, phạm vi hiển thị tùy chỉnh.
- Lưu bài viết, repost, bộ lọc/pagination bình luận, reaction/reply/report bình luận.
- Chọn thumbnail từ ảnh hoặc frame; bản nháp; lên lịch đăng; dashboard lượt xem/thích/chia sẻ.
- Tab đề cập và mute/unmute thông báo nhanh.

## Cộng đồng và trò chuyện

- Taxonomy “tường”, “không quan tâm”, cài đặt ưu tiên/hạn chế cộng đồng.
- Form chấp thuận quy tắc, duyệt thành viên, danh sách cấm và quyền theo vai trò.
- Tin nhắn ghim, chủ đề chat, danh hiệu trong nhóm, rời trong im lặng.
- Upload tệp chat, nội dung đang gửi/thử lại, phân vùng media/file/friend detail.

## RTC

- Mở cửa sổ/app riêng, mã phòng, lựa chọn layout và thiết bị mic/camera/loa.
- Chat riêng/toàn phòng, video bản thân và quy trình xin phép ghi hình.

## Marketplace

- Phân loại/variant sản phẩm.
- Bỏ payment provider khỏi UX; hiển thị QR/số tiền người bán và liên hệ trực tiếp.
- Trạng thái hủy không có hoàn trả trong ứng dụng.

## AI

- Trợ lý thu nhỏ nổi, hỏi lại khi yêu cầu thiếu.
- Tóm tắt tối đa 10.000 dòng và xuất PDF.
- Loại route AI-03; hiển thị phiên âm trực tiếp dưới video hoặc tin nhắn thoại.
