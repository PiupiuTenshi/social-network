---
id: incident
ket_qua_chinh: Dòng thời gian, phạm vi ảnh hưởng, giả thuyết và phương án xử lý có kiểm soát
---
# Điều tra sự cố an toàn

## Chế độ thực hiện

Mặc định chỉ đọc. Không thay đổi môi trường vận hành, dữ liệu, cờ chức năng, hạ tầng, secret hoặc quyền truy cập nếu chưa có ủy quyền riêng cho từng hành động.

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

Điều tra sự cố `{{DESCRIPTION}}` an toàn, xác định dòng thời gian, phiên bản, tác động, phạm vi ảnh hưởng và giả thuyết; tách giảm thiểu tức thời, bản sửa bền vững, triển khai và quay lui.

## Yêu cầu bắt buộc

- Ưu tiên log, metric, trace, trạng thái sức khỏe và truy vấn chỉ đọc đã làm sạch.
- Mỗi hành động đề xuất phải nêu tín hiệu mong đợi, rủi ro, quyền cần có và cách quay lui.
- Không thử nghiệm phá hủy hoặc lấy dữ liệu người dùng ngoài phạm vi.
- So sánh môi trường lỗi với môi trường khỏe về phiên bản, cấu hình, phụ thuộc, hình dạng dữ liệu và lưu lượng.
- Giữ chuỗi bằng chứng theo thời gian, correlationId và phiên bản đã triển khai.
- Không coi biện pháp giảm thiểu là bản sửa nguyên nhân gốc.

## Quy trình

1. Xác định dòng thời gian, tác động, người dùng/dịch vụ bị ảnh hưởng và phiên bản.
2. Liệt kê và xếp hạng giả thuyết; chọn dữ liệu quan sát có khả năng phân biệt an toàn.
3. Thu bằng chứng chỉ đọc và cập nhật bảng giả thuyết.
4. Đề xuất biện pháp giảm thiểu riêng với bản sửa bền vững; chờ quyền trước hành động làm thay đổi hệ thống.
5. Xác định kiểm chứng, triển khai, quay lui và giám sát sau sửa.
6. Tạo tóm tắt sau sự cố gồm nguyên nhân gốc, yếu tố góp phần, khoảng trống phát hiện và hành động phòng ngừa.

## Tiêu chí hoàn thành

- Không có hành động thay đổi môi trường vận hành ngầm định.
- Nguyên nhân gốc có bằng chứng và tách khỏi triệu chứng.
- Biện pháp phòng ngừa có người chịu trách nhiệm, mức ưu tiên và cách kiểm chứng.

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
