# Ma trận truy vết triển khai

## Tài khoản

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| ACC-01 | POST /auth/register | account, profile, outbox | UserRegistered | Email/username duy nhất; băm mật khẩu; rate limit | Đăng ký thành công, trùng, dữ liệu sai, Outbox | P0 |
| ACC-02 | POST /auth/login | refresh_token | Không bắt buộc | Rate limit; tài khoản active; không lộ email tồn tại | Sai mật khẩu, khóa tạm, token claims | P0 |
| ACC-03 | POST /auth/refresh | refresh_token family | Audit tùy chọn | Xoay một lần; phát hiện tái sử dụng; giao dịch | Token cũ, token hết hạn, race refresh | P0 |
| ACC-04 | POST /auth/logout | refresh_token | Không bắt buộc | Đúng chủ sở hữu; lặp an toàn | Đăng xuất lặp; token đã thu hồi | P0 |
| ACC-05 | GET/PATCH /users | profile | UserProfileUpdated | Quyền riêng tư; If-Match | Ẩn hồ sơ; cập nhật stale trả 412 | P0 |
| ACC-06 | PATCH /users/me/avatar | profile | UserAvatarUpdated | MediaReady; quyền sử dụng; If-Match | Media chưa sẵn sàng; ảnh không thuộc quyền | P1 |
| ACC-07 | PATCH /users/me/settings | account_setting | Sự kiện khi cần | Chỉ self/admin; whitelist | Enum sai; mass assignment | P0 |
| ACC-08 | POST /auth/forgot-password | password_reset_token | PasswordResetRequested | Phản hồi chung; OTP băm; rate limit | Email tồn tại/không tồn tại giống nhau; SMTP lỗi | P1 |
| ACC-09 | POST /auth/reset-password | account, reset token, refresh token | UserPasswordReset | OTP một lần; số lần thử; password policy | OTP sai/hết hạn; thu hồi mọi phiên | P1 |
| ACC-10 | POST /auth/google | account_oauth, account, profile | UserRegistered nếu mới | issuer/audience/signature; không tự gộp tài khoản | Token Google sai; email trùng | P1 |
| ACC-11 | DELETE /users/me; cancel | account_deletion_request | UserDeletionRequested/Cancelled/Completed | Xác thực lại; grace period; audit | Ẩn nhanh; hủy; purge lặp; thiếu ack | P1 |

## Mạng xã hội

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| SOC-01 | POST/DELETE /users/{id}/follow | follow | UserFollowed/Unfollowed | Cấm self; chặn hai chiều; unique | Theo dõi lặp; blocked | P0 |
| SOC-02 | POST/DELETE /users/{id}/block | block, follow | UserBlocked/Unblocked | Cấm self; dọn follow; lặp an toàn | Block race; visibility sau block | P0 |
| SOC-03 | POST /posts | post, media_ref, outbox | PostCreated | Nội dung; quyền media; Idempotency-Key | Create lặp; media sai; Kafka down | P0 |
| SOC-04 | PATCH /posts/{id} | post | PostUpdated | Owner; If-Match; sanitize | Stale trả 412; không phải owner | P0 |
| SOC-05 | DELETE /posts/{id} | post | PostDeleted | Owner/moderator; soft delete; lặp an toàn | Xóa lặp; projection được dọn | P0 |
| SOC-06 | GET /posts; /users/{id}/posts | post | Không | Visibility + block; cursor ổn định | Ẩn nội dung; cursor không trùng/bỏ | P0 |
| SOC-07 | POST /posts/{id}/comments | comment | CommentCreated | Parent cùng bài; độ sâu; rate limit | Parent sai; private/blocked | P0 |
| SOC-08 | PUT/DELETE reaction | reaction | ReactionAdded/Removed | Unique; visibility; upsert | Race cùng user; bộ đếm đúng | P0 |
| SOC-09 | POST /posts type=video | post, media_ref | PostCreated, PostUpdated | Media pipeline; owner-only khi processing | Ready/Failed; không vào bảng tin sớm | P1 |
| SOC-10 | POST /posts/{id}/share | post_share | PostShared | Visibility; link an toàn | Nền tảng lạ; copy-link fallback | P1 |

## Cộng đồng và RTC

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| COM-01 | POST/PATCH /communities | community, member, role, channel | CommunityCreated/Updated | Owner; If-Match; transaction | Tạo mặc định; slug trùng; stale | P1 |
| COM-02 | invite/join/leave | invite, community_member | MemberJoined/LeftCommunity | Hết hạn; max uses; ban; transfer owner | Invite hết; join lặp; owner leave | P1 |
| COM-03 | roles/member roles | role, member_role | RoleUpdated/PermissionUpdated | Không leo quyền; owner protected | Escalation bị chặn; cache invalidation | P1 |
| COM-04 | POST /communities/{id}/channels | channel, outbox | ChannelCreated | ManageChannel; type-specific | Projection Trò chuyện eventual | P1 |
| COM-05 | POST member moderation | community_member | MemberModerated | Role hierarchy; audit | Mute/kick/ban; target cao hơn | P1 |
| RTC-01 | POST /channels/{id}/rtc-token | room metadata tùy chọn | Lifecycle tùy chọn | Identity từ claims; quyền Join/Speak/Screen | Không member; LiveKit down | P1 |
| RTC-02 | LiveKit SDK | Không lưu media | Lifecycle | Token scoped; track permissions | RTC lỗi không hỏng text chat | P1 |
| RTC-03 | LiveKit screen track | Session metadata tùy chọn | StreamStarted/Ended tùy chọn | ScreenShare permission; giới hạn tài nguyên | Mạng yếu; giới hạn room | P1 |

## Trò chuyện và thời gian thực

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| CHT-01 | POST /conversations | conversation, members | ConversationCreated tùy chọn | Block policy; participant limits | DM trùng; member sai | P0 |
| CHT-02 | SignalR/POST messages | message, outbox | MessageSent + MessageCreated | Membership; clientMessageId; rate limit | Gửi lặp; DB fail không ghost | P0 |
| CHT-03 | PATCH/DELETE /messages/{id} | message | MessageEdited/Deleted | Sender/moderator; If-Match | Stale 412; soft delete | P0 |
| CHT-04 | PUT/DELETE message reaction | message_reaction | SignalR ReactionChanged | Membership; unique; rate limit | Thêm/xóa lặp | P0 |
| CHT-05 | SignalR Typing | Valkey TTL tùy chọn | TypingChanged | Membership; throttle; ephemeral | Drop khi offline; auto-expire | P0 |
| CHT-06 | SignalR connect/disconnect | Valkey presence | PresenceChanged | Nhiều thiết bị; privacy | Disconnect bất thường; TTL | P0 |
| CHT-07 | POST read / MarkRead | conversation_member | ReadUpdated | Cursor chỉ tăng; membership | Không lùi; message sai | P0 |
| CHT-08 | GET/PATCH notifications | notification, inbox | NotificationCreated/Read | Recipient filter; EventId unique | Event lặp; SignalR offline | P0 |
| CHT-09 | POST call-invites | call invite metadata | CallInvite/CallStateChanged | Membership/block/privacy; timeout | Reject/timeout không rò resource | P1 |

## Bảng tin và gợi ý

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| FED-01 | Kafka consumer | feed_entry, summaries, inbox | Nhận Post/Follow/Profile | Idempotency; privacy/block | Duplicate; rebuild; lag | P0 |
| FED-02 | GET /feed | feed_db, Valkey | Không | Cursor ổn định; hard filter | Cache miss; không lộ private | P0 |
| FED-03 | Kafka consumer | summaries, cache | Nhận update/delete | Event version; invalidation | Out-of-order; avatar update | P0 |
| FED-04 | GET /feed nội bộ | recommendation cache | Không | Privacy trước trả; diversity | Cold start; AI down fallback | P2 |
| FED-05 | Background worker | interest embedding | EmbeddingGenerated tùy chọn | Loại dữ liệu không còn quyền; decay | Backpressure; retry | P2 |

## Phương tiện

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| MED-01 | POST /media/uploads | upload_session | Không | MIME/size/purpose; key server sinh | Sai loại/kích thước; rate limit | P1 |
| MED-02 | PUT URL ký trước | Object storage | Không | Signature, TTL, key constraints | Hết hạn; backend không nhận bytes | P1 |
| MED-03 | POST complete | session, media_asset, outbox | MediaUploaded | HEAD/stat; owner; Idempotency-Key | Claim giả; complete lặp | P1 |
| MED-04 | Worker | media_asset | MediaReady/Failed | Magic bytes; bounded concurrency | Poison media; retry/DLQ | P1 |
| MED-05 | DELETE /media/{id}; cleanup | media_asset, object | MediaDeleted | Reference policy; orphan TTL | Delete object fail; retry | P1 |
| MED-06 | Media flow + Chat ref | media_asset + message ref | MediaReady; TranscriptReady tùy chọn | Chat membership; duration | Transcription fail không xóa audio | P1 |

## Thương mại

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| MKT-01 | POST/PATCH /listings | listing, media_ref | ListingCreated/Updated | Seller owner; price; If-Match | Stale 412; media sai | P2 |
| MKT-02 | GET /listings | listing | Không | Active filter; cursor | Search down -> DB fallback | P2 |
| MKT-03 | PUT inventory; checkout | inventory | Reserved/Released | Atomic update/row lock; non-negative | Hai buyer không oversell | P2 |
| MKT-04 | POST /orders | order, items, inventory | OrderCreated | Idempotency-Key; price snapshot | Stock fail không ghost order | P2 |
| MKT-05 | POST /orders/{id}/pay | payment, order | PaymentSucceeded/Failed | Idempotency-Key; amount match | Retry trả cùng kết quả | P2 |
| MKT-06 | State transition/cancel | order, status_history | OrderStatusChanged | Transition whitelist; compensation | Invalid transition; release once | P2 |
| MKT-07 | Listing media refs | listing_media_ref | Không | MediaReady; ownership/purpose | Shared media không bị xóa sớm | P2 |

## AI và tìm kiếm

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| AI-01 | Worker/event | ai_embedding, ai_job | EmbeddingGenerated | Authorized text; model version; max input | Retry/DLQ; upsert idempotent | P2 |
| AI-02 | GET /search/semantic | pgvector | Không | Authorization trước exposure | AI down -> FTS; private filter | P2 |
| AI-03 | POST /ai/ask | chunks, request metadata | AiToken/AiCompleted | Scoped retrieval; prompt limit; rate limit | Prompt injection; AI down | P2 |
| AI-04 | POST /ai/summaries | summary tùy chọn | AiSummaryReady | Trò chuyện cấp nội dung; không query chat_db | Large chunk; deleted messages | P2 |
| AI-05 | POST transcriptions/worker | ai_job, transcript | TranscriptReady | Authorized object; duration; concurrency | Fail giữ audio; retry/DLQ | P2 |
| AI-06 | Kafka consumer | OpenSearch projection | Không | Chỉ searchable fields; checkpoint | Disabled -> PostgreSQL | P2 |

## Báo cáo và điều hành nội dung

| Mã | Hợp đồng vào | Dữ liệu chính | Sự kiện / thời gian thực | Kiểm soát bắt buộc | Kiểm thử tối thiểu | Ưu tiên |
| --- | --- | --- | --- | --- | --- | --- |
| MOD-01 | POST /reports | content_report, evidence | ContentReported | Target visible; rate limit; dedupe | Target sai; report spam; snapshot tối thiểu | P1 |
| MOD-02 | GET /moderation/reports | content_report | Không | Moderator role; field masking | Người thường bị 403; cursor/filter | P1 |
| MOD-03 | POST /reports/{id}/actions | moderation_action, outbox | ModerationActionRequested | Role/hierarchy; reason; append-only | Action lặp; target service reject | P1 |
| MOD-04 | POST /reports/{id}/close | content_report | Completed/Rejected | If-Match; audit; evidence retention | Close stale; reopen policy | P1 |
