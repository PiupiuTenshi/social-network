# Yêu cầu phi chức năng

| Hạng mục | Mục tiêu cơ sở | Cách đo hoặc thực thi |
| --- | --- | --- |
| Độ trễ API đọc | p95 < 300 ms cho điểm cuối đọc không tìm kiếm trên bộ dữ liệu thử nghiệm. | Đo bằng k6 và OpenTelemetry; truy vấn N+1 được xem là lỗi. |
| Độ trễ API ghi | p95 < 500 ms cho thao tác ghi có Outbox. | Tính cả việc ghi dữ liệu nghiệp vụ và Outbox trong cùng giao dịch. |
| Phát thời gian thực qua SignalR | < 200 ms từ lúc phát đến máy khách trong cùng vùng mạng. | Đo bằng dấu thời gian trong DTO tin nhắn. |
| Tham gia RTC qua LiveKit | < 2 giây từ lúc yêu cầu token đến trạng thái đã kết nối. | Không tính độ trễ bất thường do STUN/TURN hoặc mạng yếu. |
| Tính sẵn sàng cơ sở | Vận hành theo khả năng tốt nhất trên một nút; không cam kết SLA nhiều số 9. | Mô hình nhiều nút thuộc hướng phát triển. |
| Độ bền dữ liệu | Không mất dữ liệu đã cam kết khi khởi động lại container có volume. | Dùng PostgreSQL WAL và thời gian lưu topic Kafka tối thiểu 7 ngày. |
| Mô hình nhất quán | Nhất quán mạnh trong từng dịch vụ; nhất quán cuối giữa các dịch vụ. | Outbox bảo đảm phát ít nhất một lần; bộ nhận sự kiện phải xử lý lặp an toàn. |
| Xử lý đồng thời | Chịu tải mô phỏng khoảng 50-100 người dùng đồng thời. | Dùng k6 với kịch bản đọc, ghi, chat và giữ tồn kho. |
| Bảo mật | Access token sống ngắn, xoay vòng refresh token và giới hạn tần suất OTP. | Thực thi theo mục 16 và kiểm thử các trường hợp từ chối. |
| Khả năng quan sát | Mọi yêu cầu có traceId xuyên dịch vụ. | OpenTelemetry và Jaeger/Zipkin; có thể tắt cấu hình đầy đủ khi thiếu tài nguyên. |
| Độ phủ kiểm thử | Kiểm thử đơn vị cho quy tắc cốt lõi và ít nhất một kiểm thử tích hợp cho mỗi dịch vụ. | Không yêu cầu 100% độ phủ; ưu tiên quy tắc nghiệp vụ và luồng lỗi. |
| Khôi phục dữ liệu | RPO <= 24 giờ; RTO <= 4 giờ cho nhóm P0. | Sao lưu tự động, kiểm tra checksum và diễn tập khôi phục trên môi trường tách biệt. |
| Xóa tài khoản | Ẩn truy cập trong 5 phút; xóa cứng dữ liệu định danh trong tối đa 45 ngày nếu không có giữ lại hợp lệ. | Theo dõi account_deletion_request, sự kiện liên dịch vụ và cảnh báo công việc quá hạn. |
| Chất lượng phát hành | 100% tiêu chí P0 đạt; không còn lỗi Critical/High hoặc lỗ hổng nghiêm trọng chưa có ngoại lệ được phê duyệt. | Bắt buộc qua CI/CD, kiểm thử hợp đồng, quét bí mật/phụ thuộc và hồ sơ nghiệm thu. |
