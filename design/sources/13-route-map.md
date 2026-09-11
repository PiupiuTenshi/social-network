# 13. Bản đồ route

Bản đồ chi tiết máy đọc được: `data/routes.json`.

## Route công khai

- `/`
- `/dang-nhap`
- `/dang-ky`
- `/quen-mat-khau`
- `/dat-lai-mat-khau`
- `/loi-moi/:code`

## Route người dùng

- `/bang-tin`
- `/bai-viet/*`
- `/toi`
- `/nguoi-dung/:id`
- `/tim-kiem`
- `/thong-bao`
- `/tin-nhan/*`
- `/cong-dong/*`
- `/phuong-tien/*`
- `/thiet-lap/*`

## Route P2 theo feature flag

- `/cho/*`
- `/tro-ly/*`

## Route điều hành

- `/dieu-hanh/bao-cao`
- `/dieu-hanh/bao-cao/:id`

Route điều hành bắt buộc guard vai trò ở client để UX rõ, nhưng server vẫn là nơi quyết định quyền.
