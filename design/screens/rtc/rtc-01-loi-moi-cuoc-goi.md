---
id: RTC-01
title: Lời mời cuộc gọi
group: RTC
route: /cuoc-goi/:id
priority: P1
status: approved
roles:
- Người dùng
- Thành viên
functions:
- CHT-09
- RTC-01
desktop_svg: assets/editable/svg/desktop/rtc-01-loi-moi-cuoc-goi.svg
mobile_svg: assets/editable/svg/mobile/rtc-01-loi-moi-cuoc-goi.svg
review_round: 3
approved_at: '2026-09-07'
---

# RTC-01 - Lời mời cuộc gọi

## Mục tiêu

Hiển thị lời mời thoại/video với thời gian chờ, kiểm tra quyền và điều hướng đến LiveKit.

## Vai trò và ưu tiên

- Vai trò: Người dùng, Thành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `CHT-09`, `RTC-01`
- Route dự kiến: `/cuoc-goi/:id`

## Bố cục

- Overlay hoặc full-screen mobile với avatar, loại cuộc gọi, thời gian chờ.
- Nút Tham gia/Từ chối lớn và không đặt quá gần.

## Hành động

### Chính

- Tham gia

### Phụ

- Từ chối

## Component

- `CallOverlay`
- `AvatarGroup`
- `Timer`
- `PrimaryButton`
- `SecondaryButton`

## Dữ liệu và hợp đồng liên quan

- SignalR CallInvite/CallStateChanged
- POST /api/v1/channels/{id}/rtc-token khi chấp nhận

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang đổ chuông
- Hết thời gian
- Đã từ chối
- Không có quyền
- LiveKit tạm thời không khả dụng

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

- Âm thanh rung có tùy chọn tắt; nội dung vẫn hiểu được khi không nghe.
- Focus mặc định không nằm trên nút nguy hiểm.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mất kết nối/reconnect không được tạo dữ liệu hoặc phiên trùng.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, Thành viên, khi mở `/cuoc-goi/:id`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tham gia”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Lời mời cuộc gọi - desktop](../../assets/preview/png/desktop/rtc-01-loi-moi-cuoc-goi.png)

Nguồn SVG: `../../assets/editable/svg/desktop/rtc-01-loi-moi-cuoc-goi.svg`

### Mobile

![Lời mời cuộc gọi - mobile](../../assets/preview/png/mobile/rtc-01-loi-moi-cuoc-goi.png)

Nguồn SVG: `../../assets/editable/svg/mobile/rtc-01-loi-moi-cuoc-goi.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
