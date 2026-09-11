#!/usr/bin/env python3
"""Sinh roadmap và prompt theo ID từ nguồn dự án; không sửa trạng thái thực thi."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/execution"
BASE = ["AGENTS.md", "RULES.md", "docs/START_HERE.md", ".ai/context-map.yaml",
        "docs/PROJECT_CONTEXT.md", "docs/SERVICE_BOUNDARIES.md",
        "docs/DEFINITION_OF_READY.md", "docs/DEFINITION_OF_DONE.md"]
REF = "docs/reference/"
PHASES = [
    ("PH00", "Khảo sát, quyết định và G0", "Tuần 1, trước mã nghiệp vụ", "G0"),
    ("PH01", "Nền tảng Backend, Data và Frontend", "Tuần 1–2", "Các nền tảng được nghiệm thu"),
    ("PH02", "Tài khoản P0", "Tuần 2; chỉ mở sau nền tảng", "Account chạy và đo NFR cơ sở"),
    ("PH03", "Mạng xã hội, Bảng tin, Trò chuyện P0", "Tuần 3–8", "G1"),
    ("PH04", "Cộng đồng, RTC, Phương tiện và tài khoản P1", "Tuần 9–12, sau G1", "Các luồng P1 được kiểm chứng"),
    ("PH05", "Xóa liên dịch vụ, điều hành và nghiệm thu P1", "Tuần 13–14", "G2"),
    ("PH06", "Thương mại, AI và tìm kiếm P2 có điều kiện", "Tuần 15–18, sau G2", "G3 hoặc quyết định cắt phạm vi có bằng chứng"),
    ("PH07", "Gia cố, NFR, bảo mật và khôi phục", "Tuần 19–22", "Hồ sơ ứng viên phát hành"),
    ("PH08", "Diễn tập phát hành và bàn giao", "Tuần 23–24", "G4; sau đó mới tag/push/deploy được ủy quyền"),
]
DOMAINS = {"ACC": "account", "SOC": "social", "COM": "community", "RTC": "community",
           "CHT": "chat", "FED": "feed", "MED": "media", "MKT": "commerce", "AI": "ai", "MOD": "social"}
SERVICE_DIR = {"account": "Account", "social": "Social", "community": "Community", "chat": "Chat",
               "feed": "Feed", "media": "Media", "commerce": "Commerce", "ai": "AiSearch"}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def source_functions():
    result = {}
    for part in re.split(r"^## ", read(REF + "FUNCTION_SPECIFICATIONS.md"), flags=re.M)[1:]:
        heading, body = part.split("\n", 1)
        fid, title = heading.split(" - ", 1)
        fields = {}
        for line in body.splitlines():
            if line.startswith("| "):
                cells = [x.strip() for x in line.strip("|").split("|")]
                if len(cells) == 2:
                    fields[cells[0]] = cells[1]
        result[fid] = {"id": fid, "title": title, "spec": fields}
    for line in read(REF + "TRACEABILITY_MATRIX.md").splitlines():
        cells = [x.strip() for x in line.strip("|").split("|")]
        if len(cells) == 7 and cells[0] in result:
            result[cells[0]].update(dict(zip(["id", "contract", "data", "events", "controls", "tests", "priority"], cells)))
    assert len(result) == 66 and all("priority" in f for f in result.values())
    return result


def build():
    functions = source_functions()
    screens = json.loads(read("design/data/screen-inventory.json"))
    nodes, tasks = [], []

    def task(tid, phase, track, title, priority, domain, deps, steps, sources=(), fids=(), screen=None, note="", mode="implementation", dependency_scopes=None):
        ids = [f"{tid}-{i:02d}" for i in range(1, len(steps) + 1)]
        tasks.append({"id": tid, "phase": phase, "track": track, "title": title, "priority": priority,
                      "domain": domain, "subtasks": ids, "functions": list(fids), "screen": screen, "note": note})
        for i, (goal, actions, acceptance) in enumerate(steps):
            refs = list(dict.fromkeys(BASE + list(sources)))
            n = {"id": ids[i], "task_id": tid, "phase": phase, "track": track, "priority": priority,
                 "domain": domain, "goal": goal, "actions": actions, "depends_on": list(deps) if i == 0 else [ids[i-1]],
                 "acceptance": {f"AC{k:02d}": v for k, v in enumerate(acceptance, 1)},
                 "sources": refs, "functions": list(fids), "screen": screen, "note": note, "mode": mode,
                 "branch": f"{'docs' if mode == 'planning' else 'feat'}/{ids[i]}"}
            if i == 0 and dependency_scopes:
                n["dependency_scopes"] = dependency_scopes
            nodes.append(n)
        return ids[-1]

    def one(tid, phase, track, title, priority, domain, deps, actions, acceptance, sources=(), mode="implementation", dependency_scopes=None):
        return task(tid, phase, track, title, priority, domain, deps, [(title, actions, acceptance)], sources, mode=mode, dependency_scopes=dependency_scopes)

    audit = one("PH00-GOV-AUDIT", "PH00", "GOV", "Xác nhận nguồn, quy tắc và phạm vi thực tế", "P0", "cross-cutting", [],
        ["Đọc DOCUMENT_AUDIT.md và BLOCKERS.md; đối chiếu toàn bộ nguồn v3.0, ADR, UI 1.2 Final.",
         "Xác nhận AGENTS.md canonical trên Windows/Linux; ghi quyết định về phiên bản quy tắc và đường vào duy nhất.",
         "Ghi kiểm kê 66 chức năng, 47 màn hình; phiên bản SDK, ứng dụng, remote và Git hiện chưa có."],
        ["Có bản kiểm kê nguồn/dấu vân tay và quyết định về đường vào AGENTS không tự tham chiếu.",
         "Chủ dự án xác nhận P0/P1/P2, phạm vi đóng/tắt gap và cơ chế nghiệm thu; không xem UI approved là API approved.",
         "Mọi điểm chưa biết có owner và đầu ra cần quyết định; không đánh dấu đã build sản phẩm."],
        [REF+"SOURCE_BASELINE.md", "docs/adr/0010-priority-gates.md", "design/STATUS.md"], "planning")
    contracts = one("PH00-BE-CONTRACT", "PH00", "BE", "Khóa hợp đồng P0 và xử lý mâu thuẫn nền", "P0", "cross-cutting", [audit],
        ["Giải quyết BL-02/03/04/05/06: lỗi version, API đọc, SignalR, Kafka partition/correlation, privacy propagation.",
         "Tạo OpenAPI/schema/AsyncAPI P0 đầy đủ request/response/error/permission; đối chiếu API còn thiếu để dùng thực tế cho UI.",
         "Ghi ADR đề xuất và chỉ chốt khi có quyết định; xác định P0 text-only và các khả năng P1/P2 mặc định tắt."],
        ["Mọi API dùng ở P0 có operation, DTO và lỗi khóa; không còn endpoint suy đoán.",
         "Schema sự kiện có partition key, aggregate version, actor/scope, replay và quyền rõ; các mâu thuẫn có quyết định được chấp thuận.",
         "Có contract tests/fixtures cho luồng P0; P1/P2 giữ hợp đồng tham chiếu và danh sách quyết định còn mở."],
        [REF+x for x in ["FUNCTION_SPECIFICATIONS.md", "API_CATALOG.md", "EVENT_CATALOG.md", "SIGNALR_CATALOG.md", "TOPIC_CATALOG.md"]], "planning")
    schema = one("PH00-DATA-BOUNDARY", "PH00", "DATA", "Khóa ownership, ERD P0 và chiến lược dữ liệu", "P0", "cross-cutting", [contracts],
        ["Đối chiếu ERD trong DOCX/PDF với DATA_MODEL; cụ thể hóa bảng Chat/Feed còn mô tả tóm tắt.",
         "Khóa tài khoản DB riêng, giao dịch/outbox/inbox, seed test, version/unique, retention và migration runner.",
         "Ghi chính sách rebuild khi sự kiện đã quá retention; không dùng Kafka như bản sao lưu DB."],
        ["Mỗi bảng/aggregate có đúng một owner; sơ đồ không có FK/query xuyên DB.",
         "Schema P0 được chấp thuận, chỉ mục gắn access pattern; projection có export/checkpoint/rebuild.",
         "Kế hoạch migration từ rỗng/nâng cấp và backup/restore có lệnh cần xác minh, owner và tiêu chí RPO/RTO."],
        [REF+"DATA_MODEL.md", REF+"SERVICE_OWNERSHIP.md", REF+"OPERATIONS_BASELINE.md", "docs/DATABASE_RULES.md"], mode="planning", dependency_scopes={contracts: ["contract:data", "contract:event", "contract:ownership"]})
    toolchain = one("PH00-BE-TOOLCHAIN", "PH00", "BE", "Dựng harness kiến trúc và khóa toolchain", "P0", "building-blocks", [schema],
        ["Chốt phiên bản .NET/EF/Angular/Node/container từ tài liệu chính thức tại thời điểm triển khai; lưu lockfiles.",
         "Dựng solution skeleton, harness kiến trúc và migration rỗng để kiểm G0; chưa viết nghiệp vụ.",
         "Khởi tạo Git/remote chỉ khi được ủy quyền theo GIT_PLAYBOOK.md; sửa vấn đề ignore/manifest trước commit đầu."],
        ["global.json, Directory.Packages.props, Node/Angular lock và image pin có bằng chứng lựa chọn.",
         "Harness chứng minh Domain không phụ thuộc framework; migration rỗng chạy trên môi trường test.",
         "Lệnh build/test cơ sở được chạy thật, tài liệu local development đã ghi đúng đường dẫn."],
        ["docs/SOURCE_STRUCTURE.md", "docs/LOCAL_DEVELOPMENT.md", "docs/CODING_CONVENTIONS.md"], dependency_scopes={schema: ["data:ownership", "data:migration", "data:rebuild"]})
    g0 = one("G0", "PH00", "GATE", "Nghiệm thu kiến trúc trước khi viết nghiệp vụ", "P0", "cross-cutting", [toolchain],
        ["Rà soát bằng chứng của AUDIT, CONTRACT, BOUNDARY, TOOLCHAIN; ghi kết luận từng tiêu chí G0."],
        ["Ownership, schema P0, API/event/error đã khóa và không còn blocker trong phạm vi.",
         "ADR, sơ đồ, migration rỗng, kiểm thử kiến trúc có artifact thật được rà soát."], [REF+"QUALITY_GATES.md"], mode="planning", dependency_scopes={toolchain: ["toolchain:architecture", "toolchain:migration"]})
    infra = one("PH01-DATA-INFRA", "PH01", "DATA", "Hạ tầng dữ liệu core và migration runner", "P0", "deploy", [g0],
        ["Docker Compose PostgreSQL/Kafka/Valkey; SeaweedFS cấu hình hạ tầng, chưa mở tính năng P1.",
         "Tách DB/credentials/topic prefix dev/test/staging, healthcheck/volume/resource limit.",
         "Runner migration độc quyền theo DB; kiểm restart container không mất dữ liệu đã commit."],
        ["Một lệnh dựng hạ tầng, healthcheck và volumes đạt; thiếu cấu hình fail fast.",
         "Credential một dịch vụ không truy cập DB dịch vụ khác; không public cổng DB/broker.",
         "Chỉ một runner migration; không auto-migrate từ mỗi replica; có test restart/restore tối thiểu."],
        ["docs/LOCAL_DEVELOPMENT.md", REF+"OPERATIONS_BASELINE.md"], dependency_scopes={g0: ["architecture:data", "architecture:migration", "architecture:service-boundary"]})
    common = one("PH01-BE-PLATFORM", "PH01", "BE", "BuildingBlocks, Gateway và quan sát cơ sở", "P0", "building-blocks", [infra],
        ["Triển khai Outbox publisher, Inbox transaction, Idempotency-Key và schema envelope trong từng DB.",
         "Gateway YARP, Problem Details, ETag, correlation, JWT biên, service JWT, Kafka ACL, CORS/rate limit.",
         "Bổ sung trace RED, outbox age, lag, DLQ, retry bounded; mô phỏng broker/DB lỗi và crash sau publish."],
        ["Commit nghiệp vụ/outbox cùng giao dịch; phát lại cùng eventId không lặp tác dụng phụ.",
         "DB lỗi không phát dữ liệu ảo; Kafka down không làm mất sự kiện đã commit.",
         "BOLA checks ở dịch vụ; test contract lỗi, correlation, timeout/cancellation và kiến trúc đạt."],
        ["docs/EVENT_RULES.md", "docs/API_RULES.md", "docs/SECURITY_RULES.md", "docs/OBSERVABILITY.md", REF+"TOPIC_CATALOG.md"], dependency_scopes={infra: ["infrastructure:data", "infrastructure:messaging", "migration:runner"]})
    ci = one("PH01-BE-CI", "PH01", "BE", "CI có kiểm tra bắt buộc và bảo vệ nhánh", "P0", "deploy", [common],
        ["Thay các nhánh skip/--if-present không bảo đảm build bằng cổng yêu cầu rõ theo component đã có.",
         "Chạy unit/integration/contract/architecture/migration/scan/SBOM theo phạm vi; artifact theo SHA.",
         "Tích hợp execution gate và kiểm Git trên Linux, Windows; thiết lập ruleset remote khi được ủy quyền."],
        ["Thiếu script/build/test bắt buộc làm CI đỏ; không thể xem job skipped là sản phẩm đạt.",
         "Main yêu cầu PR và status checks thực có; bằng chứng cấu hình remote hoặc ghi chưa cấu hình và giữ chặn.",
         "CI không ghi secret, checksums/manifest không tính .git/build/cache; hook không là cổng duy nhất."],
        [".github/workflows/ci.yml", ".github/workflows/docs-validation.yml", "docs/GIT_FLOW.md", REF+"QUALITY_GATES.md"])
    fe_base = task("PH01-FE-FOUNDATION", "PH01", "FE", "Nền tảng Angular theo thiết kế đã khóa", "P0", "cross-cutting", [g0], [
        ("Dựng app shell, token, navigation và trạng thái dùng chung", ["Khóa workspace Angular/Node; nhập design token và primitives.", "Tạo shell desktop/mobile, route guards, safe deep links và feature flags tắt gap/P2."],
         ["Build/type/lint chạy thật; app shell đúng desktop/mobile và không có link chết khi flag tắt.", "Keyboard/focus, 44x44, contrast và reduced motion có kiểm chứng."]),
        ("HTTP/auth/realtime adapters có xử lý lỗi và vòng đời", ["Sinh type từ hợp đồng P0 đã khóa; auth refresh coordinator chỉ một lần, không loop.", "Map Problem Details/412/429, hủy request, response cũ; SignalR adapter tách LiveKit."],
         ["Refresh đồng thời không tạo nhiều rotation; không lộ token trong URL/log/storage ngoài policy.", "Retry giữ nội dung và khóa idempotency; mock chỉ dev/test; có component/service tests."])
    ], ["design/design.md", "design/tokens/design-tokens.json", "design/sources/11-state-matrix.md", "docs/UIUX_WORKFLOW.md"], dependency_scopes={g0: ["architecture:frontend", "architecture:service-boundary"]})
    # Mỗi service/priority có một owner migration, không tạo migration trùng cho từng endpoint.
    data_done = {}
    data_groups = [
        ("ACC", "P0", "PH02", "account, profile, refresh_token, account_setting; token hash/family/version và email/username unique"),
        ("SOC", "P0", "PH03", "follow, block, post, post_media_ref, comment, reaction; unique/check, visibility/version và cursor"),
        ("CHT", "P0", "PH03", "conversation, conversation_member, message, message_reaction, notification; unique clientMessageId và read cursor tăng"),
        ("FED", "P0", "PH03", "FeedEntry/UserSummary/PostSummary, Inbox/checkpoint; quyền/block, invalidation và rebuild"),
        ("ACC", "P1", "PH04", "password_reset_token, account_oauth, avatar refs; OTP hash/attempt/TTL và unique provider identity"),
        ("COM", "P1", "PH04", "community/member/role/member_role/channel/invite; hierarchy, owner protection, uses/version"),
        ("MED", "P1", "PH04", "UploadSession/MediaAsset, object metadata; state, expiry, reference/retention_hold và cleanup"),
        ("SOC", "P1", "PH04", "post_share và video processing/publication; không gộp nhầm visibility/privacy"),
        ("CHT", "P1", "PH04", "community permission projection, call invite, media refs; expiry và quyền stale"),
        ("DEL", "P1", "PH05", "account_deletion_request/ack theo dịch vụ, grace/purge/cancel, retention_hold; không tạo DB chung"),
        ("MOD", "P1", "PH05", "content_report/moderation_evidence/moderation_action; audit append-only và state machine"),
        ("MKT", "P2", "PH06", "listing/media_ref/inventory/order/item/payment/history; số tiền snapshot, reserved constraint, idempotency"),
        ("AI", "P2", "PH06", "ai_embedding/chunk/job/transcript/interest vector; model version, ACL, pgvector, checkpoint/rebuild")]
    contract_p1 = one("PH04-BE-CONTRACT", "PH04", "BE", "Khóa bổ sung hợp đồng P1", "P1", "cross-cutting", ["G1-01"],
        ["Giải quyết BL-07/08/09/10 và API đọc P1: OTP, deletion/cancel/ack, video status, moderation/reopen, permission revocation/RTC.",
         "Khóa API/schema/ERD P1 và cập nhật test contract; mỗi gap UI nâng cao có quyết định dùng baseline hoặc mở rộng."],
        ["Không còn API/trạng thái/owner chưa rõ trong P1 đã chọn; các quyết định có bằng chứng chấp thuận.",
         "P2 consumer chưa triển khai không gây deadlock deletion; xác định danh sách participant theo release và quy trình backfill khi bật sau."],
        [REF+"API_CATALOG.md", REF+"SECURITY_THREAT_MODEL.md", "design/sources/18-backend-contract-gaps.md"], "planning")
    contract_p2 = one("PH06-BE-CONTRACT", "PH06", "BE", "Quyết định phạm vi và hợp đồng P2", "P2", "cross-cutting", ["G2-01"],
        ["Giải quyết BL-11/12: mock payment đối lập seller QR, variants, job AI/PDF, tài nguyên và model.",
         "Chốt từng năng lực P2 nhận triển khai; OpenSearch optional mặc định tắt; không đổi nguồn thanh toán khi chưa ADR.",
         "Khóa nguồn export/RAG ACL, cancellation, invalidation/deletion và NFR/cost từng khả năng."],
        ["Danh sách P2 đưa vào release và phần hoãn được chủ dự án quyết định; cập nhật kế hoạch trước thực thi nếu cắt.",
         "OpenAPI/AsyncAPI/data model và UI thống nhất; không nối UI QR vào MockPaymentProvider.",
         "Từng P2 có giới hạn tài nguyên, fallback và test không làm hỏng P0/P1."],
        [REF+"FUNCTION_SPECIFICATIONS.md", "design/sources/18-backend-contract-gaps.md", REF+"NFR.md"], "planning")
    for code, pri, phase, detail in data_groups:
        domain = "account" if code == "DEL" else DOMAINS[code]
        tid = f"{phase}-DATA-{code}-{pri}"
        deps = [common] if pri == "P0" else [contract_p1 if pri == "P1" else contract_p2]
        if (code, "P0") in data_done and pri != "P0":
            deps.append(data_done[(code, "P0")])
        steps = [
            (f"Thiết kế lược đồ {code} {pri}", [f"Cụ thể hóa {detail}.", "Đối chiếu ERD nguồn và hợp đồng đã khóa; chọn index từ query, mapping UTC/version, data classification."],
             [f"ERD và mapping cụ thể cho {detail}; không lấn ownership.", "Mỗi constraint/index có bất biến hoặc truy vấn chứng minh; kế hoạch migration/retention được review."]),
            (f"Migration và fixture {code} {pri}", ["Viết migration do đúng service sở hữu; dữ liệu giả dev/test có danh tính/permission deterministic.", "Thực hiện expand/backfill/checkpoint khi nâng cấp; outbox/inbox/idempotency đặt trong đúng DB."],
             ["Migration từ DB rỗng và từ bản trước đều chạy; rollback code hoặc roll-forward có hướng dẫn.", "Seed không secret/PII thật; runner độc quyền; app cũ/mới tương thích trong cửa sổ chuyển tiếp."]),
            (f"Kiểm chứng dữ liệu {code} {pri}", ["Chạy constraint/race/permission/query-plan tests và đối soát fixture.", "Ghi bằng chứng restore/rebuild, backfill resume, metadata/object consistency khi liên quan."],
             [f"Test chứng minh bất biến của {detail}; không có truy vấn chéo DB.", "Bằng chứng migration/query/index và kế hoạch recovery được bàn giao cho Backend, không chỉ ảnh ERD."])
        ]
        data_done[(code, pri)] = task(tid, phase, "DATA", f"Dữ liệu {code} {pri}", pri, domain, deps, steps,
            [REF+"DATA_MODEL.md", REF+"SERVICE_OWNERSHIP.md", "docs/DATABASE_RULES.md", REF+"OPERATIONS_BASELINE.md"], note=detail)

    def phase_of(fid):
        p = functions[fid]["priority"]
        return "PH06" if p == "P2" else "PH05" if fid.startswith("MOD") or fid == "ACC-11" else "PH04" if p == "P1" else "PH02" if fid.startswith("ACC") else "PH03"

    def be_done(fid):
        return f"{phase_of(fid)}-BE-{fid}-02"

    feature_deps = {
        "ACC-02": ["ACC-01"], "ACC-03": ["ACC-02"], "ACC-04": ["ACC-03"], "ACC-05": ["ACC-04"], "ACC-07": ["ACC-05"],
        "SOC-02": ["ACC-07"], "SOC-01": ["SOC-02"], "SOC-03": ["SOC-01"], "SOC-06": ["SOC-03"],
        "SOC-04": ["SOC-06"], "SOC-05": ["SOC-04"], "SOC-07": ["SOC-06"], "SOC-08": ["SOC-07"],
        "CHT-01": ["SOC-02", "ACC-07"], "CHT-02": ["CHT-01"], "CHT-03": ["CHT-02"], "CHT-04": ["CHT-03"],
        "CHT-05": ["CHT-02"], "CHT-06": ["CHT-01"], "CHT-07": ["CHT-02"], "CHT-08": ["SOC-08", "CHT-01"],
        "FED-01": ["SOC-03", "SOC-01"], "FED-03": ["FED-01", "SOC-05", "ACC-05"], "FED-02": ["FED-03"],
        "ACC-08": ["ACC-04"], "ACC-09": ["ACC-08"], "ACC-10": ["ACC-03"], "ACC-06": ["MED-04", "ACC-05"],
        "MED-02": ["MED-01"], "MED-03": ["MED-02"], "MED-04": ["MED-03"], "MED-05": ["MED-04"], "MED-06": ["MED-04", "CHT-02"],
        "SOC-09": ["MED-04", "SOC-04"], "SOC-10": ["SOC-06"], "COM-02": ["COM-01"], "COM-03": ["COM-02"],
        "COM-04": ["COM-03", "CHT-02"], "COM-05": ["COM-03"], "RTC-01": ["COM-04", "COM-05"], "RTC-02": ["RTC-01"],
        "RTC-03": ["RTC-02"], "CHT-09": ["RTC-01", "CHT-01"],
        "ACC-11": ["COM-05", "MED-05", "SOC-10", "CHT-09"],
        "MOD-01": ["SOC-09", "COM-05", "MED-05"], "MOD-02": ["MOD-01"], "MOD-03": ["MOD-02"], "MOD-04": ["MOD-03"],
        "MKT-01": ["MED-04"], "MKT-07": ["MKT-01", "MED-05"], "MKT-02": ["MKT-01"], "MKT-03": ["MKT-01"],
        "MKT-04": ["MKT-03", "MKT-07"], "MKT-06": ["MKT-04"], "MKT-05": ["MKT-06"],
        "AI-01": ["SOC-05", "ACC-11"], "AI-02": ["AI-01"], "AI-03": ["AI-02"], "AI-04": ["AI-03", "CHT-03"],
        "AI-05": ["MED-06", "AI-01"], "AI-06": ["AI-02", "MKT-02"], "FED-05": ["AI-01", "SOC-08"], "FED-04": ["FED-05", "FED-02"]}
    for fid, f in functions.items():
        phase, pri, code = phase_of(fid), f["priority"], fid.split("-")[0]
        domain = "ai" if fid == "FED-05" else DOMAINS[code]
        dcode = "DEL" if fid == "ACC-11" else "COM" if code == "RTC" else "AI" if fid == "FED-05" else code
        data_key = (dcode, pri) if (dcode, pri) in data_done else (dcode, "P0")
        deps = [data_done[data_key], common, ci] + [be_done(d) for d in feature_deps.get(fid, [])]
        if phase == "PH03":
            deps.append("PH02-GATE-ACCOUNT-01")
        owner = f["spec"].get("Dịch vụ sở hữu", domain)
        flow = f["spec"].get("Luồng chính", f["title"])
        note = f"Owner: {owner}. Hợp đồng tham chiếu: {f['contract']}. Dữ liệu: {f['data']}. Sự kiện: {f['events']}."
        if fid in {"SOC-03", "CHT-02"}:
            note += " P0 chỉ nội dung văn bản; từ chối media refs chưa hỗ trợ theo quyết định P0, mở ở P1."
        if fid in {"RTC-02", "RTC-03", "MED-02"}:
            note += " Task BE kiểm chứng capability/adapter/hạ tầng; bytes/track đi trực tiếp từ client, không tạo endpoint chuyển tiếp media."
        if fid == "ACC-11":
            note += " Hoàn thành API Account chưa thay cho subtask xóa của từng downstream trong PH05-BE-DELETION."
        if fid == "AI-06":
            note += " OpenSearch tùy chọn: triển khai hoặc quyết định hoãn theo quy trình scope; không giả DONE."
        steps = [
            (f"Triển khai {fid}: {f['title']}", [f"Theo hợp đồng đã khóa: {flow}", f"Thực thi: {f['controls']}.",
             f"Khảo sát src/Services/{SERVICE_DIR[domain]}, tests và hợp đồng thực tế; bổ sung log/metric/trace, cancellation, test ngay cùng mã."],
             [f"Given điều kiện trước của {fid}, when thực hiện hợp lệ, then {flow}",
              f"Kiểm soát được chứng minh: {f['controls']}.", f"Ca tối thiểu chạy thật: {f['tests']}."]),
            (f"Nghiệm thu {fid} và bàn giao", [f"Rà soát {fid} với dữ liệu/HTTP/sự kiện thật; mở rộng từ happy path sang các ca {f['tests']}.",
             "Chạy unit/integration/contract/architecture phù hợp, format/analyzer/build; đồng bộ tài liệu và handoff."],
             [f"Tất cả tiêu chí {fid} có report: {f['tests']}; không test bỏ qua hoặc lỗi Critical/High.",
              "Contract/data/docs khớp; quyền, transaction, retry và lỗi phụ thuộc có bằng chứng phù hợp.",
              "Ghi đường dẫn artifact, lệnh, exit code, commit/branch và bước phụ thuộc; chưa chạy ghi chưa xác minh."])
        ]
        task(f"{phase}-BE-{fid}", phase, "BE", f["title"], pri, domain, list(dict.fromkeys(deps)), steps,
             [REF+x for x in ["FUNCTION_SPECIFICATIONS.md", "TRACEABILITY_MATRIX.md", "API_CATALOG.md", "EVENT_CATALOG.md", "DATA_MODEL.md"]]
             + ["docs/TESTING_STRATEGY.md", "docs/SECURITY_RULES.md", "docs/REALTIME_RULES.md", REF+"SIGNALR_CATALOG.md"], [fid], note=note)

    # Tách frontend theo ưu tiên của từng capability, giữ nguyên ID/route màn hình.
    frontend_terminals = {"P0": [], "P1": [], "P2": []}
    screen_links = []
    for s in screens:
        mapped = [fid for fid in s["functions"] if fid in functions]
        # Hành động phụ có trong screen nhưng bị thiếu ở inventory cũng phải có dependency.
        extra = {"AUTH-02": ["ACC-10", "ACC-08"], "FEED-01": ["SOC-10", "MOD-01", "FED-04"],
                 "FEED-03": ["SOC-04", "SOC-05"], "CHAT-02": ["MED-06", "CHT-09"],
                 "PROF-02": ["CHT-01"], "SET-02": ["ACC-08"], "MKT-02": ["MKT-04", "CHT-01"],
                 "MKT-06": ["MKT-04", "MKT-05"]}.get(s["id"], [])
        mapped = list(dict.fromkeys(mapped + extra))
        levels = sorted(set([s["priority"]] + [functions[f]["priority"] for f in mapped if functions[f]["priority"] >= s["priority"]]))
        previous = None
        for pri in levels:
            fids = [f for f in mapped if functions[f]["priority"] <= pri and (previous is None or functions[f]["priority"] == pri)]
            phase = "PH03" if pri == "P0" else "PH05" if s["id"].startswith("MOD") or s["id"] == "SET-04" else "PH04" if pri == "P1" else "PH06"
            if pri == "P0" and s["id"].startswith("AUTH"):
                phase = "PH02"
            deps = [fe_base] + [be_done(f) for f in fids]
            deps += ["G1-01", contract_p1] if pri == "P1" else ["G2-01", contract_p2] if pri == "P2" else []
            if previous:
                deps.append(previous)
            if s["id"] == "SET-04":
                deps.append("PH05-BE-DELETION-08")
            note = f"Route: {s['route']}. Vai trò: {', '.join(s['roles'])}. Chỉ bật {', '.join(fids) or 'trạng thái hệ thống'} tại {pri}. Các chức năng ưu tiên cao hơn và gap chưa khóa phải tắt."
            screen_source = "design/" + s["file"]
            content = read(screen_source)
            def section(name):
                match = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", content, re.M | re.S)
                return match.group(1).strip() if match else "Đọc đặc tả màn hình."
            steps = [
                (f"Triển khai {s['id']} {pri}: {s['title']}", [f"Mục tiêu screen: {section('Mục tiêu')}",
                 "Đối chiếu tất cả hành động/API đọc với OpenAPI thực tế, ghi capability matrix baseline/gap/tắt; không suy ra endpoint từ route.",
                 "Tạo route/component/state/adapter/tests cho capability trong phạm vi; giữ desktop/mobile, token và accessibility."],
                 [f"Màn hình {s['id']} tại {s['route']} thực hiện đúng quyền {', '.join(s['roles'])} và capability {', '.join(fids) or 'NFR/FAILURE'}.",
                  f"Trạng thái riêng được kiểm chứng: {section('Trạng thái bắt buộc').replace(chr(10), '; ')}",
                  "Loading/empty/error/401/403/404/409/412/422/429/503, offline/reconnect liên quan đều có đường xử lý; giữ dữ liệu khi retry.",
                  "Tất cả hành động thiếu hợp đồng có quyết định hoặc bị tắt đúng policy; không có mock/API bịa trên đường release."]),
                (f"QA {s['id']} {pri} trên Desktop/Mobile", ["Kiểm E2E luồng chính/lỗi/quyền/retry với Backend thật; đọc mục tiêu, hành động, component và AC UI trong screen.",
                 "Đối chiếu SVG/PNG tại 320/390/768/1024/1440 px; keyboard, focus, screen reader, 200% zoom/reflow, contrast/reduced motion.",
                 "Chạy lint/type/build/test và bàn giao ảnh, video hoặc report; không gọi screen complete nếu capability bắt buộc còn thiếu."],
                 [f"{s['id']} {pri} có mapping design → code/test, ảnh Desktop/Mobile và sai khác có lý do.",
                  "E2E thật qua auth, quyền, state và duplicate/reconnect phù hợp; không lộ dữ liệu hoặc side effect trùng.",
                  "Touch target >=44x44; focus/name/contrast AA đạt; mọi check bắt buộc có artifact và kết quả thật."])
            ]
            tid = f"{phase}-FE-{s['id']}-{pri}"
            previous = task(tid, phase, "FE", s["title"] + " " + pri, pri, "cross-cutting", list(dict.fromkeys(deps)), steps,
                [screen_source, "design/design.md", "design/tokens/design-tokens.json", "design/sources/11-state-matrix.md",
                 "design/sources/18-backend-contract-gaps.md", "design/sources/19-frontend-contract-readiness.md", "docs/UIUX_WORKFLOW.md", REF+"API_CATALOG.md"], fids, s["id"], note)
            frontend_terminals[pri].append(previous)
            screen_links.append({"screen": s["id"], "priority": pri, "task": tid, "functions": fids})

    one("PH02-GATE-ACCOUNT", "PH02", "GATE", "Đo baseline Account trước Mạng xã hội", "P0", "account",
        [be_done(x) for x in ["ACC-01", "ACC-02", "ACC-03", "ACC-04", "ACC-05", "ACC-07"]],
        ["Chạy Account smoke/integration/token race, trace Gateway và k6 cơ sở trên môi trường xác định."],
        ["API đọc p95 <300ms, ghi Outbox p95 <500ms trên dataset/tải ghi rõ; không nới ngưỡng để pass.",
         "Refresh reuse/race/permissions đạt; dashboard/metric và lệnh dựng Account lặp lại được."], [REF+"NFR.md", REF+"QUALITY_GATES.md"])
    recovery = one("PH03-DATA-RECOVERY", "PH03", "DATA", "Khôi phục P0 và rebuild Feed", "P0", "deploy",
        [be_done("FED-02"), be_done("CHT-08")],
        ["Backup mỗi DB, tách khỏi volume/máy chạy; restore vào môi trường riêng, kiểm checksum.",
         "Rebuild Feed từ source export + checkpoint + Kafka delta; duplicate/out-of-order và thay quyền không rò dữ liệu.",
         "Đo RPO/RTO và smoke Account/Post/Chat sau restart/restore."],
        ["RPO <=24h, RTO P0 <=4h có timestamps và dữ liệu đối soát.", "Rebuild không cần FK/query chéo DB, không phát email/thanh toán lặp.", "Kafka/Valkey/DB outage có runbook/alert và bằng chứng không mất dữ liệu commit."],
        [REF+"OPERATIONS_BASELINE.md", "docs/INCIDENT_RUNBOOK.md"])
    g1deps = [be_done(fid) for fid,f in functions.items() if f["priority"] == "P0"] + frontend_terminals["P0"] + [recovery, ci]
    one("G1", "PH03", "GATE", "Nghiệm thu P0 trước mọi P1", "P0", "cross-cutting", g1deps,
        ["Chạy Account → Post → Kafka → Feed và Chat lưu trước SignalR; outage, retry, DLQ, privacy và restore.", "Rà soát đầy đủ bằng chứng BE/DATA/FE P0 và lỗi nghiêm trọng."],
        ["100% acceptance P0 đạt, E2E thật và không còn Critical/High.", "Trace/dashboard/Outbox/DLQ cùng báo cáo migration/restore và UI QA đủ; không chấp nhận mock-only."], [REF+"QUALITY_GATES.md"], "planning")
    # Các downstream phải tự thực thi xóa, không để Account ghi DB của chúng.
    deletion_steps = []
    for domain, action in [
        ("social", "Ẩn/ẩn danh post/comment, dọn follow/block và bảo vệ retention_hold"),
        ("feed", "Xóa FeedEntry/UserSummary/cache trong 5 phút"),
        ("chat", "Ẩn PII profile, giữ lịch sử người khác theo policy, xử lý quyền/reconnect"),
        ("community", "Vô hiệu membership/role/invite và chuyển owner trước purge"),
        ("media", "Đối soát tham chiếu, dọn object không dùng, giữ evidence có hold"),
        ("account", "Đối soát ack/retry/timeouts, cancel trong grace, chặn completed khi thiếu participant"),
        ("cross-cutting", "Kiểm thử tích hợp hủy/purge/race/duplicate, ẩn <=5 phút, grace 30 ngày, PII <=45 ngày"),
        ("cross-cutting", "Bàn giao xóa liên dịch vụ và restore không làm sống lại dữ liệu đã xóa")]:
        deletion_steps.append((f"Xóa tài khoản: {action}", [f"Owner xử lý: {domain}; {action}.", "Chỉ qua contract/event; ghi ack cùng transaction, lặp an toàn và có metric."],
            [action + " có bằng chứng test và artifact được đối soát.", "Không query/ghi DB dịch vụ khác; thiếu ack không được completed; contract participant đã khóa."]))
    deletion = task("PH05-BE-DELETION", "PH05", "BE", "Lan truyền và đối soát xóa tài khoản", "P1", "cross-cutting", [be_done("ACC-11")],
         deletion_steps, [REF+"SECURITY_THREAT_MODEL.md", REF+"NFR.md", "docs/EVENT_RULES.md"])
    p1restore = one("PH05-DATA-RESTORE", "PH05", "DATA", "Khôi phục Media và dữ liệu P1", "P1", "deploy", [deletion, be_done("MOD-04")],
        ["Khôi phục metadata trước object; đối soát object key/size/hash và asset thiếu.", "Diễn tập retention_hold, audit, retry và deletion ledger sau restore."],
        ["Media RPO <=24h/RTO <=8h; dữ liệu P0 vẫn đạt <=4h và smoke đầy đủ.", "Object không public; audit/retention và dữ liệu xóa không bị phục hồi sai."], [REF+"OPERATIONS_BASELINE.md"])
    one("G2", "PH05", "GATE", "Nghiệm thu P1 trước P2", "P1", "cross-cutting",
        [be_done(fid) for fid,f in functions.items() if f["priority"] == "P1"] + frontend_terminals["P1"] + [deletion, p1restore],
        ["Nghiệm thu community permissions, RTC <2s, text chat khi LiveKit lỗi, Media pipeline, OTP/OAuth, moderation và deletion."],
        ["100% tiêu chí P1 trong phạm vi đạt; không Critical/High và không làm hỏng P0.", "Threat/integration/retry/restore/UI tests đạt, đúng nguồn v3.0 và ADR mới được chấp thuận."], [REF+"QUALITY_GATES.md"], "planning")
    p2life = one("PH06-DATA-LIFECYCLE", "PH06", "DATA", "Xóa, phục hồi và rebuild P2", "P2", "cross-cutting", [be_done("MKT-05"), be_done("AI-05"), be_done("FED-04")],
        ["Commerce giữ snapshot tối thiểu, ẩn PII; AI xóa chunk/vector/transcript/index theo deletion.",
         "Đăng ký participant xóa cho P2 mới bật; backfill ledger xóa cũ, export nguồn theo quyền.",
         "Restore order/inventory không phát lại payment; rebuild vector theo model/checkpoint."],
        ["Hai buyer không oversell, bù trừ một lần và restore Commerce <=8h, RPO <=24h.",
         "Dữ liệu dẫn xuất ẩn trong 5 phút, AI rebuild <=24h; replay không hồi sinh nội dung mất quyền.",
         "AI/OpenSearch tắt hoặc quá tải vẫn giữ P0/P1, có metric cost/resource và fallback test."], [REF+"OPERATIONS_BASELINE.md", REF+"SECURITY_THREAT_MODEL.md"])
    one("G3", "PH06", "GATE", "Nghiệm thu P2 và đóng phạm vi", "P2", "cross-cutting",
        [be_done(fid) for fid,f in functions.items() if f["priority"] == "P2"] + frontend_terminals["P2"] + [p2life],
        ["Đánh giá mọi P2 được chọn và NFR riêng; phần cắt phải sửa scope/dependency bằng quyết định có review trước G3."],
        ["Mọi P2 được chọn có load/fallback/cost metrics và không hồi quy P0/P1.", "Các gap QR/PDF/variants đã giải quyết hoặc tắt/hoãn minh bạch; không đánh dấu việc hoãn là DONE."], [REF+"QUALITY_GATES.md"], "planning")
    hard = task("PH07-GOV-HARDEN", "PH07", "GOV", "Gia cố ứng viên phát hành", "P0", "cross-cutting", ["G3-01"], [
        ("Đo tải và xử lý bottleneck", ["k6 50–100 user trên cấu hình/dataset cố định; API read/write, SignalR/RTC, inventory và AI queues.", "Sửa N+1, pool/lock, backpressure theo bằng chứng; không nới NFR."],
         ["Read p95 <300ms, write <500ms, SignalR <200ms, RTC <2s theo phạm vi phép đo.", "Có report CPU/RAM/disk, lỗi và ngưỡng capacity một nút; P2 không lấy tài nguyên cốt lõi."]),
        ("Rà soát bảo mật và chuỗi cung ứng", ["Chạy BOLA/XSS/SSRF/JWT/OTP/RAG injection, secret/dependency/container/license scan và SBOM.", "Diễn tập rotation/least privilege; xử lý Critical/High trước đóng."],
         ["Không có secret thật/Critical/High tồn đọng; SBOM và scan gắn cùng candidate SHA.", "RAG private filter, nội bộ service JWT/Kafka ACL, upload và moderation đạt negative tests."]),
        ("Di trú, khôi phục và rollback ứng viên", ["Restore trên môi trường tách biệt; migration empty/upgrade, backfill resume, expand/contract.", "Diễn tập rollback code khi schema tương thích hoặc roll-forward; kiểm P0 smoke và deletion reconciliation."],
         ["RPO/RTO theo từng miền đạt và backup ngoài máy/volume chạy được xác minh.", "Runbook có lệnh thật, checksum, checkpoint và người vận hành; rollback không làm mất dữ liệu."]),
        ("Đồng bộ hồ sơ bàn giao", ["Cập nhật OpenAPI/AsyncAPI/ERD/ADR, README local, dashboard/alerts, demo/test users, release notes và known limitations."],
         ["66 chức năng/47 screen được ánh xạ vào DONE hoặc scope hoãn được chấp thuận; không khai đủ khi chỉ mock.", "Tài liệu/trace/test/dashboard và cấu hình không bí mật đồng bộ ứng viên phát hành."])
    ], [REF+"NFR.md", REF+"QUALITY_GATES.md", "docs/RELEASE_CHECKLIST.md", "docs/SECURITY_RULES.md"])
    rehearsal = one("PH08-GOV-REHEARSAL", "PH08", "GOV", "Diễn tập phát hành từ môi trường sạch", "P0", "deploy", [hard],
        ["Dùng candidate SHA cố định, dựng hệ thống mới bằng runbook; chạy toàn bộ demo và smoke.", "Đối chiếu image digest/SBOM/migration/flag, diễn tập deploy/rollback trong môi trường được ủy quyền."],
        ["Clone/config/build/migration/start/demo chạy lặp lại không sửa tay DB.", "Có biên bản thời gian, môi trường, candidate SHA và rollback; lỗi mở còn lại không chặn nghiệm thu."],
        [REF+"QUALITY_GATES.md", "docs/RELEASE_CHECKLIST.md"])
    one("G4", "PH08", "GATE", "Nghiệm thu phát hành", "P0", "cross-cutting", [rehearsal],
        ["Đối chiếu DoD và release checklist trên đúng candidate SHA; xác nhận scopes, scan/SBOM, restore/rollback và demo.", "Ghi kết luận G4; thực hiện tag/push/release/deploy riêng sau khi có ủy quyền, theo Git playbook."],
        ["Không Critical/High; 100% tiêu chí bắt buộc đạt; docs/contracts khớp candidate.",
         "Backup/restore/rollback/demo có bằng chứng; tag tương lai phải trỏ đúng candidate SHA đã nghiệm thu.",
         "Chủ dự án có hồ sơ có thể kiểm tra và lệnh phát hành cụ thể; G4 không ngầm cấp quyền deploy."], [REF+"QUALITY_GATES.md", "docs/RELEASE_CHECKLIST.md"], "planning")

    # Thuộc tính sẵn sàng luôn được xét lúc chạy; không sinh DONE/READY giả.
    for n in nodes:
        # Hash văn bản chuẩn hóa LF để checkout Windows/Linux không tự làm stale.
        n["source_hashes"] = {p: hashlib.sha256(read(p).encode("utf-8")).hexdigest() for p in n["sources"]}
    return {"version": 1, "baseline_date": "2026-09-07", "policy": "fail-closed", "phases": [dict(zip(["id", "title", "window", "exit"], p)) for p in PHASES],
            "tasks": tasks, "subtasks": nodes, "function_coverage": functions, "screen_coverage": screen_links}


def prompt(n):
    ident = n["id"]
    lines = [f"# {ident} — {n['goal']}", "", "## Mục tiêu và phạm vi", "",
             f"- Phase: {n['phase']} | Nhóm: {n['track']} | Ưu tiên: {n['priority']} | Task cha: {n['task_id']}.",
             f"- Mục tiêu duy nhất: {n['goal']}.", f"- Miền: {n['domain']} | Chức năng: {', '.join(n['functions']) or 'nền tảng/quy trình'}.",
             f"- Chế độ: {n['mode']}. Chỉ sửa đầu ra trong phạm vi subtask; không làm task kế tiếp.",
             f"- Nhánh đề xuất: `{n['branch']}`; chưa được tạo chỉ vì có trong prompt.",
             f"- {n['note']}" if n["note"] else "- Bản kế hoạch không chứng minh mã ứng dụng đã tồn tại.",
             "", "## Cổng bắt buộc trước khi thực hiện", "", "```powershell",
             f"python -X utf8 scripts/task_gate.py check {ident}", "if ($LASTEXITCODE -ne 0) { throw 'NOT_READY: dừng subtask' }", "```", "",
             "Nếu chưa READY: chỉ báo lý do, phụ thuộc và bằng chứng cần bổ sung; không chỉnh mã sản phẩm, không tự ghi PASS hoặc chạy task sau.",
             "READY phải được tính lại tại thời điểm bắt đầu; đọc prompt bằng tay không bỏ qua gate. Sau READY, dùng lệnh start để khóa một subtask đang làm.",
             "", "## Phụ thuộc phải DONE có bằng chứng", ""]
    lines += [f"- `{d}`" for d in n["depends_on"]] or ["- Không có tiền nhiệm; vẫn phải chuẩn bị Definition of Ready."]
    lines += ["", "## Nguồn phải đọc", ""] + [f"- `{p}`" for p in n["sources"]]
    lines += ["- `docs/execution/BLOCKERS.md`, `docs/execution/READY_GATE.md` và hồ sơ bàn giao của các tiền nhiệm.",
              "- Hợp đồng/mã/tests/lockfile thực tế; tên thư mục trong roadmap là mục tiêu, phải xác minh trước khi dùng.",
              "", "## Các bước trong subtask", ""] + [f"{i}. {a}" for i,a in enumerate(n["actions"],1)]
    lines += ["", "## Tiêu chí chấp nhận", ""] + [f"- **{k}**: {v}" for k,v in n["acceptance"].items()]
    lines += ["", "## Kiểm chứng và bằng chứng", "",
              "- Khám phá lệnh thật trong solution/package scripts/CI. Nếu chưa có, ghi blocker hoặc tạo harness đúng phạm vi; không ghi lệnh đoán là đã chạy.",
              "- Kiểm thử mục tiêu → unit/integration/contract/architecture phù hợp → format/analyzer/build → review diff/tài liệu.",
              "- Với planning, kiểm nguồn/decision/contract bằng validator và review thay cho giả build sản phẩm.",
              "- Lưu lệnh, exit code, thời gian UTC, môi trường, artifact và SHA-256; ánh xạ đủ AC. Thiếu/skip một AC bắt buộc không được DONE.",
              "", "## Điều kiện dừng", "",
              "- Nguồn mâu thuẫn, API/data/ownership/quyền chưa khóa; dependency hoặc bằng chứng thay đổi; kiểm thử thất bại.",
              "- Không tự thêm thư viện, chạy migration phá hủy, thay production hoặc nới điều kiện READY.",
              "- Không commit, push, merge, tag, deploy hoặc gửi thông tin cho người khác nếu chưa có ủy quyền rõ cho thao tác đó.",
              "", "## Bàn giao", "",
              f"Ghi `TASK_ID={ident}`, mục tiêu, file/ký hiệu đã đổi, contract/ADR, từng AC → artifact → kết quả, lệnh thật, rủi ro và blocker.",
              "Dùng mẫu TEST_EVIDENCE/IMPLEMENTATION_REPORT. Submit chỉ chuyển REVIEW; accept sau rà soát mới DONE và mới xét task phụ thuộc.", ""]
    return "\n".join(lines)


def prompt_order(plan):
    """Render a stable topological index without inventing dependencies."""
    nodes = {n["id"]: n for n in plan["subtasks"]}
    positions = {n["id"]: i for i, n in enumerate(plan["subtasks"])}
    pending = {ident: set(n["depends_on"]) for ident, n in nodes.items()}
    completed, waves = set(), []
    while pending:
        ready = sorted((ident for ident, deps in pending.items() if deps <= completed), key=positions.__getitem__)
        if not ready:
            raise ValueError("Không thể tạo thứ tự prompt: đồ thị có chu kỳ")
        waves.append(ready)
        completed.update(ready)
        for ident in ready:
            del pending[ident]

    lines = [
        "# Thứ tự prompt theo phụ thuộc",
        "",
        "Sinh từ `build_execution_plan.py`. Đây là chỉ mục đọc/thực hiện đề nghị theo đồ thị dependency, không phải quyền bỏ qua cổng READY.",
        "Một đợt chứa các prompt không phụ thuộc lẫn nhau; có thể chuẩn bị song song khi ownership/hợp đồng ổn định và coordinator cho phép. Trước khi thực hiện bất kỳ prompt nào vẫn chạy `task_gate.py check ID`; chỉ `READY` hoặc đúng task `IN_PROGRESS` mới được làm.",
        "",
        "Bước đầu tiên luôn là `PH00-GOV-AUDIT-01`. Các mục sau có thể xuất hiện sớm trong chỉ mục nhưng vẫn bị chặn đến khi toàn bộ dependency của chính chúng `DONE` hợp lệ.",
        "",
    ]
    sequence = 0
    for number, wave in enumerate(waves, 1):
        phases = ", ".join(dict.fromkeys(nodes[ident]["phase"] for ident in wave))
        lines += [f"## Đợt {number:02d} — {phases}", "", "| STT | Prompt | Nhóm | Ưu tiên | Mục tiêu | Chờ DONE |", "|---:|---|---|---|---|---|"]
        for ident in wave:
            sequence += 1
            n = nodes[ident]
            deps = ", ".join(n["depends_on"]) or "Không; cần DoR"
            lines.append(f"| {sequence:03d} | [{ident}](prompts/{ident}.md) | {n['track']} | {n['priority']} | {n['goal']} | {deps} |")
        lines.append("")
    lines += [
        "## Cách dùng",
        "",
        "1. Chọn prompt đầu tiên của đợt sớm nhất còn khả thi, hoặc dùng `python -X utf8 scripts/task_gate.py next` để xem trạng thái thật.",
        "2. Dùng `prompt ID --preview` để đọc. Chỉ dùng `prompt ID` sau `check ID` trả exit 0.",
        "3. Hoàn thành đủ DoR → start → completion → review → accept. `DONE` hợp lệ mới mở dependency; không đánh dấu cả đợt là hoàn thành cùng lúc.",
        "4. Nếu nguồn, evidence hoặc dependency đổi, trạng thái thành `STALE`/`BLOCKED`; quay lại cổng thay vì tiếp tục theo số thứ tự.",
        "",
    ]
    return "\n".join(lines)


def outputs(plan):
    files = {"plan.json": json.dumps(plan, ensure_ascii=False, indent=2) + "\n"}
    for n in plan["subtasks"]:
        files[f"prompts/{n['id']}.md"] = prompt(n)
    files["PROMPT_ORDER.md"] = prompt_order(plan)
    for track, name in [("BE", "BACKEND"), ("DATA", "DATA"), ("FE", "FRONTEND"), ("GOV", "GOVERNANCE"), ("GATE", "QUALITY_GATES")]:
        lines = [f"# Danh mục {name}", "", "Sinh từ build_execution_plan.py; mục tiêu, acceptance và prompt nằm dưới từng ID. Trạng thái thật xem task_gate.py status.", ""]
        for phase in plan["phases"]:
            items = [t for t in plan["tasks"] if t["track"] == track and t["phase"] == phase["id"]]
            if not items:
                continue
            lines += [f"## {phase['id']} — {phase['title']}", ""]
            for t in items:
                lines += [f"### {t['id']} — {t['title']}", "", f"Ưu tiên {t['priority']}; miền {t['domain']}. {t['note']}", "",
                          "| Subtask / prompt | Mục tiêu | Phụ thuộc DONE |", "|---|---|---|"]
                for n in plan["subtasks"]:
                    if n["task_id"] == t["id"]:
                        lines.append(f"| [{n['id']}](prompts/{n['id']}.md) | {n['goal']} | {', '.join(n['depends_on']) or 'Không; cần DoR'} |")
                lines += [""]
        files[name+".md"] = "\n".join(lines)
    lines = ["# Truy vết chức năng và màn hình", "", "ID chức năng và ID màn hình là hai namespace khác nhau. AI-03 chức năng RAG vẫn thuộc phạm vi; màn hình AI-03 riêng đã bị loại.", "",
             "| Chức năng | Ưu tiên | Task Backend | Task Frontend |", "|---|---|---|---|"]
    for fid,f in plan["function_coverage"].items():
        be = next(t for t in plan["tasks"] if t["track"] == "BE" and t["functions"] == [fid])
        fes = [s["task"] for s in plan["screen_coverage"] if fid in s["functions"]]
        lines.append(f"| {fid} — {f['title']} | {f['priority']} | {be['id']} | {', '.join(fes) or 'Worker/API; không có màn hình riêng'} |")
    lines += ["", "## 47 màn hình và các lát cắt ưu tiên", "", "| Màn hình | Ưu tiên lát cắt | Task | Chức năng |", "|---|---|---|---|"]
    for s in plan["screen_coverage"]:
        lines.append(f"| {s['screen']} | {s['priority']} | {s['task']} | {', '.join(s['functions']) or 'NFR/FAILURE'} |")
    files["TRACEABILITY.md"] = "\n".join(lines) + "\n"
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Chỉ kiểm generated files đồng bộ, không ghi")
    args = parser.parse_args()
    plan = build()
    rendered = outputs(plan)
    errors = []
    for relative, content in rendered.items():
        path = OUT / relative
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                errors.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    extras = {p.relative_to(OUT).as_posix() for p in (OUT/"prompts").glob("*.md")} - set(rendered)
    errors.extend(sorted(extras))
    if errors:
        print("Generated files lệch; cần review/sinh lại: " + ", ".join(errors))
        return 1
    print(f"Execution plan: {len(plan['phases'])} phases, {len(plan['tasks'])} tasks, {len(plan['subtasks'])} subtasks, 66 functions, 47 screens")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
