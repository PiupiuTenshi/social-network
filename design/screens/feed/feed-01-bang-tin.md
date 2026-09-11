---
id: FEED-01
title: Bảng tin
group: Bảng tin
route: /bang-tin
priority: P0
status: approved
roles:
- Người dùng
functions:
- FED-02
- SOC-03
- SOC-08
- CHT-08
desktop_svg: assets/editable/svg/desktop/feed-01-bang-tin.svg
mobile_svg: assets/editable/svg/mobile/feed-01-bang-tin.svg
review_round: 3
approved_at: '2026-09-07'
---

# FEED-01 - Bảng tin

## Mục tiêu

Hiển thị bảng tin theo con trỏ, hỗ trợ tạo bài viết nhanh, tương tác và điều hướng đến chi tiết.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `FED-02`, `SOC-03`, `SOC-08`, `CHT-08`
- Route dự kiến: `/bang-tin`

## Bố cục

- Desktop ba vùng: điều hướng 240 px, nội dung 680-760 px, thanh phụ 300-340 px.
- Mobile dùng thanh trên và điều hướng đáy; nội dung toàn chiều rộng.
- Mỗi PostCard là một vùng độc lập với header, nội dung, media và action row.

## Hành động

### Chính

- Tạo bài viết
- Tương tác
- Bình luận

### Phụ

- Lưu vị trí cuộn
- Ẩn gợi ý
- Báo cáo

## Component

- `AppShell`
- `PostComposer`
- `PostCard`
- `PostActionBar`
- `RightRail`
- `Skeleton`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/feed?cursor=&limit=
- POST /api/v1/posts
- PUT/DELETE reaction
- SignalR cho thông báo; không dùng để thay nguồn dữ liệu bảng tin.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang tải khung
- Có dữ liệu
- Hết dữ liệu
- Cache miss
- Ngoại tuyến
- Bài viết bị ẩn theo quyền

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

- Nút tương tác có tên và trạng thái pressed.
- Tải thêm không làm mất focus; có lựa chọn nút 'Xem thêm' khi cần.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/bang-tin`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tạo bài viết”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Bảng tin - desktop](../../assets/preview/png/desktop/feed-01-bang-tin.png)

Nguồn SVG: `../../assets/editable/svg/desktop/feed-01-bang-tin.svg`

### Mobile

![Bảng tin - mobile](../../assets/preview/png/mobile/feed-01-bang-tin.png)

Nguồn SVG: `../../assets/editable/svg/mobile/feed-01-bang-tin.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Đưa Thích, Bình luận và Đăng lại xuống dưới video.
- Mở rộng video hết chiều ngang vùng nội dung; Lưu và Chia sẻ ở cùng action bar.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
