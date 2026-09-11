# Legacy Hermes Adapter Checklist

Use only after the user selects Hermes. No running Hermes service or installed profile is assumed.
First load `../../kanban-agent-pipelines/SKILL.md` and `../../agent-self-learning/SKILL.md` for the
portable source-of-truth workflow. The main-session Architect owns this adapter's decisions.

1. Confirm the selected repository, Hermes installation/version and supported tools. Preserve existing
   project context. Establish a durable evidence location and verify actual lifecycle APIs before use.
2. Map canonical repository roles into isolated profiles and load their current role content plus
   `agent-self-learning`; Read-and-Summarize also needs `knowledge-handoff-summary`. Resolve model
   preferences against the installation's real catalog. Do not assume cloning loads the correct role.
3. Map durable task records, parent dependencies, same-card reviews where supported, and isolated
   Architect gate/Judge learning tasks. Verify how failed or blocked attempts can be reviewed without
   falsely completing them. If unsupported, Architect records and routes those transitions explicitly.
4. Check review coverage for every eligible attempt, the exemption for learning-review attempts and
   retries, stable deduplication IDs, and Architect ownership of missing feedback. A success-only child
   dependency is insufficient for failure review. Learning verdicts never approve delivery.
5. Check actual scheduler/worker and recovery evidence. Historical deployments used an embedded gateway
   dispatcher and an observation-only launchd sentinel; verify whether this installation has them.
   If present, keep mutation/reclaim/spawn ownership in the dispatcher. An observer must not become a
   competing scheduler. If absent, do not install or assume them as a prerequisite to repository work.
6. Validate exported profile contents with `just validate-role-snapshot /absolute/profiles/root` in the
   skills repository, then verify actual skill activation and model routing separately in the runtime.
   The validator also accepts an explicitly set `HERMES_HOME` for legacy callers; it never defaults to
   a user's home directory. Run `just test-agent-contracts` for repository consistency.
7. Before reporting ready, verify readable durable handoffs, source definition versions, QA→Developer→
   Integration→fresh gate dependencies, repair verification, failed-attempt review and the termination
   exemption. Record all manual coordination still required. No result from static checks proves this.

For migration away, preserve source records and artifacts until the replacement evidence is verified.
Record original/replacement IDs and do not assume a mirror or status export contains full run history.
Do not delete superseded evidence merely to tidy a board. No commit, deployment, or service change is
implied by running this checklist.
