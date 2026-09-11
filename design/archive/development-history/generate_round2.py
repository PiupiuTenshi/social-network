#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
INV_PATH = ROOT / 'data' / 'screen-inventory.json'
FEEDBACK = Path('/mnt/data/approval-status.yaml')

BRAND = {
    'ink': '#0B1020',
    'muted': '#64748B',
    'line': '#DCE3EE',
    'surface': '#FFFFFF',
    'surface2': '#F6F8FC',
    'night': '#07162B',
    'primary': '#6C5CE7',
    'primary2': '#496DFF',
    'cyan': '#1EC8E5',
    'coral': '#FF6B81',
    'green': '#10B981',
    'amber': '#F59E0B',
    'danger': '#EF4444',
    'soft': '#EFEAFF',
    'blueSoft': '#EAF2FF',
}


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def tx(x: float, y: float, text: str, size: int = 14, weight: int = 500,
       color: str | None = None, anchor: str = 'start', cls: str = '') -> str:
    c = color or BRAND['ink']
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{c}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>'


def rect(x: float, y: float, w: float, h: float, fill: str = '#fff', stroke: str = 'none',
         rx: float = 14, sw: float = 1, opacity: float = 1, extra: str = '') -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}" {extra}/>'


def circle(x: float, y: float, r: float, fill: str, stroke: str = 'none', sw: float = 1, extra: str = '') -> str:
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def line(x1: float, y1: float, x2: float, y2: float, color: str = '#DCE3EE', sw: float = 1, extra: str = '') -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" {extra}/>'


def pill(x: float, y: float, w: float, label: str, fill: str = '#EFEAFF', color: str = '#5B4AD1') -> str:
    return rect(x, y, w, 28, fill, 'none', 14) + tx(x + w / 2, y + 19, label, 11, 700, color, 'middle')


def btn(x: float, y: float, w: float, label: str, primary: bool = True, h: float = 40, icon: str = '') -> str:
    fill = 'url(#brand)' if primary else '#FFFFFF'
    stroke = 'none' if primary else BRAND['line']
    color = '#FFFFFF' if primary else BRAND['ink']
    text = f'{icon} {label}'.strip()
    return rect(x, y, w, h, fill, stroke, 12, 1, extra='filter="url(#tinyShadow)"' if primary else '') + tx(x + w / 2, y + h / 2 + 5, text, 13, 700, color, 'middle')


def input_box(x: float, y: float, w: float, label: str, value: str = '', valid: str = '', h: float = 46) -> str:
    out = tx(x, y - 8, label, 11, 700, BRAND['muted'])
    out += rect(x, y, w, h, '#FFFFFF', BRAND['line'], 12)
    out += tx(x + 14, y + h / 2 + 5, value or f'Nhập {label.lower()}', 13, 500, BRAND['ink'] if value else '#94A3B8')
    if valid:
        col = BRAND['green'] if valid == 'ok' else BRAND['danger']
        sym = '✓' if valid == 'ok' else '×'
        out += circle(x + w - 22, y + h / 2, 11, col) + tx(x + w - 22, y + h / 2 + 5, sym, 13, 800, '#FFFFFF', 'middle')
    return out


def toast(x: float, y: float, title: str, body: str, kind: str = 'success', w: float = 300) -> str:
    c = BRAND['green'] if kind == 'success' else BRAND['danger'] if kind == 'error' else BRAND['amber']
    out = rect(x, y, w, 82, '#FFFFFF', BRAND['line'], 14, extra='filter="url(#shadow)"')
    out += rect(x, y, 5, 82, c, c, 3)
    out += circle(x + 28, y + 27, 13, c)
    out += tx(x + 28, y + 32, '✓' if kind == 'success' else '!', 13, 800, '#FFFFFF', 'middle')
    out += tx(x + 49, y + 27, title, 13, 800)
    out += tx(x + 49, y + 50, body, 11, 500, BRAND['muted'])
    out += tx(x + w - 18, y + 24, '×', 16, 700, BRAND['muted'], 'middle')
    return out


def avatar(x: float, y: float, r: float = 20, label: str = 'M', color: str = '#6C5CE7', status: str = '') -> str:
    out = circle(x, y, r, color)
    out += circle(x, y - r * .22, r * .28, '#FFE0CC')
    out += f'<path d="M {x-r*.52} {y+r*.48} Q {x} {y-r*.05} {x+r*.52} {y+r*.48} Z" fill="#FFFFFF" opacity=".95"/>'
    if status:
        s = BRAND['green'] if status == 'online' else '#94A3B8'
        out += circle(x + r * .74, y + r * .72, max(4, r * .22), s, '#FFFFFF', 2)
    return out


def icon_button(x: float, y: float, label: str, symbol: str, active: bool = False, size: float = 38) -> str:
    fill = BRAND['soft'] if active else '#FFFFFF'
    stroke = BRAND['primary'] if active else BRAND['line']
    out = rect(x, y, size, size, fill, stroke, 11)
    out += tx(x + size / 2, y + size / 2 + 5, symbol, 16, 700, BRAND['primary'] if active else BRAND['ink'], 'middle')
    return out


def wrap_text(text: str, width_chars: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur: list[str] = []
    for word in words:
        trial = ' '.join(cur + [word])
        if len(trial) <= width_chars or not cur:
            cur.append(word)
        else:
            lines.append(' '.join(cur))
            cur = [word]
    if cur:
        lines.append(' '.join(cur))
    return lines


def paragraph(x: float, y: float, text: str, width_chars: int = 55, size: int = 13,
              color: str | None = None, leading: int = 20, max_lines: int = 5) -> str:
    out = ''
    for i, row in enumerate(wrap_text(text, width_chars)[:max_lines]):
        out += tx(x, y + i * leading, row, size, 500, color or BRAND['muted'])
    return out


def svg_head(width: int, height: int, title: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{esc(title)}</title><desc id="desc">Twight Light UI/UX vòng duyệt 2, SVG chỉnh sửa được.</desc>
<defs>
  <linearGradient id="brand" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6C5CE7"/><stop offset="1" stop-color="#496DFF"/></linearGradient>
  <linearGradient id="twilight" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07162B"/><stop offset=".58" stop-color="#2B245B"/><stop offset="1" stop-color="#E05A78"/></linearGradient>
  <linearGradient id="media" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#73B8FF"/><stop offset=".5" stop-color="#7C62E5"/><stop offset="1" stop-color="#FF9A8B"/></linearGradient>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#07162B" flood-opacity=".14"/></filter>
  <filter id="tinyShadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#07162B" flood-opacity=".12"/></filter>
  <style>
    text {{ font-family: Inter, "Be Vietnam Pro", "DejaVu Sans", Arial, sans-serif; }}
    .small {{ letter-spacing:.02em; }}
  </style>
</defs>'''


def avatar_menu(x: float, y: float) -> str:
    out = rect(x, y, 248, 274, '#FFFFFF', BRAND['line'], 16, extra='filter="url(#shadow)"')
    out += avatar(x + 34, y + 38, 20, 'M', '#6C5CE7', 'online')
    out += tx(x + 64, y + 34, 'Phạm Minh Sáng', 13, 800)
    out += tx(x + 64, y + 53, '@minhsang', 11, 500, BRAND['muted'])
    out += line(x + 16, y + 72, x + 232, y + 72)
    items = [('P', 'Trang cá nhân'), ('S', 'Cài đặt'), ('L', 'Ngôn ngữ'), ('D', 'Sáng / tối'), ('O', 'Đăng xuất')]
    for i, (ic, lab) in enumerate(items):
        yy = y + 91 + i * 36
        out += tx(x + 24, yy + 6, ic, 14, 700, BRAND['primary'])
        out += tx(x + 52, yy + 6, lab, 13, 600)
    return out


def global_header(active: str = 'Trang chủ', show_menu: bool = False, width: int = 1440) -> str:
    out = rect(0, 0, width, 74, '#FFFFFF', BRAND['line'], 0)
    out += rect(22, 15, 44, 44, 'url(#brand)', 'none', 12)
    out += tx(44, 45, 'T', 19, 900, '#FFFFFF', 'middle')
    out += tx(78, 34, 'Twight Light', 17, 900)
    out += tx(78, 52, 'Multi Social Comunity', 10, 600, BRAND['muted'])
    tabs = [('Trang chủ', 270), ('Video', 375), ('Mua bán', 458), ('Cộng đồng', 557)]
    for lab, x in tabs:
        active_here = lab == active
        out += tx(x, 42, lab, 13, 800 if active_here else 600, BRAND['primary'] if active_here else BRAND['muted'], 'middle')
        if active_here:
            out += rect(x - 30, 67, 60, 3, BRAND['primary'], 'none', 2)
    out += rect(706, 17, 380, 40, BRAND['surface2'], BRAND['line'], 20)
    out += tx(730, 43, 'Tìm', 11, 800, BRAND['muted'])
    out += tx(770, 43, 'người, bài viết, cộng đồng...', 12, 500, '#94A3B8')
    out += icon_button(1112, 18, 'Tin nhắn', 'C')
    out += icon_button(1158, 18, 'Thông báo', 'N')
    out += icon_button(1204, 18, 'Trợ lý', 'AI')
    out += avatar(1306, 37, 22, 'M', '#6C5CE7', 'online')
    out += tx(1340, 42, '⌄', 16, 800, BRAND['muted'])
    if show_menu:
        out += avatar_menu(1165, 68)
    return out


def shortcut_rail(active: str = '', y: int = 74, height: int = 950) -> str:
    out = rect(0, y, 224, height, '#FFFFFF', BRAND['line'], 0)
    out += tx(22, y + 34, 'LỐI TẮT CỦA BẠN', 10, 800, BRAND['muted'])
    items = [('Nhóm thiết kế', 'N'), ('Bạn bè', 'B'), ('Bài đã lưu', 'L'), ('Video đã xem', 'V'), ('Backend .NET', 'D'), ('Blockchain', 'K')]
    for i, (lab, ic) in enumerate(items):
        yy = y + 52 + i * 49
        selected = lab == active
        if selected:
            out += rect(12, yy, 200, 40, BRAND['soft'], 'none', 10)
        out += rect(22, yy + 5, 30, 30, BRAND['blueSoft'] if not selected else BRAND['primary'], 'none', 9)
        out += tx(37, yy + 25, ic, 13, 800, '#FFFFFF' if selected else BRAND['primary'], 'middle')
        out += tx(64, yy + 25, lab, 12, 700 if selected else 600, BRAND['ink'])
    out += line(18, y + 364, 206, y + 364)
    out += tx(22, y + 394, '+ Thêm tiện ích', 12, 800, BRAND['primary'])
    out += tx(22, y + 425, 'Sắp xếp và ghim các mục', 10, 500, BRAND['muted'])
    out += tx(22, y + 442, 'bạn dùng thường xuyên.', 10, 500, BRAND['muted'])
    return out


def app_shell(active: str, show_menu: bool = False, rail: bool = True) -> str:
    out = rect(0, 0, 1440, 1024, BRAND['surface2'], 'none', 0)
    out += global_header(active, show_menu)
    if rail:
        out += shortcut_rail()
    return out


def sticky_composer(x: float, y: float, w: float) -> str:
    out = rect(x, y, w, 72, '#FFFFFF', BRAND['line'], 16, extra='filter="url(#tinyShadow)"')
    out += avatar(x + 36, y + 36, 20, 'M', '#6C5CE7', 'online')
    out += rect(x + 68, y + 15, w - 88, 42, BRAND['surface2'], BRAND['line'], 21)
    out += tx(x + 88, y + 42, 'Bạn đang nghĩ gì?', 13, 600, '#7C8798')
    out += tx(x + w - 42, y + 42, '+', 19, 700, BRAND['primary'], 'middle')
    return out


def post_card(x: float, y: float, w: float, h: float = 470, video: bool = True, transcript: bool = False) -> str:
    out = rect(x, y, w, h, '#FFFFFF', BRAND['line'], 18, extra='filter="url(#tinyShadow)"')
    out += avatar(x + 38, y + 38, 21, 'L', '#FF8B6A', 'online')
    out += tx(x + 70, y + 32, 'Linh Nguyễn', 14, 800)
    out += tx(x + 70, y + 52, '2 giờ · Bạn bè', 11, 500, BRAND['muted'])
    out += tx(x + w - 30, y + 39, '•••', 18, 800, BRAND['muted'], 'middle')
    out += tx(x + 22, y + 90, 'Một khoảnh khắc nhỏ, nhưng đủ khiến cả ngày trở nên đáng nhớ.', 13, 600)
    media_y = y + 110
    media_h = 252 if video else 190
    out += rect(x + 22, media_y, w - 86, media_h, 'url(#media)', 'none', 16)
    out += circle(x + (w - 42) / 2, media_y + media_h / 2, 31, '#FFFFFF', 'none', 1, 'opacity=".92"')
    out += tx(x + (w - 42) / 2 + 2, media_y + media_h / 2 + 8, '▶', 24, 800, BRAND['primary'], 'middle')
    out += pill(x + 34, media_y + 18, 94, '01:42 · HD', '#07162BCC', '#FFFFFF')
    out += icon_button(x + w - 54, media_y + media_h - 44, 'Toàn màn hình', 'F', False, 34)
    # action rail on right
    action_x = x + w - 48
    actions = [('♡', '1,2K'), ('◯', '128'), ('↻', '45')]
    for i, (ic, count) in enumerate(actions):
        yy = media_y + 26 + i * 68
        out += circle(action_x, yy, 19, BRAND['surface2'], BRAND['line'])
        out += tx(action_x, yy + 6, ic, 16, 700, BRAND['ink'], 'middle')
        out += tx(action_x, yy + 36, count, 10, 700, BRAND['muted'], 'middle')
    out += line(x + 22, media_y + media_h + 16, x + w - 22, media_y + media_h + 16)
    out += tx(x + 24, media_y + media_h + 45, '◇ Lưu', 12, 700, BRAND['ink'])
    out += tx(x + 104, media_y + media_h + 45, '↗ Chia sẻ', 12, 700, BRAND['ink'])
    if transcript:
        out += rect(x + 22, media_y + media_h + 60, w - 44, 54, BRAND['surface2'], 'none', 10)
        out += tx(x + 36, media_y + media_h + 82, 'Phiên âm', 11, 800, BRAND['primary'])
        out += tx(x + 36, media_y + media_h + 101, '“Hôm nay mình muốn kể về cách một ý tưởng nhỏ trở thành sản phẩm...”', 11, 500, BRAND['muted'])
    return out


def section_card(x: float, y: float, w: float, h: float, title: str, subtitle: str = '') -> str:
    out = rect(x, y, w, h, '#FFFFFF', BRAND['line'], 16, extra='filter="url(#tinyShadow)"')
    out += tx(x + 20, y + 32, title, 15, 800)
    if subtitle:
        out += tx(x + 20, y + 52, subtitle, 11, 500, BRAND['muted'])
    return out


def screen_title(x: float, y: float, title: str, subtitle: str = '') -> str:
    out = tx(x, y, title, 26, 900)
    if subtitle:
        out += tx(x, y + 26, subtitle, 12, 500, BRAND['muted'])
    return out


def auth_scene(item: dict[str, Any]) -> str:
    sid = item['id']
    out = rect(0, 0, 1440, 1024, BRAND['surface2'], 'none', 0)
    out += rect(0, 0, 780, 1024, 'url(#twilight)', 'none', 0)
    out += rect(34, 30, 46, 46, 'url(#brand)', 'none', 13)
    out += tx(57, 61, 'T', 20, 900, '#FFFFFF', 'middle')
    out += tx(94, 50, 'Twight Light', 18, 900, '#FFFFFF')
    out += tx(94, 68, 'Multi Social Comunity', 11, 600, '#D8DAFF')
    # animated avatar field concept
    paths = [
        'M80 250 C210 120 400 380 680 170',
        'M50 500 C280 650 380 300 720 520',
        'M120 810 C300 630 490 920 690 700',
        'M130 140 C300 330 520 40 730 260',
    ]
    for i, d in enumerate(paths):
        out += f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="2" stroke-dasharray="7 12"><animate attributeName="stroke-dashoffset" from="0" to="-38" dur="{5+i}s" repeatCount="indefinite"/></path>'
    avs = [(130,220,'A','#F97376'),(330,160,'B','#6C5CE7'),(550,290,'C','#22C1C3'),(210,485,'D','#F59E0B'),(480,520,'E','#EC4899'),(650,420,'F','#3B82F6'),(130,760,'G','#10B981'),(380,820,'H','#8B5CF6'),(630,735,'I','#F97316')]
    for i,(x,y,l,c) in enumerate(avs):
        out += avatar(x,y,35,l,c,'online' if i%3==0 else '')
        out += f'<animateTransform href="#nothing" attributeName="transform" type="translate" values="0 0; {8 if i%2==0 else -7} {-6 if i%3==0 else 7}; 0 0" dur="{3.8+i*.27}s" repeatCount="indefinite"/>'
    out += tx(74, 875, 'One human, boring!!!', 26, 800, '#FFFFFF')
    out += tx(74, 910, 'One million humans, Nice, very nice', 28, 900, '#FFFFFF')
    out += tx(74, 944, 'Kết nối cá tính. Khám phá cộng đồng. Tạo nên điều đáng nhớ.', 13, 600, '#DDE1FF')

    form_x, form_y, form_w = 890, 146, 420
    title_map = {
        'AUTH-01': ('Chào mừng đến với Twight Light', 'Một không gian đa cộng đồng, đúng chất của bạn.'),
        'AUTH-02': ('Chào mừng trở lại', 'Tiếp tục câu chuyện và những kết nối đang chờ bạn.'),
        'AUTH-03': ('Tạo tài khoản của bạn', 'Chỉ vài bước để bước vào hàng triệu câu chuyện.'),
        'AUTH-04': ('Khôi phục quyền truy cập', 'Nhập email để nhận mã xác minh an toàn.'),
        'AUTH-05': ('Tạo mật khẩu mới', 'Mã xác minh đã đúng. Hãy đặt mật khẩu mới cho tài khoản.'),
    }
    title, sub = title_map[sid]
    out += tx(form_x, form_y, title, 29, 900)
    out += paragraph(form_x, form_y + 34, sub, 53, 13, BRAND['muted'], 20, 2)

    if sid == 'AUTH-01':
        out += section_card(form_x, form_y + 100, form_w, 270, 'Bắt đầu theo cách của bạn', 'Một tài khoản mở ra mọi không gian.')
        out += btn(form_x + 22, form_y + 170, form_w - 44, 'Đăng ký miễn phí', True, 48)
        out += btn(form_x + 22, form_y + 230, form_w - 44, 'Đăng nhập', False, 48)
        out += line(form_x + 22, form_y + 300, form_x + form_w - 22, form_y + 300)
        out += tx(form_x + 22, form_y + 332, '✓ Cá nhân hóa bảng tin', 12, 700, BRAND['green'])
        out += tx(form_x + 214, form_y + 332, '✓ Tham gia cộng đồng', 12, 700, BRAND['green'])
        out += btn(form_x, form_y + 395, form_w, 'Khám phá Twight Light', True, 52)
    elif sid == 'AUTH-02':
        out += input_box(form_x, form_y + 120, form_w, 'Email hoặc tên người dùng', 'minhsang@example.com', 'ok')
        out += input_box(form_x, form_y + 198, form_w, 'Mật khẩu', '••••••••••')
        out += tx(form_x, form_y + 278, '☐ Ghi nhớ đăng nhập', 12, 600, BRAND['muted'])
        out += tx(form_x + form_w, form_y + 278, 'Quên mật khẩu?', 12, 700, BRAND['primary'], 'end')
        out += btn(form_x, form_y + 306, form_w, 'Đăng nhập', True, 50)
        out += btn(form_x, form_y + 370, form_w, 'Tiếp tục với Google', False, 48)
        out += toast(1090, 62, 'Đăng nhập thành công', 'Đang đưa bạn về Trang chủ.', 'success', 320)
    elif sid == 'AUTH-03':
        out += input_box(form_x, form_y + 95, form_w, 'Tên người dùng', 'minhsang', 'ok')
        out += input_box(form_x, form_y + 167, form_w, 'Email', 'minhsang@example.com', 'ok')
        out += input_box(form_x, form_y + 239, form_w, 'Mật khẩu', '••••••••••', 'ok')
        out += input_box(form_x, form_y + 311, form_w, 'Xác nhận mật khẩu', '•••••••', 'bad')
        out += tx(form_x, form_y + 390, 'Mật khẩu xác nhận chưa khớp.', 11, 600, BRAND['danger'])
        out += btn(form_x, form_y + 414, form_w, 'Tạo tài khoản', True, 50)
        out += toast(1080, 62, 'Kiểm tra thông tin', 'Một trường vẫn chưa hợp lệ.', 'error', 330)
    elif sid == 'AUTH-04':
        out += input_box(form_x, form_y + 130, form_w, 'Email', 'minhsang@example.com', 'ok')
        out += btn(form_x, form_y + 212, form_w, 'Gửi mã xác minh', True, 50)
        out += tx(form_x, form_y + 292, 'Bạn sẽ nhận mã 6 chữ số có hiệu lực trong 10 phút.', 12, 500, BRAND['muted'])
        out += tx(form_x, form_y + 326, '← Quay lại đăng nhập', 12, 700, BRAND['primary'])
        out += toast(1080, 62, 'Đã gửi mã', 'Hãy kiểm tra hộp thư của bạn.', 'success', 330)
    elif sid == 'AUTH-05':
        out += pill(form_x, form_y + 95, 188, '✓ Mã xác minh hợp lệ', '#DCFCE7', '#15803D')
        out += input_box(form_x, form_y + 150, form_w, 'Mật khẩu mới', '••••••••••', 'ok')
        out += input_box(form_x, form_y + 230, form_w, 'Xác nhận mật khẩu mới', '••••••••••', 'ok')
        out += paragraph(form_x, form_y + 312, 'Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt.', 55, 11, BRAND['muted'], 18, 2)
        out += btn(form_x, form_y + 365, form_w, 'Đổi mật khẩu', True, 50)
        out += toast(1080, 62, 'Mật khẩu đã được đổi', 'Tất cả phiên cũ đã đăng xuất.', 'success', 330)
    return out


def feed_scene(item: dict[str, Any]) -> str:
    sid = item['id']
    out = app_shell('Video' if sid == 'FEED-05' else 'Trang chủ', show_menu=False)
    if sid == 'FEED-01':
        out += sticky_composer(252, 94, 760)
        out += post_card(252, 184, 760, 510, True, False)
        out += section_card(1036, 94, 370, 236, 'Khám phá theo nhịp của bạn', 'Gợi ý mới cho hôm nay')
        for i,(lab,c) in enumerate([('Công nghệ','#EAF2FF'),('Âm nhạc','#FDF2F8'),('Du lịch','#ECFDF5')]):
            out += pill(1058 + (i%2)*150, 164 + (i//2)*44, 130, lab, c, BRAND['ink'])
        out += section_card(1036, 350, 370, 250, 'Người bạn có thể biết', 'Ưu tiên kết nối liên quan')
        for i,n in enumerate(['An Trần','Lê Vân','Phạm Thư']):
            yy=418+i*55
            out += avatar(1064,yy,18,n[0],['#F97376','#10B981','#3B82F6'][i], 'online' if i==0 else '')
            out += tx(1092,yy-2,n,12,800)
            out += tx(1092,yy+16,'Có 8 bạn chung',10,500,BRAND['muted'])
            out += tx(1374,yy+4,'Theo dõi',11,800,BRAND['primary'],'end')
        out += avatar_menu(1154, 68)
    elif sid in {'FEED-02','FEED-04'}:
        title = 'Tạo bài viết' if sid=='FEED-02' else 'Chỉnh sửa bài viết'
        out += screen_title(258, 118, title, 'Biến suy nghĩ thành một bài viết giàu cảm xúc và dễ tiếp cận.')
        out += section_card(258, 170, 790, 730, 'Nội dung bài viết')
        out += avatar(292, 220, 22, 'M', '#6C5CE7', 'online')
        out += tx(326, 216, 'Phạm Minh Sáng', 13, 800)
        out += pill(326, 228, 134, 'Bạn bè và tùy chỉnh', '#F1F5F9', BRAND['ink'])
        out += tx(278, 292, 'Định dạng', 11, 800, BRAND['muted'])
        tools=['B','I','U','S','H1','H2','•','1.','↗','☺']
        for i,t in enumerate(tools): out += icon_button(278+i*46,310,t,t,active=i in {0,4},size=36)
        out += rect(278, 364, 750, 210, '#FFFFFF', BRAND['line'], 12)
        body = 'Hôm nay mình muốn chia sẻ một điều thú vị...' if sid=='FEED-02' else 'Huy và Lưu vừa hoàn thiện một bản thiết kế mới...'
        out += paragraph(296, 396, body, 72, 14, BRAND['ink'], 23, 4)
        out += tx(1008, 550, '248 / 5.000', 10, 600, BRAND['muted'], 'end')
        out += tx(278, 616, 'Ảnh và video', 11, 800, BRAND['muted'])
        for i in range(3):
            out += rect(278+i*150, 636, 134, 98, 'url(#media)' if i<2 else BRAND['surface2'], BRAND['line'], 12)
            if i==2: out += tx(345+i*150, 691, '+ Thêm', 13, 800, BRAND['primary'], 'middle')
        out += line(278, 760, 1028, 760)
        out += btn(278, 790, 130, 'Hủy', False, 44)
        out += btn(868, 790, 160, 'Đăng bài' if sid=='FEED-02' else 'Lưu thay đổi', True, 44)
        out += section_card(1070, 170, 336, 375, 'Phạm vi hiển thị', 'Chọn đúng nhóm người xem')
        opts=['Tất cả mọi người','Bạn bè','Chỉ mình tôi','Tùy chỉnh']
        for i,o in enumerate(opts):
            yy=232+i*62
            out += circle(1100,yy,9,'#FFFFFF',BRAND['primary'],2)
            if (sid=='FEED-02' and i==3) or (sid=='FEED-04' and i==1): out += circle(1100,yy,5,BRAND['primary'])
            out += tx(1122,yy+5,o,12,700)
            if i==3: out += tx(1122,yy+22,'Chọn danh sách hoặc loại trừ người xem',10,500,BRAND['muted'])
    elif sid == 'FEED-03':
        # elevated modal layer
        out += rect(224, 74, 1216, 950, '#0B1020', 'none', 0, opacity=.38)
        out += rect(316, 98, 930, 860, '#FFFFFF', BRAND['line'], 22, extra='filter="url(#shadow)"')
        out += tx(350, 138, 'Chi tiết bài viết', 20, 900)
        out += tx(1208, 138, '×', 22, 700, BRAND['muted'], 'middle')
        out += post_card(350, 166, 610, 500, True, True)
        out += tx(988, 182, 'Bình luận', 16, 900)
        for i,(lab,w) in enumerate([('Mới nhất',78),('Tất cả',62),('Cũ nhất',70)]):
            out += pill(988+sum(v for _,v in [('Mới nhất',78),('Tất cả',62),('Cũ nhất',70)][:i])+i*8, 202, w, lab, BRAND['soft'] if i==0 else BRAND['surface2'], BRAND['primary'] if i==0 else BRAND['muted'])
        comments=[('An Trần','Đoạn video hay quá!','12 phút'),('Lê Vân','Mình cũng từng gặp trải nghiệm tương tự.','28 phút'),('Huy Đỗ','Cảm ơn bạn đã chia sẻ.','1 giờ')]
        for i,(n,c,t) in enumerate(comments):
            yy=270+i*122
            out += avatar(1010,yy,18,n[0],['#F97376','#10B981','#3B82F6'][i])
            out += rect(1038,yy-24,170,66,BRAND['surface2'],'none',12)
            out += tx(1050,yy-4,n,11,800)
            out += paragraph(1050,yy+15,c,24,10,BRAND['ink'],15,2)
            out += tx(1040,yy+62,f'♡ Thích  ·  ↩ Trả lời  ·  ••• Báo cáo  ·  {t}',9,600,BRAND['muted'])
        out += btn(988, 650, 220, 'Hiển thị thêm bình luận', False, 40)
        out += rect(988, 710, 220, 90, '#FFFFFF', BRAND['line'], 14)
        out += tx(1002, 738, 'Viết bình luận...', 11, 500, '#94A3B8')
        out += btn(1092, 752, 100, 'Gửi', True, 34)
    elif sid == 'FEED-05':
        out += screen_title(258, 118, 'Video của bạn đang được xử lý', 'Bạn có thể rời trang; tiến trình tiếp tục chạy ở nền.')
        out += section_card(258, 170, 790, 610, 'Trạng thái xử lý', 'Video “Một ngày cùng đội dự án”')
        out += rect(282, 232, 742, 18, '#E8ECF3', 'none', 9)
        out += rect(282, 232, 534, 18, 'url(#brand)', 'none', 9)
        out += tx(282, 278, '72% · Đang tạo nhiều độ phân giải và ảnh thu nhỏ', 12, 800, BRAND['primary'])
        out += tx(1008, 278, 'Khoảng 2 phút', 11, 600, BRAND['muted'], 'end')
        out += tx(282, 330, 'Chọn ảnh thu nhỏ', 13, 800)
        for i in range(4):
            out += rect(282+i*178, 352, 160, 104, 'url(#media)', BRAND['primary'] if i==1 else BRAND['line'], 12, 3 if i==1 else 1)
            out += pill(292+i*178, 362, 58, 'Khung '+str(i+1), '#07162BCC', '#FFFFFF')
        out += btn(282, 478, 188, 'Tải ảnh từ máy', False, 42)
        out += tx(282, 556, 'Sau khi hoàn tất', 13, 800)
        out += tx(282, 588, '☑ Tự động đăng theo phạm vi đã chọn', 12, 600)
        out += tx(282, 620, '☐ Lưu thành bản nháp để xem lại', 12, 600)
        out += tx(282, 652, '☐ Lên lịch đăng lúc 20:30 hôm nay', 12, 600)
        out += btn(844, 704, 180, 'Đóng và chạy nền', True, 44)
        out += toast(1068, 190, 'Xử lý thất bại', 'Âm thanh không hợp lệ. Sửa và thử lại.', 'error', 334)
        out += section_card(1068, 294, 334, 264, 'Dashboard video', 'Số liệu sẽ mở sau khi đăng')
        stats=[('Lượt xem','—'),('Lượt thích','—'),('Chia sẻ','—'),('Thời gian đăng','20:30')]
        for i,(a,b) in enumerate(stats):
            yy=354+i*46
            out += tx(1090,yy,a,11,600,BRAND['muted'])+tx(1374,yy,b,12,800,BRAND['ink'],'end')
    return out


def profile_scene(item: dict[str, Any]) -> str:
    sid=item['id']
    out=app_shell('Trang chủ',show_menu=(sid=='PROF-01'))
    if sid in {'PROF-01','PROF-02'}:
        out += rect(250,94,1158,230,'url(#twilight)','none',22)
        out += btn(1220,112,158,'Cửa hàng',False,40,'V') if sid=='PROF-01' else btn(1210,112,168,'Theo dõi',True,40)
        out += avatar(342,300,68,'M' if sid=='PROF-01' else 'A','#6C5CE7','online')
        out += rect(388,260,104,44,'#FFFFFF',BRAND['line'],18,extra='filter="url(#tinyShadow)"')
        out += tx(440,287,'☁ Đang vui',11,800,BRAND['primary'],'middle')
        name='Phạm Minh Sáng (Sáng)' if sid=='PROF-01' else 'An Trần (Annie)'
        out += tx(432,350,name,24,900)
        out += tx(432,376,'@minhsang · TP. Hồ Chí Minh' if sid=='PROF-01' else '@annie · Đà Nẵng',12,600,BRAND['muted'])
        out += tx(432,410,'245 bài viết   ·   3,4K người theo dõi   ·   486 đang theo dõi',12,700)
        if sid=='PROF-01':
            out += btn(1184,342,194,'Chỉnh sửa hồ sơ',False,42)
        else:
            out += btn(1100,342,134,'Nhắn tin',False,42)+btn(1246,342,132,'•••',False,42)
        out += section_card(250,448,760,468,'Bài viết','Nội dung mới nhất từ hồ sơ')
        out += post_card(272,504,716,385,False,False)
        out += section_card(1034,448,374,172,'Đang phát trên Spotify','Âm nhạc gắn với hồ sơ')
        out += rect(1056,500,74,74,'url(#media)','none',12)
        out += tx(1148,524,'Night Changes',13,800)
        out += tx(1148,548,'One Direction',11,600,BRAND['muted'])
        out += tx(1372,548,'▶',20,800,BRAND['primary'],'end')
        out += section_card(1034,640,374,276,'Thông tin cá nhân','Chỉ hiển thị theo quyền riêng tư')
        infos=[('Công việc','Backend .NET Developer'),('Học vấn','Công nghệ thông tin'),('Quê quán','Bình Định'),('Ngày tham gia','09/2026')]
        for i,(a,b) in enumerate(infos):
            yy=704+i*46;out += tx(1056,yy,a,10,700,BRAND['muted'])+tx(1378,yy,b,11,700,BRAND['ink'],'end')
    elif sid=='PROF-03':
        out += screen_title(258,118,'Chỉnh sửa hồ sơ','Tạo một hồ sơ phản ánh đúng bạn, với quyền riêng tư rõ ràng.')
        out += section_card(258,170,1148,744,'Hồ sơ công khai')
        out += rect(282,224,1100,150,'url(#twilight)','none',16)
        out += btn(1200,244,160,'Đổi ảnh bìa',False,38)
        out += avatar(360,374,60,'M','#6C5CE7','online')
        out += btn(430,350,150,'Đổi ảnh đại diện',False,38)
        out += input_box(282,448,330,'Tên hiển thị','Phạm Minh Sáng','ok')
        out += input_box(632,448,330,'Biệt danh','Sáng')
        out += input_box(982,448,380,'Tâm trạng','Đang vui · ☁')
        out += input_box(282,532,520,'Email bắt buộc','minhsang@example.com','ok')
        out += input_box(842,532,520,'Số điện thoại bắt buộc','0901 234 567','ok')
        out += tx(282,620,'Thông tin chi tiết',13,800)
        fields=[('Công việc','Lập trình viên'),('Học vấn','Đại học'),('Tỉnh/Thành phố','TP. Hồ Chí Minh'),('Tình trạng','Độc thân')]
        for i,(a,b) in enumerate(fields):
            xx=282+(i%2)*560; yy=654+(i//2)*82
            out += input_box(xx,yy,520,a,b)
            out += tx(xx+494,yy+29,'⌄',13,800,BRAND['muted'],'middle')
        out += btn(282,836,126,'Hủy',False,44)+btn(1192,836,170,'Lưu thay đổi',True,44)
        out += tx(1078,896,'Hiệu ứng hồ sơ lấy cảm hứng từ thẻ hồ sơ Discord.',10,600,BRAND['muted'])
    elif sid=='PROF-04':
        out += screen_title(258,118,'Kết nối của bạn','Quản lý người theo dõi, đang theo dõi và trạng thái hoạt động.')
        out += section_card(258,170,1148,700,'Mạng lưới kết nối')
        out += pill(282,222,132,'Người theo dõi',BRAND['soft'],BRAND['primary'])
        out += pill(424,222,132,'Đang theo dõi',BRAND['surface2'],BRAND['muted'])
        out += pill(566,222,105,'Bạn bè',BRAND['surface2'],BRAND['muted'])
        out += rect(1032,215,330,42,BRAND['surface2'],BRAND['line'],21)+tx(1052,241,'⌕ Tìm trong danh sách...',11,500,'#94A3B8')
        names=['An Trần','Lê Vân','Huy Đỗ','Mai Phạm','Đức Nguyễn','Lưu Trần']
        for i,n in enumerate(names):
            yy=298+i*82
            out += avatar(312,yy,22,n[0],['#F97376','#10B981','#3B82F6','#EC4899','#F59E0B','#8B5CF6'][i],'online' if i in {0,3} else 'offline')
            out += tx(348,yy-4,n,13,800)+tx(348,yy+17,'@'+n.lower().replace(' ',''),10,500,BRAND['muted'])
            out += btn(1060,yy-20,138,'Hủy theo dõi',False,38)+btn(1210,yy-20,112,'Chặn',False,38)
            out += line(282,yy+38,1368,yy+38)
        out += tx(282,834,'‹ Trước',12,700,BRAND['muted'])+tx(824,834,'1   2   3   …   24',12,800,BRAND['primary'],'middle')+tx(1368,834,'Tiếp ›',12,700,BRAND['muted'],'end')
    return out


def settings_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Trang chủ')
    out += screen_title(258,118,item['title'],'Kiểm soát tài khoản và quyền riêng tư theo cách dễ hiểu.')
    # settings nav
    out += section_card(258,170,248,690,'Cài đặt')
    nav=[('SET-01','Quyền riêng tư'),('SET-02','Bảo mật'),('SET-03','Đã chặn'),('SET-04','Xóa tài khoản')]
    for i,(idv,lab) in enumerate(nav):
        yy=226+i*52
        if sid==idv: out += rect(274,yy-24,216,42,BRAND['soft'],'none',10)
        out += tx(292,yy,lab,12,800 if sid==idv else 600,BRAND['primary'] if sid==idv else BRAND['ink'])
    x=532
    if sid=='SET-01':
        out += section_card(x,170,874,690,'Quyền riêng tư và khả năng được tìm thấy','Bạn luôn có thể xem trước tác động của từng lựa chọn.')
        sections=[('Ai có thể xem hồ sơ?',['Tất cả','Bạn bè','Tùy chọn','Không cho phép']),('Ai có thể nhắn tin và xem hồ sơ?',['Tất cả','Bạn bè','Tùy chọn','Không cho phép']),('Cho phép tìm bằng thông tin cá nhân',['Email','Số điện thoại','Tên người dùng'])]
        yy=236
        for title,ops in sections:
            out += tx(558,yy,title,13,800)
            yy+=28
            for i,o in enumerate(ops):
                out += pill(558+i*150,yy,136,o,BRAND['soft'] if i==1 else BRAND['surface2'],BRAND['primary'] if i==1 else BRAND['muted'])
            yy+=64
        out += tx(558,yy,'Trạng thái hoạt động',13,800)
        out += rect(1180,yy-20,68,32,BRAND['primary'],'none',16)+circle(1232,yy-4,12,'#FFFFFF')+tx(1260,yy,'Bật',12,800,BRAND['green'])
        yy+=64
        out += rect(558,yy-22,800,72,'#FFF7ED','#FED7AA',12)
        out += tx(578,yy+4,'🔔 Khi một người lạ xem hồ sơ hoặc gửi tin, bạn sẽ nhận thông báo.',11,700,'#9A3412')
        out += btn(1210,806,148,'Lưu thiết lập',True,42)
    elif sid=='SET-02':
        out += section_card(x,170,874,690,'Bảo mật tài khoản','Đổi mật khẩu và kiểm soát phiên đăng nhập.')
        out += tx(558,230,'Đổi mật khẩu',15,900)
        out += input_box(558,260,360,'Mật khẩu hiện tại','••••••••')
        out += input_box(944,260,386,'Mật khẩu mới','••••••••','ok')
        out += btn(1136,340,194,'Đổi mật khẩu',True,42)
        out += line(558,410,1358,410)
        out += tx(558,454,'Phiên đăng nhập',15,900)
        devices=[('Windows · Edge','Thiết bị hiện tại · TP.HCM','Hiện tại'),('Android · Chrome','Hoạt động 12 phút trước','Cần OTP'),('iPad · Safari','Hoạt động hôm qua','Cần OTP')]
        for i,(a,b,c) in enumerate(devices):
            yy=504+i*82
            out += rect(558,yy-30,800,66,BRAND['surface2'],'none',12)
            out += tx(582,yy-3,'▣ '+a,12,800)+tx(582,yy+18,b,10,500,BRAND['muted'])
            out += btn(1188,yy-18,146,'Đăng xuất',False,36)
            out += pill(1062,yy-14,106,c,'#DCFCE7' if i==0 else '#FFF7ED','#15803D' if i==0 else '#9A3412')
        out += btn(558,760,184,'Đăng xuất',False,42)+btn(758,760,252,'Đăng xuất mọi thiết bị',True,42)
        out += tx(558,830,'Đăng xuất thiết bị riêng cần mã OTP qua email.',11,600,BRAND['muted'])
    elif sid=='SET-03':
        out += section_card(x,170,874,690,'Tài khoản đã chặn','Hai bên không thể nhìn thấy hồ sơ hoặc nhắn tin cho nhau.')
        blocked=[('Nguyễn A','Spam liên tục','12/08/2026'),('Trần B','Quấy rối trong cộng đồng','02/09/2026'),('Lê C','Không muốn tương tác','04/09/2026')]
        for i,(n,r,d) in enumerate(blocked):
            yy=252+i*130
            out += avatar(586,yy,23,n[0],['#F97376','#10B981','#3B82F6'][i],'offline')
            out += tx(622,yy-5,n,13,800)+tx(622,yy+18,'Lý do: '+r,11,600,BRAND['muted'])
            out += tx(1092,yy+5,'Đã chặn '+d,10,600,BRAND['muted'])
            out += btn(1200,yy-20,134,'Bỏ chặn',False,40)
            out += line(558,yy+56,1358,yy+56)
        out += rect(558,650,800,96,'#FFF7ED','#FED7AA',14)
        out += tx(580,682,'Cảnh báo khi gặp trong cộng đồng chung',12,900,'#9A3412')
        out += paragraph(580,706,'“Bạn đã chặn người này. Bạn vẫn muốn tham gia cộng đồng có họ không?”',86,11,'#9A3412',18,2)
    elif sid=='SET-04':
        out += section_card(x,170,874,690,'Xóa và khôi phục tài khoản','Quy trình có xác thực lại và thời gian khôi phục 30 ngày.')
        out += rect(558,224,800,100,'#FEF2F2','#FECACA',14)
        out += tx(580,256,'Bạn sẽ mất quyền truy cập ngay sau khi xác nhận.',13,900,'#B91C1C')
        out += paragraph(580,282,'Tài khoản cũ chỉ bị xóa cứng sau 30 ngày nếu không có yêu cầu khôi phục.',88,11,'#991B1B',18,2)
        out += input_box(558,370,800,'Mật khẩu hiện tại','••••••••')
        out += input_box(558,454,800,'Mã OTP gửi qua email','123 456','ok')
        out += tx(558,532,'Email sau khi yêu cầu xóa',13,800)
        out += tx(558,558,'Có thể tạo tài khoản mới bằng email này. Nếu khôi phục trong 30 ngày,',11,600,BRAND['muted'])
        out += tx(558,577,'hệ thống sẽ hướng dẫn chọn giữ tài khoản mới hoặc lấy lại tài khoản cũ.',11,600,BRAND['muted'])
        out += tx(558,634,'☐ Tôi hiểu nội dung và muốn tiếp tục',12,700)
        out += btn(1130,700,228,'Yêu cầu xóa tài khoản',True,44)
    return out


def discovery_scene(item: dict[str, Any]) -> str:
    out=app_shell('Trang chủ')
    out += screen_title(258,118,'Tìm kiếm','Kết quả gần đúng, ưu tiên người bạn đã theo dõi và nội dung liên quan.')
    out += rect(258,170,1148,62,'#FFFFFF',BRAND['line'],31)+tx(286,208,'T',20,700,BRAND['primary'])+tx(322,208,'thiết kế hệ thống',15,600)+btn(1246,181,140,'Tìm kiếm',True,40)
    out += pill(258,254,132,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(400,254,132,'Người dùng','#EAF2FF','#1D4ED8')+pill(542,254,132,'Bài viết','#FDF2F8','#BE185D')+pill(684,254,132,'Cộng đồng','#ECFDF5','#047857')
    out += section_card(258,310,1148,574,'Kết quả phù hợp','Sắp xếp theo mối quan hệ, độ gần đúng và mức độ liên quan')
    out += tx(282,360,'Người bạn đang theo dõi',12,900,'#1D4ED8')
    for i,n in enumerate(['An Trần · @anthietke','Lê Vân · @levanux']):
        yy=404+i*74;out += rect(282,yy-32,1080,58,'#EEF5FF','none',12)+avatar(312,yy-4,20,n[0],'#3B82F6','online')+tx(348,yy-8,n,12,800)+tx(348,yy+12,'Khớp gần đúng: thiết kế · hệ thống',10,600,BRAND['muted'])+pill(1218,yy-18,120,'Đang theo dõi','#DBEAFE','#1D4ED8')
    out += tx(282,560,'Bài viết liên quan',12,900,'#BE185D')
    for i,title in enumerate(['Thiết kế hệ thống cho mạng xã hội','Từ wireframe đến frontend production']):
        yy=608+i*82;out += rect(282,yy-34,1080,66,'#FFF1F7','none',12)+rect(298,yy-22,66,42,'url(#media)','none',8)+tx(382,yy-7,title,12,800)+tx(382,yy+14,'Linh Nguyễn · 2 giờ trước',10,600,BRAND['muted'])
    out += tx(282,766,'Cộng đồng',12,900,'#047857')
    out += rect(282,790,1080,58,'#ECFDF5','none',12)+tx(306,825,'# UI/UX Việt Nam · 48,2K thành viên',12,800,'#047857')+btn(1196,799,142,'Xem cộng đồng',False,40)
    return out


def notification_scene(item: dict[str, Any]) -> str:
    out=app_shell('Trang chủ')
    out += screen_title(258,118,'Thông báo','Nội dung ngắn gọn; mở chi tiết khi bạn cần thêm ngữ cảnh.')
    out += section_card(258,170,700,716,'Hộp thông báo')
    out += pill(282,220,102,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(394,220,102,'Đề cập',BRAND['surface2'],BRAND['muted'])+pill(506,220,132,'Chưa đọc',BRAND['surface2'],BRAND['muted'])
    out += icon_button(890,214,'Tắt nhanh','N',False,38)
    notes=[('Linh đã thích bài viết của bạn','2 phút','♥'),('Bạn được đề cập trong #backend-dotnet','12 phút','@'),('Cộng đồng UI/UX có bài viết nổi bật','1 giờ','▦'),('An Trần đã gửi cho bạn một tin nhắn','2 giờ','✉')]
    for i,(a,b,ic) in enumerate(notes):
        yy=300+i*102
        out += rect(282,yy-42,652,84,'#F7F5FF' if i<2 else '#FFFFFF',BRAND['line'],12)
        out += circle(316,yy,20,BRAND['soft'])+tx(316,yy+5,ic,14,800,BRAND['primary'],'middle')
        out += tx(350,yy-5,a,12,800)+tx(350,yy+16,b,10,600,BRAND['muted'])
        out += circle(906,yy,5,BRAND['primary'] if i<2 else '#CBD5E1')
        out += tx(886,yy+5,'N',13,700,BRAND['muted'],'end')
    out += btn(584,736,350,'Xem tất cả thông báo',False,42)
    out += section_card(984,170,422,430,'Chi tiết thông báo','Mở khi chọn một thông báo')
    out += avatar(1018,236,22,'L','#FF8B6A','online')
    out += tx(1052,230,'Linh Nguyễn',13,800)+tx(1052,250,'đã thích bài viết của bạn',11,600,BRAND['muted'])
    out += rect(1008,284,374,142,'url(#media)','none',14)
    out += tx(1008,460,'“Một khoảnh khắc nhỏ trong ngày...”',12,700)
    out += btn(1008,500,374,'Đi đến bài viết',True,44)
    out += tx(1008,570,'Thông báo này sẽ được đánh dấu đã đọc.',10,600,BRAND['muted'])
    return out


def community_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Cộng đồng')
    if sid=='COMM-01':
        out += screen_title(258,118,'Khám phá cộng đồng','Tìm đúng “tường” nội dung và giảm những chủ đề bạn không quan tâm.')
        categories=['Thời sự','Thế giới','Kinh doanh','Khoa học công nghệ','Góc nhìn','Spotlight','Bất động sản','Sức khỏe','Giải trí','Thể thao','Pháp luật','Giáo dục','Đời sống','Xe','Du lịch','Ảnh','Infographic','Ý kiến','Tâm sự','Thư giãn']
        for i,c in enumerate(categories):
            col=i%5;row=i//5
            out += pill(258+col*224,172+row*42,204,c,BRAND['soft'] if i in {0,3,8} else '#FFFFFF',BRAND['primary'] if i in {0,3,8} else BRAND['muted'])
        out += section_card(258,360,1148,542,'Cộng đồng gợi ý','Dựa trên chủ đề và kết nối của bạn')
        cards=[('UI/UX Việt Nam','48,2K thành viên','Khoa học công nghệ'),('Backend .NET','21,4K thành viên','Khoa học công nghệ'),('Góc nhìn trẻ','80,1K thành viên','Góc nhìn')]
        for i,(n,m,c) in enumerate(cards):
            xx=282+i*354
            out += rect(xx,416,330,410,'#FFFFFF',BRAND['line'],16,extra='filter="url(#tinyShadow)"')
            out += rect(xx,416,330,148,'url(#media)','none',16)
            out += avatar(xx+48,560,30,n[0],['#6C5CE7','#3B82F6','#F97376'][i])
            out += tx(xx+24,620,n,15,900)+tx(xx+24,644,m,11,600,BRAND['muted'])+pill(xx+24,662,190,c,'#ECFDF5','#047857')
            out += paragraph(xx+24,720,'Nơi chia sẻ kinh nghiệm, bài viết và cuộc trò chuyện chuyên sâu.',35,11,BRAND['muted'],18,3)
            out += btn(xx+24,780,134,'Tham gia',True,40)+btn(xx+170,780,136,'Không quan tâm',False,40)
    elif sid=='COMM-02':
        out += rect(250,94,1158,210,'url(#twilight)','none',20)
        out += tx(282,244,'UI/UX Việt Nam',28,900,'#FFFFFF')+tx(282,270,'48.240 thành viên · 1.382 đang hoạt động',12,600,'#E5E7FF')
        out += btn(962,236,126,'Mời',False,40)+btn(1098,236,126,'Chia sẻ',False,40)+btn(1234,236,144,'Đã tham gia',True,40)
        out += pill(258,330,126,'Bài viết',BRAND['soft'],BRAND['primary'])+pill(394,330,126,'Giới thiệu',BRAND['surface2'],BRAND['muted'])+pill(530,330,126,'Thành viên',BRAND['surface2'],BRAND['muted'])
        out += sticky_composer(258,386,760)
        out += post_card(258,478,760,418,False,False)
        out += section_card(1042,386,364,230,'Quy tắc cộng đồng','Cần chấp thuận khi tham gia')
        rules=['Tôn trọng thành viên','Không spam hoặc quảng cáo sai chỗ','Không chia sẻ dữ liệu riêng tư']
        for i,r in enumerate(rules):out += tx(1062,448+i*40,f'{i+1}. {r}',11,700)
        out += section_card(1042,636,364,260,'Thông báo cộng đồng')
        out += tx(1062,700,'Mức ưu tiên',11,700,BRAND['muted'])+pill(1180,680,150,'Yêu thích',BRAND['soft'],BRAND['primary'])
        out += tx(1062,758,'Hạn chế bài viết',11,700,BRAND['muted'])+pill(1180,738,150,'Bình thường',BRAND['surface2'],BRAND['muted'])
    elif sid=='COMM-03':
        out += screen_title(258,118,'Tham gia cộng đồng','Xem rõ điều kiện và quy tắc trước khi đồng ý.')
        out += section_card(398,176,868,650,'Lời mời vào UI/UX Việt Nam','Được mời bởi An Trần · 48.240 thành viên')
        out += rect(430,238,804,120,'url(#twilight)','none',16)
        out += tx(460,318,'Một cộng đồng sáng tạo, an toàn và hữu ích.',18,900,'#FFFFFF')
        out += tx(430,400,'Điều kiện tham gia',14,900)
        checks=['Tôi đã đọc và đồng ý quy tắc cộng đồng.','Tôi hiểu vi phạm nghiêm trọng có thể bị cấm vĩnh viễn.','Tôi đồng ý nhận thông báo quan trọng từ quản trị viên.']
        for i,c in enumerate(checks): out += tx(438,446+i*52,'☑ '+c,12,700)
        out += rect(430,618,804,74,'#FFF7ED','#FED7AA',12)+paragraph(452,648,'Quyết định ban vĩnh viễn phải có lý do và được lưu dấu kiểm toán.',86,11,'#9A3412',18,2)
        out += btn(430,736,160,'Từ chối',False,44)+btn(1030,736,204,'Chấp thuận và tham gia',True,44)
    elif sid=='COMM-04':
        out += screen_title(258,118,'Vai trò và quyền','Chỉ chủ sở hữu nhìn thấy và thay đổi ma trận quyền này.')
        out += section_card(258,170,1148,730,'Ma trận vai trò')
        roles=['Chủ sở hữu','Điều phối viên','Thành viên','Khách']
        perms=['Quản lý vai trò','Quản lý kênh','Duyệt thành viên','Cảnh báo thành viên','Cấm tài khoản','Đăng bài','Tham gia thoại']
        for i,r in enumerate(roles):out += tx(660+i*170,226,r,11,800,BRAND['primary'] if i==0 else BRAND['ink'],'middle')
        for j,p in enumerate(perms):
            yy=280+j*68;out += tx(286,yy,p,12,700)
            for i,r in enumerate(roles):
                allowed=(i==0) or (i==1 and j in {1,2,3,4,5,6}) or (i==2 and j in {5,6}) or (i==3 and j==6)
                out += rect(630+i*170,yy-23,60,34,BRAND['primary'] if allowed else '#E2E8F0','none',17)+circle(674+i*170 if allowed else 646+i*170,yy-6,12,'#FFFFFF')
            out += line(282,yy+24,1374,yy+24)
        out += btn(1184,842,190,'Lưu quyền',True,44)
    elif sid=='COMM-05':
        out += screen_title(258,118,'Quản lý kênh và thành viên chờ duyệt','Chủ sở hữu kiểm soát cấu trúc kênh và quyền tham gia.')
        out += section_card(258,170,560,720,'Danh sách kênh')
        chans=['# chào-mừng','# thông-báo','# trò-chuyện','🔊 Phòng chung','🔊 Học nhóm']
        for i,c in enumerate(chans):
            yy=230+i*62;out += rect(282,yy-26,512,48,BRAND['soft'] if i==2 else BRAND['surface2'],'none',10)+tx(300,yy+4,c,12,800 if i==2 else 600,BRAND['primary'] if i==2 else BRAND['ink'])+tx(766,yy+4,'⋮',18,800,BRAND['muted'],'middle')
        out += btn(282,566,206,'+ Tạo kênh mới',True,42)
        out += section_card(842,170,564,720,'Yêu cầu tham gia','3 tài khoản đang chờ')
        names=['Ngọc Minh','Tuấn Anh','Vy Trần']
        for i,n in enumerate(names):
            yy=246+i*106;out += avatar(876,yy,22,n[0],['#F97376','#10B981','#3B82F6'][i]) + tx(912,yy-4,n,12,800)+tx(912,yy+16,'Đã chấp thuận quy tắc',10,600,BRAND['muted'])+btn(1162,yy-22,98,'Duyệt',True,38)+btn(1270,yy-22,110,'Từ chối',False,38)
            out += line(866,yy+48,1382,yy+48)
        out += rect(866,598,516,110,'#FEF2F2','#FECACA',12)+tx(888,628,'Cấm tài khoản khỏi cộng đồng',12,900,'#B91C1C')+paragraph(888,652,'Chỉ chủ sở hữu hoặc vai trò được cấp quyền mới có thể thực hiện.',52,11,'#991B1B',18,2)+btn(1200,654,154,'Mở danh sách cấm',False,38)
    elif sid=='COMM-06':
        out += screen_title(258,118,'Điều hành thành viên','Trạng thái hoạt động thể hiện bằng chấm xanh hoặc xám.')
        out += section_card(258,170,1148,720,'Thành viên · 48.240')
        out += rect(282,218,480,42,BRAND['surface2'],BRAND['line'],21)+tx(302,244,'⌕ Tìm thành viên...',11,500,'#94A3B8')
        people=['An Trần','Lê Vân','Huy Đỗ','Mai Phạm','Đức Nguyễn','Lưu Trần']
        for i,n in enumerate(people):
            yy=320+i*82;out += avatar(314,yy,23,n[0],['#F97376','#10B981','#3B82F6','#EC4899','#F59E0B','#8B5CF6'][i],'online' if i%2==0 else 'offline')+tx(352,yy-6,n,13,800)+tx(352,yy+16,'Thành viên · Tham gia 08/2026',10,600,BRAND['muted'])+pill(866,yy-16,126,'Đang hoạt động' if i%2==0 else 'Ngoại tuyến','#DCFCE7' if i%2==0 else '#F1F5F9','#15803D' if i%2==0 else BRAND['muted'])+btn(1070,yy-20,114,'Cảnh báo',False,38)+btn(1196,yy-20,88,'Ban',False,38)+tx(1352,yy+4,'•••',16,800,BRAND['muted'],'middle')+line(282,yy+40,1382,yy+40)
    elif sid=='COMM-07':
        # community chat with bottom composer
        out += section_card(244,88,230,908,'UI/UX Việt Nam')
        chans=['THÔNG TIN','# chào-mừng','# thông-báo','KÊNH CHỮ','# trò-chuyện','# góp-ý','KÊNH THOẠI','🔊 Phòng chung']
        for i,c in enumerate(chans):
            yy=144+i*45;out += tx(264,yy,c,10 if c.isupper() else 12,800 if c.isupper() else 600,BRAND['muted'] if c.isupper() else BRAND['ink'])
        out += section_card(492,88,914,908,'# trò-chuyện','125 thành viên · cộng đồng')
        msgs=[('An Trần','Mọi người thấy bản thiết kế mới thế nào?','09:12'),('Phạm Minh Sáng','Mình đang chỉnh phần mobile dựa trên desktop.','09:14'),('Lê Vân','Mình thích thanh điều hướng mới đó!','09:16')]
        for i,(n,m,t) in enumerate(msgs):
            yy=192+i*144; mine=i==1
            bx=724 if mine else 552; bw=610 if mine else 570
            out += avatar(524 if not mine else 1360,yy,20,n[0],['#F97376','#6C5CE7','#10B981'][i],'online' if i!=2 else 'offline')
            out += rect(bx,yy-34,bw,84,BRAND['soft'] if mine else BRAND['surface2'],'none',14)
            out += tx(bx+18,yy-9,n,11,800,BRAND['primary'] if mine else BRAND['ink'])+tx(bx+18,yy+15,m,12,600)+tx(bx+bw-16,yy+38,t,9,600,BRAND['muted'],'end')
            out += tx(bx+18,yy+70,'♡ Thích   ↩ Trả lời   ••• Báo cáo',10,700,BRAND['muted'])
        out += tx(552,650,'An và 2 người khác đang nhập',10,600,BRAND['muted'])
        for i in range(3):out += circle(706+i*10,646+(i%2)*4,3,BRAND['primary'])
        out += rect(520,814,850,120,'#FFFFFF',BRAND['line'],16)
        out += icon_button(536,834,'Thêm tệp','+',False,42)
        out += tx(596,860,'Nhắn tin trong #trò-chuyện',12,500,'#94A3B8')
        out += tx(596,906,'Enter để gửi · Shift + Enter để xuống dòng',9,600,BRAND['muted'])
        out += icon_button(1260,834,'Emoji','☺',False,42)+btn(1312,834,44,'➤',True,42)
        out += toast(1076,706,'Gửi thất bại','Kết nối gián đoạn.  ↻ Gửi lại', 'error', 300)
    return out


def chat_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Trang chủ')
    if sid=='CHAT-01':
        out += screen_title(258,118,'Tin nhắn','Hội thoại ưu tiên theo tin mới, chưa đọc và trạng thái thông báo.')
        out += section_card(258,170,1148,720,'Hội thoại')
        out += rect(282,218,500,42,BRAND['surface2'],BRAND['line'],21)+tx(302,244,'⌕ Tìm hội thoại...',11,500,'#94A3B8')+btn(1190,218,192,'+ Hội thoại mới',True,42)
        chats=[('An Trần','Bạn xem giúp mình bản mới nhé','2 phút','3',False),('Nhóm Đồ án','Huy: Build đã chạy xong','15 phút','12',True),('Lê Vân','Đã gửi một ảnh','1 giờ','',False),('UI/UX Việt Nam','Mai: Mình đồng ý','3 giờ','',True)]
        for i,(n,m,t,u,mute) in enumerate(chats):
            yy=310+i*122;out += rect(282,yy-48,1100,98,BRAND['soft'] if i==0 else '#FFFFFF',BRAND['line'],14)+avatar(326,yy,25,n[0],['#F97376','#6C5CE7','#10B981','#3B82F6'][i],'online' if i in {0,2} else 'offline')+tx(366,yy-12,n,13,900)+tx(366,yy+14,m,11,600,BRAND['muted'])+tx(1304,yy-14,t,10,600,BRAND['muted'],'end')
            if u: out += circle(1328,yy+16,13,BRAND['primary'])+tx(1328,yy+20,u,9,800,'#FFFFFF','middle')
            if mute: out += tx(1270,yy+22,'🔕',14,700,BRAND['muted'],'end')
    elif sid=='CHAT-02':
        out += section_card(244,88,310,908,'Tin nhắn')
        convs=['An Trần','Nhóm Đồ án','Lê Vân','UI/UX Việt Nam']
        for i,n in enumerate(convs):
            yy=154+i*72;out += rect(258,yy-35,282,62,BRAND['soft'] if i==0 else '#FFFFFF','none',12)+avatar(284,yy-4,20,n[0],['#F97376','#6C5CE7','#10B981','#3B82F6'][i],'online' if i in {0,2} else 'offline')+tx(316,yy-8,n,11,800)+tx(316,yy+12,'Tin nhắn gần nhất...',9,500,BRAND['muted'])
        out += rect(570,88,550,908,'#FFFFFF',BRAND['line'],16)
        out += avatar(606,132,22,'A','#F97376','online')+tx(642,126,'An Trần',13,900)+tx(642,146,'Đang hoạt động',10,600,BRAND['green'])
        out += icon_button(1000,110,'Gọi thoại','A',False,38)+icon_button(1046,110,'Gọi video','V',False,38)
        msgs=[('An','Bạn đã hoàn thiện desktop chưa?'),('Me','Mình vừa xong, giờ đang đồng bộ mobile.'),('An','Gửi mình xem nhé!')]
        for i,(who,msg) in enumerate(msgs):
            yy=240+i*116;mine=who=='Me';x=770 if mine else 610;w=310 if mine else 360
            out += rect(x,yy-30,w,66,BRAND['soft'] if mine else BRAND['surface2'],'none',15)+tx(x+16,yy+4,msg,11,700)+tx(x+w-14,yy+26,'09:'+str(12+i*2),9,500,BRAND['muted'],'end')
        out += rect(594,824,502,130,'#FFFFFF',BRAND['line'],14)+icon_button(608,842,'Tệp','+',False,40)+tx(660,868,'Nhập tin nhắn...',11,500,'#94A3B8')+tx(660,926,'Enter gửi · Shift+Enter xuống dòng',9,600,BRAND['muted'])+btn(1038,842,42,'➤',True,40)
        out += section_card(1140,88,266,908,'Thông tin')
        out += avatar(1273,170,42,'A','#F97376','online')+tx(1273,232,'An Trần',14,900,BRAND['ink'],'middle')
        out += pill(1164,258,105,'Bạn bè',BRAND['soft'],BRAND['primary'])+pill(1278,258,104,'Đang online','#DCFCE7','#15803D')
        for i,(a,b) in enumerate([('Ảnh & video','26'),('Tệp đã chia sẻ','8'),('Liên kết','12'),('Phiên âm gần đây','3')]):
            yy=338+i*58;out += tx(1164,yy,a,11,700)+tx(1380,yy,b,11,800,BRAND['primary'],'end')+line(1164,yy+18,1382,yy+18)
        out += rect(1164,600,218,88,BRAND['surface2'],'none',12)+tx(1180,628,'Phiên âm tin nhắn thoại',10,800,BRAND['primary'])+paragraph(1180,650,'“Mình gửi bạn file lúc chiều nhé...”',28,10,BRAND['muted'],16,2)
    elif sid=='CHAT-03':
        out += screen_title(258,118,'Tạo hội thoại','Chọn một hoặc nhiều người; hội thoại 1:1 trùng sẽ được tái sử dụng.')
        out += section_card(380,170,904,700,'Chọn người nhận')
        out += rect(408,224,848,46,BRAND['surface2'],BRAND['line'],23)+tx(430,252,'⌕ Tìm theo tên hoặc tên người dùng...',11,500,'#94A3B8')
        out += pill(408,292,120,'An Trần ×',BRAND['soft'],BRAND['primary'])+pill(540,292,120,'Lê Vân ×',BRAND['soft'],BRAND['primary'])
        names=['An Trần','Lê Vân','Huy Đỗ','Mai Phạm','Đức Nguyễn']
        for i,n in enumerate(names):
            yy=380+i*74;out += avatar(438,yy,21,n[0],['#F97376','#10B981','#3B82F6','#EC4899','#F59E0B'][i],'online' if i<2 else 'offline')+tx(474,yy-4,n,12,800)+tx(474,yy+16,'@'+n.lower().replace(' ',''),10,500,BRAND['muted'])+circle(1218,yy,11,'#FFFFFF',BRAND['primary'],2)+(circle(1218,yy,6,BRAND['primary']) if i<2 else '')+line(408,yy+34,1256,yy+34)
        out += btn(408,798,126,'Hủy',False,44)+btn(1044,798,212,'Bắt đầu trò chuyện',True,44)
    elif sid=='CHAT-04':
        out += screen_title(258,118,'Thiết lập hội thoại','Tùy chỉnh trải nghiệm mà không làm thay đổi hồ sơ bên ngoài.')
        out += section_card(258,170,1148,720,'Nhóm Đồ án')
        settings=[('Danh hiệu trong nhóm','Backend Lead','Chỉ hiện trong hội thoại'),('Chủ đề trò chuyện','Twilight Purple','Áp dụng cho thành viên'),('Tin nhắn đã ghim','5 mục','Xem và quản lý'),('Thông báo','Chỉ đề cập','Có thể tắt hoàn toàn')]
        for i,(a,b,c) in enumerate(settings):
            yy=250+i*110;out += tx(286,yy,a,13,800)+tx(286,yy+24,c,10,600,BRAND['muted'])+pill(1110,yy-22,250,b,BRAND['surface2'],BRAND['ink'])+line(282,yy+52,1380,yy+52)
        out += rect(282,706,1098,92,'#F8FAFC',BRAND['line'],14)+tx(304,738,'Rời nhóm trong im lặng',13,900)+tx(304,762,'Không gửi thông báo rời nhóm cho các thành viên khác.',10,600,BRAND['muted'])+btn(1192,724,164,'Rời trong im lặng',False,42)
    return out


def rtc_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=rect(0,0,1440,1024,'#090B12','none',0)
    out += rect(0,0,1440,70,'#111522','none',0)+rect(22,14,42,42,'url(#brand)','none',12)+tx(43,43,'T',18,900,'#FFFFFF','middle')+tx(78,34,'Twight Light Call',16,900,'#FFFFFF')+tx(78,52,'Mở trong tab / ứng dụng riêng',10,600,'#AAB2C7')
    out += tx(1390,42,'×',22,700,'#AAB2C7','end')
    if sid=='RTC-01':
        out += rect(370,180,700,600,'#161B29','#283044',22,extra='filter="url(#shadow)"')
        out += avatar(720,330,70,'A','#F97376','online')+tx(720,432,'An Trần đang gọi cho bạn',26,900,'#FFFFFF','middle')+tx(720,468,'Cuộc gọi video · Nhóm Đồ án',13,600,'#AAB2C7','middle')
        out += circle(625,584,36,'#EF4444')+tx(625,591,'×',25,900,'#FFFFFF','middle')+tx(625,642,'Từ chối',11,700,'#AAB2C7','middle')
        out += circle(815,584,36,'#10B981')+tx(815,591,'✓',24,900,'#FFFFFF','middle')+tx(815,642,'Chấp nhận',11,700,'#AAB2C7','middle')
        out += tx(720,712,'Cuộc gọi sẽ mở trong cửa sổ riêng.',11,600,'#AAB2C7','middle')
    elif sid=='RTC-02':
        out += rect(20,90,1030,830,'#111522','#283044',18)
        out += tx(42,126,'Phòng chung · Mã TW-8F2K',13,800,'#FFFFFF')
        out += pill(830,106,196,'Bố cục: Lưới ⌄','#232B42','#FFFFFF')
        people=[('An',50,160),('Sáng',545,160),('Lê Vân',50,460),('Phạm Thư',545,460)]
        for i,(n,x,y) in enumerate(people):
            out += rect(x,y,455,260,'url(#media)' if i!=3 else '#1B2233','#283044',16)
            out += avatar(x+44,y+44,24,n[0],['#F97376','#6C5CE7','#10B981','#3B82F6'][i],'online')
            out += pill(x+18,y+216,120,n,'#07162BCC','#FFFFFF')
            out += pill(x+340,y+216,86,'Mic bật' if i<2 else 'Mic tắt','#07162BCC','#FFFFFF')
        out += rect(1070,90,350,830,'#111522','#283044',18)
        out += tx(1092,128,'Trò chuyện',15,900,'#FFFFFF')+pill(1092,150,126,'Tất cả','#3A315F','#FFFFFF')+pill(1228,150,126,'Riêng tư','#1B2233','#AAB2C7')
        msgs=[('An','Mọi người nghe rõ không?'),('Sáng','Rõ nhé!'),('Lê Vân','Mình vào rồi.')]
        for i,(n,m) in enumerate(msgs):
            yy=230+i*92;out += avatar(1104,yy,16,n[0],['#F97376','#6C5CE7','#10B981'][i])+tx(1128,yy-5,n,10,800,'#FFFFFF')+paragraph(1128,yy+15,m,28,10,'#D7DCEE',16,2)
        out += rect(1092,798,306,82,'#1B2233','#303A54',12)+tx(1110,828,'Nhắn cho mọi người...',10,500,'#818AA4')+btn(1318,832,58,'Gửi',True,34)
        out += rect(20,936,1400,70,'#111522','none',0)
        out += btn(38,950,178,'Mời thành viên',False,42)+pill(232,956,136,'Mã TW-8F2K','#232B42','#FFFFFF')
        # device controls with dropdowns
        out += btn(570,950,118,'Mic ✓ ⌄',False,42)+btn(700,950,118,'Camera ✓ ⌄',False,42)+btn(830,950,116,'Chia sẻ',False,42)+btn(958,950,116,'Bố cục ⌄',False,42)+btn(1240,950,150,'Rời phòng',True,42)
        out += pill(120,116,180,'Tham gia thoại','#10B981','#FFFFFF')
    elif sid=='RTC-03':
        out += rect(20,90,1060,828,'#111522','#283044',18)
        out += rect(42,124,1016,650,'url(#media)','none',16)+pill(64,146,236,'Đang chia sẻ: Toàn màn hình','#07162BCC','#FFFFFF')
        out += rect(802,588,230,154,'#181E2E','#303A54',14)+avatar(917,645,46,'M','#6C5CE7','online')+tx(917,716,'Camera của bạn',10,700,'#FFFFFF','middle')
        out += section_card(1100,90,320,828,'Kiểm soát phiên')
        controls=[('Camera bản thân','Bật'),('Mic','Bật'),('Loa','Tai nghe USB'),('Ghi hình','Cần xin phép'),('Chia sẻ âm thanh','Bật')]
        for i,(a,b) in enumerate(controls):
            yy=170+i*74;out += tx(1124,yy,a,11,700,'#AAB2C7')+pill(1240,yy-22,150,b,'#232B42','#FFFFFF')
        out += rect(1122,548,276,94,'#3A1820','#6B2533',12)+tx(1144,578,'● Ghi hình chưa bắt đầu',11,900,'#FCA5A5')+paragraph(1144,602,'Cần toàn bộ người tham gia đồng ý.',30,10,'#FCA5A5',16,2)
        out += btn(1122,676,276,'Yêu cầu cho phép ghi',False,42)+btn(1122,734,276,'Dừng chia sẻ',True,42)
        out += rect(20,936,1400,70,'#111522','none',0)+btn(520,950,120,'Mic ✓ ⌄',False,42)+btn(652,950,128,'Camera ✓ ⌄',False,42)+btn(792,950,130,'Loa ⌄',False,42)+btn(1244,950,146,'Rời phòng',True,42)
    return out


def media_scene(item: dict[str, Any]) -> str:
    out=app_shell('Video')
    out += screen_title(258,118,'Trung tâm nội dung','Tải lên, lưu bản nháp, lên lịch và theo dõi hiệu quả video.')
    out += section_card(258,170,720,700,'Tải phương tiện')
    out += rect(282,226,672,184,'#F7F5FF','#AFA6F3',16,2,extra='stroke-dasharray="8 8"')+tx(618,292,'UP',36,800,BRAND['primary'],'middle')+tx(618,330,'Kéo thả video hoặc chọn từ máy',14,900,BRAND['ink'],'middle')+tx(618,354,'MP4, MOV · tối đa 2 GB',11,600,BRAND['muted'],'middle')
    out += tx(282,456,'Ảnh thu nhỏ',13,800)+rect(282,480,214,126,'url(#media)','none',12)+btn(516,522,198,'Chọn ảnh hoặc khung hình',False,42)
    out += tx(282,648,'Xuất bản',13,800)+pill(282,670,120,'Bản nháp',BRAND['soft'],BRAND['primary'])+pill(412,670,120,'Đăng ngay',BRAND['surface2'],BRAND['muted'])+pill(542,670,120,'Lên lịch',BRAND['surface2'],BRAND['muted'])
    out += input_box(282,734,370,'Thời gian đăng','20:30 · 06/09/2026')+btn(782,756,172,'Bắt đầu tải lên',True,44)
    out += section_card(1002,170,404,700,'Dashboard nội dung','Dữ liệu trong 30 ngày')
    stats=[('Lượt xem','128K','+18%'),('Lượt thích','12,4K','+11%'),('Chia sẻ','2.918','+8%'),('Thời gian xem','4.280 giờ','+22%')]
    for i,(a,b,c) in enumerate(stats):
        yy=242+i*106;out += rect(1026,yy-34,356,84,BRAND['surface2'],'none',12)+tx(1048,yy-7,a,11,700,BRAND['muted'])+tx(1048,yy+25,b,20,900)+pill(1260,yy-10,96,c,'#DCFCE7','#15803D')
    out += tx(1026,690,'Bản nháp gần đây',13,900)+rect(1026,714,356,100,'url(#media)','none',12)+pill(1042,730,90,'Bản nháp','#07162BCC','#FFFFFF')
    return out


def market_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Mua bán')
    if sid=='MKT-01':
        out += screen_title(258,118,'Mua bán cộng đồng','Tìm nhanh, xem rõ mô tả và liên hệ trực tiếp với người bán.')
        out += rect(258,170,1000,52,'#FFFFFF',BRAND['line'],26)+tx(282,202,'⌕ Tìm tin đăng, sản phẩm, người bán...',12,500,'#94A3B8')+btn(1268,176,138,'Tìm kiếm',True,42)
        out += icon_button(258,242,'Bộ lọc','⏷',False,42)+pill(312,250,118,'Danh mục',BRAND['surface2'],BRAND['muted'])+pill(440,250,112,'Khoảng giá',BRAND['surface2'],BRAND['muted'])+pill(562,250,122,'Gần bạn',BRAND['surface2'],BRAND['muted'])
        products=[('Bàn phím cơ','1.250.000đ','Linear switch · Còn mới 95%'),('Màn hình 27 inch','3.900.000đ','2K IPS · Bảo hành 8 tháng'),('Máy ảnh Fuji','18.500.000đ','Kèm lens kit · Ít sử dụng'),('Ghế công thái học','2.200.000đ','Lưới thoáng · Tải 120kg'),('Tai nghe studio','1.680.000đ','Âm thanh cân bằng'),('iPad Air','13.800.000đ','64GB · Wifi · Xanh')]
        for i,(n,p,d) in enumerate(products):
            col=i%3;row=i//3;xx=258+col*382;yy=324+row*300
            out += rect(xx,yy,358,276,'#FFFFFF',BRAND['line'],16,extra='filter="url(#tinyShadow)"')+rect(xx,yy,358,126,'url(#media)','none',16)+pill(xx+18,yy+16,86,'Đã kiểm tra','#07162BCC','#FFFFFF')+tx(xx+18,yy+164,n,14,900)+tx(xx+18,yy+190,p,16,900,BRAND['primary'])+tx(xx+18,yy+214,d,10,600,BRAND['muted'])+btn(xx+18,yy+228,144,'Mua',True,36)+btn(xx+174,yy+228,166,'Liên hệ người bán',False,36)
    elif sid=='MKT-02':
        out += screen_title(258,118,'Chi tiết tin đăng','Xem biến thể, mô tả và liên hệ người bán trước khi quyết định.')
        out += section_card(258,170,730,700,'Bàn phím cơ Custom')
        out += rect(282,226,682,350,'url(#media)','none',16)
        for i in range(4):out += rect(282+i*128,598,112,80,'url(#media)',BRAND['primary'] if i==0 else BRAND['line'],10,3 if i==0 else 1)
        out += section_card(1012,170,394,700,'Bàn phím cơ Custom')
        out += tx(1036,238,'1.250.000đ',24,900,BRAND['primary'])+tx(1036,266,'Đăng 2 giờ trước · TP.HCM',10,600,BRAND['muted'])
        out += tx(1036,316,'Phân loại',12,800)
        for i,v in enumerate(['Switch Red','Switch Brown','Barebone']):out += pill(1036+(i%2)*160,338+(i//2)*42,148,v,BRAND['soft'] if i==0 else BRAND['surface2'],BRAND['primary'] if i==0 else BRAND['muted'])
        out += tx(1036,434,'Mô tả sản phẩm',12,800)+paragraph(1036,460,'Bàn phím 75%, foam đầy đủ, keycap PBT, kết nối ba chế độ. Có thể xem và thử trực tiếp.',42,11,BRAND['muted'],18,5)
        out += tx(1036,574,'Người bán',12,800)+avatar(1060,614,22,'A','#F97376','online')+tx(1096,610,'An Trần',12,800)+tx(1096,630,'Phản hồi trong 10 phút',10,600,BRAND['muted'])
        out += btn(1036,686,346,'Mua sản phẩm',True,44)+btn(1036,744,346,'Liên hệ người bán',False,44)
    elif sid=='MKT-03':
        out += screen_title(258,118,'Tạo hoặc sửa tin đăng','Mô tả rõ từng phân loại để người mua chọn đúng sản phẩm.')
        out += section_card(258,170,1148,720,'Thông tin tin đăng')
        out += input_box(282,226,516,'Tên sản phẩm','Bàn phím cơ Custom','ok')+input_box(822,226,560,'Danh mục','Thiết bị công nghệ')
        out += rect(282,314,1100,116,'#FFFFFF',BRAND['line'],12)+tx(298,344,'Mô tả sản phẩm',11,800,BRAND['muted'])+paragraph(298,374,'Tình trạng, phụ kiện kèm theo, chính sách xem hàng và cách liên hệ...',95,12,BRAND['ink'],20,3)
        out += tx(282,478,'Phân loại sản phẩm',13,900)
        headers=['Tên phân loại','Giá','Số lượng','Mã riêng']
        for i,h in enumerate(headers):out += tx(302+i*255,520,h,10,800,BRAND['muted'])
        variants=[('Switch Red','1.250.000','3','RED-75'),('Switch Brown','1.300.000','2','BRN-75')]
        for r,row in enumerate(variants):
            yy=548+r*58
            for i,v in enumerate(row):out += rect(288+i*255,yy,230,42,'#FFFFFF',BRAND['line'],10)+tx(302+i*255,yy+26,v,11,600)
        out += btn(282,682,180,'+ Thêm phân loại',False,42)
        out += tx(282,756,'Ảnh sản phẩm',13,900)
        for i in range(5):out += rect(282+i*126,780,110,78,'url(#media)' if i<3 else BRAND['surface2'],BRAND['line'],10)+(tx(337+i*126,826,'+',18,800,BRAND['primary'],'middle') if i>=3 else '')
        out += btn(1204,824,178,'Lưu tin đăng',True,44)
    elif sid=='MKT-04':
        out += screen_title(258,118,'Xác nhận yêu cầu mua','Ứng dụng chỉ kết nối hai bên; thanh toán thực hiện trực tiếp.')
        out += section_card(258,170,720,700,'Sản phẩm đã chọn')
        out += rect(282,228,160,120,'url(#media)','none',12)+tx(468,248,'Bàn phím cơ Custom',14,900)+tx(468,276,'Phân loại: Switch Red',11,700,BRAND['muted'])+tx(468,304,'1.250.000đ',16,900,BRAND['primary'])
        out += tx(282,400,'Số lượng',12,800)+pill(382,382,116,'−   1   +',BRAND['surface2'],BRAND['ink'])
        out += input_box(282,458,672,'Lời nhắn cho người bán','Mình muốn xem hàng lúc 18:00 hôm nay.')
        out += rect(282,558,672,120,'#FFF7ED','#FED7AA',12)+paragraph(304,590,'Không có giữ tiền hoặc hoàn tiền trong ứng dụng. Hai bên tự xác minh thông tin và giao dịch.',68,11,'#9A3412',18,4)
        out += section_card(1002,170,404,700,'Tóm tắt')
        rows=[('Sản phẩm','1.250.000đ'),('Số lượng','1'),('Phí nền tảng','0đ'),('Tổng trao đổi','1.250.000đ')]
        for i,(a,b) in enumerate(rows):yy=240+i*58;out += tx(1026,yy,a,11,700,BRAND['muted'])+tx(1382,yy,b,12,900,BRAND['ink'],'end')+line(1026,yy+20,1382,yy+20)
        out += btn(1026,518,356,'Gửi yêu cầu mua',True,44)+btn(1026,578,356,'Nhắn người bán',False,44)
    elif sid=='MKT-05':
        out += screen_title(258,118,'Thanh toán trực tiếp','Twight Light không xử lý tiền; hãy xác nhận với người bán trước khi chuyển.')
        out += section_card(352,176,736,650,'Thông tin thanh toán của người bán','Đơn TL-2026-0912 · Bàn phím cơ Custom')
        out += rect(392,246,300,300,'#FFFFFF',BRAND['line'],16)
        # QR pattern
        for r in range(8):
            for c in range(8):
                if (r*c+r+c)%3!=0: out += rect(412+c*31,266+r*31,22,22,'#111827','none',2)
        out += tx(742,294,'Số tiền',11,700,BRAND['muted'])+tx(742,326,'1.250.000đ',26,900,BRAND['primary'])
        out += tx(742,380,'Ngân hàng',11,700,BRAND['muted'])+tx(742,404,'Vietcombank',13,800)
        out += tx(742,448,'Số tài khoản',11,700,BRAND['muted'])+tx(742,472,'0123 456 789',13,800)
        out += tx(742,516,'Chủ tài khoản',11,700,BRAND['muted'])+tx(742,540,'NGUYEN VAN AN',13,800)
        out += btn(392,586,300,'Lưu mã QR',False,42)+btn(716,586,332,'Tôi đã liên hệ người bán',True,42)
        out += rect(392,650,656,86,'#FFF7ED','#FED7AA',12)+paragraph(414,682,'Không chuyển tiền khi chưa kiểm tra đúng người bán và thông tin sản phẩm.',68,11,'#9A3412',18,3)
    elif sid=='MKT-06':
        out += screen_title(258,118,'Sản phẩm và yêu cầu mua','Theo dõi theo trạng thái, có phân trang và không có luồng trả hàng.')
        out += pill(258,170,116,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(384,170,146,'Đang liên hệ',BRAND['surface2'],BRAND['muted'])+pill(540,170,130,'Đã hoàn tất',BRAND['surface2'],BRAND['muted'])+pill(680,170,112,'Đã hủy',BRAND['surface2'],BRAND['muted'])
        out += section_card(258,220,1148,650,'Danh sách')
        orders=[('TL-0912','Bàn phím cơ Custom','Đang liên hệ','1.250.000đ'),('TL-0908','Màn hình 27 inch','Đã hoàn tất','3.900.000đ'),('TL-0902','Tai nghe studio','Đã hủy','1.680.000đ'),('TL-0829','Ghế công thái học','Đang liên hệ','2.200.000đ')]
        for i,(idv,n,s,p) in enumerate(orders):
            yy=286+i*118;out += rect(282,yy-42,1100,90,'#FFFFFF',BRAND['line'],14)+rect(300,yy-26,100,58,'url(#media)','none',10)+tx(420,yy-10,n,13,900)+tx(420,yy+16,idv+' · '+p,10,600,BRAND['muted'])+pill(1000,yy-15,152,s,'#FFF7ED' if s=='Đang liên hệ' else '#DCFCE7' if s=='Đã hoàn tất' else '#F1F5F9','#9A3412' if s=='Đang liên hệ' else '#15803D' if s=='Đã hoàn tất' else BRAND['muted'])+btn(1180,yy-22,170,'Xem / Liên hệ',False,40)
        out += tx(282,838,'‹ Trước',12,700,BRAND['muted'])+tx(824,838,'1   2   3   …   12',12,800,BRAND['primary'],'middle')+tx(1380,838,'Tiếp ›',12,700,BRAND['muted'],'end')
    return out


def ai_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Trang chủ')
    if sid=='AI-01':
        out += sticky_composer(258,94,760)+post_card(258,184,760,450,False,False)
        # floating assistant
        out += rect(902,358,500,590,'#FFFFFF',BRAND['line'],20,extra='filter="url(#shadow)"')
        out += rect(902,358,500,64,'url(#brand)','none',20)+tx(930,397,'✦ Trợ lý Twight',15,900,'#FFFFFF')+tx(1372,397,'—  ×',16,800,'#FFFFFF','end')
        out += rect(928,454,352,76,BRAND['surface2'],'none',14)+paragraph(946,482,'Bạn muốn mình tìm cộng đồng, tóm tắt nội dung hay hỗ trợ viết bài?',42,11,BRAND['ink'],18,3)
        out += rect(1020,556,356,64,BRAND['soft'],'none',14)+paragraph(1038,584,'Gợi ý cộng đồng phù hợp với tôi.',38,11,BRAND['ink'],18,2)
        out += rect(928,646,400,104,BRAND['surface2'],'none',14)+paragraph(946,674,'Bạn muốn cộng đồng về chủ đề nào và ưu tiên tiếng Việt hay quốc tế?',46,11,BRAND['ink'],18,4)
        out += rect(928,840,448,82,'#FFFFFF',BRAND['line'],14)+tx(946,872,'Nhập câu hỏi hoặc yêu cầu...',11,500,'#94A3B8')+btn(1310,862,48,'➤',True,38)
        out += circle(1362,966,26,BRAND['primary'])+tx(1362,972,'AI',18,900,'#FFFFFF','middle')
    elif sid=='AI-02':
        out += screen_title(258,118,'Tóm tắt hội thoại hoặc kênh','Tối đa 10.000 dòng; kết quả có thể xuất PDF.')
        out += section_card(258,170,720,700,'Nguồn cần tóm tắt')
        out += input_box(282,230,672,'Hội thoại hoặc kênh','Nhóm Đồ án · #trò-chuyện')
        out += input_box(282,314,320,'Từ ngày','01/09/2026')+input_box(634,314,320,'Đến ngày','05/09/2026')
        out += tx(282,412,'Số dòng ước tính',11,700,BRAND['muted'])+tx(954,412,'8.240 / 10.000',12,900,BRAND['primary'],'end')
        out += rect(282,432,672,16,'#E8ECF3','none',8)+rect(282,432,554,16,'url(#brand)','none',8)
        out += tx(282,492,'Kiểu tóm tắt',12,800)+pill(282,514,128,'Điểm chính',BRAND['soft'],BRAND['primary'])+pill(420,514,128,'Theo chủ đề',BRAND['surface2'],BRAND['muted'])+pill(558,514,128,'Hành động',BRAND['surface2'],BRAND['muted'])
        out += btn(282,608,240,'Tạo bản tóm tắt',True,44)
        out += section_card(1002,170,404,700,'Bản tóm tắt','Được tạo từ nội dung bạn có quyền xem')
        bullets=['Đội đã thống nhất cấu trúc UI/UX mới.','Desktop là nguồn để suy ra mobile.','AI phiên âm được đưa vào bài viết và chat.','Cần rà soát hợp đồng backend phát sinh.']
        for i,b in enumerate(bullets):out += circle(1032,250+i*66,6,BRAND['primary'])+paragraph(1050,254+i*66,b,39,11,BRAND['ink'],18,3)
        out += btn(1026,574,356,'Xuất PDF',False,42,'⇩')+btn(1026,632,356,'Sao chép',True,42)
        out += tx(1026,706,'Nguồn: 8.240 dòng · 4 người tham gia',10,600,BRAND['muted'])
    return out


def moderation_scene(item: dict[str, Any]) -> str:
    sid=item['id'];out=app_shell('Trang chủ')
    if sid=='MOD-01':
        out += rect(224,74,1216,950,'#0B1020','none',0,opacity=.42)
        out += rect(470,170,620,650,'#FFFFFF',BRAND['line'],22,extra='filter="url(#shadow)"')
        out += tx(506,216,'Báo cáo nội dung',20,900)+tx(1054,216,'×',22,700,BRAND['muted'],'middle')
        out += tx(506,260,'Bạn đang báo cáo bài viết của Linh Nguyễn',12,700,BRAND['muted'])
        reasons=['Spam hoặc lừa đảo','Quấy rối / bắt nạt','Ngôn từ thù ghét','Nội dung nhạy cảm','Thông tin sai lệch','Lý do khác']
        for i,r in enumerate(reasons):
            yy=312+i*54;out += circle(520,yy,9,'#FFFFFF',BRAND['primary'],2)+(circle(520,yy,5,BRAND['primary']) if i==1 else '')+tx(544,yy+5,r,12,700)
        out += rect(506,628,548,86,'#FFFFFF',BRAND['line'],12)+tx(520,654,'Mô tả thêm (không bắt buộc)',10,700,BRAND['muted'])+tx(520,682,'Nội dung khiến tôi cảm thấy bị nhắm đến...',11,500,BRAND['ink'])
        out += btn(506,746,140,'Hủy',False,44)+btn(842,746,212,'Gửi báo cáo',True,44)
    elif sid=='MOD-02':
        out += screen_title(258,118,'Hàng đợi điều hành','Phân trang, lọc phạm vi và chỉ hiển thị dữ liệu theo quyền.')
        out += pill(258,170,120,'Đang chờ',BRAND['soft'],BRAND['primary'])+pill(388,170,130,'Đang duyệt',BRAND['surface2'],BRAND['muted'])+pill(528,170,130,'Đã xử lý',BRAND['surface2'],BRAND['muted'])+icon_button(1358,164,'Lọc','⏷',False,42)
        out += section_card(258,220,1148,650,'Báo cáo')
        reports=[('#R-1042','Bài viết','Quấy rối','Cao','12 phút'),('#R-1041','Bình luận','Spam','Trung bình','26 phút'),('#R-1039','Tin nhắn','Ngôn từ thù ghét','Cao','1 giờ'),('#R-1036','Hồ sơ','Mạo danh','Thấp','3 giờ')]
        for i,(rid,target,reason,prio,time) in enumerate(reports):
            yy=294+i*116;out += rect(282,yy-40,1100,88,'#FFFFFF',BRAND['line'],14)+tx(306,yy-10,rid,12,900,BRAND['primary'])+tx(306,yy+15,target+' · '+reason,11,700)+pill(780,yy-14,130,prio,'#FEF2F2' if prio=='Cao' else '#FFF7ED' if prio=='Trung bình' else '#F1F5F9','#B91C1C' if prio=='Cao' else '#9A3412' if prio=='Trung bình' else BRAND['muted'])+tx(1040,yy+4,time,10,600,BRAND['muted'])+btn(1198,yy-20,154,'Mở báo cáo',False,40)
        out += tx(282,838,'‹ Trước',12,700,BRAND['muted'])+tx(824,838,'1   2   3   …   18',12,800,BRAND['primary'],'middle')+tx(1380,838,'Tiếp ›',12,700,BRAND['muted'],'end')
    elif sid=='MOD-03':
        out += screen_title(258,118,'Chi tiết điều hành #R-1042','Mọi hành động cần lý do, quyền phù hợp và dấu vết kiểm toán.')
        out += section_card(258,170,720,700,'Nội dung và bằng chứng')
        out += post_card(282,224,672,390,False,False)
        out += rect(282,642,672,116,BRAND['surface2'],'none',12)+tx(302,672,'Bằng chứng được lưu',12,900)+tx(302,700,'Ảnh chụp · Hash: 8F2C…A90D · Hết hạn sau 180 ngày',10,600,BRAND['muted'])+btn(756,678,170,'Xem bằng chứng',False,38)
        out += section_card(1002,170,404,700,'Quyết định')
        out += input_box(1026,230,356,'Hành động','Ẩn bài viết tạm thời')
        out += input_box(1026,314,356,'Thời hạn','7 ngày')
        out += rect(1026,398,356,120,'#FFFFFF',BRAND['line'],12)+tx(1042,426,'Lý do bắt buộc',10,800,BRAND['muted'])+paragraph(1042,456,'Nội dung công kích cá nhân và vi phạm quy tắc cộng đồng.',38,11,BRAND['ink'],18,4)
        out += rect(1026,548,356,84,'#FFF7ED','#FED7AA',12)+paragraph(1046,580,'Hành động sẽ được gửi tới dịch vụ sở hữu nội dung.',38,10,'#9A3412',16,3)
        out += btn(1026,674,168,'Từ chối báo cáo',False,42)+btn(1206,674,176,'Áp dụng hành động',True,42)
        out += tx(1026,742,'Lịch sử kiểm toán',11,800,BRAND['muted'])+tx(1026,772,'12:06 · Moderator A mở báo cáo',10,600,BRAND['muted'])+tx(1026,796,'12:08 · Xem bằng chứng',10,600,BRAND['muted'])
    return out


def system_scene(item: dict[str, Any]) -> str:
    out=app_shell('Trang chủ')
    out += screen_title(258,118,'Trạng thái giao diện','Mỗi trạng thái đều có hành động rõ ràng, không phụ thuộc màu duy nhất.')
    states=[('Đang tải','Skeleton giữ bố cục ổn định','▧'),('Không có dữ liệu','Giải thích và đề xuất hành động tiếp theo','○'),('Lỗi tạm thời','Giữ dữ liệu nhập và cho phép thử lại','!'),('Ngoại tuyến','Hiển thị nội dung cache và trạng thái kết nối','↯'),('Không có quyền','Không tiết lộ dữ liệu nhạy cảm','⊘'),('Xung đột phiên bản','Yêu cầu đọc lại trước khi ghi đè','↻')]
    for i,(a,b,ic) in enumerate(states):
        col=i%3;row=i//3;xx=258+col*382;yy=184+row*330
        out += rect(xx,yy,358,284,'#FFFFFF',BRAND['line'],18,extra='filter="url(#tinyShadow)"')+circle(xx+179,yy+82,36,BRAND['soft'])+tx(xx+179,yy+92,ic,28,900,BRAND['primary'],'middle')+tx(xx+179,yy+150,a,16,900,BRAND['ink'],'middle')+paragraph(xx+34,yy+184,b,42,11,BRAND['muted'],18,3)+btn(xx+82,yy+230,194,'Hành động phù hợp',False,38)
    return out


def desktop_scene(item: dict[str, Any]) -> str:
    group=item['group']
    if group=='Xác thực': return auth_scene(item)
    if group=='Bảng tin': return feed_scene(item)
    if group=='Hồ sơ': return profile_scene(item)
    if group=='Thiết lập': return settings_scene(item)
    if group=='Khám phá': return discovery_scene(item)
    if group=='Thông báo': return notification_scene(item)
    if group=='Cộng đồng': return community_scene(item)
    if group=='Trò chuyện': return chat_scene(item)
    if group=='RTC': return rtc_scene(item)
    if group=='Phương tiện': return media_scene(item)
    if group=='Thương mại': return market_scene(item)
    if group=='AI': return ai_scene(item)
    if group=='Điều hành': return moderation_scene(item)
    if group=='Hệ thống': return system_scene(item)
    return app_shell('Trang chủ')+screen_title(258,118,item['title'])


def mobile_post_card(x: float, y: float, w: float, h: float = 486, transcript: bool = False) -> str:
    out = rect(x, y, w, h, '#FFFFFF', BRAND['line'], 18)
    out += avatar(x + 34, y + 36, 20, 'L', '#FF8B6A', 'online')
    out += tx(x + 68, y + 30, 'Linh Nguyễn', 13, 800)
    out += tx(x + 68, y + 50, '2 giờ · Bạn bè', 10, 500, BRAND['muted'])
    out += tx(x + w - 24, y + 36, '...', 16, 800, BRAND['muted'], 'middle')
    out += paragraph(x + 20, y + 86, 'Một khoảnh khắc nhỏ, nhưng đủ khiến cả ngày trở nên đáng nhớ.', 42, 11, BRAND['ink'], 18, 2)
    media_y = y + 126
    media_h = 238 if not transcript else 210
    out += rect(x + 20, media_y, w - 70, media_h, 'url(#media)', 'none', 14)
    out += circle(x + (w - 30) / 2, media_y + media_h / 2, 27, '#FFFFFF', 'none', 1, 'opacity=".92"')
    out += tx(x + (w - 30) / 2 + 2, media_y + media_h / 2 + 7, '▶', 20, 800, BRAND['primary'], 'middle')
    out += pill(x + 30, media_y + 14, 88, '01:42 · HD', '#07162BCC', '#FFFFFF')
    action_x = x + w - 34
    for i, (ic, count) in enumerate([('♡','1,2K'),('○','128'),('R','45')]):
        yy = media_y + 30 + i * 66
        out += circle(action_x, yy, 17, BRAND['surface2'], BRAND['line'])
        out += tx(action_x, yy + 5, ic, 14, 800, BRAND['ink'], 'middle')
        out += tx(action_x, yy + 31, count, 9, 700, BRAND['muted'], 'middle')
    if transcript:
        out += rect(x + 20, media_y + media_h + 14, w - 40, 54, BRAND['surface2'], 'none', 10)
        out += tx(x + 34, media_y + media_h + 35, 'Phiên âm', 9, 800, BRAND['primary'])
        out += tx(x + 34, media_y + media_h + 52, '“Hôm nay mình muốn kể về một ý tưởng nhỏ...”', 9, 500, BRAND['muted'])
        line_y = media_y + media_h + 80
    else:
        line_y = media_y + media_h + 16
    out += line(x + 20, line_y, x + w - 20, line_y)
    out += tx(x + 24, line_y + 34, '◇ Lưu', 11, 700)
    out += tx(x + 132, line_y + 34, '↗ Chia sẻ', 11, 700)
    return out


def mobile_content_preview(x: float, y: float, w: float, h: float = 236) -> str:
    out = rect(x, y, w, h, '#FFFFFF', BRAND['line'], 14)
    out += avatar(x + 28, y + 30, 17, 'L', '#FF8B6A')
    out += tx(x + 54, y + 27, 'Linh Nguyễn', 10, 800)
    out += tx(x + 54, y + 43, '2 giờ · Bạn bè', 8, 500, BRAND['muted'])
    out += paragraph(x + 16, y + 76, 'Một khoảnh khắc nhỏ trong ngày.', 38, 10, BRAND['ink'], 16, 2)
    out += rect(x + 16, y + 116, w - 32, 82, 'url(#media)', 'none', 10)
    out += tx(x + 16, y + h - 14, '♡ 128   ○ 24   ↗ Chia sẻ', 9, 700, BRAND['muted'])
    return out


def mobile_header(active: str='Trang chủ') -> str:
    out=rect(0,0,390,844,BRAND['surface2'],'none',0)
    out+=rect(0,0,390,60,'#FFFFFF',BRAND['line'],0)+rect(14,10,40,40,'url(#brand)','none',11)+tx(34,37,'T',18,900,'#FFFFFF','middle')+tx(64,28,'Twight Light',14,900)+tx(64,44,'Multi Social Comunity',8,600,BRAND['muted'])
    out+=icon_button(292,11,'Tìm','T',False,38)+avatar(360,30,18,'M','#6C5CE7','online')
    # top category strip
    labels=['Trang chủ','Video','Mua bán','Cộng đồng']
    for i,l in enumerate(labels):
        out+=tx(50+i*96,88,l,10,800 if l==active else 600,BRAND['primary'] if l==active else BRAND['muted'],'middle')
    out+=line(0,102,390,102)
    # bottom nav
    out+=rect(0,782,390,62,'#FFFFFF',BRAND['line'],0)
    nav=[('H','Nhà'),('V','Video'),('+','Đăng'),('C','Tin'),('M','Tôi')]
    for i,(ic,lab) in enumerate(nav):
        x=39+i*78
        if i==2: out+=circle(x,802,22,BRAND['primary'])+tx(x,809,ic,22,800,'#FFFFFF','middle')
        else: out+=tx(x,806,ic,17,800,BRAND['primary'] if i==0 else BRAND['muted'],'middle')
        out+=tx(x,828,lab,8,700,BRAND['primary'] if i==0 else BRAND['muted'],'middle')
    return out


def mobile_auth(item: dict[str,Any]) -> str:
    sid=item['id'];out=rect(0,0,390,844,'#F8FAFC','none',0)
    out+=rect(0,0,390,230,'url(#twilight)','none',0)
    out+=rect(18,18,40,40,'url(#brand)','none',11)+tx(38,45,'T',18,900,'#FFFFFF','middle')+tx(68,32,'Twight Light',14,900,'#FFFFFF')+tx(68,49,'Multi Social Comunity',8,600,'#DDE1FF')
    # moving avatar band
    for i,(x,y,c) in enumerate([(40,100,'#F97376'),(112,142,'#6C5CE7'),(190,94,'#10B981'),(274,152,'#3B82F6'),(348,104,'#EC4899')]):
        out+=avatar(x,y,24,str(i+1),c,'online' if i%2==0 else '')
    out+=tx(20,202,'One human, boring!!! One million humans, Nice, very nice',9,800,'#FFFFFF')
    title={'AUTH-01':'Bắt đầu cùng Twight Light','AUTH-02':'Chào mừng trở lại','AUTH-03':'Tạo tài khoản','AUTH-04':'Quên mật khẩu','AUTH-05':'Mật khẩu mới'}[sid]
    out+=tx(20,272,title,22,900)
    y=318
    if sid=='AUTH-01':
        out+=paragraph(20,y,'Kết nối cá tính, khám phá cộng đồng và tạo nên điều đáng nhớ.',46,12,BRAND['muted'],19,3)+btn(20,402,350,'Đăng ký miễn phí',True,48)+btn(20,464,350,'Đăng nhập',False,48)+btn(20,548,350,'Khám phá Twight Light',True,50)
    elif sid=='AUTH-02':
        out+=input_box(20,y,350,'Email hoặc tên người dùng','minhsang@example.com','ok')+input_box(20,y+78,350,'Mật khẩu','••••••••')+tx(20,y+154,'☐ Ghi nhớ',10,600,BRAND['muted'])+tx(370,y+154,'Quên mật khẩu?',10,700,BRAND['primary'],'end')+btn(20,y+178,350,'Đăng nhập',True,48)+btn(20,y+240,350,'Tiếp tục với Google',False,46)+toast(68,696,'Đăng nhập thành công','Đang mở Trang chủ.','success',302)
    elif sid=='AUTH-03':
        out+=input_box(20,y,350,'Tên người dùng','minhsang','ok')+input_box(20,y+70,350,'Email','minhsang@example.com','ok')+input_box(20,y+140,350,'Mật khẩu','••••••••','ok')+input_box(20,y+210,350,'Xác nhận mật khẩu','•••••••','bad')+tx(20,y+275,'Mật khẩu xác nhận chưa khớp.',10,600,BRAND['danger'])+btn(20,y+300,350,'Tạo tài khoản',True,48)
    elif sid=='AUTH-04':
        out+=input_box(20,y,350,'Email','minhsang@example.com','ok')+btn(20,y+80,350,'Gửi mã xác minh',True,48)+paragraph(20,y+152,'Mã 6 chữ số có hiệu lực trong 10 phút.',45,11,BRAND['muted'],18,2)+toast(68,628,'Đã gửi mã','Kiểm tra hộp thư của bạn.','success',302)
    elif sid=='AUTH-05':
        out+=pill(20,y,178,'✓ Mã xác minh hợp lệ','#DCFCE7','#15803D')+input_box(20,y+58,350,'Mật khẩu mới','••••••••','ok')+input_box(20,y+136,350,'Xác nhận mật khẩu','••••••••','ok')+btn(20,y+222,350,'Đổi mật khẩu',True,48)+toast(52,650,'Đổi mật khẩu thành công','Mọi phiên cũ đã đăng xuất.','success',320)
    return out


def mobile_generic(item: dict[str, Any]) -> str:
    sid=item['id']; group=item['group']
    active='Mua bán' if group=='Thương mại' else 'Video' if group in {'Phương tiện'} or sid=='FEED-05' else 'Cộng đồng' if group=='Cộng đồng' else 'Trang chủ'
    out=mobile_header(active)
    out+=tx(16,132,item['title'],20,900)
    out+=tx(16,154,'Bản mobile được suy ra từ desktop vòng duyệt 2.',9,600,BRAND['muted'])
    # custom compositions
    if sid=='FEED-01':
        out+=sticky_composer(12,170,366)+mobile_post_card(12,258,366,486,False)
    elif sid in {'FEED-02','FEED-04'}:
        out+=rect(12,174,366,584,'#FFFFFF',BRAND['line'],16)+avatar(38,210,18,'M','#6C5CE7','online')+tx(68,208,'Phạm Minh Sáng',11,800)+pill(68,220,142,'Bạn bè · Tùy chỉnh',BRAND['surface2'],BRAND['ink'])
        tools=['B','I','H1','•','☺'];
        for i,t in enumerate(tools):out+=icon_button(20+i*48,270,t,t,i==0,38)
        out+=rect(20,324,350,170,'#FFFFFF',BRAND['line'],12)+paragraph(34,354,'Hôm nay mình muốn chia sẻ...',40,12,BRAND['ink'],20,5)
        out+=tx(20,532,'Ảnh và video',11,800)+rect(20,550,104,74,'url(#media)','none',10)+rect(134,550,104,74,'url(#media)','none',10)+rect(248,550,104,74,BRAND['surface2'],BRAND['line'],10)+tx(300,594,'+',18,800,BRAND['primary'],'middle')
        out+=btn(20,676,114,'Hủy',False,42)+btn(212,676,140,'Đăng bài' if sid=='FEED-02' else 'Lưu',True,42)
    elif sid=='FEED-03':
        out+=rect(0,102,390,680,'#0B1020','none',0,opacity=.35)+rect(8,120,374,650,'#FFFFFF',BRAND['line'],18,extra='filter="url(#shadow)"')+tx(24,152,'Chi tiết bài viết',15,900)+tx(360,152,'×',18,800,BRAND['muted'],'middle')+mobile_post_card(18,174,354,390,True)+pill(20,582,76,'Mới nhất',BRAND['soft'],BRAND['primary'])+pill(104,582,62,'Tất cả',BRAND['surface2'],BRAND['muted'])+rect(20,622,350,84,BRAND['surface2'],'none',12)+tx(34,646,'An Trần',10,800)+paragraph(34,666,'Video hay quá!  ♡ Thích · ↩ Trả lời · •••',42,10,BRAND['ink'],16,2)+btn(20,718,350,'Xem thêm bình luận',False,38)
    elif sid=='FEED-05':
        out+=rect(12,174,366,570,'#FFFFFF',BRAND['line'],16)+tx(28,210,'72% · Đang xử lý ở nền',13,900,BRAND['primary'])+rect(28,232,334,14,'#E8ECF3','none',7)+rect(28,232,240,14,'url(#brand)','none',7)+tx(28,286,'Chọn ảnh thu nhỏ',11,800)
        for i in range(3):out+=rect(28+i*112,306,100,68,'url(#media)',BRAND['primary'] if i==1 else BRAND['line'],9,3 if i==1 else 1)
        out+=btn(28,398,190,'Tải ảnh từ máy',False,40)+tx(28,462,'☑ Tự động đăng khi xong',11,700)+tx(28,496,'☐ Lưu thành bản nháp',11,700)+tx(28,530,'☐ Lên lịch đăng',11,700)+btn(28,584,334,'Đóng và chạy nền',True,44)+toast(42,668,'Xử lý thất bại','Âm thanh không hợp lệ.','error',306)
    elif sid in {'PROF-01','PROF-02'}:
        out+=rect(0,166,390,150,'url(#twilight)','none',0)+avatar(70,304,48,'M' if sid=='PROF-01' else 'A','#6C5CE7','online')+rect(102,274,88,38,'#FFFFFF',BRAND['line'],16)+tx(146,298,'☁ Vui',10,800,BRAND['primary'],'middle')+tx(20,374,'Phạm Minh Sáng (Sáng)' if sid=='PROF-01' else 'An Trần (Annie)',18,900)+tx(20,398,'3,4K người theo dõi · 486 đang theo dõi',10,600,BRAND['muted'])+btn(20,426,166,'Chỉnh sửa hồ sơ' if sid=='PROF-01' else 'Nhắn tin',False,40)+btn(196,426,174,'Cửa hàng' if sid=='PROF-01' else 'Theo dõi',True,40)+section_card(12,486,366,112,'Spotify · Night Changes','One Direction · ▶')+section_card(12,612,366,132,'Thông tin cá nhân','Backend .NET · TP.HCM · Tham gia 09/2026')
    elif sid=='PROF-03':
        out+=rect(12,174,366,584,'#FFFFFF',BRAND['line'],16)+rect(20,192,350,90,'url(#twilight)','none',12)+btn(232,206,128,'Đổi ảnh bìa',False,36)+avatar(62,286,38,'M','#6C5CE7','online')+input_box(20,350,350,'Tên hiển thị','Phạm Minh Sáng','ok')+input_box(20,422,350,'Biệt danh','Sáng')+input_box(20,494,350,'Email','minhsang@example.com','ok')+input_box(20,566,350,'Số điện thoại','0901 234 567','ok')+input_box(20,638,350,'Công việc','Lập trình viên')+btn(220,710,150,'Lưu',True,42)
    elif sid=='PROF-04':
        out+=pill(16,174,126,'Người theo dõi',BRAND['soft'],BRAND['primary'])+pill(152,174,126,'Đang theo dõi',BRAND['surface2'],BRAND['muted'])
        names=['An Trần','Lê Vân','Huy Đỗ','Mai Phạm']
        for i,n in enumerate(names):
            yy=244+i*112;out+=rect(12,yy-36,366,94,'#FFFFFF',BRAND['line'],14)+avatar(42,yy,20,n[0],['#F97376','#10B981','#3B82F6','#EC4899'][i],'online' if i%2==0 else 'offline')+tx(74,yy-6,n,11,800)+tx(74,yy+14,'@'+n.lower().replace(' ',''),9,500,BRAND['muted'])+btn(250,yy-22,112,'Hủy theo dõi',False,36)
        out+=tx(195,744,'‹  1  2  3  ›',11,800,BRAND['primary'],'middle')
    elif group=='Thiết lập':
        out+=pill(16,174,94,'Riêng tư',BRAND['soft'] if sid=='SET-01' else BRAND['surface2'],BRAND['primary'] if sid=='SET-01' else BRAND['muted'])+pill(118,174,84,'Bảo mật',BRAND['soft'] if sid=='SET-02' else BRAND['surface2'],BRAND['primary'] if sid=='SET-02' else BRAND['muted'])+pill(210,174,78,'Đã chặn',BRAND['soft'] if sid=='SET-03' else BRAND['surface2'],BRAND['primary'] if sid=='SET-03' else BRAND['muted'])+pill(296,174,78,'Xóa',BRAND['soft'] if sid=='SET-04' else BRAND['surface2'],BRAND['primary'] if sid=='SET-04' else BRAND['muted'])
        out+=rect(12,222,366,530,'#FFFFFF',BRAND['line'],16)
        if sid=='SET-01':
            out+=tx(28,258,'Ai có thể xem hồ sơ?',12,900)+pill(28,278,92,'Bạn bè',BRAND['soft'],BRAND['primary'])+pill(128,278,92,'Tùy chọn',BRAND['surface2'],BRAND['muted'])+tx(28,346,'Ai có thể nhắn tin và xem?',12,900)+pill(28,366,92,'Bạn bè',BRAND['soft'],BRAND['primary'])+pill(128,366,92,'Tùy chọn',BRAND['surface2'],BRAND['muted'])+tx(28,434,'Tìm bằng thông tin cá nhân',12,900)+tx(28,466,'☑ Email   ☑ Số điện thoại   ☑ Tên người dùng',10,700)+tx(28,534,'Trạng thái hoạt động',12,900)+pill(270,514,78,'Bật',BRAND['soft'],BRAND['primary'])+rect(28,584,334,72,'#FFF7ED','#FED7AA',12)+paragraph(44,612,'Có thông báo khi người lạ xem hồ sơ hoặc nhắn tin.',44,10,'#9A3412',16,3)+btn(212,690,150,'Lưu',True,42)
        elif sid=='SET-02':
            out+=tx(28,258,'Đổi mật khẩu',12,900)+input_box(28,284,334,'Mật khẩu hiện tại','••••••••')+input_box(28,356,334,'Mật khẩu mới','••••••••','ok')+btn(212,430,150,'Đổi mật khẩu',True,40)+line(28,490,362,490)+tx(28,526,'Phiên đăng nhập',12,900)+tx(28,562,'Windows · Edge   ·   Hiện tại',10,700)+tx(28,606,'Android · Chrome   ·   Cần OTP',10,700)+btn(28,646,150,'Đăng xuất',False,40)+btn(188,646,174,'Đăng xuất tất cả',True,40)
        elif sid=='SET-03':
            for i,(n,r) in enumerate([('Nguyễn A','Spam liên tục'),('Trần B','Quấy rối'),('Lê C','Không muốn tương tác')]):
                yy=286+i*126;out+=avatar(44,yy,20,n[0],['#F97376','#10B981','#3B82F6'][i],'offline')+tx(76,yy-6,n,11,800)+tx(76,yy+14,'Lý do: '+r,9,600,BRAND['muted'])+btn(250,yy-20,104,'Bỏ chặn',False,36)+line(28,yy+46,362,yy+46)
            out+=rect(28,642,334,72,'#FFF7ED','#FED7AA',12)+paragraph(44,670,'Cảnh báo khi gặp trong cộng đồng chung.',42,10,'#9A3412',16,2)
        else:
            out+=rect(28,258,334,78,'#FEF2F2','#FECACA',12)+paragraph(44,286,'Khóa truy cập ngay; xóa cứng sau 30 ngày nếu không khôi phục.',40,10,'#991B1B',16,3)+input_box(28,376,334,'Mật khẩu','••••••••')+input_box(28,448,334,'OTP qua email','123 456','ok')+tx(28,530,'☐ Tôi hiểu và muốn tiếp tục',10,700)+btn(28,580,334,'Yêu cầu xóa tài khoản',True,42)
    elif sid=='DISC-01':
        out+=rect(12,174,366,46,'#FFFFFF',BRAND['line'],23)+tx(28,203,'⌕ thiết kế hệ thống',11,600)+pill(16,238,82,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(106,238,82,'Người', '#EAF2FF','#1D4ED8')+pill(196,238,82,'Bài viết','#FDF2F8','#BE185D')+pill(286,238,90,'Cộng đồng','#ECFDF5','#047857')
        out+=tx(16,302,'Bạn đang theo dõi',11,900,'#1D4ED8')
        results=[('An Trần','Khớp gần đúng: thiết kế','user'),('Thiết kế hệ thống mạng xã hội','Linh Nguyễn · 2 giờ','post'),('UI/UX Việt Nam','48,2K thành viên','comm')]
        for i,(a,b,k) in enumerate(results):
            yy=350+i*116;bg={'user':'#EEF5FF','post':'#FFF1F7','comm':'#ECFDF5'}[k];out+=rect(12,yy-38,366,94,bg,'none',14)+avatar(44,yy,20,a[0],['#3B82F6','#EC4899','#10B981'][i])+tx(76,yy-8,a,11,900)+tx(76,yy+14,b,9,600,BRAND['muted'])
    elif sid=='NOTI-01':
        out+=pill(16,174,84,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(108,174,84,'Đề cập',BRAND['surface2'],BRAND['muted'])+icon_button(336,169,'Chuông','N',False,38)
        notes=['Linh đã thích bài viết','Bạn được đề cập trong #backend','An đã gửi tin nhắn','UI/UX Việt Nam có bài nổi bật']
        for i,n in enumerate(notes):
            yy=250+i*106;out+=rect(12,yy-36,366,88,'#F7F5FF' if i<2 else '#FFFFFF',BRAND['line'],14)+circle(44,yy,18,BRAND['soft'])+tx(44,yy+5,'@' if i==1 else '♥',12,800,BRAND['primary'],'middle')+tx(74,yy-4,n,11,800)+tx(74,yy+16,str(2+i*8)+' phút',9,600,BRAND['muted'])+tx(348,yy+4,'N',12,700,BRAND['muted'],'end')
        out+=btn(20,700,350,'Xem tất cả thông báo',False,40)
    elif group=='Cộng đồng':
        if sid=='COMM-01':
            cats=['Thời sự','Công nghệ','Giải trí','Thể thao','Du lịch','Tâm sự']
            for i,c in enumerate(cats):out+=pill(12+(i%3)*124,176+(i//3)*38,116,c,BRAND['soft'] if i in {0,1} else '#FFFFFF',BRAND['primary'] if i in {0,1} else BRAND['muted'])
            for i,(n,m) in enumerate([('UI/UX Việt Nam','48,2K thành viên'),('Backend .NET','21,4K thành viên')]):
                yy=292+i*218;out+=rect(12,yy,366,198,'#FFFFFF',BRAND['line'],14)+rect(12,yy,366,80,'url(#media)','none',14)+tx(28,yy+116,n,13,900)+tx(28,yy+140,m,10,600,BRAND['muted'])+btn(28,yy+152,130,'Tham gia',True,36)+btn(168,yy+152,180,'Không quan tâm',False,36)
        elif sid=='COMM-02':
            out+=rect(0,170,390,150,'url(#twilight)','none',0)+tx(20,268,'UI/UX Việt Nam',20,900,'#FFFFFF')+tx(20,292,'48.240 thành viên',10,600,'#E5E7FF')+btn(20,334,98,'Mời',False,36)+btn(128,334,98,'Chia sẻ',False,36)+btn(236,334,134,'Đã tham gia',True,36)+sticky_composer(12,390,366)+section_card(12,478,366,150,'Quy tắc cộng đồng','Bạn đã chấp thuận 3/3 quy tắc')+section_card(12,642,366,110,'Thông báo cộng đồng','Yêu thích · Ưu tiên bài mới')
        elif sid=='COMM-03':
            out+=rect(12,174,366,560,'#FFFFFF',BRAND['line'],16)+rect(24,190,342,100,'url(#twilight)','none',12)+tx(36,258,'UI/UX Việt Nam',16,900,'#FFFFFF')+tx(28,334,'Điều kiện tham gia',12,900)
            for i,c in enumerate(['Đồng ý quy tắc cộng đồng','Hiểu chính sách ban','Nhận thông báo quan trọng']):out+=tx(28,378+i*54,'☑ '+c,11,700)
            out+=rect(28,552,334,72,'#FFF7ED','#FED7AA',12)+paragraph(44,580,'Ban vĩnh viễn phải có lý do và audit.',40,10,'#9A3412',16,3)+btn(28,660,334,'Chấp thuận và tham gia',True,42)
        elif sid=='COMM-04':
            out+=rect(12,174,366,566,'#FFFFFF',BRAND['line'],16)+tx(28,210,'Chỉ chủ sở hữu',11,800,BRAND['primary'])
            roles=['Chủ sở hữu','Điều phối','Thành viên','Khách']
            for i,r in enumerate(roles):out+=pill(28,238+i*56,150,r,BRAND['soft'] if i==0 else BRAND['surface2'],BRAND['primary'] if i==0 else BRAND['muted'])+pill(210,238+i*56,140,'Quyền riêng ⌄',BRAND['surface2'],BRAND['ink'])
            out+=tx(28,492,'Khách / thành viên chỉ xem danh sách thành viên;',10,600,BRAND['muted'])+tx(28,510,'không thấy hành động cảnh báo hoặc ban.',10,600,BRAND['muted'])+btn(212,676,150,'Lưu quyền',True,42)
        elif sid=='COMM-05':
            out+=pill(16,174,120,'Kênh',BRAND['soft'],BRAND['primary'])+pill(146,174,166,'Chờ duyệt (3)',BRAND['surface2'],BRAND['muted'])
            chans=['# chào-mừng','# thông-báo','# trò-chuyện','🔊 Phòng chung']
            for i,c in enumerate(chans):out+=rect(12,232+i*64,366,50,BRAND['soft'] if i==2 else '#FFFFFF',BRAND['line'],12)+tx(28,263+i*64,c,11,800 if i==2 else 600,BRAND['primary'] if i==2 else BRAND['ink'])+tx(350,263+i*64,'⋮',16,800,BRAND['muted'],'end')
            out+=btn(12,512,366,'+ Tạo kênh mới',True,42)+section_card(12,570,366,160,'Duyệt thành viên','Duyệt, từ chối hoặc mở danh sách cấm')
        elif sid=='COMM-06':
            people=['An Trần','Lê Vân','Huy Đỗ','Mai Phạm']
            for i,n in enumerate(people):
                yy=212+i*118;out+=rect(12,yy,366,96,'#FFFFFF',BRAND['line'],14)+avatar(42,yy+42,20,n[0],['#F97376','#10B981','#3B82F6','#EC4899'][i],'online' if i%2==0 else 'offline')+tx(74,yy+36,n,11,800)+tx(74,yy+56,'Thành viên',9,600,BRAND['muted'])+btn(238,yy+28,58,'!',False,36)+btn(304,yy+28,58,'Ban',False,36)
        else:
            out+=rect(12,174,366,562,'#FFFFFF',BRAND['line'],16)+tx(28,210,'# trò-chuyện',13,900)+tx(28,230,'125 thành viên',9,600,BRAND['muted'])
            msgs=[('An','Mọi người thấy bản mới thế nào?'),('Sáng','Mình đang đồng bộ mobile.'),('Lê Vân','Mình thích đó!')]
            for i,(n,m) in enumerate(msgs):
                yy=286+i*112;mine=i==1;out+=rect(92 if mine else 28,yy-30,266 if mine else 284,62,BRAND['soft'] if mine else BRAND['surface2'],'none',14)+tx((108 if mine else 44),yy-5,n,10,800,BRAND['primary'] if mine else BRAND['ink'])+tx((108 if mine else 44),yy+16,m,10,600)+tx((108 if mine else 44),yy+50,'♡  ↩  •••',9,700,BRAND['muted'])
            out+=tx(28,606,'An đang nhập  • • •',9,600,BRAND['muted'])+rect(20,638,350,80,'#FFFFFF',BRAND['line'],14)+icon_button(28,650,'Tệp','+',False,38)+tx(78,675,'Nhắn tin...',10,500,'#94A3B8')+btn(318,650,42,'➤',True,38)
    elif group=='Trò chuyện':
        if sid=='CHAT-01':
            convs=[('An Trần','Bạn xem giúp mình bản mới nhé','3'),('Nhóm Đồ án','Build đã chạy xong','12'),('Lê Vân','Đã gửi một ảnh','')]
            for i,(n,m,u) in enumerate(convs):
                yy=190+i*118;out+=rect(12,yy,366,96,'#FFFFFF',BRAND['line'],14)+avatar(42,yy+42,20,n[0],['#F97376','#6C5CE7','#10B981'][i],'online' if i!=1 else 'offline')+tx(74,yy+34,n,11,900)+tx(74,yy+56,m,9,600,BRAND['muted'])
                if u:out+=circle(346,yy+42,12,BRAND['primary'])+tx(346,yy+46,u,8,800,'#FFFFFF','middle')
                if i==1:out+=tx(316,yy+62,'🔕',12,700,BRAND['muted'])
            out+=btn(20,682,350,'+ Hội thoại mới',True,42)
        elif sid=='CHAT-02':
            out+=rect(0,166,390,54,'#FFFFFF',BRAND['line'],0)+avatar(26,193,18,'A','#F97376','online')+tx(54,190,'An Trần',11,900)+tx(54,208,'Đang hoạt động',8,600,BRAND['green'])+icon_button(294,174,'Gọi','A',False,36)+icon_button(336,174,'Video','V',False,36)
            msgs=[('An','Bạn đã hoàn thiện desktop chưa?'),('Me','Mình đang đồng bộ mobile.'),('An','Gửi mình xem nhé!')]
            for i,(n,m) in enumerate(msgs):
                yy=278+i*106;mine=n=='Me';out+=rect(82 if mine else 16,yy-28,288 if mine else 318,62,BRAND['soft'] if mine else '#FFFFFF',BRAND['line'] if not mine else 'none',14)+tx((98 if mine else 32),yy+6,m,10,700)
            out+=rect(12,632,366,116,'#FFFFFF',BRAND['line'],14)+icon_button(20,646,'Tệp','+',False,38)+tx(70,672,'Nhập tin nhắn...',10,500,'#94A3B8')+btn(318,646,42,'➤',True,38)+tx(70,724,'Enter gửi · Shift+Enter xuống dòng',8,600,BRAND['muted'])
        elif sid=='CHAT-03':
            out+=rect(12,174,366,530,'#FFFFFF',BRAND['line'],16)+rect(20,192,350,42,BRAND['surface2'],BRAND['line'],21)+tx(36,218,'⌕ Tìm người...',10,500,'#94A3B8')
            for i,n in enumerate(['An Trần','Lê Vân','Huy Đỗ','Mai Phạm']):
                yy=280+i*82;out+=avatar(44,yy,20,n[0],['#F97376','#10B981','#3B82F6','#EC4899'][i],'online' if i<2 else 'offline')+tx(76,yy-4,n,11,800)+circle(346,yy,10,'#FFFFFF',BRAND['primary'],2)+(circle(346,yy,5,BRAND['primary']) if i<2 else '')+line(28,yy+36,362,yy+36)
            out+=btn(20,648,350,'Bắt đầu trò chuyện',True,42)
        else:
            out+=rect(12,174,366,544,'#FFFFFF',BRAND['line'],16)
            settings=[('Danh hiệu trong nhóm','Backend Lead'),('Chủ đề','Twilight Purple'),('Tin nhắn ghim','5 mục'),('Thông báo','Chỉ đề cập')]
            for i,(a,b) in enumerate(settings):
                yy=226+i*92;out+=tx(28,yy,a,11,800)+pill(188,yy-22,170,b,BRAND['surface2'],BRAND['ink'])+line(28,yy+28,362,yy+28)
            out+=rect(28,602,334,76,BRAND['surface2'],BRAND['line'],12)+tx(44,630,'Rời nhóm trong im lặng',11,900)+tx(44,650,'Không thông báo cho thành viên khác.',9,600,BRAND['muted'])
    elif group=='RTC':
        out=rect(0,0,390,844,'#090B12','none',0)+rect(0,0,390,58,'#111522','none',0)+rect(12,9,40,40,'url(#brand)','none',11)+tx(32,36,'T',18,900,'#FFFFFF','middle')+tx(62,28,'Twight Light Call',13,900,'#FFFFFF')+tx(62,44,'Cửa sổ riêng',8,600,'#AAB2C7')
        if sid=='RTC-01':
            out+=avatar(195,230,64,'A','#F97376','online')+tx(195,330,'An Trần đang gọi',22,900,'#FFFFFF','middle')+tx(195,358,'Cuộc gọi video · Nhóm Đồ án',10,600,'#AAB2C7','middle')+circle(128,504,34,'#EF4444')+tx(128,512,'×',24,900,'#FFFFFF','middle')+circle(262,504,34,'#10B981')+tx(262,512,'✓',24,900,'#FFFFFF','middle')
        elif sid=='RTC-02':
            out+=tx(16,92,'Phòng chung · TW-8F2K',11,800,'#FFFFFF')+pill(248,70,126,'Lưới ⌄','#232B42','#FFFFFF')
            for i in range(4):
                x=12+(i%2)*188;y=120+(i//2)*190;out+=rect(x,y,178,170,'url(#media)' if i<3 else '#1B2233','#283044',12)+avatar(x+30,y+30,18,str(i+1),['#F97376','#6C5CE7','#10B981','#3B82F6'][i],'online')+pill(x+12,y+132,100,['An','Sáng','Lê Vân','Phạm Thư'][i],'#07162BCC','#FFFFFF')
            out+=pill(14,510,136,'Tham gia thoại','#10B981','#FFFFFF')+btn(14,558,92,'Mic ⌄',False,38)+btn(114,558,104,'Cam ⌄',False,38)+btn(226,558,148,'Mời / mã phòng',False,38)+rect(12,614,366,140,'#111522','#283044',12)+tx(28,642,'Chat: Tất cả · Riêng tư',10,800,'#FFFFFF')+rect(24,690,342,46,'#1B2233','#303A54',12)+tx(40,718,'Nhắn trong phòng...',9,500,'#818AA4')
        else:
            out+=rect(12,78,366,400,'url(#media)','none',14)+pill(24,92,190,'Đang chia sẻ màn hình','#07162BCC','#FFFFFF')+rect(254,352,104,82,'#181E2E','#303A54',10)+avatar(306,384,24,'M','#6C5CE7','online')+tx(306,424,'Camera bạn',8,700,'#FFFFFF','middle')+tx(20,530,'Camera bản thân',10,700,'#AAB2C7')+pill(246,508,120,'Bật','#232B42','#FFFFFF')+tx(20,580,'Mic / Loa',10,700,'#AAB2C7')+pill(246,558,120,'Thiết bị ⌄','#232B42','#FFFFFF')+tx(20,630,'Ghi hình',10,700,'#AAB2C7')+pill(220,608,146,'Cần xin phép','#3A1820','#FCA5A5')+btn(20,690,350,'Dừng chia sẻ',True,42)
    elif sid=='MEDIA-01':
        out+=rect(12,174,366,552,'#FFFFFF',BRAND['line'],16)+rect(20,194,350,140,'#F7F5FF','#AFA6F3',12,2,extra='stroke-dasharray="8 8"')+tx(195,248,'UP',28,800,BRAND['primary'],'middle')+tx(195,282,'Chọn video từ máy',12,900,BRAND['ink'],'middle')+tx(20,374,'Ảnh thu nhỏ',11,800)+rect(20,392,120,80,'url(#media)','none',10)+btn(154,412,196,'Chọn ảnh / khung',False,38)+pill(20,510,96,'Bản nháp',BRAND['soft'],BRAND['primary'])+pill(126,510,96,'Đăng ngay',BRAND['surface2'],BRAND['muted'])+pill(232,510,96,'Lên lịch',BRAND['surface2'],BRAND['muted'])+input_box(20,566,350,'Thời gian đăng','20:30 · 06/09')+btn(20,646,350,'Bắt đầu tải lên',True,42)
    elif group=='Thương mại':
        if sid=='MKT-01':
            out+=rect(12,174,300,44,'#FFFFFF',BRAND['line'],22)+tx(28,201,'⌕ Tìm sản phẩm...',10,500,'#94A3B8')+icon_button(324,176,'Lọc','⏷',False,40)
            products=[('Bàn phím cơ','1.250.000đ'),('Màn hình 27”','3.900.000đ'),('Máy ảnh Fuji','18.500.000đ'),('Ghế ergonomic','2.200.000đ')]
            for i,(n,p) in enumerate(products):
                x=12+(i%2)*188;y=244+(i//2)*242;out+=rect(x,y,178,222,'#FFFFFF',BRAND['line'],14)+rect(x,y,178,90,'url(#media)','none',14)+tx(x+12,y+122,n,11,900)+tx(x+12,y+146,p,12,900,BRAND['primary'])+tx(x+12,y+166,'Mô tả ngắn...',8,600,BRAND['muted'])+btn(x+12,y+180,70,'Mua',True,30)+btn(x+88,y+180,78,'Liên hệ',False,30)
        elif sid=='MKT-02':
            out+=rect(12,174,366,230,'url(#media)','none',14)+tx(16,442,'Bàn phím cơ Custom',18,900)+tx(16,472,'1.250.000đ',20,900,BRAND['primary'])+tx(16,514,'Phân loại',11,800)+pill(16,532,112,'Switch Red',BRAND['soft'],BRAND['primary'])+pill(136,532,118,'Switch Brown',BRAND['surface2'],BRAND['muted'])+tx(16,594,'Mô tả sản phẩm',11,800)+paragraph(16,620,'Bàn phím 75%, keycap PBT, kết nối ba chế độ...',48,10,BRAND['muted'],17,3)+btn(16,700,170,'Mua sản phẩm',True,42)+btn(196,700,178,'Liên hệ',False,42)
        elif sid=='MKT-03':
            out+=rect(12,174,366,560,'#FFFFFF',BRAND['line'],16)+input_box(20,202,350,'Tên sản phẩm','Bàn phím cơ Custom','ok')+input_box(20,274,350,'Danh mục','Thiết bị công nghệ')+tx(20,360,'Phân loại sản phẩm',11,900)
            for i,(n,p) in enumerate([('Switch Red','1.250.000'),('Switch Brown','1.300.000')]):
                yy=392+i*68;out+=rect(20,yy,164,46,'#FFFFFF',BRAND['line'],10)+tx(32,yy+28,n,10,600)+rect(194,yy,168,46,'#FFFFFF',BRAND['line'],10)+tx(206,yy+28,p,10,600)
            out+=btn(20,536,160,'+ Thêm phân loại',False,38)+tx(20,610,'Ảnh sản phẩm',11,900)+rect(20,628,94,66,'url(#media)','none',9)+rect(124,628,94,66,'url(#media)','none',9)+rect(228,628,94,66,BRAND['surface2'],BRAND['line'],9)+tx(275,669,'+',16,800,BRAND['primary'],'middle')+btn(220,704,142,'Lưu',True,38)
        elif sid=='MKT-04':
            out+=rect(12,174,366,552,'#FFFFFF',BRAND['line'],16)+rect(20,194,110,80,'url(#media)','none',10)+tx(144,214,'Bàn phím cơ Custom',11,900)+tx(144,238,'Switch Red · 1.250.000đ',9,600,BRAND['muted'])+tx(20,320,'Số lượng',11,800)+pill(118,302,110,'−   1   +',BRAND['surface2'],BRAND['ink'])+input_box(20,366,350,'Lời nhắn','Mình muốn xem hàng lúc 18:00')+rect(20,458,350,92,'#FFF7ED','#FED7AA',12)+paragraph(36,488,'Twight Light chỉ kết nối hai bên, không giữ tiền.',42,10,'#9A3412',16,3)+btn(20,590,350,'Gửi yêu cầu mua',True,42)
        elif sid=='MKT-05':
            out+=rect(12,174,366,550,'#FFFFFF',BRAND['line'],16)+tx(28,208,'Thanh toán trực tiếp với người bán',12,900)+rect(64,240,262,262,'#FFFFFF',BRAND['line'],14)
            for r in range(7):
                for c in range(7):
                    if (r*c+r+c)%3!=0:out+=rect(82+c*34,258+r*34,24,24,'#111827','none',2)
            out+=tx(28,548,'Số tiền',10,700,BRAND['muted'])+tx(362,548,'1.250.000đ',18,900,BRAND['primary'],'end')+tx(28,582,'Vietcombank · 0123 456 789',10,800)+tx(28,608,'NGUYEN VAN AN',10,800)+btn(28,646,334,'Tôi đã liên hệ người bán',True,42)
        else:
            out+=pill(16,174,80,'Tất cả',BRAND['soft'],BRAND['primary'])+pill(104,174,90,'Liên hệ',BRAND['surface2'],BRAND['muted'])+pill(202,174,78,'Xong',BRAND['surface2'],BRAND['muted'])+pill(288,174,78,'Đã hủy',BRAND['surface2'],BRAND['muted'])
            for i,(n,s,p) in enumerate([('Bàn phím cơ','Đang liên hệ','1.250.000đ'),('Màn hình 27”','Đã hoàn tất','3.900.000đ'),('Tai nghe','Đã hủy','1.680.000đ')]):
                yy=240+i*136;out+=rect(12,yy,366,112,'#FFFFFF',BRAND['line'],14)+rect(24,yy+18,86,62,'url(#media)','none',10)+tx(124,yy+34,n,11,900)+tx(124,yy+56,p,10,700,BRAND['primary'])+pill(230,yy+22,126,s,BRAND['surface2'],BRAND['muted'])+btn(124,yy+70,232,'Xem / Liên hệ',False,34)
            out+=tx(195,724,'‹  1  2  3  ›',11,800,BRAND['primary'],'middle')
    elif group=='AI':
        if sid=='AI-01':
            out+=sticky_composer(12,170,366)+mobile_content_preview(12,258,366,150)+rect(16,424,358,320,'#FFFFFF',BRAND['line'],18,extra='filter="url(#shadow)"')+rect(16,424,358,54,'url(#brand)','none',18)+tx(36,458,'✦ Trợ lý Twight',13,900,'#FFFFFF')+rect(30,500,286,62,BRAND['surface2'],'none',12)+paragraph(44,526,'Bạn muốn mình hỗ trợ điều gì?',36,10,BRAND['ink'],16,2)+rect(84,582,276,54,BRAND['soft'],'none',12)+tx(98,614,'Gợi ý cộng đồng phù hợp',10,700)+rect(30,652,330,70,'#FFFFFF',BRAND['line'],12)+tx(44,681,'Nhập câu hỏi...',10,500,'#94A3B8')+btn(310,666,38,'➤',True,34)
        else:
            out+=rect(12,174,366,560,'#FFFFFF',BRAND['line'],16)+input_box(20,202,350,'Nguồn','Nhóm Đồ án · #trò-chuyện')+input_box(20,274,350,'Khoảng thời gian','01/09 - 05/09')+tx(20,360,'8.240 / 10.000 dòng',11,900,BRAND['primary'])+rect(20,378,350,14,'#E8ECF3','none',7)+rect(20,378,288,14,'url(#brand)','none',7)+pill(20,424,102,'Điểm chính',BRAND['soft'],BRAND['primary'])+pill(132,424,102,'Chủ đề',BRAND['surface2'],BRAND['muted'])+pill(244,424,102,'Hành động',BRAND['surface2'],BRAND['muted'])+btn(20,490,350,'Tạo tóm tắt',True,42)+section_card(20,550,350,120,'Bản tóm tắt','• Desktop là nguồn mobile\n• Phiên âm nằm trong chat/post')+btn(20,686,170,'Xuất PDF',False,38)+btn(200,686,170,'Sao chép',True,38)
    elif group=='Điều hành':
        if sid=='MOD-01':
            out+=rect(0,102,390,680,'#0B1020','none',0,opacity=.38)+rect(12,150,366,560,'#FFFFFF',BRAND['line'],18)+tx(28,188,'Báo cáo nội dung',16,900)+tx(360,188,'×',18,800,BRAND['muted'],'middle')
            reasons=['Spam','Quấy rối / bắt nạt','Ngôn từ thù ghét','Nội dung nhạy cảm','Lý do khác']
            for i,r in enumerate(reasons):out+=circle(32,240+i*52,8,'#FFFFFF',BRAND['primary'],2)+(circle(32,240+i*52,4,BRAND['primary']) if i==1 else '')+tx(54,245+i*52,r,11,700)
            out+=rect(28,512,334,84,'#FFFFFF',BRAND['line'],12)+tx(42,540,'Mô tả thêm...',10,500,'#94A3B8')+btn(28,630,334,'Gửi báo cáo',True,42)
        elif sid=='MOD-02':
            out+=pill(16,174,108,'Đang chờ',BRAND['soft'],BRAND['primary'])+pill(134,174,108,'Đang duyệt',BRAND['surface2'],BRAND['muted'])+icon_button(334,170,'Lọc','⏷',False,40)
            for i,(r,t,p) in enumerate([('#R-1042','Bài viết · Quấy rối','Cao'),('#R-1041','Bình luận · Spam','TB'),('#R-1039','Tin nhắn · Thù ghét','Cao')]):
                yy=240+i*136;out+=rect(12,yy,366,112,'#FFFFFF',BRAND['line'],14)+tx(28,yy+30,r,11,900,BRAND['primary'])+tx(28,yy+56,t,10,700)+pill(270,yy+18,82,p,'#FEF2F2' if p=='Cao' else '#FFF7ED','#B91C1C' if p=='Cao' else '#9A3412')+btn(28,yy+72,324,'Mở báo cáo',False,34)
            out+=tx(195,718,'‹  1  2  3  ›',11,800,BRAND['primary'],'middle')
        else:
            out+=rect(12,174,366,560,'#FFFFFF',BRAND['line'],16)+mobile_content_preview(20,194,350,250)+input_box(20,508,350,'Hành động','Ẩn bài viết 7 ngày')+rect(20,580,350,76,'#FFFFFF',BRAND['line'],12)+tx(34,608,'Lý do bắt buộc...',10,500,'#94A3B8')+btn(20,674,166,'Từ chối',False,38)+btn(196,674,174,'Áp dụng',True,38)
    else: # system
        states=[('Đang tải','▧'),('Rỗng','○'),('Lỗi','!'),('Ngoại tuyến','↯')]
        for i,(n,ic) in enumerate(states):
            x=12+(i%2)*188;y=186+(i//2)*238;out+=rect(x,y,178,210,'#FFFFFF',BRAND['line'],14)+circle(x+89,y+66,28,BRAND['soft'])+tx(x+89,y+75,ic,22,900,BRAND['primary'],'middle')+tx(x+89,y+122,n,12,900,BRAND['ink'],'middle')+btn(x+20,y+152,138,'Hành động',False,34)
    return out


def mobile_scene(item: dict[str, Any]) -> str:
    if item['group']=='Xác thực': return mobile_auth(item)
    return mobile_generic(item)


def write_svg(path: Path, width: int, height: int, title: str, body: str, footer: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    svg=svg_head(width,height,title)+body+(tx(width-14,height-12,footer,8,700,'#94A3B8','end') if width>500 else '')+'</svg>\n'
    path.write_text(svg,encoding='utf-8')


def update_screen_md(item: dict[str, Any], feedback_note: str) -> None:
    p=ROOT/item['file']; text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): return
    _, front, body=text.split('---\n',2)
    meta=yaml.safe_load(front) or {}
    meta['status']='draft'
    meta['review_round']=2
    if item['id']=='FEED-03' and 'AI-05' not in meta.get('functions',[]): meta.setdefault('functions',[]).append('AI-05')
    if item['id']=='CHAT-02' and 'AI-05' not in meta.get('functions',[]): meta.setdefault('functions',[]).append('AI-05')
    body=body.lstrip()
    body=body.split('\n## Thay đổi đã áp dụng ở vòng 1')[0].rstrip()
    applied=f'''\n\n## Thay đổi đã áp dụng ở vòng 1\n\n- Đổi thương hiệu thành **Twight Light** và dòng mô tả **Multi Social Comunity**.\n- Đồng bộ app shell desktop: điều hướng miền chức năng ở thanh trên, avatar mở menu cá nhân, lối tắt có thể tùy biến bên trái.\n- Dựng lại bố cục desktop theo phản hồi và suy ra bố cục mobile theo cùng thứ tự ưu tiên.\n- Giữ trạng thái `draft` để người duyệt đánh giá vòng 2.\n\n## Bố cục vòng duyệt 2\n\n- Desktop: `assets/editable/svg/desktop/{Path(item['file']).stem}.svg`.\n- Mobile: `assets/editable/svg/mobile/{Path(item['file']).stem}.svg`.\n- PNG chỉ dùng xem nhanh; SVG là nguồn chỉnh sửa.\n\n## Ảnh hưởng hợp đồng và backend\n\nCác chi tiết giao diện mới chỉ được xem là hợp đồng frontend sau khi OpenAPI/AsyncAPI hoặc đặc tả backend tương ứng được cập nhật. Xem `sources/18-backend-contract-gaps.md`.\n\n## Phản hồi gốc đã áp dụng\n\n> {feedback_note.replace(chr(10), chr(10)+'> ')}\n\n## Ghi chú duyệt vòng 2\n\n- Trạng thái: `draft`\n- Người duyệt:\n- Ngày:\n- Thay đổi yêu cầu:\n'''
    dumped=yaml.safe_dump(meta,allow_unicode=True,sort_keys=False).strip()
    p.write_text('---\n'+dumped+'\n---\n\n'+body+applied,encoding='utf-8')


def build_sources() -> None:
    (ROOT/'sources/00-product-goals.md').write_text('''# Mục tiêu sản phẩm\n\n## Thương hiệu\n\n- Tên: **Twight Light**.\n- Dòng mô tả: **Multi Social Comunity**.\n- Slogan: **One human, boring!!! One million humans, Nice, very nice**.\n\n## Lời hứa trải nghiệm\n\nTwight Light giúp người dùng kết nối cá tính, tham gia nhiều cộng đồng, trò chuyện theo thời gian thực, chia sẻ nội dung và giao dịch trực tiếp với người bán trong cùng một sản phẩm.\n\n## Nguyên tắc\n\n1. Nội dung và cộng đồng là trung tâm.\n2. Desktop thiết lập cấu trúc; mobile giữ nguyên mục tiêu nhưng ưu tiên hành động chính.\n3. Quyền riêng tư, trạng thái lỗi và khả năng phục hồi phải nhìn thấy được.\n4. Giao diện không được tự tạo hợp đồng backend chưa được khóa.\n''',encoding='utf-8')
    (ROOT/'sources/02-information-architecture.md').write_text('''# Kiến trúc thông tin vòng 2\n\n## Điều hướng toàn cục desktop\n\n- Thanh trên: Trang chủ, Video, Mua bán, Cộng đồng.\n- Lối tắt trái: nhóm, bạn bè, bài đã lưu, nội dung ghim và tiện ích người dùng chọn.\n- Góc phải: tìm kiếm, tin nhắn, thông báo, trợ lý và avatar mở menu cá nhân.\n- Không đặt nút Tạo bài viết cố định ở thanh trái; composer dính phía trên bảng tin là điểm bắt đầu đăng bài.\n\n## Điều hướng mobile\n\n- Thanh trên: thương hiệu, tìm kiếm và avatar.\n- Thanh danh mục cuộn ngang: Trang chủ, Video, Mua bán, Cộng đồng.\n- Điều hướng đáy: Nhà, Video, Đăng, Tin, Tôi.\n- Các cột phụ desktop chuyển thành drawer, bottom sheet hoặc route con.\n''',encoding='utf-8')
    (ROOT/'sources/03-navigation.md').write_text('''# Điều hướng\n\n## Menu avatar\n\nAvatar ở góc phải chỉ hiển thị hình đại diện. Khi mở, menu gồm Trang cá nhân, Cài đặt, Ngôn ngữ, chế độ sáng/tối và Đăng xuất.\n\n## Lối tắt cá nhân\n\nNgười dùng có thể thêm, bỏ, sắp xếp hoặc ghim nhóm, bạn bè, cộng đồng và nội dung thường dùng.\n\n## Nguyên tắc responsive\n\nMobile không sao chép nguyên ba cột desktop. Nội dung chính ở trước; metadata và tác vụ phụ chuyển sang drawer hoặc sheet.\n''',encoding='utf-8')
    (ROOT/'sources/05-design-system.md').write_text('''# Hệ thống thiết kế Twight Light\n\n## Bảng màu\n\n- Twilight Navy `#07162B`: nền RTC và vùng thương hiệu.\n- Twilight Violet `#6C5CE7`: hành động chính.\n- Electric Blue `#496DFF`: gradient thương hiệu.\n- Coral `#FF6B81`: điểm nhấn cảm xúc.\n- Success `#10B981`, Warning `#F59E0B`, Danger `#EF4444`.\n- Surface `#FFFFFF`, Canvas `#F6F8FC`, Ink `#0B1020`.\n\n## Typography\n\nƯu tiên Inter hoặc Be Vietnam Pro. Fallback DejaVu Sans/Arial. Tối thiểu 16px cho nội dung nhập trên mobile để tránh zoom không chủ đích.\n\n## Hình dạng\n\n- Card 14-20px.\n- Button/input 10-12px.\n- Touch target tối thiểu 44x44px.\n- Focus ring 2px, độ tương phản phù hợp WCAG AA.\n''',encoding='utf-8')
    (ROOT/'sources/06-component-library.md').write_text('''# Thư viện component vòng 2\n\n- `TwightAppShell`, `TopDomainTabs`, `PersonalShortcutRail`, `AvatarMenu`.\n- `StickyPostComposer`, `RichPostEditor`, `PostCard`, `VerticalEngagementRail`, `CommentThread`.\n- `ProfileHero`, `MoodBubble`, `SpotifyProfileCard`, `SellerStoreLink`.\n- `PrivacySelector`, `SessionDeviceList`, `BlockedAccountRow`, `DeletionRecoveryPanel`.\n- `CommunityCategoryWall`, `JoinRuleConsent`, `RolePermissionMatrix`, `MemberApprovalQueue`.\n- `ConversationList`, `MessageBubble`, `MessageComposer`, `SharedMediaPanel`, `InlineTranscript`.\n- `RtcRoom`, `DeviceSelector`, `LayoutSelector`, `RoomChatPanel`, `RecordingConsent`.\n- `VariantEditor`, `SellerContactPanel`, `DirectPaymentQr`, `OrderStatusList`.\n- `FloatingAssistant`, `SummaryBuilder`, `ModerationQueue`.\n''',encoding='utf-8')
    (ROOT/'sources/07-interactions-motion.md').write_text('''# Tương tác và chuyển động\n\n- Vùng auth có avatar vector chuyển động ngang, chéo và theo đường cong; tôn trọng `prefers-reduced-motion`.\n- Toast xuất hiện góc phải desktop và phía dưới thanh trên trên mobile; không che trường nhập hoặc CTA.\n- Composer bảng tin dùng `position: sticky` nhưng không che nội dung khi bàn phím hoặc thanh trình duyệt mobile thay đổi.\n- Tin nhắn đang gửi: chấm động; lỗi: nhãn “Gửi lỗi” kèm nút thử lại.\n- Enter gửi, Shift+Enter xuống dòng; phải cấu hình được cho accessibility.\n- Bài viết chi tiết mở ở layer trên desktop và route toàn màn hình trên mobile.\n''',encoding='utf-8')
    (ROOT/'sources/08-responsive.md').write_text('''# Responsive\n\n## Desktop\n\n- Khung tham chiếu 1440x1024.\n- Header 74px; rail 224px; nội dung chính 680-820px; panel phụ 260-400px.\n\n## Mobile\n\n- Khung tham chiếu 390x844.\n- Header 60px; danh mục 42px; bottom nav 62px.\n- Chuyển cột phụ thành drawer/bottom sheet.\n- Giữ CTA chính trong vùng ngón cái; không thu nhỏ text/table đến mức khó đọc.\n\n## Thứ tự suy ra\n\nDesktop xác định hệ thống nội dung và quan hệ vùng. Mobile giữ thứ tự: hành động chính -> nội dung -> trạng thái -> metadata -> tác vụ phụ.\n''',encoding='utf-8')
    (ROOT/'sources/10-content-style.md').write_text('''# Phong cách nội dung\n\n- Tiếng Việt rõ ràng, thân thiện, có tính marketing nhưng không phóng đại.\n- Dùng tên sản phẩm **Twight Light** và mô tả **Multi Social Comunity** đúng theo quyết định hiện tại.\n- Thông báo thành công mô tả bước tiếp theo; lỗi nêu nguyên nhân có thể hành động.\n- Không dùng “thanh toán trong ứng dụng” cho marketplace; dùng “thanh toán trực tiếp với người bán”.\n- Với xóa tài khoản, nói rõ khóa truy cập, thời gian khôi phục và thời điểm xóa cứng.\n''',encoding='utf-8')
    (ROOT/'sources/12-frontend-handoff.md').write_text('''# Bàn giao frontend vòng 2\n\n1. Dùng SVG desktop làm nguồn bố cục chính.\n2. Dùng SVG mobile để kiểm tra thứ tự ưu tiên và biến thể responsive.\n3. Dùng `tokens/design-tokens.json` cho token; không hard-code lại màu ở component.\n4. Dùng OpenAPI/AsyncAPI làm nguồn hợp đồng dữ liệu; mockup chỉ là yêu cầu giao diện.\n5. Các gap trong `18-backend-contract-gaps.md` phải được quyết định trước khi code luồng tương ứng.\n6. Chỉ tạo `design.md` sau khi toàn bộ màn hình bắt buộc được duyệt.\n''',encoding='utf-8')
    (ROOT/'sources/18-backend-contract-gaps.md').write_text('''# Khoảng trống hợp đồng phát sinh từ vòng duyệt 2\n\nCác mục dưới đây là yêu cầu UI/UX mới, chưa mặc nhiên được backend v3.0 hỗ trợ. Cần ADR hoặc cập nhật đặc tả trước khi triển khai.\n\n## Tài khoản và hồ sơ\n\n- Biệt danh, ảnh bìa, tâm trạng, bài hát Spotify, thông tin chi tiết hồ sơ và cửa hàng người bán.\n- Số điện thoại bắt buộc khi sửa hồ sơ; khả năng tìm bằng email/số điện thoại.\n- Đăng xuất một thiết bị bằng OTP và danh sách phiên nhiều thiết bị.\n- Lý do chặn; cảnh báo khi gặp người đã chặn trong cộng đồng chung.\n- Dùng lại email trong thời gian chờ xóa và quy tắc hòa giải giữa tài khoản mới/cũ.\n\n## Bài viết, video và thông báo\n\n- Định dạng rich text, font/kích thước/đậm nhạt, phạm vi hiển thị tùy chỉnh.\n- Lưu bài viết, repost, bộ lọc/pagination bình luận, reaction/reply/report bình luận.\n- Chọn thumbnail từ ảnh hoặc frame; bản nháp; lên lịch đăng; dashboard lượt xem/thích/chia sẻ.\n- Tab đề cập và mute/unmute thông báo nhanh.\n\n## Cộng đồng và trò chuyện\n\n- Taxonomy “tường”, “không quan tâm”, cài đặt ưu tiên/hạn chế cộng đồng.\n- Form chấp thuận quy tắc, duyệt thành viên, danh sách cấm và quyền theo vai trò.\n- Tin nhắn ghim, chủ đề chat, danh hiệu trong nhóm, rời trong im lặng.\n- Upload tệp chat, nội dung đang gửi/thử lại, phân vùng media/file/friend detail.\n\n## RTC\n\n- Mở cửa sổ/app riêng, mã phòng, lựa chọn layout và thiết bị mic/camera/loa.\n- Chat riêng/toàn phòng, video bản thân và quy trình xin phép ghi hình.\n\n## Marketplace\n\n- Phân loại/variant sản phẩm.\n- Bỏ payment provider khỏi UX; hiển thị QR/số tiền người bán và liên hệ trực tiếp.\n- Trạng thái hủy không có hoàn trả trong ứng dụng.\n\n## AI\n\n- Trợ lý thu nhỏ nổi, hỏi lại khi yêu cầu thiếu.\n- Tóm tắt tối đa 10.000 dòng và xuất PDF.\n- Loại route AI-03; hiển thị phiên âm trực tiếp dưới video hoặc tin nhắn thoại.\n''',encoding='utf-8')


def main() -> None:
    inventory=json.loads(INV_PATH.read_text(encoding='utf-8'))
    feedback=yaml.safe_load(FEEDBACK.read_text(encoding='utf-8'))
    notes=(feedback or {}).get('screens',{})
    # archive and remove AI-03 from active inventory
    updated=[]
    for item in inventory:
        if item['id']=='AI-03':
            p=ROOT/item['file']
            if p.exists():
                (ROOT/'archive').mkdir(parents=True, exist_ok=True)
                target = ROOT/'archive/ai-03-phien-am-rejected.md'
                archived = p.read_text(encoding='utf-8')
                if '\n## Hình chỉnh sửa\n' in archived:
                    archived = archived.split('\n## Hình chỉnh sửa\n', 1)[0].rstrip() + '\n\n## Trạng thái\n\nMàn hình độc lập đã bị loại theo phản hồi vòng 1. Phiên âm được tích hợp vào FEED-03 và CHAT-02.\n'
                target.write_text(archived, encoding='utf-8')
                p.unlink()
            for kind in ['desktop','mobile']:
                for base in [ROOT/'assets/editable/svg'/kind,ROOT/'assets/preview/png'/kind]:
                    for f in base.glob('ai-03-phien-am.*'): f.unlink(missing_ok=True)
            continue
        if item['id']=='MKT-05': item['title']='Thanh toán trực tiếp với người bán'
        if item['id'] in {'FEED-03','CHAT-02'} and 'AI-05' not in item.get('functions',[]): item.setdefault('functions',[]).append('AI-05')
        updated.append(item)
    INV_PATH.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # SVG and docs
    for item in updated:
        slug=Path(item['file']).stem
        write_svg(ROOT/f'assets/editable/svg/desktop/{slug}.svg',1440,1024,f"{item['id']} - {item['title']} - Desktop",desktop_scene(item),f"{item['id']} · DESKTOP · VÒNG 2")
        write_svg(ROOT/f'assets/editable/svg/mobile/{slug}.svg',390,844,f"{item['id']} - {item['title']} - Mobile",mobile_scene(item),f"{item['id']} · MOBILE · VÒNG 2")
        note=str((notes.get(item['id']) or {}).get('note','Đã áp dụng phản hồi vòng 1.'))
        update_screen_md(item,note)
    # approval round 2
    approval={'version':'2.0-review','updatedAt':'2026-09-06','screens':{},'shared':{'sources':'draft','tokens':'draft','flows':'draft','boards':'draft'}}
    for item in updated:
        approval['screens'][item['id']]={'status':'draft','required':item.get('priority') in {'P0','P1'},'note':'Đã áp dụng phản hồi vòng 1; chờ duyệt desktop và mobile vòng 2.'}
    (ROOT/'review/feedback-round-1.yaml').write_text(FEEDBACK.read_text(encoding='utf-8'),encoding='utf-8')
    (ROOT/'review/approval-status.yaml').write_text(yaml.safe_dump(approval,allow_unicode=True,sort_keys=False),encoding='utf-8')
    build_sources()
    (ROOT/'FEEDBACK_APPLIED.md').write_text('''# Phản hồi đã áp dụng - Vòng 1\n\n- 47 màn hình đang hoạt động đã được dựng lại; AI-03 bị loại khỏi danh mục theo phản hồi.\n- Phiên âm được tích hợp vào FEED-03 và CHAT-02.\n- Desktop là nguồn bố cục; mobile được tái cấu trúc từ desktop theo mức ưu tiên hành động.\n- Toàn bộ phản hồi gốc được lưu tại `review/feedback-round-1.yaml` và trong từng đặc tả màn hình.\n- Các yêu cầu làm thay đổi hợp đồng backend được liệt kê tại `sources/18-backend-contract-gaps.md`.\n''',encoding='utf-8')
    # inventory markdown
    rows=['# Danh mục màn hình vòng 2','','Tổng cộng **47 màn hình**. AI-03 đã bị loại và phiên âm được tích hợp vào bài viết/chat.','','| Mã | Màn hình | Route | Nhóm | Ưu tiên |','|---|---|---|---|---|']
    for item in updated: rows.append(f"| {item['id']} | {item['title']} | `{item['route']}` | {item['group']} | {item['priority']} |")
    (ROOT/'SCREEN_INVENTORY.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    # optional CSV
    import csv
    with (ROOT/'data/screen-inventory.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['id','title','route','group','priority','roles','functions','file'])
        for it in updated:w.writerow([it['id'],it['title'],it['route'],it['group'],it['priority'],'; '.join(it['roles']),'; '.join(it['functions']),it['file']])
    print(f'Generated {len(updated)} Twight Light screens for round 2.')


if __name__=='__main__':
    main()
