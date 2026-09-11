# Hồ sơ quyết định kiến trúc

ADR ghi lại các quyết định có ảnh hưởng lâu dài đến ranh giới dịch vụ, dữ liệu, hợp đồng, bảo mật và vận hành.

## Quy tắc quản lý

- Trạng thái dùng một trong: `Đề xuất`, `Chấp thuận`, `Thay thế`, `Hủy`.
- Không sửa lịch sử của ADR đã chấp thuận để làm như quyết định cũ chưa từng tồn tại.
- Khi thay đổi quyết định, tạo ADR mới và liên kết ADR bị thay thế.
- Mỗi ADR phải có bối cảnh, quyết định, lý do, hệ quả, ràng buộc thực thi và điều kiện xem xét lại.
- Dùng [`../../templates/ADR.md`](../../templates/ADR.md) khi tạo quyết định mới.

## Danh mục

- `ADR-001`: Mỗi aggregate chỉ có một dịch vụ sở hữu.
- `ADR-002`: Cơ sở dữ liệu logic riêng cho từng dịch vụ.
- `ADR-003`: Kafka, Transactional Outbox và giao nhận ít nhất một lần.
- `ADR-004`: Tách mặt phẳng SignalR và LiveKit.
- `ADR-005`: Bảng tin dùng bản chiếu theo CQRS.
- `ADR-006`: Tải phương tiện trực tiếp bằng URL ký trước.
- `ADR-007`: RAG giới hạn theo phạm vi phân quyền.
- `ADR-008`: Docker Compose một nút là cấu hình cơ sở.
- `ADR-009`: Metadata điều hành nội dung thuộc Mạng xã hội.
- `ADR-010`: Phạm vi P0/P1/P2 và cổng chất lượng.
