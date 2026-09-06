---
name: hermes-role-profile
description: Use when creating or editing a Hermes role profile.
---

# Hermes Role Profile

Stand up or modify a persistent install-wide role profile in Hermes (e.g. architect, planning, developer, qa, integration, read-and-summarize). These are GLOBAL profiles reusable across all projects, each 'consumed when starting a new project'. A profile is a directory under `~/.hermes/profiles/<name>/` that Hermes discovers automatically — there is no registry to register in.

## When to Use

- User asks to add a new persistent role/agent profile (the workflow in the migration project's 6-role setup)
- Editing an existing role's persona, model, or installed skills
- Verifying a profile is recognized and runnable
- Do NOT use for: one-shot delegation (`delegate_task`), authoring an in-repo skill, or ad-hoc agent spawns

## Profile anatomy (a directory, auto-discovered)

```
~/.hermes/profiles/<name>/
├── profile.yaml                 # description (one line, the role summary)
├── config.yaml                  # model pinning + full settings
├── SOUL.md                      # persona body (house style below)
├── memories/
│   ├── MEMORY.md                # environment + standing rules
│   └── USER.md                  # who the user is + role roster
└── skills/                      # skills installed into this profile
    └── <skill>/SKILL.md
```

## Procedure

1. **Determine the model** by role cost: expensive/long-term-planning roles (architect, planning) use `openai/gpt-6-astra-flex`; cheap-execution roles (developer, qa, integration, read-and-summarize) use `qwen/qwen3.8-flash`. Provider is `nous`. Live-confirm routing strings before trusting them.
2. **Create the dir tree:** `mkdir -p ~/.hermes/profiles/<name>/memories ~/.hermes/profiles/<name>/skills`.
3. **Reuse a sibling's config for the model.** Copy the config from an existing profile using the SAME model (e.g. `cp ~/.hermes/profiles/developer/config.yaml ~/.hermes/profiles/<name>/config.yaml` for a cheap role). Do not hand-rebuild 248 lines — the model pinning is `model.default` + `model.provider` at the top. Verify with `sed -n '1,7p'`. (Existing profiles all share the same config scaffold; only the model default differs.)
4. **Write `profile.yaml`** — `description:` one line summarizing the role + `description_auto: false`.
5. **Write `SOUL.md` persona** in the user's house style: a direct opening ("You are the <ROLE> agent — ..."), then **'Your job'** numbered steps, **'Absolute rules'** (no soft language), and **'report to the main-session agent, NOT the user directly'**. The cheap reader role: read in full, extract into tiers, never solve — only extract and report.
6. **Copy memories** from a sibling cheap profile (`cp .../developer/memories/*.md`), then update: the USER.md roster line ("These N role profiles ...") to the new count and add a one-line description of the new role.
7. **Install any skills** the role consumes into `~/.hermes/profiles/<name>/skills/<skill>/SKILL.md` (`cp -r` from the global `~/.hermes/skills/<category>/<skill>`).
8. **Register the alias:** `hermes profile alias <name>` creates `/Users/<user>/.local/bin/<name>` so the role runs as a command. (Sibling roles have aliases; a profile without one still runs via `hermes profile use`.)
9. **Verify:** `hermes profile list` — the new row must show the correct model. `hermes profile describe` to confirm the description.
10. **Mirror into memory:** update the default-profile USER.md roster to the new role count and description (this is what future sessions read).

## Pitfalls

- **`skill_manage` create enforces a 60-char description budget**, not the 1024 the validator may allow. Keep the description under ~59 chars, one sentence, trigger first, ends with a period. Trim words ('costly'/'senior' vs 'expensive') to fit — the system-prompt index truncates at 57 chars + '...'.
- **`skill_manage` delete must be the SOLE op in the operations array** — it does not compose with other ops' rollback. Delete first in one call, then create in another.
- **Never hand-edit a sibling profile's config to change its model** if a copy already matches — copy-and-paste from the same-model sibling avoids the 248-line rebuild and any YAML drift.
- **Default profile has no per-role memories** — the root `~/.hermes/` memories are the default profile's. A role profile gets its own `memories/`; update those, and mirror the roster change to the default (root) memory too.

## Verification

- `hermes profile list` shows the new profile with the intended model.
- `hermes profile alias <name>` succeeds and the binary exists.
- The role's SKILL.md is present under its profile `skills/` dir (if it consumes one).
- The default-profile USER.md roster line reflects the new role count + description.
