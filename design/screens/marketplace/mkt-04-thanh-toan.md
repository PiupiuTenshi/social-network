---
id: MKT-04
title: Xác nhận đơn hàng
group: Thương mại
route: /cho/thanh-toan
priority: P2
status: approved
roles:
- Người mua
functions:
- MKT-03
- MKT-04
desktop_svg: assets/editable/svg/desktop/mkt-04-thanh-toan.svg
mobile_svg: assets/editable/svg/mobile/mkt-04-thanh-toan.svg
review_round: 3
approved_at: '2026-09-07'
---

# MKT-04 - Xác nhận đơn hàng

## Mục tiêu

Xác nhận mặt hàng, số lượng, giá chụp và giữ tồn kho trước khi thanh toán giả lập.

## Vai trò và ưu tiên

- Vai trò: Người mua
- Mức ưu tiên: **P2**
- Mã chức năng: `MKT-03`, `MKT-04`
- Route dự kiến: `/cho/thanh-toan`

## Bố cục

- Tóm tắt đơn hàng, số lượng, giá chụp và tổng tiền; không thu thông tin thẻ thật.
- Xác nhận tồn kho trước khi tạo đơn.

## Hành động

### Chính

- Tạo đơn hàng

### Phụ

- Quay lại
- Thay đổi số lượng

## Component

- `CheckoutShell`
- `OrderItem`
- `QuantityControl`
- `PriceSummary`
- `InlineAlert`
- `Button`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/orders với Idempotency-Key

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Hợp lệ
- Tồn kho thay đổi
- Hết hàng
- Đơn hàng đã tồn tại do gửi lại

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

- Tổng tiền là heading/summary rõ.
- Thông báo thay đổi giá/tồn kho yêu cầu xác nhận lại.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Người mua, khi mở `/cho/thanh-toan`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo đơn hàng”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Xác nhận đơn hàng - desktop](../../assets/preview/png/desktop/mkt-04-thanh-toan.png)

Nguồn SVG: `../../assets/editable/svg/desktop/mkt-04-thanh-toan.svg`

### Mobile

![Xác nhận đơn hàng - mobile](../../assets/preview/png/mobile/mkt-04-thanh-toan.png)

Nguồn SVG: `../../assets/editable/svg/mobile/mkt-04-thanh-toan.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
