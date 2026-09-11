#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CiHelperTests(unittest.TestCase):
    def test_sbom_and_checksum_manifest(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets = root / "project.assets.json"
            assets.write_text(json.dumps({"libraries": {"Example.Package/1.2.3": {"type": "package"}}}), encoding="utf-8")
            lock = root / "package-lock.json"
            lock.write_text(json.dumps({"packages": {"node_modules/example": {"version": "4.5.6"}}}), encoding="utf-8")
            artifact_dir = root / "artifacts"
            sbom = artifact_dir / "sbom.cdx.json"
            subprocess.run([sys.executable, str(ROOT / "scripts/ci/generate_sbom.py"), "--assets", str(assets), "--package-lock", str(lock), "--output", str(sbom)], check=True)
            data = json.loads(sbom.read_text(encoding="utf-8"))
            self.assertEqual(data["bomFormat"], "CycloneDX")
            self.assertEqual(len(data["components"]), 2)
            manifest = artifact_dir / "SHA256SUMS"
            command = [sys.executable, str(ROOT / "scripts/ci/write_checksums.py"), "--root", str(artifact_dir), "--output", str(manifest)]
            subprocess.run(command, check=True)
            subprocess.run([*command, "--verify"], check=True)


if __name__ == "__main__":
    unittest.main()
