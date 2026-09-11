---
id: AUTH-04
title: Quên mật khẩu
group: Xác thực
route: /quen-mat-khau
priority: P1
status: approved
roles:
- Khách
functions:
- ACC-08
desktop_svg: assets/editable/svg/desktop/auth-04-quen-mat-khau.svg
mobile_svg: assets/editable/svg/mobile/auth-04-quen-mat-khau.svg
review_round: 3
approved_at: '2026-09-07'
---

# AUTH-04 - Quên mật khẩu

## Mục tiêu

Yêu cầu mã OTP mà không tiết lộ email có tồn tại trong hệ thống hay không.

## Vai trò và ưu tiên

- Vai trò: Khách
- Mức ưu tiên: **P1**
- Mã chức năng: `ACC-08`
- Route dự kiến: `/quen-mat-khau`

## Bố cục

- Một trường email và giải thích phản hồi chung.
- Sau khi gửi, thay biểu mẫu bằng trạng thái đã ghi nhận và đếm ngược gửi lại.

## Hành động

### Chính

- Gửi mã OTP

### Phụ

- Quay lại đăng nhập

## Component

- `AuthShell`
- `TextField`
- `Button`
- `StatusMessage`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/auth/forgot-password
- Phản hồi UI giống nhau dù email tồn tại hay không.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Đang gửi
- Phản hồi chung
- Giới hạn tần suất
- SMTP chậm nhưng yêu cầu đã được ghi nhận

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

- Thông báo thành công dùng live region mức polite.
- Đếm ngược không cập nhật quá dày cho trình đọc màn hình.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Khách, khi mở `/quen-mat-khau`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Gửi mã OTP”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Quên mật khẩu - desktop](../../assets/preview/png/desktop/auth-04-quen-mat-khau.png)

Nguồn SVG: `../../assets/editable/svg/desktop/auth-04-quen-mat-khau.svg`

### Mobile

![Quên mật khẩu - mobile](../../assets/preview/png/mobile/auth-04-quen-mat-khau.png)

Nguồn SVG: `../../assets/editable/svg/mobile/auth-04-quen-mat-khau.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Toast gửi mã đặt ở góc trên phải, không nằm dưới form.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
