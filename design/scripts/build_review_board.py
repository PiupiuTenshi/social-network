#!/usr/bin/env python3
"""Build the self-contained local UI/UX review board."""
from __future__ import annotations

import html
import json
from pathlib import Path

from common import ROOT, load_approval, load_inventory


def main() -> None:
    inventory = load_inventory()
    approval = load_approval()
    statuses = approval.get("screens", {})
    entries = []
    for item in inventory:
        info = statuses.get(item["id"], {}) or {}
        slug = Path(item["file"]).stem
        entries.append(
            {
                **item,
                "slug": slug,
                "status": info.get("status", "draft"),
                "required": bool(info.get("required", item.get("priority") in {"P0", "P1"})),
                "note": info.get("note", ""),
                "desktopPng": f"../assets/preview/png/desktop/{slug}.png",
                "mobilePng": f"../assets/preview/png/mobile/{slug}.png",
                "desktopSvg": f"../assets/editable/svg/desktop/{slug}.svg",
                "mobileSvg": f"../assets/editable/svg/mobile/{slug}.svg",
                "spec": f"../{item['file']}",
            }
        )
    payload = json.dumps(entries, ensure_ascii=False)
    shared = json.dumps(approval.get("shared", {}), ensure_ascii=False)
    version = html.escape(str(approval.get("version", "1.0-draft")))
    output = ROOT / "review/REVIEW_BOARD.html"
    output.write_text(
        f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Duyệt UI/UX · Twight Light · Vòng 2</title>
  <style>
    :root {{ color-scheme: light; --brand:#4f46e5; --brand-subtle:#eef2ff; --ink:#0f172a; --muted:#64748b; --line:#e2e8f0; --bg:#f8fafc; --surface:#fff; --danger:#b91c1c; --warning:#b45309; --success:#15803d; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font:14px/1.5 Inter,"Be Vietnam Pro",system-ui,sans-serif; }}
    button,input,select,textarea {{ font:inherit; }}
    a {{ color:var(--brand); text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    header {{ position:sticky; top:0; z-index:20; background:rgba(255,255,255,.96); border-bottom:1px solid var(--line); backdrop-filter:blur(14px); }}
    .bar {{ max-width:1720px; margin:auto; padding:18px 24px; display:grid; gap:14px; }}
    .heading {{ display:flex; align-items:flex-start; justify-content:space-between; gap:20px; }}
    h1 {{ font-size:24px; margin:0; }}
    .sub {{ color:var(--muted); margin-top:3px; }}
    .stats {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .pill {{ border:1px solid var(--line); background:var(--surface); border-radius:999px; padding:5px 10px; white-space:nowrap; }}
    .controls {{ display:grid; grid-template-columns:minmax(220px,1fr) repeat(3,minmax(130px,auto)) auto auto; gap:10px; }}
    input,select,textarea {{ border:1px solid var(--line); background:var(--surface); color:var(--ink); border-radius:10px; padding:10px 12px; }}
    button {{ border:0; border-radius:10px; padding:10px 14px; font-weight:700; cursor:pointer; }}
    .primary {{ background:var(--brand); color:white; }}
    .secondary {{ background:var(--brand-subtle); color:var(--brand); }}
    .danger {{ background:#fef2f2; color:var(--danger); }}
    main {{ max-width:1720px; margin:auto; padding:24px; }}
    .shared {{ background:var(--surface); border:1px solid var(--line); border-radius:16px; padding:16px; margin-bottom:18px; display:flex; flex-wrap:wrap; gap:14px; align-items:center; }}
    .shared strong {{ margin-right:8px; }}
    .shared label {{ display:flex; align-items:center; gap:8px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(390px,1fr)); gap:18px; }}
    .card {{ background:var(--surface); border:1px solid var(--line); border-radius:18px; overflow:hidden; box-shadow:0 8px 26px rgba(15,23,42,.06); }}
    .cardHead {{ padding:15px 16px 12px; display:flex; align-items:flex-start; justify-content:space-between; gap:12px; border-bottom:1px solid var(--line); }}
    .id {{ font-size:12px; font-weight:800; color:var(--brand); letter-spacing:.04em; }}
    .title {{ font-size:18px; font-weight:800; margin-top:2px; }}
    .meta {{ color:var(--muted); font-size:12px; margin-top:3px; }}
    .badge {{ border-radius:999px; padding:4px 9px; font-size:12px; font-weight:800; white-space:nowrap; }}
    .badge.approved {{ background:#ecfdf5; color:var(--success); }}
    .badge.draft {{ background:#f1f5f9; color:#475569; }}
    .badge.needs_changes {{ background:#fff7ed; color:var(--warning); }}
    .badge.deferred {{ background:#f8fafc; color:#64748b; border:1px dashed #94a3b8; }}
    .previewTabs {{ display:flex; gap:8px; padding:10px 14px; border-bottom:1px solid var(--line); }}
    .previewTabs button {{ padding:7px 10px; background:#f1f5f9; color:#475569; }}
    .previewTabs button.active {{ background:var(--brand-subtle); color:var(--brand); }}
    .preview {{ height:360px; background:#eef2f7; display:flex; align-items:flex-start; justify-content:center; overflow:auto; padding:12px; }}
    .preview img {{ display:block; max-width:100%; height:auto; border:1px solid #cbd5e1; background:white; }}
    .preview img.mobile {{ width:195px; }}
    .form {{ padding:14px 16px 16px; display:grid; gap:10px; }}
    .row {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
    .form label {{ display:grid; gap:5px; color:#334155; font-size:12px; font-weight:700; }}
    textarea {{ min-height:72px; resize:vertical; }}
    .links {{ display:flex; flex-wrap:wrap; gap:12px; font-size:12px; }}
    .empty {{ padding:48px; text-align:center; color:var(--muted); }}
    dialog {{ border:0; border-radius:16px; width:min(720px,92vw); box-shadow:0 24px 70px rgba(15,23,42,.25); }}
    dialog::backdrop {{ background:rgba(15,23,42,.55); }}
    pre {{ white-space:pre-wrap; background:#0f172a; color:#e2e8f0; padding:16px; border-radius:12px; max-height:52vh; overflow:auto; }}
    @media (max-width:900px) {{ .controls {{ grid-template-columns:1fr 1fr; }} .controls input {{ grid-column:1/-1; }} .grid {{ grid-template-columns:1fr; }} }}
    @media (max-width:560px) {{ .heading {{ display:block; }} .stats {{ margin-top:12px; }} .controls {{ grid-template-columns:1fr; }} main,.bar {{ padding:14px; }} .preview {{ height:300px; }} }}
  </style>
</head>
<body>
<header>
  <div class="bar">
    <div class="heading">
      <div><h1>Duyệt UI/UX Twight Light - Vòng 2</h1><div class="sub">Phiên bản {version} · Chỉnh trạng thái, ghi chú và xuất lại <code>approval-status.yaml</code>.</div></div>
      <div class="stats" id="stats"></div>
    </div>
    <div class="controls">
      <input id="search" type="search" placeholder="Tìm theo mã, tên, route, chức năng…" aria-label="Tìm màn hình" />
      <select id="group"><option value="">Tất cả nhóm</option></select>
      <select id="priority"><option value="">Tất cả ưu tiên</option><option>P0</option><option>P1</option><option>P2</option></select>
      <select id="status"><option value="">Tất cả trạng thái</option><option value="draft">Bản nháp</option><option value="needs_changes">Cần sửa</option><option value="approved">Đã duyệt</option><option value="deferred">Hoãn</option></select>
      <button class="secondary" id="save">Lưu cục bộ</button>
      <button class="primary" id="export">Xuất YAML</button>
    </div>
  </div>
</header>
<main>
  <section class="shared" id="shared"></section>
  <section class="grid" id="grid"></section>
  <div class="empty" id="empty" hidden>Không có màn hình phù hợp bộ lọc.</div>
</main>
<dialog id="dialog"><h2>approval-status.yaml</h2><p>Tải tệp hoặc sao chép nội dung dưới đây vào <code>review/approval-status.yaml</code>.</p><pre id="yaml"></pre><div style="display:flex;gap:10px;justify-content:flex-end"><button class="secondary" id="copy">Sao chép</button><button class="primary" id="download">Tải YAML</button><button class="danger" id="close">Đóng</button></div></dialog>
<script>
const original = {payload};
const originalShared = {shared};
const STORAGE_KEY = 'twight-light-uiux-review-v2';
const labels = {{draft:'Bản nháp',needs_changes:'Cần sửa',approved:'Đã duyệt',deferred:'Hoãn'}};
let state = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null') || {{screens:Object.fromEntries(original.map(x=>[x.id,{{status:x.status,note:x.note,required:x.required}}])),shared:originalShared}};
for (const item of original) if (!state.screens[item.id]) state.screens[item.id]={{status:item.status,note:item.note,required:item.required}};
state.shared = Object.assign({{sources:'draft',tokens:'draft',flows:'draft',boards:'draft'}}, state.shared||{{}});
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
const groupSelect=$('#group');
[...new Set(original.map(x=>x.group))].sort().forEach(g=>groupSelect.insertAdjacentHTML('beforeend',`<option>${{esc(g)}}</option>`));
function statusSelect(id) {{ const current=state.screens[id].status; return `<select class="statusSelect" data-id="${{id}}">${{Object.entries(labels).map(([v,l])=>`<option value="${{v}}" ${{v===current?'selected':''}}>${{l}}</option>`).join('')}}</select>`; }}
function sharedView() {{ $('#shared').innerHTML='<strong>Khối dùng chung</strong>'+['sources','tokens','flows','boards'].map(k=>`<label>${{k}} <select data-shared="${{k}}">${{Object.entries(labels).filter(([v])=>v!=='deferred').map(([v,l])=>`<option value="${{v}}" ${{state.shared[k]===v?'selected':''}}>${{l}}</option>`).join('')}}</select></label>`).join('')+'<button class="secondary" id="approveVisible">Duyệt các màn hình đang hiển thị</button>'; }}
function filtered() {{ const q=$('#search').value.trim().toLowerCase(); return original.filter(x=>{{const s=state.screens[x.id]; const hay=[x.id,x.title,x.group,x.route,x.priority,...x.functions,...x.roles].join(' ').toLowerCase(); return (!q||hay.includes(q))&&(!$('#group').value||x.group===$('#group').value)&&(!$('#priority').value||x.priority===$('#priority').value)&&(!$('#status').value||s.status===$('#status').value);}}); }}
function render() {{ sharedView(); const list=filtered(); $('#empty').hidden=!!list.length; $('#grid').innerHTML=list.map(x=>{{const s=state.screens[x.id];return `<article class="card" data-id="${{x.id}}"><div class="cardHead"><div><div class="id">${{esc(x.id)}} · ${{esc(x.priority)}}${{s.required?' · BẮT BUỘC':''}}</div><div class="title">${{esc(x.title)}}</div><div class="meta">${{esc(x.group)}} · <code>${{esc(x.route)}}</code> · ${{x.functions.map(esc).join(', ')}}</div></div><span class="badge ${{s.status}}">${{labels[s.status]||esc(s.status)}}</span></div><div class="previewTabs"><button class="active" data-view="desktop">Desktop</button><button data-view="mobile">Mobile</button></div><div class="preview"><img src="${{x.desktopPng}}" alt="${{esc(x.title)}} desktop" loading="lazy"></div><div class="form"><div class="row"><label>Trạng thái${{statusSelect(x.id)}}</label><label>Phạm vi<select class="requiredSelect" data-id="${{x.id}}"><option value="true" ${{s.required?'selected':''}}>Bắt buộc</option><option value="false" ${{!s.required?'selected':''}}>Tùy chọn</option></select></label></div><label>Ghi chú<textarea class="note" data-id="${{x.id}}" placeholder="Điều cần chỉnh hoặc lý do duyệt…">${{esc(s.note)}}</textarea></label><div class="links"><a href="${{x.spec}}" target="_blank">Đặc tả MD</a><a href="${{x.desktopSvg}}" target="_blank">SVG desktop</a><a href="${{x.mobileSvg}}" target="_blank">SVG mobile</a></div></div></article>`;}}).join(''); stats(); bindCards(); }}
function stats() {{ const vals=Object.values(state.screens); $('#stats').innerHTML=`<span class="pill">Tổng: ${{vals.length}}</span><span class="pill">Đã duyệt: ${{vals.filter(x=>x.status==='approved').length}}</span><span class="pill">Cần sửa: ${{vals.filter(x=>x.status==='needs_changes').length}}</span><span class="pill">Bắt buộc chưa duyệt: ${{vals.filter(x=>x.required&&x.status!=='approved').length}}</span>`; }}
function bindCards() {{ document.querySelectorAll('.card').forEach(card=>{{const item=original.find(x=>x.id===card.dataset.id); card.querySelectorAll('[data-view]').forEach(btn=>btn.onclick=()=>{{card.querySelectorAll('[data-view]').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const img=card.querySelector('.preview img');const mobile=btn.dataset.view==='mobile';img.src=mobile?item.mobilePng:item.desktopPng;img.classList.toggle('mobile',mobile);}});}}); }}
function syncFromDom() {{ document.querySelectorAll('.statusSelect').forEach(el=>state.screens[el.dataset.id].status=el.value);document.querySelectorAll('.requiredSelect').forEach(el=>state.screens[el.dataset.id].required=el.value==='true');document.querySelectorAll('.note').forEach(el=>state.screens[el.dataset.id].note=el.value);document.querySelectorAll('[data-shared]').forEach(el=>state.shared[el.dataset.shared]=el.value); }}
function save() {{ syncFromDom(); localStorage.setItem(STORAGE_KEY,JSON.stringify(state)); render(); }}
function yamlQuote(s) {{ return "'"+String(s??'').replace(/'/g,"''")+"'"; }}
function toYaml() {{ syncFromDom(); let y=`version: 1.0-draft
screens:
`; for (const item of original){{const s=state.screens[item.id];y+=`  ${{item.id}}:
    status: ${{s.status}}
    required: ${{s.required?'true':'false'}}
    note: ${{yamlQuote(s.note)}}
`;}} y+=`shared:
`; for(const k of ['sources','tokens','flows','boards'])y+=`  ${{k}}: ${{state.shared[k]}}
`; return y; }}
function showExport() {{ $('#yaml').textContent=toYaml(); $('#dialog').showModal(); }}
['search','group','priority','status'].forEach(id=>$('#'+id).addEventListener(id==='search'?'input':'change',render));
$('#save').onclick=save; $('#export').onclick=showExport; $('#close').onclick=()=>$('#dialog').close(); $('#copy').onclick=()=>navigator.clipboard.writeText($('#yaml').textContent);
$('#download').onclick=()=>{{const blob=new Blob([$('#yaml').textContent],{{type:'text/yaml;charset=utf-8'}});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='approval-status.yaml';a.click();URL.revokeObjectURL(a.href);}};
document.addEventListener('change',e=>{{if(e.target.matches('.statusSelect,.requiredSelect,[data-shared]')){{syncFromDom();localStorage.setItem(STORAGE_KEY,JSON.stringify(state));render();}}}});
document.addEventListener('input',e=>{{if(e.target.matches('.note')){{state.screens[e.target.dataset.id].note=e.target.value;localStorage.setItem(STORAGE_KEY,JSON.stringify(state));}}}});
document.addEventListener('click',e=>{{if(e.target.id==='approveVisible'){{syncFromDom();for(const item of filtered())state.screens[item.id].status='approved';localStorage.setItem(STORAGE_KEY,JSON.stringify(state));render();}}}});
render();
</script>
</body>
</html>''',
        encoding="utf-8",
    )
    print(f"Đã tạo {output.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
