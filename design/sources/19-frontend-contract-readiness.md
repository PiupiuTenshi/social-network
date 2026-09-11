# 19. Trạng thái sẵn sàng hợp đồng cho Frontend

Tài liệu UI/UX mô tả trải nghiệm đích, nhưng không tự tạo hợp đồng Backend. Khi triển khai, phân loại mỗi khả năng theo ba trạng thái dưới đây.

## Sẵn sàng triển khai theo hợp đồng v3.0

- Đăng ký, đăng nhập, refresh token, đăng xuất, hồ sơ cơ sở và quyền riêng tư.
- Theo dõi, chặn, bài viết cơ sở, bình luận, tương tác, chia sẻ và bảng tin.
- Cộng đồng, kênh, vai trò, quyền, trò chuyện, thông báo và RTC cơ sở.
- Tải phương tiện, xử lý video cơ sở, báo cáo vi phạm và hàng đợi điều hành.
- Luồng thương mại và AI chỉ được bật theo mức ưu tiên/feature flag đã định nghĩa.

## Chỉ triển khai giao diện có cờ tính năng hoặc dữ liệu giả ở môi trường phát triển

Các khả năng trong `18-backend-contract-gaps.md` có thể được dựng component và trạng thái giao diện, nhưng không được nối vào API tự suy đoán. Mỗi khả năng phải có:

1. Feature flag mặc định tắt ngoài môi trường phát triển.
2. Kiểu dữ liệu tạm đặt trong adapter/mock riêng, không trộn vào domain contract đã khóa.
3. Nhãn `contract-gap` trong issue hoặc pull request.
4. Quyết định ADR/OpenAPI/AsyncAPI trước khi bật trong bản phát hành.

## Bị chặn cho đến khi hợp đồng được cập nhật

- Đăng xuất từng thiết bị bằng OTP.
- Rich text đầy đủ, lưu/repost bài viết và điều hành bình luận nâng cao.
- Draft/lịch đăng/dashboard video nếu Backend chưa có job và endpoint tương ứng.
- Duyệt thành viên, ghim/chủ đề chat và upload file chat nâng cao.
- QR thanh toán trực tiếp với người bán khi mô hình Commerce hiện tại chưa được đổi bằng ADR.
- Xuất PDF/tóm tắt 10.000 dòng nếu chưa có giới hạn, job và cơ chế tải kết quả.

## Quy tắc dừng

Khi mockup, `design.md` và OpenAPI/AsyncAPI không khớp, dừng tại adapter. Không sửa tên field, status code, quyền hoặc hành vi Backend trong Frontend để “làm cho chạy”. Ghi khoảng trống vào `18-backend-contract-gaps.md` và mở nhiệm vụ hợp đồng riêng.
