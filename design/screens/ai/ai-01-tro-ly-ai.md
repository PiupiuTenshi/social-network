---
id: AI-01
title: Trợ lý AI
group: AI
route: /tro-ly
priority: P2
status: approved
roles:
- Người dùng
functions:
- AI-03
desktop_svg: assets/editable/svg/desktop/ai-01-tro-ly-ai.svg
mobile_svg: assets/editable/svg/mobile/ai-01-tro-ly-ai.svg
review_round: 3
approved_at: '2026-09-07'
---

# AI-01 - Trợ lý AI

## Mục tiêu

Hỏi đáp dựa trên nguồn người dùng được phép truy cập, stream câu trả lời và hiển thị nguồn tham chiếu.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P2**
- Mã chức năng: `AI-03`
- Route dự kiến: `/tro-ly`

## Bố cục

- Lịch sử câu hỏi, vùng trả lời stream, danh sách nguồn và composer.
- CTA dừng sinh luôn hiển thị khi streaming.

## Hành động

### Chính

- Gửi câu hỏi

### Phụ

- Dừng sinh
- Mở nguồn
- Bắt đầu phiên mới

## Component

- `AppShell`
- `AIConversation`
- `AIMessage`
- `CitationCard`
- `AIComposer`
- `StreamingIndicator`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/ai/ask
- SignalR AiToken/AiCompleted hoặc HTTP stream

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Đang truy xuất
- Đang stream
- Đã hoàn tất
- AI không khả dụng
- Bị giới hạn tần suất

Ngoài các trạng thái trên, áp dụng trạng thái dùng chung trong `sources/11-state-matrix.md`.

## Tương tác và phản hồi

- Hành động có request phải có trạng thái `idle -> submitting -> success/error`.
- Double-click hoặc reconnect không được tạo side effect trùng.
- Dữ liệu nhập phải được giữ khi lỗi có thể thử lại.
- Khi route không còn quyền, điều hướng về vị trí an toàn và không tiết lộ nội dung.
- Mọi toast quan trọng phải có bản inline hoặc lịch sử phù hợp khi người dùng cần hành động.

## Responsive

- Desktop dùng frame 1440 x 1024 trong mockup.
- Mobile dùng frame 390 x 844.
- Nội dung và hành động giữ cùng ý nghĩa; không chỉ thu nhỏ tỷ lệ.
- Bảng hoặc split view phải chuyển thành danh sách, drawer hoặc route con trên mobile.
- Touch target tối thiểu 44 x 44 px.

## Accessibility

- Không công bố mỗi token; gom cập nhật theo đoạn.
- Nguồn có tên tài nguyên và trạng thái quyền.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/tro-ly`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Gửi câu hỏi”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Trợ lý AI - desktop](../../assets/preview/png/desktop/ai-01-tro-ly-ai.png)

Nguồn SVG: `../../assets/editable/svg/desktop/ai-01-tro-ly-ai.svg`

### Mobile

![Trợ lý AI - mobile](../../assets/preview/png/mobile/ai-01-tro-ly-ai.png)

Nguồn SVG: `../../assets/editable/svg/mobile/ai-01-tro-ly-ai.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
