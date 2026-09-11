# Đặc tả chức năng tham chiếu

## ACC-01 - Đăng ký

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Khách |
| Điều kiện trước | Email và username chưa tồn tại. |
| Luồng chính | Kiểm tra dữ liệu -> băm mật khẩu -> tạo Account/Profile -> ghi Outbox UserRegistered -> trả thông tin tài khoản. |
| Kiểm tra và phân quyền | Định dạng email, chính sách mật khẩu, username duy nhất và giới hạn tần suất. |
| Thay đổi dữ liệu | Thêm bản ghi account/profile/outbox. |
| Sự kiện và thời gian thực | Phát UserRegistered qua Kafka. |
| Lỗi và trường hợp biên | 409 khi email hoặc username trùng; 422 khi dữ liệu không hợp lệ; lỗi DB tạm thời trả 503 và chỉ thử lại tại tầng an toàn. |
| Ghi chú | Không bao giờ trả password_hash. |

## ACC-02 - Đăng nhập

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Khách |
| Điều kiện trước | Tài khoản đang hoạt động. |
| Luồng chính | Xác minh thông tin đăng nhập -> cấp access token sống ngắn và refresh token -> lưu hash của refresh token. |
| Kiểm tra và phân quyền | Giới hạn tần suất; có thể khóa tạm theo chính sách; từ chối tài khoản bị vô hiệu hóa. |
| Thay đổi dữ liệu | Thêm bản ghi refresh_token và chỉ lưu token_hash. |
| Sự kiện và thời gian thực | Không yêu cầu phát sự kiện Kafka. |
| Lỗi và trường hợp biên | 401 không hợp lệ; 403 bị vô hiệu hóa. |
| Ghi chú | Không tiết lộ email hoặc tài khoản có tồn tại. |

## ACC-03 - Xoay vòng refresh token

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Đã xác thực bằng refresh token |
| Điều kiện trước | Refresh token hợp lệ và chưa bị thu hồi. |
| Luồng chính | Xác minh hash -> thu hồi token cũ -> tạo token thay thế -> cấp access token và refresh token mới. |
| Kiểm tra và phân quyền | Refresh token chỉ được xoay vòng một lần; phát hiện tái sử dụng theo family_id và thu hồi họ phiên khi cần. |
| Thay đổi dữ liệu | Cập nhật revoked_at của token cũ và thêm token thay thế trong cùng giao dịch. |
| Sự kiện và thời gian thực | Sự kiện kiểm toán bảo mật là tùy chọn. |
| Lỗi và trường hợp biên | 401 khi token hết hạn, đã bị thu hồi hoặc bị tái sử dụng. |

## ACC-04 - Đăng xuất

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Refresh token hoặc phiên tồn tại. |
| Luồng chính | Thu hồi refresh token được yêu cầu hoặc toàn bộ họ phiên. |
| Kiểm tra và phân quyền | Token hoặc phiên phải thuộc người gọi. |
| Thay đổi dữ liệu | Cập nhật refresh_token.revoked_at. |
| Sự kiện và thời gian thực | Không yêu cầu. |
| Lỗi và trường hợp biên | Đăng xuất xử lý lặp an toàn và vẫn trả thành công khi token đã bị thu hồi. |

## ACC-05 - Xem và cập nhật hồ sơ

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Hồ sơ đích được phép hiển thị theo chính sách riêng tư. |
| Luồng chính | GET đọc hồ sơ hoặc PATCH các trường cho phép -> kiểm tra version -> cập nhật profile -> ghi Outbox UserProfileUpdated. |
| Kiểm tra và phân quyền | Kiểm tra ràng buộc username và tên hiển thị; chỉ chủ sở hữu được sửa. |
| Thay đổi dữ liệu | Cập nhật profile/version. |
| Sự kiện và thời gian thực | UserProfileUpdated. |
| Lỗi và trường hợp biên | 409 khi version xung đột; 403 khi không đủ quyền hoặc vi phạm chính sách riêng tư. |

## ACC-06 - Cập nhật tham chiếu avatar

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Người dùng |
| Điều kiện trước | MediaAsset ở trạng thái Ready và thuộc quyền sở hữu hoặc sử dụng của người gọi. |
| Luồng chính | Gán avatar_media_id -> phát sự kiện cập nhật hồ sơ. |
| Kiểm tra và phân quyền | Kiểm tra quyền sở hữu và tham chiếu Phương tiện qua hợp đồng hoặc bản chiếu. |
| Thay đổi dữ liệu | Cập nhật profile. |
| Sự kiện và thời gian thực | UserProfileUpdated/UserAvatarUpdated. |
| Lỗi và trường hợp biên | 422 khi MediaAsset chưa ở trạng thái Ready hoặc không được phép sử dụng. |

## ACC-07 - Quyền riêng tư và thiết lập tài khoản

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực. |
| Luồng chính | Cập nhật mức hiển thị và thiết lập bằng tập giá trị cho phép rõ ràng. |
| Kiểm tra và phân quyền | Chỉ chính người dùng hoặc quản trị viên được thực hiện thao tác trạng thái tương ứng. |
| Thay đổi dữ liệu | Cập nhật account_setting hoặc các trường thiết lập tương ứng. |
| Sự kiện và thời gian thực | Chỉ phát sự kiện quyền riêng tư hoặc hồ sơ khi dịch vụ hạ nguồn thực sự cần. |
| Lỗi và trường hợp biên | 422 khi enum hoặc giá trị thiết lập không hợp lệ; 409 khi version xung đột. |

## ACC-08 - Yêu cầu OTP khôi phục mật khẩu

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Khách |
| Điều kiện trước | Hệ thống xử lý khi có tài khoản khớp email nhưng phản hồi phải giống nhau trong mọi trường hợp. |
| Luồng chính | Kiểm tra định dạng email -> sinh OTP 6 chữ số -> lưu otp_hash, expires_at và attempt_count=0 -> gửi OTP qua SMTP -> trả phản hồi thành công chung. |
| Kiểm tra và phân quyền | Giới hạn theo tài khoản và IP; không tiết lộ email có tồn tại. |
| Thay đổi dữ liệu | Thêm password_reset_token với otp_hash, expires_at, attempt_count=0; vô hiệu OTP chưa dùng trước đó của cùng account. |
| Sự kiện và thời gian thực | Phát PasswordResetRequested để gửi email và kiểm toán; Kafka không nằm trên đường xử lý bắt buộc của API. |
| Lỗi và trường hợp biên | Khi nhà cung cấp email không sẵn sàng, xếp hàng và thử lại bất đồng bộ; API vẫn trả phản hồi chung. |
| Ghi chú | OTP có TTL mặc định 10 phút; OTP mới làm mất hiệu lực mọi OTP chưa dùng trước đó của cùng tài khoản. |

## ACC-09 - Đặt lại mật khẩu bằng OTP

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Khách |
| Điều kiện trước | OTP của tài khoản hợp lệ, chưa hết hạn và chưa được sử dụng. |
| Luồng chính | Xác minh otp_hash, thời hạn và số lần thử -> băm mật khẩu mới -> cập nhật account -> đánh dấu token đã dùng -> thu hồi mọi refresh token. |
| Kiểm tra và phân quyền | OTP dùng một lần; tối đa 5 lần thử theo cấu hình; bắt buộc chính sách mật khẩu; khóa token khi vượt ngưỡng. |
| Thay đổi dữ liệu | Cập nhật account.password_hash, password_reset_token.consumed_at và thu hồi mọi hàng refresh_token đang hoạt động. |
| Sự kiện và thời gian thực | Có thể phát UserPasswordReset cho mục đích kiểm toán. |
| Lỗi và trường hợp biên | 401 khi OTP sai, hết hạn hoặc đã dùng; 429 khi vượt số lần thử. |

## ACC-10 - Đăng nhập bằng Google OAuth

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Khách |
| Điều kiện trước | Máy khách có Google id_token hợp lệ theo OAuth 2.0/OpenID Connect. |
| Luồng chính | Xác minh id_token với Google theo issuer, audience và chữ ký -> tìm account_oauth theo (provider, provider_user_id) -> nếu chưa có thì tạo account, account_oauth và profile mặc định -> cấp access token/refresh token như ACC-02. |
| Kiểm tra và phân quyền | Chỉ chấp nhận id_token đúng client_id đã cấu hình; email do Google xác minh được xem là đã xác thực. |
| Thay đổi dữ liệu | Thêm bản ghi account (nếu mới), account_oauth, profile. |
| Sự kiện và thời gian thực | UserRegistered (nếu tài khoản mới), tương tự ACC-01. |
| Lỗi và trường hợp biên | Email Google trùng với account dùng mật khẩu -> yêu cầu liên kết thủ công thay vì tự động gộp, tránh chiếm quyền tài khoản. |
| Ghi chú | Tài khoản tạo qua Google có thể không có password_hash; ACC-08/09 chỉ áp dụng sau khi người dùng tự đặt mật khẩu. |

## SOC-01 - Theo dõi và bỏ theo dõi

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Người dùng đích tồn tại và không bị chặn theo chính sách. |
| Luồng chính | Theo dõi: thêm quan hệ duy nhất; bỏ theo dõi: xóa quan hệ theo cách xử lý lặp an toàn. |
| Kiểm tra và phân quyền | Cấm tự theo dõi; quan hệ chặn ở bất kỳ hướng nào đều ngăn theo dõi. |
| Thay đổi dữ liệu | Thêm hoặc xóa bản ghi follow. |
| Sự kiện và thời gian thực | UserFollowed/UserUnfollowed. |
| Lỗi và trường hợp biên | Theo dõi trùng trả thành công theo tính lặp an toàn; bị chặn trả 403 hoặc 409 theo hợp đồng. |

## SOC-02 - Chặn và bỏ chặn

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đối tượng đích tồn tại. |
| Luồng chính | Tạo quan hệ block, xóa các quan hệ follow không còn hợp lệ và phát sự kiện. |
| Kiểm tra và phân quyền | Cấm tự chặn; chỉ người gọi được quản lý quan hệ chặn của mình. |
| Thay đổi dữ liệu | Thêm hoặc xóa block; dọn quan hệ follow theo quy tắc đã chọn. |
| Sự kiện và thời gian thực | UserBlocked/UserUnblocked. |
| Lỗi và trường hợp biên | Yêu cầu chặn hoặc bỏ chặn lặp được xử lý an toàn. |

## SOC-03 - Tạo bài viết

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực; phương tiện tham chiếu ở trạng thái Ready. |
| Luồng chính | Kiểm tra nội dung -> ghi Post, PostMediaRef và Outbox trong cùng giao dịch -> trả DTO đã tạo. |
| Kiểm tra và phân quyền | Kiểm tra độ dài, mức hiển thị, quyền sử dụng Phương tiện và giới hạn tần suất. |
| Thay đổi dữ liệu | Thêm post, post_media_ref và outbox_message. |
| Sự kiện và thời gian thực | PostCreated. |
| Lỗi và trường hợp biên | 422 khi nội dung hoặc Phương tiện không hợp lệ; có thể dùng Idempotency-Key để tạo lại an toàn. |

## SOC-04 - Sửa bài viết

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng/Chủ sở hữu |
| Điều kiện trước | Bài viết đang hoạt động; người gọi là chủ sở hữu. |
| Luồng chính | Kiểm tra version -> cập nhật các trường được phép -> ghi Outbox PostUpdated. |
| Kiểm tra và phân quyền | Kiểm tra chủ sở hữu, mức hiển thị, nội dung và version lạc quan. |
| Thay đổi dữ liệu | Cập nhật post/version. |
| Sự kiện và thời gian thực | PostUpdated. |
| Lỗi và trường hợp biên | 409 khi version xung đột; 404 khi bài viết đã xóa hoặc không tồn tại; 403 khi không phải chủ sở hữu. |

## SOC-05 - Xóa bài viết

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Chủ sở hữu/Điều hành viên |
| Điều kiện trước | Bài viết tồn tại hoặc đã được xóa mềm. |
| Luồng chính | Xóa mềm bài viết và ghi Outbox PostDeleted; bộ nhận sự kiện xóa hoặc ẩn các bản chiếu liên quan. |
| Kiểm tra và phân quyền | Kiểm tra quyền; yêu cầu xóa lặp phải an toàn. |
| Thay đổi dữ liệu | Gán deleted_at/status. |
| Sự kiện và thời gian thực | PostDeleted. |
| Lỗi và trường hợp biên | 404 không tồn tại; xóa lặp được xử lý an toàn. |

## SOC-06 - Xem bài viết và danh sách bài viết

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người xem |
| Điều kiện trước | Bài viết tồn tại và mức hiển thị cho phép người xem. |
| Luồng chính | Áp dụng bộ lọc mức hiển thị và trạng thái chặn -> truy vấn bằng con trỏ ổn định. |
| Kiểm tra và phân quyền | Bắt buộc áp dụng chính sách riêng tư và chặn. |
| Thay đổi dữ liệu | Không ghi dữ liệu. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Có thể trả 404 cho nội dung bị ẩn để tránh tiết lộ sự tồn tại. |

## SOC-07 - Bình luận và trả lời

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Bài viết có thể xem; người gọi đã xác thực. |
| Luồng chính | Tạo bình luận hoặc trả lời và ghi Outbox CommentCreated. |
| Kiểm tra và phân quyền | Bình luận cha phải thuộc cùng post; giới hạn độ sâu trả lời và tần suất. |
| Thay đổi dữ liệu | Thêm bản ghi comment. |
| Sự kiện và thời gian thực | CommentCreated. |
| Lỗi và trường hợp biên | 422 khi parent_id không hợp lệ; 403 khi bị chặn hoặc không có quyền xem bài viết. |

## SOC-08 - Tương tác

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Bài viết có thể xem; người gọi đã xác thực. |
| Luồng chính | Thêm hoặc thay một reaction cho mỗi cặp user/post; xóa bản ghi khi bỏ tương tác. |
| Kiểm tra và phân quyền | Bắt buộc UNIQUE(post_id, user_id) và type hợp lệ. |
| Thay đổi dữ liệu | Thêm/cập nhật/xóa reaction. |
| Sự kiện và thời gian thực | ReactionAdded/Removed. |
| Lỗi và trường hợp biên | Tranh chấp được xử lý bằng ràng buộc duy nhất; yêu cầu thử lại không tạo reaction trùng. |

## SOC-09 - Tạo bài viết video

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã hoàn tất phiên tải lên qua Phương tiện (MED-01/02); video sẵn sàng được xử lý. |
| Luồng chính | Tạo post với type=video và visibility=processing -> Phương tiện chuyển mã và tạo ảnh thu nhỏ bất đồng bộ -> khi nhận MediaReady, Mạng xã hội chuyển visibility sang published. SOC-03 với type=content được hiển thị ngay. |
| Kiểm tra và phân quyền | Giới hạn dung lượng và thời lượng video theo cấu hình; chỉ chủ sở hữu xem được post khi còn ở trạng thái processing. |
| Thay đổi dữ liệu | Thêm bản ghi post (type=video, visibility=processing); post_media_ref trỏ media video. |
| Sự kiện và thời gian thực | PostCreated (visibility=processing); PostUpdated khi chuyển sang published (theo MediaReady, mục 9). |
| Lỗi và trường hợp biên | Xử lý video thất bại -> post chuyển hoặc giữ trạng thái failed và không xuất hiện trong Bảng tin; áp dụng chính sách lỗi tại mục 17. |
| Ghi chú | SOC-03 với nội dung thông thường không qua xử lý bất đồng bộ; bài viết video luôn đi qua chuỗi xử lý Phương tiện trước khi vào Bảng tin. |

## SOC-10 - Chia sẻ bài viết ra nền tảng ngoài

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Bài viết tồn tại và mức hiển thị cho phép người dùng hiện tại xem sau khi áp dụng quy tắc chặn và riêng tư. |
| Luồng chính | Người dùng chọn chia sẻ -> máy chủ sinh liên kết kèm Open Graph metadata và ghi post_share -> trả liên kết để máy khách mở thao tác chia sẻ tới nền tảng ngoài. |
| Kiểm tra và phân quyền | Áp dụng cùng quy tắc hiển thị như khi đọc post. |
| Thay đổi dữ liệu | Thêm bản ghi post_share (post_id, user_id, platform, created_at). |
| Sự kiện và thời gian thực | Mạng xã hội phát PostShared; Bảng tin có thể dùng sự kiện này như tín hiệu xếp hạng. |
| Lỗi và trường hợp biên | Khi nền tảng không xác định, vẫn trả liên kết chung để máy khách sao chép hoặc tự xử lý. |
| Ghi chú | Việc đăng lên nền tảng ngoài do máy khách hoặc deep link xử lý; máy chủ chỉ sinh liên kết và ghi nhận lượt chia sẻ. |

## COM-01 - Tạo và cập nhật cộng đồng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Người dùng/Chủ sở hữu |
| Điều kiện trước | Đã xác thực. |
| Luồng chính | Tạo membership chủ sở hữu, vai trò và kênh mặc định trong một giao dịch; cập nhật Cộng đồng bằng version. |
| Kiểm tra và phân quyền | Kiểm tra tên; chỉ chủ sở hữu được đổi thiết lập quan trọng. |
| Thay đổi dữ liệu | Thêm/cập nhật community/member/role/channel. |
| Sự kiện và thời gian thực | CommunityCreated/Updated. |
| Lỗi và trường hợp biên | 409 khi slug bị trùng nếu hệ thống dùng slug duy nhất. |

## COM-02 - Mời, tham gia và rời cộng đồng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Lời mời hợp lệ hoặc chính sách cộng đồng cho phép tham gia. |
| Luồng chính | Tạo lời mời; tham gia thì tạo membership; rời đi thì chuyển membership sang không hoạt động. |
| Kiểm tra và phân quyền | Kiểm tra thời hạn, số lượt dùng tối đa và trạng thái cấm; chủ sở hữu không được rời đi khi chưa chuyển quyền. |
| Thay đổi dữ liệu | Thêm hoặc cập nhật membership, invite và số lượt sử dụng. |
| Sự kiện và thời gian thực | MemberJoined/LeftCommunity. |
| Lỗi và trường hợp biên | 410 khi lời mời hết hạn; 403 khi người dùng bị cấm. |

## COM-03 - Vai trò và quyền

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Chủ sở hữu/Điều hành viên |
| Điều kiện trước | Người gọi có quyền ManageRole. |
| Luồng chính | Tạo hoặc cập nhật vai trò, gán cho thành viên và tính quyền hiệu lực. |
| Kiểm tra và phân quyền | Không được nâng quyền vượt quá thứ bậc của người thực hiện; vai trò chủ sở hữu được bảo vệ. |
| Thay đổi dữ liệu | Thêm hoặc cập nhật role và member_role. |
| Sự kiện và thời gian thực | RoleUpdated/PermissionUpdated. |
| Lỗi và trường hợp biên | 403 khi có hành vi nâng quyền vượt quá thứ bậc cho phép. |

## COM-04 - Tạo kênh văn bản hoặc kênh thoại

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Điều hành viên |
| Điều kiện trước | Người gọi có quyền ManageChannel. |
| Luồng chính | Tạo siêu dữ liệu kênh và phát sự kiện; Trò chuyện tạo bản chiếu cho kênh văn bản. |
| Kiểm tra và phân quyền | Kiểm tra thiết lập theo loại kênh; có thể áp dụng tên duy nhất. |
| Thay đổi dữ liệu | Thêm bản ghi channel/outbox. |
| Sự kiện và thời gian thực | ChannelCreated. |
| Lỗi và trường hợp biên | Bản chiếu Trò chuyện được tạo theo nhất quán cuối; trạng thái chờ phải quan sát được. |

## COM-05 - Điều hành thành viên

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Điều hành viên |
| Điều kiện trước | Đối tượng là thành viên và người thực hiện có quyền phù hợp. |
| Luồng chính | Tắt tiếng, loại hoặc cấm theo chính sách; sau đó phát sự kiện. |
| Kiểm tra và phân quyền | Tuân theo thứ bậc vai trò; không được điều hành chủ sở hữu hoặc vai trò cao hơn. |
| Thay đổi dữ liệu | Cập nhật community_member.status và các trường điều hành liên quan. |
| Sự kiện và thời gian thực | MemberModerated. |
| Lỗi và trường hợp biên | 403 khi vi phạm thứ bậc vai trò. |

## RTC-01 - Cấp token tham gia LiveKit

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Cộng đồng |
| Tác nhân chính | Thành viên |
| Điều kiện trước | Kênh thoại hoặc video tồn tại. |
| Luồng chính | Kiểm tra thành viên và quyền JoinVoice/Speak -> sinh token sống ngắn, giới hạn phạm vi. |
| Kiểm tra và phân quyền | Không tin userId do máy khách gửi; định danh lấy từ claim đã xác thực. |
| Thay đổi dữ liệu | Chỉ ghi siêu dữ liệu cuộc gọi hoặc phòng khi chức năng yêu cầu. |
| Sự kiện và thời gian thực | Sự kiện vòng đời cuộc gọi hoặc phòng là tùy chọn. |
| Lỗi và trường hợp biên | 403 khi thiếu quyền; 503 khi LiveKit tạm thời không sẵn sàng. |

## RTC-02 - Thoại, video và chia sẻ màn hình

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mặt phẳng LiveKit |
| Tác nhân chính | Thành viên |
| Điều kiện trước | Token và quyền phương tiện hợp lệ. |
| Luồng chính | Máy khách phát hoặc đăng ký track trực tiếp với LiveKit; dùng coturn khi kết nối trực tiếp thất bại. |
| Kiểm tra và phân quyền | Kiểm tra quyền ScreenShare/Speak và trạng thái tắt tiếng của máy khách. |
| Thay đổi dữ liệu | Ứng dụng không lưu các gói phương tiện; chỉ có siêu dữ liệu tùy chọn. |
| Sự kiện và thời gian thực | Chỉ phát siêu dữ liệu vòng đời. |
| Lỗi và trường hợp biên | Lỗi RTC không được làm gián đoạn Trò chuyện văn bản. |

## RTC-03 - Phát trực tiếp màn hình trong phòng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mặt phẳng LiveKit |
| Tác nhân chính | Thành viên |
| Điều kiện trước | Đã tham gia phòng thoại và có quyền ScreenShare. |
| Luồng chính | Phát track màn hình; người tham gia đăng ký nhận có chọn lọc. |
| Kiểm tra và phân quyền | Không dùng SRS hoặc phát công khai trong phạm vi cơ sở. |
| Thay đổi dữ liệu | Không ghi dữ liệu quan hệ ngoài siêu dữ liệu phiên tùy chọn. |
| Sự kiện và thời gian thực | StreamStarted/StreamEnded là tùy chọn. |
| Lỗi và trường hợp biên | Giới hạn tài nguyên hoặc mạng phải được trả rõ ràng cho người dùng và không làm gián đoạn Trò chuyện. |

## CHT-01 - Tạo hội thoại trực tiếp hoặc nhóm

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Người tham gia hợp lệ và không bị chặn theo chính sách. |
| Luồng chính | Tạo hội thoại và thành viên; trả về DTO hội thoại. |
| Kiểm tra và phân quyền | Giới hạn số người tham gia; hội thoại trực tiếp 1:1 trùng có thể dùng lại hội thoại hiện có. |
| Thay đổi dữ liệu | Thêm conversation và conversation_member. |
| Sự kiện và thời gian thực | ConversationCreated là tùy chọn. |
| Lỗi và trường hợp biên | 403 khi bị chặn; 409 khi vi phạm chính sách hội thoại nhóm trùng. |

## CHT-02 - Gửi tin nhắn

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Thành viên hội thoại |
| Điều kiện trước | Người gọi là thành viên hội thoại. |
| Luồng chính | Lưu message và Outbox trong một giao dịch -> phát SignalR tới nhóm đang trực tuyến -> phát sự kiện Kafka bất đồng bộ. |
| Kiểm tra và phân quyền | Kiểm tra độ dài, loại, tham chiếu Phương tiện, tư cách thành viên, giới hạn tần suất và clientMessageId chống gửi lặp. |
| Thay đổi dữ liệu | Thêm message và outbox_message trong cùng giao dịch; client_message_id duy nhất trong phạm vi hội thoại/người gửi. |
| Sự kiện và thời gian thực | MessageSent + SignalR MessageCreated. |
| Lỗi và trường hợp biên | clientMessageId trùng trả về tin nhắn hiện có; nếu DB lỗi thì không phát tin nhắn ảo qua thời gian thực. |

## CHT-03 - Sửa và xóa tin nhắn

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Người gửi/Điều hành viên |
| Điều kiện trước | Tin nhắn tồn tại; người gọi là người gửi hoặc điều hành viên được cấp quyền. |
| Luồng chính | Cập nhật lạc quan hoặc xóa mềm -> phát cập nhật SignalR -> phát sự kiện. |
| Kiểm tra và phân quyền | Có thể giới hạn thời gian sửa; bắt buộc kiểm tra chủ sở hữu. |
| Thay đổi dữ liệu | Cập nhật message.version, edited_at hoặc deleted_at; ghi Outbox cho MessageEdited/MessageDeleted. |
| Sự kiện và thời gian thực | MessageEdited/Deleted. |
| Lỗi và trường hợp biên | 409 xung đột. |

## CHT-04 - Tương tác với tin nhắn

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Thành viên hội thoại |
| Điều kiện trước | Người gọi là thành viên hội thoại và tin nhắn đích tồn tại. |
| Luồng chính | Thêm, cập nhật hoặc xóa tương tác bằng ràng buộc duy nhất. |
| Kiểm tra và phân quyền | Chỉ cho phép emoji hoặc type hợp lệ và áp dụng giới hạn tần suất. |
| Thay đổi dữ liệu | Thêm, cập nhật hoặc xóa message_reaction. |
| Sự kiện và thời gian thực | SignalR MessageReactionChanged; Kafka tùy chọn. |
| Lỗi và trường hợp biên | Tương tác trùng được xử lý an toàn bằng ràng buộc duy nhất. |

## CHT-05 - Trạng thái đang nhập

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện/SignalR |
| Tác nhân chính | Thành viên hội thoại |
| Điều kiện trước | Kết nối đang hoạt động. |
| Luồng chính | Phát trạng thái đang nhập tạm thời; trạng thái tự dừng hoặc hết hạn. |
| Kiểm tra và phân quyền | Giới hạn tần suất; không ghi PostgreSQL. |
| Thay đổi dữ liệu | Chỉ ghi khóa Valkey có TTL khi cần; không ghi PostgreSQL. |
| Sự kiện và thời gian thực | SignalR TypingChanged. |
| Lỗi và trường hợp biên | Bỏ qua sự kiện trạng thái đang nhập khi người dùng ngoại tuyến. |

## CHT-06 - Trạng thái hiện diện

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện/SignalR |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đang kết nối. |
| Luồng chính | Theo dõi số kết nối và lần hoạt động gần nhất trong Valkey với TTL; phát theo chính sách riêng tư. |
| Kiểm tra và phân quyền | Hỗ trợ nhiều kết nối thiết bị và áp dụng quyền riêng tư. |
| Thay đổi dữ liệu | Chỉ cập nhật Valkey; last_seen bền vững là tùy chọn và phải được điều tiết tần suất ghi. |
| Sự kiện và thời gian thực | SignalR PresenceChanged. |
| Lỗi và trường hợp biên | Mất kết nối mạng được xử lý bằng TTL và kết nối lại. |

## CHT-07 - Xác nhận đã đọc

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Thành viên hội thoại |
| Điều kiện trước | Tin nhắn thuộc hội thoại. |
| Luồng chính | Chỉ tăng con trỏ last_read và phát xác nhận đã đọc. |
| Kiểm tra và phân quyền | Không cho phép con trỏ đã đọc lùi lại. |
| Thay đổi dữ liệu | Cập nhật conversation_member. |
| Sự kiện và thời gian thực | SignalR ReadUpdated. |
| Lỗi và trường hợp biên | 422 khi messageId không thuộc conversationId; 404 khi không tìm thấy hội thoại hoặc tin nhắn. |

## CHT-08 - Hộp thông báo

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã nhận sự kiện Mạng xã hội, Cộng đồng hoặc Trò chuyện liên quan. |
| Luồng chính | Bộ nhận sự kiện xử lý lặp an toàn tạo thông báo -> phát SignalR khi người dùng trực tuyến -> cho phép đánh dấu đã đọc. |
| Kiểm tra và phân quyền | Kiểm tra người nhận, riêng tư, bộ lọc và EventId trùng. |
| Thay đổi dữ liệu | Thêm/cập nhật notification/inbox. |
| Sự kiện và thời gian thực | Phát SignalR NotificationCreated; thao tác đánh dấu đọc cập nhật NotificationRead. |
| Lỗi và trường hợp biên | Lỗi của bộ nhận sự kiện được thử lại hữu hạn; lỗi kéo dài chuyển DLQ. |

## CHT-09 - Lời mời cuộc gọi

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Trò chuyện + cộng đồng |
| Tác nhân chính | Người dùng/Thành viên |
| Điều kiện trước | Người gọi có quyền đối với phòng hoặc cuộc gọi. |
| Luồng chính | Tạo trạng thái lời mời nhẹ -> phát SignalR tới người nhận -> khi chấp nhận thì chuyển sang luồng cấp token LiveKit. |
| Kiểm tra và phân quyền | Kiểm tra thành viên, chặn và quyền riêng tư. |
| Thay đổi dữ liệu | Có thể lưu call_invite tạm thời hoặc bền vững tùy yêu cầu lịch sử. |
| Sự kiện và thời gian thực | SignalR CallInvite/CallStateChanged. |
| Lỗi và trường hợp biên | Hết thời gian hoặc từ chối không được để lại tài nguyên Phương tiện hoặc phòng không sử dụng. |

## FED-01 - Xây dựng bản chiếu bảng tin theo dõi

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Bảng tin |
| Tác nhân chính | Bộ nhận sự kiện Kafka |
| Điều kiện trước | Có sự kiện PostCreated và UserFollowed cần xử lý. |
| Luồng chính | Xử lý sự kiện lặp an toàn -> tạo hoặc cập nhật FeedEntry, FeedPostSummary và FeedUserSummary khi cần. |
| Kiểm tra và phân quyền | Bỏ qua ứng viên bị chặn, đã xóa hoặc không hợp lệ theo quyền riêng tư. |
| Thay đổi dữ liệu | Thêm hoặc cập nhật bản chiếu và inbox_message trong cùng giao dịch xử lý sự kiện. |
| Sự kiện và thời gian thực | Không yêu cầu sự kiện bên ngoài. |
| Lỗi và trường hợp biên | Sự kiện trùng không tạo bản chiếu trùng; độ trễ xử lý sự kiện phải được đo và cảnh báo. |

## FED-02 - Đọc bảng tin bằng con trỏ

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Bảng tin |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực. |
| Luồng chính | Kiểm tra bộ nhớ đệm Valkey -> đọc FeedDb khi không có -> áp dụng con trỏ và giới hạn -> trả DTO đầy đủ. |
| Kiểm tra và phân quyền | Giới hạn kích thước trang; lọc cứng theo hiển thị và bảo đảm thứ tự ổn định. |
| Thay đổi dữ liệu | Không ghi dữ liệu ngoài bộ nhớ đệm. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Không có dữ liệu trong bộ nhớ đệm là bình thường; khi hệ thống gợi ý lỗi thì dùng Bảng tin theo thời gian. |

## FED-03 - Cập nhật bản chiếu và làm mất hiệu lực bộ nhớ đệm

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Bảng tin |
| Tác nhân chính | Bộ nhận sự kiện Kafka |
| Điều kiện trước | Có sự kiện Profile hoặc Post. |
| Luồng chính | Cập nhật bản tóm tắt cục bộ rồi làm mất hiệu lực các khóa bộ nhớ đệm liên quan. |
| Kiểm tra và phân quyền | Kiểm tra phiên bản sự kiện và khả năng xử lý lặp an toàn. |
| Thay đổi dữ liệu | Cập nhật bản chiếu và inbox_message; chỉ làm mất hiệu lực cache sau khi giao dịch thành công. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Sự kiện cũ hoặc sai thứ tự được xử lý bằng version hoặc dấu thời gian khi cần. |

## FED-04 - Sinh ứng viên và chấm điểm gợi ý

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Bảng tin và dữ liệu AI |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Có đủ dữ liệu ứng viên hoặc có phương án dự phòng. |
| Luồng chính | Kết hợp ứng viên từ theo dõi, phổ biến, ngữ nghĩa và cộng tác -> chấm điểm -> điều chỉnh đa dạng -> lấy N kết quả đầu. |
| Kiểm tra và phân quyền | Áp dụng bộ lọc cứng về quyền riêng tư và chặn trước khi trả kết quả. |
| Thay đổi dữ liệu | Lưu Top-N trong Valkey; điểm gợi ý bền vững là tùy chọn. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Khi chưa có dữ liệu dùng nội dung phổ biến hoặc đang theo dõi; khi AI/pgvector lỗi dùng thứ tự thời gian. |

## FED-05 - Cập nhật embedding sở thích

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Tiến trình nền |
| Điều kiện trước | Đã thu thập tương tác của người dùng. |
| Luồng chính | Xử lý theo lô hoặc bất đồng bộ để suy ra vector sở thích từ embedding của nội dung đã tương tác. |
| Kiểm tra và phân quyền | Loại nội dung không thể truy cập hoặc đã xóa; giảm trọng số tín hiệu cũ. |
| Thay đổi dữ liệu | Cập nhật embedding hoặc kho đặc trưng của người dùng. |
| Sự kiện và thời gian thực | EmbeddingGenerated là tùy chọn. |
| Lỗi và trường hợp biên | Áp dụng backpressure và thử lại; không nằm trên đường xử lý đồng bộ của yêu cầu. |

## MED-01 - Tạo phiên tải lên

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Phương tiện |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực. |
| Luồng chính | Kiểm tra siêu dữ liệu khai báo -> sinh khóa đối tượng -> tạo UploadSession -> sinh URL PUT ký trước sống ngắn. |
| Kiểm tra và phân quyền | Chỉ cho phép MIME, kích thước và mục đích hợp lệ; khóa đối tượng do máy chủ sinh. |
| Thay đổi dữ liệu | Thêm bản ghi UploadSession. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Áp dụng giới hạn tần suất; trả 422 khi kích thước, MIME hoặc mục đích không hợp lệ. |

## MED-02 - Tải trực tiếp

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mặt phẳng SeaweedFS |
| Tác nhân chính | Người dùng |
| Điều kiện trước | URL ký trước còn hiệu lực. |
| Luồng chính | Máy khách gửi dữ liệu bằng PUT trực tiếp tới kho đối tượng. |
| Kiểm tra và phân quyền | Kiểm tra chữ ký, TTL và ràng buộc khóa đối tượng. |
| Thay đổi dữ liệu | Chỉ ghi đối tượng vào kho lưu trữ. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Không sử dụng băng thông của backend cho nội dung tệp. |

## MED-03 - Hoàn tất và xác minh tải lên

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Phương tiện |
| Tác nhân chính | Chủ sở hữu |
| Điều kiện trước | UploadSession đang chờ hoàn tất. |
| Luồng chính | Gọi HEAD/stat đối tượng -> xác minh tồn tại, kích thước và loại -> chuyển sang Uploaded -> ghi Outbox. |
| Kiểm tra và phân quyền | Kiểm tra chủ sở hữu và thời hạn phiên; không tin tuyên bố thành công từ máy khách. |
| Thay đổi dữ liệu | Cập nhật upload_session, media_asset và outbox_message. |
| Sự kiện và thời gian thực | MediaUploaded. |
| Lỗi và trường hợp biên | Yêu cầu hoàn tất lặp trả kết quả hiện có; 410 khi UploadSession hết hạn. |

## MED-04 - Xử lý phương tiện

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tiến trình nền Phương tiện |
| Tác nhân chính | Tiến trình nền |
| Điều kiện trước | Đã nhận sự kiện MediaUploaded. |
| Luồng chính | Kiểm tra chữ ký tệp -> tùy chọn đổi kích thước ảnh và loại siêu dữ liệu -> chuyển sang Ready hoặc Failed. |
| Kiểm tra và phân quyền | Giới hạn số tác vụ đồng thời; chỉ thử lại lỗi tạm thời. |
| Thay đổi dữ liệu | Cập nhật MediaAsset. |
| Sự kiện và thời gian thực | MediaReady/Failed. |
| Lỗi và trường hợp biên | Phương tiện không xử lý được -> chuyển DLQ và trạng thái Failed. |

## MED-05 - Xóa và dọn dẹp phương tiện

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Phương tiện |
| Tác nhân chính | Chủ sở hữu/Hệ thống |
| Điều kiện trước | Chính sách tham chiếu cho phép xóa. |
| Luồng chính | Đánh dấu hoặc xóa siêu dữ liệu và đối tượng; nếu cần thì lên lịch dọn dẹp. |
| Kiểm tra và phân quyền | Không xóa Phương tiện còn tham chiếu; dọn đối tượng mồ côi bằng tác vụ TTL. |
| Thay đổi dữ liệu | Cập nhật hoặc xóa media_asset và đối tượng lưu trữ theo chính sách. |
| Sự kiện và thời gian thực | MediaDeleted. |
| Lỗi và trường hợp biên | Lỗi xóa đối tượng được thử lại bất đồng bộ. |

## MED-06 - Phương tiện cho tin nhắn thoại

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Phương tiện và trò chuyện |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Người gọi là thành viên Trò chuyện. |
| Luồng chính | Tải âm thanh qua luồng Phương tiện thông thường; message Trò chuyện chỉ tham chiếu MediaAsset Ready; tác vụ chuyển lời nói thành văn bản là tùy chọn. |
| Kiểm tra và phân quyền | Áp dụng chính sách MIME, kích thước và thời lượng âm thanh. |
| Thay đổi dữ liệu | Phương tiện lưu MediaAsset; Trò chuyện lưu tham chiếu MediaId trong message. |
| Sự kiện và thời gian thực | MediaReady có thể kích hoạt tác vụ chuyển lời nói thành văn bản trong AI và tìm kiếm. |
| Lỗi và trường hợp biên | Lỗi chuyển lời nói thành văn bản không làm mất tin nhắn âm thanh gốc. |

## MKT-01 - Tạo và sửa tin đăng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Người bán |
| Điều kiện trước | Người bán đã xác thực. |
| Luồng chính | Tạo hoặc cập nhật listing với tham chiếu Phương tiện, giá, trạng thái và version. |
| Kiểm tra và phân quyền | Giá > 0; kiểm tra chủ sở hữu; Phương tiện ở Ready; kiểm tra version lạc quan. |
| Thay đổi dữ liệu | Thêm hoặc cập nhật listing, listing_media_ref và outbox_message. |
| Sự kiện và thời gian thực | ListingCreated/Updated. |
| Lỗi và trường hợp biên | 409 khi version xung đột; 422 khi giá hoặc Phương tiện không hợp lệ. |

## MKT-02 - Duyệt và tìm kiếm tin đăng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Người dùng/Khách theo chính sách |
| Điều kiện trước | Tin đăng đang hoạt động tồn tại. |
| Luồng chính | Truy vấn bằng cursor và bộ lọc; dùng PostgreSQL FTS làm cơ sở hoặc OpenSearch khi được bật. |
| Kiểm tra và phân quyền | Không trả tin đăng không hoạt động hoặc không được phép xem. |
| Thay đổi dữ liệu | Không ghi dữ liệu. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Khi phân hệ tìm kiếm lỗi, dùng truy vấn DB dự phòng nếu khả thi. |

## MKT-03 - Cập nhật và giữ tồn kho

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Người bán/Hệ thống |
| Điều kiện trước | Tin đăng đang hoạt động. |
| Luồng chính | Người bán điều chỉnh tồn kho; bước thanh toán giữ số lượng bằng thao tác nguyên tử. |
| Kiểm tra và phân quyền | quantity >= 0; ngăn bán vượt tồn bằng giao dịch, version hoặc khóa dòng theo thiết kế đã chọn. |
| Thay đổi dữ liệu | Cập nhật inventory/version. |
| Sự kiện và thời gian thực | InventoryReserved/Released tùy chọn. |
| Lỗi và trường hợp biên | Xung đột tồn kho trả trạng thái hết hàng; yêu cầu thử lại không được giữ hàng hai lần. |

## MKT-04 - Tạo đơn hàng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Người mua |
| Điều kiện trước | Mặt hàng đang hoạt động và số lượng hợp lệ. |
| Luồng chính | Tạo bản chụp đơn hàng -> giữ tồn kho -> chuyển sang AwaitingPayment. |
| Kiểm tra và phân quyền | Áp dụng chính sách người mua/người bán nếu cần; chụp giá và dùng idempotency key. |
| Thay đổi dữ liệu | Thêm order, order_item, order_status_history và cập nhật inventory trong giao dịch. |
| Sự kiện và thời gian thực | OrderCreated. |
| Lỗi và trường hợp biên | Giữ tồn kho thất bại -> chuyển Cancelled và không để lại đơn hàng dở dang. |

## MKT-05 - Thanh toán giả lập

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Người mua |
| Điều kiện trước | Đơn hàng ở trạng thái AwaitingPayment. |
| Luồng chính | Gọi MockPaymentProvider -> lưu kết quả lặp an toàn -> xác nhận hoặc thực hiện bù trừ. |
| Kiểm tra và phân quyền | Idempotency-Key phải duy nhất; số tiền phải khớp đơn hàng. |
| Thay đổi dữ liệu | Thêm payment, cập nhật order và thực hiện bù trừ inventory khi thanh toán thất bại. |
| Sự kiện và thời gian thực | PaymentSucceeded/Failed. |
| Lỗi và trường hợp biên | Yêu cầu lặp trả cùng kết quả. |

## MKT-06 - Trạng thái đơn hàng và Saga đơn giản hóa

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Thương mại |
| Tác nhân chính | Hệ thống |
| Điều kiện trước | Trạng thái hiện tại hợp lệ. |
| Luồng chính | Áp dụng máy trạng thái: Pending, AwaitingPayment, Paid, Processing, Completed và Cancelled. |
| Kiểm tra và phân quyền | Từ chối chuyển trạng thái không hợp lệ. |
| Thay đổi dữ liệu | Cập nhật order và thêm order_status_history. |
| Sự kiện và thời gian thực | OrderStatusChanged. |
| Lỗi và trường hợp biên | Bù trừ giải phóng tồn kho đã giữ khi thất bại hoặc hủy. |

## MKT-07 - Phương tiện của tin đăng

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Commerce + Phương tiện |
| Tác nhân chính | Người bán |
| Điều kiện trước | Phương tiện ở trạng thái Ready. |
| Luồng chính | Lưu tham chiếu MediaId trong listing; không sao chép dữ liệu nhị phân. |
| Kiểm tra và phân quyền | Kiểm tra chủ sở hữu và mục đích sử dụng. |
| Thay đổi dữ liệu | Chỉ thêm hoặc xóa listing_media_ref. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Xóa listing không xóa ngay Phương tiện dùng chung; chỉ dọn khi không còn tham chiếu. |

## AI-01 - Tạo embedding

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Tiến trình nền |
| Điều kiện trước | Có thực thể nguồn hoặc sự kiện nguồn. |
| Luồng chính | Chuẩn hóa văn bản đã cấp quyền -> gọi mô hình embedding qua bộ chuyển đổi Ollama -> lưu vector cùng tên mô hình và phiên bản. |
| Kiểm tra và phân quyền | Giới hạn đầu vào; loại trường không hỗ trợ hoặc riêng tư; xử lý lặp an toàn theo thực thể và phiên bản mô hình. |
| Thay đổi dữ liệu | Upsert ai_embedding và cập nhật ai_job. |
| Sự kiện và thời gian thực | EmbeddingGenerated là tùy chọn. |
| Lỗi và trường hợp biên | Thử lại lỗi tạm thời; lỗi mô hình hoặc đầu vào kéo dài được chuyển DLQ. |

## AI-02 - Tìm kiếm ngữ nghĩa

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác định phạm vi tìm kiếm. |
| Luồng chính | Tạo embedding cho truy vấn -> tính độ tương đồng bằng pgvector -> lọc theo phạm vi được cấp quyền -> trả tham chiếu và đoạn trích đã xếp hạng. |
| Kiểm tra và phân quyền | Bắt buộc lọc theo quyền trước khi hiển thị dữ liệu. |
| Thay đổi dữ liệu | Không ghi dữ liệu ngoài chỉ số và bộ nhớ đệm. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Dùng PostgreSQL FTS dự phòng khi runtime embedding không sẵn sàng. |

## AI-03 - Trợ lý RAG

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực và có quyền truy cập phạm vi nguồn được yêu cầu. |
| Luồng chính | Truy xuất các chunk đã cấp quyền -> tạo prompt -> gọi Ollama -> truyền phản hồi tăng dần qua SignalR hoặc luồng HTTP. |
| Kiểm tra và phân quyền | Giới hạn prompt/ngữ cảnh, kiểm tra quyền và giới hạn tần suất AI. |
| Thay đổi dữ liệu | Có thể lưu nhật ký yêu cầu/hội thoại nhưng không lưu nội dung nhạy cảm. |
| Sự kiện và thời gian thực | SignalR AiToken/AiCompleted. |
| Lỗi và trường hợp biên | Khi AI không sẵn sàng, trả thông báo suy giảm; không làm lỗi chức năng cốt lõi. |

## AI-04 - Tóm tắt tin nhắn hoặc kênh

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm + trò chuyện |
| Tác nhân chính | Thành viên hội thoại |
| Điều kiện trước | Trò chuyện đã cấp quyền cho khoảng nội dung được yêu cầu. |
| Luồng chính | Trò chuyện cung cấp nội dung đã giới hạn hoặc hợp đồng xuất dữ liệu -> AI tóm tắt -> trả kết quả. |
| Kiểm tra và phân quyền | AI không được truy vấn trực tiếp chat_db; Trò chuyện phải kiểm tra tư cách thành viên. |
| Thay đổi dữ liệu | Có thể lưu ai_summary kèm phạm vi nguồn và phiên bản mô hình. |
| Sự kiện và thời gian thực | AiSummaryReady là tùy chọn. |
| Lỗi và trường hợp biên | Chia nhỏ lịch sử dài; tuân theo quy tắc tin nhắn đã xóa và riêng tư. |

## AI-05 - Chuyển lời nói thành văn bản

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Tiến trình nền/Người dùng |
| Điều kiện trước | Âm thanh đã MediaReady và có yêu cầu chuyển lời nói thành văn bản. |
| Luồng chính | Tiến trình nền tải đối tượng đã cấp quyền -> xử lý bằng whisper.cpp -> lưu bản chép lời -> phát sự kiện cho Trò chuyện. |
| Kiểm tra và phân quyền | Kiểm tra kích thước, thời lượng, ngôn ngữ và giới hạn số tiến trình xử lý đồng thời. |
| Thay đổi dữ liệu | Cập nhật ai_job và siêu dữ liệu transcript. |
| Sự kiện và thời gian thực | TranscriptReady. |
| Lỗi và trường hợp biên | Khi thất bại, âm thanh gốc vẫn dùng được; áp dụng thử lại hoặc DLQ. |

## AI-06 - Đánh chỉ mục OpenSearch - tùy chọn

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | AI và tìm kiếm |
| Tác nhân chính | Bộ nhận sự kiện Kafka |
| Điều kiện trước | Cấu hình OpenSearch được bật. |
| Luồng chính | Nhận sự kiện Post, Listing và User -> cập nhật chỉ mục lặp an toàn; hỗ trợ bù dữ liệu theo lô và điểm kiểm tra. |
| Kiểm tra và phân quyền | Chỉ đánh chỉ mục các trường được phép tìm kiếm. |
| Thay đổi dữ liệu | Cập nhật bản chiếu và điểm kiểm tra của OpenSearch. |
| Sự kiện và thời gian thực | Không có. |
| Lỗi và trường hợp biên | Khi OpenSearch bị tắt, PostgreSQL FTS vẫn là phương án cơ sở. |

## ACC-11 - Yêu cầu xóa và khôi phục tài khoản

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Tài khoản |
| Tác nhân chính | Người dùng hoặc quản trị viên có lý do được kiểm toán |
| Điều kiện trước | Đã xác thực; thao tác tự xóa yêu cầu xác thực lại gần đây. |
| Luồng chính | Tạo account_deletion_request -> đặt account.status=pending_deletion -> thu hồi mọi refresh token -> phát UserDeletionRequested -> các dịch vụ ẩn dữ liệu và xác nhận -> sau 30 ngày tiến trình purge xóa/ẩn danh dữ liệu -> phát UserDeletionCompleted. |
| Hủy yêu cầu | Trong thời gian ân hạn, người dùng xác thực lại và gọi điểm cuối cancel; dịch vụ phát UserDeletionCancelled và khôi phục các projection có thể khôi phục. |
| Kiểm tra và phân quyền | Chỉ self/admin; id từ claim; rate limit; audit bắt buộc; không cho hủy sau khi purge bắt đầu. |
| Thay đổi dữ liệu | account, refresh_token, account_deletion_request; downstream xóa projection, media không còn tham chiếu và dữ liệu AI dẫn xuất. |
| Lỗi và trường hợp biên | Yêu cầu lặp trả trạng thái hiện tại; thiếu xác nhận dịch vụ không chặn ẩn tài khoản nhưng chặn completed và phát cảnh báo. |

## MOD-01 - Gửi báo cáo vi phạm

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội - khối điều hành |
| Tác nhân chính | Người dùng |
| Điều kiện trước | Đã xác thực và có quyền nhìn thấy target tại thời điểm báo cáo. |
| Luồng chính | Xác minh target qua contract/projection -> kiểm tra giới hạn -> tạo content_report và evidence tối thiểu -> Outbox ContentReported -> trả mã báo cáo. |
| Kiểm tra và phân quyền | Không tin target owner từ client; reason_code whitelist; giới hạn theo user/IP/target; chống report trùng đang mở. |
| Lỗi và trường hợp biên | Target không tồn tại/không được thấy trả 404; vượt giới hạn trả 429; retry với Idempotency-Key không tạo bản ghi trùng. |

## MOD-02 - Duyệt hàng đợi báo cáo

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội - khối điều hành |
| Tác nhân chính | Người điều hành hoặc quản trị viên |
| Điều kiện trước | Có global_role hoặc quyền điều hành cộng đồng phù hợp. |
| Luồng chính | Lọc theo status/priority/type -> lấy bằng con trỏ -> kiểm tra phạm vi -> trả dữ liệu đã che trường nhạy cảm -> ghi audit truy cập. |
| Kiểm tra và phân quyền | Người điều hành cộng đồng chỉ thấy target thuộc cộng đồng mình; không trả object_key bằng chứng nếu chưa có quyền xem. |
| Lỗi và trường hợp biên | Người dùng thường trả 403; target đã xóa vẫn hiển thị metadata/bằng chứng tối thiểu theo retention. |

## MOD-03 - Áp dụng hành động điều hành

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội điều phối; dịch vụ nguồn áp dụng |
| Tác nhân chính | Người điều hành |
| Điều kiện trước | Báo cáo InReview, người thực hiện có quyền và If-Match còn đúng. |
| Luồng chính | Ghi moderation_action bất biến + Outbox ModerationActionRequested -> dịch vụ nguồn kiểm tra/áp dụng lặp an toàn -> phát Completed hoặc Rejected -> cập nhật report. |
| Kiểm tra và phân quyền | Không được điều hành đối tượng có thứ bậc cao hơn; action_type theo target_type; reason bắt buộc; hành động tạm thời có expires_at. |
| Lỗi và trường hợp biên | Event giao lặp không áp dụng hai lần; dịch vụ nguồn từ chối giữ báo cáo InReview và ghi lý do; timeout được cảnh báo. |

## MOD-04 - Đóng báo cáo và kiểm toán

| Trường | Đặc tả |
| --- | --- |
| Dịch vụ sở hữu | Mạng xã hội - khối điều hành |
| Tác nhân chính | Người điều hành |
| Điều kiện trước | Không còn hành động ở trạng thái chờ. |
| Luồng chính | Ghi kết luận -> chuyển Closed/Rejected -> đặt thời hạn evidence -> tạo thông báo phù hợp cho người báo cáo mà không lộ thông tin nội bộ. |
| Kiểm tra và phân quyền | If-Match; audit append-only; chỉ admin đặc biệt được reopen và phải nêu lý do. |
| Lỗi và trường hợp biên | Đóng lặp trả trạng thái hiện tại; không xóa audit khi target hoặc account bị xóa. |
