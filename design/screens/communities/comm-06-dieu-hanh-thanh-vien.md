---
id: COMM-06
title: Điều hành thành viên
group: Cộng đồng
route: /cong-dong/:id/thanh-vien
priority: P1
status: approved
roles:
- Điều hành viên
functions:
- COM-05
desktop_svg: assets/editable/svg/desktop/comm-06-dieu-hanh-thanh-vien.svg
mobile_svg: assets/editable/svg/mobile/comm-06-dieu-hanh-thanh-vien.svg
review_round: 3
approved_at: '2026-09-07'
---

# COMM-06 - Điều hành thành viên

## Mục tiêu

Tìm thành viên, xem vai trò và áp dụng mute, kick hoặc ban theo phân cấp.

## Vai trò và ưu tiên

- Vai trò: Điều hành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `COM-05`
- Route dự kiến: `/cong-dong/:id/thanh-vien`

## Bố cục

- Bảng/list thành viên với lọc vai trò/trạng thái.
- Action drawer chứa mute/kick/ban và lý do bắt buộc.

## Hành động

### Chính

- Áp dụng hành động

### Phụ

- Đổi vai trò
- Xem nhật ký

## Component

- `AdminShell`
- `FilterBar`
- `MemberTable`
- `ModerationDrawer`
- `ConfirmDialog`

## Dữ liệu và hợp đồng liên quan

- GET members
- POST member moderation

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có dữ liệu
- Đang lọc
- Mục tiêu cao hơn không thể thao tác
- Hành động đang chờ

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

- Bảng desktop chuyển thành card mobile nhưng giữ heading và nhãn.
- Hành động nguy hiểm yêu cầu xác nhận.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Điều hành viên, khi mở `/cong-dong/:id/thanh-vien`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Áp dụng hành động”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Điều hành thành viên - desktop](../../assets/preview/png/desktop/comm-06-dieu-hanh-thanh-vien.png)

Nguồn SVG: `../../assets/editable/svg/desktop/comm-06-dieu-hanh-thanh-vien.svg`

### Mobile

![Điều hành thành viên - mobile](../../assets/preview/png/mobile/comm-06-dieu-hanh-thanh-vien.png)

Nguồn SVG: `../../assets/editable/svg/mobile/comm-06-dieu-hanh-thanh-vien.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
