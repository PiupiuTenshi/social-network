---
id: PROF-01
title: Hồ sơ của tôi
group: Hồ sơ
route: /toi
priority: P0
status: approved
roles:
- Người dùng
functions:
- ACC-05
- SOC-06
desktop_svg: assets/editable/svg/desktop/prof-01-ho-so-cua-toi.svg
mobile_svg: assets/editable/svg/mobile/prof-01-ho-so-cua-toi.svg
review_round: 3
approved_at: '2026-09-07'
---

# PROF-01 - Hồ sơ của tôi

## Mục tiêu

Hiển thị hồ sơ, số liệu mạng xã hội, bài viết và lối vào chỉnh sửa hoặc thiết lập.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P0**
- Mã chức năng: `ACC-05`, `SOC-06`
- Route dự kiến: `/toi`

## Bố cục

- Header hồ sơ gồm avatar, tên, bio, số liệu và CTA.
- Tabs bài viết/phương tiện; desktop có card thông tin phụ.

## Hành động

### Chính

- Chỉnh sửa hồ sơ
- Tạo bài viết

### Phụ

- Xem người theo dõi
- Mở thiết lập

## Component

- `AppShell`
- `ProfileHeader`
- `Tabs`
- `PostGridOrList`
- `EmptyState`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/users/me
- GET /api/v1/users/{id}/posts

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Đang tải
- Có bài viết
- Chưa có bài viết
- Ảnh đại diện lỗi

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

- Tabs dùng roving tabindex hoặc điều hướng tab chuẩn.
- Số liệu có nhãn đầy đủ, không đọc chuỗi số rời.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/toi`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Chỉnh sửa hồ sơ”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Hồ sơ của tôi - desktop](../../assets/preview/png/desktop/prof-01-ho-so-cua-toi.png)

Nguồn SVG: `../../assets/editable/svg/desktop/prof-01-ho-so-cua-toi.svg`

### Mobile

![Hồ sơ của tôi - mobile](../../assets/preview/png/mobile/prof-01-ho-so-cua-toi.png)

Nguồn SVG: `../../assets/editable/svg/mobile/prof-01-ho-so-cua-toi.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
