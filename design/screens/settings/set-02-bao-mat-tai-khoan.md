---
id: SET-02
title: Bảo mật tài khoản
group: Thiết lập
route: /thiet-lap/bao-mat
priority: P0
status: approved
roles:
- Người dùng
functions:
- ACC-03
- ACC-04
- ACC-09
desktop_svg: assets/editable/svg/desktop/set-02-bao-mat-tai-khoan.svg
mobile_svg: assets/editable/svg/mobile/set-02-bao-mat-tai-khoan.svg
review_round: 3
approved_at: '2026-09-07'
---

# SET-02 - Bảo mật tài khoản

## Mục tiêu

Đổi mật khẩu, đăng xuất phiên hiện tại hoặc mọi phiên và xem thông tin bảo mật cơ bản.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-03`, `ACC-04`, `ACC-09`
- Route dự kiến: `/thiet-lap/bao-mat`

## Bố cục

- Nhóm đổi mật khẩu, phiên hiện tại và đăng xuất mọi phiên.
- Hành động phá hủy dùng vùng nguy hiểm tách biệt.

## Hành động

### Chính

- Đổi mật khẩu
- Đăng xuất mọi phiên

### Phụ

- Đăng xuất phiên hiện tại

## Component

- `SettingsShell`
- `PasswordForm`
- `SessionCard`
- `DangerZone`
- `ConfirmDialog`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/auth/logout
- Luồng đổi/reset mật khẩu theo hợp đồng được triển khai.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Mặc định
- Đang xử lý
- Xác thực lại
- Thành công
- Thất bại

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

- Yêu cầu xác thực lại được mô tả trước khi mở dialog.
- Thông báo thành công không tự biến mất quá nhanh.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/thiet-lap/bao-mat`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Đổi mật khẩu”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Bảo mật tài khoản - desktop](../../assets/preview/png/desktop/set-02-bao-mat-tai-khoan.png)

Nguồn SVG: `../../assets/editable/svg/desktop/set-02-bao-mat-tai-khoan.svg`

### Mobile

![Bảo mật tài khoản - mobile](../../assets/preview/png/mobile/set-02-bao-mat-tai-khoan.png)

Nguồn SVG: `../../assets/editable/svg/mobile/set-02-bao-mat-tai-khoan.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
