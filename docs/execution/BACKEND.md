# Danh mục BACKEND

Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.

## PH00 — Khảo sát, quyết định và G0

### PH00-BE-CONTRACT — Khóa hợp đồng P0 và xử lý mâu thuẫn nền

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH00-BE-CONTRACT-01](prompts/PH00-BE-CONTRACT-01.md) | Khóa hợp đồng P0 và xử lý mâu thuẫn nền | PH00-GOV-AUDIT-01 |

### PH00-BE-TOOLCHAIN — Dựng harness kiến trúc và khóa toolchain

Ưu tiên P0; miền building-blocks. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH00-BE-TOOLCHAIN-01](prompts/PH00-BE-TOOLCHAIN-01.md) | Dựng harness kiến trúc và khóa toolchain | PH00-DATA-BOUNDARY-01 |

## PH01 — Nền tảng Backend, Data và Frontend

### PH01-BE-PLATFORM — BuildingBlocks, Gateway và quan sát cơ sở

Ưu tiên P0; miền building-blocks. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH01-BE-PLATFORM-01](prompts/PH01-BE-PLATFORM-01.md) | BuildingBlocks, Gateway và quan sát cơ sở | PH01-DATA-INFRA-01 |

### PH01-BE-CI — CI có kiểm tra bắt buộc và bảo vệ nhánh

Ưu tiên P0; miền deploy. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH01-BE-CI-01](prompts/PH01-BE-CI-01.md) | CI có kiểm tra bắt buộc và bảo vệ nhánh | PH01-BE-PLATFORM-01 |

## PH02 — Tài khoản P0

### PH02-BE-ACC-01 — Đăng ký

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/register. Dữ liệu: account, profile, outbox. Sự kiện: UserRegistered.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-01-01](prompts/PH02-BE-ACC-01-01.md) | Triển khai ACC-01: Đăng ký | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |
| [PH02-BE-ACC-01-02](prompts/PH02-BE-ACC-01-02.md) | Nghiệm thu ACC-01 và bàn giao | PH02-BE-ACC-01-01 |

### PH02-BE-ACC-02 — Đăng nhập

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/login. Dữ liệu: refresh_token. Sự kiện: Không bắt buộc.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-02-01](prompts/PH02-BE-ACC-02-01.md) | Triển khai ACC-02: Đăng nhập | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-01-02 |
| [PH02-BE-ACC-02-02](prompts/PH02-BE-ACC-02-02.md) | Nghiệm thu ACC-02 và bàn giao | PH02-BE-ACC-02-01 |

### PH02-BE-ACC-03 — Xoay vòng refresh token

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/refresh. Dữ liệu: refresh_token family. Sự kiện: Audit tùy chọn.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-03-01](prompts/PH02-BE-ACC-03-01.md) | Triển khai ACC-03: Xoay vòng refresh token | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-02-02 |
| [PH02-BE-ACC-03-02](prompts/PH02-BE-ACC-03-02.md) | Nghiệm thu ACC-03 và bàn giao | PH02-BE-ACC-03-01 |

### PH02-BE-ACC-04 — Đăng xuất

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/logout. Dữ liệu: refresh_token. Sự kiện: Không bắt buộc.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-04-01](prompts/PH02-BE-ACC-04-01.md) | Triển khai ACC-04: Đăng xuất | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-03-02 |
| [PH02-BE-ACC-04-02](prompts/PH02-BE-ACC-04-02.md) | Nghiệm thu ACC-04 và bàn giao | PH02-BE-ACC-04-01 |

### PH02-BE-ACC-05 — Xem và cập nhật hồ sơ

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: GET/PATCH /users. Dữ liệu: profile. Sự kiện: UserProfileUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-05-01](prompts/PH02-BE-ACC-05-01.md) | Triển khai ACC-05: Xem và cập nhật hồ sơ | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-04-02 |
| [PH02-BE-ACC-05-02](prompts/PH02-BE-ACC-05-02.md) | Nghiệm thu ACC-05 và bàn giao | PH02-BE-ACC-05-01 |

### PH02-BE-ACC-07 — Quyền riêng tư và thiết lập tài khoản

Ưu tiên P0; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: PATCH /users/me/settings. Dữ liệu: account_setting. Sự kiện: Sự kiện khi cần.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-BE-ACC-07-01](prompts/PH02-BE-ACC-07-01.md) | Triển khai ACC-07: Quyền riêng tư và thiết lập tài khoản | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-05-02 |
| [PH02-BE-ACC-07-02](prompts/PH02-BE-ACC-07-02.md) | Nghiệm thu ACC-07 và bàn giao | PH02-BE-ACC-07-01 |

## PH03 — Mạng xã hội, Bảng tin, Trò chuyện P0

### PH03-BE-SOC-01 — Theo dõi và bỏ theo dõi

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST/DELETE /users/{id}/follow. Dữ liệu: follow. Sự kiện: UserFollowed/Unfollowed.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-01-01](prompts/PH03-BE-SOC-01-01.md) | Triển khai SOC-01: Theo dõi và bỏ theo dõi | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-02-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-01-02](prompts/PH03-BE-SOC-01-02.md) | Nghiệm thu SOC-01 và bàn giao | PH03-BE-SOC-01-01 |

### PH03-BE-SOC-02 — Chặn và bỏ chặn

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST/DELETE /users/{id}/block. Dữ liệu: block, follow. Sự kiện: UserBlocked/Unblocked.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-02-01](prompts/PH03-BE-SOC-02-01.md) | Triển khai SOC-02: Chặn và bỏ chặn | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-07-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-02-02](prompts/PH03-BE-SOC-02-02.md) | Nghiệm thu SOC-02 và bàn giao | PH03-BE-SOC-02-01 |

### PH03-BE-SOC-03 — Tạo bài viết

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST /posts. Dữ liệu: post, media_ref, outbox. Sự kiện: PostCreated. P0 chỉ nội dung văn bản; từ chối media refs chưa hỗ trợ theo quyết định P0, mở ở P1.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-03-01](prompts/PH03-BE-SOC-03-01.md) | Triển khai SOC-03: Tạo bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-01-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-03-02](prompts/PH03-BE-SOC-03-02.md) | Nghiệm thu SOC-03 và bàn giao | PH03-BE-SOC-03-01 |

### PH03-BE-SOC-04 — Sửa bài viết

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: PATCH /posts/{id}. Dữ liệu: post. Sự kiện: PostUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-04-01](prompts/PH03-BE-SOC-04-01.md) | Triển khai SOC-04: Sửa bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-04-02](prompts/PH03-BE-SOC-04-02.md) | Nghiệm thu SOC-04 và bàn giao | PH03-BE-SOC-04-01 |

### PH03-BE-SOC-05 — Xóa bài viết

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: DELETE /posts/{id}. Dữ liệu: post. Sự kiện: PostDeleted.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-05-01](prompts/PH03-BE-SOC-05-01.md) | Triển khai SOC-05: Xóa bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-04-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-05-02](prompts/PH03-BE-SOC-05-02.md) | Nghiệm thu SOC-05 và bàn giao | PH03-BE-SOC-05-01 |

### PH03-BE-SOC-06 — Xem bài viết và danh sách bài viết

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: GET /posts; /users/{id}/posts. Dữ liệu: post. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-06-01](prompts/PH03-BE-SOC-06-01.md) | Triển khai SOC-06: Xem bài viết và danh sách bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-03-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-06-02](prompts/PH03-BE-SOC-06-02.md) | Nghiệm thu SOC-06 và bàn giao | PH03-BE-SOC-06-01 |

### PH03-BE-SOC-07 — Bình luận và trả lời

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST /posts/{id}/comments. Dữ liệu: comment. Sự kiện: CommentCreated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-07-01](prompts/PH03-BE-SOC-07-01.md) | Triển khai SOC-07: Bình luận và trả lời | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-07-02](prompts/PH03-BE-SOC-07-02.md) | Nghiệm thu SOC-07 và bàn giao | PH03-BE-SOC-07-01 |

### PH03-BE-SOC-08 — Tương tác

Ưu tiên P0; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: PUT/DELETE reaction. Dữ liệu: reaction. Sự kiện: ReactionAdded/Removed.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-SOC-08-01](prompts/PH03-BE-SOC-08-01.md) | Triển khai SOC-08: Tương tác | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-07-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-SOC-08-02](prompts/PH03-BE-SOC-08-02.md) | Nghiệm thu SOC-08 và bàn giao | PH03-BE-SOC-08-01 |

### PH03-BE-CHT-01 — Tạo hội thoại trực tiếp hoặc nhóm

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: POST /conversations. Dữ liệu: conversation, members. Sự kiện: ConversationCreated tùy chọn.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-01-01](prompts/PH03-BE-CHT-01-01.md) | Triển khai CHT-01: Tạo hội thoại trực tiếp hoặc nhóm | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-02-02, PH02-BE-ACC-07-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-01-02](prompts/PH03-BE-CHT-01-02.md) | Nghiệm thu CHT-01 và bàn giao | PH03-BE-CHT-01-01 |

### PH03-BE-CHT-02 — Gửi tin nhắn

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: SignalR/POST messages. Dữ liệu: message, outbox. Sự kiện: MessageSent + MessageCreated. P0 chỉ nội dung văn bản; từ chối media refs chưa hỗ trợ theo quyết định P0, mở ở P1.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-02-01](prompts/PH03-BE-CHT-02-01.md) | Triển khai CHT-02: Gửi tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-02-02](prompts/PH03-BE-CHT-02-02.md) | Nghiệm thu CHT-02 và bàn giao | PH03-BE-CHT-02-01 |

### PH03-BE-CHT-03 — Sửa và xóa tin nhắn

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: PATCH/DELETE /messages/{id}. Dữ liệu: message. Sự kiện: MessageEdited/Deleted.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-03-01](prompts/PH03-BE-CHT-03-01.md) | Triển khai CHT-03: Sửa và xóa tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-03-02](prompts/PH03-BE-CHT-03-02.md) | Nghiệm thu CHT-03 và bàn giao | PH03-BE-CHT-03-01 |

### PH03-BE-CHT-04 — Tương tác với tin nhắn

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: PUT/DELETE message reaction. Dữ liệu: message_reaction. Sự kiện: SignalR ReactionChanged.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-04-01](prompts/PH03-BE-CHT-04-01.md) | Triển khai CHT-04: Tương tác với tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-03-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-04-02](prompts/PH03-BE-CHT-04-02.md) | Nghiệm thu CHT-04 và bàn giao | PH03-BE-CHT-04-01 |

### PH03-BE-CHT-05 — Trạng thái đang nhập

Ưu tiên P0; miền chat. Owner: Trò chuyện/SignalR. Hợp đồng tham chiếu: SignalR Typing. Dữ liệu: Valkey TTL tùy chọn. Sự kiện: TypingChanged.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-05-01](prompts/PH03-BE-CHT-05-01.md) | Triển khai CHT-05: Trạng thái đang nhập | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-05-02](prompts/PH03-BE-CHT-05-02.md) | Nghiệm thu CHT-05 và bàn giao | PH03-BE-CHT-05-01 |

### PH03-BE-CHT-06 — Trạng thái hiện diện

Ưu tiên P0; miền chat. Owner: Trò chuyện/SignalR. Hợp đồng tham chiếu: SignalR connect/disconnect. Dữ liệu: Valkey presence. Sự kiện: PresenceChanged.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-06-01](prompts/PH03-BE-CHT-06-01.md) | Triển khai CHT-06: Trạng thái hiện diện | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-06-02](prompts/PH03-BE-CHT-06-02.md) | Nghiệm thu CHT-06 và bàn giao | PH03-BE-CHT-06-01 |

### PH03-BE-CHT-07 — Xác nhận đã đọc

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: POST read / MarkRead. Dữ liệu: conversation_member. Sự kiện: ReadUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-07-01](prompts/PH03-BE-CHT-07-01.md) | Triển khai CHT-07: Xác nhận đã đọc | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-07-02](prompts/PH03-BE-CHT-07-02.md) | Nghiệm thu CHT-07 và bàn giao | PH03-BE-CHT-07-01 |

### PH03-BE-CHT-08 — Hộp thông báo

Ưu tiên P0; miền chat. Owner: Trò chuyện. Hợp đồng tham chiếu: GET/PATCH notifications. Dữ liệu: notification, inbox. Sự kiện: NotificationCreated/Read.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-CHT-08-01](prompts/PH03-BE-CHT-08-01.md) | Triển khai CHT-08: Hộp thông báo | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-08-02, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-CHT-08-02](prompts/PH03-BE-CHT-08-02.md) | Nghiệm thu CHT-08 và bàn giao | PH03-BE-CHT-08-01 |

### PH03-BE-FED-01 — Xây dựng bản chiếu bảng tin theo dõi

Ưu tiên P0; miền feed. Owner: Bảng tin. Hợp đồng tham chiếu: Kafka consumer. Dữ liệu: feed_entry, summaries, inbox. Sự kiện: Nhận Post/Follow/Profile.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-FED-01-01](prompts/PH03-BE-FED-01-01.md) | Triển khai FED-01: Xây dựng bản chiếu bảng tin theo dõi | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-03-02, PH03-BE-SOC-01-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-FED-01-02](prompts/PH03-BE-FED-01-02.md) | Nghiệm thu FED-01 và bàn giao | PH03-BE-FED-01-01 |

### PH03-BE-FED-02 — Đọc bảng tin bằng con trỏ

Ưu tiên P0; miền feed. Owner: Bảng tin. Hợp đồng tham chiếu: GET /feed. Dữ liệu: feed_db, Valkey. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-FED-02-01](prompts/PH03-BE-FED-02-01.md) | Triển khai FED-02: Đọc bảng tin bằng con trỏ | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-FED-03-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-FED-02-02](prompts/PH03-BE-FED-02-02.md) | Nghiệm thu FED-02 và bàn giao | PH03-BE-FED-02-01 |

### PH03-BE-FED-03 — Cập nhật bản chiếu và làm mất hiệu lực bộ nhớ đệm

Ưu tiên P0; miền feed. Owner: Bảng tin. Hợp đồng tham chiếu: Kafka consumer. Dữ liệu: summaries, cache. Sự kiện: Nhận update/delete.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-BE-FED-03-01](prompts/PH03-BE-FED-03-01.md) | Triển khai FED-03: Cập nhật bản chiếu và làm mất hiệu lực bộ nhớ đệm | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-FED-01-02, PH03-BE-SOC-05-02, PH02-BE-ACC-05-02, PH02-GATE-ACCOUNT-01 |
| [PH03-BE-FED-03-02](prompts/PH03-BE-FED-03-02.md) | Nghiệm thu FED-03 và bàn giao | PH03-BE-FED-03-01 |

## PH04 — Cộng đồng, RTC, Phương tiện và tài khoản P1

### PH04-BE-CONTRACT — Khóa bổ sung hợp đồng P1

Ưu tiên P1; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-CONTRACT-01](prompts/PH04-BE-CONTRACT-01.md) | Khóa bổ sung hợp đồng P1 | G1-01 |

### PH04-BE-ACC-06 — Cập nhật tham chiếu avatar

Ưu tiên P1; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: PATCH /users/me/avatar. Dữ liệu: profile. Sự kiện: UserAvatarUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-ACC-06-01](prompts/PH04-BE-ACC-06-01.md) | Triển khai ACC-06: Cập nhật tham chiếu avatar | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH02-BE-ACC-05-02 |
| [PH04-BE-ACC-06-02](prompts/PH04-BE-ACC-06-02.md) | Nghiệm thu ACC-06 và bàn giao | PH04-BE-ACC-06-01 |

### PH04-BE-ACC-08 — Yêu cầu OTP khôi phục mật khẩu

Ưu tiên P1; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/forgot-password. Dữ liệu: password_reset_token. Sự kiện: PasswordResetRequested.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-ACC-08-01](prompts/PH04-BE-ACC-08-01.md) | Triển khai ACC-08: Yêu cầu OTP khôi phục mật khẩu | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-04-02 |
| [PH04-BE-ACC-08-02](prompts/PH04-BE-ACC-08-02.md) | Nghiệm thu ACC-08 và bàn giao | PH04-BE-ACC-08-01 |

### PH04-BE-ACC-09 — Đặt lại mật khẩu bằng OTP

Ưu tiên P1; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/reset-password. Dữ liệu: account, reset token, refresh token. Sự kiện: UserPasswordReset.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-ACC-09-01](prompts/PH04-BE-ACC-09-01.md) | Triển khai ACC-09: Đặt lại mật khẩu bằng OTP | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-ACC-08-02 |
| [PH04-BE-ACC-09-02](prompts/PH04-BE-ACC-09-02.md) | Nghiệm thu ACC-09 và bàn giao | PH04-BE-ACC-09-01 |

### PH04-BE-ACC-10 — Đăng nhập bằng Google OAuth

Ưu tiên P1; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: POST /auth/google. Dữ liệu: account_oauth, account, profile. Sự kiện: UserRegistered nếu mới.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-ACC-10-01](prompts/PH04-BE-ACC-10-01.md) | Triển khai ACC-10: Đăng nhập bằng Google OAuth | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-03-02 |
| [PH04-BE-ACC-10-02](prompts/PH04-BE-ACC-10-02.md) | Nghiệm thu ACC-10 và bàn giao | PH04-BE-ACC-10-01 |

### PH04-BE-SOC-09 — Tạo bài viết video

Ưu tiên P1; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST /posts type=video. Dữ liệu: post, media_ref. Sự kiện: PostCreated, PostUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-SOC-09-01](prompts/PH04-BE-SOC-09-01.md) | Triển khai SOC-09: Tạo bài viết video | PH04-DATA-SOC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH03-BE-SOC-04-02 |
| [PH04-BE-SOC-09-02](prompts/PH04-BE-SOC-09-02.md) | Nghiệm thu SOC-09 và bàn giao | PH04-BE-SOC-09-01 |

### PH04-BE-SOC-10 — Chia sẻ bài viết ra nền tảng ngoài

Ưu tiên P1; miền social. Owner: Mạng xã hội. Hợp đồng tham chiếu: POST /posts/{id}/share. Dữ liệu: post_share. Sự kiện: PostShared.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-SOC-10-01](prompts/PH04-BE-SOC-10-01.md) | Triển khai SOC-10: Chia sẻ bài viết ra nền tảng ngoài | PH04-DATA-SOC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02 |
| [PH04-BE-SOC-10-02](prompts/PH04-BE-SOC-10-02.md) | Nghiệm thu SOC-10 và bàn giao | PH04-BE-SOC-10-01 |

### PH04-BE-COM-01 — Tạo và cập nhật cộng đồng

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: POST/PATCH /communities. Dữ liệu: community, member, role, channel. Sự kiện: CommunityCreated/Updated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-COM-01-01](prompts/PH04-BE-COM-01-01.md) | Triển khai COM-01: Tạo và cập nhật cộng đồng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |
| [PH04-BE-COM-01-02](prompts/PH04-BE-COM-01-02.md) | Nghiệm thu COM-01 và bàn giao | PH04-BE-COM-01-01 |

### PH04-BE-COM-02 — Mời, tham gia và rời cộng đồng

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: invite/join/leave. Dữ liệu: invite, community_member. Sự kiện: MemberJoined/LeftCommunity.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-COM-02-01](prompts/PH04-BE-COM-02-01.md) | Triển khai COM-02: Mời, tham gia và rời cộng đồng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-01-02 |
| [PH04-BE-COM-02-02](prompts/PH04-BE-COM-02-02.md) | Nghiệm thu COM-02 và bàn giao | PH04-BE-COM-02-01 |

### PH04-BE-COM-03 — Vai trò và quyền

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: roles/member roles. Dữ liệu: role, member_role. Sự kiện: RoleUpdated/PermissionUpdated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-COM-03-01](prompts/PH04-BE-COM-03-01.md) | Triển khai COM-03: Vai trò và quyền | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-02-02 |
| [PH04-BE-COM-03-02](prompts/PH04-BE-COM-03-02.md) | Nghiệm thu COM-03 và bàn giao | PH04-BE-COM-03-01 |

### PH04-BE-COM-04 — Tạo kênh văn bản hoặc kênh thoại

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: POST /communities/{id}/channels. Dữ liệu: channel, outbox. Sự kiện: ChannelCreated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-COM-04-01](prompts/PH04-BE-COM-04-01.md) | Triển khai COM-04: Tạo kênh văn bản hoặc kênh thoại | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-03-02, PH03-BE-CHT-02-02 |
| [PH04-BE-COM-04-02](prompts/PH04-BE-COM-04-02.md) | Nghiệm thu COM-04 và bàn giao | PH04-BE-COM-04-01 |

### PH04-BE-COM-05 — Điều hành thành viên

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: POST member moderation. Dữ liệu: community_member. Sự kiện: MemberModerated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-COM-05-01](prompts/PH04-BE-COM-05-01.md) | Triển khai COM-05: Điều hành thành viên | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-03-02 |
| [PH04-BE-COM-05-02](prompts/PH04-BE-COM-05-02.md) | Nghiệm thu COM-05 và bàn giao | PH04-BE-COM-05-01 |

### PH04-BE-RTC-01 — Cấp token tham gia LiveKit

Ưu tiên P1; miền community. Owner: Cộng đồng. Hợp đồng tham chiếu: POST /channels/{id}/rtc-token. Dữ liệu: room metadata tùy chọn. Sự kiện: Lifecycle tùy chọn.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-RTC-01-01](prompts/PH04-BE-RTC-01-01.md) | Triển khai RTC-01: Cấp token tham gia LiveKit | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-04-02, PH04-BE-COM-05-02 |
| [PH04-BE-RTC-01-02](prompts/PH04-BE-RTC-01-02.md) | Nghiệm thu RTC-01 và bàn giao | PH04-BE-RTC-01-01 |

### PH04-BE-RTC-02 — Thoại, video và chia sẻ màn hình

Ưu tiên P1; miền community. Owner: Mặt phẳng LiveKit. Hợp đồng tham chiếu: LiveKit SDK. Dữ liệu: Không lưu media. Sự kiện: Lifecycle. Task BE kiểm chứng capability/adapter/hạ tầng; bytes/track đi trực tiếp từ client, không tạo endpoint chuyển tiếp media.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-RTC-02-01](prompts/PH04-BE-RTC-02-01.md) | Triển khai RTC-02: Thoại, video và chia sẻ màn hình | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-01-02 |
| [PH04-BE-RTC-02-02](prompts/PH04-BE-RTC-02-02.md) | Nghiệm thu RTC-02 và bàn giao | PH04-BE-RTC-02-01 |

### PH04-BE-RTC-03 — Phát trực tiếp màn hình trong phòng

Ưu tiên P1; miền community. Owner: Mặt phẳng LiveKit. Hợp đồng tham chiếu: LiveKit screen track. Dữ liệu: Session metadata tùy chọn. Sự kiện: StreamStarted/Ended tùy chọn. Task BE kiểm chứng capability/adapter/hạ tầng; bytes/track đi trực tiếp từ client, không tạo endpoint chuyển tiếp media.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-RTC-03-01](prompts/PH04-BE-RTC-03-01.md) | Triển khai RTC-03: Phát trực tiếp màn hình trong phòng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-02-02 |
| [PH04-BE-RTC-03-02](prompts/PH04-BE-RTC-03-02.md) | Nghiệm thu RTC-03 và bàn giao | PH04-BE-RTC-03-01 |

### PH04-BE-CHT-09 — Lời mời cuộc gọi

Ưu tiên P1; miền chat. Owner: Trò chuyện + cộng đồng. Hợp đồng tham chiếu: POST call-invites. Dữ liệu: call invite metadata. Sự kiện: CallInvite/CallStateChanged.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-CHT-09-01](prompts/PH04-BE-CHT-09-01.md) | Triển khai CHT-09: Lời mời cuộc gọi | PH04-DATA-CHT-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-01-02, PH03-BE-CHT-01-02 |
| [PH04-BE-CHT-09-02](prompts/PH04-BE-CHT-09-02.md) | Nghiệm thu CHT-09 và bàn giao | PH04-BE-CHT-09-01 |

### PH04-BE-MED-01 — Tạo phiên tải lên

Ưu tiên P1; miền media. Owner: Phương tiện. Hợp đồng tham chiếu: POST /media/uploads. Dữ liệu: upload_session. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-01-01](prompts/PH04-BE-MED-01-01.md) | Triển khai MED-01: Tạo phiên tải lên | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |
| [PH04-BE-MED-01-02](prompts/PH04-BE-MED-01-02.md) | Nghiệm thu MED-01 và bàn giao | PH04-BE-MED-01-01 |

### PH04-BE-MED-02 — Tải trực tiếp

Ưu tiên P1; miền media. Owner: Mặt phẳng SeaweedFS. Hợp đồng tham chiếu: PUT URL ký trước. Dữ liệu: Object storage. Sự kiện: Không. Task BE kiểm chứng capability/adapter/hạ tầng; bytes/track đi trực tiếp từ client, không tạo endpoint chuyển tiếp media.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-02-01](prompts/PH04-BE-MED-02-01.md) | Triển khai MED-02: Tải trực tiếp | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-01-02 |
| [PH04-BE-MED-02-02](prompts/PH04-BE-MED-02-02.md) | Nghiệm thu MED-02 và bàn giao | PH04-BE-MED-02-01 |

### PH04-BE-MED-03 — Hoàn tất và xác minh tải lên

Ưu tiên P1; miền media. Owner: Phương tiện. Hợp đồng tham chiếu: POST complete. Dữ liệu: session, media_asset, outbox. Sự kiện: MediaUploaded.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-03-01](prompts/PH04-BE-MED-03-01.md) | Triển khai MED-03: Hoàn tất và xác minh tải lên | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-02-02 |
| [PH04-BE-MED-03-02](prompts/PH04-BE-MED-03-02.md) | Nghiệm thu MED-03 và bàn giao | PH04-BE-MED-03-01 |

### PH04-BE-MED-04 — Xử lý phương tiện

Ưu tiên P1; miền media. Owner: Tiến trình nền Phương tiện. Hợp đồng tham chiếu: Worker. Dữ liệu: media_asset. Sự kiện: MediaReady/Failed.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-04-01](prompts/PH04-BE-MED-04-01.md) | Triển khai MED-04: Xử lý phương tiện | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-03-02 |
| [PH04-BE-MED-04-02](prompts/PH04-BE-MED-04-02.md) | Nghiệm thu MED-04 và bàn giao | PH04-BE-MED-04-01 |

### PH04-BE-MED-05 — Xóa và dọn dẹp phương tiện

Ưu tiên P1; miền media. Owner: Phương tiện. Hợp đồng tham chiếu: DELETE /media/{id}; cleanup. Dữ liệu: media_asset, object. Sự kiện: MediaDeleted.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-05-01](prompts/PH04-BE-MED-05-01.md) | Triển khai MED-05: Xóa và dọn dẹp phương tiện | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02 |
| [PH04-BE-MED-05-02](prompts/PH04-BE-MED-05-02.md) | Nghiệm thu MED-05 và bàn giao | PH04-BE-MED-05-01 |

### PH04-BE-MED-06 — Phương tiện cho tin nhắn thoại

Ưu tiên P1; miền media. Owner: Phương tiện và trò chuyện. Hợp đồng tham chiếu: Media flow + Chat ref. Dữ liệu: media_asset + message ref. Sự kiện: MediaReady; TranscriptReady tùy chọn.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-BE-MED-06-01](prompts/PH04-BE-MED-06-01.md) | Triển khai MED-06: Phương tiện cho tin nhắn thoại | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH03-BE-CHT-02-02 |
| [PH04-BE-MED-06-02](prompts/PH04-BE-MED-06-02.md) | Nghiệm thu MED-06 và bàn giao | PH04-BE-MED-06-01 |

## PH05 — Xóa liên dịch vụ, điều hành và nghiệm thu P1

### PH05-BE-ACC-11 — Yêu cầu xóa và khôi phục tài khoản

Ưu tiên P1; miền account. Owner: Tài khoản. Hợp đồng tham chiếu: DELETE /users/me; cancel. Dữ liệu: account_deletion_request. Sự kiện: UserDeletionRequested/Cancelled/Completed. Hoàn thành API Account chưa thay cho subtask xóa của từng downstream trong PH05-BE-DELETION.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-ACC-11-01](prompts/PH05-BE-ACC-11-01.md) | Triển khai ACC-11: Yêu cầu xóa và khôi phục tài khoản | PH05-DATA-DEL-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-05-02, PH04-BE-MED-05-02, PH04-BE-SOC-10-02, PH04-BE-CHT-09-02 |
| [PH05-BE-ACC-11-02](prompts/PH05-BE-ACC-11-02.md) | Nghiệm thu ACC-11 và bàn giao | PH05-BE-ACC-11-01 |

### PH05-BE-MOD-01 — Gửi báo cáo vi phạm

Ưu tiên P1; miền social. Owner: Mạng xã hội - khối điều hành. Hợp đồng tham chiếu: POST /reports. Dữ liệu: content_report, evidence. Sự kiện: ContentReported.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-MOD-01-01](prompts/PH05-BE-MOD-01-01.md) | Triển khai MOD-01: Gửi báo cáo vi phạm | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-SOC-09-02, PH04-BE-COM-05-02, PH04-BE-MED-05-02 |
| [PH05-BE-MOD-01-02](prompts/PH05-BE-MOD-01-02.md) | Nghiệm thu MOD-01 và bàn giao | PH05-BE-MOD-01-01 |

### PH05-BE-MOD-02 — Duyệt hàng đợi báo cáo

Ưu tiên P1; miền social. Owner: Mạng xã hội - khối điều hành. Hợp đồng tham chiếu: GET /moderation/reports. Dữ liệu: content_report. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-MOD-02-01](prompts/PH05-BE-MOD-02-01.md) | Triển khai MOD-02: Duyệt hàng đợi báo cáo | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-01-02 |
| [PH05-BE-MOD-02-02](prompts/PH05-BE-MOD-02-02.md) | Nghiệm thu MOD-02 và bàn giao | PH05-BE-MOD-02-01 |

### PH05-BE-MOD-03 — Áp dụng hành động điều hành

Ưu tiên P1; miền social. Owner: Mạng xã hội điều phối; dịch vụ nguồn áp dụng. Hợp đồng tham chiếu: POST /reports/{id}/actions. Dữ liệu: moderation_action, outbox. Sự kiện: ModerationActionRequested.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-MOD-03-01](prompts/PH05-BE-MOD-03-01.md) | Triển khai MOD-03: Áp dụng hành động điều hành | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-02-02 |
| [PH05-BE-MOD-03-02](prompts/PH05-BE-MOD-03-02.md) | Nghiệm thu MOD-03 và bàn giao | PH05-BE-MOD-03-01 |

### PH05-BE-MOD-04 — Đóng báo cáo và kiểm toán

Ưu tiên P1; miền social. Owner: Mạng xã hội - khối điều hành. Hợp đồng tham chiếu: POST /reports/{id}/close. Dữ liệu: content_report. Sự kiện: Completed/Rejected.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-MOD-04-01](prompts/PH05-BE-MOD-04-01.md) | Triển khai MOD-04: Đóng báo cáo và kiểm toán | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-03-02 |
| [PH05-BE-MOD-04-02](prompts/PH05-BE-MOD-04-02.md) | Nghiệm thu MOD-04 và bàn giao | PH05-BE-MOD-04-01 |

### PH05-BE-DELETION — Lan truyền và đối soát xóa tài khoản

Ưu tiên P1; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-BE-DELETION-01](prompts/PH05-BE-DELETION-01.md) | Xóa tài khoản: Ẩn/ẩn danh post/comment, dọn follow/block và bảo vệ retention_hold | PH05-BE-ACC-11-02 |
| [PH05-BE-DELETION-02](prompts/PH05-BE-DELETION-02.md) | Xóa tài khoản: Xóa FeedEntry/UserSummary/cache trong 5 phút | PH05-BE-DELETION-01 |
| [PH05-BE-DELETION-03](prompts/PH05-BE-DELETION-03.md) | Xóa tài khoản: Ẩn PII profile, giữ lịch sử người khác theo policy, xử lý quyền/reconnect | PH05-BE-DELETION-02 |
| [PH05-BE-DELETION-04](prompts/PH05-BE-DELETION-04.md) | Xóa tài khoản: Vô hiệu membership/role/invite và chuyển owner trước purge | PH05-BE-DELETION-03 |
| [PH05-BE-DELETION-05](prompts/PH05-BE-DELETION-05.md) | Xóa tài khoản: Đối soát tham chiếu, dọn object không dùng, giữ evidence có hold | PH05-BE-DELETION-04 |
| [PH05-BE-DELETION-06](prompts/PH05-BE-DELETION-06.md) | Xóa tài khoản: Đối soát ack/retry/timeouts, cancel trong grace, chặn completed khi thiếu participant | PH05-BE-DELETION-05 |
| [PH05-BE-DELETION-07](prompts/PH05-BE-DELETION-07.md) | Xóa tài khoản: Kiểm thử tích hợp hủy/purge/race/duplicate, ẩn <=5 phút, grace 30 ngày, PII <=45 ngày | PH05-BE-DELETION-06 |
| [PH05-BE-DELETION-08](prompts/PH05-BE-DELETION-08.md) | Xóa tài khoản: Bàn giao xóa liên dịch vụ và restore không làm sống lại dữ liệu đã xóa | PH05-BE-DELETION-07 |

## PH06 — Thương mại, AI và tìm kiếm P2 có điều kiện

### PH06-BE-CONTRACT — Quyết định phạm vi và hợp đồng P2

Ưu tiên P2; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-CONTRACT-01](prompts/PH06-BE-CONTRACT-01.md) | Quyết định phạm vi và hợp đồng P2 | G2-01 |

### PH06-BE-FED-04 — Sinh ứng viên và chấm điểm gợi ý

Ưu tiên P2; miền feed. Owner: Bảng tin và dữ liệu AI. Hợp đồng tham chiếu: GET /feed nội bộ. Dữ liệu: recommendation cache. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-FED-04-01](prompts/PH06-BE-FED-04-01.md) | Triển khai FED-04: Sinh ứng viên và chấm điểm gợi ý | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-FED-05-02, PH03-BE-FED-02-02 |
| [PH06-BE-FED-04-02](prompts/PH06-BE-FED-04-02.md) | Nghiệm thu FED-04 và bàn giao | PH06-BE-FED-04-01 |

### PH06-BE-FED-05 — Cập nhật embedding sở thích

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: Background worker. Dữ liệu: interest embedding. Sự kiện: EmbeddingGenerated tùy chọn.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-FED-05-01](prompts/PH06-BE-FED-05-01.md) | Triển khai FED-05: Cập nhật embedding sở thích | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-01-02, PH03-BE-SOC-08-02 |
| [PH06-BE-FED-05-02](prompts/PH06-BE-FED-05-02.md) | Nghiệm thu FED-05 và bàn giao | PH06-BE-FED-05-01 |

### PH06-BE-MKT-01 — Tạo và sửa tin đăng

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: POST/PATCH /listings. Dữ liệu: listing, media_ref. Sự kiện: ListingCreated/Updated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-01-01](prompts/PH06-BE-MKT-01-01.md) | Triển khai MKT-01: Tạo và sửa tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02 |
| [PH06-BE-MKT-01-02](prompts/PH06-BE-MKT-01-02.md) | Nghiệm thu MKT-01 và bàn giao | PH06-BE-MKT-01-01 |

### PH06-BE-MKT-02 — Duyệt và tìm kiếm tin đăng

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: GET /listings. Dữ liệu: listing. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-02-01](prompts/PH06-BE-MKT-02-01.md) | Triển khai MKT-02: Duyệt và tìm kiếm tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02 |
| [PH06-BE-MKT-02-02](prompts/PH06-BE-MKT-02-02.md) | Nghiệm thu MKT-02 và bàn giao | PH06-BE-MKT-02-01 |

### PH06-BE-MKT-03 — Cập nhật và giữ tồn kho

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: PUT inventory; checkout. Dữ liệu: inventory. Sự kiện: Reserved/Released.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-03-01](prompts/PH06-BE-MKT-03-01.md) | Triển khai MKT-03: Cập nhật và giữ tồn kho | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02 |
| [PH06-BE-MKT-03-02](prompts/PH06-BE-MKT-03-02.md) | Nghiệm thu MKT-03 và bàn giao | PH06-BE-MKT-03-01 |

### PH06-BE-MKT-04 — Tạo đơn hàng

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: POST /orders. Dữ liệu: order, items, inventory. Sự kiện: OrderCreated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-04-01](prompts/PH06-BE-MKT-04-01.md) | Triển khai MKT-04: Tạo đơn hàng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-03-02, PH06-BE-MKT-07-02 |
| [PH06-BE-MKT-04-02](prompts/PH06-BE-MKT-04-02.md) | Nghiệm thu MKT-04 và bàn giao | PH06-BE-MKT-04-01 |

### PH06-BE-MKT-05 — Thanh toán giả lập

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: POST /orders/{id}/pay. Dữ liệu: payment, order. Sự kiện: PaymentSucceeded/Failed.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-05-01](prompts/PH06-BE-MKT-05-01.md) | Triển khai MKT-05: Thanh toán giả lập | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-06-02 |
| [PH06-BE-MKT-05-02](prompts/PH06-BE-MKT-05-02.md) | Nghiệm thu MKT-05 và bàn giao | PH06-BE-MKT-05-01 |

### PH06-BE-MKT-06 — Trạng thái đơn hàng và Saga đơn giản hóa

Ưu tiên P2; miền commerce. Owner: Thương mại. Hợp đồng tham chiếu: State transition/cancel. Dữ liệu: order, status_history. Sự kiện: OrderStatusChanged.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-06-01](prompts/PH06-BE-MKT-06-01.md) | Triển khai MKT-06: Trạng thái đơn hàng và Saga đơn giản hóa | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-04-02 |
| [PH06-BE-MKT-06-02](prompts/PH06-BE-MKT-06-02.md) | Nghiệm thu MKT-06 và bàn giao | PH06-BE-MKT-06-01 |

### PH06-BE-MKT-07 — Phương tiện của tin đăng

Ưu tiên P2; miền commerce. Owner: Commerce + Phương tiện. Hợp đồng tham chiếu: Listing media refs. Dữ liệu: listing_media_ref. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-MKT-07-01](prompts/PH06-BE-MKT-07-01.md) | Triển khai MKT-07: Phương tiện của tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02, PH04-BE-MED-05-02 |
| [PH06-BE-MKT-07-02](prompts/PH06-BE-MKT-07-02.md) | Nghiệm thu MKT-07 và bàn giao | PH06-BE-MKT-07-01 |

### PH06-BE-AI-01 — Tạo embedding

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: Worker/event. Dữ liệu: ai_embedding, ai_job. Sự kiện: EmbeddingGenerated.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-01-01](prompts/PH06-BE-AI-01-01.md) | Triển khai AI-01: Tạo embedding | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-05-02, PH05-BE-ACC-11-02 |
| [PH06-BE-AI-01-02](prompts/PH06-BE-AI-01-02.md) | Nghiệm thu AI-01 và bàn giao | PH06-BE-AI-01-01 |

### PH06-BE-AI-02 — Tìm kiếm ngữ nghĩa

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: GET /search/semantic. Dữ liệu: pgvector. Sự kiện: Không.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-02-01](prompts/PH06-BE-AI-02-01.md) | Triển khai AI-02: Tìm kiếm ngữ nghĩa | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-01-02 |
| [PH06-BE-AI-02-02](prompts/PH06-BE-AI-02-02.md) | Nghiệm thu AI-02 và bàn giao | PH06-BE-AI-02-01 |

### PH06-BE-AI-03 — Trợ lý RAG

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: POST /ai/ask. Dữ liệu: chunks, request metadata. Sự kiện: AiToken/AiCompleted.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-03-01](prompts/PH06-BE-AI-03-01.md) | Triển khai AI-03: Trợ lý RAG | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-02-02 |
| [PH06-BE-AI-03-02](prompts/PH06-BE-AI-03-02.md) | Nghiệm thu AI-03 và bàn giao | PH06-BE-AI-03-01 |

### PH06-BE-AI-04 — Tóm tắt tin nhắn hoặc kênh

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm + trò chuyện. Hợp đồng tham chiếu: POST /ai/summaries. Dữ liệu: summary tùy chọn. Sự kiện: AiSummaryReady.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-04-01](prompts/PH06-BE-AI-04-01.md) | Triển khai AI-04: Tóm tắt tin nhắn hoặc kênh | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-03-02, PH03-BE-CHT-03-02 |
| [PH06-BE-AI-04-02](prompts/PH06-BE-AI-04-02.md) | Nghiệm thu AI-04 và bàn giao | PH06-BE-AI-04-01 |

### PH06-BE-AI-05 — Chuyển lời nói thành văn bản

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: POST transcriptions/worker. Dữ liệu: ai_job, transcript. Sự kiện: TranscriptReady.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-05-01](prompts/PH06-BE-AI-05-01.md) | Triển khai AI-05: Chuyển lời nói thành văn bản | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-06-02, PH06-BE-AI-01-02 |
| [PH06-BE-AI-05-02](prompts/PH06-BE-AI-05-02.md) | Nghiệm thu AI-05 và bàn giao | PH06-BE-AI-05-01 |

### PH06-BE-AI-06 — Đánh chỉ mục OpenSearch - tùy chọn

Ưu tiên P2; miền ai. Owner: AI và tìm kiếm. Hợp đồng tham chiếu: Kafka consumer. Dữ liệu: OpenSearch projection. Sự kiện: Không. OpenSearch tùy chọn: triển khai hoặc quyết định hoãn theo quy trình scope; không giả DONE.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-BE-AI-06-01](prompts/PH06-BE-AI-06-01.md) | Triển khai AI-06: Đánh chỉ mục OpenSearch - tùy chọn | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-02-02, PH06-BE-MKT-02-02 |
| [PH06-BE-AI-06-02](prompts/PH06-BE-AI-06-02.md) | Nghiệm thu AI-06 và bàn giao | PH06-BE-AI-06-01 |
