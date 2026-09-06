# Personal Agent Skills

Reusable, vendor-neutral agent know-how: skills organized by capability domain, plus the agent role definitions and the standing working conventions this repo's owner runs on. Each skill is a self-contained package rooted at `SKILL.md`; shared assets and knowledge across skills lives in `shared/`.

## Layout

- `skills/*` — skills available in this repository, organized by domain (and sub-domain)
- `agents/*` — reusable agent role definitions (architect, planning, developer, qa, integration, read-and-summarize), one `AGENT.md` per role
- `AGENTS.md` — the standing working conventions (TDD-first, `just` recipes, script-once-loop, docs-as-source-of-truth, knowledge handoff, communication style)
- `shared/` — reusable assets and knowledge
- `templates/skill/` — starting structure for new skills
- `migrate_prompts` — a landing folder to add standalone markdown files of standalone prompts, ready to hand to off to an agent to migrate into skill definitions
- `migrate_skills/` — a staging folder for lifting and shifting complete skill packages into the repository taxonomy

## Using a skill

Read the selected skill's `SKILL.md`, then load only the references it names for the current task. Treat the paths in this repository as portable; do not assume a particular agent runtime.

## Using an agent

Each role definition in `agents/<name>/AGENT.md` is a portable agent contract: YAML frontmatter (`name`, `description`, `model`, `tools`) plus the persona body in the house style ('Your job' steps, 'Absolute rules', no soft language, 'report to X'). The five-role QA-first pipeline they implement is documented in `skills/dev-agents/`. Per-repo rules are never baked into these — they load from the consuming project's own context file.

## Adding a skill

Run `just add-skill <path>` to copy `templates/skill/` under `skills/<path>`. For example, `just add-skill newsletter/medium-custom` creates `skills/newsletter/medium-custom/` and initializes its skill name. Complete `SKILL.md` and `agents/openai.yaml`. Keep procedural instructions in `SKILL.md`, UI metadata in `agents/openai.yaml`, detailed knowledge in `references/`, deterministic tools in `scripts/`, and output resources in `assets/`.

## Migrating standalone prompts

Add a markdown for each prompt you want to migrate in `migrate_prompts`. The [Skill mapper](migrate_prompts/mapper.yaml) file must be update with the mapping of skill file name (i.e. the markdown file name) to the location where you want to store the skill. 

Note the target location is a relative path to the /skills folder.

At that point, you can hand off the migration to an agent to migrate all existing markdown files in that folder into skills in this repository.

For additional clarifications, consult [Migration README](migrate_prompts/README.md).

## Migrating skills

Place complete skill folders in `migrate_skills/` and map each folder name to its target parent path in [the complete-skill mapper](migrate_skills/mapper.yaml). The mapped value is relative to `skills/` and does not include the skill folder name.

Run `just migrate-skills` to migrate every mapped package, or run `just migrate-skill <folder-name> <target-parent>` for one package. This workflow preserves the complete directory rather than creating a new template: `SKILL.md`, `agents/openai.yaml`, assets, references, scripts, binary files, and executable files move together. It validates the folder name against the skill frontmatter, refuses to overwrite existing targets, compares the copied package with its source, and removes the staged source only after verification succeeds.

For the mapper format, safety rules, and examples, consult the [complete skill migration guide](migrate_skills/README.md).
