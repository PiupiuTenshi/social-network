# Khả năng quan sát

## Correlation

- Nhận hoặc sinh `X-Correlation-ID` tại biên.
- Truyền mã này qua HTTP, Outbox, vỏ sự kiện và log.
- Giữ OpenTelemetry trace context khi bên phát và bên nhận hỗ trợ.

## Log

- Dùng JSON có thời gian UTC, mức độ, dịch vụ, môi trường, `traceId`, `correlationId`, `eventId` và `aggregateId` khi liên quan.
- Không log secret, token, OTP, PII thô hoặc nội dung riêng tư.
- Lỗi phải có loại và thao tác; tránh ghi cùng exception lặp lại ở nhiều tầng không cần thiết.

## Metric

- RED cho HTTP và dịch vụ.
- Độ trễ consumer, số lần thử lại, DLQ và sự kiện Inbox bị từ chối.
- Số bản ghi Outbox chờ và tuổi bản ghi cũ nhất.
- Pool kết nối, độ trễ/khóa cơ sở dữ liệu và dung lượng đĩa.
- Bộ nhớ và eviction của Valkey.
- Số room/participant cùng CPU/mạng của LiveKit.
- Độ sâu hàng đợi AI, thời gian xử lý và loại lỗi.

## Trace

Tạo span cho Gateway, endpoint/ca sử dụng, cơ sở dữ liệu, phát/nhận sự kiện, phụ thuộc ngoài và tiến trình nền. Không đưa dữ liệu nhạy cảm vào thuộc tính trace.

## Cảnh báo

Mỗi cảnh báo phải có người hoặc thành phần phụ trách, mức độ, ngưỡng, thời gian duy trì, liên kết dashboard và runbook. Không tạo cảnh báo không thể hành động.
