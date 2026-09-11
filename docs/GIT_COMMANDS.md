# Lệnh Git an toàn theo quy trình dự án

Nếu bắt đầu từ bộ kit chưa có `.git` hoặc cần luồng branch/push/PR/tag/rollback theo từng ID, dùng [Git playbook chi tiết](execution/GIT_PLAYBOOK.md) cùng [cổng READY](execution/READY_GATE.md).

Tài liệu này bổ sung cho [`GIT_FLOW.md`](GIT_FLOW.md). Các lệnh chỉ là mẫu cho kho mã đã có remote `origin`; xác minh nhánh và trạng thái trước khi chạy.

## 1. Bắt đầu nhiệm vụ

```bash
git status
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c feat/ACC-01-register
```

Đổi tên nhánh theo loại công việc và mã chức năng. Không bắt đầu trên worktree có thay đổi không liên quan.

## 2. Kiểm tra thay đổi trước commit

```bash
git status --short
git diff --check
git diff
git diff --staged
```

Chỉ stage tệp thuộc phạm vi:

```bash
git add path/to/file1 path/to/file2
git diff --staged
```

Không dùng `git add .` khi worktree có thay đổi không liên quan mà chưa được rà soát.

## 3. Commit

```bash
git commit
```

Mẫu dòng đầu:

```text
feat(account): triển khai đăng ký ACC-01
fix(chat): ngăn tạo trùng tin nhắn CHT-02
```

Hook `commit-msg` kiểm tra định dạng. Nội dung commit phải mô tả một thay đổi có thể hiểu và kiểm chứng độc lập.

## 4. Đồng bộ nhánh trước pull request

```bash
git fetch origin
git rebase origin/main
```

Chỉ rebase nhánh riêng chưa được người khác dùng. Không viết lại lịch sử nhánh dùng chung. Sau rebase, chạy lại kiểm chứng trước khi push.

```bash
git push -u origin feat/ACC-01-register
```

Không dùng `--force` hoặc `--force-with-lease` nếu chưa hiểu rõ tác động và chưa được thống nhất.

## 5. Sửa commit mà chưa push

Bổ sung tệp vào commit cuối:

```bash
git add path/to/file
git commit --amend
```

Chỉ amend commit chưa chia sẻ. Sau khi đã push hoặc có người khác dựa vào commit, tạo commit mới.

## 6. Bỏ stage mà không xóa nội dung

```bash
git restore --staged path/to/file
```

Khôi phục nội dung tệp sẽ làm mất thay đổi chưa commit; chỉ chạy khi đã xem diff và thật sự muốn bỏ:

```bash
git diff -- path/to/file
git restore path/to/file
```

## 7. Hoàn tác thay đổi đã hợp nhất

Ưu tiên tạo commit đảo ngược để giữ lịch sử:

```bash
git revert <commit-sha>
```

Không dùng `git reset --hard` hoặc xóa branch/commit để xử lý sự cố trên nhánh dùng chung.

## 8. Sau khi hợp nhất

```bash
git switch main
git pull --ff-only origin main
git branch -d feat/ACC-01-register
```

Chỉ xóa nhánh remote sau khi xác nhận pull request đã hợp nhất và không còn công việc cần giữ.
