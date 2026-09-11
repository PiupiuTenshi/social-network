---
id: COMM-07
title: Kênh văn bản
group: Cộng đồng
route: /cong-dong/:id/kenh/:channelId
priority: P1
status: approved
roles:
- Thành viên
functions:
- COM-04
- CHT-02
- CHT-07
desktop_svg: assets/editable/svg/desktop/comm-07-kenh-van-ban.svg
mobile_svg: assets/editable/svg/mobile/comm-07-kenh-van-ban.svg
review_round: 3
approved_at: '2026-09-07'
---

# COMM-07 - Kênh văn bản

## Mục tiêu

Trò chuyện theo kênh, xem lịch sử bằng con trỏ và nhận cập nhật thời gian thực.

## Vai trò và ưu tiên

- Vai trò: Thành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `COM-04`, `CHT-02`, `CHT-07`
- Route dự kiến: `/cong-dong/:id/kenh/:channelId`

## Bố cục

- Sidebar kênh, nội dung tin nhắn, danh sách thành viên tùy rộng.
- Mobile dùng drawer kênh và member; composer cố định dưới.

## Hành động

### Chính

- Gửi tin nhắn

### Phụ

- Trả lời
- Tương tác
- Đánh dấu đã đọc

## Component

- `CommunityShell`
- `ChannelList`
- `MessageLog`
- `MessageComposer`
- `MemberList`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/conversations/{id}/messages
- SignalR SendMessage/MessageCreated/MarkRead/Typing

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang kết nối
- Đã kết nối
- Mất kết nối
- Không có quyền
- Kênh đang đồng bộ

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

- Vùng tin nhắn là log với aria-live phù hợp, không đọc tràn.
- Phím tắt gửi không phá nhập multiline.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mất kết nối/reconnect không được tạo dữ liệu hoặc phiên trùng.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên, khi mở `/cong-dong/:id/kenh/:channelId`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Gửi tin nhắn”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Kênh văn bản - desktop](../../assets/preview/png/desktop/comm-07-kenh-van-ban.png)

Nguồn SVG: `../../assets/editable/svg/desktop/comm-07-kenh-van-ban.svg`

### Mobile

![Kênh văn bản - mobile](../../assets/preview/png/mobile/comm-07-kenh-van-ban.png)

Nguồn SVG: `../../assets/editable/svg/mobile/comm-07-kenh-van-ban.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
