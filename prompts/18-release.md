---
id: release
ket_qua_chinh: Gói phát hành có bằng chứng cổng chất lượng và phương án quay lui
---
# Chuẩn bị và xác minh phát hành

## Chế độ thực hiện

Chỉ chuẩn bị và xác minh. Không triển khai, tạo tag, hợp nhất hoặc thay đổi môi trường vận hành khi chưa được ủy quyền riêng.

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

Đánh giá bản phát hành chứa `{{DESCRIPTION}}` so với P0/P1/P2, cổng G0-G4, tiêu chí chấp nhận, di trú dữ liệu, bảo mật, khả năng quan sát và kế hoạch quay lui.

## Yêu cầu bắt buộc

- Xác minh commit/phần khác biệt và danh sách thay đổi thực tế; không dựa trên mô tả PR riêng lẻ.
- Mọi cổng bắt buộc phải có lệnh hoặc tệp bằng chứng.
- Không tiếp tục khi còn lỗi Nghiêm trọng/Cao, sai lệch hợp đồng, di trú dữ liệu chưa kiểm chứng hoặc khôi phục chưa sẵn sàng.
- Ảnh container, SBOM, quét phụ thuộc/bí mật và cấu hình phải gắn với commit.
- Runbook, kiểm tra sức khỏe, kiểm thử nhanh và kế hoạch quay lui/tiến tiếp phải rõ.
- Phân biệt chuẩn bị phát hành với hành động triển khai.

## Quy trình

1. Lập danh sách commit, tệp phát hành, hợp đồng và di trú dữ liệu và cấu hình thay đổi.
2. Ánh xạ tiêu chí chấp nhận và cổng chất lượng sang bằng chứng.
3. Chạy hoặc xác minh biên dịch, kiểm thử, quét bảo mật, diễn tập di trú dữ liệu và kiểm thử nhanh.
4. Đánh giá tính tương thích, cờ chức năng, thứ tự triển khai và quay lui.
5. Tạo ghi chú phát hành cùng giới hạn đã biết.
6. Kết luận cho phép phát hành, không cho phép phát hành hoặc cho phép có điều kiện; không tự triển khai.

## Tiêu chí hoàn thành

- Không có tiêu chí bắt buộc ở trạng thái mơ hồ nhưng vẫn đánh dấu GO.
- Mọi tệp phát hành truy vết được về commit.
- Có phương án quay lui hoặc tiến tiếp đã kiểm chứng phù hợp.

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
