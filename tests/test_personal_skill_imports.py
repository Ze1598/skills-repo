"""Verify the approved Codex snapshots without requiring a local Codex install."""

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "migrate_skills" / "codex-personal-snapshot.json"
EXPECTED = {
    "narrative-style": "skills/writing/narrative-style",
    **{name: f"skills/video-generation/{name}" for name in (
        "generate-video-essay", "generate-essay-audio", "animate-recorded-audio"
    )},
    **{name: f"skills/game-development/godot/{name}" for name in (
        "godot-foundations", "godot-performance", "godot-ps1-art-direction"
    )},
}


class PersonalSkillImportTests(unittest.TestCase):
    def test_complete_packages_match_approved_source_bytes_and_executable_flags(self):
        manifest = json.loads(MANIFEST.read_text())
        self.assertEqual({p["name"]: p["target"] for p in manifest["packages"]}, EXPECTED)
        for package in manifest["packages"]:
            with self.subTest(skill=package["name"]):
                target = ROOT / package["target"]
                files = {str(p.relative_to(target)): p for p in target.rglob("*") if p.is_file()}
                self.assertEqual(set(files), set(package["files"]))
                for name, expected in package["files"].items():
                    self.assertEqual(hashlib.sha256(files[name].read_bytes()).hexdigest(), expected["sha256"], name)
                    self.assertEqual(bool(files[name].stat().st_mode & 0o111), expected["executable"], name)
                metadata = yaml.safe_load((target / "SKILL.md").read_text().split("---", 2)[1])
                self.assertEqual(metadata["name"], package["name"])
                self.assertTrue(metadata["description"])

    def test_legacy_name_routes_to_existing_video_skill(self):
        target = ROOT / "skills/social-media-content/leadership-visual-essay"
        text = (target / "SKILL.md").read_text()
        metadata = yaml.safe_load(text.split("---", 2)[1])
        self.assertEqual(metadata["name"], "leadership-visual-essay")
        self.assertIn("../../video-generation/generate-video-essay/SKILL.md", text)
        self.assertTrue((target / "../../video-generation/generate-video-essay/SKILL.md").is_file())
        self.assertNotIn("eleven_multilingual_v2", text)
        self.assertLess(len(text.splitlines()), 25)

    def test_video_sibling_skill_links_resolve(self):
        for source, dependency in (
            ("generate-video-essay", "generate-essay-audio"),
            ("generate-video-essay", "animate-recorded-audio"),
            ("animate-recorded-audio", "generate-video-essay"),
        ):
            with self.subTest(source=source, dependency=dependency):
                target = ROOT / EXPECTED[source]
                self.assertIn(f"../{dependency}/SKILL.md", (target / "SKILL.md").read_text())
                self.assertTrue((target / ".." / dependency / "SKILL.md").is_file())

    def test_import_replaces_stale_files_and_rejects_changed_sources_before_writes(self):
        spec = importlib.util.spec_from_file_location("import_personal_skills", ROOT / "scripts/import_personal_skills.py")
        importer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(importer)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            repo = root / "repo"
            packages = []
            for name in ("first", "second"):
                folder = source / name
                folder.mkdir(parents=True)
                (folder / "SKILL.md").write_text(f"name: {name}\n")
                packages.append({"name": name, "target": f"skills/{name}", "files": importer.fingerprint(folder)})
                target = repo / "skills" / name
                target.mkdir(parents=True)
                (target / "stale.txt").write_text("old")
            manifest = {"packages": packages}
            (source / "second/SKILL.md").write_text("changed")
            with self.assertRaises(ValueError):
                importer.sync(manifest, source, repo)
            self.assertTrue((repo / "skills/first/stale.txt").is_file())
            self.assertFalse((repo / "skills/first/SKILL.md").exists())
            (source / "second/SKILL.md").write_text("name: second\n")
            importer.sync(manifest, source, repo)
            for package in packages:
                self.assertEqual(importer.fingerprint(repo / package["target"]), package["files"])


if __name__ == "__main__":
    unittest.main()
