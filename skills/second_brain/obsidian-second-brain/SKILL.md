---
name: obsidian-second-brain
description: Operating manual for the global Obsidian Brain memory layer — read/write the vault, follow ROUTING, honor ownership.
---

# Obsidian Second Brain — Operating Manual

Use when interacting with the global Obsidian memory layer. This is the per-vault contract for the
agent: how to read and write `Brain/`, follow `ROUTING.md`, and respect the hard ownership boundary.

Read the canonical design in the repo-root `SECOND_BRAIN.md` for the full system. This skill is the
hands-on operating manual; `brain-signals`, `brain-dream`, and `brain-digest` carry their own scoped
procedures.

## Vault path

Resolve the vault from `OBSIDIAN_VAULT_PATH` (set in `~/.hermes/.env`; fallback `~/Documents/Obsidian
Vault`). Use file tools with the resolved absolute path — never pass `$OBSIDIAN_VAULT_PATH` to file
tools; file tools don't expand shell vars.

## Ownership rule (non-negotiable)

- The agent writes **only under `Brain/`**.
- Never mutate `Daily/`, `Personal/`, or any other owner folder in the vault.
- The agent may *read* owner folders only for `@markers` listed in `_brain.yaml` `notes.read_paths`.

## Session start

At the start of any session that interacts with the vault:

1. Read `Brain/_BRAIN.md` (this per-vault operating manual).
2. Read `Brain/ROUTING.md` (the topic→note map the hot memory points to).
3. Pull only the referenced note(s) you need on demand — never load the whole vault.

## Reading on demand

Follow `ROUTING.md`: a topic → a `[[wikilink]]` → locate the note and read only what you need. Keep
context lean; the map is the index, specific notes are the detail.

## Writing

- **Signals and evidence** → append to `Brain/log/<today>.md` (or `Brain/inbox/`) using the exact
  line formats in the `brain-signals` skill.
- **Reference notes** → `Brain/ref/<domain>.md`, one topic per note, `[[wikilink]]`ed from
  `ROUTING.md`.
- **Never hand-edit preference `status`/`confidence`** — only the `brain-dream` pass sets those.

## When to load the companion skills

- Logging a signal or evidence → `brain-signals`.
- Consolidation / promotion / retirement → `brain-dream`.
- Nightly digest / review cron → `brain-digest`.

## Verification

A write is correct when: it's under `Brain/`, every signal line carries a `ref:` citation, and no
preference `status` was hand-edited.