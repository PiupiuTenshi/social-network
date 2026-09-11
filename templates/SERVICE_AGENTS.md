# Hướng dẫn cục bộ cho [TÊN_DỊCH_VỤ]

Tệp này được đặt thành `[đường-dẫn-dịch-vụ]/AGENTS.md`. Nó bổ sung `AGENTS.md` ở thư mục gốc và không được nới lỏng bất kỳ điều cấm nào của kho mã.

## Phạm vi áp dụng

- Thư mục:
- Dịch vụ sở hữu:
- Mã chức năng chính:

## Quyền sở hữu dữ liệu

- Aggregate và thực thể được sở hữu:
- Cơ sở dữ liệu logic:
- Bảng nguồn sự thật:
- Bản chiếu được phép duy trì:
- Dữ liệu tuyệt đối không được truy cập trực tiếp:

## Hợp đồng

- API được phát hành:
- Sự kiện được phát hành:
- Sự kiện được nhận:
- SignalR hoặc RTC liên quan:
- Bên sử dụng chính:

## Hướng phụ thuộc và quy ước cục bộ

- Tầng và thư mục:
- Mẫu tương tự cần tham khảo:
- Quy tắc transaction, Outbox/Inbox và xử lý lặp an toàn:
- Quy tắc phân quyền:
- Quy tắc log, metric và trace:

## Kiểm chứng

- Khôi phục phụ thuộc:
- Biên dịch:
- Kiểm thử đơn vị:
- Kiểm thử tích hợp:
- Kiểm thử hợp đồng:
- Chạy cục bộ:

Chỉ ghi lệnh đã được xác minh trong kho mã. Giữ `CHƯA XÁC MINH` đối với lệnh chưa tồn tại.

## Điều kiện dừng cục bộ

Dừng và hỏi trước khi thay đổi quyền sở hữu, hợp đồng công khai, lược đồ phá vỡ, chính sách lưu giữ, phân quyền, secret, tác dụng phụ ngoài hệ thống hoặc thao tác môi trường vận hành.
