---
name: kanban-agent-pipelines
description: Map the portable QA-first role pipeline and learning-review lifecycle to a selected task runtime, with explicit main-session coordination where automation is absent.
---
# Portable Agent Pipelines

The skill name is retained for existing links; Kanban and Hermes are not prerequisites.
Canonical role contracts live in `agents/<role>/AGENT.md`. Architect and Judge skill copies must match
those definitions. Apply the consuming project's conventions. Model identifiers in definitions are
routing preferences to map and verify when a runtime is chosen, not installation requirements now.

Read `../agent-self-learning/SKILL.md` for feedback, failed-attempt recovery, review termination,
retention, repository changes and evaluation. Read `../architect/SKILL.md` for coordinator/gate modes
and `../judge/SKILL.md` for delivery/learning modes. No runtime deployment is part of tightening these docs.

## Roles and order

Architect (main session) owns user communication, infrastructure, runtime mapping and final acceptance.
Planning creates self-contained tasks and documentation updates. QA authors the requirement-derived
feature scenarios, executable acceptance tests and fixtures before new implementation changes.
Developer writes independent unit tests first, confirms expected failure, implements and reruns.
Integration reruns both suites for every implementation, including single-module work. Add cross-module
scenarios only when modules interact. A fresh Architect gate reviews the diff and reruns tests.
Judge arbitrates delivery disputes or reviews learning in an explicitly selected mode.
Read-and-Summarize provides cited extraction when needed, not a mandatory implementation stage.

Initial dependencies: QA → Developer → Integration → fresh Architect gate → main-session decision.
Developer repairs implementation defects; QA repairs contract defects. Judge resolves disputed ownership.
After any repair, arrange new execution evidence before the gate. Do not blindly replay completed work
or use a prior passing result after the workspace changes. Trivial direct work may bypass the full DAG.

Canonical-workspace execution is serial under sole claims; no parallel writes or Integration merge
responsibility. Claims, dependency release and failed-task states must be mapped to actual runtime
capabilities. Workers report durable handoffs rather than requiring live peer chat. Only the main-session
Architect provisions or tears down infrastructure; keep it available through repair and final verification.

## Explicit coordination and learning

Architect ensures one independent learning review per eligible attempt; Planning may pre-create it.
Eligible roles/modes and the learning-review exemption are defined in the shared self-learning skill.
Learning-review attempts and retries do not create another learning review. Judge delivery attempts do.
Use stable task and attempt IDs to deduplicate scheduling. Completion never implies automatic review
creation. Record pending transitions and owners; if automation is unavailable, Architect routes them.

Failed, blocked and interrupted attempts also require review coverage. Architect assembles missing
feedback from preserved run evidence and routes learning independently of success-only dependencies.
Keep the source task's delivery state intact. A learning verdict cannot release a delivery gate.
A learning review may proceed after a terminal attempt without delaying unrelated delivery work;
its pending state remains visible. Repeated blockers are escalated, not hidden in the learning backlog.

## Readiness and migration checklist

Before claiming runtime readiness, Architect records evidence for:

1. Selected runtime, durable record/evidence store and which transitions require main-session action.
   If none is selected, record `runtime pending`; repository validation is still available.
2. Canonical role versions and copies actually loaded; explicit mode and model mapping for each role.
   Install required `agent-self-learning` content for all roles and `knowledge-handoff-summary` for
   Read-and-Summarize, using the target's supported loading mechanism.
3. Task dependencies, serial workspace ownership, isolated gate and learning contexts, and repair flow.
4. One review mapping per eligible attempt, including failed attempts; learning-review exemption;
   Architect ownership of missing feedback, scheduling and evidence preservation.
5. Verified task/run evidence for scheduling, failure recovery and durable handoff retrieval. A state
   label alone is insufficient. Do not invent an API or claim that prose enforces these transitions.

Migration preserves task bodies, dependency links, attempt IDs, definition versions, feedback, run
artifacts, rulings and original/replacement ID mappings. Verify copied evidence remains readable before
removing its source. If preservation is unsupported, retain the original and report the limitation.

## Verification

Run `just test-agent-contracts` in this repository. The tests cover document consistency and validator
behavior, not runtime readiness or whether a proposed behavioral change improves agents.

For an exported layout `<role>/skills/**/SKILL.md`, run the declared recipe:
`just validate-role-snapshot /absolute/export/root`. It requires PyYAML and checks exact role names,
non-empty metadata/body, duplicates of required skills and role dependencies. It does not verify skill
activation, model availability or current deployed content. Other layouts need a separately verified
adapter; no live runtime is assumed or modified.

The historical Hermes-specific adapter remains in `../onboard-hermes/SKILL.md`. Load it only if Hermes
is explicitly selected; its old infrastructure assumptions are not portable requirements.
