"""Import the explicitly approved personal Codex packages, preserving source bytes."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "migrate_skills/codex-personal-snapshot.json"
TARGETS = {
    "narrative-style": "skills/writing/narrative-style",
    **{name: f"skills/video-generation/{name}" for name in (
        "generate-video-essay", "generate-essay-audio", "animate-recorded-audio"
    )},
    **{name: f"skills/game-development/godot/{name}" for name in (
        "godot-foundations", "godot-performance", "godot-ps1-art-direction"
    )},
}
IGNORED = {".DS_Store", "__pycache__", ".git", ".pytest_cache"}


def fingerprint(folder):
    return {
        str(path.relative_to(folder)): {
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "executable": bool(path.stat().st_mode & 0o111),
        }
        for path in sorted(folder.rglob("*"))
        if path.is_file() and not IGNORED.intersection(path.relative_to(folder).parts)
        and path.suffix != ".pyc"
    }


def sync(manifest, source_root, repo):
    # Validate every source before replacing any destination.
    for package in manifest["packages"]:
        source = source_root / package["name"]
        if not (source / "SKILL.md").is_file() or fingerprint(source) != package["files"]:
            raise ValueError(f"Source differs from approved snapshot: {source}")
        target = (repo / package["target"]).resolve()
        if not target.is_relative_to((repo / "skills").resolve()):
            raise ValueError(f"Destination must be beneath skills/: {target}")
    for package in manifest["packages"]:
        target = repo / package["target"]
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source_root / package["name"], target,
                        ignore=shutil.ignore_patterns(*IGNORED, "*.pyc"))
        if fingerprint(target) != package["files"]:
            raise ValueError(f"Copied package differs from snapshot: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path.home() / ".codex/skills")
    parser.add_argument("--record-snapshot", action="store_true",
                        help="Explicitly approve current source hashes without copying packages")
    args = parser.parse_args()
    if args.record_snapshot:
        packages = []
        for name, target in TARGETS.items():
            source = args.source_root / name
            if not (source / "SKILL.md").is_file():
                raise ValueError(f"Missing source skill: {source}")
            packages.append({"name": name, "target": target, "files": fingerprint(source)})
        MANIFEST.write_text(json.dumps({"source": "Codex personal skills", "packages": packages}, indent=2) + "\n")
        print(f"Recorded {len(packages)} personal skill packages.")
    else:
        manifest = json.loads(MANIFEST.read_text())
        sync(manifest, args.source_root, ROOT)
        print(f"Imported and verified {len(manifest['packages'])} personal skill packages.")


if __name__ == "__main__":
    main()
