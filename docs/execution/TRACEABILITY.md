# Truy vết chức năng và màn hình

ID chức năng và ID màn hình là hai namespace khác nhau. AI-03 chức năng RAG vẫn thuộc phạm vi; màn hình AI-03 riêng đã bị loại.

| Chức năng | Ưu tiên | Task Backend | Task Frontend |
|---|---|---|---|
| ACC-01 — Đăng ký | P0 | PH02-BE-ACC-01 | PH02-FE-AUTH-01-P0, PH02-FE-AUTH-03-P0 |
| ACC-02 — Đăng nhập | P0 | PH02-BE-ACC-02 | PH02-FE-AUTH-01-P0, PH02-FE-AUTH-02-P0 |
| ACC-03 — Xoay vòng refresh token | P0 | PH02-BE-ACC-03 | PH02-FE-AUTH-02-P0, PH03-FE-SET-02-P0 |
| ACC-04 — Đăng xuất | P0 | PH02-BE-ACC-04 | PH03-FE-SET-02-P0 |
| ACC-05 — Xem và cập nhật hồ sơ | P0 | PH02-BE-ACC-05 | PH03-FE-PROF-01-P0, PH03-FE-PROF-02-P0, PH04-FE-PROF-03-P1 |
| ACC-06 — Cập nhật tham chiếu avatar | P1 | PH04-BE-ACC-06 | PH04-FE-PROF-03-P1 |
| ACC-07 — Quyền riêng tư và thiết lập tài khoản | P0 | PH02-BE-ACC-07 | PH03-FE-SET-01-P0 |
| ACC-08 — Yêu cầu OTP khôi phục mật khẩu | P1 | PH04-BE-ACC-08 | PH04-FE-AUTH-02-P1, PH04-FE-AUTH-04-P1, PH04-FE-SET-02-P1 |
| ACC-09 — Đặt lại mật khẩu bằng OTP | P1 | PH04-BE-ACC-09 | PH04-FE-AUTH-05-P1, PH04-FE-SET-02-P1 |
| ACC-10 — Đăng nhập bằng Google OAuth | P1 | PH04-BE-ACC-10 | PH04-FE-AUTH-02-P1, PH04-FE-AUTH-03-P1 |
| SOC-01 — Theo dõi và bỏ theo dõi | P0 | PH03-BE-SOC-01 | PH03-FE-PROF-02-P0, PH03-FE-PROF-04-P0 |
| SOC-02 — Chặn và bỏ chặn | P0 | PH03-BE-SOC-02 | PH03-FE-PROF-02-P0, PH03-FE-PROF-04-P0, PH03-FE-SET-03-P0 |
| SOC-03 — Tạo bài viết | P0 | PH03-BE-SOC-03 | PH03-FE-FEED-01-P0, PH03-FE-FEED-02-P0 |
| SOC-04 — Sửa bài viết | P0 | PH03-BE-SOC-04 | PH03-FE-FEED-03-P0, PH03-FE-FEED-04-P0 |
| SOC-05 — Xóa bài viết | P0 | PH03-BE-SOC-05 | PH03-FE-FEED-03-P0 |
| SOC-06 — Xem bài viết và danh sách bài viết | P0 | PH03-BE-SOC-06 | PH03-FE-FEED-03-P0, PH03-FE-PROF-01-P0, PH03-FE-PROF-02-P0, PH06-FE-DISC-01-P2 |
| SOC-07 — Bình luận và trả lời | P0 | PH03-BE-SOC-07 | PH03-FE-FEED-03-P0 |
| SOC-08 — Tương tác | P0 | PH03-BE-SOC-08 | PH03-FE-FEED-01-P0, PH03-FE-FEED-03-P0 |
| SOC-09 — Tạo bài viết video | P1 | PH04-BE-SOC-09 | PH04-FE-FEED-05-P1 |
| SOC-10 — Chia sẻ bài viết ra nền tảng ngoài | P1 | PH04-BE-SOC-10 | PH04-FE-FEED-01-P1, PH04-FE-FEED-03-P1 |
| COM-01 — Tạo và cập nhật cộng đồng | P1 | PH04-BE-COM-01 | PH04-FE-COMM-01-P1, PH04-FE-COMM-02-P1 |
| COM-02 — Mời, tham gia và rời cộng đồng | P1 | PH04-BE-COM-02 | PH04-FE-COMM-01-P1, PH04-FE-COMM-02-P1, PH04-FE-COMM-03-P1 |
| COM-03 — Vai trò và quyền | P1 | PH04-BE-COM-03 | PH04-FE-COMM-04-P1 |
| COM-04 — Tạo kênh văn bản hoặc kênh thoại | P1 | PH04-BE-COM-04 | PH04-FE-COMM-02-P1, PH04-FE-COMM-05-P1, PH04-FE-COMM-07-P1 |
| COM-05 — Điều hành thành viên | P1 | PH04-BE-COM-05 | PH04-FE-COMM-06-P1 |
| RTC-01 — Cấp token tham gia LiveKit | P1 | PH04-BE-RTC-01 | PH04-FE-RTC-01-P1, PH04-FE-RTC-02-P1 |
| RTC-02 — Thoại, video và chia sẻ màn hình | P1 | PH04-BE-RTC-02 | PH04-FE-RTC-02-P1 |
| RTC-03 — Phát trực tiếp màn hình trong phòng | P1 | PH04-BE-RTC-03 | PH04-FE-RTC-03-P1 |
| CHT-01 — Tạo hội thoại trực tiếp hoặc nhóm | P0 | PH03-BE-CHT-01 | PH03-FE-PROF-02-P0, PH03-FE-CHAT-01-P0, PH03-FE-CHAT-03-P0, PH03-FE-CHAT-04-P0, PH06-FE-MKT-02-P2 |
| CHT-02 — Gửi tin nhắn | P0 | PH03-BE-CHT-02 | PH04-FE-COMM-07-P1, PH03-FE-CHAT-02-P0 |
| CHT-03 — Sửa và xóa tin nhắn | P0 | PH03-BE-CHT-03 | PH03-FE-CHAT-02-P0, PH03-FE-CHAT-04-P0 |
| CHT-04 — Tương tác với tin nhắn | P0 | PH03-BE-CHT-04 | PH03-FE-CHAT-02-P0 |
| CHT-05 — Trạng thái đang nhập | P0 | PH03-BE-CHT-05 | PH03-FE-CHAT-02-P0 |
| CHT-06 — Trạng thái hiện diện | P0 | PH03-BE-CHT-06 | PH03-FE-CHAT-02-P0 |
| CHT-07 — Xác nhận đã đọc | P0 | PH03-BE-CHT-07 | PH04-FE-COMM-07-P1, PH03-FE-CHAT-02-P0 |
| CHT-08 — Hộp thông báo | P0 | PH03-BE-CHT-08 | PH03-FE-FEED-01-P0, PH03-FE-NOTI-01-P0, PH03-FE-CHAT-01-P0 |
| CHT-09 — Lời mời cuộc gọi | P1 | PH04-BE-CHT-09 | PH04-FE-CHAT-02-P1, PH04-FE-RTC-01-P1 |
| FED-01 — Xây dựng bản chiếu bảng tin theo dõi | P0 | PH03-BE-FED-01 | Worker/API; không có màn hình riêng |
| FED-02 — Đọc bảng tin bằng con trỏ | P0 | PH03-BE-FED-02 | PH03-FE-FEED-01-P0 |
| FED-03 — Cập nhật bản chiếu và làm mất hiệu lực bộ nhớ đệm | P0 | PH03-BE-FED-03 | Worker/API; không có màn hình riêng |
| FED-04 — Sinh ứng viên và chấm điểm gợi ý | P2 | PH06-BE-FED-04 | PH06-FE-FEED-01-P2 |
| FED-05 — Cập nhật embedding sở thích | P2 | PH06-BE-FED-05 | Worker/API; không có màn hình riêng |
| MED-01 — Tạo phiên tải lên | P1 | PH04-BE-MED-01 | PH04-FE-FEED-02-P1, PH04-FE-PROF-03-P1, PH04-FE-MEDIA-01-P1 |
| MED-02 — Tải trực tiếp | P1 | PH04-BE-MED-02 | PH04-FE-MEDIA-01-P1 |
| MED-03 — Hoàn tất và xác minh tải lên | P1 | PH04-BE-MED-03 | PH04-FE-FEED-02-P1, PH04-FE-MEDIA-01-P1 |
| MED-04 — Xử lý phương tiện | P1 | PH04-BE-MED-04 | PH04-FE-FEED-05-P1, PH04-FE-MEDIA-01-P1 |
| MED-05 — Xóa và dọn dẹp phương tiện | P1 | PH04-BE-MED-05 | Worker/API; không có màn hình riêng |
| MED-06 — Phương tiện cho tin nhắn thoại | P1 | PH04-BE-MED-06 | PH04-FE-CHAT-02-P1 |
| MKT-01 — Tạo và sửa tin đăng | P2 | PH06-BE-MKT-01 | PH06-FE-MKT-03-P2 |
| MKT-02 — Duyệt và tìm kiếm tin đăng | P2 | PH06-BE-MKT-02 | PH06-FE-DISC-01-P2, PH06-FE-MKT-01-P2, PH06-FE-MKT-02-P2 |
| MKT-03 — Cập nhật và giữ tồn kho | P2 | PH06-BE-MKT-03 | PH06-FE-MKT-03-P2, PH06-FE-MKT-04-P2 |
| MKT-04 — Tạo đơn hàng | P2 | PH06-BE-MKT-04 | PH06-FE-MKT-02-P2, PH06-FE-MKT-04-P2, PH06-FE-MKT-06-P2 |
| MKT-05 — Thanh toán giả lập | P2 | PH06-BE-MKT-05 | PH06-FE-MKT-05-P2, PH06-FE-MKT-06-P2 |
| MKT-06 — Trạng thái đơn hàng và Saga đơn giản hóa | P2 | PH06-BE-MKT-06 | PH06-FE-MKT-06-P2 |
| MKT-07 — Phương tiện của tin đăng | P2 | PH06-BE-MKT-07 | PH06-FE-MKT-02-P2, PH06-FE-MKT-03-P2 |
| AI-01 — Tạo embedding | P2 | PH06-BE-AI-01 | Worker/API; không có màn hình riêng |
| AI-02 — Tìm kiếm ngữ nghĩa | P2 | PH06-BE-AI-02 | PH06-FE-DISC-01-P2 |
| AI-03 — Trợ lý RAG | P2 | PH06-BE-AI-03 | PH06-FE-AI-01-P2 |
| AI-04 — Tóm tắt tin nhắn hoặc kênh | P2 | PH06-BE-AI-04 | PH06-FE-AI-02-P2 |
| AI-05 — Chuyển lời nói thành văn bản | P2 | PH06-BE-AI-05 | PH06-FE-FEED-03-P2, PH06-FE-CHAT-02-P2 |
| AI-06 — Đánh chỉ mục OpenSearch - tùy chọn | P2 | PH06-BE-AI-06 | Worker/API; không có màn hình riêng |
| ACC-11 — Yêu cầu xóa và khôi phục tài khoản | P1 | PH05-BE-ACC-11 | PH05-FE-SET-04-P1 |
| MOD-01 — Gửi báo cáo vi phạm | P1 | PH05-BE-MOD-01 | PH04-FE-FEED-01-P1, PH04-FE-FEED-03-P1, PH05-FE-MOD-01-P1 |
| MOD-02 — Duyệt hàng đợi báo cáo | P1 | PH05-BE-MOD-02 | PH05-FE-MOD-02-P1 |
| MOD-03 — Áp dụng hành động điều hành | P1 | PH05-BE-MOD-03 | PH05-FE-MOD-03-P1 |
| MOD-04 — Đóng báo cáo và kiểm toán | P1 | PH05-BE-MOD-04 | PH05-FE-MOD-03-P1 |

## 47 màn hình và các lát cắt ưu tiên

| Màn hình | Ưu tiên lát cắt | Task | Chức năng |
|---|---|---|---|
| AUTH-01 | P0 | PH02-FE-AUTH-01-P0 | ACC-01, ACC-02 |
| AUTH-02 | P0 | PH02-FE-AUTH-02-P0 | ACC-02, ACC-03 |
| AUTH-02 | P1 | PH04-FE-AUTH-02-P1 | ACC-10, ACC-08 |
| AUTH-03 | P0 | PH02-FE-AUTH-03-P0 | ACC-01 |
| AUTH-03 | P1 | PH04-FE-AUTH-03-P1 | ACC-10 |
| AUTH-04 | P1 | PH04-FE-AUTH-04-P1 | ACC-08 |
| AUTH-05 | P1 | PH04-FE-AUTH-05-P1 | ACC-09 |
| FEED-01 | P0 | PH03-FE-FEED-01-P0 | FED-02, SOC-03, SOC-08, CHT-08 |
| FEED-01 | P1 | PH04-FE-FEED-01-P1 | SOC-10, MOD-01 |
| FEED-01 | P2 | PH06-FE-FEED-01-P2 | FED-04 |
| FEED-02 | P0 | PH03-FE-FEED-02-P0 | SOC-03 |
| FEED-02 | P1 | PH04-FE-FEED-02-P1 | MED-01, MED-03 |
| FEED-03 | P0 | PH03-FE-FEED-03-P0 | SOC-06, SOC-07, SOC-08, SOC-04, SOC-05 |
| FEED-03 | P1 | PH04-FE-FEED-03-P1 | SOC-10, MOD-01 |
| FEED-03 | P2 | PH06-FE-FEED-03-P2 | AI-05 |
| FEED-04 | P0 | PH03-FE-FEED-04-P0 | SOC-04 |
| FEED-05 | P1 | PH04-FE-FEED-05-P1 | SOC-09, MED-04 |
| PROF-01 | P0 | PH03-FE-PROF-01-P0 | ACC-05, SOC-06 |
| PROF-02 | P0 | PH03-FE-PROF-02-P0 | ACC-05, SOC-01, SOC-02, SOC-06, CHT-01 |
| PROF-03 | P1 | PH04-FE-PROF-03-P1 | ACC-05, ACC-06, MED-01 |
| PROF-04 | P0 | PH03-FE-PROF-04-P0 | SOC-01, SOC-02 |
| SET-01 | P0 | PH03-FE-SET-01-P0 | ACC-07 |
| SET-02 | P0 | PH03-FE-SET-02-P0 | ACC-03, ACC-04 |
| SET-02 | P1 | PH04-FE-SET-02-P1 | ACC-09, ACC-08 |
| SET-03 | P0 | PH03-FE-SET-03-P0 | SOC-02 |
| SET-04 | P1 | PH05-FE-SET-04-P1 | ACC-11 |
| DISC-01 | P2 | PH06-FE-DISC-01-P2 | AI-02, MKT-02, SOC-06 |
| NOTI-01 | P0 | PH03-FE-NOTI-01-P0 | CHT-08 |
| COMM-01 | P1 | PH04-FE-COMM-01-P1 | COM-01, COM-02 |
| COMM-02 | P1 | PH04-FE-COMM-02-P1 | COM-01, COM-02, COM-04 |
| COMM-03 | P1 | PH04-FE-COMM-03-P1 | COM-02 |
| COMM-04 | P1 | PH04-FE-COMM-04-P1 | COM-03 |
| COMM-05 | P1 | PH04-FE-COMM-05-P1 | COM-04 |
| COMM-06 | P1 | PH04-FE-COMM-06-P1 | COM-05 |
| COMM-07 | P1 | PH04-FE-COMM-07-P1 | COM-04, CHT-02, CHT-07 |
| CHAT-01 | P0 | PH03-FE-CHAT-01-P0 | CHT-01, CHT-08 |
| CHAT-02 | P0 | PH03-FE-CHAT-02-P0 | CHT-02, CHT-03, CHT-04, CHT-05, CHT-06, CHT-07 |
| CHAT-02 | P1 | PH04-FE-CHAT-02-P1 | MED-06, CHT-09 |
| CHAT-02 | P2 | PH06-FE-CHAT-02-P2 | AI-05 |
| CHAT-03 | P0 | PH03-FE-CHAT-03-P0 | CHT-01 |
| CHAT-04 | P0 | PH03-FE-CHAT-04-P0 | CHT-01, CHT-03 |
| RTC-01 | P1 | PH04-FE-RTC-01-P1 | CHT-09, RTC-01 |
| RTC-02 | P1 | PH04-FE-RTC-02-P1 | RTC-01, RTC-02 |
| RTC-03 | P1 | PH04-FE-RTC-03-P1 | RTC-03 |
| MEDIA-01 | P1 | PH04-FE-MEDIA-01-P1 | MED-01, MED-02, MED-03, MED-04 |
| MKT-01 | P2 | PH06-FE-MKT-01-P2 | MKT-02 |
| MKT-02 | P2 | PH06-FE-MKT-02-P2 | MKT-02, MKT-07, MKT-04, CHT-01 |
| MKT-03 | P2 | PH06-FE-MKT-03-P2 | MKT-01, MKT-03, MKT-07 |
| MKT-04 | P2 | PH06-FE-MKT-04-P2 | MKT-03, MKT-04 |
| MKT-05 | P2 | PH06-FE-MKT-05-P2 | MKT-05 |
| MKT-06 | P2 | PH06-FE-MKT-06-P2 | MKT-06, MKT-04, MKT-05 |
| AI-01 | P2 | PH06-FE-AI-01-P2 | AI-03 |
| AI-02 | P2 | PH06-FE-AI-02-P2 | AI-04 |
| MOD-01 | P1 | PH05-FE-MOD-01-P1 | MOD-01 |
| MOD-02 | P1 | PH05-FE-MOD-02-P1 | MOD-02 |
| MOD-03 | P1 | PH05-FE-MOD-03-P1 | MOD-03, MOD-04 |
| SYS-01 | P0 | PH03-FE-SYS-01-P0 | NFR/FAILURE |
