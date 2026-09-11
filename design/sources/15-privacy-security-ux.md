# 15. Bảo mật và quyền riêng tư trong UX

## Xác thực

- Không để access/refresh token trong URL.
- Không hiển thị chi tiết issuer/audience/signature cho người dùng.
- Refresh thất bại: thử một lần theo interceptor; nếu vẫn thất bại, đưa về login và giữ deep link an toàn.
- Không tạo vòng lặp refresh.

## Dữ liệu cá nhân

- Email/số điện thoại được che khi không phải chủ sở hữu.
- Không hiển thị OTP sau khi gửi.
- Không prefill mật khẩu.
- Tránh ghi dữ liệu nhạy cảm vào localStorage.
- Draft bài/tin nhắn riêng tư cần chính sách lưu cục bộ rõ.

## Authorization

- Client guard chỉ hỗ trợ trải nghiệm; không thay server authorization.
- Menu/action ẩn khi chắc chắn không có quyền.
- Khi quyền có thể thay đổi realtime, xử lý 403 và cập nhật UI.

## RAG/AI

- UI phải hiển thị nguồn mà người dùng có quyền.
- Không gửi context tùy ý từ client.
- Không render HTML do mô hình sinh nếu chưa sanitize.
- Citation link phải đi qua route kiểm tra quyền.

## Điều hành

- Bằng chứng nhạy cảm không tự phát.
- Access vào case được audit.
- PII được che theo vai trò.
- Copy/download bằng chứng là quyền riêng, không mặc định.
