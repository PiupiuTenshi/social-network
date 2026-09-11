# Hướng dẫn cho GitHub Copilot

Luôn tuân thủ `AGENTS.md`, `RULES.md` và hướng dẫn cục bộ gần tệp đang chỉnh sửa nhất.

Trước khi đề xuất hoặc sửa mã:

1. Xác định mã chức năng, dịch vụ sở hữu, nguồn sự thật và tiêu chí chấp nhận.
2. Đọc luồng mã hiện tại, kiểm thử tương tự, hợp đồng, di trú dữ liệu và thay đổi Git chưa commit.
3. Đánh giá ảnh hưởng đến API, dữ liệu, sự kiện, phân quyền, xử lý đồng thời, xử lý lặp an toàn và khả năng quan sát.
4. Chỉ tạo thay đổi nhỏ nhất nhưng hoàn chỉnh theo chiều dọc.

Không được:

- truy cập trực tiếp cơ sở dữ liệu của dịch vụ khác;
- bỏ qua Outbox/Inbox, phân quyền hoặc kiểm thử;
- ghi secret, token, OTP hoặc PII thô vào mã và log;
- đoán phiên bản, đường dẫn, lệnh hoặc hành vi chưa được xác minh;
- tự commit, push, merge, deploy hoặc chạy thao tác phá hủy.

Với Backend .NET, ưu tiên I/O bất đồng bộ có `CancellationToken`, truy vấn EF Core có giới hạn và phép chiếu rõ ràng, nullable đúng thực tế, transaction đúng ranh giới và kiểm thử hành vi quan sát được.
