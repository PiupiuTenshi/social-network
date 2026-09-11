# Checklist QA UI/UX sau khi khóa

## Mỗi màn hình

- [ ] Mục tiêu phù hợp mã chức năng và route.
- [ ] Hành động chính rõ, không có dark pattern.
- [ ] Loading, empty, error, offline, forbidden và retry được xác định khi liên quan.
- [ ] Quyền riêng tư, block và authorization không bị suy đoán ở client.
- [ ] Desktop và Mobile giữ cùng mục tiêu nhưng có thứ tự ưu tiên phù hợp thiết bị.
- [ ] Touch target tối thiểu 44 x 44 px; focus và bàn phím hoạt động.
- [ ] Microcopy tiếng Việt rõ; tên kỹ thuật chỉ giữ khi cần cho code.
- [ ] Toast không che CTA/form; lỗi cần hành động có trạng thái inline hoặc bền vững.
- [ ] API/event mapping không tự phát minh hợp đồng mới.

## Toàn hệ thống

- [ ] Navigation, token, component và trạng thái nhất quán.
- [ ] P0 được triển khai trước P1/P2.
- [ ] Feature `contract-gap` mặc định tắt ngoài môi trường phát triển.
- [ ] SignalR/LiveKit/AI/search có trải nghiệm suy giảm rõ.
- [ ] `design.md`, SVG và PNG cùng phiên bản.
- [ ] `python scripts/validate_design.py --require-final` đạt.
