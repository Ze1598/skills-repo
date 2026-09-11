---
name: agent-self-learning
description: Collect cited dispatch feedback, route independent learning reviews, and evaluate proposed changes to repository agent definitions across runtimes.
---
# Agent Self-Learning

This is a portable contract. A card means a durable task record, not a particular product API.
The main-session Architect owns coordination. No board, automatic dispatcher, profile installation,
or active runtime is assumed. While migrating, keep records in a user-selected durable store;
repository role edits and static checks can proceed without deploying anything.

## Eligibility and termination

Every dispatched Planning, QA, Developer, Integration, Read-and-Summarize, Architect gate, and
Judge delivery attempt supplies feedback, whether successful, failed, blocked, or interrupted.
Learning-review attempts are exempt from feedback-triggered learning reviews, including their retries.
This terminates the chain. A learning-review failure goes to Architect for repair or escalation,
not to an automatically generated Judge-of-Judge. The main orchestration session is the coordinator,
not an additional dispatched worker. Two occurrences of the same failure mechanism require escalation.

## Worker feedback

Keep normal task results and test evidence. Append observations in exactly these buckets:
`As expected`, `Unexpected -> positive`, `Unexpected -> negative`. Use an empty list when there is
nothing to report. Workers do not propose role rules or learning verdicts.

Each observation cites a path and line with source version, preserved command output, or durable
record/run ID. Tier A is verbatim evidence; tier B is a cited interpretation; tier C is an explicit
hypothesis, excluded from change justification until verified. Do not fabricate a citation for a guess.
Read-and-Summarize keeps its normal tiered extraction and adds this separate feedback section.

The durable handoff includes:

- `attempt_id`, task ID, role and mode; distinguish retries from distinct tasks;
- `definition_version`: repository revision plus content hash when dirty, and deployed hash if applicable;
- terminal status and normal deliverable/test evidence;
- `feedback_origin`: `worker` or `coordinator`;
- `missing_worker_feedback`: boolean, with reason when true;
- the three feedback buckets and preserved evidence references;
- `review_id`: pending until Architect links a separate learning-review record.

## Coordination and failed attempts

Architect ensures one learning-review record per eligible `attempt_id`; retries of scheduling reuse
that identity. Planning may pre-create records, but Architect checks coverage after every terminal
attempt. Completion does not itself create a review. Use only transitions verified for the selected
runtime; if automation is unavailable, the main session records and routes the work explicitly.
Pending learning reviews remain visible and do not silently approve or block delivery.

For crashes, budget exhaustion, cancellation, or blocked work without a worker handoff, Architect
assembles a cited failure handoff from available logs and run evidence. Set `feedback_origin` to
`coordinator` and `missing_worker_feedback` to true. Preserve unknowns rather than inventing worker
observations. Route Judge independently of the failed task's success dependencies.
Never mark failed work complete to release a learning review. Keep delivery status unchanged.
If evidence is unavailable, record that gap and let Judge reject unsupported learning changes.

## Independent review

Use a separate Judge in learning mode. Provide the current handoff, affected repository definition and
version, and a cited bundle of relevant earlier attempts and decisions. Architect supplies this history
from the durable store; a single parent handoff or reviewer memory is not an aggregation mechanism.
Judge reads summaries and pulls targeted evidence. Repeated runs of one unchanged failing attempt
must not be presented as independent proof of generality; identify the recurring mechanism and context.

Judge follows `agents/judge/AGENT.md`: `adopt` recommends a concrete change, `revise` proposes a revised
candidate, `reject` makes no change (including insufficient evidence). A single observation is a data
point, not sufficient evidence of a recurring pattern. Learning decisions never approve delivery.

## Canonical changes and evaluation

`agents/<role>/AGENT.md` in this repository is authoritative. Judge proposes a repository diff;
Architect decides to accept, reject, or defer it and records the decision. Architect applies accepted
changes to the repository and synchronizes duplicated role skills in the same edit. Never stage or
commit automatically. Installed copies are derived artifacts: synchronize them only when an active
runtime and deployment authorization exist. Otherwise record deployment as pending or not applicable.
Record definition hashes on later dispatches so feedback can be attributed to the version actually used.

Each proposal records cited recurring evidence, intended behavioral change, `regression_check`, and
`evaluation_criterion` (observable measure, comparison baseline, evaluation window/sample and owner).
Write a failing deterministic regression check before changing a testable defect; run it after the fix.
Static tests establish contract consistency, not agent behavior. For behavioral proposals without a
meaningful deterministic check, record that limitation and the controlled evaluation required.

Architect records `evaluation_status`: `pending`, `improved`, `no_improvement`, `regressed`, or
`insufficient_evidence`, separately from adoption and deployment. After the declared window, an
independent Judge evaluates cited outcomes against the baseline. Until a runtime is selected, behavioral
evaluation remains pending. Architect reverts or revises accepted changes that fail the criterion,
recording the reason and new version; no automatic deployment or rollback is implied.

## Evidence retention

Before deleting a superseded record, Architect copies its relevant feedback, run evidence, rulings,
and source versions into a durable replacement and verifies that referenced evidence remains readable.
A pointer to a soon-to-be-deleted record is not preservation. If the store cannot preserve the evidence,
retain the original, mark it superseded where supported, and report the limitation. Preserve the mapping
between original and replacement IDs. This rule also applies during migration between tools.
