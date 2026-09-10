---
name: brain-digest
description: Periodic review surface for the Obsidian Brain — the nightly dream+digest cron, how output reaches the owner, and how to read it.
---

# Brain Digest — Periodic Review

Use when the nightly Brain consolidation runs, when wiring/reviewing the digest cron, or when reading a
digest to decide what the owner should act on. This is the automated "periodic review point" of the
second brain.

Siblings: `obsidian-second-brain` (operating manual), `brain-signals` (capture),
`brain-dream` (consolidation).

## The cron job

Registered as `brain-digest-nightly`:

```bash
hermes cron create '0 3 * * *' --name brain-digest-nightly \
  --deliver local --no-agent --script brain-digest.sh
```

- **Schedule:** nightly 03:00.
- **Script:** `~/.hermes/scripts/brain-digest.sh` — runs the dream pass (consolidate), then renders
  the digest for the trailing window.
- **Delivery:** `local` (into the chat). `--no-agent --script` = no LLM; stdout delivered verbatim.
- **Silent when quiet:** the script is invoked with `--silent-if-empty`, which exits `2` with empty
  stdout when nothing changed → Hermes posts nothing.

Wrapper (`~/.hermes/scripts/brain-digest.sh`) is a thin shell that calls the dream skill's script:

```bash
#!/usr/bin/env bash
set -euo pipefail
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/obsidian}"
DREAM_PY="$HOME/Documents/projects/kurothos-deckbuilder/tools/brain_dream.py"
"$DREAM_PY" "$VAULT" >/dev/null 2>&1 || true
exec "$DREAM_PY" "$VAULT" --digest --silent-if-empty
```

(When the dream script lives with the `brain-dream` skill, point `DREAM_PY` at that copy so the digest
is not tied to any single project.)

## The digest output

```
# Brain digest — <date>

- new-unconfirmed: <slug> (topic=<topic>, N signals)
- confirmed: <slug> (first apply)
- quarantine: <slug> (violations>=applied, low base)
- recovered: <slug> -> confirmed
- retired: <slug> (stale-no-evidence / expired-unconfirmed / rebutted / quarantine-violated)
- confidence-shift: <slug> -> high (applied N, violated N)
```

## Reading it as the owner/reviewer

- **New unconfirmed** — rules in a 14-day trial; glance at the cited signals, decide whether to keep
  or reject (`user_rejected`).
- **Confirmed** — a rule now shapes behavior; worth a quick sanity check.
- **Retired** — memory freed; check for any that shouldn't have been.
- **Confidence shifts** — rising/falling confidence on a rule you care about.

The digest is opt-in automation: it reports changes; the owner decides what to act on.

## Prerequisite

The gateway must be running for cron to fire. When it's down, run the digest ad-hoc with
`python3 <dream-skill>/scripts/brain_dream.py <vault> --digest`.

## Verification

`hermes cron list` shows the job; `hermes cron run brain-digest-nightly` does a one-shot dry run and
prints the digest to confirm it's wired before you trust it to fire.