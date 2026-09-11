---
id: kafka
ket_qua_chinh: Sự kiện có hợp đồng, xử lý lặp an toàn và khả năng vận hành
---
# Thiết kế hoặc triển khai sự kiện Kafka

## Chế độ thực hiện

Được phép chỉnh bên phát, bên nhận, lược đồ sự kiện, Outbox/Inbox và kiểm thử. Không đổi phiên bản hoặc phát lại dữ liệu vận hành khi chưa được cho phép.

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

Thiết kế hoặc triển khai sự kiện liên quan `{{FUNCTION_ID}}`, khóa bên phát, bên nhận, khóa phân vùng, phiên bản lược đồ, thứ tự, thử lại, DLQ, phát lại và khả năng quan sát.

## Yêu cầu bắt buộc

- Ghi dữ liệu nghiệp vụ và Outbox trong cùng giao dịch; không phát trước commit.
- Bên nhận xử lý giao nhận ít nhất một lần bằng Inbox hoặc khóa xử lý lặp trong cùng giao dịch với tác dụng phụ.
- Dùng `eventId`, `eventType`, `eventVersion`, `occurredAt`, `producer`, `correlationId`, `aggregateId` và `payload` theo quy ước.
- Phân biệt lỗi tạm thời, dữ liệu độc và lỗi nghiệp vụ; thử lại có giới hạn và giãn cách tăng dần.
- Trong cùng phiên bản chính chỉ thêm trường tùy chọn; thay đổi phá vỡ dùng phiên bản mới.
- Replay không được gửi lặp email, thanh toán, thông báo ngoài ý muốn hoặc hành động điều hành.

## Quy trình

1. Đọc danh mục sự kiện, danh mục topic, bên phát/bên nhận hiện tại và kho lược đồ hoặc tệp hợp đồng.
2. Lập ma trận bên phát, bên nhận, key, version, thứ tự, thử lại/DLQ và side effect.
3. Triển khai bên phát/bên nhận cùng Outbox/Inbox tại đúng ranh giới giao dịch.
4. Thêm kiểm thử hợp đồng, kiểm thử giao lặp, thứ tự/version test và kiểm thử lỗi.
5. Chạy kiểm thử mục tiêu, biên dịch và kiểm thử tích hợp với broker thử nghiệm.
6. Ghi bảng điều khiển/cảnh báo cần theo dõi, quy trình phát lại và tính tương thích.

## Tiêu chí hoàn thành

- Sự kiện trùng không tạo tác dụng phụ trùng.
- Broker tạm ngừng không làm mất dữ liệu đã commit.
- Schema và catalog được đồng bộ.

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
