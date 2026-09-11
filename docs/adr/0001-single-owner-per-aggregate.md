# ADR-001 - Mỗi aggregate chỉ có một dịch vụ sở hữu

- Trạng thái: Chấp thuận
- Ngày: 2026-09-05

## Bối cảnh

Hệ thống gồm nhiều dịch vụ độc lập. Nếu nhiều dịch vụ cùng ghi một aggregate hoặc truy cập trực tiếp cùng bảng, bất biến nghiệp vụ, quyền sửa dữ liệu và trách nhiệm xử lý sự cố sẽ trở nên mơ hồ.

## Quyết định

Mỗi aggregate giao dịch chỉ được một dịch vụ sở hữu và ghi. Dịch vụ khác phải dùng API của dịch vụ sở hữu hoặc duy trì bản chiếu từ sự kiện. Không tạo khóa ngoại vật lý hoặc truy vấn trực tiếp xuyên cơ sở dữ liệu dịch vụ.

## Lý do

Quyết định này giữ ranh giới nhất quán rõ ràng, cho phép triển khai và di trú độc lập, đồng thời tránh việc một dịch vụ phá vỡ bất biến của dịch vụ khác.

## Hệ quả

- Chấp nhận nhất quán cuối cùng giữa các dịch vụ.
- Phải thiết kế API, sự kiện, bản chiếu và quy trình đối soát rõ ràng.
- Một số luồng đọc cần dữ liệu tóm tắt cục bộ thay vì nối bảng xuyên dịch vụ.

## Ràng buộc thực thi

- Mọi thay đổi quyền sở hữu cần ADR thay thế và kế hoạch di trú dữ liệu.
- Gateway, worker và dịch vụ AI không được trở thành đường vòng truy cập dữ liệu nguồn.

## Điều kiện xem xét lại

Chỉ xem xét lại khi có số liệu vận hành, yêu cầu sản phẩm hoặc ràng buộc mới đủ mạnh để biện minh chi phí chuyển đổi. ADR thay thế phải nêu rõ di trú dữ liệu, tính tương thích, triển khai và quay lui hoặc tiến tiếp.
