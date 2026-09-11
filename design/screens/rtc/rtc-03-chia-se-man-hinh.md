---
id: RTC-03
title: Chia sẻ màn hình
group: RTC
route: /cong-dong/:id/phong/:roomId/chia-se
priority: P1
status: approved
roles:
- Thành viên có quyền
functions:
- RTC-03
desktop_svg: assets/editable/svg/desktop/rtc-03-chia-se-man-hinh.svg
mobile_svg: assets/editable/svg/mobile/rtc-03-chia-se-man-hinh.svg
review_round: 3
approved_at: '2026-09-07'
---

# RTC-03 - Chia sẻ màn hình

## Mục tiêu

Chọn nguồn màn hình, xem trước và theo dõi trạng thái phát trong phòng.

## Vai trò và ưu tiên

- Vai trò: Thành viên có quyền
- Mức ưu tiên: **P1**
- Mã chức năng: `RTC-03`
- Route dự kiến: `/cong-dong/:id/phong/:roomId/chia-se`

## Bố cục

- Preview nguồn chia sẻ và danh sách cửa sổ/màn hình do trình duyệt cung cấp.
- Khi đang phát, hiển thị chip rõ ràng và nút dừng luôn truy cập được.

## Hành động

### Chính

- Bắt đầu chia sẻ

### Phụ

- Dừng chia sẻ
- Đổi nguồn

## Component

- `RTCShell`
- `SourcePicker`
- `SharePreview`
- `RTCControlBar`
- `StatusChip`

## Dữ liệu và hợp đồng liên quan

- LiveKit publish screen track
- Lifecycle metadata tùy chọn

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chưa chia sẻ
- Đang chọn nguồn
- Đang phát
- Mạng yếu
- Không có quyền

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

- Không phụ thuộc viền màu để biết nguồn đang chọn.
- Tôn trọng quyền hệ điều hành/trình duyệt.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên có quyền, khi mở `/cong-dong/:id/phong/:roomId/chia-se`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Bắt đầu chia sẻ”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Chia sẻ màn hình - desktop](../../assets/preview/png/desktop/rtc-03-chia-se-man-hinh.png)

Nguồn SVG: `../../assets/editable/svg/desktop/rtc-03-chia-se-man-hinh.svg`

### Mobile

![Chia sẻ màn hình - mobile](../../assets/preview/png/mobile/rtc-03-chia-se-man-hinh.png)

Nguồn SVG: `../../assets/editable/svg/mobile/rtc-03-chia-se-man-hinh.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
