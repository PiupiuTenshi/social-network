# Danh mục sự kiện Kafka

| Sự kiện | Bên phát | Bên nhận | Khóa phân vùng | Phiên bản |
| --- | --- | --- | --- | --- |
| UserRegistered | Tài khoản | Mạng xã hội, Bảng tin, Trò chuyện, AI và tìm kiếm | UserId | v1 |
| UserProfileUpdated | Tài khoản | Bảng tin, Trò chuyện | UserId | v1 |
| UserAvatarUpdated | Tài khoản | Bảng tin, Trò chuyện | UserId | v1 |
| PasswordResetRequested | Tài khoản | Tiến trình gửi email và nhật ký kiểm toán | AccountId | v1 |
| UserPasswordReset | Tài khoản | Nhật ký bảo mật; bộ nhận sự kiện tùy chọn | AccountId | v1 |
| UserDeletionRequested | Tài khoản | Mạng xã hội, Bảng tin, Trò chuyện, Cộng đồng, Phương tiện, Thương mại, AI và tìm kiếm | AccountId | v1 |
| UserDeletionCancelled | Tài khoản | Các dịch vụ đã nhận yêu cầu xóa | AccountId | v1 |
| UserDeletionCompleted | Tài khoản | Nhật ký kiểm toán và dịch vụ cần xóa bản chiếu cuối | AccountId | v1 |
| UserFollowed | Mạng xã hội | Bảng tin, Trò chuyện | FollowerId | v1 |
| UserUnfollowed | Mạng xã hội | Bảng tin, Trò chuyện | FollowerId | v1 |
| UserBlocked | Mạng xã hội | Bảng tin, Trò chuyện | BlockerId | v1 |
| UserUnblocked | Mạng xã hội | Bảng tin, Trò chuyện | BlockerId | v1 |
| PostCreated | Mạng xã hội | Bảng tin, AI và tìm kiếm | PostId | v1 |
| PostUpdated | Mạng xã hội | Bảng tin, AI và tìm kiếm | PostId | v1 |
| PostDeleted | Mạng xã hội | Bảng tin, AI và tìm kiếm | PostId | v1 |
| CommentCreated | Mạng xã hội | Trò chuyện tạo thông báo | PostId | v1 |
| ReactionAdded | Mạng xã hội | Trò chuyện tạo thông báo; Bảng tin cập nhật bộ đếm | PostId | v1 |
| ReactionRemoved | Mạng xã hội | Bảng tin cập nhật bộ đếm; Trò chuyện tùy chọn | PostId | v1 |
| PostShared | Mạng xã hội | Bảng tin dùng tùy chọn cho xếp hạng | PostId | v1 |
| ContentReported | Mạng xã hội | Hàng đợi điều hành và Trò chuyện tạo thông báo nội bộ | ReportId | v1 |
| ModerationActionRequested | Mạng xã hội | Dịch vụ sở hữu target_type | TargetId | v1 |
| ModerationActionCompleted | Dịch vụ sở hữu nội dung | Mạng xã hội và Trò chuyện | ReportId | v1 |
| ModerationActionRejected | Dịch vụ sở hữu nội dung | Mạng xã hội và Trò chuyện | ReportId | v1 |
| CommunityCreated | Cộng đồng | Trò chuyện tạo bản chiếu | CommunityId | v1 |
| CommunityUpdated | Cộng đồng | Trò chuyện cập nhật bản chiếu | CommunityId | v1 |
| MemberJoined | Cộng đồng | Trò chuyện cập nhật bản chiếu | CommunityId | v1 |
| MemberLeftCommunity | Cộng đồng | Trò chuyện cập nhật bản chiếu | CommunityId | v1 |
| ChannelCreated | Cộng đồng | Trò chuyện tạo bản chiếu | ChannelId | v1 |
| RoleUpdated | Cộng đồng | Trò chuyện cập nhật quyền cục bộ | CommunityId | v1 |
| PermissionUpdated | Cộng đồng | Trò chuyện cập nhật quyền cục bộ | CommunityId | v1 |
| MemberModerated | Cộng đồng | Trò chuyện tạo thông báo hoặc cập nhật quyền | CommunityId | v1 |
| ConversationCreated | Trò chuyện | Bộ nhận sự kiện phân tích tùy chọn | ConversationId | v1 |
| MessageSent | Trò chuyện | AI và tìm kiếm tùy chọn; thông báo/phân tích | ConversationId | v1 |
| MessageEdited | Trò chuyện | AI và tìm kiếm cập nhật dữ liệu dẫn xuất tùy chọn | ConversationId | v1 |
| MessageDeleted | Trò chuyện | AI và tìm kiếm xóa hoặc ẩn dữ liệu dẫn xuất | ConversationId | v1 |
| MediaUploaded | Phương tiện | Tiến trình xử lý phương tiện | MediaId | v1 |
| MediaReady | Phương tiện | Mạng xã hội, Thương mại hoặc Trò chuyện theo tham chiếu | MediaId | v1 |
| MediaFailed | Phương tiện | Dịch vụ tham chiếu phương tiện và hộp thông báo | MediaId | v1 |
| MediaDeleted | Phương tiện | Dịch vụ giữ tham chiếu và AI và tìm kiếm | MediaId | v1 |
| ListingCreated | Thương mại | AI và tìm kiếm tùy chọn | ListingId | v1 |
| ListingUpdated | Thương mại | AI và tìm kiếm tùy chọn | ListingId | v1 |
| InventoryReserved | Thương mại | Quy trình nội bộ | ListingId | v1 |
| InventoryReleased | Thương mại | Quy trình nội bộ | ListingId | v1 |
| OrderCreated | Thương mại | Quy trình nội bộ và Trò chuyện tạo thông báo tùy chọn | OrderId | v1 |
| PaymentSucceeded | Thương mại | Quy trình nội bộ và Trò chuyện tạo thông báo | OrderId | v1 |
| PaymentFailed | Thương mại | Quy trình bù trừ và Trò chuyện tạo thông báo | OrderId | v1 |
| OrderStatusChanged | Thương mại | Quy trình nội bộ và Trò chuyện tạo thông báo | OrderId | v1 |
| EmbeddingGenerated | AI và tìm kiếm | Bộ nhận sự kiện nội bộ tùy chọn | EntityId | v1 |
| AiSummaryReady | AI và tìm kiếm | Trò chuyện | RequestId | v1 |
| TranscriptReady | AI và tìm kiếm | Trò chuyện | MessageId | v1 |

## Vỏ sự kiện và delivery

| Hợp đồng sự kiện Vỏ sự kiện gồm: eventId, eventType, eventVersion, occurredAt, producer, correlationId, aggregateId và trường payload. Bộ nhận sự kiện xử lý theo cơ chế phát ít nhất một lần; cùng một EventId không được tạo tác dụng phụ trùng. |
| --- |
