# PH01-FE-FOUNDATION-01 — Definition of Ready

- Thời điểm: 2026-09-09T00:00:00+07:00
- Môi trường: Windows PowerShell; Node v22.19.0; npm 11.6.0 qua `npm.cmd`.
- Baseline: working-tree snapshot, repository chưa khởi tạo Git/remote.

## Phạm vi và nguồn đã xác minh

- Chỉ dựng Angular shell, token/primitives, navigation, guard, deep link và shared state; không triển khai màn hình nghiệp vụ hay tự suy diễn API.
- `frontend/package.json`, `frontend/package-lock.json` và `frontend/angular.json` tồn tại. Lệnh thực: `npm.cmd --prefix frontend ci`, `npm.cmd --prefix frontend run build`; workspace chưa khai báo script lint/type riêng, nên Angular build là type-check hiện có.
- `design/design.md` đã khóa 47 màn hình; token nằm ở `design/tokens/design-tokens.json`; state matrix là `design/sources/11-state-matrix.md`.
- G0-01 đã DONE. `design/sources/19-frontend-contract-readiness.md` yêu cầu P2 và contract-gap bị tắt mặc định; shell không gọi API nghiệp vụ.

## Quyết định và điều kiện dừng

- Deep link chưa xác thực chuyển về route hợp lệ; guard chỉ dùng trạng thái client trong shell, không thay thế kiểm tra quyền backend.
- Không xử lý PII, migration, retry hoặc ghi dữ liệu trong task này.
- Dừng khi thiết kế/hợp đồng mâu thuẫn, hoặc cần API/claim/permission chưa được khóa.

## Kiểm chứng dự kiến

1. `npm.cmd --prefix frontend ci`
2. `npm.cmd --prefix frontend run build`
3. Accessibility harness cho keyboard/focus, target 44px, contrast và reduced motion.
