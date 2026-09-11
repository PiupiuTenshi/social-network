# Cổng chất lượng và nghiệm thu

## Cổng CI/CD

| Cổng | Kiểm tra bắt buộc | Điều kiện đạt |
| --- | --- | --- |
| Biên dịch | dotnet restore/build và biên dịch giao diện | Không cảnh báo được nâng thành lỗi; khóa phiên bản phụ thuộc. |
| Kiểm thử đơn vị | Quy tắc miền và kiểm tra dữ liệu cốt lõi | Toàn bộ kiểm thử đạt; không bỏ qua ca lỗi mà không có lý do. |
| Kiểm thử tích hợp | PostgreSQL/Kafka/Valkey/SeaweedFS bằng môi trường container thử nghiệm | Di trú lược đồ chạy sạch; luồng Outbox/Inbox và giao dịch đạt. |
| Kiểm thử kiến trúc | Ranh giới phụ thuộc, cấm truy vấn chéo DB và cấm tầng API truy cập DbContext trực tiếp | Các luật kiến trúc chạy tự động và toàn bộ đạt. |
| Kiểm thử hợp đồng | OpenAPI và schema sự kiện v1 | Không có thay đổi phá vỡ chưa tăng phiên bản. |
| Kiểm tra di trú lược đồ | Nâng cấp từ phiên bản trước và tạo cơ sở dữ liệu mới | Cả hai đường chạy thành công; không để nhiều bản chạy di trú lược đồ đồng thời. |
| Quét bảo mật | Quét phụ thuộc, bí mật và ảnh container | Không còn bí mật thật hoặc lỗ hổng mức nghiêm trọng chưa có ngoại lệ. |
| SBOM và nguồn cung ứng | Sinh SBOM, khóa phiên bản gói và quét giấy phép/phụ thuộc | Không có gói không rõ nguồn gốc hoặc lỗ hổng nghiêm trọng chưa xử lý. |
| Đóng gói và triển khai | Tạo ảnh container theo commit, kiểm tra sức khỏe và kiểm thử nhanh | Chỉ triển khai khi các cổng trước đạt; có phương án quay lui. |

## Kế hoạch hai tuần đầu

| Ngày | Công việc | Kết quả kiểm chứng |
| --- | --- | --- |
| 1-2 | Tạo solution, cấu trúc dịch vụ, BuildingBlocks, quy tắc định dạng và chuỗi biên dịch/kiểm thử. | Kho mã biên dịch; CI chạy tự động trên nhánh hợp nhất. |
| 3-4 | Docker Compose cho PostgreSQL, Kafka, Valkey, SeaweedFS; kiểm tra sức khỏe và cấu hình môi trường. | Hạ tầng khởi động bằng một lệnh; volume và mạng nội bộ hoạt động. |
| 5-7 | ACC-01 đến ACC-04: đăng ký, đăng nhập, xoay vòng token, đăng xuất; di trú lược đồ Account. | API và kiểm thử tích hợp chạy xuyên suốt; không lưu token thô. |
| 8-9 | BuildingBlocks Outbox/Inbox, vỏ sự kiện và tiến trình phát Kafka; bộ nhận sự kiện mẫu. | UserRegistered được phát lại an toàn; EventId trùng không tạo dữ liệu trùng. |
| 10-11 | Problem Details, correlationId, giới hạn tần suất, nhật ký có cấu trúc, OpenTelemetry và OpenAPI. | Lỗi API có cùng định dạng; trace đi qua Gateway và Account. |
| 12-14 | Kiểm thử tích hợp, k6 cơ sở, bảng điều khiển tối thiểu, kiểm tra di trú lược đồ và cập nhật tài liệu. | Đạt NFR cơ sở của Account; có số liệu và bằng chứng trước khi sang Mạng xã hội. |

## Mức ưu tiên

| Mức | Mục đích | Phạm vi | Điều kiện hoàn thành |
| --- | --- | --- | --- |
| P0 | Nền tảng nghiệm thu bắt buộc | Tài khoản cốt lõi; mạng xã hội; bản chiếu/đọc bảng tin; trò chuyện; Outbox/Inbox; phân quyền; quan sát; sao lưu/khôi phục; CI/CD. | Mọi luồng chính và kịch bản lỗi đạt; không còn lỗi Critical/High; dựng môi trường và phục hồi bằng quy trình tự động. |
| P1 | Hoàn thiện sản phẩm | OTP/OAuth; xóa tài khoản; cộng đồng/RTC; phương tiện; bài viết video/chia sẻ; báo cáo và điều hành thủ công. | Chỉ bắt đầu sau P0; chức năng có kiểm thử tích hợp, quyền tài nguyên, metric và quy trình suy giảm. |
| P2 | Mở rộng có điều kiện | Thương mại; AI/tìm kiếm; gợi ý nâng cao; OpenSearch tùy chọn. | Chỉ bắt đầu khi P0/P1 không còn lỗi nghiêm trọng; được phép giảm phạm vi trước tiên khi chậm tiến độ. |
| Tương lai | Không thuộc cam kết | HA nhiều nút, Kubernetes, sharding, graph DB, phát công khai quy mô lớn, cổng thanh toán thật, kiểm duyệt tự động. | Chỉ triển khai khi có số liệu hoặc yêu cầu vận hành đủ rõ để biện minh độ phức tạp. |

## Cổng chuyển giai đoạn

| Cổng | Thời điểm | Điều kiện | Bằng chứng |
| --- | --- | --- | --- |
| G0 - Kiến trúc | Trước khi phát triển miền | Ranh giới dịch vụ, ownership, schema, API/event và quy ước lỗi đã được khóa. | ADR, sơ đồ, migration rỗng, kiểm thử kiến trúc. |
| G1 - P0 | Trước khi mở rộng sản phẩm | Luồng tài khoản -> bài viết -> Kafka -> bảng tin và gửi tin nhắn chạy xuyên suốt; lỗi broker/DB được xử lý đúng. | Trace, test report, dashboard, DLQ/outbox evidence. |
| G2 - P1 | Trước khi bắt đầu P2 | Cộng đồng, phương tiện, xóa tài khoản và điều hành đạt quyền, bảo mật, retry và khôi phục. | Integration tests, threat tests, restore drill. |
| G3 - P2 | Trước khi đóng phạm vi chức năng | Mỗi chức năng mở rộng đạt NFR riêng và có đường suy giảm không làm hỏng P0/P1. | Load test, fallback test, cost/resource metrics. |
| G4 - Phát hành | Trước khi bàn giao | Không lỗi nghiêm trọng; OpenAPI/AsyncAPI đồng bộ; backup/restore, rollback và demo được diễn tập. | Biên bản nghiệm thu, SBOM, runbook, bản phát hành theo commit. |

## Định nghĩa hoàn thành theo tài liệu nguồn

| Nhóm | Điều kiện đạt |
| --- | --- |
| Chức năng | Mã chức năng có API/event/data/test tương ứng; acceptance đạt; không còn TODO ẩn trên đường chính. |
| Mã nguồn | Build sạch, format/analyzer đạt, ranh giới tầng và dịch vụ đúng, không secret/debug code. |
| Dữ liệu | Migration up từ rỗng và từ bản trước; index/constraint/concurrency đúng; seed chỉ cho dev/test. |
| Hợp đồng | OpenAPI, schema sự kiện và AsyncAPI đồng bộ; không thay đổi phá vỡ không tăng phiên bản. |
| Kiểm thử | Unit + integration + contract + kịch bản lỗi; P0 bắt buộc 100% acceptance. |
| Bảo mật | Threat cases chính đạt; quét secret/dependency/container; không Critical/High chưa xử lý. |
| Quan sát | TraceId/correlationId, log có cấu trúc, metric RED và cảnh báo cho failure mode liên quan. |
| Khả năng chịu lỗi | Outbox/Inbox, retry/DLQ, fallback và idempotency được chứng minh bằng test. |
| Vận hành | Docker Compose/profile, healthcheck, backup/restore, migration, rollback và runbook đã diễn tập. |
| Tài liệu | ERD/UML/API/event/ADR/roadmap phản ánh đúng mã nguồn; không có nội dung lỗi thời hoặc trộn thuật ngữ không cần thiết. |

## Kịch bản trình diễn

| Bước | Kịch bản | Thao tác | Bằng chứng |
| --- | --- | --- | --- |
| 1 | Dựng hệ thống | Clone -> cấu hình secret -> docker compose up -> migration | Healthcheck toàn bộ; không thao tác tay trong DB. |
| 2 | Đăng ký/đăng nhập | Đăng ký, login, refresh rotation, thử reuse token | Token claims đúng; reuse thu hồi họ phiên. |
| 3 | Bài viết đến bảng tin | Tạo bài viết, xem Outbox/Kafka/Feed trace | Projection xuất hiện; duplicate event không tạo trùng. |
| 4 | Kafka gián đoạn | Tắt broker, tạo bài, bật lại | Ghi cục bộ thành công; Outbox phát sau; alert/metric đúng. |
| 5 | Trò chuyện | Gửi message, mất kết nối, reconnect | DB có trước realtime; lịch sử bù tin nhắn bị lỡ. |
| 6 | Phương tiện | Tạo URL, upload, complete, worker xử lý | Backend không nhận bytes; MediaReady; tệp giả bị từ chối. |
| 7 | Quyền và RTC | Người không phải thành viên xin token | Bị 403; thành viên đúng quyền kết nối; text chat không phụ thuộc RTC. |
| 8 | Điều hành | Báo cáo nội dung, moderator xử lý, người thường thử đọc queue | Audit/action/event đúng; truy cập trái quyền bị chặn. |
| 9 | Xóa tài khoản | Yêu cầu xóa, kiểm tra projection, chạy purge thử | Ẩn nhanh, ack đầy đủ, thao tác lặp không lỗi. |
| 10 | Khôi phục | Restore backup vào môi trường mới | Đạt RTO mục tiêu và chạy smoke test P0. |

## Hồ sơ bàn giao

| Nhóm | Thành phần |
| --- | --- |
| Mã nguồn | Repository, tag/commit phát hành, README dựng môi trường, quy ước nhánh và commit. |
| Hợp đồng | OpenAPI từng dịch vụ, AsyncAPI/schema sự kiện, collection Bruno/Postman và ví dụ lỗi. |
| Dữ liệu | Migration, ERD, seed dev/test, script backup/restore và biên bản restore drill. |
| Triển khai | Docker Compose profiles, Caddy/YARP config, healthcheck, release/rollback script. |
| Kiểm thử | Unit/integration/contract/load/security report; k6 scripts; danh sách known limitations. |
| Quan sát | Dashboard Grafana, alert rules, log/trace query mẫu và runbook xử lý sự cố. |
| Bảo mật | Threat model, SBOM, kết quả quét, danh sách secret cần cấp và lịch rotation. |
| Kiến trúc | Tài liệu thiết kế cuối, ADR, risk register, capacity assumptions và future evolution. |
| Demo | Kịch bản, dữ liệu mẫu, tài khoản theo vai trò, ảnh/video dự phòng khi hạ tầng mạng không ổn định. |
