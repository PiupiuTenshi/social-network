# ADR-003 - Kafka, Transactional Outbox và giao nhận ít nhất một lần

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Ghi dữ liệu nghiệp vụ vào PostgreSQL và phát sự kiện lên Kafka không thể được bảo vệ bằng một distributed transaction phù hợp với baseline.

## Quyết định

Bên phát ghi dữ liệu nghiệp vụ và `outbox_message` trong cùng transaction. Worker phát sự kiện sau commit. Bên nhận dùng `inbox_message`, khóa duy nhất hoặc cơ chế tương đương để xử lý lặp an toàn. Hệ thống coi sự kiện trùng và phát lại là tình huống bình thường.

## Lý do

Mô hình này tránh mất sự kiện giữa lúc commit dữ liệu và gọi broker, đồng thời giữ khả năng phục hồi khi Kafka hoặc consumer tạm thời không sẵn sàng.

## Hệ quả

- Không có cam kết exactly-once toàn hệ thống.
- Phải có retry có giới hạn, DLQ, metric độ trễ Outbox và consumer lag.
- Tác dụng phụ ngoài hệ thống như email hoặc thanh toán phải có khóa xử lý lặp riêng.

## Ràng buộc thực thi

- Không phát integration event trước khi transaction nghiệp vụ commit.
- Không commit offset trước khi tác dụng phụ và Inbox đã ở trạng thái an toàn.
- Phát lại không được tạo tác dụng phụ lặp.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
