---
id: SET-04
title: Xóa tài khoản
group: Thiết lập
route: /thiet-lap/xoa-tai-khoan
priority: P1
status: approved
roles:
- Người dùng
functions:
- ACC-11
desktop_svg: assets/editable/svg/desktop/set-04-xoa-tai-khoan.svg
mobile_svg: assets/editable/svg/mobile/set-04-xoa-tai-khoan.svg
review_round: 3
approved_at: '2026-09-07'
---

# SET-04 - Xóa tài khoản

## Mục tiêu

Giải thích ảnh hưởng, yêu cầu xác thực lại, tạo thời gian ân hạn và hỗ trợ hủy yêu cầu.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P1**
- Mã chức năng: `ACC-11`
- Route dự kiến: `/thiet-lap/xoa-tai-khoan`

## Bố cục

- Vùng nguy hiểm có checklist hậu quả, xác thực lại và thời gian ân hạn.
- Khi đã yêu cầu, thay CTA xóa bằng CTA hủy yêu cầu và mốc thời gian.

## Hành động

### Chính

- Yêu cầu xóa tài khoản

### Phụ

- Hủy yêu cầu xóa
- Tải dữ liệu nếu có

## Component

- `SettingsShell`
- `DangerZone`
- `ReauthDialog`
- `DeletionTimeline`
- `Button`

## Dữ liệu và hợp đồng liên quan

- DELETE /api/v1/users/me
- POST endpoint hủy theo hợp đồng triển khai
- Hiển thị trạng thái AccountDeletionRequest

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chưa yêu cầu
- Xác thực lại
- Đang trong thời gian ân hạn
- Đang đối soát xóa
- Đã hoàn tất

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

- Không dùng dark pattern; CTA phá hủy không là lựa chọn mặc định.
- Yêu cầu nhập xác nhận chỉ khi thật sự cần và có label.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Hành động có hậu quả lớn không dùng cập nhật lạc quan và phải có xác nhận rõ.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/thiet-lap/xoa-tai-khoan`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Yêu cầu xóa tài khoản”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Xóa tài khoản - desktop](../../assets/preview/png/desktop/set-04-xoa-tai-khoan.png)

Nguồn SVG: `../../assets/editable/svg/desktop/set-04-xoa-tai-khoan.svg`

### Mobile

![Xóa tài khoản - mobile](../../assets/preview/png/mobile/set-04-xoa-tai-khoan.png)

Nguồn SVG: `../../assets/editable/svg/mobile/set-04-xoa-tai-khoan.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
