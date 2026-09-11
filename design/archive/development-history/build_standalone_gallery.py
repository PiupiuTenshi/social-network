#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review' / 'TWIGHT_LIGHT_REVIEW_ROUND2_STANDALONE.html'


def data_url(path: Path) -> str:
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode('ascii')


def main() -> None:
    inventory = json.loads((ROOT/'data/screen-inventory.json').read_text(encoding='utf-8'))
    approval = yaml.safe_load((ROOT/'review/approval-status.yaml').read_text(encoding='utf-8')) or {}
    state = approval.get('screens', {})
    payload=[]
    for item in inventory:
        slug=Path(item['file']).stem
        payload.append({
            **item,
            'slug':slug,
            'desktop':data_url(ROOT/f'assets/preview/png/desktop/{slug}.png'),
            'mobile':data_url(ROOT/f'assets/preview/png/mobile/{slug}.png'),
            'status':(state.get(item['id']) or {}).get('status','draft'),
            'note':(state.get(item['id']) or {}).get('note',''),
            'required':bool((state.get(item['id']) or {}).get('required', item.get('priority') in {'P0','P1'})),
        })
    data=json.dumps(payload,ensure_ascii=False).replace('</','<\\/')
    html=f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Twight Light UI/UX — Duyệt vòng 2</title>
<style>
:root{{--bg:#f4f6fb;--card:#fff;--ink:#0b1020;--muted:#64748b;--line:#dce3ee;--brand:#6c5ce7;--brand2:#496dff;--good:#10b981;--warn:#f59e0b;--bad:#ef4444}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);font:14px/1.5 Inter,"Be Vietnam Pro",system-ui,sans-serif;color:var(--ink)}}
header{{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.96);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}}
.bar{{max-width:1660px;margin:auto;padding:16px 22px}} .brand{{display:flex;align-items:center;gap:12px}} .logo{{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff;display:grid;place-items:center;font-size:22px;font-weight:900}}
h1{{font-size:22px;line-height:1.15;margin:0}} .sub{{color:var(--muted);font-size:12px;margin-top:3px}} .top{{display:flex;justify-content:space-between;gap:20px;align-items:center}}
.stats{{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}} .stat{{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 10px;font-size:11px;font-weight:750}}
.controls{{margin-top:14px;display:grid;grid-template-columns:minmax(250px,1fr) 180px 120px 120px 120px auto auto;gap:8px}}
input,select,textarea,button{{font:inherit}} input,select,textarea{{border:1px solid var(--line);border-radius:10px;background:#fff;padding:10px 12px;color:var(--ink)}} button{{border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer}} .primary{{background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff}} .secondary{{background:#fff;border:1px solid var(--line);color:var(--ink)}}
main{{max-width:1660px;margin:auto;padding:22px}} .notice{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin-bottom:16px;display:flex;gap:12px;justify-content:space-between;align-items:center}} .notice strong{{color:var(--brand)}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}} .card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;box-shadow:0 8px 24px rgba(7,22,43,.06)}}
.cardhead{{padding:14px 16px;display:flex;gap:12px;justify-content:space-between;align-items:flex-start;border-bottom:1px solid var(--line)}} .id{{font-size:11px;font-weight:900;color:var(--brand);letter-spacing:.03em}} .title{{font-size:17px;font-weight:900;margin-top:2px}} .meta{{font-size:11px;color:var(--muted);margin-top:4px}}
.badge{{border-radius:999px;padding:5px 9px;font-size:10px;font-weight:900;white-space:nowrap}} .draft{{background:#eef2ff;color:#5145cd}} .needs_changes{{background:#fff7ed;color:#9a3412}} .approved{{background:#dcfce7;color:#15803d}} .deferred{{background:#f1f5f9;color:#475569}} .rejected{{background:#fee2e2;color:#b91c1c}}
.tabs{{display:flex;gap:4px;padding:10px 12px;background:#f8fafc;border-bottom:1px solid var(--line)}} .tabs button{{padding:7px 12px;background:transparent;color:var(--muted)}} .tabs button.active{{background:#fff;color:var(--brand);border:1px solid var(--line)}}
.preview{{height:520px;background:#e9edf4;display:flex;align-items:flex-start;justify-content:center;overflow:auto;padding:10px}} .preview img{{display:block;max-width:100%;height:auto;background:#fff;border:1px solid #ccd5e1;cursor:zoom-in}} .preview img.mobile{{width:390px;max-width:100%}}
.form{{padding:14px 16px;display:grid;gap:10px}} .row{{display:grid;grid-template-columns:1fr 1fr;gap:10px}} label{{display:grid;gap:5px;font-size:11px;font-weight:800;color:#334155}} textarea{{min-height:72px;resize:vertical}} .empty{{text-align:center;color:var(--muted);padding:60px}}
dialog{{border:0;border-radius:18px;padding:0;max-width:95vw;max-height:95vh;box-shadow:0 24px 80px rgba(0,0,0,.35)}} dialog::backdrop{{background:rgba(7,22,43,.7)}} .modalbar{{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line)}} .modalimg{{display:block;max-width:92vw;max-height:84vh;width:auto;height:auto}} pre{{white-space:pre-wrap;background:#07162b;color:#e8ecff;padding:16px;border-radius:12px;max-height:60vh;overflow:auto}}
.exportbox{{padding:18px;width:min(780px,92vw)}}
@media(max-width:1100px){{.controls{{grid-template-columns:1fr 1fr 1fr}} .controls input{{grid-column:1/-1}} .grid{{grid-template-columns:1fr}}}}
@media(max-width:650px){{.top{{display:block}} .stats{{justify-content:flex-start;margin-top:10px}} .controls{{grid-template-columns:1fr 1fr}} .controls input{{grid-column:1/-1}} main,.bar{{padding:12px}} .notice{{display:block}} .preview{{height:430px}} .row{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<header><div class="bar"><div class="top"><div class="brand"><div class="logo">T</div><div><h1>Twight Light — Duyệt UI/UX vòng 2</h1><div class="sub">Desktop đã áp dụng phản hồi · Mobile được suy ra từ desktop · Ảnh được nhúng trực tiếp, mở file là xem được</div></div></div><div class="stats" id="stats"></div></div>
<div class="controls"><input id="search" type="search" placeholder="Tìm mã, màn hình, route hoặc chức năng…"><select id="group"><option value="">Tất cả nhóm</option></select><select id="priority"><option value="">P0/P1/P2</option><option>P0</option><option>P1</option><option>P2</option></select><select id="status"><option value="">Mọi trạng thái</option><option value="draft">Bản nháp</option><option value="needs_changes">Cần sửa</option><option value="approved">Đã duyệt</option><option value="deferred">Hoãn</option><option value="rejected">Loại</option></select><select id="globalView"><option value="desktop">Xem Desktop</option><option value="mobile">Xem Mobile</option></select><button class="secondary" id="save">Lưu cục bộ</button><button class="primary" id="export">Xuất YAML</button></div></div></header>
<main><div class="notice"><div><strong>47 màn hình đang chờ duyệt vòng 2.</strong> AI-03 đã bị loại; phiên âm được đưa vào FEED-03 và CHAT-02. Hãy ưu tiên duyệt desktop, sau đó chuyển sang mobile để kiểm tra responsive.</div><button class="secondary" id="approveVisible">Duyệt các màn hình đang hiển thị</button></div><section class="grid" id="grid"></section><div class="empty" id="empty" hidden>Không có màn hình phù hợp.</div></main>
<dialog id="zoom"><div class="modalbar"><strong id="zoomTitle"></strong><button class="secondary" id="closeZoom">Đóng</button></div><img class="modalimg" id="zoomImg" alt="Ảnh phóng to"></dialog>
<dialog id="exportDialog"><div class="exportbox"><div class="modalbar" style="padding:0 0 12px"><strong>approval-status.yaml vòng 2</strong><button class="secondary" id="closeExport">Đóng</button></div><pre id="yaml"></pre><div style="display:flex;gap:8px;justify-content:flex-end"><button class="secondary" id="copy">Sao chép</button><button class="primary" id="download">Tải YAML</button></div></div></dialog>
<script>
const items={data};
const STORAGE='twight-light-review-round2-v1';
const labels={{draft:'Bản nháp',needs_changes:'Cần sửa',approved:'Đã duyệt',deferred:'Hoãn',rejected:'Loại'}};
let state=JSON.parse(localStorage.getItem(STORAGE)||'null')||{{screens:Object.fromEntries(items.map(x=>[x.id,{{status:x.status,note:x.note,required:x.required}}]))}};
for(const x of items) if(!state.screens[x.id]) state.screens[x.id]={{status:x.status,note:x.note,required:x.required}};
const $=s=>document.querySelector(s); const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
[...new Set(items.map(x=>x.group))].sort().forEach(g=>$('#group').insertAdjacentHTML('beforeend',`<option>${{esc(g)}}</option>`));
function filtered(){{const q=$('#search').value.toLowerCase().trim();return items.filter(x=>{{const st=state.screens[x.id];const hay=[x.id,x.title,x.route,x.group,x.priority,...x.functions,...x.roles].join(' ').toLowerCase();return(!q||hay.includes(q))&&(!$('#group').value||x.group===$('#group').value)&&(!$('#priority').value||x.priority===$('#priority').value)&&(!$('#status').value||st.status===$('#status').value)}})}}
function statusOptions(id){{const cur=state.screens[id].status;return Object.entries(labels).map(([v,l])=>`<option value="${{v}}" ${{cur===v?'selected':''}}>${{l}}</option>`).join('')}}
function render(){{const view=$('#globalView').value;const list=filtered();$('#empty').hidden=!!list.length;$('#grid').innerHTML=list.map(x=>{{const st=state.screens[x.id];const src=view==='desktop'?x.desktop:x.mobile;return`<article class="card" data-id="${{x.id}}"><div class="cardhead"><div><div class="id">${{x.id}} · ${{x.priority}}${{st.required?' · BẮT BUỘC':''}}</div><div class="title">${{esc(x.title)}}</div><div class="meta">${{esc(x.group)}} · ${{esc(x.route)}} · ${{x.functions.join(', ')}}</div></div><span class="badge ${{st.status}}">${{labels[st.status]||st.status}}</span></div><div class="tabs"><button class="viewBtn ${{view==='desktop'?'active':''}}" data-view="desktop">Desktop</button><button class="viewBtn ${{view==='mobile'?'active':''}}" data-view="mobile">Mobile</button></div><div class="preview"><img class="${{view==='mobile'?'mobile':''}}" src="${{src}}" data-full="${{src}}" alt="${{esc(x.id+' '+x.title+' '+view)}}"></div><div class="form"><div class="row"><label>Trạng thái<select class="statusSelect" data-id="${{x.id}}">${{statusOptions(x.id)}}</select></label><label>Phạm vi<select class="requiredSelect" data-id="${{x.id}}"><option value="true" ${{st.required?'selected':''}}>Bắt buộc</option><option value="false" ${{!st.required?'selected':''}}>Tùy chọn</option></select></label></div><label>Ghi chú vòng 2<textarea class="note" data-id="${{x.id}}" placeholder="Điều cần sửa hoặc lý do duyệt…">${{esc(st.note)}}</textarea></label></div></article>`}}).join('');bind();stats()}}
function stats(){{const a=Object.values(state.screens);$('#stats').innerHTML=`<span class="stat">Tổng: ${{a.length}}</span><span class="stat">Đã duyệt: ${{a.filter(x=>x.status==='approved').length}}</span><span class="stat">Cần sửa: ${{a.filter(x=>x.status==='needs_changes').length}}</span><span class="stat">Bắt buộc chưa duyệt: ${{a.filter(x=>x.required&&x.status!=='approved').length}}</span>`}}
function bind(){{document.querySelectorAll('.card').forEach(card=>{{const item=items.find(x=>x.id===card.dataset.id);card.querySelectorAll('.viewBtn').forEach(b=>b.onclick=()=>{{card.querySelectorAll('.viewBtn').forEach(z=>z.classList.remove('active'));b.classList.add('active');const img=card.querySelector('img');const mobile=b.dataset.view==='mobile';img.src=mobile?item.mobile:item.desktop;img.dataset.full=img.src;img.classList.toggle('mobile',mobile)}});card.querySelector('img').onclick=e=>{{$('#zoomTitle').textContent=item.id+' · '+item.title;$('#zoomImg').src=e.currentTarget.dataset.full;$('#zoom').showModal()}}}})}}
function sync(){{document.querySelectorAll('.statusSelect').forEach(e=>state.screens[e.dataset.id].status=e.value);document.querySelectorAll('.requiredSelect').forEach(e=>state.screens[e.dataset.id].required=e.value==='true');document.querySelectorAll('.note').forEach(e=>state.screens[e.dataset.id].note=e.value)}}
function save(){{sync();localStorage.setItem(STORAGE,JSON.stringify(state));render()}}
function quote(s){{return JSON.stringify(String(s??''))}}
function toYaml(){{
  sync();
  const lines=['version: 2','updatedAt: '+new Date().toISOString(),'screens:'];
  for(const x of items){{
    const st=state.screens[x.id];
    lines.push('  '+x.id+':');
    lines.push('    status: '+st.status);
    lines.push('    required: '+(st.required?'true':'false'));
    lines.push('    note: '+quote(st.note));
  }}
  lines.push('shared:','  sources: draft','  tokens: draft','  flows: draft','  boards: draft');
  return lines.join(String.fromCharCode(10))+String.fromCharCode(10);
}}
['search'].forEach(id=>$('#'+id).addEventListener('input',render));['group','priority','status','globalView'].forEach(id=>$('#'+id).addEventListener('change',render));
$('#save').onclick=save;$('#export').onclick=()=>{{$('#yaml').textContent=toYaml();$('#exportDialog').showModal()}};$('#closeZoom').onclick=()=>$('#zoom').close();$('#closeExport').onclick=()=>$('#exportDialog').close();$('#copy').onclick=()=>navigator.clipboard.writeText($('#yaml').textContent);$('#download').onclick=()=>{{const b=new Blob([$('#yaml').textContent],{{type:'text/yaml;charset=utf-8'}});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='approval-status-round2.yaml';a.click();URL.revokeObjectURL(a.href)}};
$('#approveVisible').onclick=()=>{{sync();for(const x of filtered())state.screens[x.id].status='approved';localStorage.setItem(STORAGE,JSON.stringify(state));render()}};
document.addEventListener('change',e=>{{if(e.target.matches('.statusSelect,.requiredSelect'))save()}});document.addEventListener('input',e=>{{if(e.target.matches('.note')){{state.screens[e.target.dataset.id].note=e.target.value;localStorage.setItem(STORAGE,JSON.stringify(state))}}}});
render();
</script>
</body></html>'''
    OUT.write_text(html,encoding='utf-8')
    print(f'Wrote {OUT} ({OUT.stat().st_size:,} bytes)')

if __name__=='__main__': main()
