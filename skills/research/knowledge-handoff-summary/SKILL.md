---
name: knowledge-handoff-summary
description: Use when a cheap subagent hands findings to a senior agent.
---

# Knowledge Handoff Summary

Produce bullet-point summaries that let an expensive downstream agent consume your findings **without re-reading the source**. The summary is a locator index + embedded ground truth, not a lossy paraphrase. Applies to ANY source material — code, documents, prose, a light novel, transcripts, data, logs — wherever a cheap reader must feed a senior agent.

## The three trust tiers (memorize this)

Every line of your summary is exactly one of three kinds:

| Tier | Content | Downstream treatment |
|---|---|---|
| **A. Ground truth** | Exact values, sample data, verbatim quotes, names, numbers, signatures, line/section/page numbers, API responses, test output | Trusted as-is, verbatim. Never paraphrase — paste the real bytes. |
| **B. Cited claim** | An observation/interpretation **with** a citation (see citation schemes below) | Trusted; traceable cheaply if ever needed. |
| **C. Hypothesis** | A guess, suspicion, or uncertainty **without** a reliable citation | Flagged as a HYPOTHESIS — explicitly the senior agent's job to investigate. NOT an error, NOT something to bury. |

## Citation schemes (use the one that fits the source)

- **Code / structured files:** `path:line` or `path:start-end`
- **Prose / books / novels:** `chapter:section` or `chapter:page` (e.g. `ch3:12`), plus file path when the text is digital
- **Transcripts / audio / video:** `source + HH:MM:SS` timestamp
- **Documents / reports:** `path + section heading` or page number

## Rules

1. **Always cite.** Any claim carries a citation from the matching scheme. No bare "the file does X" or "the chapter reveals X" — always tie it to a locator.
2. **Verbatim over paraphrase for data.** Exact strings, numbers, names, quotes, signatures pass through untouched. Never summarize a literal or a key passage.
3. **Never invent citations.** A citation you didn't actually verify is worse than no citation — it corrupts tier B. If you didn't see it, put the thought in tier C.
4. **Surface hypotheses explicitly.** Mark them clearly (e.g. `HYPOTHESIS: ...`) so the senior agent sees at a glance where to spend attention. Do not hedge them into weak claims.
5. **No blind-scan dumping.** Don't dump large blocks of source into the summary. For anything big, give the citation and a one-line description of what's there — the consumer pulls depth on demand.
6. **One subject per bullet.** Each bullet = one fact, claim, or hypothesis. No run-ons.

## Template

```markdown
## Summary — <source/area>

### Ground truth
- <citation> — exact <value/quote/signature> verbatim
- ...

### Cited claims
- <observation> — citation
- <observation> — citation

### Hypotheses (needs investigation)
- HYPOTHESIS: <guess/suspicion> — related region <citation> (if known)
- HYPOTHESIS: <uncertainty without citation>
```

## Consumed by
Delegated cheap subagents producing findings for a main-session planner/architect. The senior agent reads ONLY the summary (tiers A+B) and pulls targeted depth at cited locations; tier C items are its investigation queue. Main session context grows only by the summary's tokens.