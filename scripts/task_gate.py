#!/usr/bin/env python3
"""Cổng thực thi subtask: đóng khi thiếu DoR, dependency, bằng chứng hoặc review."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/execution/plan.json"
STATE = ROOT / "docs/execution/state.json"
DOR = {
    "DOR01": "Mục tiêu, trong/ngoài phạm vi và acceptance đã rõ",
    "DOR02": "Nguồn, ownership, hợp đồng và quyết định chặn đã khóa cho phạm vi",
    "DOR03": "Phân quyền, PII, concurrency/idempotency và failure modes đã xét",
    "DOR04": "Phụ thuộc và đầu vào bàn giao đã có trên baseline làm việc",
    "DOR05": "Lệnh kiểm chứng và môi trường thật đã xác định",
    "DOR06": "Migration/rollback hoặc lý do không áp dụng được review",
    "DOR07": "Người thực hiện, phạm vi quyền và điều kiện dừng đã xác định",
}
SCOPE_RE = re.compile(r"(?:\*|[a-z][a-z0-9._-]*(?::(?:[a-z][a-z0-9._-]*|\*))*)$")


class GateError(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def task_fingerprint(node):
    # dependency_scopes controls invalidation routing; it is not a task-output change.
    return digest({key: value for key, value in node.items() if key != "dependency_scopes"})


def scope_valid(value):
    return (isinstance(value, str) and bool(SCOPE_RE.fullmatch(value))
            and ("*" not in value or value == "*" or value.endswith(":*")))


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def local_path(root, value):
    if not isinstance(value, str) or not value.strip():
        raise GateError("Đường dẫn bằng chứng rỗng")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise GateError("Bằng chứng phải nằm trong repository")
    return path


def load_json(path):
    def unique_pairs(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise GateError(f"JSON có khóa trùng: {key}")
            obj[key] = value
        return obj
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
    except (OSError, json.JSONDecodeError) as exc:
        raise GateError(f"Không đọc được {path.name}: {exc}") from exc


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


@contextmanager
def state_lock(path):
    lock = path.with_name(path.name + ".lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise GateError("Có tiến trình đang sửa state; không chạy hai gate đồng thời. Kiểm tra tiến trình trước khi xử lý lock cũ.") from exc
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        yield
    finally:
        lock.unlink(missing_ok=True)


def validate_graph(plan):
    if plan.get("version") != 1 or not isinstance(plan.get("subtasks"), list) or not plan["subtasks"]:
        raise GateError("Plan sai schema/version hoặc không có subtask")
    nodes = {}
    for n in plan["subtasks"]:
        ident = n.get("id", "")
        if not re.fullmatch(r"[A-Z0-9]+(?:-[A-Z0-9]+)+", ident) or ident in nodes:
            raise GateError(f"ID không hợp lệ/trùng: {ident}")
        if not n.get("goal") or not isinstance(n.get("acceptance"), dict) or not n["acceptance"]:
            raise GateError(f"Thiếu goal/acceptance: {ident}")
        if not isinstance(n.get("depends_on"), list) or len(set(n["depends_on"])) != len(n["depends_on"]):
            raise GateError(f"Dependency không hợp lệ: {ident}")
        scopes = n.get("dependency_scopes", {})
        if not isinstance(scopes, dict) or not set(scopes).issubset(n["depends_on"]):
            raise GateError(f"Dependency scope khong hop le: {ident}")
        for dependency, values in scopes.items():
            if (not isinstance(values, list) or not values or len(set(values)) != len(values)
                    or any(not scope_valid(x) for x in values)):
                raise GateError(f"Dependency scope sai cho {ident} <- {dependency}")
        nodes[ident] = n
    visiting, visited = set(), set()
    def visit(ident):
        if ident not in nodes:
            raise GateError(f"Dependency không tồn tại: {ident}")
        if ident in visiting:
            raise GateError(f"Dependency có chu kỳ: {ident}")
        if ident in visited:
            return
        visiting.add(ident)
        for dep in nodes[ident]["depends_on"]:
            visit(dep)
        visiting.remove(ident)
        visited.add(ident)
    for ident in nodes:
        visit(ident)
    return nodes


def scopes_intersect(left, right):
    """Return true when hierarchical scopes overlap; '*' is a terminal wildcard."""
    for a in left:
        for b in right:
            if a == "*" or b == "*":
                return True
            aa, bb = a.split(":"), b.split(":")
            shared = min(len(aa), len(bb))
            compatible = True
            for x, y in zip(aa[:shared], bb[:shared]):
                if x == "*" or y == "*":
                    break
                if x != y:
                    compatible = False
                    break
            if compatible:
                return True
    return False


class Gate:
    def __init__(self, root, plan, state):
        self.root, self.plan, self.state = root, plan, state
        self.nodes = validate_graph(plan)
        if state.get("version") != 1 or not isinstance(state.get("tasks"), dict) or not isinstance(state.get("history"), list):
            raise GateError("State sai schema/version; không tự reset")
        unknown = set(state["tasks"]) - set(self.nodes)
        if unknown:
            raise GateError("State chứa task không còn trong plan: " + ", ".join(sorted(unknown)))
        for ident, record in state["tasks"].items():
            if not isinstance(record, dict) or record.get("status") not in {"PREPARED", "IN_PROGRESS", "REVIEW", "DONE", "BLOCKED"}:
                raise GateError(f"State không hợp lệ: {ident}")
        self.cache = {}

    def node(self, ident):
        if ident not in self.nodes:
            raise GateError(f"ID không tồn tại: {ident}")
        return self.nodes[ident]

    def source_errors(self, ident):
        errors = []
        for relative, expected in self.node(ident).get("source_hashes", {}).items():
            path = local_path(self.root, relative)
            if not path.is_file() or hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest() != expected:
                errors.append(f"Nguồn thay đổi/thiếu: {relative}; review và sinh lại plan")
        return errors

    def evidence(self, ident, path, kind, required, completion_hash=None):
        evidence = load_json(path)
        if not isinstance(evidence, dict) or evidence.get("version") != 1 or evidence.get("kind") != kind or evidence.get("task_id") != ident:
            raise GateError("Evidence sai version/kind/task_id")
        if evidence.get("task_fingerprint") != task_fingerprint(self.node(ident)):
            raise GateError("Evidence thuộc phiên bản task khác")
        for field in ["actor", "recorded_at", "environment", "baseline"]:
            val = evidence.get(field)
            if not isinstance(val, str) or not val.strip() or re.search(r"TODO|CHƯA|PLACEHOLDER", val, re.I):
                raise GateError(f"Evidence chưa điền {field}")
        try:
            stamp = datetime.fromisoformat(evidence["recorded_at"].replace("Z", "+00:00"))
            if stamp.tzinfo is None or stamp > datetime.now(timezone.utc):
                raise ValueError()
        except ValueError as exc:
            raise GateError("recorded_at phải là thời gian ISO có timezone, không nằm ở tương lai") from exc
        checks = evidence.get("checks")
        if not isinstance(checks, dict) or set(checks) != set(required):
            raise GateError("Evidence thiếu/thừa checklist: " + ", ".join(required))
        for key, check in checks.items():
            if not isinstance(check, dict) or check.get("passed") is not True or not check.get("detail") or "TODO" in check["detail"]:
                raise GateError(f"Checklist chưa đạt: {key}")
        artifacts = evidence.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts:
            raise GateError("Cần artifact thật; checkbox đơn thuần không đủ")
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                raise GateError("Artifact sai cấu trúc")
            ap = local_path(self.root, artifact.get("path"))
            if not ap.is_file() or ap.stat().st_size == 0 or file_hash(ap) != artifact.get("sha256"):
                raise GateError(f"Artifact thiếu/rỗng/đổi hash: {artifact.get('path')}")
        # Mọi AC/DoR phải trỏ tới ít nhất một artifact nằm trong manifest.
        paths = {a["path"] for a in artifacts}
        for key, check in checks.items():
            refs = check.get("artifacts")
            if not isinstance(refs, list) or not refs or not set(refs).issubset(paths):
                raise GateError(f"Checklist chưa ánh xạ artifact: {key}")
        if kind == "completion":
            impact = evidence.get("impact")
            if impact is not None:
                if not isinstance(impact, dict):
                    raise GateError("Impact metadata sai cau truc")
                classification = impact.get("classification")
                scopes = impact.get("scopes")
                summary = impact.get("summary")
                refs = impact.get("artifacts")
                if classification not in {"none", "additive", "breaking"}:
                    raise GateError("Impact classification phai la none/additive/breaking")
                if not isinstance(scopes, list) or len(set(scopes)) != len(scopes) or any(not scope_valid(x) for x in scopes):
                    raise GateError("Impact scopes khong hop le")
                if classification == "none" and scopes:
                    raise GateError("Impact none phai co danh sach scope rong")
                if classification == "breaking" and scopes != ["*"]:
                    raise GateError("Impact breaking phai dung scope *")
                if classification == "additive" and not scopes:
                    raise GateError("Impact additive can it nhat mot scope")
                if not isinstance(summary, str) or not summary.strip() or re.search(r"TODO|CHUA|PLACEHOLDER", summary, re.I):
                    raise GateError("Impact metadata thieu summary")
                if not isinstance(refs, list) or not refs or not set(refs).issubset(paths):
                    raise GateError("Impact metadata thieu artifact")
            commands = evidence.get("commands")
            if not isinstance(commands, list) or not commands:
                raise GateError("Thiếu lệnh đã chạy")
            for cmd in commands:
                if not isinstance(cmd, dict) or type(cmd.get("exit_code")) is not int or cmd["exit_code"] != 0 or not cmd.get("command") or cmd.get("artifact") not in paths:
                    raise GateError("Lệnh chưa đạt hoặc thiếu command/artifact")
        if kind == "review" and (evidence.get("decision") != "approved" or evidence.get("completion_sha256") != completion_hash):
            raise GateError("Review chưa approve đúng completion manifest")
        return {"path": path.relative_to(self.root).as_posix(), "sha256": file_hash(path)}

    def receipt_errors(self, ident, record, slot, kind, keys, completion_hash=None):
        try:
            ref = record.get(slot, {})
            path = local_path(self.root, ref.get("path"))
            if not path.is_file() or file_hash(path) != ref.get("sha256"):
                raise GateError("Manifest bằng chứng thiếu hoặc đã thay đổi")
            self.evidence(ident, path, kind, keys, completion_hash)
            return []
        except (GateError, TypeError, KeyError) as exc:
            return [f"{ident} {slot}: {exc}"]

    def dependency_errors(self, ident, record=None):
        errors = []
        for dep in self.node(ident)["depends_on"]:
            status, reasons = self.status(dep)
            if status != "DONE":
                errors.append(f"Dependency {dep}: {status}")
                continue
            if record is None or record.get("dependencies", {}).get(dep) == digest(self.state["tasks"][dep]):
                continue
            consumer_scopes = self.node(ident).get("dependency_scopes", {}).get(dep)
            completion_ref = self.state["tasks"][dep].get("completion", {})
            try:
                completion = load_json(local_path(self.root, completion_ref.get("path")))
                impact = completion.get("impact")
            except (GateError, TypeError, KeyError):
                impact = None
            # A legacy receipt or undeclared consumer scope is intentionally fail-closed.
            if (isinstance(impact, dict) and isinstance(consumer_scopes, list)
                    and impact.get("classification") in {"none", "additive"}
                    and isinstance(impact.get("scopes"), list)
                    and not scopes_intersect(impact["scopes"], consumer_scopes)):
                continue
            errors.append(f"B?n giao {dep} ?? thay ??i trong scope c?n d?ng; chu?n b? l?i")
        return errors

    def status(self, ident):
        if ident in self.cache:
            return self.cache[ident]
        self.node(ident)
        r = self.state["tasks"].get(ident)
        errors = self.source_errors(ident) + self.dependency_errors(ident, r)
        if r is None:
            answer = ("BLOCKED" if errors else "NEEDS_READY", errors or ["Chưa có hồ sơ Definition of Ready"])
        elif r["status"] == "BLOCKED":
            answer = ("BLOCKED", errors + [r.get("reason", "Bị chặn")])
        else:
            errors += self.receipt_errors(ident, r, "readiness", "readiness", DOR)
            if r["status"] in {"REVIEW", "DONE"}:
                errors += self.receipt_errors(ident, r, "completion", "completion", self.node(ident)["acceptance"])
            if r["status"] == "DONE":
                errors += self.receipt_errors(ident, r, "review", "review", {"REVIEW01": "Rà soát đạt"}, r.get("completion", {}).get("sha256"))
            answer = ("STALE" if errors else "READY" if r["status"] == "PREPARED" else r["status"], errors)
        self.cache[ident] = answer
        return answer

    def mutate(self, action, ident, evidence=None, reason=None):
        n = self.node(ident)
        status, errors = self.status(ident)
        old = self.state["tasks"].get(ident, {}).copy()
        r = old.copy()
        if action == "prepare":
            if old.get("status") in {"IN_PROGRESS", "REVIEW", "DONE"}:
                raise GateError("Cần reopen có lý do trước khi thay hồ sơ task đang làm/đã nghiệm thu")
            blocking = self.source_errors(ident) + self.dependency_errors(ident)
            if blocking:
                raise GateError("; ".join(blocking))
            ref = self.evidence(ident, evidence, "readiness", DOR)
            r = {"status": "PREPARED", "readiness": ref, "dependencies": {d: digest(self.state["tasks"][d]) for d in n["depends_on"]}}
        elif action == "start":
            if status != "READY":
                raise GateError(f"{status}: " + "; ".join(errors))
            active = [i for i,x in self.state["tasks"].items() if x["status"] in {"IN_PROGRESS", "REVIEW"}]
            if active:
                raise GateError("Hoàn tất hoặc block subtask hiện tại trước: " + ", ".join(active))
            r["status"] = "IN_PROGRESS"
        elif action == "submit":
            if status != "IN_PROGRESS":
                raise GateError(f"Chỉ submit từ IN_PROGRESS hợp lệ; hiện là {status}")
            r["completion"] = self.evidence(ident, evidence, "completion", n["acceptance"])
            r["status"] = "REVIEW"
        elif action == "accept":
            if status != "REVIEW":
                raise GateError(f"Chỉ accept từ REVIEW hợp lệ; hiện là {status}")
            r["review"] = self.evidence(ident, evidence, "review", {"REVIEW01": "Rà soát đạt"}, r["completion"]["sha256"])
            r["status"] = "DONE"
        elif action in {"block", "reopen"}:
            if not reason or not reason.strip():
                raise GateError("Cần lý do block/reopen")
            if action == "reopen" and not old:
                raise GateError("Task chưa từng bắt đầu; dùng prepare")
            r = {"status": "BLOCKED", "reason": reason}
        r["updated_at"] = now()
        self.state["tasks"][ident] = r
        self.state["history"].append({"at": now(), "action": action, "task_id": ident, "previous": old, "record_hash": digest(r)})
        self.cache.clear()


def template(gate, ident, kind):
    n = gate.node(ident)
    keys = DOR if kind == "readiness" else n["acceptance"] if kind == "completion" else {"REVIEW01": "Đối chiếu toàn bộ AC, artifacts và rủi ro; không còn lỗi chặn"}
    e = {"version": 1, "kind": kind, "task_id": ident, "task_fingerprint": task_fingerprint(n),
         "actor": "TODO: người ghi/xác nhận", "recorded_at": "TODO: ISO 8601 UTC", "environment": "TODO: môi trường thật",
         "baseline": "TODO: commit/branch hoặc snapshot tài liệu trước Git",
         "checks": {k: {"passed": False, "detail": v, "artifacts": []} for k,v in keys.items()}, "artifacts": []}
    if kind == "completion":
        e["impact"] = {"classification": "TODO", "scopes": [], "summary": "TODO: impact da duoc review", "artifacts": []}
        e["commands"] = []
    if kind == "review":
        e.update(decision="pending", completion_sha256=gate.state["tasks"].get(ident, {}).get("completion", {}).get("sha256", "TODO"))
    return e


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    p = sub.add_parser("status")
    p.add_argument("--phase")
    sub.add_parser("next")
    for name in ["check", "prompt", "prepare", "start", "submit", "accept", "block", "reopen", "template"]:
        p = sub.add_parser(name)
        p.add_argument("id")
        if name in {"prepare", "submit", "accept"}:
            p.add_argument("--evidence", required=True)
        if name in {"block", "reopen"}:
            p.add_argument("--reason", required=True)
        if name == "prompt":
            p.add_argument("--preview", action="store_true", help="Chỉ xem tài liệu, không cấp quyền thực thi")
        if name == "template":
            p.add_argument("kind", choices=["readiness", "completion", "review"])
            p.add_argument("--output", required=True)
    args = parser.parse_args()
    mutations = {"prepare", "start", "submit", "accept", "block", "reopen"}
    try:
        if args.command in mutations:
            with state_lock(STATE):
                gate = Gate(ROOT, load_json(PLAN), load_json(STATE))
                path = local_path(ROOT, args.evidence) if hasattr(args, "evidence") else None
                gate.mutate(args.command, args.id, path, getattr(args, "reason", None))
                write_json(STATE, gate.state)
                print(args.id, *gate.status(args.id))
            return 0
        gate = Gate(ROOT, load_json(PLAN), load_json(STATE))
        if args.command == "validate":
            stale = [(i,e) for i in gate.nodes for s,e in [gate.status(i)] if s == "STALE"]
            source = [(i,gate.source_errors(i)) for i in gate.nodes if gate.source_errors(i)]
            if stale or source:
                raise GateError(str(stale + source))
            print(f"Plan/state hợp lệ: {len(gate.nodes)} subtasks, DAG không chu kỳ. Hợp lệ không có nghĩa các task đã READY/DONE.")
        elif args.command in {"status", "next"}:
            for ident,n in gate.nodes.items():
                status, errors = gate.status(ident)
                if getattr(args, "phase", None) and n["phase"] != args.phase:
                    continue
                if args.command == "next" and status not in {"READY", "NEEDS_READY", "IN_PROGRESS", "REVIEW"}:
                    continue
                print(f"{ident}: {status} — {n['goal']}")
                if args.command == "next" and errors:
                    print("  " + "; ".join(errors))
        elif args.command == "template":
            output = local_path(ROOT, args.output)
            # Chỉ ghi vào khu bằng chứng, không thể dùng --output ghi đè plan/script/rules.
            if not output.is_relative_to(ROOT / "docs/execution/evidence"):
                raise GateError("Template chỉ được ghi trong docs/execution/evidence/")
            if output.exists():
                raise GateError("Không ghi đè evidence đã tồn tại")
            write_json(output, template(gate, args.id, args.kind))
            print("Đã tạo mẫu chưa đạt:", output.relative_to(ROOT))
        else:
            status, errors = gate.status(args.id)
            preview = getattr(args, "preview", False)
            # Prompt khi IN_PROGRESS chỉ để tiếp tục đúng task, không mở task khác.
            allowed = status in {"READY", "IN_PROGRESS"}
            if not allowed and not preview:
                print(f"NOT_READY {args.id}: {status}")
                for e in errors:
                    print("- " + e)
                return 1
            if args.command == "prompt":
                if preview:
                    print("PREVIEW ONLY — không được triển khai khi chưa READY\n")
                print((ROOT / f"docs/execution/prompts/{args.id}.md").read_text(encoding="utf-8"))
            else:
                print(f"{status} {args.id}")
        return 0
    except (GateError, OSError, TypeError, KeyError, AttributeError) as exc:
        print("GATE_ERROR:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
