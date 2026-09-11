---
id: database
ket_qua_chinh: Bất biến miền được bảo vệ bằng mã và lược đồ tương thích
---
# Thay đổi mô hình miền và cơ sở dữ liệu

## Chế độ thực hiện

Được phép chỉnh Domain, mô hình EF Core, di trú dữ liệu và kiểm thử trong phạm vi. Không chạy migration trên môi trường vận hành hoặc xóa dữ liệu thật.

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

Thiết kế và triển khai thay đổi dữ liệu cho `{{FUNCTION_ID}}`, bảo vệ bất biến bằng aggregate, giao dịch, ràng buộc, chỉ mục và chiến lược xử lý đồng thời phù hợp.

## Yêu cầu bắt buộc

- Chỉ dịch vụ sở hữu được đổi dữ liệu nguồn; không khóa ngoại hoặc truy vấn xuyên dịch vụ.
- Đánh giá dữ liệu cũ, null, trùng, kích thước, tải đọc/ghi và thời gian khóa.
- Dùng trình tự mở rộng -> lấp dữ liệu -> chuyển đọc/ghi -> thu hẹp khi cần tương thích.
- Không giữ transaction hoặc khóa DB trong khi gọi mạng ngoài.
- Chỉ mục phải gắn với mẫu truy cập và kế hoạch đo.
- Migration phải chạy được từ DB rỗng và từ phiên bản trước; có cách tiến tiếp hoặc quay lui.

## Quy trình

1. Khảo sát aggregate, DbContext, ánh xạ, migration, truy vấn và dữ liệu giả định.
2. Đề xuất thay đổi lược đồ, bất biến, xử lý đồng thời và tính tương thích trước khi chỉnh.
3. Thực hiện thay đổi nhỏ nhất, thêm kiểm tra dữ liệu, ràng buộc và chỉ mục cần thiết.
4. Thêm kiểm thử migration, giao dịch, ràng buộc duy nhất/phiên bản và tranh chấp khi liên quan.
5. Chạy migration trên môi trường thử nghiệm, biên dịch, kiểm thử mục tiêu và tích hợp.
6. Ghi rõ rủi ro khóa, lấp dữ liệu, triển khai, quay lui/tiến tiếp và quan sát sau phát hành.

## Tiêu chí hoàn thành

- Bất biến được bảo vệ cả ở tầng phù hợp và cơ sở dữ liệu khi cần.
- Di trú dữ liệu có bằng chứng trên hai đường nâng cấp.
- Không có truy cập hoặc ràng buộc xuyên dịch vụ.

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
