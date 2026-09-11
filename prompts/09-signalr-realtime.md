---
id: signalr
ket_qua_chinh: Luồng thời gian thực đúng quyền, bền vững và phục hồi được
---
# Triển khai thời gian thực bằng SignalR

## Chế độ thực hiện

Được phép chỉnh Hub, luồng ứng dụng, lưu trữ, quản lý nhóm và hợp đồng phía máy khách. Không dùng SignalR thay cho lưu trữ bền vững.

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

Triển khai luồng SignalR cho `{{FUNCTION_ID}}`, bảo đảm xác thực kết nối, kiểm tra thành viên, lưu trước phát, xử lý gửi lặp, kết nối lại và phân phối đúng nhóm.

## Yêu cầu bắt buộc

- Danh tính lấy từ claim; không tin `userId` do máy khách gửi.
- Tin nhắn bền vững phải được ghi thành công trước `MessageCreated`; DB lỗi không tạo tin nhắn ảo.
- Dùng `clientMessageId` hoặc khóa tương đương để gửi lặp trả lại kết quả cũ.
- Tư cách thành viên nhóm được thêm/xóa theo quyền thực tế và kiểm tra lại tại hành động quan trọng.
- Hiện diện/trạng thái gõ là trạng thái tạm thời có TTL; read cursor chỉ tiến.
- RTC media không đi qua SignalR.

## Quy trình

1. Truy vết phương thức Hub, trình xử lý ứng dụng, cơ sở dữ liệu, Outbox, nhóm và phía máy khách nhận sự kiện.
2. Lập sơ đồ thứ tự lưu, phát, acknowledgement, reconnect và bù lịch sử.
3. Triển khai thay đổi nhỏ nhất và thêm log/metric theo `connectionId`, `userId`, `conversationId`, `correlationId` an toàn.
4. Thêm kiểm thử quyền, `clientMessageId` lặp, lỗi cơ sở dữ liệu, kết nối lại và nhiều thiết bị.
5. Chạy kiểm thử mục tiêu, kiểm thử tích hợp SignalR/cơ sở dữ liệu và biên dịch.
6. Rà soát rò rỉ nhóm, thứ tự và tranh chấp khi ngắt kết nối và dữ liệu nhạy cảm.

## Tiêu chí hoàn thành

- Người không có quyền không nhận hoặc phát dữ liệu.
- Mọi dữ liệu bền vững có thể khôi phục sau reconnect.
- Không có tin nhắn ảo hoặc duplicate side effect.

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
