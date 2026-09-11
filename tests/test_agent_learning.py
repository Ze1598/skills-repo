"""Regression checks for portable learning contracts and installation validation."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / 'skills/dev-agents/kanban-agent-pipelines/scripts/validate-role-setup.py'

class InstallationTests(unittest.TestCase):
    def run_fixture(self, files, role='developer'):
        with tempfile.TemporaryDirectory() as home:
            for relative, content in files.items():
                path = Path(home) / 'profiles' / role / 'skills' / relative / 'SKILL.md'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            return subprocess.run([sys.executable, str(VALIDATOR), role],
                                  env={**os.environ, 'HERMES_HOME': home},
                                  capture_output=True, text=True)

    def skill(self, name):
        return f'---\nname: {name}\ndescription: Test fixture\n---\nContract body.\n'

    def test_missing_role(self):
        self.assertNotEqual(self.run_fixture({}).returncode, 0)

    def test_unrelated_skill_is_not_role(self):
        self.assertNotEqual(self.run_fixture({'other': self.skill('unrelated')}).returncode, 0)

    def test_malformed_metadata_and_empty_body(self):
        for content in ['---\nname: [\n---\nbody',
                        '---\nname: developer\ndescription: ""\n---\nbody',
                        '---\nname: developer\ndescription: ok\n---\n']:
            with self.subTest(content=content):
                self.assertNotEqual(self.run_fixture({'role': content}).returncode, 0)

    def test_correct_role_and_dependency(self):
        result = self.run_fixture({'role': self.skill('developer'),
                                   'learning': self.skill('agent-self-learning')})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_dependency(self):
        self.assertNotEqual(self.run_fixture({'role': self.skill('developer')}).returncode, 0)

    def test_duplicate_role_rejected(self):
        files = {'a': self.skill('developer'), 'b': self.skill('developer'),
                 'learning': self.skill('agent-self-learning')}
        self.assertNotEqual(self.run_fixture(files).returncode, 0)

    def test_reader_requires_both_dependencies(self):
        files = {'role': self.skill('read-and-summarize'),
                 'learning': self.skill('agent-self-learning')}
        self.assertNotEqual(self.run_fixture(files, 'read-and-summarize').returncode, 0)
        files['citations'] = self.skill('knowledge-handoff-summary')
        self.assertEqual(self.run_fixture(files, 'read-and-summarize').returncode, 0)

class LearningContracts(unittest.TestCase):
    def test_role_skill_copies_match_canonical_definitions(self):
        for role in ('architect', 'judge'):
            canonical = (ROOT / f'agents/{role}/AGENT.md').read_text().split('---', 2)
            skill = (ROOT / f'skills/dev-agents/{role}/SKILL.md').read_text().split('---', 2)
            definition = yaml.safe_load(canonical[1])
            packaged = yaml.safe_load(skill[1])
            self.assertEqual(set(packaged), {'name', 'description', 'metadata'})
            self.assertEqual({**packaged['metadata'], 'name': packaged['name'],
                              'description': packaged['description']}, definition)
            self.assertEqual(canonical[2], skill[2])

    def test_all_roles_reference_shared_learning_contract(self):
        for path in (ROOT / 'agents').glob('*/AGENT.md'):
            self.assertIn('skills/dev-agents/agent-self-learning/SKILL.md', path.read_text(), str(path))

    def test_portable_roles_do_not_require_old_runtime(self):
        for path in (ROOT / 'agents').glob('*/AGENT.md'):
            for token in ('kanban_', 'hermes ', 'launchd', '~/.hermes', 'worker_context'):
                self.assertNotIn(token, path.read_text(), str(path))

    def test_learning_lifecycle_obligations(self):
        text = (ROOT / 'skills/dev-agents/agent-self-learning/SKILL.md').read_text()
        # Required data fields make missing feedback/version/evaluation state explicit.
        for field in ('attempt_id', 'definition_version', 'feedback_origin',
                      'missing_worker_feedback', 'review_id', 'evaluation_status',
                      'evaluation_criterion', 'regression_check'):
            self.assertIn(f'`{field}`', text)
        self.assertIn('Learning-review attempts are exempt', text)
        self.assertIn('Never mark failed work complete', text)
        self.assertIn('retain the original', text)
        self.assertIn('agents/<role>/AGENT.md', text)

if __name__ == '__main__':
    unittest.main()
