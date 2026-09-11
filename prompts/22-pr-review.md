---
id: pr-review
ket_qua_chinh: Kết luận hợp nhất dựa trên tiêu chí và bằng chứng
---
# Xác minh pull request trước khi hợp nhất

## Chế độ thực hiện

Chỉ đọc và xác minh. Không sửa mã, không phê duyệt, hợp nhất, commit hoặc push thay người dùng.

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

Xác minh pull request hoặc phần khác biệt `{{DESCRIPTION}}` so với yêu cầu, kế hoạch, tiêu chí chấp nhận, định nghĩa hoàn thành và quy tắc kho mã.

## Yêu cầu bắt buộc

- Xác minh phạm vi thực tế, tệp thay đổi, commit và trạng thái CI.
- Đối chiếu hợp đồng, di trú dữ liệu, lược đồ sự kiện, kiểm thử và tài liệu khi bị ảnh hưởng.
- Kiểm tra secret, mã gỡ lỗi, tệp sinh tự động, TODO và thay đổi không liên quan.
- Không chấp nhận kết quả kiểm thử chỉ được mô tả mà không có log/tệp bằng chứng phù hợp.
- Phân loại lỗi chặn, phát hiện không chặn, câu hỏi và rủi ro còn lại.
- Không đưa nhận xét cách trình bày đã được công cụ tự động xử lý.

## Quy trình

1. Đọc yêu cầu/tiêu chí chấp nhận, hướng dẫn, toàn bộ diff và bằng chứng CI.
2. Ánh xạ từng tiêu chí sang tệp/kiểm thử/bằng chứng.
3. Rà soát tính đúng đắn, phân quyền, toàn vẹn dữ liệu, xử lý đồng thời, tính tương thích và hiệu năng.
4. Kiểm tra Definition of Done và tài liệu đồng bộ.
5. Kết luận sẵn sàng, chưa sẵn sàng hoặc sẵn sàng có điều kiện với lý do.
6. Không thay đổi tệp hoặc trạng thái pull request.

## Tiêu chí hoàn thành

- Mỗi lỗi chặn có vị trí, kịch bản và cách sửa.
- Mọi tiêu chí có trạng thái Đạt/Không đạt/Chưa xác minh.
- Kết luận không vượt quá bằng chứng.

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
