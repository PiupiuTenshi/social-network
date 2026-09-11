---
id: performance
ket_qua_chinh: Nút thắt được chứng minh và cải thiện trên cùng tải thử
---
# Tối ưu dựa trên số liệu

## Chế độ thực hiện

Được phép đo và chỉnh mã trong phạm vi. Không tối ưu dựa trên cảm giác hoặc thay đổi semantics để đạt số đẹp.

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

Đo luồng `{{DESCRIPTION}}`, thiết lập số liệu cơ sở lặp lại được, xác định nút thắt bằng trace, hồ sơ thực thi/kế hoạch truy vấn rồi thực hiện thay đổi nhỏ nhất đạt mục tiêu NFR.

## Yêu cầu bắt buộc

- Ghi tải thử, dữ liệu, môi trường, độ trễ/thông lượng/bộ nhớ/CPU hiện tại và mục tiêu.
- Dùng cùng điều kiện đo trước/sau; nêu độ biến thiên và số lần chạy.
- Kiểm tra N+1, cấp phát bộ nhớ, I/O, truy vấn/chỉ mục, cache và khóa/tranh chấp và công việc không giới hạn.
- Không thêm cache nếu chưa có quy tắc vô hiệu hóa/tính nhất quán.
- Không làm yếu phân quyền, độ bền hoặc tính đúng để tăng tốc.
- Thêm regression guard hoặc benchmark phù hợp.

## Quy trình

1. Tạo kịch bản đo có thể lặp và ghi baseline.
2. Dùng dữ liệu quan sát để chứng minh nút thắt; so sánh ít nhất hai phương án khi cần.
3. Triển khai thay đổi nhỏ nhất và giữ semantics.
4. Chạy kiểm thử tính đúng trước khi đo lại.
5. Đo trước/sau trên cùng tải thử và đối chiếu NFR.
6. Rà soát chi phí bộ nhớ, tính nhất quán, xử lý đồng thời và hành vi khi cache hoặc phụ thuộc lỗi.

## Tiêu chí hoàn thành

- Có số liệu trước/sau cùng phương pháp.
- Mục tiêu đạt hoặc nguyên nhân chưa đạt được chứng minh.
- Tính đúng và bảo mật vẫn có kiểm thử.

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
