# Flat Skill Migration

This directory is a staging area for skills that begin as standalone Markdown files. The migration process turns each flat source file into a complete skill package under `skills/`, using `mapper.yaml` to select its capability-domain location and the repository template to create the package structure.

Run every command in this guide from the repository root.

## Source format

Add one Markdown file per skill:

```text
migrate_prompts/
├── mapper.yaml
├── example-skill.md
└── another-skill.md
```

Use a lowercase, hyphenated filename. Its basename becomes the skill name:

```text
example-skill.md → example-skill
```

A source file may already be a complete skill with YAML frontmatter:

```markdown
---
name: example-skill
description: Explain what the skill does and when it should be used.
---

# Example Skill
```

It may also contain only the instruction body. During migration, add valid `name` and `description` frontmatter before that body. Preserve the original source content; do not rewrite the instructions as part of a storage migration.

## Mapper structure

`mapper.yaml` is a YAML sequence of one-entry mappings:

```yaml
- example-skill.md: capability-domain
- another-skill.md: capability-domain/subdomain
```

The key identifies a Markdown file in this directory. The `.md` suffix may be omitted, although including it consistently is preferred. The value is the destination parent path relative to `skills/`; it must not begin with `skills/` or `/`.

Resolve each entry as follows:

```text
source:        migrate_prompts/<source-name>.md
skill name:    <source-name without .md>
target parent: skills/<mapped-value>/
target skill:  skills/<mapped-value>/<skill-name>/
```

For example:

```yaml
- medium-custom.md: newsletter
- generate-character.md: image-generation/character-design
```

resolves to:

```text
skills/newsletter/medium-custom/
skills/image-generation/character-design/generate-character/
```

Before migration, verify that every mapped source exists, every destination uses lowercase letters, numbers, and hyphens, and no destination skill directory already exists.

## Create each skill package

Run the root `just` recipe once for every mapper entry. Pass the mapped parent followed by the skill name:

```bash
just add-skill newsletter/medium-custom
just add-skill image-generation/character-design/generate-character
```

The recipe copies `templates/skill/` into the target directory, initializes the `name` field in `SKILL.md`, and updates the `$skill-name` placeholder in `agents/openai.yaml`. It rejects invalid paths, traversal attempts, and existing destinations; it never overwrites an existing skill.

## Populate `SKILL.md`

After running the recipe, replace the generated `SKILL.md` placeholder with the corresponding source Markdown.

If the source already contains valid `name` and `description` frontmatter, copy it unchanged.

If the source is instruction-only, prepend:

```yaml
---
name: <skill-name>
description: <what the skill does and the requests or contexts that should trigger it>
---
```

Then append the complete source body without changing its instructions. The `name` must exactly match the final directory name.

## Update `agents/openai.yaml`

Replace all template placeholders with metadata derived from the completed skill:

```yaml
interface:
  display_name: "Human-Readable Skill Name"
  short_description: "A concise description between 25 and 64 characters"
  default_prompt: "Use $skill-name to perform a representative task."
```

Requirements:

- Use a readable title rather than the raw hyphenated directory name.
- Keep `short_description` between 25 and 64 characters.
- Make `default_prompt` a short, realistic invocation.
- Mention the exact skill as `$skill-name` in `default_prompt`.
- Add icons or other optional interface fields only when the corresponding assets exist.

## Remove unused resource directories

The template creates `assets/`, `references/`, and `scripts/`. Keep directories that receive real files. After all migrations are complete, remove only empty resource directories across the skill library:

```bash
find skills -type d \( -name assets -o -name references -o -name scripts \) -empty -delete
```

This command deletes directories only when they are empty. It does not remove populated resource directories or their contents.

## Validate the migration

For each created skill, run:

```bash
python3 /Users/josecosta/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<mapped-value>/<skill-name>
```

Also verify:

1. Every mapper entry produced exactly one target skill.
2. The target directory name matches the `SKILL.md` frontmatter name.
3. The original source body is present in the target `SKILL.md`.
4. `agents/openai.yaml` is valid YAML and contains no template placeholders.
5. No empty `assets/`, `references/`, or `scripts/` directories remain under `skills/`.
6. Existing skills were not overwritten or otherwise modified.

## Migration summary

The complete workflow is:

```text
flat Markdown source
    → mapper.yaml destination
    → just add-skill <destination>/<name>
    → replace generated SKILL.md
    → add frontmatter when missing
    → update agents/openai.yaml
    → validate the package
    → remove empty resource directories
```
