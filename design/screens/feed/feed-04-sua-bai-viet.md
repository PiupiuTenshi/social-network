---
id: FEED-04
title: Sửa bài viết
group: Bảng tin
route: /bai-viet/:id/sua
priority: P0
status: approved
roles:
- Chủ sở hữu
functions:
- SOC-04
desktop_svg: assets/editable/svg/desktop/feed-04-sua-bai-viet.svg
mobile_svg: assets/editable/svg/mobile/feed-04-sua-bai-viet.svg
review_round: 3
approved_at: '2026-09-07'
---

# FEED-04 - Sửa bài viết

## Mục tiêu

Cập nhật nội dung hoặc phạm vi hiển thị bằng If-Match để tránh ghi đè dữ liệu mới.

## Vai trò và ưu tiên

- Vai trò: Chủ sở hữu
- Mức ưu tiên: **P0**
- Mã chức năng: `SOC-04`
- Route dự kiến: `/bai-viet/:id/sua`

## Bố cục

- Dùng cùng composer với tạo bài nhưng có trạng thái phiên bản.
- Cảnh báo thay đổi chưa lưu khi rời màn hình.

## Hành động

### Chính

- Lưu thay đổi

### Phụ

- Hủy
- Xem phiên bản hiện tại

## Component

- `DialogOrPage`
- `PostComposer`
- `ConflictDialog`
- `Button`

## Dữ liệu và hợp đồng liên quan

- PATCH /api/v1/posts/{id} với If-Match
- GET lại tài nguyên khi 412 để hỗ trợ so sánh.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Mặc định
- Đang lưu
- Xung đột phiên bản 412
- Không có quyền
- Bài viết đã xóa

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

- Hộp thoại xung đột mô tả rõ lựa chọn tải bản mới hoặc sao chép nội dung đang sửa.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Chủ sở hữu, khi mở `/bai-viet/:id/sua`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Lưu thay đổi”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Sửa bài viết - desktop](../../assets/preview/png/desktop/feed-04-sua-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/desktop/feed-04-sua-bai-viet.svg`

### Mobile

![Sửa bài viết - mobile](../../assets/preview/png/mobile/feed-04-sua-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/mobile/feed-04-sua-bai-viet.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Đồng bộ editor với FEED-02; nội dung sửa đổi có typography đậm và dễ nhận biết.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
