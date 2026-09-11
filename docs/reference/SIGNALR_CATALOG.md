# Danh mục SignalR

| Hướng | Phương thức/Sự kiện | Dữ liệu và quy tắc |
| --- | --- | --- |
| Máy khách -> Hub | SendMessage | conversationId, clientMessageId, content, replyTo; bắt buộc kiểm tra thành viên và chống gửi lặp. |
| Máy khách -> Hub | Typing | conversationId, isTyping; trạng thái tạm thời, có giới hạn tần suất và tự hết hạn. |
| Máy khách -> Hub | MarkRead | conversationId, messageId; con trỏ đã đọc chỉ được tiến về phía trước. |
| Máy chủ -> Máy khách | MessageCreated | DTO tin nhắn; chỉ gửi tới nhóm hội thoại đã được cấp quyền. |
| Máy chủ -> Máy khách | MessageUpdated/Deleted | messageId, version và trạng thái mới. |
| Máy chủ -> Máy khách | MessageReactionChanged | messageId và bản tóm tắt tương tác mới. |
| Máy chủ -> Máy khách | TypingChanged | conversationId, userId, isTyping và thời điểm hết hạn. |
| Máy chủ -> Máy khách | ReadUpdated | conversationId, userId, messageId. |
| Máy chủ -> Máy khách | PresenceChanged | userId và trạng thái; áp dụng quyền riêng tư. |
| Máy chủ -> Máy khách | NotificationCreated | DTO thông báo đã được lọc theo người nhận. |
| Máy chủ -> Máy khách | CallInvite | channel hoặc conversation, người mời và siêu dữ liệu RTC. |
| Máy chủ -> Máy khách | AiToken/AiCompleted | requestId, đoạn văn bản tăng dần và trạng thái hoàn tất. |
