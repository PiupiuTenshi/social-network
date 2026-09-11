# 14. Sự kiện phân tích UX

Đây là sự kiện phân tích phía client, không thay thế Kafka domain event.

## Quy tắc

- Không gửi nội dung bài viết/tin nhắn, OTP, token, email đầy đủ hoặc dữ liệu nhạy cảm.
- Dùng ID giả danh hoặc category khi cần.
- Tôn trọng consent/chính sách quyền riêng tư.
- Không dùng analytics làm nguồn nghiệp vụ.

## Danh mục đề xuất

| Sự kiện | Thuộc tính an toàn |
|---|---|
| screen_view | screenId, routeTemplate |
| auth_submit | method, resultCategory |
| post_create_submit | mediaCount, visibility, resultCategory |
| reaction_toggle | reactionType, resultCategory |
| follow_toggle | resultCategory |
| message_send | type, resultCategory, latencyBucket |
| realtime_connection | state, transport, retryCountBucket |
| rtc_join | resultCategory, connectionMode |
| media_upload | purpose, sizeBucket, resultCategory |
| search_submit | scope, queryLengthBucket, fallbackUsed |
| order_create | itemCountBucket, resultCategory |
| ai_request | capability, resultCategory, latencyBucket |
| report_submit | targetType, reasonCode, resultCategory |
