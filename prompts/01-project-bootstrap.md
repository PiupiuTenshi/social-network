---
id: project-bootstrap
ket_qua_chinh: Bản đồ kho mã và bộ hướng dẫn nền đã được xác minh
---
# Khảo sát và thiết lập nền tảng kho mã

## Chế độ thực hiện

Chỉ khảo sát và tạo hoặc cập nhật tệp nền, cấu hình phát triển và tài liệu điều phối. Không triển khai chức năng sản phẩm trong nhiệm vụ này.

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

Khảo sát kho mã chưa quen thuộc, xác định kiến trúc thực tế, công nghệ, đường chạy, lệnh kiểm chứng và khoảng trống nền tảng. Sau đó tạo hoặc cập nhật cấu trúc hướng dẫn tối thiểu để các nhiệm vụ sau có thể làm việc an toàn.

## Yêu cầu bắt buộc

- Không suy luận kiến trúc chỉ từ tên thư mục; truy vết ít nhất một luồng từ đầu vào đến đầu ra.
- Ghi lại phiên bản công nghệ từ tệp khai báo thực tế; dùng `CHƯA XÁC MINH` khi chưa có bằng chứng.
- Không tạo solution, dịch vụ hoặc phụ thuộc tùy ý khi ranh giới chưa được chấp thuận.
- Không ghi secret thật; chỉ tạo tệp mẫu và tên biến cấu hình.
- Tài liệu mới phải liên kết về nguồn chính thay vì sao chép quy tắc dài ở nhiều nơi.

## Quy trình

1. Đọc hướng dẫn, README, ADR, manifest, quy trình CI, cấu trúc thư mục, kiểm thử và trạng thái Git.
2. Lập bản đồ công nghệ, điểm vào, ranh giới, nguồn sự thật và lệnh có thể chạy.
3. Đối chiếu với Thiết kế v3.0; nêu rõ phần đã có, thiếu hoặc mâu thuẫn.
4. Tạo hoặc cập nhật tệp nền nhỏ nhất cần thiết; không sửa hành vi sản phẩm.
5. Chạy kiểm tra liên kết, cú pháp và tính toàn vẹn của tài liệu/cấu hình mới.
6. Bàn giao bản đồ kho mã, điểm chưa biết và thứ tự nhiệm vụ khởi tạo tiếp theo.

## Tiêu chí hoàn thành

- Bản đồ kho mã có bằng chứng và không chứa phiên bản/lệnh bịa đặt.
- Tệp nền không mâu thuẫn với `AGENTS.md`, `RULES.md` hoặc ADR.
- Có đường kiểm chứng rõ cho nhiệm vụ đầu tiên.

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
