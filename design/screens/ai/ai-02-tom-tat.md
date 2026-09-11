---
id: AI-02
title: Tóm tắt hội thoại hoặc kênh
group: AI
route: /tro-ly/tom-tat
priority: P2
status: approved
roles:
- Thành viên có quyền
functions:
- AI-04
desktop_svg: assets/editable/svg/desktop/ai-02-tom-tat.svg
mobile_svg: assets/editable/svg/mobile/ai-02-tom-tat.svg
review_round: 3
approved_at: '2026-09-07'
---

# AI-02 - Tóm tắt hội thoại hoặc kênh

## Mục tiêu

Chọn phạm vi nội dung đã được Trò chuyện cấp quyền và tạo bản tóm tắt có giới hạn.

## Vai trò và ưu tiên

- Vai trò: Thành viên có quyền
- Mức ưu tiên: **P2**
- Mã chức năng: `AI-04`
- Route dự kiến: `/tro-ly/tom-tat`

## Bố cục

- Bộ chọn nguồn/phạm vi, khung kết quả và hành động sao chép.
- Cảnh báo nội dung đã xóa/không còn quyền sẽ bị loại.

## Hành động

### Chính

- Tạo tóm tắt

### Phụ

- Chọn khoảng thời gian
- Sao chép

## Component

- `AppShell`
- `ScopePicker`
- `DateRange`
- `SummaryCard`
- `Button`
- `InlineAlert`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/ai/summaries

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chưa chọn phạm vi
- Đang xử lý
- Hoàn tất
- Nội dung quá lớn
- Mất quyền

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

- Kết quả có cấu trúc heading/list, không chỉ một khối văn bản.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên có quyền, khi mở `/tro-ly/tom-tat`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo tóm tắt”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Tóm tắt hội thoại hoặc kênh - desktop](../../assets/preview/png/desktop/ai-02-tom-tat.png)

Nguồn SVG: `../../assets/editable/svg/desktop/ai-02-tom-tat.svg`

### Mobile

![Tóm tắt hội thoại hoặc kênh - mobile](../../assets/preview/png/mobile/ai-02-tom-tat.png)

Nguồn SVG: `../../assets/editable/svg/mobile/ai-02-tom-tat.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
