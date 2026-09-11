---
id: SYS-01
title: Trạng thái tải, rỗng, lỗi và ngoại tuyến
group: Hệ thống
route: toàn ứng dụng
priority: P0
status: approved
roles:
- Mọi vai trò
functions:
- NFR
- FAILURE
desktop_svg: assets/editable/svg/desktop/sys-01-trang-thai-he-thong.svg
mobile_svg: assets/editable/svg/mobile/sys-01-trang-thai-he-thong.svg
review_round: 3
approved_at: '2026-09-07'
---

# SYS-01 - Trạng thái tải, rỗng, lỗi và ngoại tuyến

## Mục tiêu

Chuẩn hóa skeleton, empty state, lỗi có thể thử lại, lỗi quyền, ngoại tuyến và reconnect.

## Vai trò và ưu tiên

- Vai trò: Mọi vai trò
- Mức ưu tiên: **P0**
- Mã chức năng: `NFR`, `FAILURE`
- Route dự kiến: `toàn ứng dụng`

## Bố cục

- Bộ mẫu dùng chung cho skeleton, rỗng, lỗi, cấm, không tìm thấy, ngoại tuyến và rate limit.
- Mỗi trạng thái có tiêu đề, mô tả, CTA chính/phụ và vùng chi tiết kỹ thuật có thể thu gọn.

## Hành động

### Chính

- Thử lại
- Quay lại

### Phụ

- Xem chi tiết hỗ trợ

## Component

- `StateBoard`
- `Skeleton`
- `EmptyState`
- `ErrorState`
- `OfflineBanner`
- `RateLimitState`

## Dữ liệu và hợp đồng liên quan

- Problem Details
- Retry-After
- traceId để hỗ trợ nhưng không hiển thị mặc định quá nổi bật.

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Loading
- Empty
- Error
- Forbidden
- Not found
- Offline
- Reconnecting
- Rate limited
- Service unavailable

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

- Lỗi form dùng role=alert hợp lý; lỗi trang dùng heading và focus.
- Skeleton ẩn khỏi accessibility tree hoặc có label tải.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Giữ microcopy và trạng thái đồng nhất với các màn hình cùng miền.

## Tiêu chí chấp nhận UI

- Với vai trò Mọi vai trò, khi mở `toàn ứng dụng`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Thử lại”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Trạng thái tải, rỗng, lỗi và ngoại tuyến - desktop](../../assets/preview/png/desktop/sys-01-trang-thai-he-thong.png)

Nguồn SVG: `../../assets/editable/svg/desktop/sys-01-trang-thai-he-thong.svg`

### Mobile

![Trạng thái tải, rỗng, lỗi và ngoại tuyến - mobile](../../assets/preview/png/mobile/sys-01-trang-thai-he-thong.png)

Nguồn SVG: `../../assets/editable/svg/mobile/sys-01-trang-thai-he-thong.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
