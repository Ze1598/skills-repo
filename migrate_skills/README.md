# Complete Skill Migration

This directory stages complete skill packages for lift-and-shift migration into the repository's `skills/` taxonomy. Unlike `migrate_prompts/`, this workflow does not create a template or rewrite metadata. It preserves the entire source folder, including `SKILL.md`, `agents/`, assets, references, scripts, binary files, and executable files.

## Stage a complete skill

Place each package directly beneath this directory:

```text
migrate_skills/
├── mapper.yaml
└── example-skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    ├── references/
    └── scripts/
```

The folder must contain `SKILL.md`, and its folder name must exactly match the `name` in that file's YAML frontmatter.

## Map destinations

Add one mapping for each staged folder:

```yaml
- example-skill: social-media-content/image-generation
- another-skill: newsletter
```

The key is the source folder name. The value is the target parent relative to `skills/`. Do not include `migrate_skills/`, `skills/`, a leading slash, `.` components, or `..` components.

The first example resolves to:

```text
migrate_skills/example-skill/
    → skills/social-media-content/image-generation/example-skill/
```

## Run the migration

Migrate every mapped package:

```bash
just migrate-skills
```

Or migrate one staged package directly:

```bash
just migrate-skill example-skill social-media-content/image-generation
```

For each package, the recipe:

1. Validates the source and target names.
2. Requires a source `SKILL.md`.
3. Confirms that the folder and frontmatter names match.
4. Refuses to overwrite an existing target.
5. Copies the complete package to its mapped destination.
6. Compares the copied tree with the source.
7. Removes the staged source only after the comparison succeeds.

The mapper entry remains after migration so the operation is auditable. Remove or comment out completed entries before running the batch recipe again.

## Difference from prompt migration

| Workflow | Source | Behavior |
|---|---|---|
| `migrate_prompts/` | Flat Markdown prompt | Create a template package, populate `SKILL.md`, and author OpenAI metadata |
| `migrate_skills/` | Complete skill directory | Preserve and relocate the complete package without rewriting it |
