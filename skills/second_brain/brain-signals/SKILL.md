---
name: brain-signals
description: Capture discipline for the Obsidian Brain — exact signal and apply/violate evidence line formats, and the data-never-rules rule.
---

# Brain Signals — Capture Discipline

Use when logging a signal or apply/violate evidence into the Obsidian Brain. This is the discipline
that keeps raw memory input clean and machine-parseable for the `brain-dream` pass.

## Core rule: a signal is DATA, never a proposed rule

The agent records observations; the deterministic `brain-dream` pass decides whether a pattern becomes
a preference. Do NOT phrase a signal as a rule, verdict, or instruction to future sessions. Record
*what happened* and *why it mattered* — cited.

## Signal format

Append to `Brain/log/<today>.md` (or drop a `sig-<date>-<slug>.md` in `Brain/inbox/` for uncategorized
signals). Exact line:

```
- <date> <time> | topic: <slug> | kind: <kind> | <one line> | ref: <citation>
```

`kind` is one of:
- `expected` — went as planned; outcome matched the plan. Confirms existing behavior; the dream pass
  creates no rule from it.
- `unexpected-positive` — a divergence that produced a good result (worth learning what caused it).
- `unexpected-negative` — a divergence with a bad result, e.g. the complexity delta between planning
  and build was too large, the scope was too big for the task/budget, an earlier card left tech debt,
  an estimate was wrong, an owned-path assumption broke.

`topic` is a stable lowercase-hyphen slug (`agent-timeout`, `ui-bug`, `comm-style`). `ref` is a
citation: `path:line`, card id, conversation, or diff.

Example:
```
- 2026-09-10 14:00 | topic: agent-timeout | kind: unexpected-negative | combat dev card timed out at 150/150 after authoring on disk | ref: t_b8654585
```

## Apply / violate evidence

When you act on (or against) a preference during real work, log evidence so confidence can move:

```
- <date> <time> | pref: pref-<slug> | apply   | <what you did> | ref: <...>
- <date> <time> | pref: pref-<slug> | violate | <what happened> | ref: <...>
```

- `apply` raises confidence; `violate` lowers it and can quarantine/retire the rule.
- Only log evidence for a preference that actually exists (`pref-<slug>.md`).

## Rules

1. **Always cite.** No bare observations.
2. **One topic per line** (stable slug). No run-ons.
3. **No proposed rules.** Let the dream pass aggregate; you only supply data.
4. **As-expected signals** are still worth logging (they confirm current behavior) but create no rule.

## Verification

A capture is correct when: it's under `Brain/`, the line matches the exact format, it has a `ref:`,
and it states an observation — not a rule.