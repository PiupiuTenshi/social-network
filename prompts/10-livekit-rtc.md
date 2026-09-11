---
id: livekit
ket_qua_chinh: Token RTC giới hạn quyền và luồng media không làm hỏng ứng dụng cốt lõi
---
# Triển khai luồng RTC bằng LiveKit

## Chế độ thực hiện

Được phép chỉnh điểm cuối cấp token, chính sách, siêu dữ liệu vòng đời và tích hợp phía máy khách. Không thay đổi hạ tầng công khai/môi trường vận hành hoặc cấp token rộng hơn yêu cầu.

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

Triển khai luồng LiveKit cho `{{FUNCTION_ID}}`, từ kiểm tra thành viên/quyền đến token ngắn hạn, kết nối trực tiếp máy khách-SFU, trạng thái lỗi và quan sát.

## Yêu cầu bắt buộc

- Community Service kiểm tra membership cùng `JoinVoice`, `Speak`, `ScreenShare` theo chức năng.
- Danh tính người tham gia lấy từ claim; phòng và quyền được cấp do máy chủ quyết định.
- Token có TTL ngắn và chỉ quyền cần thiết; không log token.
- Client kết nối trực tiếp LiveKit; coturn chỉ là phương án dự phòng mạng.
- LiveKit không sẵn sàng phải trả lỗi rõ nhưng không làm hỏng text chat.
- Không thêm recording, captions, HA hoặc public broadcast ngoài phạm vi.

## Quy trình

1. Đọc mô hình quyền, điểm cuối token, cấu hình LiveKit/coturn và luồng máy khách.
2. Lập ma trận tác nhân, phòng, quyền được cấp, TTL, lỗi và hành vi thu hồi/hết hạn.
3. Triển khai luồng cấp token nhỏ nhất và siêu dữ liệu vòng đời cần thiết.
4. Thêm kiểm thử non-member, thiếu quyền, token hết hạn, dịch vụ không sẵn sàng và phạm vi token.
5. Chạy kiểm thử mục tiêu, integration với mô phỏng hoặc môi trường kiểm thử và build.
6. Rà soát secret, giả mạo claim, chèn định danh phòng trái phép và sự độc lập của text chat.

## Tiêu chí hoàn thành

- Token không cấp quyền vượt quá chính sách.
- Đường lỗi RTC không ảnh hưởng dữ liệu chat.
- Không có media bytes trong API, SignalR hoặc Kafka.

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
