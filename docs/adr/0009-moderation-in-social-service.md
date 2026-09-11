# ADR-009 - Metadata điều hành nội dung thuộc Mạng xã hội

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Baseline cần báo cáo và điều hành thủ công nhưng không muốn thêm một deployable service chỉ cho moderation trong giai đoạn P1.

## Quyết định

Social Service sở hữu `content_report`, bằng chứng và metadata hành động điều hành. Dịch vụ sở hữu nội dung thật vẫn chịu trách nhiệm áp dụng ẩn, xóa hoặc hạn chế tài nguyên của nó qua hợp đồng hoặc sự kiện.

## Lý do

Giữ số lượng dịch vụ phù hợp phạm vi trong khi vẫn tách audit điều hành khỏi dữ liệu nội dung nguồn.

## Hệ quả

- Cần event hoặc command result để Social biết hành động đã được áp dụng.
- Bằng chứng phải bất biến và có chính sách lưu giữ riêng.
- Có coupling hợp đồng giữa Social và các dịch vụ sở hữu nội dung.

## Ràng buộc thực thi

- Người dùng thường không được truy cập hàng đợi điều hành.
- Mọi hành động phải có actor, lý do, timestamp và audit.
- AI moderation chỉ gắn cờ; không tự động xóa trong baseline.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
