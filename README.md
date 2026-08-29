# Personal Agent Skills

Reusable, vendor-neutral agent skills organized by capability domain. Each skill is a self-contained package rooted at `SKILL.md`; shared assets and knowledge across skills lives in `shared/`.

## Layout

- `skills/*` — skills available in this repository, organized by domain (and sub-domain)
- `shared/` — reusable assets and knowledge
- `templates/skill/` — starting structure for new skills
- `migrate_prompts` — a landing folder to add standalone markdown files of standalone prompts, ready to hand to off to an agent to migrate into skill definitions

## Using a skill

Read the selected skill's `SKILL.md`, then load only the references it names for the current task. Treat the paths in this repository as portable; do not assume a particular agent runtime.

## Adding a skill

Run `just add-skill <path>` to copy `templates/skill/` under `skills/<path>`. For example, `just add-skill newsletter/medium-custom` creates `skills/newsletter/medium-custom/` and initializes its skill name. Complete `SKILL.md` and `agents/openai.yaml`. Keep procedural instructions in `SKILL.md`, UI metadata in `agents/openai.yaml`, detailed knowledge in `references/`, deterministic tools in `scripts/`, and output resources in `assets/`.

## Migrating standalone prompts

Add a markdown for each prompt you want to migrate in `migrate_prompts`. The [Skill mapper](migrate_prompts/mapper.yaml) file must be update with the mapping of skill file name (i.e. the markdown file name) to the location where you want to store the skill. 

Note the target location is a relative path to the /skills folder.

At that point, you can hand off the migration to an agent to migrate all existing markdown files in that folder into skills in this repository.

For additional clarifications, consult [Migration README](migrate_prompts/README.md).