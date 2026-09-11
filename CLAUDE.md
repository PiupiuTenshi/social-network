# Hướng dẫn cho Claude Code

Đọc và tuân thủ `AGENTS.md` cùng `RULES.md` trước mọi thay đổi. Chỉ nạp thêm tài liệu theo `docs/CONTEXT_LOADING.md`.

- Dùng `.claude/commands/build-project-prompts.md` để tạo chuỗi prompt cho nhiệm vụ lớn.
- Dùng `.claude/commands/implement-feature.md` cho một lát cắt dọc đã khóa hợp đồng.
- Dùng `.claude/commands/fix-bug.md` cho lỗi có triệu chứng và bằng chứng.
- Không tự commit, push, deploy, thay đổi production hoặc chạy di trú phá hủy.
- Bản bàn giao phải nêu tệp đã đổi, lệnh thực sự đã chạy và kết quả thật.
