# Thứ tự prompt theo phụ thuộc

Sinh từ `build_execution_plan.py`. Đây là chỉ mục đọc/thực hiện đề nghị theo đồ thị dependency, không phải quyền bỏ qua cổng READY.
Một đợt chứa các prompt không phụ thuộc lẫn nhau; có thể chuẩn bị song song khi ownership/hợp đồng ổn định và coordinator cho phép. Trước khi thực hiện bất kỳ prompt nào vẫn chạy `task_gate.py check ID`; chỉ `READY` hoặc đúng task `IN_PROGRESS` mới được làm.

Bước đầu tiên luôn là `PH00-GOV-AUDIT-01`. Các mục sau có thể xuất hiện sớm trong chỉ mục nhưng vẫn bị chặn đến khi toàn bộ dependency của chính chúng `DONE` hợp lệ.

## Đợt 01 — PH00

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 001 | [PH00-GOV-AUDIT-01](prompts/PH00-GOV-AUDIT-01.md) | GOV | P0 | Xác nhận nguồn, quy tắc và phạm vi thực tế | Không; cần DoR |

## Đợt 02 — PH00

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 002 | [PH00-BE-CONTRACT-01](prompts/PH00-BE-CONTRACT-01.md) | BE | P0 | Khóa hợp đồng P0 và xử lý mâu thuẫn nền | PH00-GOV-AUDIT-01 |

## Đợt 03 — PH00

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 003 | [PH00-DATA-BOUNDARY-01](prompts/PH00-DATA-BOUNDARY-01.md) | DATA | P0 | Khóa ownership, ERD P0 và chiến lược dữ liệu | PH00-BE-CONTRACT-01 |

## Đợt 04 — PH00

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 004 | [PH00-BE-TOOLCHAIN-01](prompts/PH00-BE-TOOLCHAIN-01.md) | BE | P0 | Dựng harness kiến trúc và khóa toolchain | PH00-DATA-BOUNDARY-01 |

## Đợt 05 — PH00

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 005 | [G0-01](prompts/G0-01.md) | GATE | P0 | Nghiệm thu kiến trúc trước khi viết nghiệp vụ | PH00-BE-TOOLCHAIN-01 |

## Đợt 06 — PH01

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 006 | [PH01-DATA-INFRA-01](prompts/PH01-DATA-INFRA-01.md) | DATA | P0 | Hạ tầng dữ liệu core và migration runner | G0-01 |
| 007 | [PH01-FE-FOUNDATION-01](prompts/PH01-FE-FOUNDATION-01.md) | FE | P0 | Dựng app shell, token, navigation và trạng thái dùng chung | G0-01 |

## Đợt 07 — PH01

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 008 | [PH01-BE-PLATFORM-01](prompts/PH01-BE-PLATFORM-01.md) | BE | P0 | BuildingBlocks, Gateway và quan sát cơ sở | PH01-DATA-INFRA-01 |
| 009 | [PH01-FE-FOUNDATION-02](prompts/PH01-FE-FOUNDATION-02.md) | FE | P0 | HTTP/auth/realtime adapters có xử lý lỗi và vòng đời | PH01-FE-FOUNDATION-01 |

## Đợt 08 — PH01, PH02, PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 010 | [PH01-BE-CI-01](prompts/PH01-BE-CI-01.md) | BE | P0 | CI có kiểm tra bắt buộc và bảo vệ nhánh | PH01-BE-PLATFORM-01 |
| 011 | [PH02-DATA-ACC-P0-01](prompts/PH02-DATA-ACC-P0-01.md) | DATA | P0 | Thiết kế lược đồ ACC P0 | PH01-BE-PLATFORM-01 |
| 012 | [PH03-DATA-SOC-P0-01](prompts/PH03-DATA-SOC-P0-01.md) | DATA | P0 | Thiết kế lược đồ SOC P0 | PH01-BE-PLATFORM-01 |
| 013 | [PH03-DATA-CHT-P0-01](prompts/PH03-DATA-CHT-P0-01.md) | DATA | P0 | Thiết kế lược đồ CHT P0 | PH01-BE-PLATFORM-01 |
| 014 | [PH03-DATA-FED-P0-01](prompts/PH03-DATA-FED-P0-01.md) | DATA | P0 | Thiết kế lược đồ FED P0 | PH01-BE-PLATFORM-01 |
| 015 | [PH03-FE-SYS-01-P0-01](prompts/PH03-FE-SYS-01-P0-01.md) | FE | P0 | Triển khai SYS-01 P0: Trạng thái tải, rỗng, lỗi và ngoại tuyến | PH01-FE-FOUNDATION-02 |

## Đợt 09 — PH02, PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 016 | [PH02-DATA-ACC-P0-02](prompts/PH02-DATA-ACC-P0-02.md) | DATA | P0 | Migration và fixture ACC P0 | PH02-DATA-ACC-P0-01 |
| 017 | [PH03-DATA-SOC-P0-02](prompts/PH03-DATA-SOC-P0-02.md) | DATA | P0 | Migration và fixture SOC P0 | PH03-DATA-SOC-P0-01 |
| 018 | [PH03-DATA-CHT-P0-02](prompts/PH03-DATA-CHT-P0-02.md) | DATA | P0 | Migration và fixture CHT P0 | PH03-DATA-CHT-P0-01 |
| 019 | [PH03-DATA-FED-P0-02](prompts/PH03-DATA-FED-P0-02.md) | DATA | P0 | Migration và fixture FED P0 | PH03-DATA-FED-P0-01 |
| 020 | [PH03-FE-SYS-01-P0-02](prompts/PH03-FE-SYS-01-P0-02.md) | FE | P0 | QA SYS-01 P0 trên Desktop/Mobile | PH03-FE-SYS-01-P0-01 |

## Đợt 10 — PH02, PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 021 | [PH02-DATA-ACC-P0-03](prompts/PH02-DATA-ACC-P0-03.md) | DATA | P0 | Kiểm chứng dữ liệu ACC P0 | PH02-DATA-ACC-P0-02 |
| 022 | [PH03-DATA-SOC-P0-03](prompts/PH03-DATA-SOC-P0-03.md) | DATA | P0 | Kiểm chứng dữ liệu SOC P0 | PH03-DATA-SOC-P0-02 |
| 023 | [PH03-DATA-CHT-P0-03](prompts/PH03-DATA-CHT-P0-03.md) | DATA | P0 | Kiểm chứng dữ liệu CHT P0 | PH03-DATA-CHT-P0-02 |
| 024 | [PH03-DATA-FED-P0-03](prompts/PH03-DATA-FED-P0-03.md) | DATA | P0 | Kiểm chứng dữ liệu FED P0 | PH03-DATA-FED-P0-02 |

## Đợt 11 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 025 | [PH02-BE-ACC-01-01](prompts/PH02-BE-ACC-01-01.md) | BE | P0 | Triển khai ACC-01: Đăng ký | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |

## Đợt 12 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 026 | [PH02-BE-ACC-01-02](prompts/PH02-BE-ACC-01-02.md) | BE | P0 | Nghiệm thu ACC-01 và bàn giao | PH02-BE-ACC-01-01 |

## Đợt 13 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 027 | [PH02-BE-ACC-02-01](prompts/PH02-BE-ACC-02-01.md) | BE | P0 | Triển khai ACC-02: Đăng nhập | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-01-02 |
| 028 | [PH02-FE-AUTH-03-P0-01](prompts/PH02-FE-AUTH-03-P0-01.md) | FE | P0 | Triển khai AUTH-03 P0: Đăng ký | PH01-FE-FOUNDATION-02, PH02-BE-ACC-01-02 |

## Đợt 14 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 029 | [PH02-BE-ACC-02-02](prompts/PH02-BE-ACC-02-02.md) | BE | P0 | Nghiệm thu ACC-02 và bàn giao | PH02-BE-ACC-02-01 |
| 030 | [PH02-FE-AUTH-03-P0-02](prompts/PH02-FE-AUTH-03-P0-02.md) | FE | P0 | QA AUTH-03 P0 trên Desktop/Mobile | PH02-FE-AUTH-03-P0-01 |

## Đợt 15 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 031 | [PH02-BE-ACC-03-01](prompts/PH02-BE-ACC-03-01.md) | BE | P0 | Triển khai ACC-03: Xoay vòng refresh token | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-02-02 |
| 032 | [PH02-FE-AUTH-01-P0-01](prompts/PH02-FE-AUTH-01-P0-01.md) | FE | P0 | Triển khai AUTH-01 P0: Chào mừng | PH01-FE-FOUNDATION-02, PH02-BE-ACC-01-02, PH02-BE-ACC-02-02 |

## Đợt 16 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 033 | [PH02-BE-ACC-03-02](prompts/PH02-BE-ACC-03-02.md) | BE | P0 | Nghiệm thu ACC-03 và bàn giao | PH02-BE-ACC-03-01 |
| 034 | [PH02-FE-AUTH-01-P0-02](prompts/PH02-FE-AUTH-01-P0-02.md) | FE | P0 | QA AUTH-01 P0 trên Desktop/Mobile | PH02-FE-AUTH-01-P0-01 |

## Đợt 17 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 035 | [PH02-BE-ACC-04-01](prompts/PH02-BE-ACC-04-01.md) | BE | P0 | Triển khai ACC-04: Đăng xuất | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-03-02 |
| 036 | [PH02-FE-AUTH-02-P0-01](prompts/PH02-FE-AUTH-02-P0-01.md) | FE | P0 | Triển khai AUTH-02 P0: Đăng nhập | PH01-FE-FOUNDATION-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02 |

## Đợt 18 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 037 | [PH02-BE-ACC-04-02](prompts/PH02-BE-ACC-04-02.md) | BE | P0 | Nghiệm thu ACC-04 và bàn giao | PH02-BE-ACC-04-01 |
| 038 | [PH02-FE-AUTH-02-P0-02](prompts/PH02-FE-AUTH-02-P0-02.md) | FE | P0 | QA AUTH-02 P0 trên Desktop/Mobile | PH02-FE-AUTH-02-P0-01 |

## Đợt 19 — PH02, PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 039 | [PH02-BE-ACC-05-01](prompts/PH02-BE-ACC-05-01.md) | BE | P0 | Triển khai ACC-05: Xem và cập nhật hồ sơ | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-04-02 |
| 040 | [PH03-FE-SET-02-P0-01](prompts/PH03-FE-SET-02-P0-01.md) | FE | P0 | Triển khai SET-02 P0: Bảo mật tài khoản | PH01-FE-FOUNDATION-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02 |

## Đợt 20 — PH02, PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 041 | [PH02-BE-ACC-05-02](prompts/PH02-BE-ACC-05-02.md) | BE | P0 | Nghiệm thu ACC-05 và bàn giao | PH02-BE-ACC-05-01 |
| 042 | [PH03-FE-SET-02-P0-02](prompts/PH03-FE-SET-02-P0-02.md) | FE | P0 | QA SET-02 P0 trên Desktop/Mobile | PH03-FE-SET-02-P0-01 |

## Đợt 21 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 043 | [PH02-BE-ACC-07-01](prompts/PH02-BE-ACC-07-01.md) | BE | P0 | Triển khai ACC-07: Quyền riêng tư và thiết lập tài khoản | PH02-DATA-ACC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-05-02 |

## Đợt 22 — PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 044 | [PH02-BE-ACC-07-02](prompts/PH02-BE-ACC-07-02.md) | BE | P0 | Nghiệm thu ACC-07 và bàn giao | PH02-BE-ACC-07-01 |

## Đợt 23 — PH03, PH02

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 045 | [PH03-FE-SET-01-P0-01](prompts/PH03-FE-SET-01-P0-01.md) | FE | P0 | Triển khai SET-01 P0: Quyền riêng tư | PH01-FE-FOUNDATION-02, PH02-BE-ACC-07-02 |
| 046 | [PH02-GATE-ACCOUNT-01](prompts/PH02-GATE-ACCOUNT-01.md) | GATE | P0 | Đo baseline Account trước Mạng xã hội | PH02-BE-ACC-01-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02, PH02-BE-ACC-05-02, PH02-BE-ACC-07-02 |

## Đợt 24 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 047 | [PH03-BE-SOC-02-01](prompts/PH03-BE-SOC-02-01.md) | BE | P0 | Triển khai SOC-02: Chặn và bỏ chặn | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-07-02, PH02-GATE-ACCOUNT-01 |
| 048 | [PH03-FE-SET-01-P0-02](prompts/PH03-FE-SET-01-P0-02.md) | FE | P0 | QA SET-01 P0 trên Desktop/Mobile | PH03-FE-SET-01-P0-01 |

## Đợt 25 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 049 | [PH03-BE-SOC-02-02](prompts/PH03-BE-SOC-02-02.md) | BE | P0 | Nghiệm thu SOC-02 và bàn giao | PH03-BE-SOC-02-01 |

## Đợt 26 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 050 | [PH03-BE-SOC-01-01](prompts/PH03-BE-SOC-01-01.md) | BE | P0 | Triển khai SOC-01: Theo dõi và bỏ theo dõi | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-02-02, PH02-GATE-ACCOUNT-01 |
| 051 | [PH03-BE-CHT-01-01](prompts/PH03-BE-CHT-01-01.md) | BE | P0 | Triển khai CHT-01: Tạo hội thoại trực tiếp hoặc nhóm | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-02-02, PH02-BE-ACC-07-02, PH02-GATE-ACCOUNT-01 |
| 052 | [PH03-FE-SET-03-P0-01](prompts/PH03-FE-SET-03-P0-01.md) | FE | P0 | Triển khai SET-03 P0: Tài khoản đã chặn | PH01-FE-FOUNDATION-02, PH03-BE-SOC-02-02 |

## Đợt 27 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 053 | [PH03-BE-SOC-01-02](prompts/PH03-BE-SOC-01-02.md) | BE | P0 | Nghiệm thu SOC-01 và bàn giao | PH03-BE-SOC-01-01 |
| 054 | [PH03-BE-CHT-01-02](prompts/PH03-BE-CHT-01-02.md) | BE | P0 | Nghiệm thu CHT-01 và bàn giao | PH03-BE-CHT-01-01 |
| 055 | [PH03-FE-SET-03-P0-02](prompts/PH03-FE-SET-03-P0-02.md) | FE | P0 | QA SET-03 P0 trên Desktop/Mobile | PH03-FE-SET-03-P0-01 |

## Đợt 28 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 056 | [PH03-BE-SOC-03-01](prompts/PH03-BE-SOC-03-01.md) | BE | P0 | Triển khai SOC-03: Tạo bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-01-02, PH02-GATE-ACCOUNT-01 |
| 057 | [PH03-BE-CHT-02-01](prompts/PH03-BE-CHT-02-01.md) | BE | P0 | Triển khai CHT-02: Gửi tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| 058 | [PH03-BE-CHT-06-01](prompts/PH03-BE-CHT-06-01.md) | BE | P0 | Triển khai CHT-06: Trạng thái hiện diện | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| 059 | [PH03-FE-PROF-04-P0-01](prompts/PH03-FE-PROF-04-P0-01.md) | FE | P0 | Triển khai PROF-04 P0: Người theo dõi và đang theo dõi | PH01-FE-FOUNDATION-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02 |
| 060 | [PH03-FE-CHAT-03-P0-01](prompts/PH03-FE-CHAT-03-P0-01.md) | FE | P0 | Triển khai CHAT-03 P0: Tạo hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02 |

## Đợt 29 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 061 | [PH03-BE-SOC-03-02](prompts/PH03-BE-SOC-03-02.md) | BE | P0 | Nghiệm thu SOC-03 và bàn giao | PH03-BE-SOC-03-01 |
| 062 | [PH03-BE-CHT-02-02](prompts/PH03-BE-CHT-02-02.md) | BE | P0 | Nghiệm thu CHT-02 và bàn giao | PH03-BE-CHT-02-01 |
| 063 | [PH03-BE-CHT-06-02](prompts/PH03-BE-CHT-06-02.md) | BE | P0 | Nghiệm thu CHT-06 và bàn giao | PH03-BE-CHT-06-01 |
| 064 | [PH03-FE-PROF-04-P0-02](prompts/PH03-FE-PROF-04-P0-02.md) | FE | P0 | QA PROF-04 P0 trên Desktop/Mobile | PH03-FE-PROF-04-P0-01 |
| 065 | [PH03-FE-CHAT-03-P0-02](prompts/PH03-FE-CHAT-03-P0-02.md) | FE | P0 | QA CHAT-03 P0 trên Desktop/Mobile | PH03-FE-CHAT-03-P0-01 |

## Đợt 30 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 066 | [PH03-BE-SOC-06-01](prompts/PH03-BE-SOC-06-01.md) | BE | P0 | Triển khai SOC-06: Xem bài viết và danh sách bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-03-02, PH02-GATE-ACCOUNT-01 |
| 067 | [PH03-BE-CHT-03-01](prompts/PH03-BE-CHT-03-01.md) | BE | P0 | Triển khai CHT-03: Sửa và xóa tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| 068 | [PH03-BE-CHT-05-01](prompts/PH03-BE-CHT-05-01.md) | BE | P0 | Triển khai CHT-05: Trạng thái đang nhập | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| 069 | [PH03-BE-CHT-07-01](prompts/PH03-BE-CHT-07-01.md) | BE | P0 | Triển khai CHT-07: Xác nhận đã đọc | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-02-02, PH02-GATE-ACCOUNT-01 |
| 070 | [PH03-BE-FED-01-01](prompts/PH03-BE-FED-01-01.md) | BE | P0 | Triển khai FED-01: Xây dựng bản chiếu bảng tin theo dõi | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-03-02, PH03-BE-SOC-01-02, PH02-GATE-ACCOUNT-01 |
| 071 | [PH03-FE-FEED-02-P0-01](prompts/PH03-FE-FEED-02-P0-01.md) | FE | P0 | Triển khai FEED-02 P0: Tạo bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-03-02 |

## Đợt 31 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 072 | [PH03-BE-SOC-06-02](prompts/PH03-BE-SOC-06-02.md) | BE | P0 | Nghiệm thu SOC-06 và bàn giao | PH03-BE-SOC-06-01 |
| 073 | [PH03-BE-CHT-03-02](prompts/PH03-BE-CHT-03-02.md) | BE | P0 | Nghiệm thu CHT-03 và bàn giao | PH03-BE-CHT-03-01 |
| 074 | [PH03-BE-CHT-05-02](prompts/PH03-BE-CHT-05-02.md) | BE | P0 | Nghiệm thu CHT-05 và bàn giao | PH03-BE-CHT-05-01 |
| 075 | [PH03-BE-CHT-07-02](prompts/PH03-BE-CHT-07-02.md) | BE | P0 | Nghiệm thu CHT-07 và bàn giao | PH03-BE-CHT-07-01 |
| 076 | [PH03-BE-FED-01-02](prompts/PH03-BE-FED-01-02.md) | BE | P0 | Nghiệm thu FED-01 và bàn giao | PH03-BE-FED-01-01 |
| 077 | [PH03-FE-FEED-02-P0-02](prompts/PH03-FE-FEED-02-P0-02.md) | FE | P0 | QA FEED-02 P0 trên Desktop/Mobile | PH03-FE-FEED-02-P0-01 |

## Đợt 32 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 078 | [PH03-BE-SOC-04-01](prompts/PH03-BE-SOC-04-01.md) | BE | P0 | Triển khai SOC-04: Sửa bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02, PH02-GATE-ACCOUNT-01 |
| 079 | [PH03-BE-SOC-07-01](prompts/PH03-BE-SOC-07-01.md) | BE | P0 | Triển khai SOC-07: Bình luận và trả lời | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02, PH02-GATE-ACCOUNT-01 |
| 080 | [PH03-BE-CHT-04-01](prompts/PH03-BE-CHT-04-01.md) | BE | P0 | Triển khai CHT-04: Tương tác với tin nhắn | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-CHT-03-02, PH02-GATE-ACCOUNT-01 |
| 081 | [PH03-FE-PROF-01-P0-01](prompts/PH03-FE-PROF-01-P0-01.md) | FE | P0 | Triển khai PROF-01 P0: Hồ sơ của tôi | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH03-BE-SOC-06-02 |
| 082 | [PH03-FE-PROF-02-P0-01](prompts/PH03-FE-PROF-02-P0-01.md) | FE | P0 | Triển khai PROF-02 P0: Hồ sơ người dùng | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02, PH03-BE-SOC-06-02, PH03-BE-CHT-01-02 |
| 083 | [PH03-FE-CHAT-04-P0-01](prompts/PH03-FE-CHAT-04-P0-01.md) | FE | P0 | Triển khai CHAT-04 P0: Thiết lập hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02, PH03-BE-CHT-03-02 |

## Đợt 33 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 084 | [PH03-BE-SOC-04-02](prompts/PH03-BE-SOC-04-02.md) | BE | P0 | Nghiệm thu SOC-04 và bàn giao | PH03-BE-SOC-04-01 |
| 085 | [PH03-BE-SOC-07-02](prompts/PH03-BE-SOC-07-02.md) | BE | P0 | Nghiệm thu SOC-07 và bàn giao | PH03-BE-SOC-07-01 |
| 086 | [PH03-BE-CHT-04-02](prompts/PH03-BE-CHT-04-02.md) | BE | P0 | Nghiệm thu CHT-04 và bàn giao | PH03-BE-CHT-04-01 |
| 087 | [PH03-FE-PROF-01-P0-02](prompts/PH03-FE-PROF-01-P0-02.md) | FE | P0 | QA PROF-01 P0 trên Desktop/Mobile | PH03-FE-PROF-01-P0-01 |
| 088 | [PH03-FE-PROF-02-P0-02](prompts/PH03-FE-PROF-02-P0-02.md) | FE | P0 | QA PROF-02 P0 trên Desktop/Mobile | PH03-FE-PROF-02-P0-01 |
| 089 | [PH03-FE-CHAT-04-P0-02](prompts/PH03-FE-CHAT-04-P0-02.md) | FE | P0 | QA CHAT-04 P0 trên Desktop/Mobile | PH03-FE-CHAT-04-P0-01 |

## Đợt 34 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 090 | [PH03-BE-SOC-05-01](prompts/PH03-BE-SOC-05-01.md) | BE | P0 | Triển khai SOC-05: Xóa bài viết | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-04-02, PH02-GATE-ACCOUNT-01 |
| 091 | [PH03-BE-SOC-08-01](prompts/PH03-BE-SOC-08-01.md) | BE | P0 | Triển khai SOC-08: Tương tác | PH03-DATA-SOC-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-07-02, PH02-GATE-ACCOUNT-01 |
| 092 | [PH03-FE-FEED-04-P0-01](prompts/PH03-FE-FEED-04-P0-01.md) | FE | P0 | Triển khai FEED-04 P0: Sửa bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-04-02 |
| 093 | [PH03-FE-CHAT-02-P0-01](prompts/PH03-FE-CHAT-02-P0-01.md) | FE | P0 | Triển khai CHAT-02 P0: Hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-02-02, PH03-BE-CHT-03-02, PH03-BE-CHT-04-02, PH03-BE-CHT-05-02, PH03-BE-CHT-06-02, PH03-BE-CHT-07-02 |

## Đợt 35 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 094 | [PH03-BE-SOC-05-02](prompts/PH03-BE-SOC-05-02.md) | BE | P0 | Nghiệm thu SOC-05 và bàn giao | PH03-BE-SOC-05-01 |
| 095 | [PH03-BE-SOC-08-02](prompts/PH03-BE-SOC-08-02.md) | BE | P0 | Nghiệm thu SOC-08 và bàn giao | PH03-BE-SOC-08-01 |
| 096 | [PH03-FE-FEED-04-P0-02](prompts/PH03-FE-FEED-04-P0-02.md) | FE | P0 | QA FEED-04 P0 trên Desktop/Mobile | PH03-FE-FEED-04-P0-01 |
| 097 | [PH03-FE-CHAT-02-P0-02](prompts/PH03-FE-CHAT-02-P0-02.md) | FE | P0 | QA CHAT-02 P0 trên Desktop/Mobile | PH03-FE-CHAT-02-P0-01 |

## Đợt 36 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 098 | [PH03-BE-CHT-08-01](prompts/PH03-BE-CHT-08-01.md) | BE | P0 | Triển khai CHT-08: Hộp thông báo | PH03-DATA-CHT-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-08-02, PH03-BE-CHT-01-02, PH02-GATE-ACCOUNT-01 |
| 099 | [PH03-BE-FED-03-01](prompts/PH03-BE-FED-03-01.md) | BE | P0 | Triển khai FED-03: Cập nhật bản chiếu và làm mất hiệu lực bộ nhớ đệm | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-FED-01-02, PH03-BE-SOC-05-02, PH02-BE-ACC-05-02, PH02-GATE-ACCOUNT-01 |
| 100 | [PH03-FE-FEED-03-P0-01](prompts/PH03-FE-FEED-03-P0-01.md) | FE | P0 | Triển khai FEED-03 P0: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-06-02, PH03-BE-SOC-07-02, PH03-BE-SOC-08-02, PH03-BE-SOC-04-02, PH03-BE-SOC-05-02 |

## Đợt 37 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 101 | [PH03-BE-CHT-08-02](prompts/PH03-BE-CHT-08-02.md) | BE | P0 | Nghiệm thu CHT-08 và bàn giao | PH03-BE-CHT-08-01 |
| 102 | [PH03-BE-FED-03-02](prompts/PH03-BE-FED-03-02.md) | BE | P0 | Nghiệm thu FED-03 và bàn giao | PH03-BE-FED-03-01 |
| 103 | [PH03-FE-FEED-03-P0-02](prompts/PH03-FE-FEED-03-P0-02.md) | FE | P0 | QA FEED-03 P0 trên Desktop/Mobile | PH03-FE-FEED-03-P0-01 |

## Đợt 38 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 104 | [PH03-BE-FED-02-01](prompts/PH03-BE-FED-02-01.md) | BE | P0 | Triển khai FED-02: Đọc bảng tin bằng con trỏ | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-FED-03-02, PH02-GATE-ACCOUNT-01 |
| 105 | [PH03-FE-NOTI-01-P0-01](prompts/PH03-FE-NOTI-01-P0-01.md) | FE | P0 | Triển khai NOTI-01 P0: Thông báo | PH01-FE-FOUNDATION-02, PH03-BE-CHT-08-02 |
| 106 | [PH03-FE-CHAT-01-P0-01](prompts/PH03-FE-CHAT-01-P0-01.md) | FE | P0 | Triển khai CHAT-01 P0: Danh sách hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02, PH03-BE-CHT-08-02 |

## Đợt 39 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 107 | [PH03-BE-FED-02-02](prompts/PH03-BE-FED-02-02.md) | BE | P0 | Nghiệm thu FED-02 và bàn giao | PH03-BE-FED-02-01 |
| 108 | [PH03-FE-NOTI-01-P0-02](prompts/PH03-FE-NOTI-01-P0-02.md) | FE | P0 | QA NOTI-01 P0 trên Desktop/Mobile | PH03-FE-NOTI-01-P0-01 |
| 109 | [PH03-FE-CHAT-01-P0-02](prompts/PH03-FE-CHAT-01-P0-02.md) | FE | P0 | QA CHAT-01 P0 trên Desktop/Mobile | PH03-FE-CHAT-01-P0-01 |

## Đợt 40 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 110 | [PH03-FE-FEED-01-P0-01](prompts/PH03-FE-FEED-01-P0-01.md) | FE | P0 | Triển khai FEED-01 P0: Bảng tin | PH01-FE-FOUNDATION-02, PH03-BE-FED-02-02, PH03-BE-SOC-03-02, PH03-BE-SOC-08-02, PH03-BE-CHT-08-02 |
| 111 | [PH03-DATA-RECOVERY-01](prompts/PH03-DATA-RECOVERY-01.md) | DATA | P0 | Khôi phục P0 và rebuild Feed | PH03-BE-FED-02-02, PH03-BE-CHT-08-02 |

## Đợt 41 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 112 | [PH03-FE-FEED-01-P0-02](prompts/PH03-FE-FEED-01-P0-02.md) | FE | P0 | QA FEED-01 P0 trên Desktop/Mobile | PH03-FE-FEED-01-P0-01 |

## Đợt 42 — PH03

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 113 | [G1-01](prompts/G1-01.md) | GATE | P0 | Nghiệm thu P0 trước mọi P1 | PH02-BE-ACC-01-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02, PH02-BE-ACC-05-02, PH02-BE-ACC-07-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02, PH03-BE-SOC-03-02, PH03-BE-SOC-04-02, PH03-BE-SOC-05-02, PH03-BE-SOC-06-02, PH03-BE-SOC-07-02, PH03-BE-SOC-08-02, PH03-BE-CHT-01-02, PH03-BE-CHT-02-02, PH03-BE-CHT-03-02, PH03-BE-CHT-04-02, PH03-BE-CHT-05-02, PH03-BE-CHT-06-02, PH03-BE-CHT-07-02, PH03-BE-CHT-08-02, PH03-BE-FED-01-02, PH03-BE-FED-02-02, PH03-BE-FED-03-02, PH02-FE-AUTH-01-P0-02, PH02-FE-AUTH-02-P0-02, PH02-FE-AUTH-03-P0-02, PH03-FE-FEED-01-P0-02, PH03-FE-FEED-02-P0-02, PH03-FE-FEED-03-P0-02, PH03-FE-FEED-04-P0-02, PH03-FE-PROF-01-P0-02, PH03-FE-PROF-02-P0-02, PH03-FE-PROF-04-P0-02, PH03-FE-SET-01-P0-02, PH03-FE-SET-02-P0-02, PH03-FE-SET-03-P0-02, PH03-FE-NOTI-01-P0-02, PH03-FE-CHAT-01-P0-02, PH03-FE-CHAT-02-P0-02, PH03-FE-CHAT-03-P0-02, PH03-FE-CHAT-04-P0-02, PH03-FE-SYS-01-P0-02, PH03-DATA-RECOVERY-01, PH01-BE-CI-01 |

## Đợt 43 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 114 | [PH04-BE-CONTRACT-01](prompts/PH04-BE-CONTRACT-01.md) | BE | P1 | Khóa bổ sung hợp đồng P1 | G1-01 |

## Đợt 44 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 115 | [PH04-DATA-ACC-P1-01](prompts/PH04-DATA-ACC-P1-01.md) | DATA | P1 | Thiết kế lược đồ ACC P1 | PH04-BE-CONTRACT-01, PH02-DATA-ACC-P0-03 |
| 116 | [PH04-DATA-COM-P1-01](prompts/PH04-DATA-COM-P1-01.md) | DATA | P1 | Thiết kế lược đồ COM P1 | PH04-BE-CONTRACT-01 |
| 117 | [PH04-DATA-MED-P1-01](prompts/PH04-DATA-MED-P1-01.md) | DATA | P1 | Thiết kế lược đồ MED P1 | PH04-BE-CONTRACT-01 |
| 118 | [PH04-DATA-SOC-P1-01](prompts/PH04-DATA-SOC-P1-01.md) | DATA | P1 | Thiết kế lược đồ SOC P1 | PH04-BE-CONTRACT-01, PH03-DATA-SOC-P0-03 |
| 119 | [PH04-DATA-CHT-P1-01](prompts/PH04-DATA-CHT-P1-01.md) | DATA | P1 | Thiết kế lược đồ CHT P1 | PH04-BE-CONTRACT-01, PH03-DATA-CHT-P0-03 |
| 120 | [PH05-DATA-DEL-P1-01](prompts/PH05-DATA-DEL-P1-01.md) | DATA | P1 | Thiết kế lược đồ DEL P1 | PH04-BE-CONTRACT-01 |
| 121 | [PH05-DATA-MOD-P1-01](prompts/PH05-DATA-MOD-P1-01.md) | DATA | P1 | Thiết kế lược đồ MOD P1 | PH04-BE-CONTRACT-01 |

## Đợt 45 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 122 | [PH04-DATA-ACC-P1-02](prompts/PH04-DATA-ACC-P1-02.md) | DATA | P1 | Migration và fixture ACC P1 | PH04-DATA-ACC-P1-01 |
| 123 | [PH04-DATA-COM-P1-02](prompts/PH04-DATA-COM-P1-02.md) | DATA | P1 | Migration và fixture COM P1 | PH04-DATA-COM-P1-01 |
| 124 | [PH04-DATA-MED-P1-02](prompts/PH04-DATA-MED-P1-02.md) | DATA | P1 | Migration và fixture MED P1 | PH04-DATA-MED-P1-01 |
| 125 | [PH04-DATA-SOC-P1-02](prompts/PH04-DATA-SOC-P1-02.md) | DATA | P1 | Migration và fixture SOC P1 | PH04-DATA-SOC-P1-01 |
| 126 | [PH04-DATA-CHT-P1-02](prompts/PH04-DATA-CHT-P1-02.md) | DATA | P1 | Migration và fixture CHT P1 | PH04-DATA-CHT-P1-01 |
| 127 | [PH05-DATA-DEL-P1-02](prompts/PH05-DATA-DEL-P1-02.md) | DATA | P1 | Migration và fixture DEL P1 | PH05-DATA-DEL-P1-01 |
| 128 | [PH05-DATA-MOD-P1-02](prompts/PH05-DATA-MOD-P1-02.md) | DATA | P1 | Migration và fixture MOD P1 | PH05-DATA-MOD-P1-01 |

## Đợt 46 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 129 | [PH04-DATA-ACC-P1-03](prompts/PH04-DATA-ACC-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu ACC P1 | PH04-DATA-ACC-P1-02 |
| 130 | [PH04-DATA-COM-P1-03](prompts/PH04-DATA-COM-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu COM P1 | PH04-DATA-COM-P1-02 |
| 131 | [PH04-DATA-MED-P1-03](prompts/PH04-DATA-MED-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu MED P1 | PH04-DATA-MED-P1-02 |
| 132 | [PH04-DATA-SOC-P1-03](prompts/PH04-DATA-SOC-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu SOC P1 | PH04-DATA-SOC-P1-02 |
| 133 | [PH04-DATA-CHT-P1-03](prompts/PH04-DATA-CHT-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu CHT P1 | PH04-DATA-CHT-P1-02 |
| 134 | [PH05-DATA-DEL-P1-03](prompts/PH05-DATA-DEL-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu DEL P1 | PH05-DATA-DEL-P1-02 |
| 135 | [PH05-DATA-MOD-P1-03](prompts/PH05-DATA-MOD-P1-03.md) | DATA | P1 | Kiểm chứng dữ liệu MOD P1 | PH05-DATA-MOD-P1-02 |

## Đợt 47 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 136 | [PH04-BE-ACC-08-01](prompts/PH04-BE-ACC-08-01.md) | BE | P1 | Triển khai ACC-08: Yêu cầu OTP khôi phục mật khẩu | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-04-02 |
| 137 | [PH04-BE-ACC-10-01](prompts/PH04-BE-ACC-10-01.md) | BE | P1 | Triển khai ACC-10: Đăng nhập bằng Google OAuth | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH02-BE-ACC-03-02 |
| 138 | [PH04-BE-SOC-10-01](prompts/PH04-BE-SOC-10-01.md) | BE | P1 | Triển khai SOC-10: Chia sẻ bài viết ra nền tảng ngoài | PH04-DATA-SOC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-06-02 |
| 139 | [PH04-BE-COM-01-01](prompts/PH04-BE-COM-01-01.md) | BE | P1 | Triển khai COM-01: Tạo và cập nhật cộng đồng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |
| 140 | [PH04-BE-MED-01-01](prompts/PH04-BE-MED-01-01.md) | BE | P1 | Triển khai MED-01: Tạo phiên tải lên | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01 |

## Đợt 48 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 141 | [PH04-BE-ACC-08-02](prompts/PH04-BE-ACC-08-02.md) | BE | P1 | Nghiệm thu ACC-08 và bàn giao | PH04-BE-ACC-08-01 |
| 142 | [PH04-BE-ACC-10-02](prompts/PH04-BE-ACC-10-02.md) | BE | P1 | Nghiệm thu ACC-10 và bàn giao | PH04-BE-ACC-10-01 |
| 143 | [PH04-BE-SOC-10-02](prompts/PH04-BE-SOC-10-02.md) | BE | P1 | Nghiệm thu SOC-10 và bàn giao | PH04-BE-SOC-10-01 |
| 144 | [PH04-BE-COM-01-02](prompts/PH04-BE-COM-01-02.md) | BE | P1 | Nghiệm thu COM-01 và bàn giao | PH04-BE-COM-01-01 |
| 145 | [PH04-BE-MED-01-02](prompts/PH04-BE-MED-01-02.md) | BE | P1 | Nghiệm thu MED-01 và bàn giao | PH04-BE-MED-01-01 |

## Đợt 49 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 146 | [PH04-BE-ACC-09-01](prompts/PH04-BE-ACC-09-01.md) | BE | P1 | Triển khai ACC-09: Đặt lại mật khẩu bằng OTP | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-ACC-08-02 |
| 147 | [PH04-BE-COM-02-01](prompts/PH04-BE-COM-02-01.md) | BE | P1 | Triển khai COM-02: Mời, tham gia và rời cộng đồng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-01-02 |
| 148 | [PH04-BE-MED-02-01](prompts/PH04-BE-MED-02-01.md) | BE | P1 | Triển khai MED-02: Tải trực tiếp | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-01-02 |
| 149 | [PH04-FE-AUTH-02-P1-01](prompts/PH04-FE-AUTH-02-P1-01.md) | FE | P1 | Triển khai AUTH-02 P1: Đăng nhập | PH01-FE-FOUNDATION-02, PH04-BE-ACC-10-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01, PH02-FE-AUTH-02-P0-02 |
| 150 | [PH04-FE-AUTH-03-P1-01](prompts/PH04-FE-AUTH-03-P1-01.md) | FE | P1 | Triển khai AUTH-03 P1: Đăng ký | PH01-FE-FOUNDATION-02, PH04-BE-ACC-10-02, G1-01, PH04-BE-CONTRACT-01, PH02-FE-AUTH-03-P0-02 |
| 151 | [PH04-FE-AUTH-04-P1-01](prompts/PH04-FE-AUTH-04-P1-01.md) | FE | P1 | Triển khai AUTH-04 P1: Quên mật khẩu | PH01-FE-FOUNDATION-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 50 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 152 | [PH04-BE-ACC-09-02](prompts/PH04-BE-ACC-09-02.md) | BE | P1 | Nghiệm thu ACC-09 và bàn giao | PH04-BE-ACC-09-01 |
| 153 | [PH04-BE-COM-02-02](prompts/PH04-BE-COM-02-02.md) | BE | P1 | Nghiệm thu COM-02 và bàn giao | PH04-BE-COM-02-01 |
| 154 | [PH04-BE-MED-02-02](prompts/PH04-BE-MED-02-02.md) | BE | P1 | Nghiệm thu MED-02 và bàn giao | PH04-BE-MED-02-01 |
| 155 | [PH04-FE-AUTH-02-P1-02](prompts/PH04-FE-AUTH-02-P1-02.md) | FE | P1 | QA AUTH-02 P1 trên Desktop/Mobile | PH04-FE-AUTH-02-P1-01 |
| 156 | [PH04-FE-AUTH-03-P1-02](prompts/PH04-FE-AUTH-03-P1-02.md) | FE | P1 | QA AUTH-03 P1 trên Desktop/Mobile | PH04-FE-AUTH-03-P1-01 |
| 157 | [PH04-FE-AUTH-04-P1-02](prompts/PH04-FE-AUTH-04-P1-02.md) | FE | P1 | QA AUTH-04 P1 trên Desktop/Mobile | PH04-FE-AUTH-04-P1-01 |

## Đợt 51 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 158 | [PH04-BE-COM-03-01](prompts/PH04-BE-COM-03-01.md) | BE | P1 | Triển khai COM-03: Vai trò và quyền | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-02-02 |
| 159 | [PH04-BE-MED-03-01](prompts/PH04-BE-MED-03-01.md) | BE | P1 | Triển khai MED-03: Hoàn tất và xác minh tải lên | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-02-02 |
| 160 | [PH04-FE-AUTH-05-P1-01](prompts/PH04-FE-AUTH-05-P1-01.md) | FE | P1 | Triển khai AUTH-05 P1: Đặt lại mật khẩu | PH01-FE-FOUNDATION-02, PH04-BE-ACC-09-02, G1-01, PH04-BE-CONTRACT-01 |
| 161 | [PH04-FE-SET-02-P1-01](prompts/PH04-FE-SET-02-P1-01.md) | FE | P1 | Triển khai SET-02 P1: Bảo mật tài khoản | PH01-FE-FOUNDATION-02, PH04-BE-ACC-09-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-SET-02-P0-02 |
| 162 | [PH04-FE-COMM-01-P1-01](prompts/PH04-FE-COMM-01-P1-01.md) | FE | P1 | Triển khai COMM-01 P1: Khám phá cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, G1-01, PH04-BE-CONTRACT-01 |
| 163 | [PH04-FE-COMM-03-P1-01](prompts/PH04-FE-COMM-03-P1-01.md) | FE | P1 | Triển khai COMM-03 P1: Mời và tham gia cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-02-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 52 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 164 | [PH04-BE-COM-03-02](prompts/PH04-BE-COM-03-02.md) | BE | P1 | Nghiệm thu COM-03 và bàn giao | PH04-BE-COM-03-01 |
| 165 | [PH04-BE-MED-03-02](prompts/PH04-BE-MED-03-02.md) | BE | P1 | Nghiệm thu MED-03 và bàn giao | PH04-BE-MED-03-01 |
| 166 | [PH04-FE-AUTH-05-P1-02](prompts/PH04-FE-AUTH-05-P1-02.md) | FE | P1 | QA AUTH-05 P1 trên Desktop/Mobile | PH04-FE-AUTH-05-P1-01 |
| 167 | [PH04-FE-SET-02-P1-02](prompts/PH04-FE-SET-02-P1-02.md) | FE | P1 | QA SET-02 P1 trên Desktop/Mobile | PH04-FE-SET-02-P1-01 |
| 168 | [PH04-FE-COMM-01-P1-02](prompts/PH04-FE-COMM-01-P1-02.md) | FE | P1 | QA COMM-01 P1 trên Desktop/Mobile | PH04-FE-COMM-01-P1-01 |
| 169 | [PH04-FE-COMM-03-P1-02](prompts/PH04-FE-COMM-03-P1-02.md) | FE | P1 | QA COMM-03 P1 trên Desktop/Mobile | PH04-FE-COMM-03-P1-01 |

## Đợt 53 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 170 | [PH04-BE-COM-04-01](prompts/PH04-BE-COM-04-01.md) | BE | P1 | Triển khai COM-04: Tạo kênh văn bản hoặc kênh thoại | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-03-02, PH03-BE-CHT-02-02 |
| 171 | [PH04-BE-COM-05-01](prompts/PH04-BE-COM-05-01.md) | BE | P1 | Triển khai COM-05: Điều hành thành viên | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-03-02 |
| 172 | [PH04-BE-MED-04-01](prompts/PH04-BE-MED-04-01.md) | BE | P1 | Triển khai MED-04: Xử lý phương tiện | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-03-02 |
| 173 | [PH04-FE-FEED-02-P1-01](prompts/PH04-FE-FEED-02-P1-01.md) | FE | P1 | Triển khai FEED-02 P1: Tạo bài viết | PH01-FE-FOUNDATION-02, PH04-BE-MED-01-02, PH04-BE-MED-03-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-02-P0-02 |
| 174 | [PH04-FE-COMM-04-P1-01](prompts/PH04-FE-COMM-04-P1-01.md) | FE | P1 | Triển khai COMM-04 P1: Vai trò và quyền | PH01-FE-FOUNDATION-02, PH04-BE-COM-03-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 54 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 175 | [PH04-BE-COM-04-02](prompts/PH04-BE-COM-04-02.md) | BE | P1 | Nghiệm thu COM-04 và bàn giao | PH04-BE-COM-04-01 |
| 176 | [PH04-BE-COM-05-02](prompts/PH04-BE-COM-05-02.md) | BE | P1 | Nghiệm thu COM-05 và bàn giao | PH04-BE-COM-05-01 |
| 177 | [PH04-BE-MED-04-02](prompts/PH04-BE-MED-04-02.md) | BE | P1 | Nghiệm thu MED-04 và bàn giao | PH04-BE-MED-04-01 |
| 178 | [PH04-FE-FEED-02-P1-02](prompts/PH04-FE-FEED-02-P1-02.md) | FE | P1 | QA FEED-02 P1 trên Desktop/Mobile | PH04-FE-FEED-02-P1-01 |
| 179 | [PH04-FE-COMM-04-P1-02](prompts/PH04-FE-COMM-04-P1-02.md) | FE | P1 | QA COMM-04 P1 trên Desktop/Mobile | PH04-FE-COMM-04-P1-01 |

## Đợt 55 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 180 | [PH04-BE-ACC-06-01](prompts/PH04-BE-ACC-06-01.md) | BE | P1 | Triển khai ACC-06: Cập nhật tham chiếu avatar | PH04-DATA-ACC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH02-BE-ACC-05-02 |
| 181 | [PH04-BE-SOC-09-01](prompts/PH04-BE-SOC-09-01.md) | BE | P1 | Triển khai SOC-09: Tạo bài viết video | PH04-DATA-SOC-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH03-BE-SOC-04-02 |
| 182 | [PH04-BE-RTC-01-01](prompts/PH04-BE-RTC-01-01.md) | BE | P1 | Triển khai RTC-01: Cấp token tham gia LiveKit | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-04-02, PH04-BE-COM-05-02 |
| 183 | [PH04-BE-MED-05-01](prompts/PH04-BE-MED-05-01.md) | BE | P1 | Triển khai MED-05: Xóa và dọn dẹp phương tiện | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02 |
| 184 | [PH04-BE-MED-06-01](prompts/PH04-BE-MED-06-01.md) | BE | P1 | Triển khai MED-06: Phương tiện cho tin nhắn thoại | PH04-DATA-MED-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02, PH03-BE-CHT-02-02 |
| 185 | [PH04-FE-COMM-02-P1-01](prompts/PH04-FE-COMM-02-P1-01.md) | FE | P1 | Triển khai COMM-02 P1: Tổng quan cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, PH04-BE-COM-04-02, G1-01, PH04-BE-CONTRACT-01 |
| 186 | [PH04-FE-COMM-05-P1-01](prompts/PH04-FE-COMM-05-P1-01.md) | FE | P1 | Triển khai COMM-05 P1: Quản lý kênh | PH01-FE-FOUNDATION-02, PH04-BE-COM-04-02, G1-01, PH04-BE-CONTRACT-01 |
| 187 | [PH04-FE-COMM-06-P1-01](prompts/PH04-FE-COMM-06-P1-01.md) | FE | P1 | Triển khai COMM-06 P1: Điều hành thành viên | PH01-FE-FOUNDATION-02, PH04-BE-COM-05-02, G1-01, PH04-BE-CONTRACT-01 |
| 188 | [PH04-FE-COMM-07-P1-01](prompts/PH04-FE-COMM-07-P1-01.md) | FE | P1 | Triển khai COMM-07 P1: Kênh văn bản | PH01-FE-FOUNDATION-02, PH04-BE-COM-04-02, PH03-BE-CHT-02-02, PH03-BE-CHT-07-02, G1-01, PH04-BE-CONTRACT-01 |
| 189 | [PH04-FE-MEDIA-01-P1-01](prompts/PH04-FE-MEDIA-01-P1-01.md) | FE | P1 | Triển khai MEDIA-01 P1: Tải phương tiện | PH01-FE-FOUNDATION-02, PH04-BE-MED-01-02, PH04-BE-MED-02-02, PH04-BE-MED-03-02, PH04-BE-MED-04-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 56 — PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 190 | [PH04-BE-ACC-06-02](prompts/PH04-BE-ACC-06-02.md) | BE | P1 | Nghiệm thu ACC-06 và bàn giao | PH04-BE-ACC-06-01 |
| 191 | [PH04-BE-SOC-09-02](prompts/PH04-BE-SOC-09-02.md) | BE | P1 | Nghiệm thu SOC-09 và bàn giao | PH04-BE-SOC-09-01 |
| 192 | [PH04-BE-RTC-01-02](prompts/PH04-BE-RTC-01-02.md) | BE | P1 | Nghiệm thu RTC-01 và bàn giao | PH04-BE-RTC-01-01 |
| 193 | [PH04-BE-MED-05-02](prompts/PH04-BE-MED-05-02.md) | BE | P1 | Nghiệm thu MED-05 và bàn giao | PH04-BE-MED-05-01 |
| 194 | [PH04-BE-MED-06-02](prompts/PH04-BE-MED-06-02.md) | BE | P1 | Nghiệm thu MED-06 và bàn giao | PH04-BE-MED-06-01 |
| 195 | [PH04-FE-COMM-02-P1-02](prompts/PH04-FE-COMM-02-P1-02.md) | FE | P1 | QA COMM-02 P1 trên Desktop/Mobile | PH04-FE-COMM-02-P1-01 |
| 196 | [PH04-FE-COMM-05-P1-02](prompts/PH04-FE-COMM-05-P1-02.md) | FE | P1 | QA COMM-05 P1 trên Desktop/Mobile | PH04-FE-COMM-05-P1-01 |
| 197 | [PH04-FE-COMM-06-P1-02](prompts/PH04-FE-COMM-06-P1-02.md) | FE | P1 | QA COMM-06 P1 trên Desktop/Mobile | PH04-FE-COMM-06-P1-01 |
| 198 | [PH04-FE-COMM-07-P1-02](prompts/PH04-FE-COMM-07-P1-02.md) | FE | P1 | QA COMM-07 P1 trên Desktop/Mobile | PH04-FE-COMM-07-P1-01 |
| 199 | [PH04-FE-MEDIA-01-P1-02](prompts/PH04-FE-MEDIA-01-P1-02.md) | FE | P1 | QA MEDIA-01 P1 trên Desktop/Mobile | PH04-FE-MEDIA-01-P1-01 |

## Đợt 57 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 200 | [PH04-BE-RTC-02-01](prompts/PH04-BE-RTC-02-01.md) | BE | P1 | Triển khai RTC-02: Thoại, video và chia sẻ màn hình | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-01-02 |
| 201 | [PH04-BE-CHT-09-01](prompts/PH04-BE-CHT-09-01.md) | BE | P1 | Triển khai CHT-09: Lời mời cuộc gọi | PH04-DATA-CHT-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-01-02, PH03-BE-CHT-01-02 |
| 202 | [PH05-BE-MOD-01-01](prompts/PH05-BE-MOD-01-01.md) | BE | P1 | Triển khai MOD-01: Gửi báo cáo vi phạm | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-SOC-09-02, PH04-BE-COM-05-02, PH04-BE-MED-05-02 |
| 203 | [PH04-FE-FEED-05-P1-01](prompts/PH04-FE-FEED-05-P1-01.md) | FE | P1 | Triển khai FEED-05 P1: Bài viết video đang xử lý | PH01-FE-FOUNDATION-02, PH04-BE-SOC-09-02, PH04-BE-MED-04-02, G1-01, PH04-BE-CONTRACT-01 |
| 204 | [PH04-FE-PROF-03-P1-01](prompts/PH04-FE-PROF-03-P1-01.md) | FE | P1 | Triển khai PROF-03 P1: Chỉnh sửa hồ sơ | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH04-BE-ACC-06-02, PH04-BE-MED-01-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 58 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 205 | [PH04-BE-RTC-02-02](prompts/PH04-BE-RTC-02-02.md) | BE | P1 | Nghiệm thu RTC-02 và bàn giao | PH04-BE-RTC-02-01 |
| 206 | [PH04-BE-CHT-09-02](prompts/PH04-BE-CHT-09-02.md) | BE | P1 | Nghiệm thu CHT-09 và bàn giao | PH04-BE-CHT-09-01 |
| 207 | [PH05-BE-MOD-01-02](prompts/PH05-BE-MOD-01-02.md) | BE | P1 | Nghiệm thu MOD-01 và bàn giao | PH05-BE-MOD-01-01 |
| 208 | [PH04-FE-FEED-05-P1-02](prompts/PH04-FE-FEED-05-P1-02.md) | FE | P1 | QA FEED-05 P1 trên Desktop/Mobile | PH04-FE-FEED-05-P1-01 |
| 209 | [PH04-FE-PROF-03-P1-02](prompts/PH04-FE-PROF-03-P1-02.md) | FE | P1 | QA PROF-03 P1 trên Desktop/Mobile | PH04-FE-PROF-03-P1-01 |

## Đợt 59 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 210 | [PH04-BE-RTC-03-01](prompts/PH04-BE-RTC-03-01.md) | BE | P1 | Triển khai RTC-03: Phát trực tiếp màn hình trong phòng | PH04-DATA-COM-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-RTC-02-02 |
| 211 | [PH05-BE-ACC-11-01](prompts/PH05-BE-ACC-11-01.md) | BE | P1 | Triển khai ACC-11: Yêu cầu xóa và khôi phục tài khoản | PH05-DATA-DEL-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-COM-05-02, PH04-BE-MED-05-02, PH04-BE-SOC-10-02, PH04-BE-CHT-09-02 |
| 212 | [PH05-BE-MOD-02-01](prompts/PH05-BE-MOD-02-01.md) | BE | P1 | Triển khai MOD-02: Duyệt hàng đợi báo cáo | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-01-02 |
| 213 | [PH04-FE-FEED-01-P1-01](prompts/PH04-FE-FEED-01-P1-01.md) | FE | P1 | Triển khai FEED-01 P1: Bảng tin | PH01-FE-FOUNDATION-02, PH04-BE-SOC-10-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-01-P0-02 |
| 214 | [PH04-FE-FEED-03-P1-01](prompts/PH04-FE-FEED-03-P1-01.md) | FE | P1 | Triển khai FEED-03 P1: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH04-BE-SOC-10-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-03-P0-02 |
| 215 | [PH04-FE-CHAT-02-P1-01](prompts/PH04-FE-CHAT-02-P1-01.md) | FE | P1 | Triển khai CHAT-02 P1: Hội thoại | PH01-FE-FOUNDATION-02, PH04-BE-MED-06-02, PH04-BE-CHT-09-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-CHAT-02-P0-02 |
| 216 | [PH04-FE-RTC-01-P1-01](prompts/PH04-FE-RTC-01-P1-01.md) | FE | P1 | Triển khai RTC-01 P1: Lời mời cuộc gọi | PH01-FE-FOUNDATION-02, PH04-BE-CHT-09-02, PH04-BE-RTC-01-02, G1-01, PH04-BE-CONTRACT-01 |
| 217 | [PH04-FE-RTC-02-P1-01](prompts/PH04-FE-RTC-02-P1-01.md) | FE | P1 | Triển khai RTC-02 P1: Phòng thoại và video | PH01-FE-FOUNDATION-02, PH04-BE-RTC-01-02, PH04-BE-RTC-02-02, G1-01, PH04-BE-CONTRACT-01 |
| 218 | [PH05-FE-MOD-01-P1-01](prompts/PH05-FE-MOD-01-P1-01.md) | FE | P1 | Triển khai MOD-01 P1: Báo cáo nội dung | PH01-FE-FOUNDATION-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01 |

## Đợt 60 — PH04, PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 219 | [PH04-BE-RTC-03-02](prompts/PH04-BE-RTC-03-02.md) | BE | P1 | Nghiệm thu RTC-03 và bàn giao | PH04-BE-RTC-03-01 |
| 220 | [PH05-BE-ACC-11-02](prompts/PH05-BE-ACC-11-02.md) | BE | P1 | Nghiệm thu ACC-11 và bàn giao | PH05-BE-ACC-11-01 |
| 221 | [PH05-BE-MOD-02-02](prompts/PH05-BE-MOD-02-02.md) | BE | P1 | Nghiệm thu MOD-02 và bàn giao | PH05-BE-MOD-02-01 |
| 222 | [PH04-FE-FEED-01-P1-02](prompts/PH04-FE-FEED-01-P1-02.md) | FE | P1 | QA FEED-01 P1 trên Desktop/Mobile | PH04-FE-FEED-01-P1-01 |
| 223 | [PH04-FE-FEED-03-P1-02](prompts/PH04-FE-FEED-03-P1-02.md) | FE | P1 | QA FEED-03 P1 trên Desktop/Mobile | PH04-FE-FEED-03-P1-01 |
| 224 | [PH04-FE-CHAT-02-P1-02](prompts/PH04-FE-CHAT-02-P1-02.md) | FE | P1 | QA CHAT-02 P1 trên Desktop/Mobile | PH04-FE-CHAT-02-P1-01 |
| 225 | [PH04-FE-RTC-01-P1-02](prompts/PH04-FE-RTC-01-P1-02.md) | FE | P1 | QA RTC-01 P1 trên Desktop/Mobile | PH04-FE-RTC-01-P1-01 |
| 226 | [PH04-FE-RTC-02-P1-02](prompts/PH04-FE-RTC-02-P1-02.md) | FE | P1 | QA RTC-02 P1 trên Desktop/Mobile | PH04-FE-RTC-02-P1-01 |
| 227 | [PH05-FE-MOD-01-P1-02](prompts/PH05-FE-MOD-01-P1-02.md) | FE | P1 | QA MOD-01 P1 trên Desktop/Mobile | PH05-FE-MOD-01-P1-01 |

## Đợt 61 — PH05, PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 228 | [PH05-BE-MOD-03-01](prompts/PH05-BE-MOD-03-01.md) | BE | P1 | Triển khai MOD-03: Áp dụng hành động điều hành | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-02-02 |
| 229 | [PH04-FE-RTC-03-P1-01](prompts/PH04-FE-RTC-03-P1-01.md) | FE | P1 | Triển khai RTC-03 P1: Chia sẻ màn hình | PH01-FE-FOUNDATION-02, PH04-BE-RTC-03-02, G1-01, PH04-BE-CONTRACT-01 |
| 230 | [PH05-FE-MOD-02-P1-01](prompts/PH05-FE-MOD-02-P1-01.md) | FE | P1 | Triển khai MOD-02 P1: Hàng đợi điều hành | PH01-FE-FOUNDATION-02, PH05-BE-MOD-02-02, G1-01, PH04-BE-CONTRACT-01 |
| 231 | [PH05-BE-DELETION-01](prompts/PH05-BE-DELETION-01.md) | BE | P1 | Xóa tài khoản: Ẩn/ẩn danh post/comment, dọn follow/block và bảo vệ retention_hold | PH05-BE-ACC-11-02 |

## Đợt 62 — PH05, PH04

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 232 | [PH05-BE-MOD-03-02](prompts/PH05-BE-MOD-03-02.md) | BE | P1 | Nghiệm thu MOD-03 và bàn giao | PH05-BE-MOD-03-01 |
| 233 | [PH04-FE-RTC-03-P1-02](prompts/PH04-FE-RTC-03-P1-02.md) | FE | P1 | QA RTC-03 P1 trên Desktop/Mobile | PH04-FE-RTC-03-P1-01 |
| 234 | [PH05-FE-MOD-02-P1-02](prompts/PH05-FE-MOD-02-P1-02.md) | FE | P1 | QA MOD-02 P1 trên Desktop/Mobile | PH05-FE-MOD-02-P1-01 |
| 235 | [PH05-BE-DELETION-02](prompts/PH05-BE-DELETION-02.md) | BE | P1 | Xóa tài khoản: Xóa FeedEntry/UserSummary/cache trong 5 phút | PH05-BE-DELETION-01 |

## Đợt 63 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 236 | [PH05-BE-MOD-04-01](prompts/PH05-BE-MOD-04-01.md) | BE | P1 | Triển khai MOD-04: Đóng báo cáo và kiểm toán | PH05-DATA-MOD-P1-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH05-BE-MOD-03-02 |
| 237 | [PH05-BE-DELETION-03](prompts/PH05-BE-DELETION-03.md) | BE | P1 | Xóa tài khoản: Ẩn PII profile, giữ lịch sử người khác theo policy, xử lý quyền/reconnect | PH05-BE-DELETION-02 |

## Đợt 64 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 238 | [PH05-BE-MOD-04-02](prompts/PH05-BE-MOD-04-02.md) | BE | P1 | Nghiệm thu MOD-04 và bàn giao | PH05-BE-MOD-04-01 |
| 239 | [PH05-BE-DELETION-04](prompts/PH05-BE-DELETION-04.md) | BE | P1 | Xóa tài khoản: Vô hiệu membership/role/invite và chuyển owner trước purge | PH05-BE-DELETION-03 |

## Đợt 65 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 240 | [PH05-FE-MOD-03-P1-01](prompts/PH05-FE-MOD-03-P1-01.md) | FE | P1 | Triển khai MOD-03 P1: Chi tiết điều hành | PH01-FE-FOUNDATION-02, PH05-BE-MOD-03-02, PH05-BE-MOD-04-02, G1-01, PH04-BE-CONTRACT-01 |
| 241 | [PH05-BE-DELETION-05](prompts/PH05-BE-DELETION-05.md) | BE | P1 | Xóa tài khoản: Đối soát tham chiếu, dọn object không dùng, giữ evidence có hold | PH05-BE-DELETION-04 |

## Đợt 66 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 242 | [PH05-FE-MOD-03-P1-02](prompts/PH05-FE-MOD-03-P1-02.md) | FE | P1 | QA MOD-03 P1 trên Desktop/Mobile | PH05-FE-MOD-03-P1-01 |
| 243 | [PH05-BE-DELETION-06](prompts/PH05-BE-DELETION-06.md) | BE | P1 | Xóa tài khoản: Đối soát ack/retry/timeouts, cancel trong grace, chặn completed khi thiếu participant | PH05-BE-DELETION-05 |

## Đợt 67 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 244 | [PH05-BE-DELETION-07](prompts/PH05-BE-DELETION-07.md) | BE | P1 | Xóa tài khoản: Kiểm thử tích hợp hủy/purge/race/duplicate, ẩn <=5 phút, grace 30 ngày, PII <=45 ngày | PH05-BE-DELETION-06 |

## Đợt 68 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 245 | [PH05-BE-DELETION-08](prompts/PH05-BE-DELETION-08.md) | BE | P1 | Xóa tài khoản: Bàn giao xóa liên dịch vụ và restore không làm sống lại dữ liệu đã xóa | PH05-BE-DELETION-07 |

## Đợt 69 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 246 | [PH05-FE-SET-04-P1-01](prompts/PH05-FE-SET-04-P1-01.md) | FE | P1 | Triển khai SET-04 P1: Xóa tài khoản | PH01-FE-FOUNDATION-02, PH05-BE-ACC-11-02, G1-01, PH04-BE-CONTRACT-01, PH05-BE-DELETION-08 |
| 247 | [PH05-DATA-RESTORE-01](prompts/PH05-DATA-RESTORE-01.md) | DATA | P1 | Khôi phục Media và dữ liệu P1 | PH05-BE-DELETION-08, PH05-BE-MOD-04-02 |

## Đợt 70 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 248 | [PH05-FE-SET-04-P1-02](prompts/PH05-FE-SET-04-P1-02.md) | FE | P1 | QA SET-04 P1 trên Desktop/Mobile | PH05-FE-SET-04-P1-01 |

## Đợt 71 — PH05

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 249 | [G2-01](prompts/G2-01.md) | GATE | P1 | Nghiệm thu P1 trước P2 | PH04-BE-ACC-06-02, PH04-BE-ACC-08-02, PH04-BE-ACC-09-02, PH04-BE-ACC-10-02, PH04-BE-SOC-09-02, PH04-BE-SOC-10-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, PH04-BE-COM-03-02, PH04-BE-COM-04-02, PH04-BE-COM-05-02, PH04-BE-RTC-01-02, PH04-BE-RTC-02-02, PH04-BE-RTC-03-02, PH04-BE-CHT-09-02, PH04-BE-MED-01-02, PH04-BE-MED-02-02, PH04-BE-MED-03-02, PH04-BE-MED-04-02, PH04-BE-MED-05-02, PH04-BE-MED-06-02, PH05-BE-ACC-11-02, PH05-BE-MOD-01-02, PH05-BE-MOD-02-02, PH05-BE-MOD-03-02, PH05-BE-MOD-04-02, PH04-FE-AUTH-02-P1-02, PH04-FE-AUTH-03-P1-02, PH04-FE-AUTH-04-P1-02, PH04-FE-AUTH-05-P1-02, PH04-FE-FEED-01-P1-02, PH04-FE-FEED-02-P1-02, PH04-FE-FEED-03-P1-02, PH04-FE-FEED-05-P1-02, PH04-FE-PROF-03-P1-02, PH04-FE-SET-02-P1-02, PH05-FE-SET-04-P1-02, PH04-FE-COMM-01-P1-02, PH04-FE-COMM-02-P1-02, PH04-FE-COMM-03-P1-02, PH04-FE-COMM-04-P1-02, PH04-FE-COMM-05-P1-02, PH04-FE-COMM-06-P1-02, PH04-FE-COMM-07-P1-02, PH04-FE-CHAT-02-P1-02, PH04-FE-RTC-01-P1-02, PH04-FE-RTC-02-P1-02, PH04-FE-RTC-03-P1-02, PH04-FE-MEDIA-01-P1-02, PH05-FE-MOD-01-P1-02, PH05-FE-MOD-02-P1-02, PH05-FE-MOD-03-P1-02, PH05-BE-DELETION-08, PH05-DATA-RESTORE-01 |

## Đợt 72 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 250 | [PH06-BE-CONTRACT-01](prompts/PH06-BE-CONTRACT-01.md) | BE | P2 | Quyết định phạm vi và hợp đồng P2 | G2-01 |

## Đợt 73 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 251 | [PH06-DATA-MKT-P2-01](prompts/PH06-DATA-MKT-P2-01.md) | DATA | P2 | Thiết kế lược đồ MKT P2 | PH06-BE-CONTRACT-01 |
| 252 | [PH06-DATA-AI-P2-01](prompts/PH06-DATA-AI-P2-01.md) | DATA | P2 | Thiết kế lược đồ AI P2 | PH06-BE-CONTRACT-01 |

## Đợt 74 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 253 | [PH06-DATA-MKT-P2-02](prompts/PH06-DATA-MKT-P2-02.md) | DATA | P2 | Migration và fixture MKT P2 | PH06-DATA-MKT-P2-01 |
| 254 | [PH06-DATA-AI-P2-02](prompts/PH06-DATA-AI-P2-02.md) | DATA | P2 | Migration và fixture AI P2 | PH06-DATA-AI-P2-01 |

## Đợt 75 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 255 | [PH06-DATA-MKT-P2-03](prompts/PH06-DATA-MKT-P2-03.md) | DATA | P2 | Kiểm chứng dữ liệu MKT P2 | PH06-DATA-MKT-P2-02 |
| 256 | [PH06-DATA-AI-P2-03](prompts/PH06-DATA-AI-P2-03.md) | DATA | P2 | Kiểm chứng dữ liệu AI P2 | PH06-DATA-AI-P2-02 |

## Đợt 76 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 257 | [PH06-BE-MKT-01-01](prompts/PH06-BE-MKT-01-01.md) | BE | P2 | Triển khai MKT-01: Tạo và sửa tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-04-02 |
| 258 | [PH06-BE-AI-01-01](prompts/PH06-BE-AI-01-01.md) | BE | P2 | Triển khai AI-01: Tạo embedding | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH03-BE-SOC-05-02, PH05-BE-ACC-11-02 |

## Đợt 77 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 259 | [PH06-BE-MKT-01-02](prompts/PH06-BE-MKT-01-02.md) | BE | P2 | Nghiệm thu MKT-01 và bàn giao | PH06-BE-MKT-01-01 |
| 260 | [PH06-BE-AI-01-02](prompts/PH06-BE-AI-01-02.md) | BE | P2 | Nghiệm thu AI-01 và bàn giao | PH06-BE-AI-01-01 |

## Đợt 78 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 261 | [PH06-BE-FED-05-01](prompts/PH06-BE-FED-05-01.md) | BE | P2 | Triển khai FED-05: Cập nhật embedding sở thích | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-01-02, PH03-BE-SOC-08-02 |
| 262 | [PH06-BE-MKT-02-01](prompts/PH06-BE-MKT-02-01.md) | BE | P2 | Triển khai MKT-02: Duyệt và tìm kiếm tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02 |
| 263 | [PH06-BE-MKT-03-01](prompts/PH06-BE-MKT-03-01.md) | BE | P2 | Triển khai MKT-03: Cập nhật và giữ tồn kho | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02 |
| 264 | [PH06-BE-MKT-07-01](prompts/PH06-BE-MKT-07-01.md) | BE | P2 | Triển khai MKT-07: Phương tiện của tin đăng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-01-02, PH04-BE-MED-05-02 |
| 265 | [PH06-BE-AI-02-01](prompts/PH06-BE-AI-02-01.md) | BE | P2 | Triển khai AI-02: Tìm kiếm ngữ nghĩa | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-01-02 |
| 266 | [PH06-BE-AI-05-01](prompts/PH06-BE-AI-05-01.md) | BE | P2 | Triển khai AI-05: Chuyển lời nói thành văn bản | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH04-BE-MED-06-02, PH06-BE-AI-01-02 |

## Đợt 79 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 267 | [PH06-BE-FED-05-02](prompts/PH06-BE-FED-05-02.md) | BE | P2 | Nghiệm thu FED-05 và bàn giao | PH06-BE-FED-05-01 |
| 268 | [PH06-BE-MKT-02-02](prompts/PH06-BE-MKT-02-02.md) | BE | P2 | Nghiệm thu MKT-02 và bàn giao | PH06-BE-MKT-02-01 |
| 269 | [PH06-BE-MKT-03-02](prompts/PH06-BE-MKT-03-02.md) | BE | P2 | Nghiệm thu MKT-03 và bàn giao | PH06-BE-MKT-03-01 |
| 270 | [PH06-BE-MKT-07-02](prompts/PH06-BE-MKT-07-02.md) | BE | P2 | Nghiệm thu MKT-07 và bàn giao | PH06-BE-MKT-07-01 |
| 271 | [PH06-BE-AI-02-02](prompts/PH06-BE-AI-02-02.md) | BE | P2 | Nghiệm thu AI-02 và bàn giao | PH06-BE-AI-02-01 |
| 272 | [PH06-BE-AI-05-02](prompts/PH06-BE-AI-05-02.md) | BE | P2 | Nghiệm thu AI-05 và bàn giao | PH06-BE-AI-05-01 |

## Đợt 80 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 273 | [PH06-BE-FED-04-01](prompts/PH06-BE-FED-04-01.md) | BE | P2 | Triển khai FED-04: Sinh ứng viên và chấm điểm gợi ý | PH03-DATA-FED-P0-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-FED-05-02, PH03-BE-FED-02-02 |
| 274 | [PH06-BE-MKT-04-01](prompts/PH06-BE-MKT-04-01.md) | BE | P2 | Triển khai MKT-04: Tạo đơn hàng | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-03-02, PH06-BE-MKT-07-02 |
| 275 | [PH06-BE-AI-03-01](prompts/PH06-BE-AI-03-01.md) | BE | P2 | Triển khai AI-03: Trợ lý RAG | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-02-02 |
| 276 | [PH06-BE-AI-06-01](prompts/PH06-BE-AI-06-01.md) | BE | P2 | Triển khai AI-06: Đánh chỉ mục OpenSearch - tùy chọn | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-02-02, PH06-BE-MKT-02-02 |
| 277 | [PH06-FE-FEED-03-P2-01](prompts/PH06-FE-FEED-03-P2-01.md) | FE | P2 | Triển khai FEED-03 P2: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH06-BE-AI-05-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-FEED-03-P1-02 |
| 278 | [PH06-FE-DISC-01-P2-01](prompts/PH06-FE-DISC-01-P2-01.md) | FE | P2 | Triển khai DISC-01 P2: Tìm kiếm | PH01-FE-FOUNDATION-02, PH06-BE-AI-02-02, PH06-BE-MKT-02-02, PH03-BE-SOC-06-02, G2-01, PH06-BE-CONTRACT-01 |
| 279 | [PH06-FE-CHAT-02-P2-01](prompts/PH06-FE-CHAT-02-P2-01.md) | FE | P2 | Triển khai CHAT-02 P2: Hội thoại | PH01-FE-FOUNDATION-02, PH06-BE-AI-05-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-CHAT-02-P1-02 |
| 280 | [PH06-FE-MKT-01-P2-01](prompts/PH06-FE-MKT-01-P2-01.md) | FE | P2 | Triển khai MKT-01 P2: Chợ | PH01-FE-FOUNDATION-02, PH06-BE-MKT-02-02, G2-01, PH06-BE-CONTRACT-01 |
| 281 | [PH06-FE-MKT-03-P2-01](prompts/PH06-FE-MKT-03-P2-01.md) | FE | P2 | Triển khai MKT-03 P2: Tạo hoặc sửa tin đăng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-01-02, PH06-BE-MKT-03-02, PH06-BE-MKT-07-02, G2-01, PH06-BE-CONTRACT-01 |

## Đợt 81 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 282 | [PH06-BE-FED-04-02](prompts/PH06-BE-FED-04-02.md) | BE | P2 | Nghiệm thu FED-04 và bàn giao | PH06-BE-FED-04-01 |
| 283 | [PH06-BE-MKT-04-02](prompts/PH06-BE-MKT-04-02.md) | BE | P2 | Nghiệm thu MKT-04 và bàn giao | PH06-BE-MKT-04-01 |
| 284 | [PH06-BE-AI-03-02](prompts/PH06-BE-AI-03-02.md) | BE | P2 | Nghiệm thu AI-03 và bàn giao | PH06-BE-AI-03-01 |
| 285 | [PH06-BE-AI-06-02](prompts/PH06-BE-AI-06-02.md) | BE | P2 | Nghiệm thu AI-06 và bàn giao | PH06-BE-AI-06-01 |
| 286 | [PH06-FE-FEED-03-P2-02](prompts/PH06-FE-FEED-03-P2-02.md) | FE | P2 | QA FEED-03 P2 trên Desktop/Mobile | PH06-FE-FEED-03-P2-01 |
| 287 | [PH06-FE-DISC-01-P2-02](prompts/PH06-FE-DISC-01-P2-02.md) | FE | P2 | QA DISC-01 P2 trên Desktop/Mobile | PH06-FE-DISC-01-P2-01 |
| 288 | [PH06-FE-CHAT-02-P2-02](prompts/PH06-FE-CHAT-02-P2-02.md) | FE | P2 | QA CHAT-02 P2 trên Desktop/Mobile | PH06-FE-CHAT-02-P2-01 |
| 289 | [PH06-FE-MKT-01-P2-02](prompts/PH06-FE-MKT-01-P2-02.md) | FE | P2 | QA MKT-01 P2 trên Desktop/Mobile | PH06-FE-MKT-01-P2-01 |
| 290 | [PH06-FE-MKT-03-P2-02](prompts/PH06-FE-MKT-03-P2-02.md) | FE | P2 | QA MKT-03 P2 trên Desktop/Mobile | PH06-FE-MKT-03-P2-01 |

## Đợt 82 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 291 | [PH06-BE-MKT-06-01](prompts/PH06-BE-MKT-06-01.md) | BE | P2 | Triển khai MKT-06: Trạng thái đơn hàng và Saga đơn giản hóa | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-04-02 |
| 292 | [PH06-BE-AI-04-01](prompts/PH06-BE-AI-04-01.md) | BE | P2 | Triển khai AI-04: Tóm tắt tin nhắn hoặc kênh | PH06-DATA-AI-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-AI-03-02, PH03-BE-CHT-03-02 |
| 293 | [PH06-FE-FEED-01-P2-01](prompts/PH06-FE-FEED-01-P2-01.md) | FE | P2 | Triển khai FEED-01 P2: Bảng tin | PH01-FE-FOUNDATION-02, PH06-BE-FED-04-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-FEED-01-P1-02 |
| 294 | [PH06-FE-MKT-02-P2-01](prompts/PH06-FE-MKT-02-P2-01.md) | FE | P2 | Triển khai MKT-02 P2: Chi tiết tin đăng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-02-02, PH06-BE-MKT-07-02, PH06-BE-MKT-04-02, PH03-BE-CHT-01-02, G2-01, PH06-BE-CONTRACT-01 |
| 295 | [PH06-FE-MKT-04-P2-01](prompts/PH06-FE-MKT-04-P2-01.md) | FE | P2 | Triển khai MKT-04 P2: Xác nhận đơn hàng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-03-02, PH06-BE-MKT-04-02, G2-01, PH06-BE-CONTRACT-01 |
| 296 | [PH06-FE-AI-01-P2-01](prompts/PH06-FE-AI-01-P2-01.md) | FE | P2 | Triển khai AI-01 P2: Trợ lý AI | PH01-FE-FOUNDATION-02, PH06-BE-AI-03-02, G2-01, PH06-BE-CONTRACT-01 |

## Đợt 83 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 297 | [PH06-BE-MKT-06-02](prompts/PH06-BE-MKT-06-02.md) | BE | P2 | Nghiệm thu MKT-06 và bàn giao | PH06-BE-MKT-06-01 |
| 298 | [PH06-BE-AI-04-02](prompts/PH06-BE-AI-04-02.md) | BE | P2 | Nghiệm thu AI-04 và bàn giao | PH06-BE-AI-04-01 |
| 299 | [PH06-FE-FEED-01-P2-02](prompts/PH06-FE-FEED-01-P2-02.md) | FE | P2 | QA FEED-01 P2 trên Desktop/Mobile | PH06-FE-FEED-01-P2-01 |
| 300 | [PH06-FE-MKT-02-P2-02](prompts/PH06-FE-MKT-02-P2-02.md) | FE | P2 | QA MKT-02 P2 trên Desktop/Mobile | PH06-FE-MKT-02-P2-01 |
| 301 | [PH06-FE-MKT-04-P2-02](prompts/PH06-FE-MKT-04-P2-02.md) | FE | P2 | QA MKT-04 P2 trên Desktop/Mobile | PH06-FE-MKT-04-P2-01 |
| 302 | [PH06-FE-AI-01-P2-02](prompts/PH06-FE-AI-01-P2-02.md) | FE | P2 | QA AI-01 P2 trên Desktop/Mobile | PH06-FE-AI-01-P2-01 |

## Đợt 84 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 303 | [PH06-BE-MKT-05-01](prompts/PH06-BE-MKT-05-01.md) | BE | P2 | Triển khai MKT-05: Thanh toán giả lập | PH06-DATA-MKT-P2-03, PH01-BE-PLATFORM-01, PH01-BE-CI-01, PH06-BE-MKT-06-02 |
| 304 | [PH06-FE-AI-02-P2-01](prompts/PH06-FE-AI-02-P2-01.md) | FE | P2 | Triển khai AI-02 P2: Tóm tắt hội thoại hoặc kênh | PH01-FE-FOUNDATION-02, PH06-BE-AI-04-02, G2-01, PH06-BE-CONTRACT-01 |

## Đợt 85 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 305 | [PH06-BE-MKT-05-02](prompts/PH06-BE-MKT-05-02.md) | BE | P2 | Nghiệm thu MKT-05 và bàn giao | PH06-BE-MKT-05-01 |
| 306 | [PH06-FE-AI-02-P2-02](prompts/PH06-FE-AI-02-P2-02.md) | FE | P2 | QA AI-02 P2 trên Desktop/Mobile | PH06-FE-AI-02-P2-01 |

## Đợt 86 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 307 | [PH06-FE-MKT-05-P2-01](prompts/PH06-FE-MKT-05-P2-01.md) | FE | P2 | Triển khai MKT-05 P2: Thanh toán trực tiếp với người bán | PH01-FE-FOUNDATION-02, PH06-BE-MKT-05-02, G2-01, PH06-BE-CONTRACT-01 |
| 308 | [PH06-FE-MKT-06-P2-01](prompts/PH06-FE-MKT-06-P2-01.md) | FE | P2 | Triển khai MKT-06 P2: Đơn hàng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-06-02, PH06-BE-MKT-04-02, PH06-BE-MKT-05-02, G2-01, PH06-BE-CONTRACT-01 |
| 309 | [PH06-DATA-LIFECYCLE-01](prompts/PH06-DATA-LIFECYCLE-01.md) | DATA | P2 | Xóa, phục hồi và rebuild P2 | PH06-BE-MKT-05-02, PH06-BE-AI-05-02, PH06-BE-FED-04-02 |

## Đợt 87 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 310 | [PH06-FE-MKT-05-P2-02](prompts/PH06-FE-MKT-05-P2-02.md) | FE | P2 | QA MKT-05 P2 trên Desktop/Mobile | PH06-FE-MKT-05-P2-01 |
| 311 | [PH06-FE-MKT-06-P2-02](prompts/PH06-FE-MKT-06-P2-02.md) | FE | P2 | QA MKT-06 P2 trên Desktop/Mobile | PH06-FE-MKT-06-P2-01 |

## Đợt 88 — PH06

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 312 | [G3-01](prompts/G3-01.md) | GATE | P2 | Nghiệm thu P2 và đóng phạm vi | PH06-BE-FED-04-02, PH06-BE-FED-05-02, PH06-BE-MKT-01-02, PH06-BE-MKT-02-02, PH06-BE-MKT-03-02, PH06-BE-MKT-04-02, PH06-BE-MKT-05-02, PH06-BE-MKT-06-02, PH06-BE-MKT-07-02, PH06-BE-AI-01-02, PH06-BE-AI-02-02, PH06-BE-AI-03-02, PH06-BE-AI-04-02, PH06-BE-AI-05-02, PH06-BE-AI-06-02, PH06-FE-FEED-01-P2-02, PH06-FE-FEED-03-P2-02, PH06-FE-DISC-01-P2-02, PH06-FE-CHAT-02-P2-02, PH06-FE-MKT-01-P2-02, PH06-FE-MKT-02-P2-02, PH06-FE-MKT-03-P2-02, PH06-FE-MKT-04-P2-02, PH06-FE-MKT-05-P2-02, PH06-FE-MKT-06-P2-02, PH06-FE-AI-01-P2-02, PH06-FE-AI-02-P2-02, PH06-DATA-LIFECYCLE-01 |

## Đợt 89 — PH07

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 313 | [PH07-GOV-HARDEN-01](prompts/PH07-GOV-HARDEN-01.md) | GOV | P0 | Đo tải và xử lý bottleneck | G3-01 |

## Đợt 90 — PH07

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 314 | [PH07-GOV-HARDEN-02](prompts/PH07-GOV-HARDEN-02.md) | GOV | P0 | Rà soát bảo mật và chuỗi cung ứng | PH07-GOV-HARDEN-01 |

## Đợt 91 — PH07

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 315 | [PH07-GOV-HARDEN-03](prompts/PH07-GOV-HARDEN-03.md) | GOV | P0 | Di trú, khôi phục và rollback ứng viên | PH07-GOV-HARDEN-02 |

## Đợt 92 — PH07

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 316 | [PH07-GOV-HARDEN-04](prompts/PH07-GOV-HARDEN-04.md) | GOV | P0 | Đồng bộ hồ sơ bàn giao | PH07-GOV-HARDEN-03 |

## Đợt 93 — PH08

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 317 | [PH08-GOV-REHEARSAL-01](prompts/PH08-GOV-REHEARSAL-01.md) | GOV | P0 | Diễn tập phát hành từ môi trường sạch | PH07-GOV-HARDEN-04 |

## Đợt 94 — PH08

| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |
|---:|---|---|---|---|---|
| 318 | [G4-01](prompts/G4-01.md) | GATE | P0 | Nghiệm thu phát hành | PH08-GOV-REHEARSAL-01 |

## Cách dùng

1. Chọn prompt đầu tiên của đợt sớm nhất còn khả thi, hoặc dùng `python -X utf8 scripts/task_gate.py next` để xem trạng thái thật.
2. Dùng `prompt ID --preview` để đọc. Chỉ dùng `prompt ID` sau `check ID` trả exit 0.
3. Hoàn thành đủ DoR → start → completion → review → accept. `DONE` hợp lệ mới mở dependency; không đánh dấu cả đợt là hoàn thành cùng lúc.
4. Nếu nguồn, evidence hoặc dependency đổi, trạng thái thành `STALE`/`BLOCKED`; quay lại cổng thay vì tiếp tục theo số thứ tự.
