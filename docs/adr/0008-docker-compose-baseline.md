# ADR-008 - Docker Compose một nút là cấu hình cơ sở

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Dự án do một người triển khai trong sáu tháng với ngân sách hạn chế; mục tiêu là chứng minh ranh giới và hành vi phân tán, không phải giả lập production quy mô lớn.

## Quyết định

Cấu hình cơ sở chạy bằng Docker Compose trên một máy/VPS, gồm profile cốt lõi và profile mở rộng. Không tuyên bố HA. Kubernetes, Kafka nhiều broker, PostgreSQL HA và LiveKit nhiều nút là hướng phát triển sau khi có nhu cầu đo được.

## Lý do

Giảm độ phức tạp vận hành để tập trung vào chất lượng chức năng, kiểm thử, quan sát và khả năng khôi phục.

## Hệ quả

- Chấp nhận điểm lỗi chung và giới hạn capacity.
- Backup, restore, health check và runbook trở nên quan trọng hơn.
- Một số thành phần như OpenSearch, AI đầy đủ hoặc observability có thể bật theo profile.

## Ràng buộc thực thi

- Tài liệu và demo phải công khai giới hạn một nút.
- Không dùng cấu hình một nút để suy diễn SLA production.
- Chỉ chuyển sang orchestration phức tạp hơn khi lợi ích đo được lớn hơn chi phí.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
