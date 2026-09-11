---
id: FEED-03
title: Chi tiết bài viết
group: Bảng tin
route: /bai-viet/:id
priority: P0
status: approved
roles:
- Người xem
- Người dùng
functions:
- SOC-06
- SOC-07
- SOC-08
- SOC-10
- MOD-01
- AI-05
desktop_svg: assets/editable/svg/desktop/feed-03-chi-tiet-bai-viet.svg
mobile_svg: assets/editable/svg/mobile/feed-03-chi-tiet-bai-viet.svg
review_round: 3
approved_at: '2026-09-07'
---

# FEED-03 - Chi tiết bài viết

## Mục tiêu

Đọc bài viết, xem chuỗi bình luận, trả lời, tương tác, chia sẻ và báo cáo.

## Vai trò và ưu tiên

- Vai trò: Người xem, Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `SOC-06`, `SOC-07`, `SOC-08`, `SOC-10`, `MOD-01`
- Route dự kiến: `/bai-viet/:id`

## Bố cục

- Bài viết ở đầu, danh sách bình luận phân cấp tối đa theo quy tắc hệ thống.
- Composer bình luận cố định gần cuối nội dung.
- Menu hành động thay đổi theo quyền.

## Hành động

### Chính

- Bình luận
- Tương tác

### Phụ

- Chia sẻ
- Sửa hoặc xóa nếu có quyền
- Báo cáo

## Component

- `AppShell`
- `PostCard`
- `CommentThread`
- `CommentComposer`
- `Menu`
- `ReportDialog`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/posts/{id}
- POST /api/v1/posts/{id}/comments
- PUT/DELETE /reaction
- POST /api/v1/posts/{id}/share
- POST /api/v1/reports

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang tải
- Có nội dung
- Bài viết riêng tư
- Đã xóa
- Bị chặn
- Lỗi bình luận

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

- Bình luận lồng có aria-level hợp lý.
- Sau khi gửi bình luận, thông báo và đưa focus tới bình luận mới khi không gây giật.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người xem, Người dùng, khi mở `/bai-viet/:id`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Bình luận”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Chi tiết bài viết - desktop](../../assets/preview/png/desktop/feed-03-chi-tiet-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/desktop/feed-03-chi-tiet-bai-viet.svg`

### Mobile

![Chi tiết bài viết - mobile](../../assets/preview/png/mobile/feed-03-chi-tiet-bai-viet.png)

Nguồn SVG: `../../assets/editable/svg/mobile/feed-03-chi-tiet-bai-viet.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- Đưa action bar xuống dưới video, mở rộng vùng media.
- Tăng chiều rộng cột bình luận và giữ lớp nổi desktop/route toàn màn hình mobile.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
