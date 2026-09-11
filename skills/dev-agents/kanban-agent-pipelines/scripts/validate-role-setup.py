#!/usr/bin/env python3
"""Validate a role/skills directory snapshot; does not prove runtime activation.

Use --profiles-root for any exported <role>/skills/**/SKILL.md layout.
HERMES_HOME is supported only as an explicit legacy adapter input.
Requires PyYAML; missing parsing support is an error, never a partial pass.
"""
import argparse
import os
from pathlib import Path
import re
import sys

ROLES = ['architect', 'planning', 'developer', 'qa', 'integration', 'judge', 'read-and-summarize']


def validate(profiles_root, roles):
    try:
        import yaml
    except ImportError:
        return ['PyYAML is required to validate metadata; no validation performed.']
    errors = []
    for role in roles:
        profile = profiles_root / role
        names = {}
        for path in sorted(profile.glob('skills/**/SKILL.md')):
            try:
                text = path.read_text()
                match = re.fullmatch(r'---\r?\n(.*?)\r?\n---\r?\n(.*)', text, re.S)
                if not match or not match[2].strip():
                    raise ValueError('missing frontmatter delimiters or empty body')
                data = yaml.safe_load(match[1])
                if not isinstance(data, dict):
                    raise ValueError('frontmatter must be a mapping')
                for key in ('name', 'description'):
                    if not isinstance(data.get(key), str) or not data[key].strip():
                        raise ValueError(f'{key} must be a non-empty string')
                names.setdefault(data['name'], []).append(path)
            except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
                errors.append(f'{path}: {error}')
        required = [role, 'agent-self-learning']
        if role == 'read-and-summarize':
            required.append('knowledge-handoff-summary')
        for name in required:
            matches = names.get(name, [])
            if len(matches) != 1:
                errors.append(f'{role}: expected exactly one skill named {name!r}, found {len(matches)}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles-root', type=Path,
                        help='Explicit directory containing <role>/skills/**/SKILL.md')
    parser.add_argument('roles', nargs='*', choices=None)
    args = parser.parse_args()
    roles = args.roles or ROLES
    if any(role not in ROLES for role in roles):
        parser.error('Unknown role; expected one of: ' + ', '.join(ROLES))
    profiles_root = args.profiles_root
    if profiles_root is None:
        legacy_home = os.environ.get('HERMES_HOME')
        if not legacy_home:
            parser.error('Pass --profiles-root; no active runtime or home directory is assumed.')
        profiles_root = Path(legacy_home) / 'profiles'
    errors = validate(profiles_root, roles)
    for error in errors:
        print('FAIL ' + error)
    print(f"{'FAIL' if errors else 'PASS'}: {len(roles)} role snapshots checked")
    print('Checks names, metadata, bodies and dependencies only; not activation, model routing or dispatch.')
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())
