# Kiến trúc hệ thống

## Quy tắc cốt lõi

Mỗi thực thể giao dịch chỉ có một dịch vụ sở hữu. Dịch vụ khác dùng API đồng bộ hoặc bản chiếu từ sự kiện. Việc nhiều cơ sở dữ liệu dùng chung một PostgreSQL instance không cho phép truy vấn chéo.

## Các mặt phẳng

### Ứng dụng

YARP Gateway và tám dịch vụ: Tài khoản, Mạng xã hội, Cộng đồng, Trò chuyện, Bảng tin, Phương tiện, Thương mại, AI và tìm kiếm.

### Sự kiện

Kafka mang sự kiện bền vững và metadata vòng đời. Outbox thu hẹp khoảng trống giữa commit cơ sở dữ liệu và phát sự kiện; Inbox ngăn tác dụng phụ bị lặp.

### Thời gian thực

SignalR mang tin nhắn ứng dụng, presence, typing, biên nhận đọc, thông báo, lời mời gọi và luồng token AI. Dữ liệu quan trọng phải được lưu bền trước khi phát.

### Media

LiveKit/coturn mang âm thanh, video và chia sẻ màn hình. SeaweedFS lưu đối tượng tải lên. Không chuyển gói media vào Kafka hoặc SignalR và không chuyển tiếp byte tệp qua backend ứng dụng.

### Đọc và dữ liệu dẫn xuất

Bảng tin, cache, embedding và chỉ mục tìm kiếm là dữ liệu dẫn xuất. Mỗi loại phải có cách dựng lại, làm mất hiệu lực hoặc đối soát với dịch vụ nguồn.

## Hướng phụ thuộc trong một dịch vụ

```text
Api -> Application -> Domain
Infrastructure -> các cổng của Application/Domain
```

- Domain không phụ thuộc framework, HTTP, Kafka hoặc cơ sở dữ liệu.
- Application điều phối ca sử dụng và phụ thuộc các cổng trừu tượng.
- API chỉ xử lý giao thức, xác thực đầu vào và ánh xạ phản hồi.
- Infrastructure triển khai EF Core, Kafka và các adapter ngoài; không chứa quy tắc nghiệp vụ cốt lõi.

## Nhất quán và giao dịch

- ACID chỉ nằm trong cơ sở dữ liệu của một dịch vụ.
- Không dùng giao dịch phân tán giữa dịch vụ.
- Dữ liệu liên dịch vụ hội tụ qua sự kiện.
- Quy trình nhiều bước dùng state machine và hành động bù trừ.
- Mọi tác dụng phụ phải xử lý lặp an toàn và quan sát được.

## Thay đổi kiến trúc

Thay đổi ranh giới, ownership, mô hình nhất quán, hợp đồng công khai, nơi lưu trữ hoặc ranh giới tin cậy phải:

1. tạo ADR;
2. nêu di trú dữ liệu và tính tương thích;
3. cập nhật hợp đồng cùng kiểm thử;
4. có kế hoạch triển khai và quay lui hoặc tiến tới;
5. được duyệt trước khi viết mã sản phẩm.
