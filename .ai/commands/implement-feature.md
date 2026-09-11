---
id: backend-feature
ket_qua_chinh: Chức năng Backend .NET hoàn chỉnh theo hợp đồng
---
# Triển khai lát cắt dọc Backend .NET

## Chế độ thực hiện

Được phép chỉnh mã và kiểm thử trong phạm vi chức năng. Không được đổi hợp đồng, quyền sở hữu hoặc phụ thuộc nền khi chưa có quyết định riêng.

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

Triển khai `{{FUNCTION_ID}}` xuyên suốt trong dịch vụ sở hữu, từ hợp đồng giao tiếp đến Application/Domain, lưu trữ hoặc tích hợp, ánh xạ lỗi, khả năng quan sát, kiểm thử và tài liệu liên quan.

## Yêu cầu bắt buộc

- Bám mẫu thực tế của solution; không áp đặt kiến trúc hoặc thư viện mới.
- Truyền `CancellationToken` qua mọi I/O; không sync-over-async, N+1 hoặc truy vấn không giới hạn.
- Bảo vệ transaction, ràng buộc duy nhất/kiểm tra/phiên bản, Outbox/Inbox và xử lý lặp an toàn khi liên quan.
- Kiểm tra phân quyền tại dịch vụ sở hữu; không tin `userId` hoặc role từ payload.
- Không trả EF entity, exception nội bộ, secret hoặc PII qua API/log.
- Thêm kiểm thử đơn vị và kiểm thử HTTP/cơ sở dữ liệu/hợp đồng phù hợp.

## Quy trình

1. Đọc một lát cắt tương tự và truy vết luồng hiện tại.
2. Tóm tắt kế hoạch ngắn cùng tệp/ký hiệu dự kiến trước khi chỉnh sửa.
3. Triển khai thay đổi nhỏ nhất nhưng đầy đủ theo chiều dọc.
4. Cập nhật di trú dữ liệu, OpenAPI, lược đồ sự kiện, metric/trace/log và tài liệu khi bị ảnh hưởng.
5. Chạy kiểm thử mục tiêu, công cụ định dạng/phân tích tĩnh, biên dịch, kiểm thử tích hợp/hợp đồng rồi bộ rộng phù hợp.
6. Rà soát diff cho tính đúng, phân quyền, toàn vẹn dữ liệu, đồng thời, tương thích và hiệu năng.

## Tiêu chí hoàn thành

- Mọi tiêu chí chấp nhận có bằng chứng.
- Không có đường xử lý bỏ qua quyền hoặc transaction.
- Lệnh kiểm chứng và kết quả thực tế được ghi đầy đủ.

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
