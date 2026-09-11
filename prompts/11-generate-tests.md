---
id: tests
ket_qua_chinh: Bộ kiểm thử xác định bảo vệ hành vi quan sát được
---
# Bổ sung kiểm thử cho hành vi và rủi ro

## Chế độ thực hiện

Được phép thêm hoặc cập nhật mã kiểm thử và dữ liệu cố định kiểm thử. Chỉ sửa mã sản phẩm khi nhiệm vụ ghi rõ và bản sửa cần thiết để thỏa hành vi đã chốt.

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

Thiết kế và triển khai kiểm thử cho `{{DESCRIPTION}}` ở cấp độ phù hợp, tập trung vào hành vi, bất biến và rủi ro thay vì chi tiết triển khai.

## Yêu cầu bắt buộc

- Dùng quy ước, helper và hạ tầng kiểm thử hiện có.
- Bao phủ luồng thành công, ranh giới, dữ liệu đầu vào không hợp lệ, phân quyền, lỗi phụ thuộc và các ca concurrency/idempotency/thử lại liên quan.
- Kiểm thử hồi quy nên thất bại trước bản sửa khi thực tế cho phép.
- Không dùng sleep tùy ý, mạng thật không kiểm soát hoặc mock sâu che mất ranh giới quan trọng.
- Mỗi test phải xác định, cô lập và có tên mô tả hành vi.
- Không giảm độ tin cậy bằng cách bỏ qua test hoặc nới assertion.

## Quy trình

1. Khảo sát test convention, dữ liệu cố định kiểm thử, container và test tương tự.
2. Lập ma trận tiêu chí chấp nhận -> cấp test -> dữ liệu -> assertion.
3. Thêm test nhỏ nhất nhưng đủ phân biệt hành vi đúng/sai.
4. Chạy test mới riêng và xác nhận lỗi đầu ra có ý nghĩa.
5. Chạy bộ kiểm thử liên quan, build và kiểm tra không ổn định trong giới hạn hợp lý.
6. Bàn giao khoảng trống không thể test và lý do.

## Tiêu chí hoàn thành

- Mỗi tiêu chí chấp nhận có ít nhất một bằng chứng phù hợp.
- Test không phụ thuộc thứ tự hoặc thời gian tùy ý.
- Không có test bị tắt hoặc assertion yếu không giải thích.

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
