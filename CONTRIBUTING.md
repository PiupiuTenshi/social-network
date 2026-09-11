# Hướng dẫn đóng góp

## Luồng làm việc

Với các ID thuộc [execution plan](docs/execution/README.md), bắt buộc dùng `scripts/task_gate.py` để prepare/check/start và submit/review/accept. Chưa READY thì không sửa sản phẩm; tiền nhiệm chưa DONE thì chưa mở subtask phụ thuộc.

1. Chọn hoặc tạo issue có mã chức năng hoặc mã kỹ thuật rõ ràng.
2. Xác nhận các điều kiện trong `docs/DEFINITION_OF_READY.md`.
3. Tạo nhánh theo `docs/GIT_FLOW.md`.
4. Sinh bộ prompt bằng `scripts/generate_prompt_pack.py` hoặc `$build-project-prompts`.
5. Triển khai thay đổi nhỏ, kiểm thử sớm và giữ phạm vi tập trung.
6. Chạy `python scripts/validate_vibe_kit.py` cùng các lệnh biên dịch/kiểm thử thực tế của kho mã.
7. Mở pull request theo `.github/pull_request_template.md`.
8. Chỉ hợp nhất khi đạt `docs/DEFINITION_OF_DONE.md` và tài liệu/hợp đồng đã đồng bộ.

## Quy tắc pull request

- Mỗi PR có một mục tiêu chính; không trộn tái cấu trúc hoặc nâng cấp thư viện không liên quan.
- Nêu rõ API, sự kiện, lược đồ, dữ liệu và bảo mật có thay đổi hay không.
- Đính kèm kết quả kiểm thử, trace, metric hoặc ảnh dashboard khi liên quan.
- Thay đổi kiến trúc phải liên kết ADR.
- Di trú dữ liệu phải có trình tự triển khai, cửa sổ tương thích, backfill và phương án quay lui hoặc tiến tới.

## Commit

Dùng Conventional Commits:

```text
<type>(<scope>): <mô tả ngắn>
```

Loại được phép: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`, `revert`.

Ví dụ:

```text
feat(account): triển khai xoay vòng refresh token
fix(chat): ngăn gửi trùng bằng clientMessageId
```
