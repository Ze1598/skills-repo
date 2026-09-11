---
name: kanban-agent-pipelines
description: Stand up multi-agent role pipelines on Hermes Kanban.
---
# Multi-Agent Role Pipelines on Hermes Kanban

Turn markdown role definitions (Claude-Code-style: `name`/`description`/`tools`/`model` frontmatter +
persona body) into a global, reusable agent system where each role is a Hermes PROFILE + a role
SKILL, coordinated on a per-project Kanban board. Read the sibling skills `architect` and
`onboard-hermes` (user-owned, in this same category) for the concrete five-role QA-first
contract this user runs; this skill carries the generic standup PROCEDURE and pitfall set.

## Mental model — one Claude agent = THREE Hermes objects

| Claude-Code concept | Hermes object | Global or per-repo |
|---|---|---|
| agent definition (.md) | role skill (`SKILL.md` under `~/.hermes/profiles/<role>/skills/...`) | global, repo-agnostic |
| agent identity | profile (`hermes profile create`) | global |
| spawn + coordination | Kanban board + dispatcher | per project (one board per repo) |
| per-repo rules | project CLAUDE.md/AGENTS.md | per repo only |

Never bake a repo's governance (git-state prohibition, `just`-recipe layer, repo-specific env fixes)
into a GLOBAL role skill — it misfires in unrelated projects. Global roles say only "apply the
project's declared command layer / conventions"; per-repo rules load from the project context file at
project start.

## Role roster

The standard pipeline includes Architect, Judge, Planning, QA, Developer, Integration, and
Read-and-Summarize. Judge is a separate `judge` profile using `openai/gpt-5.6-luna-pro`; it handles
independent failure/review rulings and does not replace the Architect's final gate.

## When to Use
- Standing up named agent roles for a new project (or porting Claude-Code subagents into Hermes).
- Routing a substantial task through a QA-first Developer/QA/Integration pipeline.
- Choosing between Kanban (durable, persistent-role, survives restarts) vs `delegate_task` (one-shot,
  in-context, non-durable). Use Kanban when work crosses agent boundaries, needs restart survival,
  may need human input, or must be re-discoverable after the fact; `delegate_task` for short
  reasoning answers returned to the parent before continuing.
- Don't use: single-episode admin/triage, or work that lives and dies in one session.

## Procedure

1. Create each role as a profile CLONED from the working default so it inherits provider OAuth + the
   inference URL — do not create empty and re-wire auth:
   ```
   hermes profile create '<role>' --clone --description '<one-line routing desc>'
   ```
   Set the description: the kanban decomposer routes cards by it; it ships empty otherwise.
2. Pin the per-profile model — `--clone` copies default's model, so a cloned worker is on the wrong
   model until pinned:
   ```
   hermes -p '<role>' config set model '<provider-slug>/<model-slug>'
   ```
   NEVER invent routing ids. Query the live catalog and grep for the exact slug before pinning:
   `curl -s https://inference-api.nousresearch.com/v1/models`. Naming is `provider/model-version`
   (`openai/gpt-6-astra-flex`, `qwen/qwen3.8-flash`, `deepseek/deepseek-v4-flash-0731`).
3. Write each role SKILL.md into THAT role's profile skills dir so a spawned worker auto-loads it:
   `~/.hermes/profiles/<role>/skills/<category>/role/SKILL.md`. Keep `name`+`description` present;
   extra frontmatter keys (`model:`, `tools:`) and long descriptions are tolerated by the loader.
4. Orchestration recipe + the Architect/gate persona live in the DEFAULT (main-chat) profile's skills;
   Architect is the main-session persona consumed at project start, not a spawned worker.
5. Create a board per project with the canonical repo as default workdir:
   `hermes kanban boards create <slug> --default-workdir <abs-canonical-repo>`.
6. Create the task DAG with parent links so the dispatcher enforces ordering across restarts; verify
   with `hermes kanban dispatch --dry-run` and `hermes -p <role> skills list` (role skill `enabled`).

## Worker spawn reality (verify against the install; do not design around conversational spawning)
- A worker is a subprocess `hermes -p <assignee> --cli chat -q "work kanban task <id>"`. The `-p`
  sets a profile-scoped `HERMES_HOME`; the worker loads THAT profile's model/.env/memory/skills.
- `kanban_*` tools auto-enable because the spawn sets `HERMES_KANBAN_TASK`; workers call the tools,
  never shell out to `hermes kanban`.
- Workers are isolated peers: no live agent-to-agent chat, no supervising model that "spawns"
  siblings and shuttles messages. That is the Claude subagent model and a worker does not have it.
  Handoff is durable rows (summary/metadata/comments) the next worker reads as `worker_context`.
- Sequence is enforced by the parent-link engine, not by a model orchestrator; a worker that must
  "speak first" is realized by making its card the parent of the dependent card.

## QA-first TDD topology (the anti-overfit pattern this user runs)
- QA authors the acceptance contract (.feature + programmatic tests + mock datasets) BEFORE code
  exists. Developer then implements from the REQUIREMENT, never from QA's tests. Integration
  EXECUTES QA-authored tests once Developer unit tests pass. Failures return to the Developer card
  via `request_changes(reason)`; approve via `kanban_complete`. QA-authored tests sit dormant
  (un-runnable, not failing) until the code exists.
- Cards: QA on `dir:<canonical-repo>`, Developer `--parent <qa-id> --body 'from REQUIREMENT only'`,
  Integration `--parent <dev-id>` ONLY if modules genuinely interact. Single-module projects skip the
  Integration card.
- `dir:<path>` is preserved across completion; `scratch` is DELETED on completion (files vanish unless
  declared via `kanban_complete(artifacts=)`). Never design concurrent multi-worker writes to one
  shared tree to reconcile later — the system atomically claims one task at a time; serialize.

## Durable supervision and handoff
The gateway's embedded dispatcher is the sole owner of promotion, claiming, reclaim, spawning, and
failure-limit auto-blocking. A separate launchd-carried sentinel is observation-only: it reads each
running card's log and exact worker process, alerts on dead workers/provider-fatal output/blocked cards,
and may stop the exact provider-fatal worker. It must never dispatch, reclaim, complete, or mutate card
state. Do not substitute chat-session polling for either service.

Before reporting a live pipeline, verify all four independent signals: launchd state for the sentinel,
launchd state for the gateway, a worker PID matching a running card, and a gateway dispatcher log entry.
A running card without a matching worker is stale, not progress. If the chat is interrupted, the
external services remain the source of truth and must be read back after reconnection.

The board is durable SQLite, not the mirror file. For board `kurothos-deckbuilder`, the canonical
store is `~/.hermes/kanban/boards/kurothos-deckbuilder/kanban.db`; adjacent `board.json` contains
board metadata. `~/.hermes/kanban/mirror-*.json` is only a projection.

## Verification
Run `scripts/validate-role-setup.py` (roles as args, default = this user's five) to check every
role profile has a well-formed SKILL.md (delimiters, non-empty body, YAML name+description). Confirm
model routing with `hermes profile list` and per-role enablement with
`hermes -p <role> skills list | grep enabled`. For a live pipeline, also verify the four supervision
signals above and run the sentinel's deterministic tests, including dead-worker, provider-fatal, and
blocked-card cases.

## Pitfalls
- Malformed skill frontmatter on a role skill stalls the queue at spawn (loader errors on the card's
  first worker). Validate each new SKILL.md: starts `---`, YAML parses with `name`+`description`,
  closes `\n---`, non-empty body (script: `scripts/validate-role-setup.py`).
- `--clone` leaves every new profile on the DEFAULT model until you `config set` per profile; the
  model column in `hermes profile list` is the route-verify point.
- Bolting expensive-planner/cheap-executor to a pipeline means the expensive model re-runs on every
  planner card attempt and retry round — budget per-attempt, not per-call.
- QA/Integration review passes on the cheap executor model is a blind spot; per-card `-m/--provider`
  override exists independent of the assignee profile, so a review card can run a stronger model
  without changing the pipeline DAG.
- Review-gate independence: to stop an actor grading its own work, give the reviewer a fresh card /
  distinct profile; a reviewer card's context is built only from the work's handoff + diff (not the
  reviewer's accumulated memory).
