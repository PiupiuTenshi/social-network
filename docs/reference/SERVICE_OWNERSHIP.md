# Ma trận sở hữu dịch vụ và dữ liệu

| Dịch vụ | Thực thể sở hữu | Kho dữ liệu | Sự kiện chính |
| --- | --- | --- | --- |
| Tài khoản | Account, Profile, RefreshToken, AccountSetting, PasswordResetToken, AccountOAuth, AccountDeletionRequest | account_db | UserRegistered, UserProfileUpdated, UserAvatarUpdated, PasswordResetRequested, UserPasswordReset, UserDeletionRequested/Cancelled/Completed |
| Mạng xã hội | Follow, Block, Post, Comment, Reaction, PostMediaRef, PostShare, ContentReport, ModerationEvidence, ModerationAction | social_db | UserFollowed/Unfollowed, UserBlocked/Unblocked, PostCreated/Updated/Deleted, CommentCreated, ReactionAdded/Removed, PostShared, ContentReported, ModerationActionRequested/Completed/Rejected |
| Cộng đồng | Community, CommunityMember, Role, MemberRole, Channel, Invite | community_db | CommunityCreated/Updated, MemberJoined/LeftCommunity, ChannelCreated, RoleUpdated, PermissionUpdated, MemberModerated |
| Trò chuyện | Conversation, ConversationMember, Message, MessageReaction, Notification | chat_db | ConversationCreated, MessageSent/Edited/Deleted, NotificationRead |
| Bảng tin | FeedEntry, FeedUserSummary, FeedPostSummary | feed_db | Chủ yếu nhận sự kiện; có thể phát RecommendationSnapshotUpdated khi cần |
| Phương tiện | UploadSession, MediaAsset | media_db | MediaUploaded, MediaReady, MediaFailed, MediaDeleted |
| Thương mại | Listing, ListingMediaRef, Inventory, Order, OrderItem, Payment, OrderStatusHistory | commerce_db | ListingCreated/Updated, InventoryReserved/Released, OrderCreated, PaymentSucceeded/Failed, OrderStatusChanged |
| AI và tìm kiếm | AiEmbedding, AiChunk, AiJob, transcript metadata | ai_db + pgvector | EmbeddingGenerated, AiSummaryReady, TranscriptReady |
