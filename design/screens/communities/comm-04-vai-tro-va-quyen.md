---
id: COMM-04
title: Vai trò và quyền
group: Cộng đồng
route: /cong-dong/:id/vai-tro
priority: P1
status: approved
roles:
- Chủ sở hữu
- Điều hành viên
functions:
- COM-03
desktop_svg: assets/editable/svg/desktop/comm-04-vai-tro-va-quyen.svg
mobile_svg: assets/editable/svg/mobile/comm-04-vai-tro-va-quyen.svg
review_round: 3
approved_at: '2026-09-07'
---

# COMM-04 - Vai trò và quyền

## Mục tiêu

Tạo vai trò, sắp xếp độ ưu tiên, cấp quyền và gán thành viên mà không cho phép leo quyền.

## Vai trò và ưu tiên

- Vai trò: Chủ sở hữu, Điều hành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `COM-03`
- Route dự kiến: `/cong-dong/:id/vai-tro`

## Bố cục

- Desktop split view: danh sách vai trò trái, chi tiết quyền phải.
- Mobile dùng danh sách rồi trang chi tiết; cảnh báo quyền nhạy cảm.

## Hành động

### Chính

- Tạo hoặc lưu vai trò

### Phụ

- Gán thành viên
- Sao chép vai trò

## Component

- `AdminShell`
- `RoleList`
- `PermissionMatrix`
- `MemberPicker`
- `ConflictDialog`

## Dữ liệu và hợp đồng liên quan

- GET/POST/PATCH roles và member roles theo API triển khai
- If-Match cho tài nguyên có version

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Danh sách vai trò
- Đang chỉnh sửa
- Cố leo quyền bị chặn
- Xung đột phiên bản

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

- Nhóm quyền dùng fieldset/legend.
- Drag sort có phương án phím lên/xuống.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Chủ sở hữu, Điều hành viên, khi mở `/cong-dong/:id/vai-tro`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo hoặc lưu vai trò”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Vai trò và quyền - desktop](../../assets/preview/png/desktop/comm-04-vai-tro-va-quyen.png)

Nguồn SVG: `../../assets/editable/svg/desktop/comm-04-vai-tro-va-quyen.svg`

### Mobile

![Vai trò và quyền - mobile](../../assets/preview/png/mobile/comm-04-vai-tro-va-quyen.png)

Nguồn SVG: `../../assets/editable/svg/mobile/comm-04-vai-tro-va-quyen.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
