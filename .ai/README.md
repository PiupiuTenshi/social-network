# Lớp điều phối trợ lý AI

Thư mục này nối các công cụ lập trình AI với cùng một nguồn quy tắc trung tâm. Không sao chép toàn bộ hướng dẫn sang từng công cụ vì dễ tạo nhiều phiên bản mâu thuẫn.

## Nguồn chính

- `AGENTS.md`: quy trình làm việc và điều kiện dừng.
- `RULES.md`: quy tắc kỹ thuật bắt buộc.
- `docs/CONTEXT_LOADING.md`: cách nạp bối cảnh tối thiểu.
- `.ai/context-map.yaml`: ánh xạ miền và loại nhiệm vụ sang tài liệu cần đọc.
- `prompts/`: prompt chuẩn cho từng loại công việc.

## Cách dùng

1. Chọn miền và loại nhiệm vụ.
2. Dùng `scripts/build_context.py` để liệt kê hoặc ghép tài liệu liên quan.
3. Dùng `scripts/generate_prompt_pack.py` để tạo bộ prompt tám bước.
4. Thực hiện theo thứ tự và dùng tệp bàn giao gần nhất làm đầu vào cho bước kế tiếp.

`context-map.yaml` sử dụng cú pháp JSON hợp lệ đồng thời với YAML để script Python chuẩn đọc được mà không cần thư viện ngoài.
