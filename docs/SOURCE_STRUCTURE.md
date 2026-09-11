# Cấu trúc mã nguồn mục tiêu

```text
src/
  Gateway/
  BuildingBlocks/
  Services/
    Account/
      Account.Api/
      Account.Application/
      Account.Domain/
      Account.Infrastructure/
    Social/
    Community/
    Chat/
    Feed/
    Media/
    Commerce/
    AiSearch/
tests/
  Unit/
  Integration/
  Contract/
  Architecture/
  EndToEnd/
deploy/
  compose/
  caddy/
  migrations/
  observability/
docs/
  adr/
  reference/
```

Tên thực tế có thể khác nếu kho mã đã có quy ước. Không đổi cấu trúc chỉ để khớp tài liệu; ghi nhận chênh lệch và cập nhật tài liệu khi cấu trúc hiện tại đã được chấp thuận.

## Quy tắc

- Mỗi dịch vụ có điểm khởi động, cấu hình đã xác thực, health check, di trú dữ liệu và kiểm thử riêng.
- Mã dùng chung chỉ nằm trong `BuildingBlocks` khi ổn định và không mang ý nghĩa nghiệp vụ riêng của một miền.
- Không tạo thư mục “common” để né hướng phụ thuộc.
- Kiểm thử được đặt theo hành vi và mã chức năng, không chỉ theo tên lớp.
- Artifact triển khai gắn với commit bất biến; không dùng tag `latest` làm nguồn duy nhất.
