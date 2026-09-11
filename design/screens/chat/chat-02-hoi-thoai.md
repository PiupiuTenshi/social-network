---
id: CHAT-02
title: Hội thoại
group: Trò chuyện
route: /tin-nhan/:id
priority: P0
status: approved
roles:
- Thành viên hội thoại
functions:
- CHT-02
- CHT-03
- CHT-04
- CHT-05
- CHT-06
- CHT-07
- AI-05
desktop_svg: assets/editable/svg/desktop/chat-02-hoi-thoai.svg
mobile_svg: assets/editable/svg/mobile/chat-02-hoi-thoai.svg
review_round: 3
approved_at: '2026-09-07'
---

# CHAT-02 - Hội thoại

## Mục tiêu

Gửi và nhận tin nhắn an toàn, hỗ trợ trạng thái đang nhập, hiện diện, đã đọc và gửi lại khi mất mạng.

## Vai trò và ưu tiên

- Vai trò: Thành viên hội thoại
- Mức ưu tiên: **P0**
- Mã chức năng: `CHT-02`, `CHT-03`, `CHT-04`, `CHT-05`, `CHT-06`, `CHT-07`
- Route dự kiến: `/tin-nhan/:id`

## Bố cục

- Header hội thoại, log tin nhắn và composer; desktop có panel thông tin tùy chọn.
- Tin nhắn của mình/phía kia khác vị trí nhưng vẫn có nhãn sender.

## Hành động

### Chính

- Gửi tin nhắn

### Phụ

- Gửi phương tiện
- Tương tác
- Sửa/xóa
- Gọi

## Component

- `MessagingShell`
- `MessageLog`
- `MessageBubble`
- `MessageComposer`
- `TypingIndicator`
- `ConnectionBanner`

## Dữ liệu và hợp đồng liên quan

- GET history
- SignalR SendMessage, MessageCreated, MessageUpdated/Deleted, Typing, MarkRead

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang kết nối
- Đã kết nối
- Tin đang gửi
- Gửi thất bại
- Đã đọc
- Đang nhập

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

- Không dùng vị trí trái/phải làm thông tin duy nhất.
- Tin mới không tự lấy focus; có nút nhảy tới tin mới.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mất kết nối/reconnect không được tạo dữ liệu hoặc phiên trùng.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên hội thoại, khi mở `/tin-nhan/:id`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Gửi tin nhắn”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Hội thoại - desktop](../../assets/preview/png/desktop/chat-02-hoi-thoai.png)

Nguồn SVG: `../../assets/editable/svg/desktop/chat-02-hoi-thoai.svg`

### Mobile

![Hội thoại - mobile](../../assets/preview/png/mobile/chat-02-hoi-thoai.png)

Nguồn SVG: `../../assets/editable/svg/mobile/chat-02-hoi-thoai.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
