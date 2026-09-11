---
id: PROF-03
title: Chỉnh sửa hồ sơ
group: Hồ sơ
route: /toi/chinh-sua
priority: P1
status: approved
roles:
- Người dùng
functions:
- ACC-05
- ACC-06
- MED-01
desktop_svg: assets/editable/svg/desktop/prof-03-chinh-sua-ho-so.svg
mobile_svg: assets/editable/svg/mobile/prof-03-chinh-sua-ho-so.svg
review_round: 3
approved_at: '2026-09-07'
---

# PROF-03 - Chỉnh sửa hồ sơ

## Mục tiêu

Cập nhật tên hiển thị, tiểu sử, tên người dùng và avatar đã sẵn sàng.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P1**
- Mã chức năng: `ACC-05`, `ACC-06`, `MED-01`
- Route dự kiến: `/toi/chinh-sua`

## Bố cục

- Form chia nhóm Hồ sơ công khai và Ảnh đại diện.
- Preview avatar cạnh vùng tải lên; tên người dùng có trạng thái kiểm tra.

## Hành động

### Chính

- Lưu hồ sơ

### Phụ

- Đổi ảnh đại diện
- Hủy

## Component

- `SettingsShell`
- `AvatarPicker`
- `TextField`
- `TextArea`
- `Button`
- `ConflictDialog`

## Dữ liệu và hợp đồng liên quan

- PATCH /api/v1/users/me với If-Match
- PATCH /api/v1/users/me/avatar
- Luồng Media upload

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Mặc định
- Tên người dùng đang kiểm tra
- Phương tiện chưa sẵn sàng
- Xung đột phiên bản
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

- Crop ảnh nếu có phải hỗ trợ bàn phím; nếu chưa hỗ trợ thì cho tải ảnh gốc và mô tả giới hạn.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/toi/chinh-sua`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Lưu hồ sơ”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Chỉnh sửa hồ sơ - desktop](../../assets/preview/png/desktop/prof-03-chinh-sua-ho-so.png)

Nguồn SVG: `../../assets/editable/svg/desktop/prof-03-chinh-sua-ho-so.svg`

### Mobile

![Chỉnh sửa hồ sơ - mobile](../../assets/preview/png/mobile/prof-03-chinh-sua-ho-so.png)

Nguồn SVG: `../../assets/editable/svg/mobile/prof-03-chinh-sua-ho-so.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
