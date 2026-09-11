---
id: feature-plan
ket_qua_chinh: Kế hoạch có thứ tự, phụ thuộc và tiêu chí kiểm chứng
---
# Chuyển yêu cầu thành kế hoạch triển khai

## Chế độ thực hiện

Chỉ phân tích và lập kế hoạch. Không chỉnh mã, không tạo migration và không thay đổi hợp đồng.

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

Đối chiếu `{{FUNCTION_ID}}` hoặc yêu cầu với đặc tả, ma trận truy vết, danh mục API/sự kiện/dữ liệu và mã hiện tại. Chia thành các công việc có kết quả độc lập, có thể rà soát và kiểm chứng.

## Yêu cầu bắt buộc

- Mô tả hành vi hiện tại bằng bằng chứng và hành vi mong muốn.
- Xác định dịch vụ sở hữu, dữ liệu, hợp đồng, quyền, xử lý đồng thời, xử lý lặp an toàn, chế độ lỗi và NFR.
- Nêu phần trong phạm vi, ngoài phạm vi, giả định và câu hỏi thực sự chặn thiết kế.
- Không chia máy móc theo controller/service/repository; chia theo kết quả quan sát được.
- Với lỗi phải có bước tái hiện và kiểm tra giả thuyết; với dữ liệu/hợp đồng phải có triển khai và quay lui.

## Quy trình

1. Khảo sát nguồn sự thật và luồng mã hiện tại.
2. Lập bảng dữ kiện, suy luận, giả định, điểm chưa biết và mâu thuẫn.
3. Xác định thứ tự phụ thuộc và phần có thể làm song song.
4. Tạo danh sách công việc nhỏ; mỗi việc có mục tiêu, tệp/ký hiệu, phạm vi, tiêu chí chấp nhận, kiểm chứng và bàn giao.
5. Lập kế hoạch kiểm thử tổng thể, triển khai, quay lui và đồng bộ tài liệu.
6. Chỉ đặt tối đa hai câu hỏi khi câu trả lời có thể đổi kiến trúc, hợp đồng, dữ liệu hoặc bảo mật.

## Tiêu chí hoàn thành

- Mỗi công việc có một kết quả chính và định nghĩa hoàn thành.
- Thứ tự không phụ thuộc vào hợp đồng hoặc lược đồ chưa ổn định.
- Kế hoạch có thể giao cho người khác mà không cần toàn bộ hội thoại.

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
