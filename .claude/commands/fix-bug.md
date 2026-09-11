---
id: bug-fix
ket_qua_chinh: Lỗi được tái hiện, sửa đúng nguyên nhân và có kiểm thử hồi quy
---
# Điều tra và sửa nguyên nhân gốc

## Chế độ thực hiện

Được phép chỉnh mã sau khi đã có bằng chứng về nguyên nhân gốc hoặc ranh giới xử lý hợp lệ. Không vá thử theo suy đoán.

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

Điều tra lỗi `{{FUNCTION_ID}}` từ triệu chứng đến trạng thái, dữ liệu, thứ tự thời gian và phụ thuộc; kiểm tra giả thuyết, xác định nguyên nhân gốc rồi triển khai bản sửa nhỏ nhất.

## Yêu cầu bắt buộc

- Tách triệu chứng, vị trí lỗi biểu hiện, nguyên nhân gốc và yếu tố góp phần.
- Tái hiện bằng bước rõ hoặc kiểm thử tối thiểu; nếu chưa tái hiện, thu dữ liệu quan sát có khả năng phân biệt trước khi đổi hành vi.
- Không dùng kiểm tra null, `catch` rộng, thử lại hoặc phương án dự phòng chỉ để giấu triệu chứng.
- Ưu tiên sửa bên tạo dữ liệu hoặc ranh giới bất biến khi hợp đồng không cho phép trạng thái lỗi.
- Thêm kiểm thử hồi quy và ca biên/đồng thời/phân quyền liên quan.
- Không đưa secret hoặc PII vào log chẩn đoán.

## Quy trình

1. Tái hiện triệu chứng hoặc tạo kiểm thử đang thất bại có kiểm soát.
2. Liệt kê ba đến năm giả thuyết và tín hiệu xác nhận/loại trừ.
3. Truy vết luồng gọi, trạng thái, dữ liệu, thứ tự và phụ thuộc để chứng minh nguyên nhân.
4. Triển khai bản sửa nhỏ nhất tại đúng lớp/ràng buộc.
5. Chạy kiểm thử hồi quy, bộ kiểm thử liên quan, phân tích tĩnh/định dạng và biên dịch.
6. Rà soát phạm vi ảnh hưởng, tính tương thích, sửa dữ liệu và giám sát sau phát hành.

## Tiêu chí hoàn thành

- Có bằng chứng phân biệt nguyên nhân gốc với exception site.
- Kiểm thử hồi quy bảo vệ triệu chứng đã quan sát.
- Bản sửa không che lỗi hoặc tạo tác dụng phụ mới.

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
