---
name: brain-dream
description: Deterministic consolidation pass for the Obsidian Brain — turn signal patterns into confirmed preferences via the lifecycle in _brain.yaml.
---

# Brain Dream — Deterministic Consolidation

Use when running or understanding the nightly consolidation that turns raw signals into confirmed
preferences. Pure compute — no LLM. Owns `scripts/brain_dream.py`.

This is one of four `second_brain` skills. Siblings: `obsidian-second-brain` (operating manual),
`brain-signals` (capture discipline), `brain-digest` (review surface).

## The script

```
scripts/brain_dream.py <vault> [--dry-run] [--window N]
scripts/brain_dream.py <vault> --digest [--since ISO] [--silent-if-empty]
```

Run it with the Python that has `yaml` available (the sys.executable Hermes uses, or `python3`).

## What it does (in order)

1. **Snapshot** the current `Brain/` (pre-dream backup under `Brain/.snapshots/`, pruned to
   `snapshot_keep`).
2. **Collect signals** within `same_sign_window_days`, grouped by `(topic, kind)`. Reads signal lines
   from `Brain/log/*.md` and `Brain/inbox/*.md`.
3. **Create unconfirmed preferences.** Any topic with ≥`candidate_threshold` same-sign signals
   (excluding `expected`) becomes `pref-<slug>.md`, status `unconfirmed`, trial `trial_days`. Signals
   move to `Brain/inbox/processed/`.
4. **Process evidence** for every existing pref (`apply`/`violate` lines in the logs) and apply the
   lifecycle from `_brain.yaml`.
5. **Update `ROUTING.md`** / manual status and leave a summary in `Brain/log/`.

## The lifecycle (from `_brain.yaml`)

```
Inbox → Unconfirmed(≥threshold) → Confirmed(first apply)
Unconfirmed → Retired(expired: no apply before unconfirmed_until)
Confirmed → Quarantine(violations ≥ applied, low base)
Quarantine → Confirmed(recover: applied > violated)
Confirmed/Quarantine → Retired(stale: no evidence for stale_evidence_days)
Confirmed → Retired(rebutted: violations ≥ rebuttal_threshold AND ≥ applied)
Confirmed → Retired(superseded: cited outdated)
Any → Retired(user_rejected: owner rejects)
```

`confidence = min(high, low + applied - violated)` from the `confidence` map.

## Config

All thresholds live in `Brain/_brain.yaml`. Defaults: `candidate_threshold=3`,
`same_sign_window_days=30`, `trial_days=14`, `unconfirmed_until_days=30`, `confirm_on_apply=true`,
`stale_evidence_days=90`, `rebuttal_threshold=2`, `low_max_applied=3`.

## Usage notes

- **Idempotent.** Re-running on an unchanged Brain is a no-op (no log entry, no new snapshot).
- **`--dry-run`** stages the run and prints what it *would* do without writing.
- **Digest** (`--digest`) renders a summary; `--silent-if-empty` exits `2` with empty stdout when
  nothing changed (for crons).

## Verification

Run `scripts/brain_dream.py <vault> --dry-run`, confirm the expected promotions/retirements are listed
(as opposed to unexpected ones), then run for real and confirm `pref-*.md` / `retired/ret-*.md` reflect
them and `ROUTING.md` updated.