# Danh mục FRONTEND

Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.

## PH01 — Nền tảng Backend, Data và Frontend

### PH01-FE-FOUNDATION — Nền tảng Angular theo thiết kế đã khóa

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH01-FE-FOUNDATION-01](prompts/PH01-FE-FOUNDATION-01.md) | Dựng app shell, token, navigation và trạng thái dùng chung | G0-01 |
| [PH01-FE-FOUNDATION-02](prompts/PH01-FE-FOUNDATION-02.md) | HTTP/auth/realtime adapters có xử lý lỗi và vòng đời | PH01-FE-FOUNDATION-01 |

## PH02 — Tài khoản P0

### PH02-FE-AUTH-01-P0 — Chào mừng P0

Ưu tiên P0; miền cross-cutting. Route: /. Vai trò: Khách. Chỉ bật ACC-01, ACC-02 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-FE-AUTH-01-P0-01](prompts/PH02-FE-AUTH-01-P0-01.md) | Triển khai AUTH-01 P0: Chào mừng | PH01-FE-FOUNDATION-02, PH02-BE-ACC-01-02, PH02-BE-ACC-02-02 |
| [PH02-FE-AUTH-01-P0-02](prompts/PH02-FE-AUTH-01-P0-02.md) | QA AUTH-01 P0 trên Desktop/Mobile | PH02-FE-AUTH-01-P0-01 |

### PH02-FE-AUTH-02-P0 — Đăng nhập P0

Ưu tiên P0; miền cross-cutting. Route: /dang-nhap. Vai trò: Khách. Chỉ bật ACC-02, ACC-03 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-FE-AUTH-02-P0-01](prompts/PH02-FE-AUTH-02-P0-01.md) | Triển khai AUTH-02 P0: Đăng nhập | PH01-FE-FOUNDATION-02, PH02-BE-ACC-02-02, PH02-BE-ACC-03-02 |
| [PH02-FE-AUTH-02-P0-02](prompts/PH02-FE-AUTH-02-P0-02.md) | QA AUTH-02 P0 trên Desktop/Mobile | PH02-FE-AUTH-02-P0-01 |

### PH02-FE-AUTH-03-P0 — Đăng ký P0

Ưu tiên P0; miền cross-cutting. Route: /dang-ky. Vai trò: Khách. Chỉ bật ACC-01 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH02-FE-AUTH-03-P0-01](prompts/PH02-FE-AUTH-03-P0-01.md) | Triển khai AUTH-03 P0: Đăng ký | PH01-FE-FOUNDATION-02, PH02-BE-ACC-01-02 |
| [PH02-FE-AUTH-03-P0-02](prompts/PH02-FE-AUTH-03-P0-02.md) | QA AUTH-03 P0 trên Desktop/Mobile | PH02-FE-AUTH-03-P0-01 |

## PH03 — Mạng xã hội, Bảng tin, Trò chuyện P0

### PH03-FE-FEED-01-P0 — Bảng tin P0

Ưu tiên P0; miền cross-cutting. Route: /bang-tin. Vai trò: Người dùng. Chỉ bật FED-02, SOC-03, SOC-08, CHT-08 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-FEED-01-P0-01](prompts/PH03-FE-FEED-01-P0-01.md) | Triển khai FEED-01 P0: Bảng tin | PH01-FE-FOUNDATION-02, PH03-BE-FED-02-02, PH03-BE-SOC-03-02, PH03-BE-SOC-08-02, PH03-BE-CHT-08-02 |
| [PH03-FE-FEED-01-P0-02](prompts/PH03-FE-FEED-01-P0-02.md) | QA FEED-01 P0 trên Desktop/Mobile | PH03-FE-FEED-01-P0-01 |

### PH03-FE-FEED-02-P0 — Tạo bài viết P0

Ưu tiên P0; miền cross-cutting. Route: /bai-viet/moi. Vai trò: Người dùng. Chỉ bật SOC-03 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-FEED-02-P0-01](prompts/PH03-FE-FEED-02-P0-01.md) | Triển khai FEED-02 P0: Tạo bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-03-02 |
| [PH03-FE-FEED-02-P0-02](prompts/PH03-FE-FEED-02-P0-02.md) | QA FEED-02 P0 trên Desktop/Mobile | PH03-FE-FEED-02-P0-01 |

### PH03-FE-FEED-03-P0 — Chi tiết bài viết P0

Ưu tiên P0; miền cross-cutting. Route: /bai-viet/:id. Vai trò: Người xem, Người dùng. Chỉ bật SOC-06, SOC-07, SOC-08, SOC-04, SOC-05 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-FEED-03-P0-01](prompts/PH03-FE-FEED-03-P0-01.md) | Triển khai FEED-03 P0: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-06-02, PH03-BE-SOC-07-02, PH03-BE-SOC-08-02, PH03-BE-SOC-04-02, PH03-BE-SOC-05-02 |
| [PH03-FE-FEED-03-P0-02](prompts/PH03-FE-FEED-03-P0-02.md) | QA FEED-03 P0 trên Desktop/Mobile | PH03-FE-FEED-03-P0-01 |

### PH03-FE-FEED-04-P0 — Sửa bài viết P0

Ưu tiên P0; miền cross-cutting. Route: /bai-viet/:id/sua. Vai trò: Chủ sở hữu. Chỉ bật SOC-04 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-FEED-04-P0-01](prompts/PH03-FE-FEED-04-P0-01.md) | Triển khai FEED-04 P0: Sửa bài viết | PH01-FE-FOUNDATION-02, PH03-BE-SOC-04-02 |
| [PH03-FE-FEED-04-P0-02](prompts/PH03-FE-FEED-04-P0-02.md) | QA FEED-04 P0 trên Desktop/Mobile | PH03-FE-FEED-04-P0-01 |

### PH03-FE-PROF-01-P0 — Hồ sơ của tôi P0

Ưu tiên P0; miền cross-cutting. Route: /toi. Vai trò: Người dùng. Chỉ bật ACC-05, SOC-06 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-PROF-01-P0-01](prompts/PH03-FE-PROF-01-P0-01.md) | Triển khai PROF-01 P0: Hồ sơ của tôi | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH03-BE-SOC-06-02 |
| [PH03-FE-PROF-01-P0-02](prompts/PH03-FE-PROF-01-P0-02.md) | QA PROF-01 P0 trên Desktop/Mobile | PH03-FE-PROF-01-P0-01 |

### PH03-FE-PROF-02-P0 — Hồ sơ người dùng P0

Ưu tiên P0; miền cross-cutting. Route: /nguoi-dung/:id. Vai trò: Người xem. Chỉ bật ACC-05, SOC-01, SOC-02, SOC-06, CHT-01 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-PROF-02-P0-01](prompts/PH03-FE-PROF-02-P0-01.md) | Triển khai PROF-02 P0: Hồ sơ người dùng | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02, PH03-BE-SOC-06-02, PH03-BE-CHT-01-02 |
| [PH03-FE-PROF-02-P0-02](prompts/PH03-FE-PROF-02-P0-02.md) | QA PROF-02 P0 trên Desktop/Mobile | PH03-FE-PROF-02-P0-01 |

### PH03-FE-PROF-04-P0 — Người theo dõi và đang theo dõi P0

Ưu tiên P0; miền cross-cutting. Route: /nguoi-dung/:id/ket-noi. Vai trò: Người dùng. Chỉ bật SOC-01, SOC-02 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-PROF-04-P0-01](prompts/PH03-FE-PROF-04-P0-01.md) | Triển khai PROF-04 P0: Người theo dõi và đang theo dõi | PH01-FE-FOUNDATION-02, PH03-BE-SOC-01-02, PH03-BE-SOC-02-02 |
| [PH03-FE-PROF-04-P0-02](prompts/PH03-FE-PROF-04-P0-02.md) | QA PROF-04 P0 trên Desktop/Mobile | PH03-FE-PROF-04-P0-01 |

### PH03-FE-SET-01-P0 — Quyền riêng tư P0

Ưu tiên P0; miền cross-cutting. Route: /thiet-lap/quyen-rieng-tu. Vai trò: Người dùng. Chỉ bật ACC-07 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-SET-01-P0-01](prompts/PH03-FE-SET-01-P0-01.md) | Triển khai SET-01 P0: Quyền riêng tư | PH01-FE-FOUNDATION-02, PH02-BE-ACC-07-02 |
| [PH03-FE-SET-01-P0-02](prompts/PH03-FE-SET-01-P0-02.md) | QA SET-01 P0 trên Desktop/Mobile | PH03-FE-SET-01-P0-01 |

### PH03-FE-SET-02-P0 — Bảo mật tài khoản P0

Ưu tiên P0; miền cross-cutting. Route: /thiet-lap/bao-mat. Vai trò: Người dùng. Chỉ bật ACC-03, ACC-04 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-SET-02-P0-01](prompts/PH03-FE-SET-02-P0-01.md) | Triển khai SET-02 P0: Bảo mật tài khoản | PH01-FE-FOUNDATION-02, PH02-BE-ACC-03-02, PH02-BE-ACC-04-02 |
| [PH03-FE-SET-02-P0-02](prompts/PH03-FE-SET-02-P0-02.md) | QA SET-02 P0 trên Desktop/Mobile | PH03-FE-SET-02-P0-01 |

### PH03-FE-SET-03-P0 — Tài khoản đã chặn P0

Ưu tiên P0; miền cross-cutting. Route: /thiet-lap/da-chan. Vai trò: Người dùng. Chỉ bật SOC-02 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-SET-03-P0-01](prompts/PH03-FE-SET-03-P0-01.md) | Triển khai SET-03 P0: Tài khoản đã chặn | PH01-FE-FOUNDATION-02, PH03-BE-SOC-02-02 |
| [PH03-FE-SET-03-P0-02](prompts/PH03-FE-SET-03-P0-02.md) | QA SET-03 P0 trên Desktop/Mobile | PH03-FE-SET-03-P0-01 |

### PH03-FE-NOTI-01-P0 — Thông báo P0

Ưu tiên P0; miền cross-cutting. Route: /thong-bao. Vai trò: Người dùng. Chỉ bật CHT-08 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-NOTI-01-P0-01](prompts/PH03-FE-NOTI-01-P0-01.md) | Triển khai NOTI-01 P0: Thông báo | PH01-FE-FOUNDATION-02, PH03-BE-CHT-08-02 |
| [PH03-FE-NOTI-01-P0-02](prompts/PH03-FE-NOTI-01-P0-02.md) | QA NOTI-01 P0 trên Desktop/Mobile | PH03-FE-NOTI-01-P0-01 |

### PH03-FE-CHAT-01-P0 — Danh sách hội thoại P0

Ưu tiên P0; miền cross-cutting. Route: /tin-nhan. Vai trò: Người dùng. Chỉ bật CHT-01, CHT-08 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-CHAT-01-P0-01](prompts/PH03-FE-CHAT-01-P0-01.md) | Triển khai CHAT-01 P0: Danh sách hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02, PH03-BE-CHT-08-02 |
| [PH03-FE-CHAT-01-P0-02](prompts/PH03-FE-CHAT-01-P0-02.md) | QA CHAT-01 P0 trên Desktop/Mobile | PH03-FE-CHAT-01-P0-01 |

### PH03-FE-CHAT-02-P0 — Hội thoại P0

Ưu tiên P0; miền cross-cutting. Route: /tin-nhan/:id. Vai trò: Thành viên hội thoại. Chỉ bật CHT-02, CHT-03, CHT-04, CHT-05, CHT-06, CHT-07 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-CHAT-02-P0-01](prompts/PH03-FE-CHAT-02-P0-01.md) | Triển khai CHAT-02 P0: Hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-02-02, PH03-BE-CHT-03-02, PH03-BE-CHT-04-02, PH03-BE-CHT-05-02, PH03-BE-CHT-06-02, PH03-BE-CHT-07-02 |
| [PH03-FE-CHAT-02-P0-02](prompts/PH03-FE-CHAT-02-P0-02.md) | QA CHAT-02 P0 trên Desktop/Mobile | PH03-FE-CHAT-02-P0-01 |

### PH03-FE-CHAT-03-P0 — Tạo hội thoại P0

Ưu tiên P0; miền cross-cutting. Route: /tin-nhan/moi. Vai trò: Người dùng. Chỉ bật CHT-01 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-CHAT-03-P0-01](prompts/PH03-FE-CHAT-03-P0-01.md) | Triển khai CHAT-03 P0: Tạo hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02 |
| [PH03-FE-CHAT-03-P0-02](prompts/PH03-FE-CHAT-03-P0-02.md) | QA CHAT-03 P0 trên Desktop/Mobile | PH03-FE-CHAT-03-P0-01 |

### PH03-FE-CHAT-04-P0 — Thiết lập hội thoại P0

Ưu tiên P0; miền cross-cutting. Route: /tin-nhan/:id/thiet-lap. Vai trò: Thành viên, Quản trị nhóm. Chỉ bật CHT-01, CHT-03 tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-CHAT-04-P0-01](prompts/PH03-FE-CHAT-04-P0-01.md) | Triển khai CHAT-04 P0: Thiết lập hội thoại | PH01-FE-FOUNDATION-02, PH03-BE-CHT-01-02, PH03-BE-CHT-03-02 |
| [PH03-FE-CHAT-04-P0-02](prompts/PH03-FE-CHAT-04-P0-02.md) | QA CHAT-04 P0 trên Desktop/Mobile | PH03-FE-CHAT-04-P0-01 |

### PH03-FE-SYS-01-P0 — Trạng thái tải, rỗng, lỗi và ngoại tuyến P0

Ưu tiên P0; miền cross-cutting. Route: toàn ứng dụng. Vai trò: Mọi vai trò. Chỉ bật trạng thái hệ thống tại P0. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH03-FE-SYS-01-P0-01](prompts/PH03-FE-SYS-01-P0-01.md) | Triển khai SYS-01 P0: Trạng thái tải, rỗng, lỗi và ngoại tuyến | PH01-FE-FOUNDATION-02 |
| [PH03-FE-SYS-01-P0-02](prompts/PH03-FE-SYS-01-P0-02.md) | QA SYS-01 P0 trên Desktop/Mobile | PH03-FE-SYS-01-P0-01 |

## PH04 — Cộng đồng, RTC, Phương tiện và tài khoản P1

### PH04-FE-AUTH-02-P1 — Đăng nhập P1

Ưu tiên P1; miền cross-cutting. Route: /dang-nhap. Vai trò: Khách. Chỉ bật ACC-10, ACC-08 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-AUTH-02-P1-01](prompts/PH04-FE-AUTH-02-P1-01.md) | Triển khai AUTH-02 P1: Đăng nhập | PH01-FE-FOUNDATION-02, PH04-BE-ACC-10-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01, PH02-FE-AUTH-02-P0-02 |
| [PH04-FE-AUTH-02-P1-02](prompts/PH04-FE-AUTH-02-P1-02.md) | QA AUTH-02 P1 trên Desktop/Mobile | PH04-FE-AUTH-02-P1-01 |

### PH04-FE-AUTH-03-P1 — Đăng ký P1

Ưu tiên P1; miền cross-cutting. Route: /dang-ky. Vai trò: Khách. Chỉ bật ACC-10 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-AUTH-03-P1-01](prompts/PH04-FE-AUTH-03-P1-01.md) | Triển khai AUTH-03 P1: Đăng ký | PH01-FE-FOUNDATION-02, PH04-BE-ACC-10-02, G1-01, PH04-BE-CONTRACT-01, PH02-FE-AUTH-03-P0-02 |
| [PH04-FE-AUTH-03-P1-02](prompts/PH04-FE-AUTH-03-P1-02.md) | QA AUTH-03 P1 trên Desktop/Mobile | PH04-FE-AUTH-03-P1-01 |

### PH04-FE-AUTH-04-P1 — Quên mật khẩu P1

Ưu tiên P1; miền cross-cutting. Route: /quen-mat-khau. Vai trò: Khách. Chỉ bật ACC-08 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-AUTH-04-P1-01](prompts/PH04-FE-AUTH-04-P1-01.md) | Triển khai AUTH-04 P1: Quên mật khẩu | PH01-FE-FOUNDATION-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-AUTH-04-P1-02](prompts/PH04-FE-AUTH-04-P1-02.md) | QA AUTH-04 P1 trên Desktop/Mobile | PH04-FE-AUTH-04-P1-01 |

### PH04-FE-AUTH-05-P1 — Đặt lại mật khẩu P1

Ưu tiên P1; miền cross-cutting. Route: /dat-lai-mat-khau. Vai trò: Khách. Chỉ bật ACC-09 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-AUTH-05-P1-01](prompts/PH04-FE-AUTH-05-P1-01.md) | Triển khai AUTH-05 P1: Đặt lại mật khẩu | PH01-FE-FOUNDATION-02, PH04-BE-ACC-09-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-AUTH-05-P1-02](prompts/PH04-FE-AUTH-05-P1-02.md) | QA AUTH-05 P1 trên Desktop/Mobile | PH04-FE-AUTH-05-P1-01 |

### PH04-FE-FEED-01-P1 — Bảng tin P1

Ưu tiên P1; miền cross-cutting. Route: /bang-tin. Vai trò: Người dùng. Chỉ bật SOC-10, MOD-01 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-FEED-01-P1-01](prompts/PH04-FE-FEED-01-P1-01.md) | Triển khai FEED-01 P1: Bảng tin | PH01-FE-FOUNDATION-02, PH04-BE-SOC-10-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-01-P0-02 |
| [PH04-FE-FEED-01-P1-02](prompts/PH04-FE-FEED-01-P1-02.md) | QA FEED-01 P1 trên Desktop/Mobile | PH04-FE-FEED-01-P1-01 |

### PH04-FE-FEED-02-P1 — Tạo bài viết P1

Ưu tiên P1; miền cross-cutting. Route: /bai-viet/moi. Vai trò: Người dùng. Chỉ bật MED-01, MED-03 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-FEED-02-P1-01](prompts/PH04-FE-FEED-02-P1-01.md) | Triển khai FEED-02 P1: Tạo bài viết | PH01-FE-FOUNDATION-02, PH04-BE-MED-01-02, PH04-BE-MED-03-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-02-P0-02 |
| [PH04-FE-FEED-02-P1-02](prompts/PH04-FE-FEED-02-P1-02.md) | QA FEED-02 P1 trên Desktop/Mobile | PH04-FE-FEED-02-P1-01 |

### PH04-FE-FEED-03-P1 — Chi tiết bài viết P1

Ưu tiên P1; miền cross-cutting. Route: /bai-viet/:id. Vai trò: Người xem, Người dùng. Chỉ bật SOC-10, MOD-01 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-FEED-03-P1-01](prompts/PH04-FE-FEED-03-P1-01.md) | Triển khai FEED-03 P1: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH04-BE-SOC-10-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-FEED-03-P0-02 |
| [PH04-FE-FEED-03-P1-02](prompts/PH04-FE-FEED-03-P1-02.md) | QA FEED-03 P1 trên Desktop/Mobile | PH04-FE-FEED-03-P1-01 |

### PH04-FE-FEED-05-P1 — Bài viết video đang xử lý P1

Ưu tiên P1; miền cross-cutting. Route: /bai-viet/:id/xu-ly. Vai trò: Chủ sở hữu. Chỉ bật SOC-09, MED-04 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-FEED-05-P1-01](prompts/PH04-FE-FEED-05-P1-01.md) | Triển khai FEED-05 P1: Bài viết video đang xử lý | PH01-FE-FOUNDATION-02, PH04-BE-SOC-09-02, PH04-BE-MED-04-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-FEED-05-P1-02](prompts/PH04-FE-FEED-05-P1-02.md) | QA FEED-05 P1 trên Desktop/Mobile | PH04-FE-FEED-05-P1-01 |

### PH04-FE-PROF-03-P1 — Chỉnh sửa hồ sơ P1

Ưu tiên P1; miền cross-cutting. Route: /toi/chinh-sua. Vai trò: Người dùng. Chỉ bật ACC-05, ACC-06, MED-01 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-PROF-03-P1-01](prompts/PH04-FE-PROF-03-P1-01.md) | Triển khai PROF-03 P1: Chỉnh sửa hồ sơ | PH01-FE-FOUNDATION-02, PH02-BE-ACC-05-02, PH04-BE-ACC-06-02, PH04-BE-MED-01-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-PROF-03-P1-02](prompts/PH04-FE-PROF-03-P1-02.md) | QA PROF-03 P1 trên Desktop/Mobile | PH04-FE-PROF-03-P1-01 |

### PH04-FE-SET-02-P1 — Bảo mật tài khoản P1

Ưu tiên P1; miền cross-cutting. Route: /thiet-lap/bao-mat. Vai trò: Người dùng. Chỉ bật ACC-09, ACC-08 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-SET-02-P1-01](prompts/PH04-FE-SET-02-P1-01.md) | Triển khai SET-02 P1: Bảo mật tài khoản | PH01-FE-FOUNDATION-02, PH04-BE-ACC-09-02, PH04-BE-ACC-08-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-SET-02-P0-02 |
| [PH04-FE-SET-02-P1-02](prompts/PH04-FE-SET-02-P1-02.md) | QA SET-02 P1 trên Desktop/Mobile | PH04-FE-SET-02-P1-01 |

### PH04-FE-COMM-01-P1 — Khám phá cộng đồng P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong. Vai trò: Người dùng. Chỉ bật COM-01, COM-02 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-01-P1-01](prompts/PH04-FE-COMM-01-P1-01.md) | Triển khai COMM-01 P1: Khám phá cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-01-P1-02](prompts/PH04-FE-COMM-01-P1-02.md) | QA COMM-01 P1 trên Desktop/Mobile | PH04-FE-COMM-01-P1-01 |

### PH04-FE-COMM-02-P1 — Tổng quan cộng đồng P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id. Vai trò: Thành viên, Khách theo chính sách. Chỉ bật COM-01, COM-02, COM-04 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-02-P1-01](prompts/PH04-FE-COMM-02-P1-01.md) | Triển khai COMM-02 P1: Tổng quan cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-01-02, PH04-BE-COM-02-02, PH04-BE-COM-04-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-02-P1-02](prompts/PH04-FE-COMM-02-P1-02.md) | QA COMM-02 P1 trên Desktop/Mobile | PH04-FE-COMM-02-P1-01 |

### PH04-FE-COMM-03-P1 — Mời và tham gia cộng đồng P1

Ưu tiên P1; miền cross-cutting. Route: /loi-moi/:code. Vai trò: Người dùng. Chỉ bật COM-02 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-03-P1-01](prompts/PH04-FE-COMM-03-P1-01.md) | Triển khai COMM-03 P1: Mời và tham gia cộng đồng | PH01-FE-FOUNDATION-02, PH04-BE-COM-02-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-03-P1-02](prompts/PH04-FE-COMM-03-P1-02.md) | QA COMM-03 P1 trên Desktop/Mobile | PH04-FE-COMM-03-P1-01 |

### PH04-FE-COMM-04-P1 — Vai trò và quyền P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/vai-tro. Vai trò: Chủ sở hữu, Điều hành viên. Chỉ bật COM-03 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-04-P1-01](prompts/PH04-FE-COMM-04-P1-01.md) | Triển khai COMM-04 P1: Vai trò và quyền | PH01-FE-FOUNDATION-02, PH04-BE-COM-03-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-04-P1-02](prompts/PH04-FE-COMM-04-P1-02.md) | QA COMM-04 P1 trên Desktop/Mobile | PH04-FE-COMM-04-P1-01 |

### PH04-FE-COMM-05-P1 — Quản lý kênh P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/kenh. Vai trò: Điều hành viên. Chỉ bật COM-04 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-05-P1-01](prompts/PH04-FE-COMM-05-P1-01.md) | Triển khai COMM-05 P1: Quản lý kênh | PH01-FE-FOUNDATION-02, PH04-BE-COM-04-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-05-P1-02](prompts/PH04-FE-COMM-05-P1-02.md) | QA COMM-05 P1 trên Desktop/Mobile | PH04-FE-COMM-05-P1-01 |

### PH04-FE-COMM-06-P1 — Điều hành thành viên P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/thanh-vien. Vai trò: Điều hành viên. Chỉ bật COM-05 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-06-P1-01](prompts/PH04-FE-COMM-06-P1-01.md) | Triển khai COMM-06 P1: Điều hành thành viên | PH01-FE-FOUNDATION-02, PH04-BE-COM-05-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-06-P1-02](prompts/PH04-FE-COMM-06-P1-02.md) | QA COMM-06 P1 trên Desktop/Mobile | PH04-FE-COMM-06-P1-01 |

### PH04-FE-COMM-07-P1 — Kênh văn bản P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/kenh/:channelId. Vai trò: Thành viên. Chỉ bật COM-04, CHT-02, CHT-07 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-COMM-07-P1-01](prompts/PH04-FE-COMM-07-P1-01.md) | Triển khai COMM-07 P1: Kênh văn bản | PH01-FE-FOUNDATION-02, PH04-BE-COM-04-02, PH03-BE-CHT-02-02, PH03-BE-CHT-07-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-COMM-07-P1-02](prompts/PH04-FE-COMM-07-P1-02.md) | QA COMM-07 P1 trên Desktop/Mobile | PH04-FE-COMM-07-P1-01 |

### PH04-FE-CHAT-02-P1 — Hội thoại P1

Ưu tiên P1; miền cross-cutting. Route: /tin-nhan/:id. Vai trò: Thành viên hội thoại. Chỉ bật MED-06, CHT-09 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-CHAT-02-P1-01](prompts/PH04-FE-CHAT-02-P1-01.md) | Triển khai CHAT-02 P1: Hội thoại | PH01-FE-FOUNDATION-02, PH04-BE-MED-06-02, PH04-BE-CHT-09-02, G1-01, PH04-BE-CONTRACT-01, PH03-FE-CHAT-02-P0-02 |
| [PH04-FE-CHAT-02-P1-02](prompts/PH04-FE-CHAT-02-P1-02.md) | QA CHAT-02 P1 trên Desktop/Mobile | PH04-FE-CHAT-02-P1-01 |

### PH04-FE-RTC-01-P1 — Lời mời cuộc gọi P1

Ưu tiên P1; miền cross-cutting. Route: /cuoc-goi/:id. Vai trò: Người dùng, Thành viên. Chỉ bật CHT-09, RTC-01 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-RTC-01-P1-01](prompts/PH04-FE-RTC-01-P1-01.md) | Triển khai RTC-01 P1: Lời mời cuộc gọi | PH01-FE-FOUNDATION-02, PH04-BE-CHT-09-02, PH04-BE-RTC-01-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-RTC-01-P1-02](prompts/PH04-FE-RTC-01-P1-02.md) | QA RTC-01 P1 trên Desktop/Mobile | PH04-FE-RTC-01-P1-01 |

### PH04-FE-RTC-02-P1 — Phòng thoại và video P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/phong/:roomId. Vai trò: Thành viên. Chỉ bật RTC-01, RTC-02 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-RTC-02-P1-01](prompts/PH04-FE-RTC-02-P1-01.md) | Triển khai RTC-02 P1: Phòng thoại và video | PH01-FE-FOUNDATION-02, PH04-BE-RTC-01-02, PH04-BE-RTC-02-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-RTC-02-P1-02](prompts/PH04-FE-RTC-02-P1-02.md) | QA RTC-02 P1 trên Desktop/Mobile | PH04-FE-RTC-02-P1-01 |

### PH04-FE-RTC-03-P1 — Chia sẻ màn hình P1

Ưu tiên P1; miền cross-cutting. Route: /cong-dong/:id/phong/:roomId/chia-se. Vai trò: Thành viên có quyền. Chỉ bật RTC-03 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-RTC-03-P1-01](prompts/PH04-FE-RTC-03-P1-01.md) | Triển khai RTC-03 P1: Chia sẻ màn hình | PH01-FE-FOUNDATION-02, PH04-BE-RTC-03-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-RTC-03-P1-02](prompts/PH04-FE-RTC-03-P1-02.md) | QA RTC-03 P1 trên Desktop/Mobile | PH04-FE-RTC-03-P1-01 |

### PH04-FE-MEDIA-01-P1 — Tải phương tiện P1

Ưu tiên P1; miền cross-cutting. Route: /phuong-tien/tai-len. Vai trò: Người dùng. Chỉ bật MED-01, MED-02, MED-03, MED-04 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH04-FE-MEDIA-01-P1-01](prompts/PH04-FE-MEDIA-01-P1-01.md) | Triển khai MEDIA-01 P1: Tải phương tiện | PH01-FE-FOUNDATION-02, PH04-BE-MED-01-02, PH04-BE-MED-02-02, PH04-BE-MED-03-02, PH04-BE-MED-04-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH04-FE-MEDIA-01-P1-02](prompts/PH04-FE-MEDIA-01-P1-02.md) | QA MEDIA-01 P1 trên Desktop/Mobile | PH04-FE-MEDIA-01-P1-01 |

## PH05 — Xóa liên dịch vụ, điều hành và nghiệm thu P1

### PH05-FE-SET-04-P1 — Xóa tài khoản P1

Ưu tiên P1; miền cross-cutting. Route: /thiet-lap/xoa-tai-khoan. Vai trò: Người dùng. Chỉ bật ACC-11 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-FE-SET-04-P1-01](prompts/PH05-FE-SET-04-P1-01.md) | Triển khai SET-04 P1: Xóa tài khoản | PH01-FE-FOUNDATION-02, PH05-BE-ACC-11-02, G1-01, PH04-BE-CONTRACT-01, PH05-BE-DELETION-08 |
| [PH05-FE-SET-04-P1-02](prompts/PH05-FE-SET-04-P1-02.md) | QA SET-04 P1 trên Desktop/Mobile | PH05-FE-SET-04-P1-01 |

### PH05-FE-MOD-01-P1 — Báo cáo nội dung P1

Ưu tiên P1; miền cross-cutting. Route: hộp thoại. Vai trò: Người dùng. Chỉ bật MOD-01 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-FE-MOD-01-P1-01](prompts/PH05-FE-MOD-01-P1-01.md) | Triển khai MOD-01 P1: Báo cáo nội dung | PH01-FE-FOUNDATION-02, PH05-BE-MOD-01-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH05-FE-MOD-01-P1-02](prompts/PH05-FE-MOD-01-P1-02.md) | QA MOD-01 P1 trên Desktop/Mobile | PH05-FE-MOD-01-P1-01 |

### PH05-FE-MOD-02-P1 — Hàng đợi điều hành P1

Ưu tiên P1; miền cross-cutting. Route: /dieu-hanh/bao-cao. Vai trò: Điều hành viên, Quản trị viên. Chỉ bật MOD-02 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-FE-MOD-02-P1-01](prompts/PH05-FE-MOD-02-P1-01.md) | Triển khai MOD-02 P1: Hàng đợi điều hành | PH01-FE-FOUNDATION-02, PH05-BE-MOD-02-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH05-FE-MOD-02-P1-02](prompts/PH05-FE-MOD-02-P1-02.md) | QA MOD-02 P1 trên Desktop/Mobile | PH05-FE-MOD-02-P1-01 |

### PH05-FE-MOD-03-P1 — Chi tiết điều hành P1

Ưu tiên P1; miền cross-cutting. Route: /dieu-hanh/bao-cao/:id. Vai trò: Điều hành viên, Quản trị viên. Chỉ bật MOD-03, MOD-04 tại P1. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH05-FE-MOD-03-P1-01](prompts/PH05-FE-MOD-03-P1-01.md) | Triển khai MOD-03 P1: Chi tiết điều hành | PH01-FE-FOUNDATION-02, PH05-BE-MOD-03-02, PH05-BE-MOD-04-02, G1-01, PH04-BE-CONTRACT-01 |
| [PH05-FE-MOD-03-P1-02](prompts/PH05-FE-MOD-03-P1-02.md) | QA MOD-03 P1 trên Desktop/Mobile | PH05-FE-MOD-03-P1-01 |

## PH06 — Thương mại, AI và tìm kiếm P2 có điều kiện

### PH06-FE-FEED-01-P2 — Bảng tin P2

Ưu tiên P2; miền cross-cutting. Route: /bang-tin. Vai trò: Người dùng. Chỉ bật FED-04 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-FEED-01-P2-01](prompts/PH06-FE-FEED-01-P2-01.md) | Triển khai FEED-01 P2: Bảng tin | PH01-FE-FOUNDATION-02, PH06-BE-FED-04-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-FEED-01-P1-02 |
| [PH06-FE-FEED-01-P2-02](prompts/PH06-FE-FEED-01-P2-02.md) | QA FEED-01 P2 trên Desktop/Mobile | PH06-FE-FEED-01-P2-01 |

### PH06-FE-FEED-03-P2 — Chi tiết bài viết P2

Ưu tiên P2; miền cross-cutting. Route: /bai-viet/:id. Vai trò: Người xem, Người dùng. Chỉ bật AI-05 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-FEED-03-P2-01](prompts/PH06-FE-FEED-03-P2-01.md) | Triển khai FEED-03 P2: Chi tiết bài viết | PH01-FE-FOUNDATION-02, PH06-BE-AI-05-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-FEED-03-P1-02 |
| [PH06-FE-FEED-03-P2-02](prompts/PH06-FE-FEED-03-P2-02.md) | QA FEED-03 P2 trên Desktop/Mobile | PH06-FE-FEED-03-P2-01 |

### PH06-FE-DISC-01-P2 — Tìm kiếm P2

Ưu tiên P2; miền cross-cutting. Route: /tim-kiem. Vai trò: Người dùng. Chỉ bật AI-02, MKT-02, SOC-06 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-DISC-01-P2-01](prompts/PH06-FE-DISC-01-P2-01.md) | Triển khai DISC-01 P2: Tìm kiếm | PH01-FE-FOUNDATION-02, PH06-BE-AI-02-02, PH06-BE-MKT-02-02, PH03-BE-SOC-06-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-DISC-01-P2-02](prompts/PH06-FE-DISC-01-P2-02.md) | QA DISC-01 P2 trên Desktop/Mobile | PH06-FE-DISC-01-P2-01 |

### PH06-FE-CHAT-02-P2 — Hội thoại P2

Ưu tiên P2; miền cross-cutting. Route: /tin-nhan/:id. Vai trò: Thành viên hội thoại. Chỉ bật AI-05 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-CHAT-02-P2-01](prompts/PH06-FE-CHAT-02-P2-01.md) | Triển khai CHAT-02 P2: Hội thoại | PH01-FE-FOUNDATION-02, PH06-BE-AI-05-02, G2-01, PH06-BE-CONTRACT-01, PH04-FE-CHAT-02-P1-02 |
| [PH06-FE-CHAT-02-P2-02](prompts/PH06-FE-CHAT-02-P2-02.md) | QA CHAT-02 P2 trên Desktop/Mobile | PH06-FE-CHAT-02-P2-01 |

### PH06-FE-MKT-01-P2 — Chợ P2

Ưu tiên P2; miền cross-cutting. Route: /cho. Vai trò: Khách theo chính sách, Người dùng. Chỉ bật MKT-02 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-01-P2-01](prompts/PH06-FE-MKT-01-P2-01.md) | Triển khai MKT-01 P2: Chợ | PH01-FE-FOUNDATION-02, PH06-BE-MKT-02-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-01-P2-02](prompts/PH06-FE-MKT-01-P2-02.md) | QA MKT-01 P2 trên Desktop/Mobile | PH06-FE-MKT-01-P2-01 |

### PH06-FE-MKT-02-P2 — Chi tiết tin đăng P2

Ưu tiên P2; miền cross-cutting. Route: /cho/tin/:id. Vai trò: Người mua, Khách theo chính sách. Chỉ bật MKT-02, MKT-07, MKT-04, CHT-01 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-02-P2-01](prompts/PH06-FE-MKT-02-P2-01.md) | Triển khai MKT-02 P2: Chi tiết tin đăng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-02-02, PH06-BE-MKT-07-02, PH06-BE-MKT-04-02, PH03-BE-CHT-01-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-02-P2-02](prompts/PH06-FE-MKT-02-P2-02.md) | QA MKT-02 P2 trên Desktop/Mobile | PH06-FE-MKT-02-P2-01 |

### PH06-FE-MKT-03-P2 — Tạo hoặc sửa tin đăng P2

Ưu tiên P2; miền cross-cutting. Route: /cho/tin/moi. Vai trò: Người bán. Chỉ bật MKT-01, MKT-03, MKT-07 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-03-P2-01](prompts/PH06-FE-MKT-03-P2-01.md) | Triển khai MKT-03 P2: Tạo hoặc sửa tin đăng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-01-02, PH06-BE-MKT-03-02, PH06-BE-MKT-07-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-03-P2-02](prompts/PH06-FE-MKT-03-P2-02.md) | QA MKT-03 P2 trên Desktop/Mobile | PH06-FE-MKT-03-P2-01 |

### PH06-FE-MKT-04-P2 — Xác nhận đơn hàng P2

Ưu tiên P2; miền cross-cutting. Route: /cho/thanh-toan. Vai trò: Người mua. Chỉ bật MKT-03, MKT-04 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-04-P2-01](prompts/PH06-FE-MKT-04-P2-01.md) | Triển khai MKT-04 P2: Xác nhận đơn hàng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-03-02, PH06-BE-MKT-04-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-04-P2-02](prompts/PH06-FE-MKT-04-P2-02.md) | QA MKT-04 P2 trên Desktop/Mobile | PH06-FE-MKT-04-P2-01 |

### PH06-FE-MKT-05-P2 — Thanh toán trực tiếp với người bán P2

Ưu tiên P2; miền cross-cutting. Route: /cho/don/:id/thanh-toan. Vai trò: Người mua. Chỉ bật MKT-05 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-05-P2-01](prompts/PH06-FE-MKT-05-P2-01.md) | Triển khai MKT-05 P2: Thanh toán trực tiếp với người bán | PH01-FE-FOUNDATION-02, PH06-BE-MKT-05-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-05-P2-02](prompts/PH06-FE-MKT-05-P2-02.md) | QA MKT-05 P2 trên Desktop/Mobile | PH06-FE-MKT-05-P2-01 |

### PH06-FE-MKT-06-P2 — Đơn hàng P2

Ưu tiên P2; miền cross-cutting. Route: /cho/don-hang. Vai trò: Người mua, Người bán. Chỉ bật MKT-06, MKT-04, MKT-05 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-MKT-06-P2-01](prompts/PH06-FE-MKT-06-P2-01.md) | Triển khai MKT-06 P2: Đơn hàng | PH01-FE-FOUNDATION-02, PH06-BE-MKT-06-02, PH06-BE-MKT-04-02, PH06-BE-MKT-05-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-MKT-06-P2-02](prompts/PH06-FE-MKT-06-P2-02.md) | QA MKT-06 P2 trên Desktop/Mobile | PH06-FE-MKT-06-P2-01 |

### PH06-FE-AI-01-P2 — Trợ lý AI P2

Ưu tiên P2; miền cross-cutting. Route: /tro-ly. Vai trò: Người dùng. Chỉ bật AI-03 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-AI-01-P2-01](prompts/PH06-FE-AI-01-P2-01.md) | Triển khai AI-01 P2: Trợ lý AI | PH01-FE-FOUNDATION-02, PH06-BE-AI-03-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-AI-01-P2-02](prompts/PH06-FE-AI-01-P2-02.md) | QA AI-01 P2 trên Desktop/Mobile | PH06-FE-AI-01-P2-01 |

### PH06-FE-AI-02-P2 — Tóm tắt hội thoại hoặc kênh P2

Ưu tiên P2; miền cross-cutting. Route: /tro-ly/tom-tat. Vai trò: Thành viên có quyền. Chỉ bật AI-04 tại P2. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt.

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH06-FE-AI-02-P2-01](prompts/PH06-FE-AI-02-P2-01.md) | Triển khai AI-02 P2: Tóm tắt hội thoại hoặc kênh | PH01-FE-FOUNDATION-02, PH06-BE-AI-04-02, G2-01, PH06-BE-CONTRACT-01 |
| [PH06-FE-AI-02-P2-02](prompts/PH06-FE-AI-02-P2-02.md) | QA AI-02 P2 trên Desktop/Mobile | PH06-FE-AI-02-P2-01 |
