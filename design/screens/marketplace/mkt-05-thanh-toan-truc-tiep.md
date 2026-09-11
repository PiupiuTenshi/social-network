---
id: MKT-05
title: Thanh toán trực tiếp với người bán
group: Thương mại
route: /cho/don/:id/thanh-toan
priority: P2
status: approved
roles:
- Người mua
functions:
- MKT-05
desktop_svg: assets/editable/svg/desktop/mkt-05-thanh-toan-truc-tiep.svg
mobile_svg: assets/editable/svg/mobile/mkt-05-thanh-toan-truc-tiep.svg
review_round: 3
approved_at: '2026-09-07'
---

# MKT-05 - Thanh toán trực tiếp với người bán

## Mục tiêu

Thực hiện thanh toán giả lập lặp an toàn và hiển thị kết quả mà không gửi trùng.

## Vai trò và ưu tiên

- Vai trò: Người mua
- Mức ưu tiên: **P2**
- Mã chức năng: `MKT-05`
- Route dự kiến: `/cho/don/:id/thanh-toan`

## Bố cục

- Màn hình thanh toán giả lập nêu rõ là mô phỏng; trạng thái xử lý không cho gửi nút lần hai.
- Kết quả có mã tham chiếu và CTA đến đơn hàng.

## Hành động

### Chính

- Thanh toán

### Phụ

- Thử lại an toàn
- Hủy đơn

## Component

- `CheckoutShell`
- `PaymentSimulationCard`
- `Progress`
- `ResultState`
- `Button`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/orders/{id}/pay với Idempotency-Key

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chờ thanh toán
- Đang xử lý
- Thành công
- Thất bại
- Kết quả cũ được trả lại

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

- Spinner đi kèm text.
- Thành công/thất bại dùng heading và live region.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.
- Hành động có hậu quả lớn không dùng cập nhật lạc quan và phải có xác nhận rõ.

## Tiêu chí chấp nhận UI

- Với vai trò Người mua, khi mở `/cho/don/:id/thanh-toan`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Thanh toán”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Thanh toán trực tiếp với người bán - desktop](../../assets/preview/png/desktop/mkt-05-thanh-toan-truc-tiep.png)

Nguồn SVG: `../../assets/editable/svg/desktop/mkt-05-thanh-toan-truc-tiep.svg`

### Mobile

![Thanh toán trực tiếp với người bán - mobile](../../assets/preview/png/mobile/mkt-05-thanh-toan-truc-tiep.png)

Nguồn SVG: `../../assets/editable/svg/mobile/mkt-05-thanh-toan-truc-tiep.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
