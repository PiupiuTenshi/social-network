---
id: AUTH-03
title: Đăng ký
group: Xác thực
route: /dang-ky
priority: P0
status: approved
roles:
- Khách
functions:
- ACC-01
- ACC-10
desktop_svg: assets/editable/svg/desktop/auth-03-dang-ky.svg
mobile_svg: assets/editable/svg/mobile/auth-03-dang-ky.svg
review_round: 3
approved_at: '2026-09-07'
---

# AUTH-03 - Đăng ký

## Mục tiêu

Tạo tài khoản mới với email, tên người dùng và mật khẩu; cho phép chọn Google OAuth.

## Vai trò và ưu tiên

- Vai trò: Khách
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-01`, `ACC-10`
- Route dự kiến: `/dang-ky`

## Bố cục

- Biểu mẫu theo một cột; gợi ý quy tắc mật khẩu xuất hiện khi focus.
- Trạng thái kiểm tra tên người dùng hiển thị cạnh trường, không chặn nhập.
- Điều khoản là liên kết, không nhồi trong nhãn checkbox.

## Hành động

### Chính

- Tạo tài khoản

### Phụ

- Đăng ký bằng Google
- Chuyển sang đăng nhập

## Component

- `AuthShell`
- `TextField`
- `PasswordField`
- `PasswordCriteriaList`
- `PasswordPolicy`
- `Checkbox`
- `Button`
- `InlineAlert`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/auth/register
- POST /api/v1/auth/google

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Kiểm tra tên người dùng
- Dữ liệu không hợp lệ
- Email hoặc tên đã tồn tại
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

- Mỗi lỗi liên kết với trường bằng aria-describedby.
- Không dùng màu đơn độc để báo tên khả dụng.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Khách, khi mở `/dang-ky`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo tài khoản”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Đăng ký - desktop](../../assets/preview/png/desktop/auth-03-dang-ky.png)

Nguồn SVG: `../../assets/editable/svg/desktop/auth-03-dang-ky.svg`

### Mobile

![Đăng ký - mobile](../../assets/preview/png/mobile/auth-03-dang-ky.png)

Nguồn SVG: `../../assets/editable/svg/mobile/auth-03-dang-ky.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Bổ sung checklist mật khẩu với dấu tích/dấu X cho từng tiêu chí.
- Toast top-end nêu đúng tiêu chí còn thiếu.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
