# Mô hình dữ liệu tham chiếu

## Tài khoản

| Bảng | Trường chính | Quy tắc và chỉ mục |
| --- | --- | --- |
| account | id, email, password_hash, status, created_at, updated_at | UQ(email); chỉ mục status khi có nghiệp vụ quản trị; password_hash có thể null với tài khoản chỉ dùng OAuth. |
| profile | account_id, username, display_name, bio, avatar_media_id, privacy_level, version | PK/FK trong account_db; UQ(username); version dùng cho xử lý đồng thời lạc quan. |
| refresh_token | id, account_id, token_hash, family_id, expires_at, revoked_at, replaced_by_id | Index(account_id, expires_at); chỉ lưu hash; family_id hỗ trợ phát hiện tái sử dụng và thu hồi họ phiên. |
| password_reset_token | id, account_id, otp_hash, expires_at, consumed_at, attempt_count, invalidated_at | Index(account_id, expires_at); OTP băm, dùng một lần, TTL ngắn; khóa khi vượt số lần thử. |
| account_oauth | id, account_id, provider, provider_user_id, created_at | UQ(provider, provider_user_id); baseline chỉ dùng Google; không tự động gộp với tài khoản mật khẩu trùng email. |
| account_setting | account_id, notification_json, locale, timezone, updated_at | PK/FK trong account_db; chỉ chấp nhận khóa cấu hình được cho phép; không chứa bí mật. |
| account_deletion_request | id, account_id, requested_at, delete_after, cancelled_at, completed_at, status, version | UQ hoạt động theo account_id; thời gian ân hạn 30 ngày; theo dõi xác nhận từ các dịch vụ và cảnh báo khi quá hạn. |

## Mạng xã hội

| Bảng | Trường chính | Quy tắc và chỉ mục |
| --- | --- | --- |
| follow | follower_id, followee_id, created_at | UQ(follower_id, followee_id); cấm tự theo dõi; thao tác thêm/xóa xử lý lặp an toàn. |
| block | blocker_id, blocked_id, created_at | UQ(blocker_id, blocked_id); cấm tự chặn; quan hệ chặn ưu tiên hơn theo dõi và hiển thị. |
| post | id, author_id, content, type, visibility, version, created_at, updated_at, deleted_at | Index(author_id, created_at DESC); version cho xử lý đồng thời; type thuộc {content, video}; video ở processing đến khi MediaReady. |
| post_media_ref | post_id, media_id, position | UQ(post_id, position); media_id là tham chiếu ngoài; thứ tự phải xác định. |
| comment | id, post_id, author_id, parent_id, content, version, created_at, deleted_at | Index(post_id, created_at, id); parent_id phải cùng bài viết; giới hạn độ sâu trả lời. |
| reaction | id, post_id, user_id, type, created_at, updated_at | UQ(post_id, user_id) để ngăn trùng khi có tranh chấp; cập nhật kiểu tương tác bằng upsert. |
| post_share | id, post_id, user_id, platform, created_at | Index(post_id, created_at); cho phép một người dùng chia sẻ nhiều lần. |
| content_report | id, reporter_id, target_type, target_id, reason_code, description, status, priority, version, created_at | Index(status, priority, created_at); giới hạn báo cáo trùng đang mở; target_id là tham chiếu ngoài. |
| moderation_evidence | id, report_id, evidence_type, content_hash, object_key, expires_at | FK nội bộ tới content_report; dữ liệu bằng chứng được hạn chế quyền và xóa theo thời hạn lưu giữ. |
| moderation_action | id, report_id, moderator_id, action_type, reason, expires_at, created_at | Append-only; mọi hành động có người thực hiện, lý do, correlationId và kết quả từ dịch vụ sở hữu nội dung. |

## Cộng đồng và Trò chuyện

| Vấn đề thiết kế | Quyết định |
| --- | --- |
| Quyền sở hữu kênh | Cộng đồng sở hữu siêu dữ liệu, loại kênh và quyền truy cập. |
| Quyền sở hữu tin nhắn | Trò chuyện sở hữu cuộc hội thoại, tin nhắn và trạng thái đã đọc. |
| Kiểm tra thành viên | Trò chuyện dùng bản chiếu cục bộ; tại ranh giới nhạy cảm có thể gọi hợp đồng Cộng đồng. Không truy vấn trực tiếp community_db. |
| Trạng thái hiện diện | Lưu trạng thái tạm thời trong Valkey với TTL; PostgreSQL không phải nguồn dữ liệu chuẩn. |
| Thông báo | Dịch vụ trò chuyện sở hữu hộp thông báo để tránh tăng thêm dịch vụ. |
| Xử lý đồng thời tin nhắn | Message có version; clientMessageId duy nhất theo người gửi hoặc hội thoại để chống gửi lặp. |

## Bảng tin, Phương tiện và AI/tìm kiếm

| Phân hệ | Nguồn dữ liệu chuẩn và quy tắc dựng lại |
| --- | --- |
| Bản chiếu Bảng tin | Dẫn xuất từ sự kiện Account/Mạng xã hội; có thể dựng lại từ dữ liệu xuất của nguồn và phần sự kiện phát sinh sau mốc kiểm tra. |
| Siêu dữ liệu Phương tiện | Là dữ liệu giao dịch; đối tượng nhị phân trên SeaweedFS phải được lưu bền và sao lưu theo chính sách. |
| AI embedding | Là dữ liệu dẫn xuất; tạo lại khi mô hình hoặc phiên bản tiền xử lý thay đổi. |
| Đoạn dữ liệu RAG | Phải giữ loại nguồn, định danh nguồn, phạm vi và siêu dữ liệu phân quyền; không tạo kho ngữ liệu toàn cục không kiểm soát. |

## Thương mại

| Bảng | Quy tắc |
| --- | --- |
| listing | seller_id là tham chiếu ngoài; version cho xử lý đồng thời; status quyết định khả năng hiển thị. |
| listing_media_ref | UQ(listing_id, position); chỉ tham chiếu MediaAsset ở trạng thái Ready và đúng mục đích sử dụng. |
| inventory | quantity >= 0; 0 <= reserved <= quantity; cập nhật giữ hàng bằng lệnh nguyên tử hoặc khóa dòng; có version. |
| order / order_item | Chụp giá tại thời điểm tạo đơn; mỗi chuyển trạng thái phải hợp lệ và được ghi lịch sử. |
| payment | Nhà cung cấp giả lập; idempotency_key duy nhất; một thanh toán đang hoạt động cho mỗi đơn trong phạm vi cơ sở. |
| order_status_history | Chỉ thêm mới để lưu vết chuyển trạng thái; không cập nhật hoặc xóa trong luồng nghiệp vụ thông thường. |

## Bảng hạ tầng dùng chung

| Bảng | Trường chính | Quy tắc |
| --- | --- | --- |
| outbox_message | id, aggregate_type, aggregate_id, event_type, event_version, payload_json, correlation_id, occurred_at, published_at, retry_count, last_error | PK(id); index(published_at, occurred_at); nội dung sự kiện bất biến sau khi commit; thử lại có giãn cách. |
| inbox_message | consumer_name, event_id, event_type, received_at, processed_at, status, last_error | PK(consumer_name, event_id); ghi cùng giao dịch với tác dụng phụ; lỗi vĩnh viễn chuyển DLQ. |
| idempotency_request | scope, idempotency_key, request_hash, response_code, response_body, created_at, expires_at | PK(scope, idempotency_key); cùng khóa nhưng request_hash khác trả 409; TTL mặc định 24 giờ. |

## Báo cáo và điều hành nội dung

| Bảng | Trường chính | Quy tắc |
| --- | --- | --- |
| content_report | id, reporter_id, target_type, target_id, reason_code, description, status, priority, assigned_to, version, created_at, reviewed_at | Index(status, priority, created_at); target là tham chiếu ngoài; một báo cáo đang mở tương đương được gộp hoặc từ chối theo policy. |
| moderation_evidence | id, report_id, evidence_type, content_hash, object_key, captured_at, expires_at, retention_hold | Không sao chép quá mức; object private; chỉ người có quyền điều hành truy cập; xóa theo retention. |
| moderation_action | id, report_id, moderator_id, action_type, target_type, target_id, reason, expires_at, correlation_id, created_at | Append-only; không sửa/xóa; hành động lặp dùng action id làm idempotency key. |
