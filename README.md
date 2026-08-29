# Personal Agent Skills

Reusable, vendor-neutral agent skills organized by capability domain. Each skill is a self-contained package rooted at `SKILL.md`; shared assets and knowledge across skills lives in `shared/`.

## Layout

- `skills/*` — skills available in this repository, organized by domain (and sub-domain)
- `shared/` — reusable assets and knowledge
- `templates/skill/` — starting structure for new skills

## Using a skill

Read the selected skill's `SKILL.md`, then load only the references it names for the current task. Treat the paths in this repository as portable; do not assume a particular agent runtime.

## Adding a skill

Copy `templates/skill/`, rename the directory with lowercase hyphenated words, and complete `SKILL.md` and `agents/openai.yaml`. Keep procedural instructions in `SKILL.md`, UI metadata in `agents/openai.yaml`, detailed knowledge in `references/`, deterministic tools in `scripts/`, and output resources in `assets/`.
