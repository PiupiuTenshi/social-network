---
id: FEED-05
title: Bài viết video đang xử lý
group: Bảng tin
route: /bai-viet/:id/xu-ly
priority: P1
status: approved
roles:
- Chủ sở hữu
functions:
- SOC-09
- MED-04
desktop_svg: assets/editable/svg/desktop/feed-05-bai-viet-video.svg
mobile_svg: assets/editable/svg/mobile/feed-05-bai-viet-video.svg
review_round: 3
approved_at: '2026-09-07'
---

# FEED-05 - Bài viết video đang xử lý

## Mục tiêu

Cho chủ sở hữu theo dõi tải lên, xử lý video, ảnh thu nhỏ và trạng thái thất bại trước khi xuất bản.

## Vai trò và ưu tiên

- Vai trò: Chủ sở hữu
- Mức ưu tiên: **P1**
- Mã chức năng: `SOC-09`, `MED-04`
- Route dự kiến: `/bai-viet/:id/xu-ly`

## Bố cục

- Thẻ tiến trình gồm tải lên, xác minh, xử lý, tạo thumbnail và xuất bản.
- Chỉ chủ sở hữu thấy nội dung khi processing/failed.

## Hành động

### Chính

- Xem tiến trình

### Phụ

- Thử lại
- Xóa bản nháp

## Component

- `AppShell`
- `ProcessingTimeline`
- `VideoPreview`
- `InlineAlert`
- `Button`

## Dữ liệu và hợp đồng liên quan

- GET trạng thái MediaAsset/Post
- Nhận MediaReady/Failed qua polling hoặc thông báo ứng dụng theo triển khai.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Tải lên
- Đang xử lý
- Sẵn sàng
- Thất bại
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

- Không chỉ dùng animation; luôn có nhãn trạng thái văn bản.
- Tôn trọng prefers-reduced-motion.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Chủ sở hữu, khi mở `/bai-viet/:id/xu-ly`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Xem tiến trình”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Bài viết video đang xử lý - desktop](../../assets/preview/png/desktop/feed-05-bai-viet-video.png)

Nguồn SVG: `../../assets/editable/svg/desktop/feed-05-bai-viet-video.svg`

### Mobile

![Bài viết video đang xử lý - mobile](../../assets/preview/png/mobile/feed-05-bai-viet-video.png)

Nguồn SVG: `../../assets/editable/svg/mobile/feed-05-bai-viet-video.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Toast xử lý nền đặt top-end.
- Tách trạng thái đang xử lý khỏi hướng dẫn phục hồi khi thất bại để tránh mâu thuẫn.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
