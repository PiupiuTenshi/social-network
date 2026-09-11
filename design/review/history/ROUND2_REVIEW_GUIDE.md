# Hướng dẫn duyệt UI/UX — Vòng 2

## Mục tiêu

Duyệt lại bản Desktop đã sửa theo phản hồi vòng 1, sau đó kiểm tra bản Mobile được tái cấu trúc từ cùng kiến trúc thông tin và thứ tự ưu tiên hành động.

## Thứ tự duyệt khuyến nghị

1. Duyệt `Desktop` theo thứ tự P0 → P1 → P2.
2. Với mỗi màn hình Desktop, kiểm tra: nội dung, bố cục, hành động chính, trạng thái lỗi/rỗng/tải và tính nhất quán với màn hình liên quan.
3. Chuyển sang `Mobile` của chính màn hình đó; kiểm tra hành động quan trọng còn dễ tiếp cận, không bị thu nhỏ máy móc từ Desktop.
4. Chọn một trạng thái:
   - `approved`: chấp thuận.
   - `needs_changes`: cần sửa; ghi rõ thành phần, vị trí và kết quả mong muốn.
   - `deferred`: hoãn khỏi phạm vi.
   - `rejected`: loại khỏi thiết kế.
5. Xuất YAML từ bảng duyệt và gửi lại tệp đó để tạo vòng sửa tiếp theo.

## Quy tắc ghi chú

Ghi chú tốt nên có cấu trúc:

```text
[Màn hình/thiết bị] [Vị trí] [Vấn đề hiện tại] → [Kết quả mong muốn]
```

Ví dụ:

```text
Mobile · FEED-01 · Thanh hành động bên phải quá gần mép → tăng vùng chạm lên tối thiểu 44 px và giữ cách mép 12 px.
```

## Các thay đổi lớn cần chú ý

- Thương hiệu mới: **Twight Light**; dòng mô tả **Multi Social Comunity**.
- Điều hướng ứng dụng chuyển sang tab trên Desktop và thanh đáy trên Mobile.
- Avatar góc phải mở menu hồ sơ, cài đặt, ngôn ngữ và giao diện.
- Bảng tin có ô đăng bài bám dính; bài viết dùng cụm hành động dọc và hỗ trợ báo cáo.
- RTC dùng cửa sổ hoặc ứng dụng riêng.
- AI-03 đã bị loại; phiên âm xuất hiện trong chi tiết bài viết hoặc hội thoại.
- Marketplace chỉ mô tả thanh toán trực tiếp với người bán trong UI vòng này.

## Điều kiện tạo `design.md`

Chỉ khóa `design.md` khi:

- Tất cả màn hình P0 và P1 bắt buộc ở trạng thái `approved`.
- Màn hình P2 là `approved` hoặc `deferred`.
- Không còn thay đổi chưa xử lý đối với navigation, token, component và responsive.
- Các yêu cầu làm đổi hợp đồng Backend đã được chấp thuận hoặc đánh dấu chưa triển khai.
