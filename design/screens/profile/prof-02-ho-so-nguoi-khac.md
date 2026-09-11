---
id: PROF-02
title: Hồ sơ người dùng
group: Hồ sơ
route: /nguoi-dung/:id
priority: P0
status: approved
roles:
- Người xem
functions:
- ACC-05
- SOC-01
- SOC-02
- SOC-06
desktop_svg: assets/editable/svg/desktop/prof-02-ho-so-nguoi-khac.svg
mobile_svg: assets/editable/svg/mobile/prof-02-ho-so-nguoi-khac.svg
review_round: 3
approved_at: '2026-09-07'
---

# PROF-02 - Hồ sơ người dùng

## Mục tiêu

Xem hồ sơ theo quyền riêng tư, theo dõi hoặc chặn và duyệt bài viết hiển thị được.

## Vai trò và ưu tiên

- Vai trò: Người xem
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-05`, `SOC-01`, `SOC-02`, `SOC-06`
- Route dự kiến: `/nguoi-dung/:id`

## Bố cục

- Giống hồ sơ của tôi nhưng CTA phụ thuộc trạng thái follow/block/privacy.
- Nội dung ẩn dùng một empty state giải thích vừa đủ, không tiết lộ dữ liệu.

## Hành động

### Chính

- Theo dõi hoặc bỏ theo dõi

### Phụ

- Nhắn tin
- Chặn
- Báo cáo

## Component

- `AppShell`
- `ProfileHeader`
- `FollowButton`
- `BlockDialog`
- `Tabs`
- `PostGridOrList`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/users/{id}
- POST/DELETE /api/v1/users/{id}/follow
- POST/DELETE /api/v1/users/{id}/block

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Công khai
- Chỉ người theo dõi
- Đã theo dõi
- Đã chặn
- Hồ sơ không tồn tại

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

- Nút Theo dõi dùng aria-pressed.
- Hộp xác nhận chặn nêu rõ hậu quả.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người xem, khi mở `/nguoi-dung/:id`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Theo dõi hoặc bỏ theo dõi”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Hồ sơ người dùng - desktop](../../assets/preview/png/desktop/prof-02-ho-so-nguoi-khac.png)

Nguồn SVG: `../../assets/editable/svg/desktop/prof-02-ho-so-nguoi-khac.svg`

### Mobile

![Hồ sơ người dùng - mobile](../../assets/preview/png/mobile/prof-02-ho-so-nguoi-khac.png)

Nguồn SVG: `../../assets/editable/svg/mobile/prof-02-ho-so-nguoi-khac.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
