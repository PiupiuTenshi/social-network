# ADR-002 - Cơ sở dữ liệu logic riêng cho từng dịch vụ

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Bản triển khai cơ sở dùng một PostgreSQL instance để giảm chi phí, nhưng vẫn phải giữ ranh giới dữ liệu của kiến trúc microservices.

## Quyết định

Mỗi dịch vụ dùng tên cơ sở dữ liệu logic, tài khoản truy cập và lịch sử migration riêng. Tài khoản của một dịch vụ không được cấp quyền đọc hoặc ghi cơ sở dữ liệu của dịch vụ khác.

## Lý do

Tách quyền và migration giúp phát hiện truy cập chéo sớm, giữ khả năng tách instance về sau và tránh coupling qua lược đồ dùng chung.

## Hệ quả

- Một PostgreSQL instance vẫn là điểm lỗi chung trong baseline một nút.
- Không dùng transaction xuyên dịch vụ; các luồng liên dịch vụ dùng sự kiện hoặc orchestration phù hợp.
- Backup và restore phải hỗ trợ từng cơ sở dữ liệu logic và toàn instance.

## Ràng buộc thực thi

- Không tạo view, synonym hoặc connection string dùng chung để né ranh giới.
- Tách instance, replica hoặc HA chỉ thực hiện khi có nhu cầu và số liệu vận hành.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
