# Onboarding the Dev Pipeline into a New or Existing Project

Executed by the Architect role (main Hermes session) when the user says something like *"start this
project with the dev pipeline"* or *"onboard the pipeline into <repo>"*. The user does not follow
this file — the Architect runs it and reports back. Work from the canonical repo path the user gives.

## Prerequisites / confirm
- A target repo path (canonical, git). For a brand-new project, get a path to create, or confirm an
  empty dir to git-init.
- Confirm scope: new project vs onboarding Hermes into an existing repo. Existing repos have maybe a
  CLAUDE.md/AGENTS.md already — extend it, don't clobber the user's own rules.

## Step 1 — Create the board
```
hermes kanban boards create <slug> \
  --name "<Project display name>" \
  --description "<what this project is>" \
  --default-workdir /absolute/canonical/repo/path
```
`<slug>` = kebab-case alias for the repo (e.g. `data-platform`). The `--default-workdir` makes the
canonical repo the workspace every new task inherits — this is what keeps code-edit claims
one-at-a-time on the real tree. Optionally `boards switch <slug>` to make it active. The first board
setup is `default`; named boards are per-project isolation (separate DB/workspaces/logs).

## Step 2 — Write the repo's context layer (CLAUDE.md / AGENTS.md in the repo)
The global role skills are intentionally repo-agnostic. This per-repo file is what actually varies
between projects. If a repo CLAUDE.md/AGENTS.md exists, append; otherwise create one at the repo
root. Common content, adjusted to the project:
- **Git state rule**: read-only git allowed (`status/diff/log/show`), NEVER `add/commit/push/
  restore/reset` — workers report, they don't mutate history.
- **Command layer**: the repo's declared execution path (e.g. `just` recipes) for running code/tests/
  features; raw ad-hoc commands only for debugging; edit a stale recipe rather than leaving it.
- **Env/test fixes** specific to this repo (e.g. iCloud `.pth`/`ModuleNotFoundError` rebuild fix,
  `dagster dev`/`streamlit` process-kill, `uv sync --all-packages`, DebugReference.md per module).
- **Module map & integration justification** (which are the "multiple modules that genuinely
  interact" — determines whether the Integration card is created for a task).
Notes: two workers never edit the canonical repo concurrently — serialized via sole-claim cards.
Genuine parallel QA/Dev work uses isolated worktree branches, merged sequentially at Integration.

## Step 3 — Sanity-check routing
- `hermes profile list` → confirm architect/planning route `openai/gpt-6-astra-flex`, developer/qa/
  integration route `qwen/qwen3.8-flash` (nous provider). Nothing to change unless the user wants a
  different model.
- Confirm each role's skill is enabled in its profile (`hermes -p <role> skills list`): planning/qa/
  developer/integration each show their `dev-agents` role skill.
- `hermes kanban boards` → the new board is present.

## Step 4 — Report ready
Tell the user the project is onboarded: board slug, where the context file lives, that models route
per the cost split, and what to say next to route the first substantial task (e.g. *"run <requirement>
through the pipeline on <project>"*). Ask if they want a first task routed now, or nothing yet.

## Invariant reminder for the Architect during onboarding
- Architect is the only role that creates the board and writes the repo context file — do NOT delegate
  these to a worker profile.
- Do NOT bake any repo-specific rule into the global role skills under dev-agents/; the per-repo
  CLAUDE.md is the only place they belong.
- The pipeline runs only for substantial work; trivial fixes (doc/config/one-file) bypass the DAG.
