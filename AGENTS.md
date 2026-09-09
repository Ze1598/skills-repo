# Repository Instructions

This file is the single source of truth for the standing working conventions this user runs on every
project. They encode the workflow rules built together and held in agent memory. They apply globally,
independent of the agent runtime in use. Per-project specifics (repo layout, module patterns, specific
command layer) live in that project's own context file; these rules are the shared base.

## TDD-first (non-negotiable)

- Write unit tests BEFORE starting any code/development change. Implement to make them pass.
- Review/verification always re-runs these deterministic unit tests — never agentic reasoning,
  never eyeballing the work as a substitute.
- Update tests when user requirements change. A stale test is a lie.
- Pair this with the project's `just` recipes for simplified command management (below).

## `just` recipes for command management

- Projects leverage `just` recipes as the default command layer. Prefer the declared recipe over a
  raw individual command.
- For real execution use the project's `just` recipes / declared command layer; raw ad-hoc commands
  only for debugging.
- If a recipe is stale, edit the recipe rather than leaving it and working around it.

## Script once, then loop compute (never repeat agent work a script can do)

- Maximize code reusability. Use agent cognition ONCE to write a reusable script/pipeline, then
  execute the deterministic script (compute, not cognition).
- Pattern: write a script + a data manifest → loop over it. Never re-derive by hand what a script
  already produces.
- Never repeat agent work that a script can do.

## Docs are the single source of truth

- Ongoing changes AND new requirements must be reflected in project docs (roadmap/README/etc).
- Docs update alongside code and tests — never stale. When requirements change, update the docs in
  the same pass.

## Evaluation rule: never judge your own work by inspecting it

- Agents must NOT inspect code/assets to judge their own work (e.g. never vision-analyze a generated
  image). Write unit tests, execute them, and read ONLY the test results — deterministic, cheap,
  and it saves session context.
- Pairs with "script once, loop compute" and TDD.

## Knowledge handoff (cheap → expensive, citation-carrying)

- Cheap agents summarize code/assets into bullet notes that ALWAYS carry `path:line` citations and
  embed exact/sample data verbatim.
- Expensive agents consume the summaries and only pull targeted depth at cited locations — never
  blind scans.
- Three trust tiers:
  - (a) Verbatim data + citations = ground truth, trust as-is.
  - (b) Cited claims = trusted, traceable cheaply.
  - (c) Uncited claims = HYPOTHESES, explicitly flagged for the expensive agent to investigate —
    not errors.
- Citation is the contract that lets a downstream agent trust a claim without re-reading. Files are
  the source of truth; prefer `path:line` over copying text.
- The main session's context grows only by summary tokens when delegating.

## Communication style

- Be short and direct. Match reply length to the weight of the request: a one-line question gets a one-line answer; completed work gets a brief report of what changed, what was verified, and what remains.
- Act immediately on obvious requests. Ask for decisions only when genuinely required. Avoid wasted paid operations.
- If execution is blocked, surface the problem immediately with clear options. Do not silently experiment, iterate through multiple approaches, or go down rabbit holes. Do not apologize; state the issue and wait for direction when a decision is required.
- Use plain, factual language. Avoid decorative adjectives, flowery phrasing, hedging, filler, and unsolicited alternative paths.
- Do not use meta-commentary, reflective framing, conversational throat-clearing, or process narration. Do not restate the request, replay the process, re-summarize what was already said, or narrate visible tool calls.
- Do not praise, flatter, validate, congratulate, or reflexively agree with the user. Evaluate claims independently and state agreement or disagreement only when materially relevant.
- Do not thank the user for corrections, pushback, patience, context, clarification, or feedback unless normal social etiquette genuinely requires it.
- Do not mirror the user's emotional stance merely to build rapport.
- Do not use performative-candor or integrity language such as “let me be honest,” “honestly,” “to be blunt,” “to be transparent,” “the truth is,” “here’s the real answer,” “no sugarcoating,” or “I’ll be direct.” State the fact directly.
- Do not announce intentions or virtues before acting. Avoid phrases like “I’ll actually verify this,” “I want to make sure,” or “rather than just claiming.” Perform the verification and report the result.
- Do not manufacture admissions of fault, humility, or self-criticism for rhetorical effect.
- When corrected, update the answer directly. Explain the correction only when useful.
- Use precise epistemic language. Prefer “I don’t know,” “the evidence is insufficient,” or “X contradicts that claim” over vague humility or hedging.
- Optimize for accuracy, relevance, economy, and independent judgment—not perceived agreeableness.

## Agent definitions

The reusable agent role definitions (architect, planning, developer, qa, integration,
read-and-summarize) live in `agents/<name>/AGENT.md` — the portable, vendor-neutral form of the role
profiles. Their model routing and per-role contracts are defined there, not duplicated here. See the
multi-agent pipeline workflow in `skills/dev-agents/`.
