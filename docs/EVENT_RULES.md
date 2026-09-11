# Quy tắc sự kiện và Kafka

## Vỏ sự kiện

```json
{
  "eventId": "uuid-v7",
  "eventType": "PostCreated",
  "eventVersion": 1,
  "occurredAt": "2026-09-05T10:00:00Z",
  "producer": "social-service",
  "correlationId": "uuid-v7",
  "aggregateId": "uuid-v7",
  "payload": {}
}
```

## Bên phát

- Ghi aggregate và Outbox trong cùng giao dịch.
- Nội dung sự kiện bất biến sau khi commit.
- Khi trạng thái xác nhận từ Kafka không chắc chắn, phát lại cùng `eventId` thay vì tạo sự kiện mới.
- Không gọi Kafka như bước bắt buộc trước khi commit cơ sở dữ liệu.

## Bên nhận

- Xác thực lược đồ và phiên bản sự kiện.
- Ghi Inbox và tác dụng phụ trong cùng giao dịch.
- `eventId` trùng phải được xử lý thành công mà không lặp tác dụng phụ.
- Dùng `aggregateVersion` hoặc cập nhật có điều kiện khi sự kiện cũ có thể đến sau.
- Không commit offset trước khi giao dịch cục bộ an toàn.

## Thử lại và DLQ

- Thử lại cục bộ trong thời gian ngắn, số lần hữu hạn và có jitter.
- Phụ thuộc lỗi kéo dài chuyển qua topic thử lại.
- Lỗi lược đồ hoặc dữ liệu vĩnh viễn chuyển vào DLQ và phát cảnh báo.
- Từ chối nghiệp vụ không được thử lại như lỗi hạ tầng.
- Phát lại phải có kiểm toán, chạy thử, lô nhỏ, giới hạn tốc độ và mặc định tắt tác dụng phụ như email hoặc thanh toán.

## Phiên bản

- Trong cùng phiên bản lớn: chỉ thêm trường tùy chọn; không đổi ý nghĩa hoặc kiểu trường bắt buộc.
- Thay đổi phá vỡ: dùng phiên bản lớn hoặc topic mới; nâng bên nhận trước bên phát; chạy song song và có ngày kết thúc.
- Lược đồ được lưu trong kho mã và CI kiểm tra tính tương thích.

Xem `docs/reference/EVENT_CATALOG.md` và `docs/reference/TOPIC_CATALOG.md`.
