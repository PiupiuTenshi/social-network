---
id: COMM-05
title: Quản lý kênh
group: Cộng đồng
route: /cong-dong/:id/kenh
priority: P1
status: approved
roles:
- Điều hành viên
functions:
- COM-04
desktop_svg: assets/editable/svg/desktop/comm-05-quan-ly-kenh.svg
mobile_svg: assets/editable/svg/mobile/comm-05-quan-ly-kenh.svg
review_round: 3
approved_at: '2026-09-07'
---

# COMM-05 - Quản lý kênh

## Mục tiêu

Tạo, sắp xếp và cấu hình kênh văn bản hoặc thoại theo quyền.

## Vai trò và ưu tiên

- Vai trò: Điều hành viên
- Mức ưu tiên: **P1**
- Mã chức năng: `COM-04`
- Route dự kiến: `/cong-dong/:id/kenh`

## Bố cục

- Cây kênh có nhóm và khả năng sắp xếp; panel chi tiết loại kênh/quyền.
- Hiển thị badge 'Đang đồng bộ' khi Chat projection chưa sẵn sàng.

## Hành động

### Chính

- Tạo kênh

### Phụ

- Sắp xếp
- Chỉnh quyền kênh

## Component

- `AdminShell`
- `ChannelTree`
- `ChannelForm`
- `PermissionPanel`
- `SyncBadge`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/communities/{id}/channels
- PATCH channel khi API được khóa

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có kênh
- Rỗng
- Projection trò chuyện đang đồng bộ
- Không đủ quyền

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

- Reorder phải có nút bàn phím, không chỉ kéo thả.
- Thông báo kết quả đồng bộ.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Điều hành viên, khi mở `/cong-dong/:id/kenh`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo kênh”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Quản lý kênh - desktop](../../assets/preview/png/desktop/comm-05-quan-ly-kenh.png)

Nguồn SVG: `../../assets/editable/svg/desktop/comm-05-quan-ly-kenh.svg`

### Mobile

![Quản lý kênh - mobile](../../assets/preview/png/mobile/comm-05-quan-ly-kenh.png)

Nguồn SVG: `../../assets/editable/svg/mobile/comm-05-quan-ly-kenh.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
