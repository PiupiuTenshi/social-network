---
id: AUTH-05
title: Đặt lại mật khẩu
group: Xác thực
route: /dat-lai-mat-khau
priority: P1
status: approved
roles:
- Khách
functions:
- ACC-09
desktop_svg: assets/editable/svg/desktop/auth-05-dat-lai-mat-khau.svg
mobile_svg: assets/editable/svg/mobile/auth-05-dat-lai-mat-khau.svg
review_round: 3
approved_at: '2026-09-07'
---

# AUTH-05 - Đặt lại mật khẩu

## Mục tiêu

Xác minh OTP một lần và đặt mật khẩu mới; mọi phiên đang hoạt động sẽ bị thu hồi.

## Vai trò và ưu tiên

- Vai trò: Khách
- Mức ưu tiên: **P1**
- Mã chức năng: `ACC-09`
- Route dự kiến: `/dat-lai-mat-khau`

## Bố cục

- Trạng thái đầu tiên sau khi OTP hợp lệ là modal xác nhận giữa màn hình.
- Khi chọn **OK, nhập mật khẩu mới**, modal đóng, focus chuyển vào trường mật khẩu mới và OTP không còn hiển thị.
- Sau thành công, điều hướng về đăng nhập và thông báo mọi phiên đã bị thu hồi.

## Hành động

### Chính

- Đặt lại mật khẩu

### Phụ

- Gửi lại mã
- Quay lại đăng nhập

## Component

- `AuthShell`
- `VerificationSuccessModal`
- `PasswordField`
- `PasswordCriteriaList`
- `Button`
- `InlineAlert`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/auth/reset-password

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Nhập OTP
- OTP sai
- OTP hết hạn
- Quá số lần thử
- Thành công

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

- OTP vẫn có một nhãn logic; hỗ trợ nhập/dán bằng bàn phím.
- Không tự động gửi ngay khi nhập đủ nếu có nguy cơ thao tác nhầm.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Khách, khi mở `/dat-lai-mat-khau`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Đặt lại mật khẩu”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Đặt lại mật khẩu - desktop](../../assets/preview/png/desktop/auth-05-dat-lai-mat-khau.png)

Nguồn SVG: `../../assets/editable/svg/desktop/auth-05-dat-lai-mat-khau.svg`

### Mobile

![Đặt lại mật khẩu - mobile](../../assets/preview/png/mobile/auth-05-dat-lai-mat-khau.png)

Nguồn SVG: `../../assets/editable/svg/mobile/auth-05-dat-lai-mat-khau.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Sau khi OTP hợp lệ, hiển thị modal giữa màn hình.
- Chỉ sau khi chọn OK mới mở form mật khẩu mới; OTP không còn xuất hiện.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
