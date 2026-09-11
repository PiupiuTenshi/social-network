# Danh mục hợp đồng API

| Dịch vụ | Phương thức | Đường dẫn | Quyền | Mục đích |
| --- | --- | --- | --- | --- |
| Tài khoản | POST | /api/v1/auth/register | Công khai | Tạo tài khoản và phát UserRegistered |
| Tài khoản | POST | /api/v1/auth/google | Công khai | Đăng nhập/đăng ký bằng Google; phát UserRegistered nếu mới |
| Tài khoản | POST | /api/v1/auth/login | Công khai | Cấp access token và refresh token |
| Tài khoản | POST | /api/v1/auth/refresh | Refresh token | Xoay vòng refresh token và cấp cặp token mới |
| Tài khoản | POST | /api/v1/auth/logout | Người dùng | Thu hồi refresh token hoặc họ phiên |
| Tài khoản | GET | /api/v1/users/{id} | Theo chính sách | Đọc hồ sơ theo quyền riêng tư |
| Tài khoản | PATCH | /api/v1/users/me | Người dùng | Cập nhật hồ sơ; yêu cầu If-Match |
| Tài khoản | PATCH | /api/v1/users/me/avatar | Người dùng | Cập nhật ảnh đại diện sau khi xác minh MediaReady |
| Tài khoản | PATCH | /api/v1/users/me/settings | Người dùng | Cập nhật thiết lập tài khoản |
| Tài khoản | POST | /api/v1/auth/forgot-password | Công khai | Yêu cầu OTP và phát PasswordResetRequested |
| Tài khoản | POST | /api/v1/auth/reset-password | Công khai | Xác minh OTP, đổi mật khẩu và thu hồi mọi refresh token |
| Tài khoản | DELETE | /api/v1/users/me | Người dùng | Yêu cầu xóa tài khoản, thu hồi phiên và bắt đầu thời gian ân hạn |
| Tài khoản | POST | /api/v1/users/me/deletion/cancel | Người dùng | Hủy yêu cầu xóa trong thời gian ân hạn |
| Mạng xã hội | POST | /api/v1/users/{id}/follow | Người dùng | Theo dõi và phát UserFollowed |
| Mạng xã hội | DELETE | /api/v1/users/{id}/follow | Người dùng | Bỏ theo dõi và phát UserUnfollowed |
| Mạng xã hội | POST | /api/v1/users/{id}/block | Người dùng | Chặn và phát UserBlocked |
| Mạng xã hội | DELETE | /api/v1/users/{id}/block | Người dùng | Bỏ chặn và phát UserUnblocked |
| Mạng xã hội | POST | /api/v1/posts | Người dùng | Tạo bài viết hoặc bài viết video; hỗ trợ Idempotency-Key |
| Mạng xã hội | GET | /api/v1/posts/{id} | Theo chính sách | Đọc bài viết sau khi áp dụng quyền riêng tư và chặn |
| Mạng xã hội | GET | /api/v1/users/{id}/posts | Theo chính sách | Đọc danh sách bài viết bằng con trỏ |
| Mạng xã hội | PATCH | /api/v1/posts/{id} | Chủ sở hữu | Cập nhật bài viết; yêu cầu If-Match |
| Mạng xã hội | DELETE | /api/v1/posts/{id} | Chủ sở hữu/Điều hành | Xóa mềm và phát PostDeleted |
| Mạng xã hội | POST | /api/v1/posts/{id}/comments | Người dùng | Tạo bình luận hoặc trả lời |
| Mạng xã hội | PUT | /api/v1/posts/{id}/reaction | Người dùng | Thêm hoặc thay tương tác |
| Mạng xã hội | DELETE | /api/v1/posts/{id}/reaction | Người dùng | Xóa tương tác |
| Mạng xã hội | POST | /api/v1/posts/{id}/share | Người dùng | Sinh liên kết chia sẻ và ghi nhận PostShared |
| Bảng tin | GET | /api/v1/feed | Người dùng | Đọc bảng tin bằng con trỏ |
| Phương tiện | POST | /api/v1/media/uploads | Người dùng | Tạo phiên tải lên và URL ký trước |
| Phương tiện | POST | /api/v1/media/uploads/{id}/complete | Chủ sở hữu | Xác minh đối tượng và hoàn tất tải lên |
| Phương tiện | DELETE | /api/v1/media/{id} | Chủ sở hữu/Hệ thống | Đánh dấu xóa và lên lịch dọn đối tượng |
| Cộng đồng | POST | /api/v1/communities | Người dùng | Tạo cộng đồng |
| Cộng đồng | PATCH | /api/v1/communities/{id} | Chủ sở hữu | Cập nhật cộng đồng; yêu cầu If-Match |
| Cộng đồng | POST | /api/v1/communities/{id}/invites | Có quyền | Tạo lời mời có hạn dùng và số lượt |
| Cộng đồng | POST | /api/v1/communities/{id}/join | Người dùng/Lời mời | Tham gia cộng đồng |
| Cộng đồng | POST | /api/v1/communities/{id}/leave | Thành viên | Rời cộng đồng theo quy tắc chuyển chủ sở hữu |
| Cộng đồng | POST | /api/v1/communities/{id}/channels | Có quyền | Tạo kênh |
| Cộng đồng | PUT | /api/v1/communities/{id}/roles/{roleId} | Quản lý vai trò | Tạo/cập nhật vai trò và quyền |
| Cộng đồng | PUT | /api/v1/communities/{id}/members/{memberId}/roles | Quản lý vai trò | Gán vai trò theo thứ bậc |
| Cộng đồng | POST | /api/v1/communities/{id}/members/{memberId}/moderation | Điều hành | Mute/kick/ban và phát MemberModerated |
| Cộng đồng | POST | /api/v1/channels/{id}/rtc-token | Thành viên | Cấp token LiveKit theo quyền |
| Trò chuyện | POST | /api/v1/conversations | Người dùng | Tạo hội thoại trực tiếp hoặc nhóm |
| Trò chuyện | GET | /api/v1/conversations/{id}/messages | Thành viên | Đọc lịch sử tin nhắn bằng con trỏ |
| Trò chuyện | POST | /api/v1/conversations/{id}/messages | Thành viên | Gửi tin nhắn qua HTTP dự phòng; yêu cầu clientMessageId |
| Trò chuyện | PATCH | /api/v1/messages/{id} | Người gửi/Điều hành | Sửa tin nhắn; yêu cầu If-Match |
| Trò chuyện | DELETE | /api/v1/messages/{id} | Người gửi/Điều hành | Xóa mềm tin nhắn |
| Trò chuyện | PUT | /api/v1/messages/{id}/reaction | Thành viên | Thêm hoặc thay tương tác tin nhắn |
| Trò chuyện | DELETE | /api/v1/messages/{id}/reaction | Thành viên | Xóa tương tác tin nhắn |
| Trò chuyện | POST | /api/v1/conversations/{id}/read | Thành viên | Tiến con trỏ đã đọc theo chiều tăng |
| Trò chuyện | GET | /api/v1/notifications | Người dùng | Đọc hộp thông báo |
| Trò chuyện | PATCH | /api/v1/notifications/{id}/read | Người dùng | Đánh dấu thông báo đã đọc |
| Trò chuyện | POST | /api/v1/conversations/{id}/call-invites | Thành viên | Tạo lời mời cuộc gọi qua SignalR |
| Thương mại | POST | /api/v1/listings | Người bán | Tạo tin đăng |
| Thương mại | GET | /api/v1/listings | Công khai/Theo chính sách | Duyệt hoặc tìm tin đăng |
| Thương mại | PATCH | /api/v1/listings/{id} | Người bán | Cập nhật tin đăng; yêu cầu If-Match |
| Thương mại | PUT | /api/v1/listings/{id}/inventory | Người bán | Điều chỉnh tồn kho bằng cập nhật nguyên tử |
| Thương mại | POST | /api/v1/orders | Người mua | Tạo đơn và giữ tồn kho; bắt buộc Idempotency-Key |
| Thương mại | GET | /api/v1/orders/{id} | Người mua/Người bán liên quan | Đọc đơn hàng theo quyền |
| Thương mại | POST | /api/v1/orders/{id}/cancel | Người mua/Hệ thống | Hủy đơn hợp lệ và giải phóng tồn kho |
| Thương mại | POST | /api/v1/orders/{id}/pay | Người mua | Thanh toán giả lập; bắt buộc Idempotency-Key |
| AI và tìm kiếm | POST | /api/v1/ai/ask | Người dùng | Hỏi trợ lý RAG trong phạm vi được cấp quyền |
| AI và tìm kiếm | GET | /api/v1/search/semantic | Người dùng | Tìm kiếm ngữ nghĩa theo phạm vi |
| AI và tìm kiếm | POST | /api/v1/ai/summaries | Người có quyền | Tóm tắt nội dung do dịch vụ nguồn cấp quyền |
| AI và tìm kiếm | POST | /api/v1/ai/transcriptions | Người có quyền | Yêu cầu chuyển âm thanh MediaReady thành văn bản |
| Mạng xã hội - điều hành | POST | /api/v1/reports | Người dùng | Tạo báo cáo vi phạm và phát ContentReported |
| Mạng xã hội - điều hành | GET | /api/v1/moderation/reports | Điều hành | Đọc hàng đợi báo cáo theo quyền và bộ lọc |
| Mạng xã hội - điều hành | POST | /api/v1/moderation/reports/{id}/actions | Điều hành | Ghi hành động và phát ModerationActionRequested |
| Mạng xã hội - điều hành | POST | /api/v1/moderation/reports/{id}/close | Điều hành | Đóng báo cáo với kết luận và dấu vết kiểm toán |
