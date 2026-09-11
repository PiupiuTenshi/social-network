# Hướng dẫn cho Gemini CLI

Nguồn quy tắc bắt buộc là `AGENTS.md` và `RULES.md`. Khi nhận nhiệm vụ:

1. Xác định miền, mã chức năng và dịch vụ sở hữu.
2. Nạp bối cảnh tối thiểu theo `docs/CONTEXT_LOADING.md`.
3. Khảo sát mã và kiểm thử hiện tại trước khi lập kế hoạch.
4. Triển khai thay đổi nhỏ nhất nhưng hoàn chỉnh.
5. Kiểm chứng và báo cáo kết quả thật.

Không tự thay đổi hợp đồng, ownership, bảo mật hoặc production. Dùng prompt trung tâm trong `prompts/` thay vì tạo quy trình riêng dễ lệch phiên bản.
