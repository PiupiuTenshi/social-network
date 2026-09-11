# Quy tắc cho Twight Light

Nguồn bắt buộc phải đọc trước khi chỉnh mã:

- `AGENTS.md`
- `RULES.md`
- `docs/CONTEXT_LOADING.md`

Quy tắc thực hiện:

- Xác định mã chức năng, dịch vụ sở hữu và tiêu chí chấp nhận trước khi viết mã.
- Không truy vấn chéo cơ sở dữ liệu, tạo khóa ngoại xuyên dịch vụ hoặc đặt quy tắc nghiệp vụ trong Gateway, API hay Infrastructure.
- Thay đổi API, sự kiện hoặc dữ liệu phải đồng bộ hợp đồng, kiểm thử và tài liệu.
- Bên phát dùng Outbox; bên nhận dùng Inbox và xử lý lặp an toàn.
- Kiểm tra phân quyền tại dịch vụ sở hữu tài nguyên; không ghi secret hoặc PII thô vào log.
- Không tuyên bố biên dịch hoặc kiểm thử đạt khi chưa chạy lệnh thành công.
- Không tự commit, push, merge, deploy, chạy di trú phá hủy hoặc thao tác môi trường vận hành.
