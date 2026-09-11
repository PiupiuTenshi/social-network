---
id: service-scaffold
ket_qua_chinh: Khung dịch vụ có thể biên dịch và kiểm thử mà chưa chứa nghiệp vụ giả
---
# Tạo khung dịch vụ theo ranh giới đã khóa

## Chế độ thực hiện

Được phép tạo mã khung trong phạm vi dịch vụ đã được chấp thuận. Không tự tạo dịch vụ mới nếu quyền sở hữu, cơ sở dữ liệu và hợp đồng chưa được khóa.

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

Tạo khung cho dịch vụ `{{DOMAIN}}` theo cấu trúc thực tế của solution, gồm điểm vào, đăng ký dependency injection, cấu hình, kiểm tra sức khỏe, bộ chuyển đổi lưu trữ/tích hợp tối thiểu và project kiểm thử.

## Yêu cầu bắt buộc

- Xác minh dịch vụ sở hữu, thực thể, cơ sở dữ liệu logic, sự kiện phát/nhận và phụ thuộc được phép.
- Tuân theo kiến trúc đã quan sát; không áp đặt MediatR, Repository hoặc thư viện mới.
- Không thêm điểm cuối nghiệp vụ giả hoặc TODO trên đường chạy chính.
- Cấu hình phải dừng khởi động ngay khi thiếu giá trị bắt buộc và không chứa secret.
- Tạo kiểm thử kiến trúc hoặc kiểm thử nhanh tối thiểu để bảo vệ hướng phụ thuộc.

## Quy trình

1. Khảo sát một dịch vụ tương tự và các project dùng chung đang tồn tại.
2. Đề xuất cấu trúc tệp/project và phụ thuộc trước khi tạo.
3. Tạo khung nhỏ nhất, đăng ký thành phần, kiểm tra sức khỏe và cấu hình mẫu.
4. Thêm kiểm thử tối thiểu cho khởi động và ranh giới phụ thuộc.
5. Chạy restore, công cụ định dạng/phân tích tĩnh, biên dịch và test theo lệnh thật của kho mã.
6. Tự rà soát tham chiếu gói, vòng đời DI, secret, log và thay đổi ngoài phạm vi.

## Tiêu chí hoàn thành

- Khung biên dịch và kiểm thử được bằng lệnh đã ghi.
- Không có phụ thuộc hoặc truy cập dữ liệu trái ranh giới.
- Tệp cấu hình mẫu đủ dùng nhưng không chứa bí mật.

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
