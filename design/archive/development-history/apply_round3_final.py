#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
LATEST_FEEDBACK = Path('/mnt/data/01d2c240-60ac-4aaa-9421-274009a82227.yaml')

spec = importlib.util.spec_from_file_location('round2', ROOT / 'scripts' / 'generate_round2.py')
if spec is None or spec.loader is None:
    raise RuntimeError('Không tải được generator vòng 2.')
g = importlib.util.module_from_spec(spec)
sys.modules['round2'] = g
spec.loader.exec_module(g)

BRAND = g.BRAND


def auth_background() -> str:
    out = g.rect(0, 0, 1440, 1024, BRAND['surface2'], 'none', 0)
    out += g.rect(0, 0, 780, 1024, 'url(#twilight)', 'none', 0)
    out += g.rect(34, 30, 46, 46, 'url(#brand)', 'none', 13)
    out += g.tx(57, 61, 'T', 20, 900, '#FFFFFF', 'middle')
    out += g.tx(94, 50, 'Twight Light', 18, 900, '#FFFFFF')
    out += g.tx(94, 68, 'Multi Social Comunity', 11, 600, '#D8DAFF')
    paths = [
        'M80 250 C210 120 400 380 680 170',
        'M50 500 C280 650 380 300 720 520',
        'M120 810 C300 630 490 920 690 700',
        'M130 140 C300 330 520 40 730 260',
    ]
    for i, d in enumerate(paths):
        out += f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="2" stroke-dasharray="7 12"><animate attributeName="stroke-dashoffset" from="0" to="-38" dur="{5+i}s" repeatCount="indefinite"/></path>'
    avs = [(130,220,'A','#F97376'),(330,160,'B','#6C5CE7'),(550,290,'C','#22C1C3'),(210,485,'D','#F59E0B'),(480,520,'E','#EC4899'),(650,420,'F','#3B82F6'),(130,760,'G','#10B981'),(380,820,'H','#8B5CF6'),(630,735,'I','#F97316')]
    for i, (x, y, lab, color) in enumerate(avs):
        out += f'<g><animateTransform attributeName="transform" type="translate" values="0 0; {8 if i%2==0 else -7} {-6 if i%3==0 else 7}; 0 0" dur="{3.8+i*.27}s" repeatCount="indefinite"/>{g.avatar(x,y,35,lab,color,"online" if i%3==0 else "")}</g>'
    out += g.tx(74, 875, 'One human, boring!!!', 26, 800, '#FFFFFF')
    out += g.tx(74, 910, 'One million humans, Nice, very nice', 28, 900, '#FFFFFF')
    out += g.tx(74, 944, 'Kết nối cá tính. Khám phá cộng đồng. Tạo nên điều đáng nhớ.', 13, 600, '#DDE1FF')
    return out


def password_rules(x: float, y: float, compact: bool = False) -> str:
    width = 420 if not compact else 350
    cols = 2 if not compact else 1
    item_w = width / cols
    rules = [
        ('✓', 'Tối thiểu 8 ký tự', BRAND['green']),
        ('✓', 'Có chữ hoa và chữ thường', BRAND['green']),
        ('✓', 'Có ít nhất một chữ số', BRAND['green']),
        ('×', 'Thiếu ký tự đặc biệt', BRAND['danger']),
    ]
    out = g.tx(x, y - 10, 'Mức độ an toàn của mật khẩu', 11, 800, BRAND['muted'])
    for i, (symbol, label, color) in enumerate(rules):
        row = i // cols
        col = i % cols
        xx = x + col * item_w
        yy = y + row * (34 if not compact else 30)
        out += g.circle(xx + 10, yy + 1, 9, color)
        out += g.tx(xx + 10, yy + 5, symbol, 11, 900, '#FFFFFF', 'middle')
        out += g.tx(xx + 27, yy + 5, label, 10 if compact else 11, 700, color if symbol == '×' else BRAND['ink'])
    return out


def final_auth_scene(item: dict[str, Any]) -> str:
    sid = item['id']
    if sid == 'AUTH-01':
        return g.auth_scene(item)
    out = auth_background()
    form_x, form_y, form_w = 870, 174, 470
    title_map = {
        'AUTH-02': ('Chào mừng trở lại', 'Tiếp tục câu chuyện và những kết nối đang chờ bạn.'),
        'AUTH-03': ('Tạo tài khoản của bạn', 'Chỉ vài bước để bước vào hàng triệu câu chuyện.'),
        'AUTH-04': ('Khôi phục quyền truy cập', 'Nhập email để nhận mã xác minh an toàn.'),
        'AUTH-05': ('Tạo mật khẩu mới', 'Hoàn tất xác minh trước khi đặt lại mật khẩu.'),
    }
    title, sub = title_map[sid]
    out += g.tx(form_x, form_y, title, 29, 900)
    out += g.paragraph(form_x, form_y + 34, sub, 58, 13, BRAND['muted'], 20, 2)

    # Toast luôn neo top-end, nằm ngoài vùng tiêu đề và form.
    if sid == 'AUTH-02':
        out += g.toast(1090, 24, 'Đăng nhập thành công', 'Đang đưa bạn về Trang chủ.', 'success', 326)
        out += g.input_box(form_x, form_y + 112, form_w, 'Email hoặc tên người dùng', 'minhsang@example.com', 'ok')
        out += g.input_box(form_x, form_y + 192, form_w, 'Mật khẩu', '••••••••••')
        out += g.tx(form_x, form_y + 274, '☐ Ghi nhớ đăng nhập', 12, 600, BRAND['muted'])
        out += g.tx(form_x + form_w, form_y + 274, 'Quên mật khẩu?', 12, 700, BRAND['primary'], 'end')
        out += g.btn(form_x, form_y + 304, form_w, 'Đăng nhập', True, 50)
        out += g.btn(form_x, form_y + 368, form_w, 'Tiếp tục với Google', False, 48)
        out += g.tx(form_x + form_w / 2, form_y + 446, 'Chưa có tài khoản?  Đăng ký miễn phí', 11, 700, BRAND['primary'], 'middle')
    elif sid == 'AUTH-03':
        out += g.toast(1090, 24, 'Mật khẩu chưa đủ mạnh', 'Hãy bổ sung ký tự đặc biệt.', 'error', 326)
        out += g.input_box(form_x, form_y + 88, form_w, 'Tên người dùng', 'minhsang', 'ok')
        out += g.input_box(form_x, form_y + 158, form_w, 'Email', 'minhsang@example.com', 'ok')
        out += g.input_box(form_x, form_y + 228, form_w, 'Mật khẩu', 'Twight2026', 'bad')
        out += password_rules(form_x, form_y + 306, False)
        out += g.input_box(form_x, form_y + 380, form_w, 'Xác nhận mật khẩu', 'Twight2026', 'ok')
        out += g.btn(form_x, form_y + 462, form_w, 'Tạo tài khoản', True, 50)
        out += g.tx(form_x + form_w / 2, form_y + 536, 'Bằng việc đăng ký, bạn đồng ý với Điều khoản và Quyền riêng tư.', 10, 600, BRAND['muted'], 'middle')
    elif sid == 'AUTH-04':
        out += g.toast(1090, 24, 'Đã gửi mã xác minh', 'Mã có hiệu lực trong 10 phút.', 'success', 326)
        out += g.input_box(form_x, form_y + 128, form_w, 'Email', 'minhsang@example.com', 'ok')
        out += g.btn(form_x, form_y + 210, form_w, 'Gửi mã xác minh', True, 50)
        out += g.rect(form_x, form_y + 286, form_w, 92, '#EEF6FF', '#BFDBFE', 14)
        out += g.tx(form_x + 20, form_y + 317, 'Kiểm tra hộp thư đến và cả thư rác.', 12, 800, '#1D4ED8')
        out += g.paragraph(form_x + 20, form_y + 343, 'Bạn có thể yêu cầu gửi lại sau khi thời gian đếm ngược kết thúc.', 56, 11, '#475569', 18, 2)
        out += g.tx(form_x, form_y + 424, '← Quay lại đăng nhập', 12, 700, BRAND['primary'])
    elif sid == 'AUTH-05':
        # Hiển thị đúng trạng thái vừa xác minh xong: modal giữa màn hình, sau OK mới mở form.
        out += g.rect(form_x, form_y + 90, form_w, 426, '#FFFFFF', BRAND['line'], 18)
        out += g.tx(form_x + 22, form_y + 126, 'Bước 2/2 · Đặt mật khẩu mới', 12, 800, BRAND['primary'])
        out += g.input_box(form_x + 22, form_y + 164, form_w - 44, 'Mật khẩu mới', '••••••••••', 'ok')
        out += g.input_box(form_x + 22, form_y + 244, form_w - 44, 'Xác nhận mật khẩu mới', '••••••••••', 'ok')
        out += g.paragraph(form_x + 22, form_y + 330, 'Sau khi đổi mật khẩu, mọi phiên đăng nhập cũ sẽ bị thu hồi.', 55, 11, BRAND['muted'], 18, 2)
        out += g.btn(form_x + 22, form_y + 390, form_w - 44, 'Đổi mật khẩu', True, 48)
        out += g.rect(780, 0, 660, 1024, '#07162B', 'none', 0, opacity=.30)
        modal_x, modal_y, modal_w = 930, 346, 430
        out += g.rect(modal_x, modal_y, modal_w, 262, '#FFFFFF', BRAND['line'], 20, extra='filter="url(#shadow)"')
        out += g.circle(modal_x + modal_w/2, modal_y + 62, 28, BRAND['green'])
        out += g.tx(modal_x + modal_w/2, modal_y + 71, '✓', 25, 900, '#FFFFFF', 'middle')
        out += g.tx(modal_x + modal_w/2, modal_y + 116, 'Mã xác minh hợp lệ', 20, 900, BRAND['ink'], 'middle')
        out += g.paragraph(modal_x + 46, modal_y + 148, 'Nhấn tiếp tục để nhập mật khẩu mới cho tài khoản của bạn.', 49, 12, BRAND['muted'], 20, 2)
        out += g.btn(modal_x + 38, modal_y + 198, modal_w - 76, 'OK, nhập mật khẩu mới', True, 46)
    return out


def final_post_card(x: float, y: float, w: float, h: float = 520, video: bool = True, transcript: bool = False) -> str:
    out = g.rect(x, y, w, h, '#FFFFFF', BRAND['line'], 18, extra='filter="url(#tinyShadow)"')
    out += g.avatar(x + 38, y + 38, 21, 'L', '#FF8B6A', 'online')
    out += g.tx(x + 70, y + 32, 'Linh Nguyễn', 14, 800)
    out += g.tx(x + 70, y + 52, '2 giờ · Bạn bè', 11, 500, BRAND['muted'])
    out += g.tx(x + w - 30, y + 39, '•••', 18, 800, BRAND['muted'], 'middle')
    out += g.tx(x + 22, y + 90, 'Một khoảnh khắc nhỏ, nhưng đủ khiến cả ngày trở nên đáng nhớ.', 13, 700)
    media_y = y + 110
    media_h = 266 if video else 184
    out += g.rect(x + 22, media_y, w - 44, media_h, 'url(#media)', 'none', 16)
    out += g.circle(x + w/2, media_y + media_h/2, 31, '#FFFFFF', 'none', 1, 'opacity=".92"')
    out += g.tx(x + w/2 + 2, media_y + media_h/2 + 8, '▶', 24, 800, BRAND['primary'], 'middle')
    out += g.pill(x + 34, media_y + 18, 94, '01:42 · HD', '#07162BCC', '#FFFFFF')
    out += g.icon_button(x + w - 64, media_y + media_h - 46, 'Toàn màn hình', 'F', False, 34)
    row_y = media_y + media_h + 18
    out += g.line(x + 22, row_y, x + w - 22, row_y)
    actions = [
        ('♡', '1,2K', 'Thích'),
        ('◯', '128', 'Bình luận'),
        ('↻', '45', 'Đăng lại'),
        ('◇', '', 'Lưu'),
        ('↗', '', 'Chia sẻ'),
    ]
    widths = [118, 132, 122, 96, 108]
    total = sum(widths)
    gap = max(8, (w - 44 - total) / (len(widths)-1))
    xx = x + 22
    for (icon, count, label), ww in zip(actions, widths):
        out += g.rect(xx, row_y + 12, ww, 42, BRAND['surface2'], 'none', 12)
        value = f'{icon} {label}' + (f' · {count}' if count else '')
        out += g.tx(xx + ww/2, row_y + 38, value, 10, 800, BRAND['ink'], 'middle')
        xx += ww + gap
    if transcript:
        out += g.rect(x + 22, row_y + 68, w - 44, 64, BRAND['surface2'], 'none', 10)
        out += g.tx(x + 36, row_y + 91, 'Phiên âm', 11, 800, BRAND['primary'])
        out += g.tx(x + 36, row_y + 112, '“Hôm nay mình muốn kể về cách một ý tưởng nhỏ trở thành sản phẩm...”', 10, 500, BRAND['muted'])
    return out


def rich_editor_scene(sid: str) -> str:
    title = 'Tạo bài viết' if sid == 'FEED-02' else 'Chỉnh sửa bài viết'
    body = 'Hôm nay mình muốn chia sẻ một điều thú vị...' if sid == 'FEED-02' else 'Huy và Lưu vừa hoàn thiện một bản thiết kế mới...'
    out = g.app_shell('Trang chủ')
    out += g.screen_title(258, 116, title, 'Soạn nội dung rõ ràng, đẹp và dễ đọc trên mọi thiết bị.')
    out += g.section_card(258, 166, 820, 742, 'Nội dung bài viết')
    out += g.avatar(292, 214, 22, 'M', '#6C5CE7', 'online')
    out += g.tx(326, 210, 'Phạm Minh Sáng', 13, 800)
    out += g.pill(326, 224, 154, 'Bạn bè · Tùy chỉnh', '#F1F5F9', BRAND['ink'])
    # Toolbar có nhóm rõ ràng, điều khiển chữ được làm đẹp và trạng thái active rõ.
    out += g.tx(280, 286, 'ĐỊNH DẠNG CHỮ', 10, 900, BRAND['muted'])
    out += g.rect(280, 304, 772, 62, '#F8FAFC', BRAND['line'], 12)
    out += g.rect(294, 316, 132, 38, '#FFFFFF', BRAND['line'], 9) + g.tx(310, 340, 'Inter', 11, 700) + g.tx(410, 340, '⌄', 12, 700, BRAND['muted'])
    out += g.rect(436, 316, 84, 38, '#FFFFFF', BRAND['line'], 9) + g.tx(452, 340, '16 px', 11, 700) + g.tx(504, 340, '⌄', 12, 700, BRAND['muted'])
    controls = [('B', True), ('I', False), ('U', False), ('S', False), ('H1', False), ('•', False), ('1.', False), ('↗', False), ('☺', False)]
    cx = 534
    for label, active in controls:
        size = 40 if label not in {'H1'} else 46
        out += g.rect(cx, 316, size, 38, BRAND['primary'] if active else '#FFFFFF', BRAND['primary'] if active else BRAND['line'], 9)
        out += g.tx(cx + size/2, 341, label, 12, 900 if active else 700, '#FFFFFF' if active else BRAND['ink'], 'middle')
        cx += size + 8
    out += g.rect(280, 384, 772, 220, '#FFFFFF', BRAND['line'], 12)
    out += g.tx(300, 420, body, 15, 800, BRAND['ink'])
    out += g.tx(300, 452, 'Dòng được chọn đang dùng kiểu chữ đậm để tạo điểm nhấn.', 14, 800, BRAND['ink'])
    out += g.tx(300, 486, 'Nội dung thường giữ nhịp đọc thoáng, tránh dùng quá nhiều kiểu chữ.', 13, 500, BRAND['muted'])
    out += g.tx(1030, 580, '248 / 5.000', 10, 600, BRAND['muted'], 'end')
    out += g.tx(280, 644, 'ẢNH VÀ VIDEO', 10, 900, BRAND['muted'])
    for i in range(3):
        out += g.rect(280+i*154, 664, 138, 96, 'url(#media)' if i < 2 else BRAND['surface2'], BRAND['line'], 12)
        if i == 2:
            out += g.tx(349+i*154, 716, '+ Thêm', 12, 800, BRAND['primary'], 'middle')
    out += g.line(280, 790, 1052, 790)
    out += g.btn(280, 816, 132, 'Hủy', False, 44)
    out += g.btn(880, 816, 172, 'Đăng bài' if sid == 'FEED-02' else 'Lưu thay đổi', True, 44)
    out += g.section_card(1102, 166, 304, 420, 'Phạm vi hiển thị', 'Ai có thể xem bài viết này?')
    opts = [('Tất cả mọi người', False), ('Bạn bè', sid == 'FEED-04'), ('Chỉ mình tôi', False), ('Tùy chỉnh', sid == 'FEED-02')]
    for i, (label, selected) in enumerate(opts):
        yy = 236 + i*68
        out += g.rect(1124, yy-22, 260, 52, BRAND['soft'] if selected else '#FFFFFF', BRAND['primary'] if selected else BRAND['line'], 12)
        out += g.circle(1148, yy+4, 9, '#FFFFFF', BRAND['primary'], 2)
        if selected:
            out += g.circle(1148, yy+4, 5, BRAND['primary'])
        out += g.tx(1170, yy+8, label, 12, 800 if selected else 700, BRAND['primary'] if selected else BRAND['ink'])
    out += g.rect(1124, 520, 260, 42, '#EEF6FF', '#BFDBFE', 10)
    out += g.tx(1140, 546, 'Tùy chỉnh danh sách người xem', 10, 700, '#1D4ED8')
    return out


def final_feed_scene(item: dict[str, Any]) -> str:
    sid = item['id']
    if sid == 'FEED-01':
        out = g.app_shell('Trang chủ')
        out += g.sticky_composer(252, 94, 790)
        out += final_post_card(252, 184, 790, 520, True, False)
        out += g.section_card(1068, 94, 338, 236, 'Khám phá theo nhịp của bạn', 'Gợi ý mới cho hôm nay')
        for i, (lab, color) in enumerate([('Công nghệ','#EAF2FF'),('Âm nhạc','#FDF2F8'),('Du lịch','#ECFDF5')]):
            out += g.pill(1090 + (i%2)*140, 164 + (i//2)*44, 126, lab, color, BRAND['ink'])
        out += g.section_card(1068, 350, 338, 250, 'Người bạn có thể biết', 'Ưu tiên kết nối liên quan')
        for i, name in enumerate(['An Trần','Lê Vân','Phạm Thư']):
            yy = 418 + i*55
            out += g.avatar(1094, yy, 18, name[0], ['#F97376','#10B981','#3B82F6'][i], 'online' if i == 0 else '')
            out += g.tx(1122, yy-2, name, 12, 800)
            out += g.tx(1122, yy+16, 'Có 8 bạn chung', 10, 500, BRAND['muted'])
            out += g.tx(1380, yy+4, 'Theo dõi', 11, 800, BRAND['primary'], 'end')
        return out
    if sid in {'FEED-02', 'FEED-04'}:
        return rich_editor_scene(sid)
    if sid == 'FEED-03':
        out = g.app_shell('Trang chủ')
        out += g.rect(224, 74, 1216, 950, '#0B1020', 'none', 0, opacity=.40)
        out += g.rect(280, 92, 1094, 878, '#FFFFFF', BRAND['line'], 22, extra='filter="url(#shadow)"')
        out += g.tx(316, 132, 'Chi tiết bài viết', 20, 900)
        out += g.tx(1336, 132, '×', 22, 700, BRAND['muted'], 'middle')
        out += final_post_card(316, 160, 650, 548, True, True)
        out += g.tx(998, 178, 'Bình luận', 16, 900)
        tabs = [('Mới nhất', 82), ('Tất cả', 66), ('Cũ nhất', 72)]
        xx = 998
        for i, (label, ww) in enumerate(tabs):
            out += g.pill(xx, 198, ww, label, BRAND['soft'] if i == 0 else BRAND['surface2'], BRAND['primary'] if i == 0 else BRAND['muted'])
            xx += ww + 8
        comments = [('An Trần','Đoạn video hay quá!','12 phút'),('Lê Vân','Mình cũng từng gặp trải nghiệm tương tự.','28 phút'),('Huy Đỗ','Cảm ơn bạn đã chia sẻ.','1 giờ')]
        for i, (name, content, time) in enumerate(comments):
            yy = 274 + i*126
            out += g.avatar(1018, yy, 18, name[0], ['#F97376','#10B981','#3B82F6'][i])
            out += g.rect(1044, yy-24, 294, 72, BRAND['surface2'], 'none', 12)
            out += g.tx(1058, yy-3, name, 11, 800)
            out += g.paragraph(1058, yy+17, content, 36, 10, BRAND['ink'], 15, 2)
            out += g.tx(1046, yy+68, f'♡ Thích  ·  ↩ Trả lời  ·  ••• Báo cáo  ·  {time}', 9, 600, BRAND['muted'])
        out += g.btn(998, 664, 340, 'Hiển thị thêm bình luận', False, 40)
        out += g.rect(998, 720, 340, 116, '#FFFFFF', BRAND['line'], 14)
        out += g.tx(1014, 750, 'Viết bình luận...', 11, 500, '#94A3B8')
        out += g.tx(1014, 816, 'Enter để gửi · Shift+Enter xuống dòng', 9, 600, BRAND['muted'])
        out += g.btn(1218, 784, 104, 'Gửi', True, 36)
        return out
    if sid == 'FEED-05':
        out = g.app_shell('Video')
        out += g.toast(1080, 82, 'Đang xử lý dưới nền', 'Bạn có thể rời trang an toàn.', 'success', 326)
        out += g.screen_title(258, 124, 'Video của bạn đang được xử lý', 'Tiến trình tiếp tục chạy khi bạn chuyển sang màn hình khác.')
        out += g.section_card(258, 178, 790, 622, 'Trạng thái xử lý', 'Video “Một ngày cùng đội dự án”')
        out += g.rect(282, 242, 742, 18, '#E8ECF3', 'none', 9)
        out += g.rect(282, 242, 534, 18, 'url(#brand)', 'none', 9)
        out += g.tx(282, 288, '72% · Đang tạo nhiều độ phân giải và ảnh thu nhỏ', 12, 800, BRAND['primary'])
        out += g.tx(1008, 288, 'Khoảng 2 phút', 11, 600, BRAND['muted'], 'end')
        out += g.tx(282, 338, 'Chọn ảnh thu nhỏ', 13, 800)
        for i in range(4):
            out += g.rect(282+i*178, 360, 160, 104, 'url(#media)', BRAND['primary'] if i == 1 else BRAND['line'], 12, 3 if i == 1 else 1)
            out += g.pill(292+i*178, 370, 58, 'Khung '+str(i+1), '#07162BCC', '#FFFFFF')
        out += g.btn(282, 486, 188, 'Tải ảnh từ máy', False, 42)
        out += g.tx(282, 556, 'Sau khi hoàn tất', 13, 800)
        out += g.tx(282, 590, '☑ Tự động đăng theo phạm vi đã chọn', 12, 600)
        out += g.tx(282, 624, '☐ Lưu thành bản nháp để xem lại', 12, 600)
        out += g.tx(282, 658, '☐ Lên lịch đăng lúc 20:30 hôm nay', 12, 600)
        out += g.btn(824, 726, 200, 'Đóng và chạy nền', True, 44)
        out += g.section_card(1072, 190, 334, 284, 'Nếu xử lý thất bại', 'Lỗi phải có lý do và cách phục hồi')
        out += g.rect(1094, 256, 290, 84, '#FEF2F2', '#FECACA', 12)
        out += g.tx(1112, 286, 'Âm thanh không hợp lệ', 12, 900, '#B91C1C')
        out += g.tx(1112, 312, 'Thay tệp âm thanh hoặc tắt âm rồi thử lại.', 10, 600, '#991B1B')
        out += g.btn(1094, 360, 136, 'Thử lại', True, 40)
        out += g.btn(1242, 360, 142, 'Lưu bản nháp', False, 40)
        out += g.section_card(1072, 500, 334, 266, 'Dashboard video', 'Số liệu mở sau khi đăng')
        stats = [('Lượt xem','—'),('Lượt thích','—'),('Chia sẻ','—'),('Thời gian đăng','20:30')]
        for i, (label, value) in enumerate(stats):
            yy = 560 + i*46
            out += g.tx(1094, yy, label, 11, 600, BRAND['muted'])
            out += g.tx(1378, yy, value, 12, 800, BRAND['ink'], 'end')
        return out
    return g.feed_scene(item)


def mobile_auth_background() -> str:
    out = g.rect(0, 0, 390, 844, '#F8FAFC', 'none', 0)
    out += g.rect(0, 0, 390, 230, 'url(#twilight)', 'none', 0)
    out += g.rect(18, 18, 40, 40, 'url(#brand)', 'none', 11)
    out += g.tx(38, 45, 'T', 18, 900, '#FFFFFF', 'middle')
    out += g.tx(68, 32, 'Twight Light', 14, 900, '#FFFFFF')
    out += g.tx(68, 49, 'Multi Social Comunity', 8, 600, '#DDE1FF')
    for i, (x,y,color) in enumerate([(40,100,'#F97376'),(112,142,'#6C5CE7'),(190,94,'#10B981'),(274,152,'#3B82F6'),(348,104,'#EC4899')]):
        out += g.avatar(x,y,24,str(i+1),color,'online' if i%2==0 else '')
    out += g.tx(20, 202, 'One human, boring!!! One million humans, Nice, very nice', 9, 800, '#FFFFFF')
    return out


def final_mobile_auth(item: dict[str, Any]) -> str:
    sid = item['id']
    if sid == 'AUTH-01':
        return g.mobile_auth(item)
    out = mobile_auth_background()
    title = {'AUTH-02':'Chào mừng trở lại','AUTH-03':'Tạo tài khoản','AUTH-04':'Quên mật khẩu','AUTH-05':'Mật khẩu mới'}[sid]
    out += g.tx(20, 270, title, 22, 900)
    y = 314
    if sid == 'AUTH-02':
        out += g.toast(74, 72, 'Đăng nhập thành công', 'Đang mở Trang chủ.', 'success', 300)
        out += g.input_box(20,y,350,'Email hoặc tên người dùng','minhsang@example.com','ok')
        out += g.input_box(20,y+78,350,'Mật khẩu','••••••••')
        out += g.tx(20,y+154,'☐ Ghi nhớ',10,600,BRAND['muted'])
        out += g.tx(370,y+154,'Quên mật khẩu?',10,700,BRAND['primary'],'end')
        out += g.btn(20,y+180,350,'Đăng nhập',True,48)
        out += g.btn(20,y+242,350,'Tiếp tục với Google',False,46)
    elif sid == 'AUTH-03':
        out += g.toast(74, 72, 'Mật khẩu chưa đủ mạnh', 'Bổ sung ký tự đặc biệt.', 'error', 300)
        out += g.input_box(20,y,350,'Tên người dùng','minhsang','ok')
        out += g.input_box(20,y+68,350,'Email','minhsang@example.com','ok')
        out += g.input_box(20,y+136,350,'Mật khẩu','Twight2026','bad')
        out += password_rules(20, y+208, True)
        out += g.input_box(20,y+330,350,'Xác nhận mật khẩu','Twight2026','ok')
        out += g.btn(20,y+408,350,'Tạo tài khoản',True,48)
    elif sid == 'AUTH-04':
        out += g.toast(74, 72, 'Đã gửi mã xác minh', 'Mã có hiệu lực 10 phút.', 'success', 300)
        out += g.input_box(20,y,350,'Email','minhsang@example.com','ok')
        out += g.btn(20,y+80,350,'Gửi mã xác minh',True,48)
        out += g.rect(20,y+148,350,86,'#EEF6FF','#BFDBFE',12)
        out += g.tx(36,y+178,'Kiểm tra hộp thư đến và thư rác.',11,800,'#1D4ED8')
        out += g.tx(36,y+204,'Có thể gửi lại sau khi đếm ngược kết thúc.',9,600,'#475569')
        out += g.tx(20,y+276,'← Quay lại đăng nhập',11,700,BRAND['primary'])
    elif sid == 'AUTH-05':
        out += g.rect(12, 300, 366, 436, '#FFFFFF', BRAND['line'], 16)
        out += g.tx(28, 334, 'Bước 2/2 · Đặt mật khẩu mới', 11, 800, BRAND['primary'])
        out += g.input_box(28, 366, 334, 'Mật khẩu mới', '••••••••', 'ok')
        out += g.input_box(28, 444, 334, 'Xác nhận mật khẩu', '••••••••', 'ok')
        out += g.btn(28, 540, 334, 'Đổi mật khẩu', True, 48)
        out += g.rect(0, 230, 390, 614, '#07162B', 'none', 0, opacity=.30)
        out += g.rect(28, 346, 334, 252, '#FFFFFF', BRAND['line'], 18, extra='filter="url(#shadow)"')
        out += g.circle(195, 402, 26, BRAND['green'])
        out += g.tx(195, 410, '✓', 23, 900, '#FFFFFF', 'middle')
        out += g.tx(195, 454, 'Mã xác minh hợp lệ', 17, 900, BRAND['ink'], 'middle')
        out += g.paragraph(58, 486, 'Nhấn tiếp tục để nhập mật khẩu mới.', 42, 11, BRAND['muted'], 18, 2)
        out += g.btn(52, 534, 286, 'OK, nhập mật khẩu mới', True, 44)
    return out


def final_mobile_post_card(x: float, y: float, w: float, h: float = 494, transcript: bool = False) -> str:
    out = g.rect(x, y, w, h, '#FFFFFF', BRAND['line'], 18)
    out += g.avatar(x + 34, y + 36, 20, 'L', '#FF8B6A', 'online')
    out += g.tx(x + 68, y + 30, 'Linh Nguyễn', 13, 800)
    out += g.tx(x + 68, y + 50, '2 giờ · Bạn bè', 10, 500, BRAND['muted'])
    out += g.tx(x + w - 24, y + 36, '•••', 16, 800, BRAND['muted'], 'middle')
    out += g.paragraph(x + 20, y + 86, 'Một khoảnh khắc nhỏ, nhưng đủ khiến cả ngày trở nên đáng nhớ.', 42, 11, BRAND['ink'], 18, 3)
    media_y = y + 138
    media_h = 236
    out += g.rect(x + 20, media_y, w - 40, media_h, 'url(#media)', 'none', 14)
    out += g.pill(x + 30, media_y + 14, 92, '01:42 · HD', '#07162BCC', '#FFFFFF')
    out += g.circle(x + w/2, media_y + media_h/2, 27, '#FFFFFF', 'none', 1, 'opacity=".92"')
    out += g.tx(x + w/2 + 2, media_y + media_h/2 + 8, '▶', 22, 800, BRAND['primary'], 'middle')
    out += g.icon_button(x + w - 56, media_y + media_h - 42, 'Toàn màn hình', 'F', False, 32)
    row_y = media_y + media_h + 14
    out += g.line(x + 20, row_y, x + w - 20, row_y)
    labels = [('♡','1,2K'),('◯','128'),('↻','45'),('◇','Lưu'),('↗','Chia')]
    step = (w - 40) / len(labels)
    for i, (ic, lab) in enumerate(labels):
        xx = x + 20 + step*i + step/2
        out += g.tx(xx, row_y + 31, ic, 14, 800, BRAND['ink'], 'middle')
        out += g.tx(xx, row_y + 48, lab, 8, 700, BRAND['muted'], 'middle')
    if transcript:
        out += g.rect(x + 20, row_y + 62, w - 40, 52, BRAND['surface2'], 'none', 10)
        out += g.tx(x + 32, row_y + 82, 'Phiên âm', 9, 800, BRAND['primary'])
        out += g.tx(x + 32, row_y + 100, '“Một ý tưởng nhỏ trở thành sản phẩm...”', 8, 500, BRAND['muted'])
    return out


def mobile_rich_editor(sid: str) -> str:
    out = g.mobile_header('Trang chủ')
    out += g.tx(16, 132, 'Tạo bài viết' if sid == 'FEED-02' else 'Chỉnh sửa bài viết', 20, 900)
    out += g.tx(16, 154, 'Định dạng rõ ràng, đẹp và dễ đọc.', 9, 600, BRAND['muted'])
    out += g.rect(12, 174, 366, 584, '#FFFFFF', BRAND['line'], 16)
    out += g.avatar(38, 210, 18, 'M', '#6C5CE7', 'online')
    out += g.tx(68, 208, 'Phạm Minh Sáng', 11, 800)
    out += g.pill(68, 220, 142, 'Bạn bè · Tùy chỉnh', BRAND['surface2'], BRAND['ink'])
    out += g.tx(20, 282, 'ĐỊNH DẠNG CHỮ', 9, 900, BRAND['muted'])
    out += g.rect(20, 298, 350, 94, '#F8FAFC', BRAND['line'], 12)
    out += g.rect(30, 308, 112, 34, '#FFFFFF', BRAND['line'], 8) + g.tx(42, 330, 'Inter  ⌄', 10, 700)
    out += g.rect(150, 308, 72, 34, '#FFFFFF', BRAND['line'], 8) + g.tx(186, 330, '16  ⌄', 10, 700, BRAND['ink'], 'middle')
    controls = [('B', True),('I',False),('U',False),('H1',False),('•',False),('↗',False)]
    xx = 30
    for label, active in controls:
        ww = 42 if label != 'H1' else 48
        out += g.rect(xx, 350, ww, 32, BRAND['primary'] if active else '#FFFFFF', BRAND['primary'] if active else BRAND['line'], 8)
        out += g.tx(xx+ww/2, 372, label, 10, 900, '#FFFFFF' if active else BRAND['ink'], 'middle')
        xx += ww + 8
    out += g.rect(20, 408, 350, 154, '#FFFFFF', BRAND['line'], 12)
    main = 'Hôm nay mình muốn chia sẻ...' if sid == 'FEED-02' else 'Huy và Lưu vừa hoàn thiện bản thiết kế mới...'
    out += g.tx(34, 440, main, 12, 800)
    out += g.tx(34, 468, 'Dòng đậm giúp nhấn ý chính.', 11, 800)
    out += g.tx(34, 496, 'Nội dung thường giữ khoảng cách dễ đọc.', 10, 500, BRAND['muted'])
    out += g.tx(20, 596, 'Ảnh và video', 10, 900, BRAND['muted'])
    out += g.rect(20, 614, 104, 72, 'url(#media)', 'none', 10)
    out += g.rect(134, 614, 104, 72, 'url(#media)', 'none', 10)
    out += g.rect(248, 614, 104, 72, BRAND['surface2'], BRAND['line'], 10)
    out += g.tx(300, 656, '+', 18, 800, BRAND['primary'], 'middle')
    out += g.btn(20, 704, 114, 'Hủy', False, 40)
    out += g.btn(212, 704, 140, 'Đăng bài' if sid == 'FEED-02' else 'Lưu', True, 40)
    return out


def final_mobile_generic(item: dict[str, Any]) -> str:
    sid = item['id']
    if sid == 'FEED-01':
        out = g.mobile_header('Trang chủ')
        out += g.tx(16, 132, 'Bảng tin', 20, 900)
        out += g.sticky_composer(12, 168, 366)
        out += final_mobile_post_card(12, 254, 366, 494, False)
        return out
    if sid in {'FEED-02','FEED-04'}:
        return mobile_rich_editor(sid)
    if sid == 'FEED-03':
        out = g.mobile_header('Trang chủ')
        out += g.rect(0, 102, 390, 680, '#0B1020', 'none', 0, opacity=.35)
        out += g.rect(8, 116, 374, 654, '#FFFFFF', BRAND['line'], 18, extra='filter="url(#shadow)"')
        out += g.tx(24, 148, 'Chi tiết bài viết', 15, 900)
        out += g.tx(360, 148, '×', 18, 800, BRAND['muted'], 'middle')
        out += final_mobile_post_card(18, 166, 354, 448, True)
        out += g.pill(20, 624, 76, 'Mới nhất', BRAND['soft'], BRAND['primary'])
        out += g.pill(104, 624, 62, 'Tất cả', BRAND['surface2'], BRAND['muted'])
        out += g.rect(20, 664, 350, 66, BRAND['surface2'], 'none', 12)
        out += g.tx(34, 686, 'An Trần', 10, 800)
        out += g.tx(34, 710, 'Video hay quá!  ♡ · ↩ · •••', 9, 600, BRAND['ink'])
        return out
    if sid == 'FEED-05':
        out = g.mobile_header('Video')
        out += g.toast(74, 110, 'Đang xử lý dưới nền', 'Có thể rời trang an toàn.', 'success', 300)
        out += g.tx(16, 218, 'Video đang được xử lý', 20, 900)
        out += g.tx(16, 242, 'Tiến trình tiếp tục khi bạn chuyển trang.', 9, 600, BRAND['muted'])
        out += g.rect(12, 266, 366, 486, '#FFFFFF', BRAND['line'], 16)
        out += g.tx(28, 302, '72% · Đang xử lý ở nền', 13, 900, BRAND['primary'])
        out += g.rect(28, 324, 334, 14, '#E8ECF3', 'none', 7)
        out += g.rect(28, 324, 240, 14, 'url(#brand)', 'none', 7)
        out += g.tx(28, 378, 'Chọn ảnh thu nhỏ', 11, 800)
        for i in range(3):
            out += g.rect(28+i*112, 398, 100, 68, 'url(#media)', BRAND['primary'] if i == 1 else BRAND['line'], 9, 3 if i == 1 else 1)
        out += g.btn(28, 488, 190, 'Tải ảnh từ máy', False, 40)
        out += g.tx(28, 548, '☑ Tự động đăng khi xong', 11, 700)
        out += g.tx(28, 582, '☐ Lưu thành bản nháp', 11, 700)
        out += g.tx(28, 616, '☐ Lên lịch đăng', 11, 700)
        out += g.btn(28, 674, 334, 'Đóng và chạy nền', True, 44)
        return out
    return g.mobile_generic(item)


def write_board(path: Path, title: str, body: str, width: int = 1280, height: int = 720) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    svg = g.svg_head(width, height, title) + body + '</svg>\n'
    path.write_text(svg, encoding='utf-8')


def create_final_boards() -> None:
    # Board 1: phản hồi xác thực
    body = g.rect(0,0,1280,720,'#F8FAFC','none',0)
    body += g.tx(42,58,'Phản hồi xác thực · Quy tắc cuối',28,900)
    body += g.tx(42,88,'Toast top-end, kiểm tra mật khẩu theo tiêu chí và modal xác minh OTP.',12,600,BRAND['muted'])
    body += g.section_card(42,126,360,520,'1. Toast top-end','Không che tiêu đề, trường nhập hoặc CTA')
    body += g.toast(72,194,'Đăng nhập thành công','Đang mở Trang chủ.','success',300)
    body += g.toast(72,296,'Mật khẩu chưa đủ mạnh','Bổ sung ký tự đặc biệt.','error',300)
    body += g.tx(72,424,'Vị trí',11,800,BRAND['muted'])
    body += g.tx(72,450,'Desktop và mobile: top-end + safe-area.',12,700)
    body += g.tx(72,482,'Tự đóng sau 5 giây; lỗi có hành động giữ lại.',12,700)
    body += g.section_card(430,126,360,520,'2. Checklist mật khẩu','Không chỉ dùng một thanh “mạnh/yếu”')
    body += g.input_box(460,194,300,'Mật khẩu','Twight2026','bad')
    body += password_rules(460,276,True)
    body += g.tx(460,432,'Mỗi tiêu chí có biểu tượng và mô tả.',12,700)
    body += g.tx(460,462,'Thông báo bằng aria-live khi trạng thái đổi.',12,700)
    body += g.section_card(818,126,420,520,'3. OTP hợp lệ','Modal xác nhận trước khi mở form mới')
    body += g.rect(850,188,356,250,'#FFFFFF',BRAND['line'],18,extra='filter="url(#shadow)"')
    body += g.circle(1028,244,26,BRAND['green'])+g.tx(1028,252,'✓',22,900,'#FFFFFF','middle')
    body += g.tx(1028,296,'Mã xác minh hợp lệ',17,900,BRAND['ink'],'middle')
    body += g.paragraph(890,326,'Nhấn tiếp tục để nhập mật khẩu mới.',42,11,BRAND['muted'],18,2)
    body += g.btn(882,374,292,'OK, nhập mật khẩu mới',True,44)
    body += g.tx(850,482,'Sau OK:',12,900,BRAND['primary'])
    body += g.tx(850,510,'• Modal đóng và focus vào trường mật khẩu mới.',11,700)
    body += g.tx(850,538,'• OTP không còn hiển thị hoặc có thể chỉnh sửa.',11,700)
    body += g.tx(850,566,'• Thành công thu hồi mọi phiên cũ.',11,700)
    write_board(ROOT/'assets/editable/boards/auth-feedback-final.svg','Auth feedback states final',body)

    body = g.rect(0,0,1280,720,'#F8FAFC','none',0)
    body += g.tx(42,58,'PostCard · Hành động dưới phương tiện',28,900)
    body += g.tx(42,88,'Media dùng toàn bộ chiều rộng card; Like, Bình luận và Đăng lại nằm dưới video.',12,600,BRAND['muted'])
    body += final_post_card(42,126,760,520,True,False)
    body += g.section_card(832,126,406,520,'Quy tắc bố cục')
    rules = [
        'Video rộng tối đa trong vùng nội dung.',
        'Ba hành động tương tác chính ở dưới video.',
        'Lưu và Chia sẻ cùng hàng, thứ bậc thấp hơn.',
        'Nút toàn màn hình nằm trên video.',
        'Dấu ba chấm mở báo cáo và tác vụ phụ.',
        'Mobile giữ cùng thứ tự và dùng nhãn ngắn.',
    ]
    for i, rule in enumerate(rules):
        yy=194+i*54
        body += g.circle(862,yy,12,BRAND['soft'])+g.tx(862,yy+5,str(i+1),10,900,BRAND['primary'],'middle')
        body += g.paragraph(886,yy+4,rule,42,11,BRAND['ink'],18,2)
    write_board(ROOT/'assets/editable/boards/post-actions-final.svg','Post action layout final',body)


def clean_and_finalize_screen_docs(feedback: dict[str, Any]) -> None:
    inventory = json.loads((ROOT/'data/screen-inventory.json').read_text(encoding='utf-8'))
    latest = feedback.get('screens', {})
    summaries = {
        'AUTH-02': ['Toast thành công/thất bại neo ở góc trên phải và không che tiêu đề hoặc trường nhập.'],
        'AUTH-03': ['Bổ sung checklist mật khẩu với dấu tích/dấu X cho từng tiêu chí.', 'Toast top-end nêu đúng tiêu chí còn thiếu.'],
        'AUTH-04': ['Toast gửi mã đặt ở góc trên phải, không nằm dưới form.'],
        'AUTH-05': ['Sau khi OTP hợp lệ, hiển thị modal giữa màn hình.', 'Chỉ sau khi chọn OK mới mở form mật khẩu mới; OTP không còn xuất hiện.'],
        'FEED-01': ['Đưa Thích, Bình luận và Đăng lại xuống dưới video.', 'Mở rộng video hết chiều ngang vùng nội dung; Lưu và Chia sẻ ở cùng action bar.'],
        'FEED-02': ['Thiết kế lại thanh rich text theo nhóm Font, Cỡ chữ và Định dạng.', 'Trạng thái in đậm hiển thị rõ cả trên toolbar và nội dung mẫu.'],
        'FEED-03': ['Đưa action bar xuống dưới video, mở rộng vùng media.', 'Tăng chiều rộng cột bình luận và giữ lớp nổi desktop/route toàn màn hình mobile.'],
        'FEED-04': ['Đồng bộ editor với FEED-02; nội dung sửa đổi có typography đậm và dễ nhận biết.'],
        'FEED-05': ['Toast xử lý nền đặt top-end.', 'Tách trạng thái đang xử lý khỏi hướng dẫn phục hồi khi thất bại để tránh mâu thuẫn.'],
    }
    for item in inventory:
        path = ROOT/item['file']
        text = path.read_text(encoding='utf-8')
        meta, body = g.yaml.safe_load(text.split('---\n',2)[1]) if False else ({}, '')
        # parse manually to preserve YAML arrays
        if not text.startswith('---\n'):
            continue
        _, front, body = text.split('---\n',2)
        meta = yaml.safe_load(front) or {}
        meta['status'] = 'approved'
        meta['review_round'] = 3
        meta['approved_at'] = '2026-09-07'
        body = body.lstrip()
        body = re.split(r'\n## Ghi chú duyệt(?: vòng \d+)?\n', body, maxsplit=1)[0].rstrip()
        # Loại các phần review cũ nếu file có cấu trúc khác.
        body = re.split(r'\n## Thay đổi đã áp dụng ở vòng 1\n', body, maxsplit=1)[0].rstrip()
        if item['id'] == 'AUTH-05':
            body = body.replace(
                '- Nhóm 6 ô OTP có thể dán toàn bộ; mật khẩu mới và xác nhận.\n- Hiển thị số lần thử còn lại chỉ khi hợp đồng cho phép.\n- Sau thành công, điều hướng về đăng nhập và thông báo mọi phiên đã bị thu hồi.',
                '- Trạng thái đầu tiên sau khi OTP hợp lệ là modal xác nhận giữa màn hình.\n- Khi chọn **OK, nhập mật khẩu mới**, modal đóng, focus chuyển vào trường mật khẩu mới và OTP không còn hiển thị.\n- Sau thành công, điều hướng về đăng nhập và thông báo mọi phiên đã bị thu hồi.'
            )
            body = body.replace('`OTPInput`\n- `PasswordField`', '`VerificationSuccessModal`\n- `PasswordField`\n- `PasswordCriteriaList`')
        if item['id'] == 'AUTH-03':
            body = body.replace('`PasswordField`', '`PasswordField`\n- `PasswordCriteriaList`', 1)
        if item['id'] in {'FEED-01','FEED-03'}:
            body = body.replace('`ReactionBar`', '`PostActionBar`')
        final_notes = summaries.get(item['id'], ['Thiết kế vòng 2 được duyệt và giữ nguyên sau khi rà soát tính nhất quán desktop/mobile.'])
        raw_feedback = str((latest.get(item['id']) or {}).get('note', '')).strip()
        appendix = '\n\n## Quyết định cuối\n\n- Trạng thái: **Đã duyệt để triển khai Frontend**.\n'
        appendix += '- Phiên bản thiết kế: **1.2 Final**.\n'
        for note in final_notes:
            appendix += f'- {note}\n'
        if raw_feedback:
            appendix += f'- Phản hồi vòng cuối đã xử lý: “{raw_feedback}”\n'
        appendix += '- SVG là nguồn hình chỉnh sửa; PNG chỉ dùng để duyệt.\n'
        appendix += '- Các yêu cầu chưa có hợp đồng Backend phải tuân theo `sources/18-backend-contract-gaps.md`; không tự tạo API.\n'
        dumped = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
        path.write_text('---\n'+dumped+'\n---\n\n'+body+appendix, encoding='utf-8')


def update_sources_and_handoff() -> None:
    replacements = {
        'sources/02-information-architecture.md': [('vòng 2','bản cuối')],
        'sources/06-component-library.md': [('Thư viện component vòng 2','Thư viện component bản cuối'),('`VerticalEngagementRail`','`PostActionBar`')],
        'sources/07-interactions-motion.md': [
            ('Toast xuất hiện góc phải desktop và phía dưới thanh trên trên mobile; không che trường nhập hoặc CTA.',
             'Toast xuất hiện ở vị trí top-end trên cả desktop và mobile, có bù safe-area; không che tiêu đề, trường nhập hoặc CTA.'),
            ('Bài viết chi tiết mở ở layer trên desktop và route toàn màn hình trên mobile.',
             'Bài viết chi tiết mở ở layer trên desktop và route toàn màn hình trên mobile. Thích, Bình luận và Đăng lại luôn nằm dưới phương tiện.')
        ],
        'sources/12-frontend-handoff.md': [('Bàn giao frontend vòng 2','Bàn giao Frontend bản cuối'),('Chỉ tạo `design.md` sau khi toàn bộ màn hình bắt buộc được duyệt.','`design.md` đã được khóa; mọi thay đổi tiếp theo phải cập nhật changelog và chạy lại validator.')],
    }
    for rel, pairs in replacements.items():
        path = ROOT/rel
        text = path.read_text(encoding='utf-8')
        for old, new in pairs:
            text = text.replace(old,new)
        path.write_text(text,encoding='utf-8')

    # Bổ sung quy tắc trạng thái và QA cuối.
    state_path = ROOT/'sources/11-state-matrix.md'
    state = state_path.read_text(encoding='utf-8').rstrip()
    state += '''\n\n## Trạng thái xác thực bổ sung\n\n| Trạng thái | Hiển thị | Hành động |\n|---|---|---|\n| `toast_success` | Toast top-end, không che form | Tự đóng hoặc mở đích an toàn |\n| `password_criteria_invalid` | Dấu X + tiêu chí chưa đạt dưới trường mật khẩu | Giữ dữ liệu, focus tiêu chí đầu tiên chưa đạt |\n| `verification_success` | Modal giữa màn hình, focus bị giữ trong modal | Chọn OK để chuyển sang form mật khẩu mới |\n| `password_reset_ready` | Chỉ hiện mật khẩu mới và xác nhận; không hiện OTP | Đổi mật khẩu một lần, khóa gửi lặp |\n\n## Trạng thái bài viết bổ sung\n\n- Media luôn dùng toàn bộ chiều rộng khả dụng của PostCard.\n- Action bar nằm dưới media theo thứ tự: Thích, Bình luận, Đăng lại, Lưu, Chia sẻ.\n- Khi video xử lý nền, toast top-end chỉ báo tiến trình; lỗi chi tiết nằm trong vùng có nút Thử lại hoặc Lưu bản nháp.\n'''
    state_path.write_text(state+'\n',encoding='utf-8')

    qa_path = ROOT/'sources/16-design-qa.md'
    qa = qa_path.read_text(encoding='utf-8').rstrip()
    qa += '''\n\n## Kiểm tra được bổ sung ở vòng cuối\n\n- Toast top-end không chồng tiêu đề, input, menu hoặc CTA ở 390 px và 1440 px.\n- Checklist mật khẩu có cả biểu tượng, chữ và thông báo `aria-live`; không chỉ dựa vào màu.\n- Modal OTP giữ focus, đóng bằng nút rõ ràng và không để OTP tiếp tục chỉnh sửa sau xác minh.\n- Video không bị thu hẹp để dành action rail; action bar nằm dưới media trên desktop và mobile.\n- Rich text toolbar có nhóm điều khiển, trạng thái active và tên truy cập; không dùng icon mơ hồ không có nhãn.\n- Trạng thái xử lý video và trạng thái thất bại không xuất hiện mâu thuẫn trong cùng một thời điểm.\n'''
    qa_path.write_text(qa+'\n',encoding='utf-8')

    prompt = '''# Prompt triển khai Frontend từ design.md\n\nBạn là Senior Frontend Engineer phụ trách triển khai giao diện **Twight Light**.\n\n## Nguồn chuẩn\n\n1. `design.md`: kiến trúc thông tin, bố cục, component, trạng thái, responsive, accessibility và tiêu chí chấp nhận UI.\n2. OpenAPI/AsyncAPI trong repository: request, response, quyền, mã lỗi và sự kiện.\n3. `AGENTS.md`, `RULES.md` và quy ước repository: cách thay đổi mã nguồn.\n4. `sources/18-backend-contract-gaps.md`: danh sách thiết kế chưa có hợp đồng Backend; không tự tạo endpoint.\n\n## Cách triển khai\n\n- Xác minh framework, phiên bản Angular, cấu trúc thư mục và pattern hiện có trước khi sửa mã.\n- Triển khai theo thứ tự P0 -> P1 -> P2; mỗi task là một vertical slice có route, component, state, adapter API, test và accessibility.\n- Sinh design token từ `tokens/design-tokens.json`; không hard-code màu hoặc spacing đã có token.\n- Desktop dùng mockup 1440 px làm cấu trúc; mobile 390 px là thiết kế responsive độc lập, không chỉ scale nhỏ.\n- Giữ PostCard với media rộng tối đa và action bar nằm dưới media.\n- Toast dùng top-end có safe-area; lỗi cần hành động phải có nội dung bền vững ngoài toast.\n- Mọi form có trạng thái idle, validating, submitting, success, error; khóa gửi lặp và giữ dữ liệu khi lỗi có thể thử lại.\n- Không tin quyền từ UI; xử lý 401/403/404/409/412/422/429/503 theo design.md.\n- Không báo build/test đạt nếu chưa chạy lệnh thật.\n\n## Kết quả mỗi task\n\n- Danh sách route/component/file thay đổi.\n- Hành vi desktop/mobile và trạng thái đã triển khai.\n- Test component/integration/E2E phù hợp.\n- Lệnh format, lint, build, test và kết quả chính xác.\n- Các gap Backend hoặc quyết định còn chặn.\n'''
    (ROOT/'FRONTEND_IMPLEMENTATION_PROMPT.md').write_text(prompt,encoding='utf-8')

    plan = '''# Kế hoạch triển khai Frontend\n\n## Giai đoạn 0 - Nền tảng giao diện\n\n- App shell, route guard, error boundary, token, typography, icon và accessibility primitives.\n- HTTP client, Problem Details mapper, auth refresh coordinator, SignalR adapter và feature flag.\n\n## Giai đoạn 1 - P0\n\n1. Xác thực cơ sở: AUTH-01 đến AUTH-03.\n2. Bảng tin và bài viết: FEED-01 đến FEED-04.\n3. Hồ sơ và thiết lập cơ sở.\n4. Chat, notification và trạng thái hệ thống.\n\n## Giai đoạn 2 - P1\n\n- Khôi phục mật khẩu, xóa tài khoản, cộng đồng, RTC, media, video và điều hành nội dung.\n\n## Giai đoạn 3 - P2\n\n- Marketplace, AI, tóm tắt và các chức năng chỉ được bật khi hợp đồng Backend tương ứng đã khóa.\n\n## Cổng hoàn thành mỗi màn hình\n\n- Route và quyền đúng.\n- Desktop + mobile đúng thứ tự ưu tiên.\n- Loading/empty/error/offline/forbidden được xử lý.\n- Keyboard, focus, aria và độ tương phản đạt.\n- Test tối thiểu cho happy path, validation, authorization và retry/idempotency khi liên quan.\n- Không còn dữ liệu giả nằm trên đường chạy production.\n'''
    (ROOT/'FRONTEND_IMPLEMENTATION_PLAN.md').write_text(plan,encoding='utf-8')

    checklist = '''# Checklist chuyển thiết kế thành mã\n\n- [ ] Đã đọc `design.md` và đặc tả màn hình liên quan.\n- [ ] Đã kiểm tra OpenAPI/AsyncAPI, không suy đoán endpoint.\n- [ ] Đã tái sử dụng token và component hiện có.\n- [ ] Đã triển khai desktop và mobile theo thiết kế, không scale cơ học.\n- [ ] Đã có loading, empty, error, offline và unauthorized khi liên quan.\n- [ ] Toast top-end không che UI; lỗi cần xử lý có bản inline/bền vững.\n- [ ] Focus, keyboard, aria-label, aria-live và reduced-motion đạt.\n- [ ] Đã xử lý hủy request, reconnect và gửi lặp khi liên quan.\n- [ ] Đã chạy format/lint/build/test thật.\n- [ ] Đã đối chiếu screenshot với SVG/PNG nguồn và ghi lại sai khác có chủ đích.\n'''
    (ROOT/'DESIGN_TO_CODE_CHECKLIST.md').write_text(checklist,encoding='utf-8')


def update_approval(feedback: dict[str, Any]) -> None:
    inventory = json.loads((ROOT/'data/screen-inventory.json').read_text(encoding='utf-8'))
    latest = feedback.get('screens', {})
    approval = {
        'version': '1.2-final',
        'updatedAt': '2026-09-07T12:00:00+07:00',
        'status': 'approved_for_frontend',
        'screens': {},
        'shared': {'sources':'approved','tokens':'approved','flows':'approved','boards':'approved'},
    }
    changed = {'AUTH-02','AUTH-03','AUTH-04','AUTH-05','FEED-01','FEED-02','FEED-03','FEED-04','FEED-05'}
    for item in inventory:
        note = 'Đã rà soát và giữ nguyên từ vòng 2.'
        if item['id'] in changed:
            note = 'Đã áp dụng phản hồi vòng cuối và đồng bộ desktop/mobile.'
        raw = str((latest.get(item['id']) or {}).get('note','')).strip()
        if raw:
            note += ' Phản hồi: ' + raw
        approval['screens'][item['id']] = {
            'status':'approved',
            'required': item.get('priority') in {'P0','P1'},
            'note':note,
        }
    (ROOT/'review/feedback-round-2.yaml').write_text(LATEST_FEEDBACK.read_text(encoding='utf-8'),encoding='utf-8')
    (ROOT/'review/approval-status.yaml').write_text(yaml.safe_dump(approval,allow_unicode=True,sort_keys=False),encoding='utf-8')


def update_root_docs() -> None:
    changelog = '''# Lịch sử thiết kế\n\n## 1.2 Final - 07/09/2026\n\n- Áp dụng phản hồi vòng cuối cho AUTH-02 đến AUTH-05 và FEED-01 đến FEED-05.\n- Chuẩn hóa toast ở top-end cho desktop/mobile.\n- Bổ sung checklist mật khẩu theo từng tiêu chí và modal OTP hợp lệ.\n- Chuyển Like/Bình luận/Đăng lại xuống dưới video; media dùng toàn chiều rộng PostCard.\n- Thiết kế lại rich text editor với nhóm Font, Cỡ chữ và Định dạng.\n- Tách trạng thái xử lý video và hướng dẫn khôi phục lỗi.\n- Rà soát, làm sạch Markdown và khóa `design.md` cho Frontend.\n\n## 1.1 Review 2 - 05/09/2026\n\n- Áp dụng phản hồi vòng 1, đổi thương hiệu và dựng 47 màn hình desktop/mobile.\n- Loại màn hình AI-03 độc lập; tích hợp phiên âm vào bài viết và chat.\n'''
    (ROOT/'DESIGN_CHANGELOG.md').write_text(changelog,encoding='utf-8')

    status = '''# Trạng thái bộ thiết kế\n\n- Phiên bản: **1.2 Final**\n- Trạng thái: **Đã khóa để triển khai Frontend**\n- Màn hình hoạt động: **47**\n- Màn hình đã duyệt: **47/47**\n- Khối dùng chung: **sources, tokens, flows, boards đã duyệt**\n- Nguồn tổng hợp: `design.md`\n- Hợp đồng Backend còn thiếu: `sources/18-backend-contract-gaps.md`\n\nMọi thay đổi sau bản này phải cập nhật nguồn Markdown/SVG, `DESIGN_CHANGELOG.md`, approval và chạy lại validator.\n'''
    (ROOT/'STATUS.md').write_text(status,encoding='utf-8')

    readme = '''# Twight Light Frontend Design Kit 1.2 Final\n\nBộ nguồn UI/UX đã khóa để triển khai Frontend cho Twight Light.\n\n## Bắt đầu\n\n1. Đọc `design.md`.\n2. Đọc `FRONTEND_IMPLEMENTATION_PLAN.md`.\n3. Kiểm tra `sources/18-backend-contract-gaps.md` trước khi code một yêu cầu chưa có trong OpenAPI/AsyncAPI.\n4. Dùng SVG trong `assets/editable/` làm nguồn chỉnh sửa; PNG trong `assets/preview/` chỉ dùng để duyệt.\n5. Dùng `tokens/design-tokens.json` làm nguồn token.\n\n## Tệp quan trọng\n\n- `design.md`: nguồn UI/UX tổng hợp cho Frontend.\n- `screens/`: đặc tả từng màn hình.\n- `sources/`: nguyên tắc và hợp đồng trải nghiệm dùng chung.\n- `FRONTEND_IMPLEMENTATION_PROMPT.md`: prompt triển khai.\n- `DESIGN_TO_CODE_CHECKLIST.md`: checklist kiểm tra.\n- `review/FINAL_REVIEW_GALLERY_STANDALONE.html`: gallery ảnh độc lập.\n\n## Kiểm tra\n\n```bash\npython scripts/export_tokens.py\npython scripts/render_svg.py\npython scripts/build_design.py --final\npython scripts/validate_design.py --require-final\n```\n'''
    (ROOT/'README.md').write_text(readme,encoding='utf-8')

    (ROOT/'FEEDBACK_APPLIED.md').write_text('''# Phản hồi đã áp dụng\n\n- Phản hồi vòng 1: `review/feedback-round-1.yaml`.\n- Phản hồi vòng 2/cuối: `review/feedback-round-2.yaml`.\n- Tất cả màn hình được khóa ở trạng thái approved trong `review/approval-status.yaml`.\n- Các yêu cầu mới làm thay đổi hợp đồng Backend vẫn được tách trong `sources/18-backend-contract-gaps.md`.\n''',encoding='utf-8')


def main() -> None:
    feedback = yaml.safe_load(LATEST_FEEDBACK.read_text(encoding='utf-8')) or {}
    inventory = json.loads((ROOT/'data/screen-inventory.json').read_text(encoding='utf-8'))

    # Monkey-patch generator để desktop/mobile cùng dùng quyết định cuối.
    g.auth_scene = final_auth_scene
    g.feed_scene = final_feed_scene
    g.post_card = final_post_card
    g.mobile_auth = final_mobile_auth
    g.mobile_post_card = final_mobile_post_card
    g.mobile_generic = final_mobile_generic

    changed = {'AUTH-02','AUTH-03','AUTH-04','AUTH-05','FEED-01','FEED-02','FEED-03','FEED-04','FEED-05'}
    for item in inventory:
        if item['id'] not in changed:
            continue
        slug = Path(item['file']).stem
        g.write_svg(ROOT/f'assets/editable/svg/desktop/{slug}.svg',1440,1024,f"{item['id']} - {item['title']} - Desktop Final",g.desktop_scene(item),f"{item['id']} · DESKTOP · FINAL 1.2")
        g.write_svg(ROOT/f'assets/editable/svg/mobile/{slug}.svg',390,844,f"{item['id']} - {item['title']} - Mobile Final",g.mobile_scene(item),f"{item['id']} · MOBILE · FINAL 1.2")

    create_final_boards()
    clean_and_finalize_screen_docs(feedback)
    update_sources_and_handoff()
    update_approval(feedback)
    update_root_docs()
    print('Đã áp dụng phản hồi vòng cuối cho UI/UX.')


if __name__ == '__main__':
    main()
