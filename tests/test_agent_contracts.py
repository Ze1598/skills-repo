"""Static contract checks; these do not validate a live Hermes dispatcher."""
import ast
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ROLES = ('architect', 'planning', 'qa', 'developer', 'integration', 'judge', 'read-and-summarize')
DOCS = [*ROOT.glob('agents/*/AGENT.md'), *ROOT.glob('skills/dev-agents/**/*.md')]

class AgentContracts(unittest.TestCase):
    def test_role_metadata_and_references(self):
        for role in ROLES:
            text = (ROOT / 'agents' / role / 'AGENT.md').read_text()
            for field in ('name', 'description', 'model', 'tools'):
                self.assertRegex(text, rf'(?m)^{field}: .+', role)
            self.assertIn(f'name: {role}\n', text)
        for path in DOCS:
            for target in re.findall(r'`(agents/[^`]+/AGENT.md)`', path.read_text()):
                targets = [target.replace('<role>', role) for role in ROLES] if '<role>' in target else [target]
                for resolved in targets:
                    self.assertTrue((ROOT / resolved).is_file(), (path, resolved))

    def test_install_validator_covers_all_roles(self):
        script = ROOT / 'skills/dev-agents/kanban-agent-pipelines/scripts/validate-role-setup.py'
        tree = ast.parse(script.read_text())
        assignment = next(node for node in tree.body if isinstance(node, ast.Assign)
                          and any(isinstance(target, ast.Name) and target.id == 'ROLES'
                                  for target in node.targets))
        defaults = ast.literal_eval(assignment.value)
        self.assertEqual(set(defaults), set(ROLES))

    def test_no_obsolete_topology_or_ownership(self):
        forbidden = [r'five[- ](?:role|agent)', r'5-Role', r'MULTI-MODULE ONLY',
                     r'Single-module projects skip', r'Multi-module projects only', r'multi-module only', r'ONLY if multi-module', r'Integration card is NOT created',
                     r'parent Dev card', r'merged sequentially at Integration',
                     r'any red/failure routes BACK to Developer',
                     r'You do NOT fix code or tests post-implementation']
        for path in DOCS:
            for pattern in forbidden:
                self.assertNotRegex(path.read_text(), pattern, str(path))

    def test_executor_and_repair_owners(self):
        text = (ROOT / 'agents/integration/AGENT.md').read_text()
        self.assertRegex(text, r'every implementation.*single-module')
        self.assertIn('rerun Developer unit tests', text)
        for role in ('qa', 'planning', 'integration', 'judge'):
            text = (ROOT / f'agents/{role}/AGENT.md').read_text()
            self.assertIn('QA repairs contract defects', text)
            self.assertIn('Developer repairs implementation defects', text)
            self.assertIn('execution pass', text)

    def test_tdd_order(self):
        text = (ROOT / 'agents/developer/AGENT.md').read_text()
        stages = ['Write requirement-derived unit tests', 'confirm the expected failure',
                  '3. **Implement', '4. **Rerun']
        offsets = [text.index(stage) for stage in stages]
        self.assertEqual(offsets, sorted(offsets))

    def test_gate_context_and_permissions(self):
        for relative in ('agents/architect/AGENT.md', 'skills/dev-agents/architect/SKILL.md'):
            text = (ROOT / relative).read_text()
            self.assertIn('fresh reviewer card', text)
            self.assertIn('deterministic test evidence', text)
            self.assertIn('rerun', text)
        text = (ROOT / 'agents/planning/AGENT.md').read_text()
        self.assertRegex(text, r'(?m)^tools: .*documentation-only write')

if __name__ == '__main__':
    unittest.main()
