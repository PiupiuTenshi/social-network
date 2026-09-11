---
id: COMM-01
title: Khám phá cộng đồng
group: Cộng đồng
route: /cong-dong
priority: P1
status: approved
roles:
- Người dùng
functions:
- COM-01
- COM-02
desktop_svg: assets/editable/svg/desktop/comm-01-kham-pha-cong-dong.svg
mobile_svg: assets/editable/svg/mobile/comm-01-kham-pha-cong-dong.svg
review_round: 3
approved_at: '2026-09-07'
---

# COMM-01 - Khám phá cộng đồng

## Mục tiêu

Tìm cộng đồng công khai, xem gợi ý và tạo cộng đồng mới.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P1**
- Mã chức năng: `COM-01`, `COM-02`
- Route dự kiến: `/cong-dong`

## Bố cục

- Hero tìm kiếm nhỏ, lưới community card và danh mục.
- Mobile chuyển lưới thành danh sách.

## Hành động

### Chính

- Tham gia cộng đồng

### Phụ

- Tạo cộng đồng
- Tìm kiếm

## Component

- `AppShell`
- `SearchField`
- `CommunityCard`
- `CategoryChips`
- `CreateCommunityDialog`

## Dữ liệu và hợp đồng liên quan

- GET danh sách cộng đồng theo API triển khai
- POST /api/v1/communities/{id}/join
- POST /api/v1/communities

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Có gợi ý
- Không có kết quả
- Đang tham gia
- Bị cấm tham gia

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

- Card không biến toàn bộ nội dung thành một nút lồng nút.
- CTA Tham gia có trạng thái loading riêng.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/cong-dong`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Tham gia cộng đồng”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Khám phá cộng đồng - desktop](../../assets/preview/png/desktop/comm-01-kham-pha-cong-dong.png)

Nguồn SVG: `../../assets/editable/svg/desktop/comm-01-kham-pha-cong-dong.svg`

### Mobile

![Khám phá cộng đồng - mobile](../../assets/preview/png/mobile/comm-01-kham-pha-cong-dong.png)

Nguồn SVG: `../../assets/editable/svg/mobile/comm-01-kham-pha-cong-dong.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
