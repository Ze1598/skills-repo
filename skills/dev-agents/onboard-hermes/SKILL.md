---
name: onboard-hermes
description: Use when starting a new project with the five-role QA-first dev pipeline, or onboarding Hermes into an existing repo. Invoke as /onboard-hermes. Sets up per-project boards and routes tasks through the QA→Developer→Integration DAG with an Architect cold-gate.
model: (architect default)
tools: hermes kanban board/CLI + skill roster
---
# Kanban Development Pipeline — 5-Role QA-First Workflow

Invoke as **`/onboard-hermes`** (dynamic skill command, desktop + CLI + messaging) — or describe the
intent in natural language and this skill auto-loads. Executes the runbook in
`references/onboarding.md`: sets up the per-project board and routes substantial work through the
QA→Developer→Integration DAG with an Architect cold-gate.

Operating contract for the standing multi-agent development system. Every role is a global Hermes
profile (independent memory/model under provider nous) and a role skill. Every project gets its own
Kanban board. The pipeline is durable, serial, and runs with NO live parallel spokes — the board's
dispatcher + parent-link engine enforce order across restarts.

## Roles → profiles (provider nous routing, models pinned per profile)

| Role | Profile | Model | Does |
|---|---|---|---|
| Architect | (main chat session — `architect` gate skill) | openai/gpt-6-astra-flex | Talks to user, judges pipeline-vs-direct, owns README + ALL infra lifecycle, cold final-gate review |
| Planning | `planning` | openai/gpt-6-astra-flex | Tech-lead: breaks requirement into task DAG, creates cards, applies doc edits |
| QA | `qa` | qwen/qwen3.8-flash | CONTRACT AUTHOR: .feature + programmatic tests + mock datasets, authored first, before any code |
| Developer | `developer` | qwen/qwen3.8-flash | Implements from requirement (never from QA's tests) + own unit tests |
| Integration | `integration` | qwen/qwen3.8-flash | EXECUTES QA-authored integration tests against built code. Multi-module projects only |

## Order (source of truth — non-negotiable)

QA first, from the requirement alone. Then Developer implements from the REQUIREMENT, not QA's tests
(anti-overfit: code and tests both derive from the requirement, never each other). Integration
executes QA's authored integrations once Developer unit tests pass. Failure routes back to Developer
via review loop. Architect cold-gate reviews the final diff.

```
Architect → requirement (authoritative)
  QA card A        : authors .feature contract + programmatic tests + mock datasets   (no code yet)
  Developer card B : child-of-A(L), implements + unit tests from requirement           (anti-overfit)
  Integration C    : child-of-B, ONLY if multi-module; executes QA's authored tests against code
  review loop      : red/red mismatch → back to Developer via request_changes → re-implement
  Architect gate   : cold review of diff vs requirement + repo conventions
  user
```

QA does NOT execute its own integration tests at authoring (code absent). Integration is executor,
never re-author. Developer unit tests are code-internal and Developer runs them itself.

## Onboarding (trigger for this role)
When the user says *start a new project with the pipeline* or *onboard the pipeline into <repo>*, the
Architect role executes `references/onboarding.md` end-to-end — create the board, write the repo's
CLAUDE.md/AGENTS.md context layer, sanity-check routing, and report ready. Skip the pipeline for
trivial/direct fixes.

## Review loop mechanics (native)
Developer/QA use `kanban_request_review` / `kanban_request_changes(reason)` so the card returns to
its implementer for fixes automatically (no block-loop accounting). Approve via `kanban_complete`.
Workers are isolated peers; every handoff is a durable row (summary/metadata/comments) the next
worker reads. No live agent-to-agent chat, no manual spawning.

## Cost model (user's)
Expensive-reliable (openai/gpt-6-astra-flex) for Architect + Planning (planning / long-term
stability); cheap-reliable (qwen/qwen3.8-flash) for Developer/QA/Integration execution INCLUDING
their review passes. One economic note: QA/Integration review passes are Qwen — acceptable per user
decision; the Architect cold gate (GPT-6) is the quality tripwire for architecture gaps.

## Infrastructure
Architect-exclusively, both modes, never Planning/Developer/QA/Integration. Provision before routing.
If a worker hits a real infra gap it surfaces in its summary/comment; Architect (not the finder)
brings it up / tears down only when the task is fully done.

## Pitfalls / invariants
- Integration card is NOT created for single-module projects.
- Never parallelize dependent pieces; only genuinely independent sub-requirements may fan out.
- Two workers never edit the canonical repo concurrently — serialize code/doc-writes via sole-claim
  cards; genuine parallel QA/Dev work uses isolated worktree branches, merged sequentially at
  Integration (not a shared concurrent tree).
- Role skills are repo-agnostic; don't let one project's CLAUDE.md specifics leak into the global
  role files.

Verification: board has the DAG cards with correct parent links; `hermes kanban dispatch --dry-run`
shows QA claiming first; per-profile model columns (architect/planning=gpt-6-astra-flex,
qa/dev/integration=qwen) confirmed via `hermes profile list`.
