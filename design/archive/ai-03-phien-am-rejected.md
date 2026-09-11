---
id: "AI-03"
title: "Phiên âm tin nhắn thoại"
group: "AI"
route: "/tro-ly/phien-am/:id"
priority: "P2"
status: "draft"
roles:
  - "Thành viên hội thoại"
functions:
  - "AI-05"
  - "MED-06"
desktop_svg: "assets/editable/svg/desktop/ai-03-phien-am.svg"
mobile_svg: "assets/editable/svg/mobile/ai-03-phien-am.svg"
---

# AI-03 - Phiên âm tin nhắn thoại

## Mục tiêu

Hiển thị audio gốc, tiến trình phiên âm và kết quả mà không làm mất khả năng nghe khi AI thất bại.

## Vai trò và ưu tiên

- Vai trò: Thành viên hội thoại
- Mức ưu tiên: **P2**
- Mã chức năng: `AI-05`, `MED-06`
- Route dự kiến: `/tro-ly/phien-am/:id`

## Bố cục

- Audio player chuẩn, tiến trình job và transcript có timestamp tùy triển khai.
- Lỗi AI không che hoặc xóa audio gốc.

## Hành động

### Chính

- Yêu cầu phiên âm

### Phụ

- Nghe audio
- Sao chép văn bản

## Component

- `AppShell`
- `AudioPlayer`
- `JobStatus`
- `Transcript`
- `Button`

## Dữ liệu và hợp đồng liên quan

- POST transcription/job endpoint theo hợp đồng triển khai
- TranscriptReady

Mọi endpoint chưa được khóa trong OpenAPI phải được đánh dấu là **cần khóa hợp đồng**, không tự tạo chỉ vì mockup cần dữ liệu.

## Trạng thái bắt buộc

- Chưa yêu cầu
- Đang xếp hàng
- Đang xử lý
- Hoàn tất
- Thất bại nhưng audio vẫn dùng được

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

- Audio có điều khiển bàn phím và mô tả.
- Transcript sao chép được.

- Focus ring nhìn thấy.
- Icon-only button có tên truy cập.
- Trạng thái không truyền đạt bằng màu duy nhất.

## Rủi ro cần kiểm soát

- Không tự suy đoán quyền từ trạng thái UI; server là nguồn quyết định.
- Mô-đun có thể bị tắt bằng feature flag; không để điều hướng chết.

## Tiêu chí chấp nhận UI

- Với vai trò Thành viên hội thoại, khi mở `/tro-ly/phien-am/:id`, màn hình hiển thị đúng dữ liệu được phép hoặc trạng thái an toàn.
- Khi thực hiện hành động chính “Yêu cầu phiên âm”, giao diện khóa gửi lặp không chủ đích và phản ánh kết quả server.
- Khi API trả 401/403/404/409/412/422/429/503 liên quan, giao diện dùng trạng thái đã định nghĩa và không làm mất dữ liệu nhập.
- Desktop và mobile giữ cùng mục tiêu, quyền và thứ tự ưu tiên hành động.
- Luồng bàn phím, focus và nhãn truy cập đạt yêu cầu trong tài liệu accessibility.

## Trạng thái

Màn hình độc lập đã bị loại theo phản hồi vòng 1. Phiên âm được tích hợp vào FEED-03 và CHAT-02.
