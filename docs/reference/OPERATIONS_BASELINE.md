# Baseline vận hành

## RPO/RTO

| Phạm vi | RPO | RTO | Bằng chứng khôi phục |
| --- | --- | --- | --- |
| P0 - Account/Social/Chat/Feed | <= 24 giờ | <= 4 giờ | Khôi phục PostgreSQL, projection và secret; kiểm tra đăng nhập, bài viết, tin nhắn. |
| Media object | <= 24 giờ | <= 8 giờ | Khôi phục metadata trước; object theo backup; asset thiếu được đánh dấu và đối soát. |
| Commerce | <= 24 giờ | <= 8 giờ | Đối soát order/payment mock và inventory; không phát lại thanh toán ngoài ý muốn. |
| AI/Search/OpenSearch | Có thể tạo lại | <= 24 giờ | Khôi phục source metadata/job; rebuild embedding/index theo batch. |
| Kafka | Tối thiểu 7 ngày retention | <= 4 giờ | Outbox là nguồn phát lại; projection consumer chạy từ checkpoint hoặc replay có kiểm soát. |

## Chính sách sao lưu

| Thành phần | Cách sao lưu | Lưu giữ | Kiểm chứng |
| --- | --- | --- | --- |
| PostgreSQL | pg_dump theo từng database mỗi ngày; backup toàn cụm mỗi tuần | 7 ngày + 4 tuần | Restore vào instance tách biệt; chạy migration/checksum và smoke test. |
| SeaweedFS | Sao chép object + metadata mỗi ngày | 7 ngày + 4 tuần | Đối chiếu object_key, size, hash mẫu và MediaAsset. |
| Cấu hình/secret | Cấu hình không bí mật trong Git; secret export mã hóa theo quy trình | Mỗi thay đổi | Dựng môi trường mới không dùng secret từ log hoặc máy cá nhân. |
| Kafka | Không xem Kafka là bản sao DB | Retention theo topic | Dùng Outbox và source export để rebuild; backup config/schema. |
| Diễn tập | Cuối mỗi milestone lớn và tối thiểu mỗi tháng | Lưu biên bản | Đo RPO/RTO thực tế, lỗi phát hiện và hành động khắc phục. |

## Ngân sách tài nguyên

| Cấu hình/Thành phần | Ngân sách ban đầu | Phạm vi | Giới hạn |
| --- | --- | --- | --- |
| core | 4 vCPU / 8 GB RAM / 80 GB SSD | P0 + phần lớn P1; AI/OpenSearch và quan sát đầy đủ tắt | 50 người dùng mô phỏng; RTC giới hạn nhỏ |
| demo-full | 8 vCPU / 16 GB RAM / 160 GB SSD | Tất cả dịch vụ; Prometheus/Grafana; mô hình AI nhỏ dùng CPU | Bật theo lịch demo, không cam kết production |
| PostgreSQL | 1.5-3 GB RAM | Nhiều database logic, pool giới hạn theo dịch vụ | Cảnh báo pool > 80%, disk > 85% |
| Kafka | 1-2 GB RAM | Một broker, retention 7-30 ngày, payload <= 256 KB | Theo dõi heap, disk và consumer lag |
| Valkey | 256-512 MB | TTL bắt buộc, maxmemory và eviction rõ | Không lưu source-of-truth |
| LiveKit/coturn | 0.5-1.5 GB RAM | Giới hạn room/participant theo load test | CPU/network là ngưỡng chính |
| Quan sát | 1.5-3 GB RAM | Bật theo profile; retention ngắn | Giới hạn cardinality label |
| AI/Ollama | 4-8 GB RAM tùy mô hình | Bounded concurrency; queue; có thể chạy máy riêng | Không nằm trên đường sống của P0 |

## Migration và quay lui

| Bước | Quy tắc | Điều kiện an toàn |
| --- | --- | --- |
| Mở rộng | Thêm bảng/cột nullable hoặc có default an toàn; thêm index CONCURRENTLY khi phù hợp. | Ứng dụng cũ và mới cùng chạy được. |
| Chuyển dữ liệu | Backfill theo batch có checkpoint, metric và khả năng tiếp tục. | Không khóa bảng dài; có đối soát số lượng/hash. |
| Chuyển đọc/ghi | Bật bằng feature flag sau khi dữ liệu đủ; theo dõi lỗi và latency. | Có thể tắt flag mà không mất dữ liệu. |
| Thu hẹp | Chỉ xóa cột/topic/contract sau ít nhất một chu kỳ phát hành và xác nhận không còn consumer. | ADR và kiểm thử compatibility bắt buộc. |
| Quay lui code | Chỉ thực hiện nếu schema còn tương thích ngược. | Nếu migration phá vỡ thì ưu tiên roll-forward bằng bản sửa. |
| Sự kiện | Producer mới chỉ thêm trường optional trong v1; consumer được triển khai trước thay đổi producer. | Thay đổi phá vỡ dùng v2/topic mới và chạy song song. |
| Sao lưu trước phát hành | Backup hoặc snapshot có kiểm chứng cho migration rủi ro. | Ghi thời điểm, checksum và lệnh restore trong runbook. |

## Cấu hình, phụ thuộc và bí mật

| Khu vực | Quy tắc | Điều kiện |
| --- | --- | --- |
| Phiên bản gói .NET | Quản lý tập trung bằng Directory.Packages.props; khóa major/minor; Dependabot/Renovate chỉ tạo PR. | Mỗi thay đổi phải qua build/test/scan. |
| Ảnh container | Pin theo digest cho bản phát hành; base image tối thiểu; chạy non-root khi hỗ trợ. | SBOM và scan lưu cùng release. |
| Cấu hình | appsettings mặc định không chứa bí mật; override bằng biến môi trường; validate khi khởi động. | Thiếu cấu hình bắt buộc phải fail fast. |
| Bí mật | Kho bí mật hoặc file môi trường bảo vệ; tên secret chuẩn; rotation có runbook. | Không commit, không ghi log, không gửi qua chat/tài liệu. |
| Feature flag | Dùng cho chức năng P2, thay đổi đọc/ghi và tích hợp rủi ro. | Flag có owner, ngày hết hạn và trạng thái mặc định an toàn. |
| Môi trường | dev/test/staging/prod-demo tách database, topic prefix, credential và bucket. | Không dùng dữ liệu thật trong test; không chia sẻ secret giữa môi trường. |
