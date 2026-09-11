---
id: RTC-02
title: Phòng thoại và video
group: RTC
route: /cong-dong/:id/phong/:roomId
priority: P1
status: approved
roles:
- Thành viên
functions:
- RTC-01
- RTC-02
desktop_svg: assets/editable/svg/desktop/rtc-02-phong-thoai-video.svg
mobile_svg: assets/editable/svg/mobile/rtc-02-phong-thoai-video.svg
review_round: 3
approved_at: '2026-09-07'
---

# RTC-02 - Phòng thoại và video

## Mục tiêu

Hiển thị người tham gia, điều khiển micro/camera, chất lượng kết nối và quyền phát biểu.

## Vai trò và ưu tiên

- Vai trò: Thành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `RTC-01`, `RTC-02`
- Route dự kiến: `/cong-dong/:id/phong/:roomId`

## Bố cục

- Lưới người tham gia, vùng chia sẻ chính nếu có, thanh điều khiển dưới.
- Danh sách người tham gia và chất lượng mạng nằm trong drawer trên mobile.

## Hành động

### Chính

- Bật/tắt micro
- Rời phòng

### Phụ

- Bật camera
- Chia sẻ màn hình
- Xem người tham gia

## Component

- `RTCShell`
- `ParticipantGrid`
- `RTCControlBar`
- `ConnectionQuality`
- `ParticipantsDrawer`

## Dữ liệu và hợp đồng liên quan

- POST rtc-token
- LiveKit SDK trực tiếp
- Không gửi media qua API/Kafka

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang kết nối
- Đã kết nối
- Đang dùng TURN
- Mất quyền phát biểu
- LiveKit lỗi

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

- Trạng thái muted/speaking có text/aria-label.
- Nút rời phòng tách xa nút bật micro.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mất kết nối/reconnect không được tạo dữ liệu hoặc phiên trùng.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên, khi mở `/cong-dong/:id/phong/:roomId`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Bật/tắt micro”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Phòng thoại và video - desktop](../../assets/preview/png/desktop/rtc-02-phong-thoai-video.png)

Nguồn SVG: `../../assets/editable/svg/desktop/rtc-02-phong-thoai-video.svg`

### Mobile

![Phòng thoại và video - mobile](../../assets/preview/png/mobile/rtc-02-phong-thoai-video.png)

Nguồn SVG: `../../assets/editable/svg/mobile/rtc-02-phong-thoai-video.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
