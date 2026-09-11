# Quy tắc thời gian thực và RTC

## SignalR

- Xác thực kết nối và kiểm tra thành viên cho từng hành động trên cuộc trò chuyện hoặc kênh.
- Chỉ thêm kết nối vào group sau khi phân quyền thành công.
- `SendMessage` dùng `clientMessageId`; lưu bền thành công trước khi phát.
- Typing và presence là trạng thái tạm thời, có TTL/giới hạn tần suất và chấp nhận mất.
- Con trỏ đọc chỉ được tiến về phía trước.
- Sau khi kết nối lại, máy khách phải tải được phần lịch sử đã bỏ lỡ.
- SignalR không phải nguồn dữ liệu chuẩn.

## LiveKit

- Cộng đồng kiểm tra thành viên và quyền trước khi cấp token.
- Token sống ngắn và giới hạn room, participant, quyền phát/nhận track.
- Máy khách kết nối trực tiếp LiveKit; coturn chỉ chuyển tiếp khi đường trực tiếp thất bại.
- Trò chuyện văn bản vẫn hoạt động khi RTC lỗi.
- Ghi hình, phụ đề và phát sóng công khai không thuộc phạm vi bắt buộc của bản cơ sở.

## Luồng AI

- Mỗi luồng token gắn `requestId`.
- Có sự kiện hoàn tất và lỗi rõ ràng.
- Máy khách ngắt kết nối không được để job hoặc bộ đệm không giới hạn tiếp tục chạy.

Xem `docs/reference/SIGNALR_CATALOG.md`.
