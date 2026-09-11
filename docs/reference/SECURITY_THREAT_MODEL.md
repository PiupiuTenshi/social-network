# Danh tính, mô hình đe dọa và lưu giữ dữ liệu

## Claim access token

| Claim | Giá trị | Quy tắc |
| --- | --- | --- |
| sub | AccountId | Định danh người dùng duy nhất; bắt buộc. |
| sid | Session/family id | Liên kết access token với họ refresh token để thu hồi theo phiên. |
| jti | Token id | Hỗ trợ audit và danh sách thu hồi khẩn cấp khi cần. |
| iss | Issuer | Phải đúng nhà phát hành đã cấu hình. |
| aud | Audience | Phải chứa dịch vụ/cổng API được phép nhận token. |
| iat/nbf/exp | Thời gian | Kiểm tra UTC và cho phép clock skew tối đa 60 giây. |
| ver | Token version | Tăng khi đổi mật khẩu, vô hiệu tài khoản hoặc thu hồi toàn cục. |
| global_role | Vai trò toàn cục tối thiểu | Chỉ dùng cho system_admin/moderator toàn cục; không nhét vai trò cộng đồng vào JWT. |

## Xác thực nội bộ và xoay khóa

| Khu vực | Quyết định | Hệ quả |
| --- | --- | --- |
| HTTP nội bộ | JWT dịch vụ sống <= 5 phút, audience theo dịch vụ đích và scope tối thiểu. | Mạng Docker riêng không được xem là cơ chế xác thực. |
| Kafka | ACL theo principal; producer chỉ ghi topic của mình; consumer group được cấp tối thiểu. | Không dùng cùng một credential cho mọi dịch vụ. |
| Khóa ký | JWT có kid; duy trì khóa hiện tại và khóa trước trong giai đoạn chồng tối thiểu 24 giờ. | Khóa riêng chỉ ở dịch vụ phát hành/kho bí mật; dịch vụ khác chỉ nhận khóa công khai. |
| Thu hồi | Đổi password hoặc phát hiện refresh reuse tăng token_version và thu hồi session family. | Access token cũ hết hạn nhanh; điểm cuối nhạy cảm có thể kiểm tra version cache. |
| Quyền cộng đồng | Lưu projection cục bộ TTL <= 5 phút và cập nhật qua RoleUpdated/PermissionUpdated. | Hành động nhạy cảm xác minh đồng bộ với Cộng đồng khi projection nghi ngờ stale. |

## Mô hình đe dọa

| Đe dọa | Tác động | Kiểm soát |
| --- | --- | --- |
| Chiếm refresh token | Phát lại và duy trì phiên trái phép | Chỉ lưu hash, rotation, family, reuse detection, revoke all sessions, audit. |
| BOLA/IDOR | Đọc/sửa tài nguyên bằng id đoán được | Kiểm tra quyền tại dịch vụ sở hữu, 404 cho tài nguyên ẩn, test theo từng resource. |
| Giả mạo sự kiện | Ghi dữ liệu dẫn xuất sai hoặc kích hoạt tác dụng phụ | Kafka ACL, principal riêng, schema validation, producer field kiểm chứng, Inbox. |
| Sự kiện lặp/đảo thứ tự | Tăng bộ đếm, gửi thông báo hoặc ghi đè sai | EventId unique, aggregateVersion, partition key đúng và cập nhật có điều kiện. |
| XSS/nội dung độc hại | Thực thi mã ở trình duyệt | Sanitize, output encoding, CSP, không cho HTML tùy ý. |
| SSRF/tệp giả | Worker truy cập mạng nội bộ hoặc xử lý tệp nguy hiểm | Không nhận URL tùy ý; object key server sinh; magic-byte scan; outbound allowlist. |
| Prompt injection/RAG leakage | Mô hình làm theo nội dung không tin cậy hoặc lộ dữ liệu | Authorization trước retrieval, đánh dấu context là dữ liệu, không cấp công cụ nguy hiểm, giới hạn output/log. |
| Rò bí mật | Chiếm DB/JWT/SMTP | Secret store, quét bí mật, log masking, rotation, quyền tối thiểu. |
| Lạm dụng tài nguyên | DoS qua login, upload, AI hoặc báo cáo | Rate limit theo user/IP, quota, kích thước tối đa, bounded concurrency và backpressure. |
| Chuỗi cung ứng | Gói/ảnh container có lỗ hổng | Khóa phiên bản, SBOM, quét dependency/image, base image tối thiểu và cập nhật có kiểm thử. |

## Phân loại và thời hạn dữ liệu

| Mức | Ví dụ | Thời hạn/quy tắc | Kiểm soát |
| --- | --- | --- | --- |
| Bí mật | Mật khẩu, OTP, refresh token, khóa ký | Không lưu plaintext; token/OTP chỉ lưu hash; secret theo vòng đời kho bí mật. | Chỉ dịch vụ sở hữu; không ghi log. |
| Nhạy cảm | Email, IP, nội dung riêng tư, bằng chứng điều hành | PII tài khoản xóa cứng tối đa 45 ngày; bằng chứng 180 ngày sau đóng nếu không hold. | Che trường, mã hóa khi truyền, quyền tối thiểu. |
| Nghiệp vụ | Bài viết, tin nhắn, đơn hàng, trạng thái | Xóa mềm 30 ngày; đơn hàng/audit giữ theo chính sách dự án; projection xóa sớm. | Dịch vụ sở hữu quyết định; downstream chỉ giữ tối thiểu. |
| Dẫn xuất | Feed, cache, embedding, RAG chunk | Xóa/invalidate trong 5 phút sau nguồn bị ẩn; có thể dựng lại. | Không xem là nguồn dữ liệu chuẩn. |
| Vận hành | Log, trace, metric | Log/trace 7 ngày; metric tổng hợp 30 ngày; audit bảo mật 90 ngày. | Không chứa OTP, token, payload nhạy cảm. |
| Hạ tầng sự kiện | Outbox/Inbox/DLQ | Outbox đã phát 7 ngày; Inbox 14 ngày; DLQ đến khi xử lý nhưng cảnh báo ngay. | Purge theo batch, giữ eventId và metadata audit cần thiết. |
| Bản sao lưu | PostgreSQL và object storage | 7 bản ngày + 4 bản tuần; mã hóa và tách khỏi volume chạy. | Kiểm tra checksum và diễn tập khôi phục. |

## Lan truyền xóa tài khoản

| Dịch vụ | Hành động | Quy tắc |
| --- | --- | --- |
| Tài khoản | Khóa đăng nhập, thu hồi phiên, ẩn PII | AccountDeletionRequest cập nhật trạng thái và thời hạn. |
| Mạng xã hội | Ẩn hồ sơ liên quan, xử lý bài viết/bình luận theo chính sách, xóa follow/block | Ack theo AccountId; giữ nội dung đã ẩn danh nếu chính sách cho phép. |
| Bảng tin | Xóa FeedEntry/UserSummary và cache | Có thể dựng lại; phải hoàn thành trong 5 phút. |
| Trò chuyện | Ẩn profile projection; giữ tin nhắn theo chính sách nhưng thay tên/PII | Không làm hỏng lịch sử hội thoại của người khác. |
| Cộng đồng | Vô hiệu membership/role/invite | Chuyển quyền sở hữu cộng đồng trước purge nếu cần. |
| Phương tiện | Xóa tài sản không còn tham chiếu; giữ bằng chứng có retention_hold | Tác vụ dọn bất đồng bộ, lặp an toàn. |
| Thương mại | Ẩn profile; giữ snapshot đơn hàng tối thiểu | Không xóa dữ liệu cần cho tính toàn vẹn đơn hàng. |
| AI và tìm kiếm | Xóa embedding, chunk, transcript và index dẫn xuất | Không giữ prompt/payload nhạy cảm ngoài thời hạn. |
| Đối soát | Quét deletion_request quá hạn và trạng thái xác nhận | Retry dịch vụ thiếu, cảnh báo và chỉ completed khi đạt chính sách. |
