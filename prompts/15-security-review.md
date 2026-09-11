---
id: security-review
ket_qua_chinh: Rủi ro bảo mật được xác minh và xử lý tại ranh giới tin cậy
---
# Rà soát và xử lý rủi ro bảo mật

## Chế độ thực hiện

Mặc định đánh giá trong phạm vi được ủy quyền. Chỉ sửa mã khi yêu cầu bao gồm biện pháp khắc phục; không khai thác hệ thống thật hoặc truy cập dữ liệu trái phép.

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

Đánh giá `{{DESCRIPTION}}` theo tài sản, tác nhân, ranh giới tin cậy và mô hình đe dọa và bằng chứng. Khi được phép, sửa vấn đề tại ranh giới đúng và thêm kiểm thử hồi quy bảo mật.

## Yêu cầu bắt buộc

- Kiểm tra xác thực, phân quyền/BOLA, kiểm tra dữ liệu đầu vào, injection, log chứa secret/PII, SSRF/path traversal, deserialization, CORS/CSRF/XSS khi liên quan.
- Với sự kiện, kiểm tra giả mạo, phát lại, lược đồ và xử lý lặp an toàn; với RAG kiểm tra phạm vi, prompt injection và lộ dữ liệu.
- Xác định điều kiện xảy ra, tác động, khả năng xảy ra và mức độ có lý do.
- Ưu tiên từ chối mặc định và không làm yếu bảo mật để giữ tính tương thích.
- Không đưa payload nhạy cảm vào báo cáo hoặc test dữ liệu cố định kiểm thử.
- Không thay đổi secret, quyền môi trường vận hành hoặc cấu hình mạng khi chưa được cho phép.

## Quy trình

1. Lập mô hình tác nhân, tài sản, điểm vào và ranh giới tin cậy liên quan.
2. Xác minh vấn đề bằng cách an toàn và tối thiểu.
3. Phân loại severity và blast radius dựa trên bằng chứng.
4. Nếu có quyền sửa, triển khai biện pháp khắc phục nhỏ nhất và kiểm thử hồi quy bảo mật.
5. Chạy kiểm thử mục tiêu, quét tĩnh/phụ thuộc/bí mật và biên dịch phù hợp.
6. Báo rủi ro còn lại, triển khai và giám sát, cùng hành động cần quyền riêng.

## Tiêu chí hoàn thành

- Không có kết luận severity thiếu điều kiện và tác động.
- Bản sửa không tạo đường bypass khác.
- Bằng chứng được làm sạch khỏi secret và PII.

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
