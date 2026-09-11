# ADR-007 - RAG giới hạn theo phạm vi phân quyền

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

RAG có thể làm lộ nội dung riêng tư nếu dữ liệu được lập chỉ mục hoặc truy xuất như một corpus toàn cục không có metadata quyền.

## Quyết định

Dịch vụ nguồn cấp nội dung hoặc phạm vi truy xuất đã được kiểm tra quyền. AI/Search không truy vấn trực tiếp cơ sở dữ liệu dịch vụ khác. Metadata chunk và embedding phải giữ nguồn, phạm vi, chủ thể và phiên bản quyền cần thiết để lọc trước khi đưa vào prompt.

## Lý do

Phân quyền trước retrieval và context exposure là ranh giới bảo mật bắt buộc, không thể giao cho mô hình tự quyết định.

## Hệ quả

- Tăng chi phí hợp đồng và đồng bộ metadata quyền.
- Nội dung bị xóa hoặc đổi quyền phải làm mất hiệu lực chunk, embedding và cache.
- Khi không xác minh được quyền, hệ thống từ chối hoặc dùng fallback an toàn.

## Ràng buộc thực thi

- Không đưa secret, PII không cần thiết hoặc nội dung ngoài phạm vi vào prompt.
- Mọi truy vấn RAG phải có actor và scope rõ.
- Prompt injection không được phép thay đổi luật phân quyền hoặc nguồn dữ liệu.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
