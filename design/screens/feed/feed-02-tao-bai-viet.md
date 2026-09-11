---
id: FEED-02
title: Tạo bài viết
group: Bảng tin
route: /bai-viet/moi
priority: P0
status: approved
roles:
- Người dùng
functions:
- SOC-03
- MED-01
- MED-03
desktop_svg: assets/editable/svg/desktop/feed-02-tao-bai-viet.svg
mobile_svg: assets/editable/svg/mobile/feed-02-tao-bai-viet.svg
review_round: 3
approved_at: '2026-09-07'
---

# FEED-02 - Tạo bài viết

## Mục tiêu

Soạn bài, chọn phạm vi hiển thị, đính kèm phương tiện và gửi yêu cầu lặp an toàn.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `SOC-03`, `MED-01`, `MED-03`
- Route dự kiến: `/bai-viet/moi`

## Bố cục

- Modal 640 px trên desktop; trang toàn màn hình trên mobile.
- Composer, bộ chọn phạm vi, media tray và thanh hành động cố định.
- Hiển thị kích thước/loại tệp và trạng thái từng upload.

## Hành động

### Chính

- Đăng bài

### Phụ

- Thêm ảnh/video
- Chọn quyền riêng tư
- Lưu nháp cục bộ

## Component

- `DialogOrPage`
- `PostComposer`
- `VisibilitySelect`
- `MediaUploadTray`
- `Progress`
- `Button`

## Dữ liệu và hợp đồng liên quan

- POST /api/v1/media/uploads
- PUT URL ký trước
- POST /api/v1/media/uploads/{id}/complete
- POST /api/v1/posts với Idempotency-Key

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Rỗng
- Đang tải phương tiện
- Phương tiện lỗi
- Đang đăng
- Đã đăng
- Yêu cầu trùng

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

- Bẫy focus trong modal và trả focus đúng phần tử mở.
- Tiến trình upload có aria-valuenow và mô tả.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/bai-viet/moi`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Đăng bài”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Tạo bài viết - desktop](../../assets/preview/png/desktop/feed-02-tao-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/desktop/feed-02-tao-bai-viet.svg`

### Mobile

![Tạo bài viết - mobile](../../assets/preview/png/mobile/feed-02-tao-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/mobile/feed-02-tao-bai-viet.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Thiết kế lại thanh rich text theo nhóm Font, Cỡ chữ và Định dạng.
- Trạng thái in đậm hiển thị rõ cả trên toolbar và nội dung mẫu.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
