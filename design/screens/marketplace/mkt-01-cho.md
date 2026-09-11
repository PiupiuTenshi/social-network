---
id: MKT-01
title: Chợ
group: Thương mại
route: /cho
priority: P2
status: approved
roles:
- Khách theo chính sách
- Người dùng
functions:
- MKT-02
desktop_svg: assets/editable/svg/desktop/mkt-01-cho.svg
mobile_svg: assets/editable/svg/mobile/mkt-01-cho.svg
review_round: 3
approved_at: '2026-09-07'
---

# MKT-01 - Chợ

## Mục tiêu

Duyệt tin đăng bằng bộ lọc và con trỏ, có đường suy giảm khi tìm kiếm nâng cao không khả dụng.

## Vai trò và ưu tiên

- Vai trò: Khách theo chính sách, Người dùng
- Mức ưu tiên: **P2**
- Mã chức năng: `MKT-02`
- Route dự kiến: `/cho`

## Bố cục

- Desktop có sidebar filter và lưới 3 cột; mobile dùng filter bottom sheet và 2 cột.
- Card hiển thị ảnh, tiêu đề, giá, trạng thái hàng và người bán.

## Hành động

### Chính

- Mở tin đăng

### Phụ

- Tìm kiếm
- Lọc
- Tạo tin đăng

## Component

- `AppShell`
- `FilterSidebar`
- `SearchField`
- `ListingCard`
- `PaginationOrCursor`
- `EmptyState`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/listings?cursor=&filter=
- Fallback khi OpenSearch tắt

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có dữ liệu
- Không có kết quả
- Đang tải thêm
- Tìm kiếm nâng cao không khả dụng

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

- Giá đọc đúng đơn vị.
- Ảnh sản phẩm có alt mô tả hoặc alt rỗng nếu chỉ trang trí.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Khách theo chính sách, Người dùng, khi mở `/cho`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Mở tin đăng”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Chợ - desktop](../../assets/preview/png/desktop/mkt-01-cho.png)

Nguồn SVG: `../../assets/editable/svg/desktop/mkt-01-cho.svg`

### Mobile

![Chợ - mobile](../../assets/preview/png/mobile/mkt-01-cho.png)

Nguồn SVG: `../../assets/editable/svg/mobile/mkt-01-cho.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
