---
id: frontend-feature
ket_qua_chinh: Luồng giao diện hoàn chỉnh theo hợp đồng backend đã xác minh
---
# Triển khai lát cắt giao diện Angular

## Chế độ thực hiện

Được phép chỉnh mã giao diện và kiểm thử trong phạm vi chức năng. Không tự thay đổi API backend để phù hợp với giả định của giao diện.

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

Triển khai trải nghiệm `{{FUNCTION_ID}}` từ route/component đến trạng thái và API client, trạng thái tải/rỗng/lỗi, phân quyền hiển thị, accessibility và kiểm thử.

## Yêu cầu bắt buộc

- Đọc component, state, API client và kiểm thử tương tự trước khi tạo mẫu mới.
- Dùng kiểu dữ liệu sinh từ OpenAPI hoặc hợp đồng đã xác minh; không nhân bản DTO tùy ý.
- Xử lý trạng thái tải, rỗng, lỗi, thử lại, hủy yêu cầu và phản hồi cũ khi liên quan.
- Không coi ẩn nút là phân quyền; backend vẫn là nơi quyết định quyền.
- Không ghi token, PII hoặc payload nhạy cảm vào console/log.
- Giữ accessibility, bố cục đáp ứng và hiệu năng tải theo quy ước hiện có.

## Quy trình

1. Truy vết hợp đồng backend và luồng giao diện hiện tại.
2. Lập kế hoạch trạng thái, component, điều hướng, ánh xạ lỗi và kiểm thử.
3. Triển khai thay đổi nhỏ nhất; tái sử dụng hệ thống thiết kế và pattern sẵn có.
4. Thêm kiểm thử component/service và E2E cho luồng quan trọng khi hạ tầng hỗ trợ.
5. Chạy lint, kiểm tra kiểu, kiểm thử đơn vị và biên dịch bằng lệnh thật của không gian làm việc.
6. Rà soát accessibility, trạng thái lỗi, tranh chấp giữa các yêu cầu và thay đổi ngoài phạm vi.

## Tiêu chí hoàn thành

- Luồng thành công và lỗi hiển thị đúng hợp đồng.
- Không có kiểu `any` hoặc hợp đồng tự đoán trên đường chính.
- Kiểm thử và build được ghi kết quả thật.

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
