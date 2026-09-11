#!/usr/bin/env python3
"""Kiểm thử hành vi cổng READY bằng fixture tách biệt, không đổi state dự án."""
from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest

from task_gate import DOR, Gate, GateError, digest, file_hash, load_json, now, state_lock, template, validate_graph, write_json


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="twight-gate-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        source = self.root / "source.md"
        source.write_text("Nguồn fixture\n", encoding="utf-8", newline="\n")
        def node(ident, deps):
            return {"id": ident, "goal": "Mục tiêu fixture", "depends_on": deps,
                    "acceptance": {"AC01": "Kết quả quan sát được"}, "source_hashes": {"source.md": file_hash(source)}}
        self.plan = {"version": 1, "subtasks": [node("A-01", []), node("B-01", ["A-01"]), node("C-01", [])]}
        self.state = {"version": 1, "tasks": {}, "history": []}
        self.gate = Gate(self.root, self.plan, self.state)
        self.serial = 0

    def evidence(self, ident, kind, modify=None):
        self.serial += 1
        report = self.root / f"report-{self.serial}.md"
        report.write_text("Đây là dữ liệu giả chỉ dùng trong unit test của gate.\n", encoding="utf-8")
        e = template(self.gate, ident, kind)
        e.update(actor="test-reviewer", recorded_at=now(), environment="isolated unit fixture", baseline="fixture only")
        for check in e["checks"].values():
            check.update(passed=True, artifacts=[report.name])
        e["artifacts"] = [{"path": report.name, "sha256": file_hash(report)}]
        if kind == "completion":
            e["impact"] = {"classification": "additive", "scopes": ["contract:fixture"], "summary": "fixture additive impact", "artifacts": [report.name]}
            e["commands"] = [{"command": "fixture only", "exit_code": 0, "artifact": report.name}]
        if kind == "review":
            e["decision"] = "approved"
        if modify:
            modify(e)
        path = self.root / f"evidence-{self.serial}.json"
        write_json(path, e)
        return path

    def prepare(self, ident="A-01"):
        self.gate.mutate("prepare", ident, self.evidence(ident, "readiness"))

    def submit(self, ident="A-01"):
        self.prepare(ident)
        self.gate.mutate("start", ident)
        self.gate.mutate("submit", ident, self.evidence(ident, "completion"))

    def finish(self, ident="A-01"):
        self.submit(ident)
        self.gate.mutate("accept", ident, self.evidence(ident, "review"))

    def test_no_evidence_is_not_ready(self):
        self.assertEqual(self.gate.status("A-01")[0], "NEEDS_READY")
        with self.assertRaises(GateError):
            self.gate.mutate("start", "A-01")

    def test_dependency_blocks_prepare_even_if_checkboxes_pass(self):
        with self.assertRaises(GateError):
            self.prepare("B-01")

    def test_happy_path_requires_separate_review(self):
        self.submit()
        self.assertEqual(self.gate.status("A-01")[0], "REVIEW")
        self.assertEqual(self.gate.status("B-01")[0], "BLOCKED")
        self.gate.mutate("accept", "A-01", self.evidence("A-01", "review"))
        self.assertEqual(self.gate.status("A-01")[0], "DONE")
        self.assertEqual(self.gate.status("B-01")[0], "NEEDS_READY")
        self.prepare("B-01")
        self.assertEqual(self.gate.status("B-01")[0], "READY")

    def test_dor_missing_or_failed_or_string_true_rejected(self):
        for mutate in [lambda e: e["checks"].pop("DOR02"),
                       lambda e: e["checks"]["DOR02"].update(passed=False),
                       lambda e: e["checks"]["DOR02"].update(passed="true"),
                       lambda e: e["checks"]["DOR02"].update(artifacts=[])]:
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness", mutate))

    def test_artifact_outside_repository_rejected(self):
        with self.assertRaises(GateError):
            self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness", lambda e: e["artifacts"][0].update(path="../outside.md")))

    def test_artifact_hash_mismatch_rejected(self):
        with self.assertRaises(GateError):
            self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness", lambda e: e["artifacts"][0].update(sha256="0"*64)))

    def test_empty_or_missing_artifact_rejected(self):
        path = self.evidence("A-01", "readiness")
        report = self.root / load_json(path)["artifacts"][0]["path"]
        report.write_text("", encoding="utf-8")
        with self.assertRaises(GateError):
            self.gate.mutate("prepare", "A-01", path)
        report.unlink()
        with self.assertRaises(GateError):
            self.gate.mutate("prepare", "A-01", path)

    def test_wrong_task_or_fingerprint_rejected(self):
        for mutate in [lambda e: e.update(task_id="C-01"), lambda e: e.update(task_fingerprint="old")]:
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness", mutate))

    def test_template_is_fail_closed(self):
        path = self.root / "template.json"
        write_json(path, template(self.gate, "A-01", "readiness"))
        with self.assertRaises(GateError):
            self.gate.mutate("prepare", "A-01", path)

    def test_no_timezone_or_future_timestamp_rejected(self):
        for timestamp in ["2026-01-01T00:00:00", "2999-01-01T00:00:00Z", "not-time"]:
            with self.subTest(timestamp=timestamp), self.assertRaises(GateError):
                self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness", lambda e: e.update(recorded_at=timestamp)))

    def test_no_commands_or_nonzero_result_cannot_submit(self):
        self.prepare()
        self.gate.mutate("start", "A-01")
        for mutate in [lambda e: e.update(commands=[]), lambda e: e["commands"][0].update(exit_code=1),
                       lambda e: e["commands"][0].update(exit_code=False), lambda e: e["commands"][0].update(artifact="missing")]:
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                self.gate.mutate("submit", "A-01", self.evidence("A-01", "completion", mutate))

    def test_missing_or_failed_ac_cannot_submit(self):
        self.prepare()
        self.gate.mutate("start", "A-01")
        for mutate in [lambda e: e.update(checks={}), lambda e: e["checks"]["AC01"].update(passed=False)]:
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                self.gate.mutate("submit", "A-01", self.evidence("A-01", "completion", mutate))

    def test_review_must_approve_exact_completion(self):
        self.submit()
        for mutate in [lambda e: e.update(decision="rejected"), lambda e: e.update(completion_sha256="wrong")]:
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                self.gate.mutate("accept", "A-01", self.evidence("A-01", "review", mutate))

    def test_cannot_skip_states(self):
        for action, kind in [("submit", "completion"), ("accept", "review")]:
            with self.subTest(action=action), self.assertRaises(GateError):
                self.gate.mutate(action, "A-01", self.evidence("A-01", kind))

    def test_only_one_active_task_including_review(self):
        self.submit()
        self.prepare("C-01")
        with self.assertRaises(GateError):
            self.gate.mutate("start", "C-01")
        self.gate.mutate("block", "A-01", reason="Chờ quyết định")
        self.gate.mutate("start", "C-01")
        self.assertEqual(self.gate.status("C-01")[0], "IN_PROGRESS")

    def test_tampered_receipt_invalidates_transitive_done(self):
        self.finish()
        self.finish("B-01")
        ref = self.state["tasks"]["A-01"]["completion"]
        path = self.root / ref["path"]
        path.write_text(path.read_text(encoding="utf-8") + " ", encoding="utf-8")
        fresh = Gate(self.root, self.plan, self.state)
        self.assertEqual(fresh.status("A-01")[0], "STALE")
        self.assertEqual(fresh.status("B-01")[0], "STALE")

    def test_tampered_report_invalidates_even_unchanged_manifest(self):
        self.finish()
        ref = self.state["tasks"]["A-01"]["completion"]
        report = load_json(self.root / ref["path"])["artifacts"][0]["path"]
        (self.root / report).write_text("Nội dung đã đổi", encoding="utf-8")
        self.assertEqual(Gate(self.root, self.plan, self.state).status("A-01")[0], "STALE")

    def test_source_change_invalidates_ready_and_done(self):
        self.finish()
        (self.root / "source.md").write_text("Hợp đồng đã thay đổi", encoding="utf-8")
        self.assertEqual(Gate(self.root, self.plan, self.state).status("A-01")[0], "STALE")

    def test_line_ending_only_does_not_invalidate_sources(self):
        self.prepare()
        (self.root / "source.md").write_bytes("Nguồn fixture\r\n".encode("utf-8"))
        self.assertEqual(Gate(self.root, self.plan, self.state).status("A-01")[0], "READY")

    def test_reopen_preserves_history_and_blocks_successor(self):
        self.finish()
        self.prepare("B-01")
        self.gate.mutate("reopen", "A-01", reason="Phát hiện lỗi hợp đồng")
        self.assertEqual(self.gate.status("B-01")[0], "STALE")
        self.assertEqual(self.state["history"][-1]["previous"]["status"], "DONE")

    def test_cannot_replace_done_without_reopen(self):
        self.finish()
        with self.assertRaises(GateError):
            self.prepare()

    def test_forged_done_string_is_not_accepted(self):
        self.state["tasks"]["A-01"] = {"status": "DONE"}
        gate = Gate(self.root, self.plan, self.state)
        self.assertEqual(gate.status("A-01")[0], "STALE")
        self.assertEqual(gate.status("B-01")[0], "BLOCKED")

    def _recomplete_a(self, classification="additive", scopes=None):
        self.gate.mutate("reopen", "A-01", reason="fixture revalidation")
        self.gate.mutate("prepare", "A-01", self.evidence("A-01", "readiness"))
        self.gate.mutate("start", "A-01")
        def impact(e):
            e["impact"] = {"classification": classification, "scopes": scopes if scopes is not None else ["contract:fixture"], "summary": "fixture replacement impact", "artifacts": [e["artifacts"][0]["path"]]}
        self.gate.mutate("submit", "A-01", self.evidence("A-01", "completion", impact))
        self.gate.mutate("accept", "A-01", self.evidence("A-01", "review"))

    def test_scope_intersection_handles_hierarchy_and_wildcard(self):
        from task_gate import scopes_intersect
        self.assertTrue(scopes_intersect(["contract:auth"], ["contract:auth:refresh"]))
        self.assertTrue(scopes_intersect(["contract:*"], ["contract:feed"]))
        self.assertFalse(scopes_intersect(["contract:auth"], ["data:ownership"]))

    def test_unrelated_declared_impact_keeps_successor_valid(self):
        self.plan["subtasks"][1]["dependency_scopes"] = {"A-01": ["data:ownership"]}
        self.gate = Gate(self.root, self.plan, self.state)
        self.finish("A-01")
        self.finish("B-01")
        self._recomplete_a(scopes=["contract:auth:refresh"])
        self.assertEqual(self.gate.status("B-01")[0], "DONE")

    def test_intersecting_or_breaking_impact_stales_successor(self):
        self.plan["subtasks"][1]["dependency_scopes"] = {"A-01": ["contract:auth"]}
        self.gate = Gate(self.root, self.plan, self.state)
        self.finish("A-01")
        self.finish("B-01")
        self._recomplete_a(scopes=["contract:auth:refresh"])
        self.assertEqual(self.gate.status("B-01")[0], "STALE")
        # A separate fixture demonstrates that breaking changes ignore narrow consumer scopes.
        self.state = {"version": 1, "tasks": {}, "history": []}
        self.gate = Gate(self.root, self.plan, self.state)
        self.finish("A-01")
        self.finish("B-01")
        self._recomplete_a(classification="breaking", scopes=["*"])
        self.assertEqual(self.gate.status("B-01")[0], "STALE")

    def test_duplicate_unknown_and_cycle_graph_rejected(self):
        for mutate in [lambda p: p["subtasks"].append(copy.deepcopy(p["subtasks"][0])),
                       lambda p: p["subtasks"][0].update(depends_on=["MISSING-01"]),
                       lambda p: p["subtasks"][0].update(depends_on=["B-01"]),
                       lambda p: p["subtasks"][1].update(dependency_scopes={"A-01": ["contract:*:unsafe"]})]:
            p = copy.deepcopy(self.plan)
            mutate(p)
            with self.subTest(mutate=mutate), self.assertRaises(GateError):
                validate_graph(p)

    def test_unknown_id_and_state_rejected(self):
        with self.assertRaises(GateError):
            self.gate.status("MISSING-01")
        self.state["tasks"]["MISSING-01"] = {"status": "DONE"}
        with self.assertRaises(GateError):
            Gate(self.root, self.plan, self.state)

    def test_duplicate_json_keys_rejected(self):
        path = self.root / "duplicate.json"
        path.write_text('{"version": 1, "version": 2}', encoding="utf-8")
        with self.assertRaises(GateError):
            load_json(path)

    def test_concurrent_state_mutation_is_rejected(self):
        path = self.root / "state.json"
        with state_lock(path):
            with self.assertRaises(GateError):
                with state_lock(path):
                    self.fail("Không được giữ lock thứ hai")
        self.assertFalse(path.with_name("state.json.lock").exists())


class RealPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.plan = load_json(cls.root / "docs/execution/plan.json")
        cls.nodes = validate_graph(cls.plan)

    def ancestors(self, ident):
        result = set()
        stack = list(self.nodes[ident]["depends_on"])
        while stack:
            current = stack.pop()
            if current not in result:
                result.add(current)
                stack.extend(self.nodes[current]["depends_on"])
        return result

    def test_every_p1_implementation_is_behind_g1(self):
        for ident,n in self.nodes.items():
            if n["priority"] == "P1":
                self.assertIn("G1-01", self.ancestors(ident), ident)

    def test_every_p2_is_behind_g2(self):
        for ident,n in self.nodes.items():
            if n["priority"] == "P2":
                self.assertIn("G2-01", self.ancestors(ident), ident)

    def test_g1_does_not_depend_on_p1_or_p2(self):
        for ident in self.ancestors("G1-01"):
            self.assertEqual(self.nodes[ident]["priority"], "P0", ident)

    def test_g2_does_not_depend_on_p2(self):
        for ident in self.ancestors("G2-01"):
            self.assertNotEqual(self.nodes[ident]["priority"], "P2", ident)

    def test_all_functions_and_screens_covered(self):
        import re
        fids = set(re.findall(r"^## ([A-Z]+-\d+) -", (self.root/"docs/reference/FUNCTION_SPECIFICATIONS.md").read_text(encoding="utf-8"), re.M))
        self.assertEqual(fids, set(self.plan["function_coverage"]))
        screens = load_json(self.root/"design/data/screen-inventory.json")
        self.assertEqual({s["id"] for s in screens}, {s["screen"] for s in self.plan["screen_coverage"]})
        self.assertEqual(len(fids), 66)
        for fid in fids:
            be = [t for t in self.plan["tasks"] if t["track"] == "BE" and t["functions"] == [fid]]
            self.assertEqual(len(be), 1, fid)

    def test_each_subtask_has_prompt_goal_and_exact_preflight(self):
        for ident,n in self.nodes.items():
            text = (self.root/f"docs/execution/prompts/{ident}.md").read_text(encoding="utf-8")
            self.assertIn(n["goal"], text)
            self.assertIn(f"task_gate.py check {ident}", text)
            for ac in n["acceptance"]:
                self.assertIn(ac, text)

    def test_prompt_order_contains_every_subtask_once_after_dependencies(self):
        import re
        text = (self.root/"docs/execution/PROMPT_ORDER.md").read_text(encoding="utf-8")
        ordered = re.findall(r"\| \d{3} \| \[([A-Z0-9-]+)\]\(prompts/", text)
        self.assertEqual(len(ordered), len(self.nodes))
        self.assertEqual(set(ordered), set(self.nodes))
        positions = {ident: i for i, ident in enumerate(ordered)}
        for ident, node in self.nodes.items():
            for dependency in node["depends_on"]:
                self.assertLess(positions[dependency], positions[ident], f"{dependency} phải trước {ident}")

    def test_parent_child_integrity(self):
        children = []
        for t in self.plan["tasks"]:
            for ident in t["subtasks"]:
                children.append(ident)
                self.assertEqual(self.nodes[ident]["task_id"], t["id"])
        self.assertEqual(len(children), len(set(children)))
        self.assertEqual(set(children), set(self.nodes))


if __name__ == "__main__":
    unittest.main(verbosity=2)
