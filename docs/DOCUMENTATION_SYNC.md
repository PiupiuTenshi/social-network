# Đồng bộ tài liệu với mã nguồn

## Khi nào phải cập nhật

- Yêu cầu/phản hồi, mã trạng thái, lỗi, phân quyền hoặc phân trang API.
- Loại sự kiện, nội dung, khóa phân vùng, topic, phiên bản hoặc bên nhận.
- Entity, bảng, chỉ mục, ràng buộc, di trú hoặc chính sách lưu giữ.
- Quyền sở hữu dịch vụ hoặc hướng phụ thuộc.
- Cấu hình, tên secret, health check, deploy, sao lưu hoặc quay lui.
- NFR, metric, cảnh báo, kiểm thử hoặc giới hạn đã biết.

## Artifact tương ứng

- HTTP: OpenAPI, `reference/API_CATALOG.md` và ví dụ.
- Sự kiện: lược đồ/AsyncAPI, danh mục sự kiện và topic.
- Dữ liệu: di trú, ERD và `reference/DATA_MODEL.md`.
- Kiến trúc: ADR, `ARCHITECTURE.md` và `SERVICE_BOUNDARIES.md`.
- Vận hành: runbook, danh sách phát hành, dashboard và cảnh báo.
- Chức năng: đặc tả chức năng, ma trận truy vết và kiểm thử chấp nhận.

## Quy tắc

Hợp đồng có thể được sinh từ mã, nhưng ý nghĩa phải khớp nguồn sự thật. Không hợp nhất pull request khi tài liệu vẫn mô tả hành vi cũ hoặc chỗ trống bị trình bày như dữ kiện.
