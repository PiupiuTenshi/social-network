# Danh mục DATA

Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.

## PH00 — Khảo sát, quyết định và G0

### PH00-DATA-BOUNDARY — Khóa ownership, ERD P0 và chiến lược dữ liệu

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH00-DATA-BOUNDARY-01](prompts/PH00-DATA-BOUNDARY-01.md) | Khóa ownership, ERD P0 và chiến lược dữ liệu | PH00-BE-CONTRACT-01 |

## PH01 — Nền tảng Backend, Data và Frontend

### PH01-DATA-INFRA — Hạ tầng dữ liệu core và migration runner

Ưu tiên P0; miền deploy. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH01-DATA-INFRA-01](prompts/PH01-DATA-INFRA-01.md) | Hạ tầng dữ liệu core và migration runner | G0-01 |

## PH02 — Tài khoản P0

### PH02-DATA-ACC-P0 — Dữ liệu ACC P0

Ưu tiên P0; miền account. account, profile, refresh_token, account_setting; token hash/family/version và email/username unique

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-DATA-ACC-P0-01](prompts/PH02-DATA-ACC-P0-01.md) | Thiết kế lược đồ ACC P0 | PH01-BE-PLATFORM-01 |
| [PH02-DATA-ACC-P0-02](prompts/PH02-DATA-ACC-P0-02.md) | Migration và fixture ACC P0 | PH02-DATA-ACC-P0-01 |
| [PH02-DATA-ACC-P0-03](prompts/PH02-DATA-ACC-P0-03.md) | Kiểm chứng dữ liệu ACC P0 | PH02-DATA-ACC-P0-02 |

## PH03 — Mạng xã hội, Bảng tin, Trò chuyện P0

### PH03-DATA-SOC-P0 — Dữ liệu SOC P0

Ưu tiên P0; miền social. follow, block, post, post_media_ref, comment, reaction; unique/check, visibility/version và cursor

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-DATA-SOC-P0-01](prompts/PH03-DATA-SOC-P0-01.md) | Thiết kế lược đồ SOC P0 | PH01-BE-PLATFORM-01 |
| [PH03-DATA-SOC-P0-02](prompts/PH03-DATA-SOC-P0-02.md) | Migration và fixture SOC P0 | PH03-DATA-SOC-P0-01 |
| [PH03-DATA-SOC-P0-03](prompts/PH03-DATA-SOC-P0-03.md) | Kiểm chứng dữ liệu SOC P0 | PH03-DATA-SOC-P0-02 |

### PH03-DATA-CHT-P0 — Dữ liệu CHT P0

Ưu tiên P0; miền chat. conversation, conversation_member, message, message_reaction, notification; unique clientMessageId và read cursor tăng

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-DATA-CHT-P0-01](prompts/PH03-DATA-CHT-P0-01.md) | Thiết kế lược đồ CHT P0 | PH01-BE-PLATFORM-01 |
| [PH03-DATA-CHT-P0-02](prompts/PH03-DATA-CHT-P0-02.md) | Migration và fixture CHT P0 | PH03-DATA-CHT-P0-01 |
| [PH03-DATA-CHT-P0-03](prompts/PH03-DATA-CHT-P0-03.md) | Kiểm chứng dữ liệu CHT P0 | PH03-DATA-CHT-P0-02 |

### PH03-DATA-FED-P0 — Dữ liệu FED P0

Ưu tiên P0; miền feed. FeedEntry/UserSummary/PostSummary, Inbox/checkpoint; quyền/block, invalidation và rebuild

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-DATA-FED-P0-01](prompts/PH03-DATA-FED-P0-01.md) | Thiết kế lược đồ FED P0 | PH01-BE-PLATFORM-01 |
| [PH03-DATA-FED-P0-02](prompts/PH03-DATA-FED-P0-02.md) | Migration và fixture FED P0 | PH03-DATA-FED-P0-01 |
| [PH03-DATA-FED-P0-03](prompts/PH03-DATA-FED-P0-03.md) | Kiểm chứng dữ liệu FED P0 | PH03-DATA-FED-P0-02 |

### PH03-DATA-RECOVERY — Khôi phục P0 và rebuild Feed

Ưu tiên P0; miền deploy. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-DATA-RECOVERY-01](prompts/PH03-DATA-RECOVERY-01.md) | Khôi phục P0 và rebuild Feed | PH03-BE-FED-02-02, PH03-BE-CHT-08-02 |

## PH04 — Cộng đồng, RTC, Phương tiện và tài khoản P1

### PH04-DATA-ACC-P1 — Dữ liệu ACC P1

Ưu tiên P1; miền account. password_reset_token, account_oauth, avatar refs; OTP hash/attempt/TTL và unique provider identity

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-DATA-ACC-P1-01](prompts/PH04-DATA-ACC-P1-01.md) | Thiết kế lược đồ ACC P1 | PH04-BE-CONTRACT-01, PH02-DATA-ACC-P0-03 |
| [PH04-DATA-ACC-P1-02](prompts/PH04-DATA-ACC-P1-02.md) | Migration và fixture ACC P1 | PH04-DATA-ACC-P1-01 |
| [PH04-DATA-ACC-P1-03](prompts/PH04-DATA-ACC-P1-03.md) | Kiểm chứng dữ liệu ACC P1 | PH04-DATA-ACC-P1-02 |

### PH04-DATA-COM-P1 — Dữ liệu COM P1

Ưu tiên P1; miền community. community/member/role/member_role/channel/invite; hierarchy, owner protection, uses/version

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-DATA-COM-P1-01](prompts/PH04-DATA-COM-P1-01.md) | Thiết kế lược đồ COM P1 | PH04-BE-CONTRACT-01 |
| [PH04-DATA-COM-P1-02](prompts/PH04-DATA-COM-P1-02.md) | Migration và fixture COM P1 | PH04-DATA-COM-P1-01 |
| [PH04-DATA-COM-P1-03](prompts/PH04-DATA-COM-P1-03.md) | Kiểm chứng dữ liệu COM P1 | PH04-DATA-COM-P1-02 |

### PH04-DATA-MED-P1 — Dữ liệu MED P1

Ưu tiên P1; miền media. UploadSession/MediaAsset, object metadata; state, expiry, reference/retention_hold và cleanup

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-DATA-MED-P1-01](prompts/PH04-DATA-MED-P1-01.md) | Thiết kế lược đồ MED P1 | PH04-BE-CONTRACT-01 |
| [PH04-DATA-MED-P1-02](prompts/PH04-DATA-MED-P1-02.md) | Migration và fixture MED P1 | PH04-DATA-MED-P1-01 |
| [PH04-DATA-MED-P1-03](prompts/PH04-DATA-MED-P1-03.md) | Kiểm chứng dữ liệu MED P1 | PH04-DATA-MED-P1-02 |

### PH04-DATA-SOC-P1 — Dữ liệu SOC P1

Ưu tiên P1; miền social. post_share và video processing/publication; không gộp nhầm visibility/privacy

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-DATA-SOC-P1-01](prompts/PH04-DATA-SOC-P1-01.md) | Thiết kế lược đồ SOC P1 | PH04-BE-CONTRACT-01, PH03-DATA-SOC-P0-03 |
| [PH04-DATA-SOC-P1-02](prompts/PH04-DATA-SOC-P1-02.md) | Migration và fixture SOC P1 | PH04-DATA-SOC-P1-01 |
| [PH04-DATA-SOC-P1-03](prompts/PH04-DATA-SOC-P1-03.md) | Kiểm chứng dữ liệu SOC P1 | PH04-DATA-SOC-P1-02 |

### PH04-DATA-CHT-P1 — Dữ liệu CHT P1

Ưu tiên P1; miền chat. community permission projection, call invite, media refs; expiry và quyền stale

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-DATA-CHT-P1-01](prompts/PH04-DATA-CHT-P1-01.md) | Thiết kế lược đồ CHT P1 | PH04-BE-CONTRACT-01, PH03-DATA-CHT-P0-03 |
| [PH04-DATA-CHT-P1-02](prompts/PH04-DATA-CHT-P1-02.md) | Migration và fixture CHT P1 | PH04-DATA-CHT-P1-01 |
| [PH04-DATA-CHT-P1-03](prompts/PH04-DATA-CHT-P1-03.md) | Kiểm chứng dữ liệu CHT P1 | PH04-DATA-CHT-P1-02 |

## PH05 — Xóa liên dịch vụ, điều hành và nghiệm thu P1

### PH05-DATA-DEL-P1 — Dữ liệu DEL P1

Ưu tiên P1; miền account. account_deletion_request/ack theo dịch vụ, grace/purge/cancel, retention_hold; không tạo DB chung

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-DATA-DEL-P1-01](prompts/PH05-DATA-DEL-P1-01.md) | Thiết kế lược đồ DEL P1 | PH04-BE-CONTRACT-01 |
| [PH05-DATA-DEL-P1-02](prompts/PH05-DATA-DEL-P1-02.md) | Migration và fixture DEL P1 | PH05-DATA-DEL-P1-01 |
| [PH05-DATA-DEL-P1-03](prompts/PH05-DATA-DEL-P1-03.md) | Kiểm chứng dữ liệu DEL P1 | PH05-DATA-DEL-P1-02 |

### PH05-DATA-MOD-P1 — Dữ liệu MOD P1

Ưu tiên P1; miền social. content_report/moderation_evidence/moderation_action; audit append-only và state machine

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-DATA-MOD-P1-01](prompts/PH05-DATA-MOD-P1-01.md) | Thiết kế lược đồ MOD P1 | PH04-BE-CONTRACT-01 |
| [PH05-DATA-MOD-P1-02](prompts/PH05-DATA-MOD-P1-02.md) | Migration và fixture MOD P1 | PH05-DATA-MOD-P1-01 |
| [PH05-DATA-MOD-P1-03](prompts/PH05-DATA-MOD-P1-03.md) | Kiểm chứng dữ liệu MOD P1 | PH05-DATA-MOD-P1-02 |

### PH05-DATA-RESTORE — Khôi phục Media và dữ liệu P1

Ưu tiên P1; miền deploy. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-DATA-RESTORE-01](prompts/PH05-DATA-RESTORE-01.md) | Khôi phục Media và dữ liệu P1 | PH05-BE-DELETION-08, PH05-BE-MOD-04-02 |

## PH06 — Thương mại, AI và tìm kiếm P2 có điều kiện

### PH06-DATA-MKT-P2 — Dữ liệu MKT P2

Ưu tiên P2; miền commerce. listing/media_ref/inventory/order/item/payment/history; số tiền snapshot, reserved constraint, idempotency

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-DATA-MKT-P2-01](prompts/PH06-DATA-MKT-P2-01.md) | Thiết kế lược đồ MKT P2 | PH06-BE-CONTRACT-01 |
| [PH06-DATA-MKT-P2-02](prompts/PH06-DATA-MKT-P2-02.md) | Migration và fixture MKT P2 | PH06-DATA-MKT-P2-01 |
| [PH06-DATA-MKT-P2-03](prompts/PH06-DATA-MKT-P2-03.md) | Kiểm chứng dữ liệu MKT P2 | PH06-DATA-MKT-P2-02 |

### PH06-DATA-AI-P2 — Dữ liệu AI P2

Ưu tiên P2; miền ai. ai_embedding/chunk/job/transcript/interest vector; model version, ACL, pgvector, checkpoint/rebuild

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-DATA-AI-P2-01](prompts/PH06-DATA-AI-P2-01.md) | Thiết kế lược đồ AI P2 | PH06-BE-CONTRACT-01 |
| [PH06-DATA-AI-P2-02](prompts/PH06-DATA-AI-P2-02.md) | Migration và fixture AI P2 | PH06-DATA-AI-P2-01 |
| [PH06-DATA-AI-P2-03](prompts/PH06-DATA-AI-P2-03.md) | Kiểm chứng dữ liệu AI P2 | PH06-DATA-AI-P2-02 |

### PH06-DATA-LIFECYCLE — Xóa, phục hồi và rebuild P2

Ưu tiên P2; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-DATA-LIFECYCLE-01](prompts/PH06-DATA-LIFECYCLE-01.md) | Xóa, phục hồi và rebuild P2 | PH06-BE-MKT-05-02, PH06-BE-AI-05-02, PH06-BE-FED-04-02 |
