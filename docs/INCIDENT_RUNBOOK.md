# Runbook xử lý sự cố

## Nguyên tắc an toàn

Ưu tiên thao tác chỉ đọc. Không đổi production, dữ liệu, cờ chức năng, quyền, secret hoặc hạ tầng khi chưa có ủy quyền rõ. Không đưa PII hoặc secret vào kênh điều tra.

## Quy trình

1. Ghi thời điểm, phiên bản, môi trường, người báo và correlation/trace ID.
2. Xác định tác động, phạm vi ảnh hưởng, mức độ và chức năng P0 bị ảnh hưởng.
3. Kiểm tra deploy, cấu hình, di trú và thay đổi phụ thuộc gần nhất.
4. Thu thập tỷ lệ lỗi, độ trễ, Outbox, consumer lag, DLQ, pool/đĩa cơ sở dữ liệu, Valkey, LiveKit và hàng đợi AI.
5. Lập ma trận giả thuyết -> tín hiệu xác nhận hoặc bác bỏ -> truy vấn an toàn.
6. Tách biện pháp giảm thiểu, bản sửa nguyên nhân gốc, kiểm chứng, triển khai và quay lui.
7. Sau khi khôi phục, viết báo cáo sự cố và công việc phòng ngừa có người phụ trách cùng thời hạn.

## Tình huống nhanh

- **Kafka ngừng:** không xóa Outbox; khôi phục broker, theo dõi backlog/lag và kiểm tra xử lý sự kiện trùng.
- **Cơ sở dữ liệu ngừng:** dừng ghi an toàn, kiểm tra đĩa/pool; không tự khôi phục lên production khi chưa duyệt.
- **DLQ tăng:** dừng phát lại, xác định lỗi lược đồ/dữ liệu/nguyên nhân gốc, chạy thử với lô nhỏ.
- **SignalR lỗi:** API và lịch sử vẫn là nguồn; kiểm tra kết nối lại và phân quyền group.
- **LiveKit lỗi:** giữ trò chuyện văn bản; trả `503` rõ cho cấp token hoặc tham gia phòng.
- **Valkey lỗi:** cache và presence suy giảm; không coi cache là nguồn chuẩn.
- **SeaweedFS lỗi:** phiên tải lên hết hạn và dọn đối tượng mồ côi; không đánh dấu `Ready` khi chưa xác minh đối tượng.

Dùng mẫu `templates/INCIDENT_REPORT.md`.
