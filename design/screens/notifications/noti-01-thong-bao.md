---
id: NOTI-01
title: Thông báo
group: Thông báo
route: /thong-bao
priority: P0
status: approved
roles:
- Người dùng
functions:
- CHT-08
desktop_svg: assets/editable/svg/desktop/noti-01-thong-bao.svg
mobile_svg: assets/editable/svg/mobile/noti-01-thong-bao.svg
review_round: 3
approved_at: '2026-09-07'
---

# NOTI-01 - Thông báo

## Mục tiêu

Hiển thị hộp thông báo theo con trỏ, đánh dấu đã đọc và điều hướng đến đối tượng liên quan.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `CHT-08`
- Route dự kiến: `/thong-bao`

## Bố cục

- Bộ lọc Tất cả/Chưa đọc và danh sách theo ngày.
- Mỗi item có loại, actor, nội dung rút gọn, thời gian và trạng thái đọc.

## Hành động

### Chính

- Mở thông báo

### Phụ

- Đánh dấu tất cả đã đọc
- Lọc chưa đọc

## Component

- `AppShell`
- `FilterChips`
- `NotificationItem`
- `UnreadBadge`
- `EmptyState`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/notifications
- PATCH/POST đánh dấu đọc theo hợp đồng triển khai
- SignalR NotificationCreated

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có thông báo mới
- Rỗng
- Đang tải
- Ngoại tuyến
- Đối tượng đích đã bị xóa

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

- Item chưa đọc không chỉ khác màu; có nhãn 'Chưa đọc' ẩn/hiển thị.
- Không tự di chuyển item đang focus khi có thông báo mới.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/thong-bao`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Mở thông báo”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Thông báo - desktop](../../assets/preview/png/desktop/noti-01-thong-bao.png)

Nguồn SVG: `../../assets/editable/svg/desktop/noti-01-thong-bao.svg`

### Mobile

![Thông báo - mobile](../../assets/preview/png/mobile/noti-01-thong-bao.png)

Nguồn SVG: `../../assets/editable/svg/mobile/noti-01-thong-bao.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
