---
id: MKT-06
title: Đơn hàng
group: Thương mại
route: /cho/don-hang
priority: P2
status: approved
roles:
- Người mua
- Người bán
functions:
- MKT-06
desktop_svg: assets/editable/svg/desktop/mkt-06-don-hang.svg
mobile_svg: assets/editable/svg/mobile/mkt-06-don-hang.svg
review_round: 3
approved_at: '2026-09-07'
---

# MKT-06 - Đơn hàng

## Mục tiêu

Theo dõi danh sách và chi tiết trạng thái đơn hàng theo máy trạng thái được phép.

## Vai trò và ưu tiên

- Vai trò: Người mua, Người bán
- Mức ưu tiên: **P2**
- Mã chức năng: `MKT-06`
- Route dự kiến: `/cho/don-hang`

## Bố cục

- Tabs vai trò mua/bán nếu cần; lọc trạng thái và timeline đơn hàng.
- Chi tiết có lịch sử trạng thái append-only.

## Hành động

### Chính

- Mở đơn hàng

### Phụ

- Lọc trạng thái
- Hủy khi được phép

## Component

- `AppShell`
- `OrderFilter`
- `OrderCard`
- `OrderTimeline`
- `EmptyState`

## Dữ liệu và hợp đồng liên quan

- GET orders/detail theo API triển khai
- POST cancel/state transition khi được phép

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Đang chờ thanh toán
- Đã thanh toán
- Đang xử lý
- Hoàn tất
- Đã hủy

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

- Timeline có thứ tự thời gian rõ và không chỉ dùng biểu tượng.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Người mua, Người bán, khi mở `/cho/don-hang`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Mở đơn hàng”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Đơn hàng - desktop](../../assets/preview/png/desktop/mkt-06-don-hang.png)

Nguồn SVG: `../../assets/editable/svg/desktop/mkt-06-don-hang.svg`

### Mobile

![Đơn hàng - mobile](../../assets/preview/png/mobile/mkt-06-don-hang.png)

Nguồn SVG: `../../assets/editable/svg/mobile/mkt-06-don-hang.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
