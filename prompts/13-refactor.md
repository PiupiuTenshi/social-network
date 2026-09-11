---
id: refactor
ket_qua_chinh: Cấu trúc dễ bảo trì hơn với hành vi và hợp đồng được giữ nguyên
---
# Tái cấu trúc mà không đổi hành vi

## Chế độ thực hiện

Được phép chỉnh mã trong ranh giới đã chốt. Không thêm chức năng, đổi hợp đồng công khai, lược đồ, bảo mật hoặc phụ thuộc không cần thiết.

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

Tái cấu trúc `{{DESCRIPTION}}` để giảm coupling, duplication hoặc complexity đã có bằng chứng, đồng thời giữ nguyên hành vi quan sát được.

## Yêu cầu bắt buộc

- Nêu số liệu hoặc ví dụ cụ thể chứng minh vấn đề bảo trì.
- Xác định bất biến, API, sự kiện, dữ liệu và hiệu năng cần giữ.
- Thêm kiểm thử đặc trưng trước khi đổi nếu độ phủ chưa đủ.
- Thực hiện bước nhỏ, dễ rà soát và có thể quay lui.
- Không tạo lớp trừu tượng cho nhu cầu giả định hoặc dùng tái cấu trúc để đổi hành vi.
- Không trộn format diện rộng, package upgrade hoặc cleanup ngoài phạm vi.

## Quy trình

1. Khảo sát nơi sử dụng và đồ thị phụ thuộc và test bảo vệ hiện tại.
2. Chốt hành vi phải giữ và cách chứng minh.
3. Thêm kiểm thử đặc trưng khi cần.
4. Thực hiện thay đổi nhỏ theo từng bước có thể build/test.
5. Chạy kiểm thử mục tiêu, phân tích tĩnh/định dạng, biên dịch và bộ kiểm thử rộng phù hợp.
6. So sánh hợp đồng, SQL, hiệu năng hoặc đầu ra trước/sau khi liên quan.

## Tiêu chí hoàn thành

- Không có thay đổi hành vi ngoài chủ đích.
- Mã mới giảm vấn đề đã nêu và không tăng coupling khác.
- Bằng chứng kiểm chứng trước/sau được ghi.

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
