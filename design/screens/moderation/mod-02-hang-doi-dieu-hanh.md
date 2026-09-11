---
id: MOD-02
title: Hàng đợi điều hành
group: Điều hành
route: /dieu-hanh/bao-cao
priority: P1
status: approved
roles:
- Điều hành viên
- Quản trị viên
functions:
- MOD-02
desktop_svg: assets/editable/svg/desktop/mod-02-hang-doi-dieu-hanh.svg
mobile_svg: assets/editable/svg/mobile/mod-02-hang-doi-dieu-hanh.svg
review_round: 3
approved_at: '2026-09-07'
---

# MOD-02 - Hàng đợi điều hành

## Mục tiêu

Duyệt báo cáo theo ưu tiên, trạng thái, loại nội dung và người được phân công.

## Vai trò và ưu tiên

- Vai trò: Điều hành viên, Quản trị viên
- Mức ưu tiên: **P1**
- Mã chức năng: `MOD-02`
- Route dự kiến: `/dieu-hanh/bao-cao`

## Bố cục

- Bảng desktop với filter bar; card list mobile.
- Cột chính: ưu tiên, loại, lý do, trạng thái, thời gian, người xử lý.

## Hành động

### Chính

- Mở hồ sơ báo cáo

### Phụ

- Lọc
- Nhận xử lý
- Sắp xếp

## Component

- `ModerationShell`
- `FilterBar`
- `ModerationTable`
- `PriorityBadge`
- `PaginationOrCursor`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/moderation/reports

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có dữ liệu
- Rỗng
- Đang lọc
- Không đủ quyền
- Dữ liệu nhạy cảm đã che

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

- Header bảng có scope.
- PII đã che vẫn có nhãn không gây hiểu lầm.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Điều hành viên, Quản trị viên, khi mở `/dieu-hanh/bao-cao`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Mở hồ sơ báo cáo”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Hàng đợi điều hành - desktop](../../assets/preview/png/desktop/mod-02-hang-doi-dieu-hanh.png)

Nguồn SVG: `../../assets/editable/svg/desktop/mod-02-hang-doi-dieu-hanh.svg`

### Mobile

![Hàng đợi điều hành - mobile](../../assets/preview/png/mobile/mod-02-hang-doi-dieu-hanh.png)

Nguồn SVG: `../../assets/editable/svg/mobile/mod-02-hang-doi-dieu-hanh.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
