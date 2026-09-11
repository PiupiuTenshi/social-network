# Git flow tinh gọn

Bản hướng dẫn thao tác đầy đủ, gắn với ID task/subtask và cổng READY: [execution/GIT_PLAYBOOK.md](execution/GIT_PLAYBOOK.md). Tài liệu đó mở rộng mô hình nhánh bên dưới và phân biệt lệnh mẫu với thao tác đã thực hiện.

Lệnh mẫu an toàn nằm trong [`GIT_COMMANDS.md`](GIT_COMMANDS.md). Khi dùng nhiều worktree hoặc nhiều trợ lý, áp dụng thêm [`PARALLEL_AGENT_WORKFLOW.md`](PARALLEL_AGENT_WORKFLOW.md).

## Mô hình nhánh

Dự án một lập trình viên dùng `main` luôn ở trạng thái có thể phát hành và các nhánh ngắn hạn; không duy trì `develop` dài hạn.

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Chức năng | `feat/<function-id>-<slug>` | `feat/ACC-01-register` |
| Sửa lỗi | `fix/<function-id-or-issue>-<slug>` | `fix/CHT-02-duplicate-message` |
| Tái cấu trúc | `refactor/<scope>-<slug>` | `refactor/social-post-query` |
| Tài liệu | `docs/<slug>` | `docs/event-versioning` |
| Hạ tầng | `chore/<scope>-<slug>` | `chore/kafka-healthcheck` |
| Khẩn cấp | `hotfix/<issue>-<slug>` | `hotfix/SEC-17-token-reuse` |

## Chu kỳ một nhánh

1. Đồng bộ từ `main` sạch.
2. Tạo nhánh ngắn hạn từ `main`.
3. Commit nhỏ, có ý nghĩa và có thể biên dịch/kiểm thử.
4. Cập nhật từ `main` trước pull request khi cần; không viết lại lịch sử của người khác.
5. Pull request có một mục tiêu, tiêu chí chấp nhận và bằng chứng.
6. Mặc định squash khi hợp nhất; chỉ giữ nhiều commit khi lịch sử có giá trị rõ.
7. Tạo tag `vMAJOR.MINOR.PATCH` sau khi đạt G4.

## Conventional Commits

```text
<type>(<scope>): <mô tả>
```

Scope đề xuất: `account`, `social`, `community`, `chat`, `feed`, `media`, `commerce`, `ai`, `gateway`, `building-blocks`, `deploy`, `docs`.

Thay đổi phá vỡ cần dấu `!` và phần `BREAKING CHANGE:` nhưng chỉ được phép khi đã có phiên bản mới hoặc ADR.

## Bảo vệ `main`

- Bắt buộc pull request dù chỉ có một người phát triển.
- Các cổng biên dịch, kiểm thử, kiến trúc, hợp đồng, di trú dữ liệu và bảo mật phải đạt theo phạm vi.
- Không hợp nhất khi còn lỗi Critical/High, hợp đồng lệch hoặc tài liệu chưa đồng bộ.
- Không force push lên `main`; không dùng tag `latest` làm nguồn phát hành duy nhất.

## Hotfix

Tạo từ `main`, giữ phạm vi tối thiểu, thêm kiểm thử hồi quy, phát hành bản vá và tạo công việc theo dõi sau sự cố. Không gộp tái cấu trúc không liên quan.
