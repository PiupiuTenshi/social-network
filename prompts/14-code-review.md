---
id: code-review
ket_qua_chinh: Danh sách phát hiện có bằng chứng và mức độ rõ
---
# Rà soát thay đổi theo rủi ro

## Chế độ thực hiện

Chỉ đọc và rà soát. Không chỉnh mã, không tạo commit và không thay đổi tệp.

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

Rà soát `{{DESCRIPTION}}` so với yêu cầu, tiêu chí chấp nhận và quy tắc dự án. Đọc toàn bộ diff, mã xung quanh, nơi gọi, kiểm thử, hợp đồng và migration bị ảnh hưởng.

## Yêu cầu bắt buộc

- Ưu tiên tính đúng đắn, mất dữ liệu, bảo mật, phân quyền, xử lý đồng thời, tính tương thích và hiệu năng.
- Không báo lỗi cách trình bày đã được công cụ định dạng/phân tích tĩnh xử lý trừ khi gây lỗi thật.
- Mỗi phát hiện phải có mức độ, vị trí, kịch bản lỗi, tác động, bằng chứng và hướng sửa ngắn.
- Tách phát hiện đã xác nhận, câu hỏi, khoảng trống kiểm thử và rủi ro chưa xác minh.
- Kiểm tra thay đổi ngoài phạm vi, bí mật, mã gỡ lỗi, TODO và tệp sinh ngoài ý muốn.
- Khi không có phát hiện đáng kể, nói rõ và nêu phần chưa kiểm chứng.

## Quy trình

1. Đọc yêu cầu, hướng dẫn kho mã, trạng thái Git và toàn bộ diff.
2. Truy vết các nơi gọi và hợp đồng/dữ liệu/sự kiện liên quan.
3. Đối chiếu từng tiêu chí chấp nhận với mã và kiểm thử.
4. Đánh giá lỗi theo mức Nghiêm trọng (Critical), Cao (High), Trung bình (Medium), Thấp (Low) với lý do.
5. Chạy hoặc đọc kết quả kiểm chứng chỉ khi được phép; không sửa tệp.
6. Tạo báo cáo ưu tiên theo mức độ và khả năng xảy ra.

## Tiêu chí hoàn thành

- Không có phát hiện mơ hồ thiếu kịch bản lỗi.
- Mọi nhận xét quan trọng có vị trí và bằng chứng.
- Phần không thể xác minh được nêu rõ.

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
