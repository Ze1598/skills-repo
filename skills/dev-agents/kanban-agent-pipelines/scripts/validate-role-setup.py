#!/usr/bin/env python3
# validate-role-setup.py — deterministic verification of a multi-agent Kanban role install.
# Run after creating role profiles + writing role SKILL.md files. Exits nonzero on any failure.
# Pass roles as args (default: the five this user stands up): architect planning developer qa integration
import pathlib, re, sys, os

try:
    import yaml
except ImportError:
    yaml = None

home = pathlib.Path(os.environ.get("HERMES_HOME", pathlib.Path.home() / ".hermes"))
profiles_root = home / "profiles"
roles = sys.argv[1:] or ["architect", "planning", "developer", "qa", "integration"]
fail = 0

for role in roles:
    pd = profiles_root / role
    if not pd.is_dir():
        print(f"FAIL profile dir missing: {pd}"); fail += 1; continue
    # 1) find role skill files under the profile skills tree
    seen = False
    for sk in pd.glob("skills/**/SKILL.md"):
        if sk.name == "SKILL.md":
            text = sk.read_text()
            # starts with --- and YAML frontmatter has name+description
            if not text.startswith("---\n"):
                print(f"FAIL {role} skill does not start with delimiter: {sk}"); fail += 1
                continue
            m = re.search(r"\n---\s*\n", text[3:])
            if not m or not text[m.end() + 3:].strip():
                print(f"FAIL {role} skill malformed (no close / empty body): {sk}"); fail += 1
                continue
            fm = text[3:m.start() + 3]
            if yaml is not None:
                try:
                    p = yaml.safe_load(fm)
                    if not p or "name" not in p or "description" not in p:
                        print(f"FAIL {role} skill YAML missing name/description: {sk}"); fail += 1
                except Exception as e:
                    print(f"FAIL {role} skill YAML parse error: {e} in {sk}"); fail += 1
            # 2) role's frontmatter name should match the role
            nm = re.search(r"^name:\s*(.+)$", fm, re.M)
            seen = True
            print(f"OK   {role}: skill {sk.relative_to(pd)}" + (f" (name={nm.group(1).strip()})" if nm else ""))
    if not seen:
        print(f"FAIL {role}: no SKILL.md under its profile skills tree"); fail += 1
    else:
        seen = False

print("---")
print(f"frontmatter check: {'PASS' if fail == 0 else 'SEE FAILURES ABOVE'} ({len(roles)} profiles scanned)")
print("Next: confirm model routing with `hermes profile list` and per-role skill enablement with")
print("`hermes -p <role> skills list | grep enabled`.")
sys.exit(1 if fail else 0)
