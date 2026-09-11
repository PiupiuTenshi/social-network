---
id: DISC-01
title: Tìm kiếm
group: Khám phá
route: /tim-kiem
priority: P2
status: approved
roles:
- Người dùng
functions:
- AI-02
- MKT-02
- SOC-06
desktop_svg: assets/editable/svg/desktop/disc-01-tim-kiem.svg
mobile_svg: assets/editable/svg/mobile/disc-01-tim-kiem.svg
review_round: 3
approved_at: '2026-09-07'
---

# DISC-01 - Tìm kiếm

## Mục tiêu

Tìm người dùng, bài viết, cộng đồng và tin đăng; ưu tiên FTS và nâng cấp sang tìm kiếm ngữ nghĩa khi khả dụng.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P2**
- Mã chức năng: `AI-02`, `MKT-02`, `SOC-06`
- Route dự kiến: `/tim-kiem`

## Bố cục

- Ô tìm kiếm nổi bật; tabs Người dùng/Bài viết/Cộng đồng/Tin đăng.
- Kết quả có nhóm và snippet; lọc responsive bằng drawer.

## Hành động

### Chính

- Tìm kiếm

### Phụ

- Lọc loại kết quả
- Sắp xếp

## Component

- `AppShell`
- `SearchField`
- `Tabs`
- `FilterDrawer`
- `SearchResultCard`
- `EmptyState`

## Dữ liệu và hợp đồng liên quan

- GET /api/v1/search/semantic
- Fallback PostgreSQL FTS hoặc endpoint tìm kiếm miền.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Gợi ý ban đầu
- Đang tìm
- Có kết quả
- Không có kết quả
- AI không khả dụng và dùng tìm kiếm thường

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

- Kết quả dùng region có heading.
- Thông báo số kết quả bằng live region sau khi người dùng dừng gõ.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/tim-kiem`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tìm kiếm”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Tìm kiếm - desktop](../../assets/preview/png/desktop/disc-01-tim-kiem.png)

Nguồn SVG: `../../assets/editable/svg/desktop/disc-01-tim-kiem.svg`

### Mobile

![Tìm kiếm - mobile](../../assets/preview/png/mobile/disc-01-tim-kiem.png)

Nguồn SVG: `../../assets/editable/svg/mobile/disc-01-tim-kiem.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
