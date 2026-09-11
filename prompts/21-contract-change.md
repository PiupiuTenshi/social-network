---
id: contract-change
ket_qua_chinh: Kế hoạch hợp đồng tương thích và có đường chuyển đổi
---
# Quản lý thay đổi hợp đồng liên dịch vụ

## Chế độ thực hiện

Thiết kế trước, triển khai chỉ khi phạm vi ghi rõ. Không phát hành thay đổi phá vỡ hoặc di trú dữ liệu phá hủy trong cùng bước nếu chưa có phê duyệt.

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

Đánh giá thay đổi `{{DESCRIPTION}}` trên API, sự kiện, SignalR hoặc hợp đồng dữ liệu; kiểm kê bên phát/bên nhận, thiết kế phiên bản hóa, tính tương thích, triển khai và ngừng hỗ trợ.

## Yêu cầu bắt buộc

- Xác định nguồn sự thật và tất cả bên phát/bên nhận/nơi gọi.
- Phân loại bổ sung, thay đổi hành vi hoặc thay đổi phá vỡ.
- Trong cùng phiên bản chính chỉ thêm trường tùy chọn có ý nghĩa mặc định rõ.
- Thay đổi phá vỡ dùng điểm cuối/topic/event version mới hoặc giai đoạn đọc kép/ghi kép phù hợp.
- Cập nhật kiểm thử hợp đồng, ví dụ, OpenAPI/AsyncAPI/lược đồ và ADR.
- Không xóa hợp đồng cũ trước khi có bằng chứng mọi bên nhận đã chuyển.

## Quy trình

1. Lập danh sách hợp đồng hiện tại và bên nhận.
2. Đề xuất phương án tương thích cùng đánh đổi.
3. Chốt giai đoạn mở rộng, chuyển bên nhận, quan sát, ngừng cũ và thu hẹp.
4. Nếu được phép triển khai, thực hiện giai đoạn nhỏ nhất và thêm kiểm thử hợp đồng.
5. Chạy kiểm tra tương thích và kiểm thử tích hợp liên dịch vụ.
6. Báo lịch ngừng hỗ trợ, quay lui/tiến tiếp và người chịu trách nhiệm của từng bên nhận.

## Tiêu chí hoàn thành

- Không có bên nhận bị bỏ sót.
- Cửa sổ tương thích và điều kiện xóa bản cũ rõ.
- Hợp đồng máy đọc được và tài liệu được đồng bộ.

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
