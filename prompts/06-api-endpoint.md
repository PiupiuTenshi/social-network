---
id: api
ket_qua_chinh: Hợp đồng API tương thích, an toàn và có kiểm thử
---
# Thiết kế hoặc thay đổi điểm cuối API

## Chế độ thực hiện

Được phép chỉnh hợp đồng và phần triển khai trong phạm vi đã phê duyệt. Thay đổi phá vỡ phải dừng để có phiên bản hoặc kế hoạch chuyển đổi.

## Đầu vào

- Mã nhiệm vụ: `{{TASK_ID}}`
- Loại nhiệm vụ: `{{TASK_TYPE}}`
- Mã chức năng hoặc vấn đề: `{{FUNCTION_ID}}`
- Miền: `{{DOMAIN}}`
- Yêu cầu: {{DESCRIPTION}}
- Hành vi hiện tại hoặc bằng chứng: {{EVIDENCE}}
- Ràng buộc và phần ngoài phạm vi: {{CONSTRAINTS}}
- Tiêu chí chấp nhận: {{ACCEPTANCE_CRITERIA}}

## Bối cảnh bắt buộc

1. Đọc `AGENTS.md`, `RULES.md` và hướng dẫn cục bộ gần tệp sẽ chỉnh nhất.
2. Nạp tài liệu theo `.ai/context-map.yaml` thay vì đưa toàn bộ kho mã vào ngữ cảnh.
3. Kiểm tra `git status`, phần khác biệt chưa commit, tệp khai báo phụ thuộc, hợp đồng, di trú dữ liệu và kiểm thử liên quan.
4. Phân biệt dữ kiện, suy luận, giả định và điểm chưa biết; không biến chỗ trống thành dữ kiện.

## Hành động

Thiết kế hoặc triển khai điểm cuối cho `{{FUNCTION_ID}}`, đồng bộ yêu cầu/phản hồi, Problem Details, phân quyền, xử lý lặp an toàn, phân trang hoặc xử lý đồng thời với OpenAPI và bên sử dụng.

## Yêu cầu bắt buộc

- Xác định tất cả bên sử dụng và hợp đồng hiện tại trước khi đổi.
- Đường dẫn dùng `/api/v1`; JSON `camelCase`; thời gian UTC ISO 8601; danh sách lớn dùng cursor.
- Tài nguyên có version dùng `ETag`/`If-Match`; khóa cũ trả `412` theo hợp đồng.
- Tác vụ có nguy cơ lặp dùng `Idempotency-Key`; cùng khóa khác nội dung trả `409`.
- Không làm lộ exception, dữ liệu nội bộ hoặc trường nhạy cảm.
- Cập nhật OpenAPI, ví dụ yêu cầu/phản hồi và kiểm thử hợp đồng.

## Quy trình

1. Đọc điểm cuối, DTO, chính sách, nơi gọi và OpenAPI hiện tại.
2. Lập bảng đầu vào, kiểm tra dữ liệu, phản hồi thành công, lỗi, phân quyền và tính tương thích.
3. Thực hiện thay đổi nhỏ nhất tại đúng ranh giới transport/application.
4. Cập nhật máy khách hoặc bộ chuyển đổi bị ảnh hưởng trong phạm vi đã chốt.
5. Chạy kiểm thử hợp đồng/HTTP mục tiêu, biên dịch và bộ tích hợp liên quan.
6. Báo rõ thay đổi phá vỡ, cửa sổ tương thích và cách triển khai/quay lui.

## Tiêu chí hoàn thành

- OpenAPI và mã triển khai khớp nhau.
- Mọi mã trạng thái và mã lỗi có kiểm thử.
- Bên sử dụng không bị phá vỡ ngoài kế hoạch đã phê duyệt.

## Điều kiện dừng

Dừng và hỏi trước khi tiếp tục nếu thiếu thông tin có thể làm thay đổi dịch vụ sở hữu, hợp đồng công khai, lược đồ dữ liệu, bảo mật, thao tác phá hủy hoặc tác dụng phụ ngoài hệ thống. Không tự commit, push, merge, deploy hoặc thao tác môi trường vận hành.

## Đầu ra và bàn giao

- Kết quả chính và trạng thái: hoàn thành, một phần hoặc bị chặn.
- Tệp hoặc ký hiệu đã đọc; tệp đã đổi và lý do khi chế độ cho phép chỉnh sửa.
- Ảnh hưởng đến API, dữ liệu, sự kiện, bảo mật và vận hành.
- Quyết định, đánh đổi, giả định và điểm chưa biết.
- Lệnh đã chạy cùng kết quả thật; không báo đạt cho lệnh chưa chạy.
- Ánh xạ từng tiêu chí chấp nhận sang mã, kiểm thử hoặc bằng chứng.
- Rủi ro còn lại, phụ thuộc và công việc kế tiếp.
