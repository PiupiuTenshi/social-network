---
id: AUTH-01
title: Chào mừng
group: Xác thực
route: /
priority: P0
status: approved
roles:
- Khách
functions:
- ACC-01
- ACC-02
desktop_svg: assets/editable/svg/desktop/auth-01-chao-mung.svg
mobile_svg: assets/editable/svg/mobile/auth-01-chao-mung.svg
review_round: 3
approved_at: '2026-09-07'
---

# AUTH-01 - Chào mừng

## Mục tiêu

Giới thiệu ngắn gọn giá trị sản phẩm và dẫn người dùng đến đăng nhập hoặc đăng ký.

## Vai trò và ưu tiên

- Vai trò: Khách
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-01`, `ACC-02`
- Route dự kiến: `/`

## Bố cục

- Khung hero hai cột trên desktop; một cột trên mobile.
- Bên trái là thông điệp giá trị và CTA; bên phải là minh họa mô-đun sản phẩm.
- Không hiển thị điều hướng ứng dụng khi chưa xác thực.

## Hành động

### Chính

- Đăng ký tài khoản
- Đăng nhập

### Phụ

- Xem chính sách quyền riêng tư

## Component

- `AppLogo`
- `Hero`
- `FeatureCard`
- `PrimaryButton`
- `SecondaryButton`

## Dữ liệu và hợp đồng liên quan

- Không cần dữ liệu cá nhân.
- Có thể đọc trạng thái health công khai tối thiểu để hiển thị bảo trì.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Mặc định
- Mạng chậm
- Bảo trì có kiểm soát

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

- Tiêu đề H1 duy nhất.
- CTA chính xuất hiện trước CTA phụ trong thứ tự bàn phím.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Khách, khi mở `/`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Đăng ký tài khoản”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Chào mừng - desktop](../../assets/preview/png/desktop/auth-01-chao-mung.png)

Nguồn SVG: `../../assets/editable/svg/desktop/auth-01-chao-mung.svg`

### Mobile

![Chào mừng - mobile](../../assets/preview/png/mobile/auth-01-chao-mung.png)

Nguồn SVG: `../../assets/editable/svg/mobile/auth-01-chao-mung.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
