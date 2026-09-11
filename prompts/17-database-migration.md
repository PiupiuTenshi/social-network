---
id: migration
ket_qua_chinh: Di trú tương thích, có kiểm chứng và kế hoạch phục hồi
---
# Thiết kế và kiểm chứng di trú cơ sở dữ liệu

## Chế độ thực hiện

Được phép tạo migration, script lấp dữ liệu và kiểm thử trong môi trường phát triển/thử nghiệm. Không chạy trên môi trường vận hành hoặc dữ liệu thật.

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

Thiết kế di trú cho `{{DESCRIPTION}}`, bao gồm trạng thái hiện tại/mục tiêu, cửa sổ tương thích, lấp dữ liệu, truy vấn kiểm chứng, triển khai và quay lui hoặc tiến tiếp.

## Yêu cầu bắt buộc

- Đánh giá dữ liệu null, trùng, legacy, kích thước bảng, lock và thời gian chạy.
- Ưu tiên expand -> lấp dữ liệu -> switch -> contract.
- Ứng dụng cũ và mới phải chạy đồng thời trong cửa sổ đã nêu khi yêu cầu.
- Backfill có batch, checkpoint, idempotency và quan sát.
- Destructive step cần backup đã kiểm chứng và phê duyệt riêng.
- Không để nhiều bản sao dịch vụ chạy migration đồng thời lúc khởi động.

## Quy trình

1. Khảo sát mô hình, lịch sử migration, dữ liệu mẫu và mẫu truy vấn.
2. Lập kế hoạch từng giai đoạn cùng điều kiện vào/ra.
3. Tạo di trú dữ liệu và lấp dữ liệu nhỏ nhất; thêm truy vấn kiểm chứng.
4. Kiểm chứng trên DB rỗng và bản sao phiên bản trước.
5. Chạy kiểm thử ứng dụng với lược đồ cũ/mới theo cửa sổ tương thích.
6. Ghi thời gian, rủi ro khóa, quay lui/tiến tiếp và giám sát.

## Tiêu chí hoàn thành

- Hai đường di trú dữ liệu có bằng chứng thành công.
- Không mất dữ liệu hoặc tạo downtime ngoài kế hoạch.
- Bước phá hủy được tách và không tự động thực thi.

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
