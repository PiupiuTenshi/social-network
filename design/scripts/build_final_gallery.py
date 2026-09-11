#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review' / 'FINAL_REVIEW_GALLERY_STANDALONE.html'


def data_url(path: Path) -> str:
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def main() -> None:
    inventory = json.loads((ROOT / 'data' / 'screen-inventory.json').read_text(encoding='utf-8'))
    payload = []
    for item in inventory:
        slug = Path(item['file']).stem
        payload.append({
            **item,
            'slug': slug,
            'desktop': data_url(ROOT / f'assets/preview/png/desktop/{slug}.png'),
            'mobile': data_url(ROOT / f'assets/preview/png/mobile/{slug}.png'),
            'desktopPath': f'assets/preview/png/desktop/{slug}.png',
            'mobilePath': f'assets/preview/png/mobile/{slug}.png',
            'specPath': item['file'],
        })
    data = json.dumps(payload, ensure_ascii=False).replace('</', '<\\/')
    html = f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Twight Light UI/UX 1.2 Final</title>
<style>
:root{{--bg:#f5f7fb;--card:#fff;--ink:#12152a;--muted:#68738a;--line:#dde3ef;--brand:#6557ee;--brand2:#4c6fff;--good:#0e9f6e}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;background:var(--bg);font:14px/1.5 Inter,"Be Vietnam Pro",system-ui,sans-serif;color:var(--ink)}}
header{{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.96);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}}
.bar{{max-width:1700px;margin:auto;padding:16px 22px}} .top{{display:flex;justify-content:space-between;gap:20px;align-items:center}}
.brand{{display:flex;align-items:center;gap:12px}} .logo{{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff;display:grid;place-items:center;font-size:22px;font-weight:900}}
h1{{font-size:22px;line-height:1.15;margin:0}} .sub{{color:var(--muted);font-size:12px;margin-top:3px}} .status{{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}}
.pill{{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 10px;font-size:11px;font-weight:800}} .ok{{background:#e8fbf3;color:#087a54;border-color:#bfeedd}}
.controls{{margin-top:14px;display:grid;grid-template-columns:minmax(260px,1fr) 200px 120px 160px auto;gap:8px}}
input,select,button{{font:inherit}} input,select{{border:1px solid var(--line);border-radius:10px;background:#fff;padding:10px 12px;color:var(--ink)}} button{{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer}} .primary{{background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff}} .secondary{{background:#fff;border:1px solid var(--line);color:var(--ink)}}
main{{max-width:1700px;margin:auto;padding:22px}} .notice{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:16px;display:flex;gap:12px;justify-content:space-between;align-items:center}} .notice strong{{color:var(--brand)}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}} .card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;box-shadow:0 8px 24px rgba(7,22,43,.06)}}
.cardhead{{padding:14px 16px;display:flex;gap:12px;justify-content:space-between;align-items:flex-start;border-bottom:1px solid var(--line)}} .id{{font-size:11px;font-weight:900;color:var(--brand);letter-spacing:.03em}} .title{{font-size:17px;font-weight:900;margin-top:2px}} .meta{{font-size:11px;color:var(--muted);margin-top:4px}}
.badge{{border-radius:999px;padding:5px 9px;font-size:10px;font-weight:900;white-space:nowrap;background:#dcfce7;color:#15803d}}
.tabs{{display:flex;gap:4px;padding:10px 12px;background:#f8fafc;border-bottom:1px solid var(--line)}} .tabs button{{padding:7px 12px;background:transparent;color:var(--muted)}} .tabs button.active{{background:#fff;color:var(--brand);border:1px solid var(--line)}}
.preview{{height:540px;background:#e9edf4;display:flex;align-items:flex-start;justify-content:center;overflow:auto;padding:10px}} .preview img{{display:block;max-width:100%;height:auto;background:#fff;border:1px solid #ccd5e1;cursor:zoom-in}} .preview img.mobile{{width:390px;max-width:100%}}
.details{{padding:12px 16px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;color:var(--muted);font-size:11px}} code{{background:#f2f4f9;padding:3px 6px;border-radius:6px;color:#313958}}
.empty{{text-align:center;color:var(--muted);padding:60px}}
dialog{{border:0;border-radius:18px;padding:0;max-width:96vw;max-height:96vh;box-shadow:0 24px 80px rgba(0,0,0,.35)}} dialog::backdrop{{background:rgba(7,22,43,.72)}} .modalbar{{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line)}} .modalimg{{display:block;max-width:94vw;max-height:86vh;width:auto;height:auto}}
@media(max-width:1100px){{.controls{{grid-template-columns:1fr 1fr}} .controls input{{grid-column:1/-1}} .grid{{grid-template-columns:1fr}}}}
@media(max-width:650px){{.top{{display:block}} .status{{justify-content:flex-start;margin-top:10px}} .controls{{grid-template-columns:1fr 1fr}} .controls input{{grid-column:1/-1}} main,.bar{{padding:12px}} .notice{{display:block}} .preview{{height:430px}}}}
</style>
</head>
<body>
<header><div class="bar"><div class="top"><div class="brand"><div class="logo">T</div><div><h1>Twight Light — UI/UX 1.2 Final</h1><div class="sub">47 màn hình đã khóa · Desktop và Mobile · Ảnh nhúng trực tiếp, mở ngoại tuyến</div></div></div><div class="status"><span class="pill ok">47/47 đã duyệt</span><span class="pill">Nguồn triển khai: design.md</span></div></div>
<div class="controls"><input id="search" type="search" placeholder="Tìm mã, màn hình, route hoặc chức năng…"><select id="group"><option value="">Tất cả nhóm</option></select><select id="priority"><option value="">P0/P1/P2</option><option>P0</option><option>P1</option><option>P2</option></select><select id="globalView"><option value="desktop">Xem Desktop</option><option value="mobile">Xem Mobile</option></select><button class="secondary" id="top">Lên đầu trang</button></div></div></header>
<main><div class="notice"><div><strong>Bản cuối đã sẵn sàng cho Frontend.</strong> Dùng gallery để đối chiếu hình; dùng <code>design.md</code> và SVG trong <code>assets/editable/</code> làm nguồn triển khai/chỉnh sửa.</div><div id="count"></div></div><section class="grid" id="grid"></section><div class="empty" id="empty" hidden>Không có màn hình phù hợp.</div></main>
<dialog id="zoom"><div class="modalbar"><strong id="zoomTitle"></strong><button class="secondary" id="closeZoom">Đóng</button></div><img class="modalimg" id="zoomImg" alt="Ảnh phóng to"></dialog>
<script>
const items={data};
const $=s=>document.querySelector(s); const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
[...new Set(items.map(x=>x.group))].sort().forEach(g=>$('#group').insertAdjacentHTML('beforeend',`<option>${{esc(g)}}</option>`));
function filtered(){{const q=$('#search').value.toLowerCase().trim();return items.filter(x=>{{const hay=[x.id,x.title,x.route,x.group,x.priority,...x.functions,...x.roles].join(' ').toLowerCase();return(!q||hay.includes(q))&&(!$('#group').value||x.group===$('#group').value)&&(!$('#priority').value||x.priority===$('#priority').value)}})}}
function render(){{const view=$('#globalView').value;const list=filtered();$('#empty').hidden=!!list.length;$('#count').textContent=`Đang hiển thị ${{list.length}}/${{items.length}} màn hình`;$('#grid').innerHTML=list.map(x=>{{const src=view==='desktop'?x.desktop:x.mobile;return`<article class="card" data-id="${{x.id}}"><div class="cardhead"><div><div class="id">${{x.id}} · ${{x.priority}}</div><div class="title">${{esc(x.title)}}</div><div class="meta">${{esc(x.group)}} · ${{esc(x.route)}} · ${{x.functions.join(', ')}}</div></div><span class="badge">ĐÃ DUYỆT</span></div><div class="tabs"><button class="viewBtn ${{view==='desktop'?'active':''}}" data-view="desktop">Desktop</button><button class="viewBtn ${{view==='mobile'?'active':''}}" data-view="mobile">Mobile</button></div><div class="preview"><img class="${{view==='mobile'?'mobile':''}}" src="${{src}}" data-full="${{src}}" alt="${{esc(x.id+' '+x.title+' '+view)}}"></div><div class="details"><span>Đặc tả: <code>${{esc(x.specPath)}}</code></span><span>Ảnh: <code>${{esc(view==='desktop'?x.desktopPath:x.mobilePath)}}</code></span></div></article>`}}).join('');bind()}}
function bind(){{document.querySelectorAll('.card').forEach(card=>{{const item=items.find(x=>x.id===card.dataset.id);card.querySelectorAll('.viewBtn').forEach(b=>b.onclick=()=>{{card.querySelectorAll('.viewBtn').forEach(z=>z.classList.remove('active'));b.classList.add('active');const img=card.querySelector('img');const mobile=b.dataset.view==='mobile';img.src=mobile?item.mobile:item.desktop;img.dataset.full=img.src;img.classList.toggle('mobile',mobile);card.querySelector('.details code:last-child').textContent=mobile?item.mobilePath:item.desktopPath}});card.querySelector('img').onclick=e=>{{$('#zoomTitle').textContent=item.id+' · '+item.title;$('#zoomImg').src=e.currentTarget.dataset.full;$('#zoom').showModal()}}}})}}
['search'].forEach(id=>$('#'+id).addEventListener('input',render));['group','priority','globalView'].forEach(id=>$('#'+id).addEventListener('change',render));
$('#top').onclick=()=>window.scrollTo({{top:0,behavior:'smooth'}});$('#closeZoom').onclick=()=>$('#zoom').close();
render();
</script>
</body></html>'''
    OUT.write_text(html, encoding='utf-8')
    print(f'Wrote {OUT} ({OUT.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
