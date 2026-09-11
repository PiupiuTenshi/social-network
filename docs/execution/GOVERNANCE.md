# Danh mục GOVERNANCE

Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.

## PH00 — Khảo sát, quyết định và G0

### PH00-GOV-AUDIT — Xác nhận nguồn, quy tắc và phạm vi thực tế

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH00-GOV-AUDIT-01](prompts/PH00-GOV-AUDIT-01.md) | Xác nhận nguồn, quy tắc và phạm vi thực tế | Không; cần DoR |

## PH07 — Gia cố, NFR, bảo mật và khôi phục

### PH07-GOV-HARDEN — Gia cố ứng viên phát hành

Ưu tiên P0; miền cross-cutting. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH07-GOV-HARDEN-01](prompts/PH07-GOV-HARDEN-01.md) | Đo tải và xử lý bottleneck | G3-01 |
| [PH07-GOV-HARDEN-02](prompts/PH07-GOV-HARDEN-02.md) | Rà soát bảo mật và chuỗi cung ứng | PH07-GOV-HARDEN-01 |
| [PH07-GOV-HARDEN-03](prompts/PH07-GOV-HARDEN-03.md) | Di trú, khôi phục và rollback ứng viên | PH07-GOV-HARDEN-02 |
| [PH07-GOV-HARDEN-04](prompts/PH07-GOV-HARDEN-04.md) | Đồng bộ hồ sơ bàn giao | PH07-GOV-HARDEN-03 |

## PH08 — Diễn tập phát hành và bàn giao

### PH08-GOV-REHEARSAL — Diễn tập phát hành từ môi trường sạch

Ưu tiên P0; miền deploy. 

| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |
|---|---|---|
| [PH08-GOV-REHEARSAL-01](prompts/PH08-GOV-REHEARSAL-01.md) | Diễn tập phát hành từ môi trường sạch | PH07-GOV-HARDEN-04 |
