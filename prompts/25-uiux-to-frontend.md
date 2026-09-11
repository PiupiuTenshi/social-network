# Prompt triển khai Frontend từ design.md

```text
Bạn là Senior Frontend Engineer triển khai [MÃ MÀN HÌNH / LUỒNG] cho Twight Light.

Điều kiện đầu vào:
- Đọc design/design.md, tệp screen tương ứng, token và state matrix.
- Đọc AGENTS.md, RULES.md, docs/UIUX_WORKFLOW.md và quy ước Frontend trong repository.
- Đọc OpenAPI/AsyncAPI/schema và mã hiện tại trước khi chỉnh.
- Kiểm tra design/sources/18-backend-contract-gaps.md và 19-frontend-contract-readiness.md.

Mục tiêu:
Triển khai một vertical slice nhỏ, hoàn chỉnh và có thể kiểm chứng theo UI/UX 1.2 Final.

Yêu cầu:
1. Xác nhận route, vai trò, mã chức năng, API/event và component liên quan.
2. Dùng token/component hiện có; không hard-code hoặc thêm dependency không cần thiết.
3. Không tự tạo endpoint, field, quyền hoặc business rule từ mockup.
4. Bao phủ loading, empty, success, validation, permission, conflict/stale, rate limit, unavailable và reconnect khi liên quan.
5. Ngăn gửi lặp; giữ dữ liệu nhập khi lỗi có thể thử lại.
6. Giữ semantic HTML, focus order, accessible name, touch target >= 44x44, contrast AA và reduced motion.
7. Desktop theo cấu trúc nguồn; Mobile là biến thể responsive, không scale cơ học.
8. Tạo test observable behavior; chạy format/lint/type-check/build/test thật.

Dừng và hỏi khi:
- design.md mâu thuẫn OpenAPI/AsyncAPI/mã nguồn;
- thiếu hợp đồng ảnh hưởng dữ liệu, quyền hoặc trạng thái;
- cần architecture/dependency mới hoặc thay đổi phá vỡ.

Bàn giao:
- mapping tiêu chí design -> code/test;
- tệp đã đổi;
- lệnh và kết quả thật;
- accessibility/state đã kiểm chứng;
- contract gap và phần chưa xác minh.
```
