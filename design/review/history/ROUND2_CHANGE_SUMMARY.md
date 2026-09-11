# Tổng kết thay đổi UI/UX — Vòng 2

## Kết quả

- Dựng lại **47 màn hình Desktop** theo phản hồi vòng 1.
- Tái cấu trúc **47 màn hình Mobile** dựa trên Desktop, không thu nhỏ nguyên xi.
- Giữ toàn bộ nguồn chỉnh sửa ở SVG và đặc tả Markdown.
- Loại màn hình độc lập `AI-03`; đưa phiên âm vào `FEED-03` và `CHAT-02`.
- Đổi trải nghiệm thanh toán của `MKT-05` thành hướng dẫn thanh toán trực tiếp với người bán.

## Nhóm thay đổi

### Xác thực

- Đổi thương hiệu, slogan và nội dung marketing.
- Thay mảng màu tĩnh bằng mạng nhân vật dạng vector chuyển động theo đặc tả.
- Bổ sung toast thành công/thất bại, xác nhận trường hợp lệ và quy trình đặt lại mật khẩu sau khi OTP hợp lệ.

### Khung ứng dụng và bảng tin

- Avatar góc phải mở menu tài khoản.
- Tab chính đặt trên đầu; thanh bên trái dành cho lối tắt có thể tùy biến.
- Ô đăng bài bám dính khi cuộn.
- Hành động tương tác, lưu, chia sẻ, báo cáo, toàn màn hình và bình luận được tổ chức lại.
- Chi tiết bài viết hiển thị ở lớp nổi; video xử lý nền và hiển thị lý do thất bại.

### Hồ sơ, thiết lập và khám phá

- Bổ sung biệt danh, tâm trạng, nhạc hồ sơ, cửa hàng và thông tin chi tiết.
- Thiết kế lại quyền riêng tư, bảo mật, danh sách chặn và xóa tài khoản.
- Tìm kiếm ưu tiên quan hệ đã theo dõi và phân biệt loại kết quả.
- Thông báo có tab đề cập, xem chi tiết, dẫn tới nội dung và điều khiển tắt/bật nhanh.

### Cộng đồng và trò chuyện

- Bổ sung danh mục cộng đồng, không quan tâm, mời/chia sẻ, quy tắc tham gia và số thành viên.
- Tách quyền chủ sở hữu, điều phối viên, thành viên và khách.
- Bổ sung duyệt thành viên, cấm thành viên, chỉ báo hiện diện, reply/reaction/report, tệp đính kèm, gửi lại và tin nhắn ghim.

### RTC và phương tiện

- RTC mở trong cửa sổ riêng, có lựa chọn layout, thiết bị, mã phòng, mời người tham gia và chat bên cạnh.
- Bổ sung xem trước camera bản thân, điều khiển mic/loa và đồng ý ghi hình.
- Phương tiện hỗ trợ thumbnail, bản nháp, lịch đăng và số liệu cơ bản.

### Marketplace, AI và điều hành

- Marketplace có phân loại/biến thể sản phẩm, liên hệ người bán, QR/số tiền và phân trang.
- Trợ lý AI có thể thu nhỏ, hỏi lại khi thiếu dữ liệu; tóm tắt giới hạn 10.000 dòng và hỗ trợ xuất PDF ở mức thiết kế.
- Hàng đợi điều hành có phân trang; màn hình chi tiết tập trung bằng chứng, hành động và lý do.

## Khoảng trống hợp đồng

Những yêu cầu mới cần Backend, dữ liệu hoặc hợp đồng mới được tập trung tại `sources/18-backend-contract-gaps.md`. Chúng không được xem là đã có API chỉ vì đã xuất hiện trong mockup.
