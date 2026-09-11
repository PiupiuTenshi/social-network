# Hồ sơ bằng chứng thực thi

Thư mục này chưa có bằng chứng READY/DONE của mã sản phẩm. Không sao chép kết quả kiểm bộ tài liệu thành kết quả kiểm sản phẩm.

Dùng `task_gate.py template ID readiness|completion|review --output docs/execution/evidence/...json` để tạo mẫu chưa đạt. Giữ riêng manifest readiness, completion, review và artifact của từng ID/lần chạy; không ghi đè bằng chứng đã accept. Xem [READY_GATE.md](../READY_GATE.md).

Chỉ đưa artifact đã loại secret/PII vào Git. Artifact lớn đặt tại kho CI được kiểm soát; lưu bản report/checksum nhỏ tại đây và liên kết đến artifact CI trong report. Cổng local kiểm tra file report và hash, reviewer phải kiểm tra cả artifact CI gốc.
