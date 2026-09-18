from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "migrate_prompts"
SKILLS = ROOT / "skills"


class MigratedPromptTests(unittest.TestCase):
    def test_mapped_prompts_are_complete_skill_packages(self):
        mappings = yaml.safe_load((STAGING / "mapper.yaml").read_text())
        self.assertIsInstance(mappings, list)
        self.assertTrue(mappings)

        for mapping in mappings:
            self.assertEqual(len(mapping), 1)
            source_name, parent = next(iter(mapping.items()))
            name = Path(source_name).stem
            with self.subTest(name=name):
                self.assertRegex(name, r"^[a-z0-9][a-z0-9-]*$")
                self.assertRegex(parent, r"^[a-z0-9][a-z0-9-]*(/[a-z0-9][a-z0-9-]*)*$")
                source = (STAGING / source_name).read_text()
                target = SKILLS / parent / name
                content = (target / "SKILL.md").read_text()
                match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", content, re.DOTALL)
                self.assertIsNotNone(match)
                frontmatter = yaml.safe_load(match.group(1))
                self.assertEqual(frontmatter["name"], name)
                self.assertTrue(frontmatter["description"].strip())
                self.assertEqual(match.group(2), source)

                metadata = yaml.safe_load((target / "agents" / "openai.yaml").read_text())
                interface = metadata["interface"]
                self.assertTrue(interface["display_name"])
                self.assertGreaterEqual(len(interface["short_description"]), 25)
                self.assertLessEqual(len(interface["short_description"]), 64)
                self.assertIn(f"${name}", interface["default_prompt"])
                self.assertNotIn("replace-with", content + str(metadata))
                for resource in ("assets", "references", "scripts"):
                    self.assertFalse((target / resource).is_dir())


if __name__ == "__main__":
    unittest.main()
