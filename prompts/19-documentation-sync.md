---
id: docs-sync
ket_qua_chinh: Tài liệu phản ánh đúng hành vi và hợp đồng hiện tại
---
# Đồng bộ tài liệu và hợp đồng

## Chế độ thực hiện

Chỉ chỉnh tài liệu, lược đồ mô tả và ví dụ trong phạm vi. Không sửa mã sản phẩm để ép khớp tài liệu trong cùng nhiệm vụ.

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

Đối chiếu `{{DESCRIPTION}}` với mã, kiểm thử, cấu hình, OpenAPI, lược đồ sự kiện, di trú dữ liệu và ADR; cập nhật tài liệu cần thiết mà không thay đổi ý nghĩa sản phẩm âm thầm.

## Yêu cầu bắt buộc

- Xác minh lệnh, đường dẫn, field, status code và ví dụ với mã/cấu hình hiện tại.
- Không sao chép cùng quy tắc dài vào nhiều tệp; cập nhật nguồn chính và liên kết.
- Ghi `CHƯA XÁC MINH` cho phần không thể kiểm chứng.
- Khi tài liệu và mã mâu thuẫn ảnh hưởng hợp đồng/dữ liệu/bảo mật, dừng và tạo vấn đề/ADR thay vì tự chọn.
- Cập nhật README, OpenAPI, AsyncAPI/lược đồ sự kiện, di trú dữ liệu notes, ADR, runbook, changelog và bản đồ bối cảnh khi liên quan.
- Không đưa secret hoặc dữ liệu cá nhân vào ví dụ.

## Quy trình

1. Xác định danh sách tệp bị ảnh hưởng bằng ma trận đồng bộ.
2. Đối chiếu từng tuyên bố với nguồn kỹ thuật hiện tại.
3. Cập nhật nguồn chính trước, sau đó các mục lục/liên kết phụ.
4. Chạy kiểm tra liên kết, lược đồ và lint tài liệu và ví dụ có thể chạy.
5. Rà soát thuật ngữ, phiên bản, chỗ trống và nội dung lỗi thời.
6. Bàn giao phần đã đồng bộ và sai lệch cần nhiệm vụ riêng.

## Tiêu chí hoàn thành

- Không có ví dụ/lệnh được trình bày như đã xác minh khi chưa chạy.
- Hợp đồng máy đọc được và mô tả con người không mâu thuẫn.
- Liên kết nội bộ hợp lệ.

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
