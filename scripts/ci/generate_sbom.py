#!/usr/bin/env python3
"""Generate a small CycloneDX SBOM from NuGet assets and the npm lockfile."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def component(name: str, version: str, ecosystem: str, source: str) -> dict:
    return {
        "type": "library",
        "name": name,
        "version": version,
        "purl": f"pkg:{ecosystem}/{name}@{version}",
        "properties": [{"name": "twilight:source", "value": source}],
    }


def nuget_components(asset_paths: list[Path]) -> list[dict]:
    found: dict[tuple[str, str], dict] = {}
    for asset_path in asset_paths:
        assets = json.loads(asset_path.read_text(encoding="utf-8"))
        for library, metadata in assets.get("libraries", {}).items():
            if metadata.get("type") != "package" or "/" not in library:
                continue
            name, version = library.rsplit("/", 1)
            found[(name, version)] = component(name, version, "nuget", str(asset_path))
    return list(found.values())


def npm_components(lock_path: Path) -> list[dict]:
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    found: dict[tuple[str, str], dict] = {}
    for package_path, metadata in lock.get("packages", {}).items():
        if not package_path.startswith("node_modules/"):
            continue
        name = package_path.removeprefix("node_modules/")
        version = metadata.get("version")
        if name and isinstance(version, str) and version:
            found[(name, version)] = component(name, version, "npm", str(lock_path))
    return list(found.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--assets", type=Path, nargs="+", required=True)
    parser.add_argument("--package-lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for path in [*args.assets, args.package_lock]:
        if not path.is_file():
            raise SystemExit(f"Required dependency input is missing: {path}")
    components = sorted(
        [*nuget_components(args.assets), *npm_components(args.package_lock)],
        key=lambda item: (item["purl"], item["version"]),
    )
    if not components:
        raise SystemExit("SBOM would be empty")
    document = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": "urn:uuid:00000000-0000-0000-0000-000000000001",
        "version": 1,
        "metadata": {"timestamp": datetime.now(timezone.utc).isoformat()},
        "components": components,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    print(f"Generated CycloneDX SBOM with {len(components)} components: {args.output}")


if __name__ == "__main__":
    main()
