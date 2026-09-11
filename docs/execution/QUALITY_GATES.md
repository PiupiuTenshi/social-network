# Danh mục QUALITY_GATES

Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.

## PH00 — Khảo sát, quyết định và G0

### G0 — Nghiệm thu kiến trúc trước khi viết nghiệp vụ

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [G0-01](prompts/G0-01.md) | Nghiệm thu kiến trúc trước khi viết nghiệp vụ | PH00-BE-TOOLCHAIN-01 |

## PH02 — Tài khoản P0

### PH02-GATE-ACCOUNT — Đo baseline Account trước Mạng xã hội

Ưu tiên P0; miền account. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-GATE-ACCOUNT-01](prompts/PH02-GATE-ACCOUNT-01.md) | Đo baseline Account trước Mạng xã hội | PH02-BE-ACC-01-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02, PH02-BE-ACC-05-02, PH02-BE-ACC-07-02 |

## PH03 — Mạng xã hội, Bảng tin, Trò chuyện P0

### G1 — Nghiệm thu P0 trước mọi P1

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [G1-01](prompts/G1-01.md) | Nghiệm thu P0 trước mọi P1 | PH02-BE-ACC-01-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02, PH02-BE-ACC-05-02, PH02-BE-ACC-07-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02, PH03-BE-SOC-03-02, PH03-BE-SOC-04-02, PH03-BE-SOC-05-02, PH03-BE-SOC-06-02, PH03-BE-SOC-07-02, PH03-BE-SOC-08-02, PH03-BE-CHT-01-02, PH03-BE-CHT-02-02, PH03-BE-CHT-03-02, PH03-BE-CHT-04-02, PH03-BE-CHT-05-02, PH03-BE-CHT-06-02, PH03-BE-CHT-07-02, PH03-BE-CHT-08-02, PH03-BE-FED-01-02, PH03-BE-FED-02-02, PH03-BE-FED-03-02, PH02-FE-AUTH-01-P0-02, PH02-FE-AUTH-02-P0-02, PH02-FE-AUTH-03-P0-02, PH03-FE-FEED-01-P0-02, PH03-FE-FEED-02-P0-02, PH03-FE-FEED-03-P0-02, PH03-FE-FEED-04-P0-02, PH03-FE-PROF-01-P0-02, PH03-FE-PROF-02-P0-02, PH03-FE-PROF-04-P0-02, PH03-FE-SET-01-P0-02, PH03-FE-SET-02-P0-02, PH03-FE-SET-03-P0-02, PH03-FE-NOTI-01-P0-02, PH03-FE-CHAT-01-P0-02, PH03-FE-CHAT-02-P0-02, PH03-FE-CHAT-03-P0-02, PH03-FE-CHAT-04-P0-02, PH03-FE-SYS-01-P0-02, PH03-DATA-RECOVERY-01, PH01-BE-CI-01 |

## PH05 — Xóa liên dịch vụ, điều hành và nghiệm thu P1

### G2 — Nghiệm thu P1 trước P2

Ưu tiên P1; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [G2-01](prompts/G2-01.md) | Nghiệm thu P1 trước P2 | PH04-BE-ACC-06-02, PH04-BE-ACC-08-02, PH04-BE-ACC-09-02, PH04-BE-ACC-10-02, PH04-BE-SOC-09-02, PH04-BE-SOC-10-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, PH04-BE-COM-03-02, PH04-BE-COM-04-02, PH04-BE-COM-05-02, PH04-BE-RTC-01-02, PH04-BE-RTC-02-02, PH04-BE-RTC-03-02, PH04-BE-CHT-09-02, PH04-BE-MED-01-02, PH04-BE-MED-02-02, PH04-BE-MED-03-02, PH04-BE-MED-04-02, PH04-BE-MED-05-02, PH04-BE-MED-06-02, PH05-BE-ACC-11-02, PH05-BE-MOD-01-02, PH05-BE-MOD-02-02, PH05-BE-MOD-03-02, PH05-BE-MOD-04-02, PH04-FE-AUTH-02-P1-02, PH04-FE-AUTH-03-P1-02, PH04-FE-AUTH-04-P1-02, PH04-FE-AUTH-05-P1-02, PH04-FE-FEED-01-P1-02, PH04-FE-FEED-02-P1-02, PH04-FE-FEED-03-P1-02, PH04-FE-FEED-05-P1-02, PH04-FE-PROF-03-P1-02, PH04-FE-SET-02-P1-02, PH05-FE-SET-04-P1-02, PH04-FE-COMM-01-P1-02, PH04-FE-COMM-02-P1-02, PH04-FE-COMM-03-P1-02, PH04-FE-COMM-04-P1-02, PH04-FE-COMM-05-P1-02, PH04-FE-COMM-06-P1-02, PH04-FE-COMM-07-P1-02, PH04-FE-CHAT-02-P1-02, PH04-FE-RTC-01-P1-02, PH04-FE-RTC-02-P1-02, PH04-FE-RTC-03-P1-02, PH04-FE-MEDIA-01-P1-02, PH05-FE-MOD-01-P1-02, PH05-FE-MOD-02-P1-02, PH05-FE-MOD-03-P1-02, PH05-BE-DELETION-08, PH05-DATA-RESTORE-01 |

## PH06 — Thương mại, AI và tìm kiếm P2 có điều kiện

### G3 — Nghiệm thu P2 và đóng phạm vi

Ưu tiên P2; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [G3-01](prompts/G3-01.md) | Nghiệm thu P2 và đóng phạm vi | PH06-BE-FED-04-02, PH06-BE-FED-05-02, PH06-BE-MKT-01-02, PH06-BE-MKT-02-02, PH06-BE-MKT-03-02, PH06-BE-MKT-04-02, PH06-BE-MKT-05-02, PH06-BE-MKT-06-02, PH06-BE-MKT-07-02, PH06-BE-AI-01-02, PH06-BE-AI-02-02, PH06-BE-AI-03-02, PH06-BE-AI-04-02, PH06-BE-AI-05-02, PH06-BE-AI-06-02, PH06-FE-FEED-01-P2-02, PH06-FE-FEED-03-P2-02, PH06-FE-DISC-01-P2-02, PH06-FE-CHAT-02-P2-02, PH06-FE-MKT-01-P2-02, PH06-FE-MKT-02-P2-02, PH06-FE-MKT-03-P2-02, PH06-FE-MKT-04-P2-02, PH06-FE-MKT-05-P2-02, PH06-FE-MKT-06-P2-02, PH06-FE-AI-01-P2-02, PH06-FE-AI-02-P2-02, PH06-DATA-LIFECYCLE-01 |

## PH08 — Diễn tập phát hành và bàn giao

### G4 — Nghiệm thu phát hành

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [G4-01](prompts/G4-01.md) | Nghiệm thu phát hành | PH08-GOV-REHEARSAL-01 |
