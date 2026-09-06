# Handing a long-lived project across sessions

Reusable for any large, multi-session build (icon/asset packs or long agent-led repos) where the agent restarts and must not re-derive or silently contradict prior work.

## Why this breaks silently

A documentation file is only as authoritative as the last session that used it. As later sessions edit assets and move folders, a single source of truth decays unless each session reconciles it against disk and git. New agents trust ROADMAP-style docs, so a stale count, a renamed folder, or a pointer to a deleted path makes them do wrong-but-confident work (e.g. rename an approved folder or write to an old path).

## Single source of truth that resists decay

The handoff doc(s) must state, unambiguously, what a reader can CHECK:

- **Precedence**: declare which file is newer and more authoritative, and say it wins when it contradicts the original brief.
- **Authoritative current file tree**: list real locations, and label which subtrees are runtime-loadable vs design-reference vs tooling (gitignored).
- **Actual counts with a table**: give one real number (e.g. "78 assets") with per-category location + counts, so a reader can count and notice drift — not adjectives.
- **The registry + test contract**: say every manifest `target` must also appear in the integrity test's EXPECTED list, and both must exist on disk.
- **State which version of a document supersedes git history** when history contains stale versions.

Persist runnable details INTO the tooling itself: the pipeline script's docstring and the manifest banner should restate canonical paths, the one-subject-per-image rule, the registry-to-test contract, and exact run commands. A session that opens the script gets the contract even if it never reads the roadmap.

## Reconcile before acting

When asked to continue a large project you did not start, or to clean up after sessions drifted:

1. Inspect the tree on disk (`find`/`ls`), not just docs. Detect renamed authoritative folders and stray copies via `git status` + `git ls-files` + `git show HEAD:<path>`.
2. Decide the canonical current layout from disk and real intent; treat your correction as authoritative, not the earlier doc's word, and confirm genuine decisions (folder location, whether to commit) before acting.
3. Verify programmatically that manifest-`target` set == integrity-test-EXPECTED set == on-disk files (a one-liner catches drift even when the objects disagree).
4. After a restructure, search docs + scripts for stale path tokens and old counts (deleted dir suffix, superseded folder names, outdated totals) and correct them in place.
5. When you change a location or number the next session will depend on, update the doc AND the tree in one pass; leave no committed-but-inconsistent pointer.
6. Do not blanket-ignore asset folders or all JSON/Markdown; test `git check-ignore --stdin` on both retained and ignored paths, and do not untrack content without authorization.

## Pitfalls

- **A vision render of an RGBA sprite on white/checker is not proof of an opaque background.** Verify transparency with `img.mode == 'RGBA'` and the transparency percentage, not by how the preview looks.
- **Counting "succeeded" from an exit code is insufficient on a batch generator.** Compare the expected-id list against what actually exists on disk; a filtered or clipped run can report success while outputs are incomplete.
- **Keep approved superseded-state explicit.** When a later direction replaces an earlier one, record which board/version is authoritative and mark the earlier as history; a new session cannot guess that a numbered "v1" folder is superseded.
