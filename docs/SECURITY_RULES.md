# Quy tắc bảo mật

## Danh tính và phiên

- Access token sống ngắn; xác minh chữ ký, `iss`, `aud`, `exp`, `nbf`, `ver` và độ lệch đồng hồ cho phép.
- Refresh token chỉ lưu dạng băm, xoay một lần, theo dõi family và phát hiện dùng lại.
- Đổi mật khẩu hoặc phát hiện token bị đánh cắp phải tăng phiên bản token và thu hồi phiên liên quan.
- Vai trò cộng đồng không nhúng lâu dài vào JWT; dùng bản chiếu và xác minh đồng bộ cho hành động nhạy cảm khi dữ liệu có thể cũ.

## Phân quyền

- Kiểm tra tại dịch vụ sở hữu tài nguyên.
- Không tin định danh, vai trò hoặc ownership do máy khách gửi nếu có thể suy ra từ claim và tài nguyên.
- Mỗi tài nguyên cần kiểm thử âm cho BOLA/IDOR.
- Hành động quản trị hoặc điều hành phải có lý do và nhật ký kiểm toán.

## Dữ liệu đầu vào và nội dung

- Xác thực DTO trước khi vào logic nghiệp vụ.
- Dùng danh sách cho phép cho enum và định dạng cố định.
- Làm sạch rich text/Markdown và mã hóa khi hiển thị.
- CORS dùng danh sách origin cụ thể; CSP được cấu hình; cookie refresh cần kiểm soát CSRF.
- Tải tệp phải kiểm tra metadata khai báo, thông tin đối tượng thực tế và magic bytes.

## Secret và PII

- Secret không được xuất hiện trong kho mã, prompt, ticket, log hoặc ảnh chụp.
- Không log mật khẩu, OTP, JWT, refresh token, email thô hoặc nội dung riêng tư.
- PII được che theo vai trò và xóa hoặc ẩn danh theo chính sách lưu giữ.
- Bản sao lưu phải được bảo vệ và tách khỏi volume đang chạy.

## AI và RAG

- Phân quyền trước khi truy xuất và trước khi đưa dữ liệu vào ngữ cảnh mô hình.
- Nội dung truy xuất là dữ liệu không tin cậy, không phải chỉ dẫn hệ thống.
- Không cấp công cụ nguy hiểm hoặc quyền vượt quá người dùng hiện tại.
- Không log prompt hoặc ngữ cảnh nhạy cảm theo mặc định.

Xem mô hình đe dọa trong `docs/reference/SECURITY_THREAT_MODEL.md`.
