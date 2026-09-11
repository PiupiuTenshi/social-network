---
id: MEDIA-01
title: Tải phương tiện
group: Phương tiện
route: /phuong-tien/tai-len
priority: P1
status: approved
roles:
- Người dùng
functions:
- MED-01
- MED-02
- MED-03
- MED-04
desktop_svg: assets/editable/svg/desktop/media-01-tai-phuong-tien.svg
mobile_svg: assets/editable/svg/mobile/media-01-tai-phuong-tien.svg
review_round: 3
approved_at: '2026-09-07'
---

# MEDIA-01 - Tải phương tiện

## Mục tiêu

Tải trực tiếp qua URL ký trước, hiển thị tiến độ và xác minh trước khi tham chiếu.

## Vai trò và ưu tiên

- Vai trò: Người dùng
- Mức ưu tiên: **P1**
- Mã chức năng: `MED-01`, `MED-02`, `MED-03`, `MED-04`
- Route dự kiến: `/phuong-tien/tai-len`

## Bố cục

- Dropzone, danh sách file, tiến trình từng bước và CTA gắn vào mục đích sử dụng.
- Không tự coi upload thành công chỉ từ phía client.

## Hành động

### Chính

- Chọn tệp
- Tải lên

### Phụ

- Hủy
- Thử lại

## Component

- `UploadShell`
- `Dropzone`
- `UploadItem`
- `Progress`
- `InlineAlert`
- `Button`

## Dữ liệu và hợp đồng liên quan

- POST upload session
- PUT presigned URL
- POST complete
- GET/poll processing state

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chờ chọn
- Đang tải
- Đang xác minh
- Đang xử lý
- Sẵn sàng
- Thất bại

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

- Dropzone có input file tiêu chuẩn.
- Lỗi theo từng file được đọc và không làm mất các file khác.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.

## Tiêu chí chấp nhận UI

- Với vai trò Người dùng, khi mở `/phuong-tien/tai-len`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Chọn tệp”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Hình chỉnh sửa

### Desktop

![Tải phương tiện - desktop](../../assets/preview/png/desktop/media-01-tai-phuong-tien.png)

Nguồn SVG: `../../assets/editable/svg/desktop/media-01-tai-phuong-tien.svg`

### Mobile

![Tải phương tiện - mobile](../../assets/preview/png/mobile/media-01-tai-phuong-tien.png)

Nguồn SVG: `../../assets/editable/svg/mobile/media-01-tai-phuong-tien.svg`

## Quyết định cuối

- Trạng thái: **Đã duyệt để triển khai Frontend**.
- Phiên bản thiết kế: **1.2 Final**.
- Desktop và Mobile đã được đối chiếu về thứ tự ưu tiên, trạng thái, quyền và khả năng thao tác.
- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.
- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.
