# Quy tắc tối thiểu cho trợ lý AI

Nguồn đầy đủ là [`AGENTS.md`](AGENTS.md) và [`RULES.md`](RULES.md). Tệp chữ thường này là điểm vào tương thích cho công cụ chỉ tìm `rule.md`.

1. Không truy vấn hoặc ghi cơ sở dữ liệu của dịch vụ khác.
2. Không đổi API, sự kiện, lược đồ, ownership hoặc bảo mật khi chưa có hợp đồng/ADR.
3. Không sinh mã trước khi xác định mã chức năng, dịch vụ sở hữu và tiêu chí chấp nhận.
4. Không che lỗi bằng `catch` rộng, thử lại vô hạn, giá trị mặc định hoặc phương án dự phòng sai ý nghĩa.
5. Mọi I/O bất đồng bộ phải truyền `CancellationToken`.
6. Bên phát dùng Outbox; bên nhận dùng Inbox hoặc khóa xử lý lặp an toàn.
7. Kiểm tra phân quyền tại dịch vụ sở hữu tài nguyên.
8. Không ghi secret, token, OTP hoặc PII thô vào mã, log, issue hoặc prompt.
9. Bắt buộc có kiểm thử cho hành vi chính và tình huống lỗi/tranh chấp phù hợp.
10. Không tuyên bố lệnh đạt nếu chưa chạy.
11. Không commit, push, deploy hoặc chạy thao tác phá hủy khi chưa được yêu cầu rõ.
12. Đọc `AGENTS.md` và `RULES.md` trước khi chỉnh sửa kho mã.
