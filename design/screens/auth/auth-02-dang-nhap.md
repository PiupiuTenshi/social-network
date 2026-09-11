---
id: AUTH-02
title: Đăng nhập
group: Xác thực
route: /dang-nhap
priority: P0
status: approved
roles:
- Khách
functions:
- ACC-02
- ACC-03
desktop_svg: assets/editable/svg/desktop/auth-02-dang-nhap.svg
mobile_svg: assets/editable/svg/mobile/auth-02-dang-nhap.svg
review_round: 3
approved_at: '2026-09-07'
---

# AUTH-02 - Đăng nhập

## Mục tiêu

Xác thực bằng email và mật khẩu, đồng thời cung cấp lối vào Google OAuth và khôi phục mật khẩu.

## Vai trò và ưu tiên

- Vai trò: Khách
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-02`, `ACC-03`
- Route dự kiến: `/dang-nhap`

## Bố cục

- Thẻ biểu mẫu rộng 420 px, tối đa 100% trừ khoảng đệm mobile.
- Email, mật khẩu, nút chính, phân cách OAuth và liên kết hỗ trợ.
- Thông báo lỗi đặt gần trường và có vùng tổng hợp lỗi.

## Hành động

### Chính

- Đăng nhập

### Phụ

- Đăng nhập bằng Google
- Quên mật khẩu
- Tạo tài khoản

## Component

- `AuthShell`
- `TextField`
- `PasswordField`
- `Button`
- `Divider`
- `InlineAlert`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/auth/login
- POST /api/v1/auth/google
- Không lưu mật khẩu hoặc refresh token trong log/telemetry giao diện.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Đang gửi
- Sai thông tin
- Tạm khóa do quá nhiều lần thử
- Dịch vụ tạm thời không khả dụng

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

- Nhãn trường luôn hiển thị, không chỉ dùng placeholder.
- Nút hiện/ẩn mật khẩu có aria-label thay đổi theo trạng thái.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Khách, khi mở `/dang-nhap`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Đăng nhập”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Đăng nhập - desktop](../../assets/preview/png/desktop/auth-02-dang-nhap.png)

Nguồn SVG: `../../assets/editable/svg/desktop/auth-02-dang-nhap.svg`

### Mobile

![Đăng nhập - mobile](../../assets/preview/png/mobile/auth-02-dang-nhap.png)

Nguồn SVG: `../../assets/editable/svg/mobile/auth-02-dang-nhap.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Toast thành công/thất bại neo ở góc trên phải và không che tiêu đề hoặc trường nhập.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
