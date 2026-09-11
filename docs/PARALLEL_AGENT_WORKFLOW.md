# Làm việc song song với nhiều trợ lý lập trình

Chỉ tách công việc song song khi hợp đồng và lược đồ dùng chung đã ổn định. Không cho nhiều trợ lý cùng sửa một aggregate, migration hoặc hợp đồng chưa khóa.

## Khi được phép chạy song song

- Các nhiệm vụ có đầu ra độc lập và không cùng sửa một tệp trọng yếu.
- Producer/consumer đã có lược đồ sự kiện được chấp thuận.
- Backend/frontend đã có OpenAPI ổn định.
- Mỗi nhiệm vụ có mã, phạm vi, tiêu chí chấp nhận và mẫu bàn giao riêng.

## Khi không được chạy song song

- Chưa quyết định dịch vụ sở hữu.
- Cùng thay đổi một migration hoặc bảng nguồn sự thật.
- API hoặc event schema đang được thiết kế lại.
- Một nhiệm vụ phụ thuộc hành vi chưa hoàn thành của nhiệm vụ khác.
- Đang xử lý sự cố hoặc dữ liệu cần một người điều phối duy nhất.

## Tách worktree

Ví dụ tạo worktree cho hai nhiệm vụ độc lập:

```bash
git fetch origin
git worktree add ../sp-acc-01 -b feat/ACC-01-register origin/main
git worktree add ../sp-soc-01 -b feat/SOC-01-follow origin/main
```

Mỗi worktree có một bộ prompt và bản bàn giao riêng. Không chia sẻ thư mục build, secret hoặc database phát triển khi có nguy cơ xung đột.

Xem danh sách:

```bash
git worktree list
```

Sau khi nhánh đã hợp nhất và worktree sạch:

```bash
git worktree remove ../sp-acc-01
git worktree prune
```

Không xóa worktree còn thay đổi chưa commit.

## Hợp đồng bàn giao giữa các trợ lý

Trợ lý thực hiện bước trước phải ghi:

- kết quả và trạng thái;
- tệp/ký hiệu đã đổi;
- hợp đồng hoặc lược đồ đã tạo;
- lệnh và kết quả thật;
- giả định, rủi ro và phần chưa xác minh;
- đầu vào chính xác cho nhiệm vụ kế tiếp.

Trợ lý thực hiện bước sau đọc `AGENTS.md`, nguồn ổn định, hợp đồng nhiệm vụ và bản bàn giao gần nhất; không cần toàn bộ lịch sử hội thoại.

## Điều phối xung đột

1. Dừng hai nhiệm vụ nếu phát hiện cùng thay đổi hợp đồng hoặc ownership.
2. Chọn một nhiệm vụ làm nguồn quyết định và tạo ADR khi cần.
3. Cập nhật prompt của nhiệm vụ phụ thuộc bằng hợp đồng đã khóa.
4. Chỉ tiếp tục khi diff và kiểm thử cho thấy không còn xung đột ngữ nghĩa.
