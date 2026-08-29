# Personal Agent Skills

Reusable, vendor-neutral agent skills organized by capability domain. Each skill is a self-contained package rooted at `SKILL.md`; shared brand and leadership guidance lives under `shared/`.

## Layout

- `skills/content/` — newsletter and social-content generation
- `skills/video/` — visual essays and thumbnail concepts
- `skills/project-bootstrap/` — select relevant skills for a new project
- `shared/` — reusable references and brand assets
- `templates/skill/` — starting structure for new skills

## Using a skill

Read the selected skill's `SKILL.md`, then load only the references it names for the current task. Treat the paths in this repository as portable; do not assume a particular agent runtime.

## Adding a skill

Copy `templates/skill/`, rename the directory with lowercase hyphenated words, and complete `SKILL.md` and `agents/openai.yaml`. Keep procedural instructions in `SKILL.md`, UI metadata in `agents/openai.yaml`, detailed knowledge in `references/`, deterministic tools in `scripts/`, and output resources in `assets/`.
