# Bối cảnh dự án

## Sản phẩm

**Twight Light** là nền tảng xã hội đa cộng đồng gồm tài khoản, quan hệ xã hội, bài viết, bảng tin, cộng đồng, trò chuyện thời gian thực, phương tiện, thương mại và AI/tìm kiếm.

Các luồng quan trọng:

- đăng ký, đăng nhập và xoay vòng refresh token;
- tạo bài viết -> Outbox -> Kafka -> bản chiếu Bảng tin;
- gửi tin nhắn -> lưu bền -> SignalR -> sự kiện tích hợp;
- tải trực tiếp -> xác minh -> xử lý -> `MediaReady`;
- tham gia kênh RTC bằng token LiveKit có giới hạn quyền;
- tạo đơn -> giữ tồn kho -> thanh toán giả lập -> bù trừ;
- RAG và tìm kiếm chỉ trên dữ liệu người dùng được phép truy cập;
- báo cáo vi phạm và thực thi điều hành có nhật ký kiểm toán;
- xóa tài khoản và lan truyền yêu cầu xóa hoặc ẩn danh giữa các dịch vụ.

## Kiến trúc cơ sở

- Vi dịch vụ kết hợp kiến trúc hướng sự kiện.
- Nhất quán mạnh trong từng dịch vụ; nhất quán cuối giữa các dịch vụ.
- PostgreSQL dùng nhiều cơ sở dữ liệu logic; mỗi dịch vụ có thông tin truy cập và di trú riêng.
- Kafka kết hợp Transactional Outbox; cách giao at-least-once; bên nhận xử lý lặp an toàn bằng Inbox.
- SignalR cho thời gian thực của ứng dụng; LiveKit/coturn cho âm thanh, video và màn hình.
- Valkey cho cache, presence và giới hạn tần suất; không phải nguồn dữ liệu chuẩn.
- SeaweedFS giữ đối tượng nhị phân; backend quản lý metadata và URL ký trước.
- pgvector cho embedding; OpenSearch là thành phần tùy chọn.
- YARP làm API Gateway; Caddy kết thúc HTTPS.
- OpenTelemetry, Prometheus, Grafana và Jaeger/Zipkin hỗ trợ quan sát.

## Ràng buộc

- Một lập trình viên thực hiện trong sáu tháng.
- Hạ tầng cơ sở là một VPS chạy Docker Compose, một Kafka broker và một LiveKit node.
- Phải bảo vệ P0 và P1; cắt P2 trước khi đánh đổi kiểm thử, bảo mật, sao lưu/khôi phục hoặc tài liệu.
- Không tuyên bố khả năng HA hoặc quy mô production khi chưa có hạ tầng và số liệu chứng minh.

## Công nghệ và phiên bản

Tên công nghệ được khóa bởi thiết kế; **phiên bản cụ thể phải lấy từ kho mã**:

- .NET, ASP.NET Core và EF Core: `global.json`, `Directory.Packages.props`, `*.csproj`.
- Angular và Node: `package.json`, lockfile và `.nvmrc` nếu có.
- Hạ tầng: Docker Compose cùng image tag hoặc digest.

Không đoán phiên bản trong prompt hoặc tài liệu.

## Phạm vi ưu tiên

- **P0:** Tài khoản cốt lõi, Mạng xã hội, Bảng tin, Trò chuyện, Outbox/Inbox, phân quyền, quan sát, sao lưu/khôi phục và CI/CD.
- **P1:** OTP/OAuth, xóa tài khoản, Cộng đồng/RTC, Phương tiện, video/chia sẻ và điều hành thủ công.
- **P2:** Thương mại, AI/tìm kiếm, gợi ý nâng cao và OpenSearch tùy chọn.
- **Tương lai:** HA, Kubernetes, sharding, cơ sở dữ liệu đồ thị, phát sóng lớn, thanh toán thật và điều hành nội dung tự động bằng AI.


## Giao diện người dùng đã khóa

- UI/UX 1.2 Final gồm 47 màn hình Desktop/Mobile.
- Nguồn tổng hợp: `design/design.md`; bản tiện dụng: `design.md`.
- Token máy đọc được: `design/tokens/design-tokens.json`.
- Khoảng trống hợp đồng: `design/sources/18-backend-contract-gaps.md`.
- Tính năng P2 và gap mặc định tắt cho đến khi hợp đồng Backend được duyệt.
