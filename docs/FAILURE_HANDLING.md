# Xử lý lỗi, thử lại và suy giảm

## Phân loại lỗi

- **Nghiệp vụ hoặc dữ liệu sai:** không thử lại; trả kết quả ổn định.
- **Phân quyền:** không thử lại; ghi kiểm toán khi nhạy cảm.
- **Xung đột hoặc tranh chấp:** bên gọi đọc lại hoặc thử lại có kiểm soát.
- **Phụ thuộc lỗi tạm thời:** thử lại hữu hạn, có backoff và jitter.
- **Lược đồ hoặc dữ liệu lỗi vĩnh viễn:** chuyển DLQ và cảnh báo.
- **Chưa phân loại:** đóng an toàn tại ranh giới tin cậy, giữ correlation và điều tra.

## Nguyên tắc

- Thử lại không thay thế xử lý lặp an toàn.
- Không thử lại vô hạn trên đường HTTP hoặc consumer.
- Circuit breaker hoặc phương án dự phòng chỉ dùng khi vẫn giữ đúng ý nghĩa nghiệp vụ.
- Valkey lỗi: cache/presence suy giảm, dữ liệu nguồn không mất.
- LiveKit lỗi: trò chuyện văn bản vẫn hoạt động.
- AI hoặc OpenSearch lỗi: ứng dụng cốt lõi vẫn hoạt động; chỉ dùng phương án DB/tìm kiếm dự phòng đã được định nghĩa.
- Kafka lỗi sau khi cơ sở dữ liệu commit: Outbox giữ trạng thái chờ và phát sau.
- Tải tệp không hoàn tất: phiên hết hạn và job dọn đối tượng mồ côi.

## Điều tra lỗi

Phân biệt triệu chứng, vị trí biểu hiện, nguyên nhân gốc và yếu tố góp phần. Thu thập trace, log, trạng thái dữ liệu, phiên bản và thứ tự thời gian trước khi sửa. Dùng `prompts/12-fix-bug.md` hoặc `prompts/20-incident-debug.md`.
