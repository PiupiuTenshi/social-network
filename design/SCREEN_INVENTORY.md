# Danh mục màn hình — 1.2 Final

Tổng cộng **47 màn hình đã duyệt**. Màn hình AI-03 độc lập đã bị loại; phiên âm được tích hợp vào bài viết và tin nhắn thoại.

| Mã | Màn hình | Route | Nhóm | Ưu tiên |
|---|---|---|---|---|
| AUTH-01 | Chào mừng | `/` | Xác thực | P0 |
| AUTH-02 | Đăng nhập | `/dang-nhap` | Xác thực | P0 |
| AUTH-03 | Đăng ký | `/dang-ky` | Xác thực | P0 |
| AUTH-04 | Quên mật khẩu | `/quen-mat-khau` | Xác thực | P1 |
| AUTH-05 | Đặt lại mật khẩu | `/dat-lai-mat-khau` | Xác thực | P1 |
| FEED-01 | Bảng tin | `/bang-tin` | Bảng tin | P0 |
| FEED-02 | Tạo bài viết | `/bai-viet/moi` | Bảng tin | P0 |
| FEED-03 | Chi tiết bài viết | `/bai-viet/:id` | Bảng tin | P0 |
| FEED-04 | Sửa bài viết | `/bai-viet/:id/sua` | Bảng tin | P0 |
| FEED-05 | Bài viết video đang xử lý | `/bai-viet/:id/xu-ly` | Bảng tin | P1 |
| PROF-01 | Hồ sơ của tôi | `/toi` | Hồ sơ | P0 |
| PROF-02 | Hồ sơ người dùng | `/nguoi-dung/:id` | Hồ sơ | P0 |
| PROF-03 | Chỉnh sửa hồ sơ | `/toi/chinh-sua` | Hồ sơ | P1 |
| PROF-04 | Người theo dõi và đang theo dõi | `/nguoi-dung/:id/ket-noi` | Hồ sơ | P0 |
| SET-01 | Quyền riêng tư | `/thiet-lap/quyen-rieng-tu` | Thiết lập | P0 |
| SET-02 | Bảo mật tài khoản | `/thiet-lap/bao-mat` | Thiết lập | P0 |
| SET-03 | Tài khoản đã chặn | `/thiet-lap/da-chan` | Thiết lập | P0 |
| SET-04 | Xóa tài khoản | `/thiet-lap/xoa-tai-khoan` | Thiết lập | P1 |
| DISC-01 | Tìm kiếm | `/tim-kiem` | Khám phá | P2 |
| NOTI-01 | Thông báo | `/thong-bao` | Thông báo | P0 |
| COMM-01 | Khám phá cộng đồng | `/cong-dong` | Cộng đồng | P1 |
| COMM-02 | Tổng quan cộng đồng | `/cong-dong/:id` | Cộng đồng | P1 |
| COMM-03 | Mời và tham gia cộng đồng | `/loi-moi/:code` | Cộng đồng | P1 |
| COMM-04 | Vai trò và quyền | `/cong-dong/:id/vai-tro` | Cộng đồng | P1 |
| COMM-05 | Quản lý kênh | `/cong-dong/:id/kenh` | Cộng đồng | P1 |
| COMM-06 | Điều hành thành viên | `/cong-dong/:id/thanh-vien` | Cộng đồng | P1 |
| COMM-07 | Kênh văn bản | `/cong-dong/:id/kenh/:channelId` | Cộng đồng | P1 |
| CHAT-01 | Danh sách hội thoại | `/tin-nhan` | Trò chuyện | P0 |
| CHAT-02 | Hội thoại | `/tin-nhan/:id` | Trò chuyện | P0 |
| CHAT-03 | Tạo hội thoại | `/tin-nhan/moi` | Trò chuyện | P0 |
| CHAT-04 | Thiết lập hội thoại | `/tin-nhan/:id/thiet-lap` | Trò chuyện | P0 |
| RTC-01 | Lời mời cuộc gọi | `/cuoc-goi/:id` | RTC | P1 |
| RTC-02 | Phòng thoại và video | `/cong-dong/:id/phong/:roomId` | RTC | P1 |
| RTC-03 | Chia sẻ màn hình | `/cong-dong/:id/phong/:roomId/chia-se` | RTC | P1 |
| MEDIA-01 | Tải phương tiện | `/phuong-tien/tai-len` | Phương tiện | P1 |
| MKT-01 | Chợ | `/cho` | Thương mại | P2 |
| MKT-02 | Chi tiết tin đăng | `/cho/tin/:id` | Thương mại | P2 |
| MKT-03 | Tạo hoặc sửa tin đăng | `/cho/tin/moi` | Thương mại | P2 |
| MKT-04 | Xác nhận đơn hàng | `/cho/thanh-toan` | Thương mại | P2 |
| MKT-05 | Thanh toán trực tiếp với người bán | `/cho/don/:id/thanh-toan` | Thương mại | P2 |
| MKT-06 | Đơn hàng | `/cho/don-hang` | Thương mại | P2 |
| AI-01 | Trợ lý AI | `/tro-ly` | AI | P2 |
| AI-02 | Tóm tắt hội thoại hoặc kênh | `/tro-ly/tom-tat` | AI | P2 |
| MOD-01 | Báo cáo nội dung | `hộp thoại` | Điều hành | P1 |
| MOD-02 | Hàng đợi điều hành | `/dieu-hanh/bao-cao` | Điều hành | P1 |
| MOD-03 | Chi tiết điều hành | `/dieu-hanh/bao-cao/:id` | Điều hành | P1 |
| SYS-01 | Trạng thái tải, rỗng, lỗi và ngoại tuyến | `toàn ứng dụng` | Hệ thống | P0 |
