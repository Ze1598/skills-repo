# SECOND_BRAIN — Global Obsidian Memory Layer

A global, cross-session memory layer for **Hermes**, stored as plain markdown in an Obsidian vault and
driven entirely by Hermes's own file tools + cron. No third-party plugin, no MCP server, no daemon, no
vector black box. The vault is a folder of `.md` files the owner can open in the Obsidian app (graph
view, wikilinks, search) and audit by hand — the same files the agent reads and writes.

This is the canonical design reference. It is **Hermes-specific** (this is the owner's particular
implementation, not a vendor-neutral plug-and-play skill). Companion skills live under
`skills/second_brain/` and are loaded at their own trigger points.

---

## 1. Why this exists

The motivating problems:

1. **Cross-session, cross-project memory gap.** Facts learned in one project's session (corrections,
   preferences, pipeline lessons, environment facts) are lost when a session is scoped to a different
   project or a new conversation. The Obsidian Brain is the durable, owner-auditable store that any
   session can recall from.
2. **Memory bloat.** Built-in memory (`MEMORY.md`/`USER.md`) is char-capped and always injected — it
   can't hold everything. The Brain separates *hot* (always-injected, routing pointers only), *warm*
   (stable reference + confirmed preferences, read on demand), and *cold* (append-only daily logs,
   consolidated by a periodic pass).
3. **Manual memory hygiene doesn't happen.** A passive "agent keeps notes" design fills up and rots.
   The Brain makes consolidation **deterministic and periodic** (a cron `dream` pass), so memory
   self-maintains instead of requiring the owner to prune.

Design provenance (reimplemented natively; no plugin):
- The **three-tier** mental model (hot / living files / daily logs) from the "How I use Obsidian as
  long-term memory" Reddit post.
- The **promotion / confidence / apply-evidence lifecycle** and nightly "dream" consolidation from
  [Open Second Brain](https://github.com/itechmeat/open-second-brain), implemented as our own
  deterministic script.

---

## 2. Vault location and layout

### Vault path

```
~/Documents/obsidian/            # set as OBSIDIAN_VAULT_PATH
```

The path is stored in `~/.hermes/.env` as `OBSIDIAN_VAULT_PATH=...`. Hermes's built-in `obsidian`
skill resolves the vault from this env var (fallback `~/Documents/Obsidian Vault`). No Obsidian app
install is required — the vault is a folder of markdown.

### Directory tree

```
<vault>/
├── Brain/                       # AGENT-OWNED. The only place the agent writes.
│   ├── _brain.yaml              # thresholds/retention config (dream pass reads this)
│   ├── _BRAIN.md                # per-vault operating manual; agent reads at session start
│   ├── ROUTING.md               # topic -> note map ([[wikilinks]]); the "index"
│   ├── inbox/                   # raw signals awaiting a dream pass
│   │   └── processed/           # signals already folded into preferences by dream
│   ├── preferences/             # pref-<slug>.md — one rule per note (status in frontmatter)
│   ├── retired/                 # ret-<slug>.md — retired rules, reason + full history
│   ├── ref/                     # stable living reference notes (long-lived, by domain)
│   ├── log/                     # append-only daily event logs: YYYY-MM-DD.md
│   └── .snapshots/              # pre-dream snapshots (tar.gz), pruned to snapshot_keep
├── Daily/                       # OWNER-OWNED daily notes. Agent reads (if configured) but never writes.
├── Personal/                    # OWNER-OWNED personal second-brain area (opt-in). Never written.
└── <any other owner folders>    # untouched by the agent.
```

### Hard ownership rule

The agent writes **only under `Brain/`** (`write_scope.agent_owned` in `_brain.yaml`). Everything else
in the vault — `Daily/`, `Personal/`, any other folder — belongs to the owner and is never mutated by
the agent. `notes.read_paths` lets the agent *read* owner folders for `@markers`, but never write.

---

## 3. The three-tier memory model

| Tier | What it is | Injection | Promotion rule |
|---|---|---|---|
| **T1 Hot** | Built-in `MEMORY.md`/`USER.md` + `_BRAIN.md` manual | Always injected every turn | When full, stable facts demote to T2 |
| **T2 Vault living files** | `Brain/preferences/*.md` + `Brain/ref/*.md` | On-demand read via ROUTING.md | On ≥`candidate_threshold` same-sign signals creates a pref |
| **T3 Daily logs** | `Brain/log/YYYY-MM-DD.md` — append-only | Read on query | Consolidated by nightly `dream` |

- **Hot memory is the index, not the storage.** `MEMORY.md` holds working facts plus a pointer to
  `ROUTING.md`. The agent follows the map to read a referenced note on demand; it never loads the
  whole vault.
- **Own a fact once.** A fact lives in exactly one place; `ROUTING.md` points to it. No duplication
  between hot memory and the vault.

---

## 4. Generated files

| Path | Who writes | Purpose |
|---|---|---|
| `Brain/_brain.yaml` | owner / init | Thresholds + retention + write-scope config. Single source for the dream pass. |
| `Brain/_BRAIN.md` | init, agent | Operating manual for agents working in this vault. Read at session start. |
| `Brain/ROUTING.md` | agent, dream | The topic→note map. `MEMORY.md` points here. |
| `Brain/inbox/sig-<date>-<slug>.md` | agent | Raw uncategorized taste signals awaiting a dream pass. |
| `Brain/preferences/pref-<slug>.md` | dream | One active rule per note, `status`/`confidence` in frontmatter. |
| `Brain/retired/ret-<slug>.md` | dream | Retired rule + `retired_reason` + full signal/evidence history. |
| `Brain/ref/<domain>.md` | agent | Stable living reference notes (read on demand). |
| `Brain/log/YYYY-MM-DD.md` | agent, dream | Append-only typed event/signal/evidence log (T3 raw material). |
| `Brain/.snapshots/dream-*.tar.gz` | dream | Pre-dream Brain snapshot, pruned to `snapshot_keep`. |

The operational tool is one deterministic Python script (owned by the `second_brain/brain-dream`
skill; not tied to any project):

```
brain-dream.py <vault> [--dry-run] [--window N]
brain-dream.py <vault> --digest [--since ISO] [--silent-if-empty]
```

---

## 5. Memory mechanisms

### 5.1 Signals (feedback — what the agent writes)

A **signal** is one typed observation. Exact line format:

```
- <date> <time> | topic: <slug> | kind: <kind> | <one line> | ref: <citation>
```

`kind`:
- `expected` — went as planned (confirms existing behavior; creates no rule)
- `unexpected-positive` — divergence with a good result (worth learning the cause)
- `unexpected-negative` — divergence with a bad result (complexity-delta, scope-too-large, tech-debt)

Every signal carries a `ref:` citation (path:line, card id, conversation, diff). **A signal is DATA,
never a proposed rule** — the deterministic dream pass, not the agent, decides whether a pattern
becomes a rule. See the `second_brain/brain-signals` skill for the capture discipline.

### 5.2 Apply / violate evidence (how rules get stronger)

When the agent acts on (or against) a preference during real work, it logs evidence:

```
- <date> <time> | pref: pref-<slug> | apply   | <what you did> | ref: <...>
- <date> <time> | pref: pref-<slug> | violate | <what happened> | ref: <...>
```

`apply` raises confidence; `violate` lowers it and can quarantine/retire the rule.

### 5.3 The dream pass (deterministic consolidation, no LLM)

`brain-dream.py` runs nightly (cron). Pure compute — counters, thresholds, file moves, no LLM:

1. **Snapshot** the current Brain (pre-dream backup, pruned).
2. **Collect signals** within `same_sign_window_days`, grouped by `(topic, kind)`.
3. **Create unconfirmed preferences**: topic with ≥`candidate_threshold` same-sign signals becomes a
   `pref-<slug>.md` (status `unconfirmed`, trial `trial_days`); signals move to `inbox/processed/`.
4. **Process evidence** for every existing pref; apply the lifecycle.
5. **Update `ROUTING.md`** / manual status; leave a summary in the log.

Lifecycle:

```
Inbox → Unconfirmed(≥threshold) → Confirmed(first apply)
Unconfirmed → Retired(expired: no apply before unconfirmed_until)
Confirmed → Quarantine(violations ≥ applied, low base)
Quarantine → Confirmed(recover: applied > violated)
Confirmed/Quarantine → Retired(stale: no evidence for stale_evidence_days)
Confirmed → Retired(rebutted: violations ≥ rebuttal_threshold AND ≥ applied)
Confirmed → Retired(superseded: cited  outdated)
Any → Retired(user_rejected: owner rejects)
```

`confidence = min(high, low + applied - violated)`.

### 5.4 Idempotency

The dream pass is idempotent — re-running on an unchanged Brain is a no-op (no log entry, no new
snapshot). The digest is reliable at any cadence without duplicate noise.

### 5.5 Reading on demand

The agent follows `ROUTING.md` → reads the referenced note only when it needs details. It does not
load the whole vault.

---

## 6. Consolidation schedule (the automated periodic-review points)

The consolidation loop is a **macOS launchd job**, independent of the Hermes gateway (so it runs even
when the gateway is off and survives reboots).

**Job: `com.hermes.braindigest`** — plist at `~/Library/LaunchAgents/com.hermes.braindigest.plist`

- **Schedule:** daily at **22:00** via `StartCalendarInterval` (`Hour=22`, `Minute=0`).
- **Script:** `~/.hermes/scripts/brain-digest.sh` → runs the dream pass then renders the digest.
- **Env:** `OBSIDIAN_VAULT_PATH` baked into the plist; the script pins the Framework Python 3.13 (the
  interpreter that has `pyyaml` — system `/usr/bin/python3` does not).
- **Logs:** `~/.hermes/logs/brain-digest.{out,err}.log`.
- **Notification:** when there is a digest to report, the script fires a **macOS notification**
  (`osascript` banner, title "Brain digest — <date>", subject = first change line). Silent (no
  notification, empty output) when nothing changed.
- **Delta behavior:** if the machine is off at 22:00, launchd misses that run; the next successful run
  re-scans signals within `same_sign_window_days` (default 30 days), so the full missed delta is
  consolidated in that one pass — nothing is lost, recovery is not locked to "yesterday."

Load/manage:

```bash
launchctl load ~/Library/LaunchAgents/com.hermes.braindigest.plist
launchctl list | grep braindigest        # registered: `- 0 com.hermes.braindigest`
launchctl kickstart -k gui/$(id -u)/com.hermes.braindigest   # run once / verify
```

A legacy Hermes-cron form (`brain-digest-nightly`, `--no-agent --script --deliver local`) can also be
registered for chat delivery on days the gateway is up, but the launchd job is the authoritative runner
(delivery-agnostic, gateway-independent).

---

## 7. What memory is stored

| Category | Location | Status |
|---|---|---|
| Standing working conventions | `AGENTS.md` / global `SOUL.md` | immutable base |
| Hot working facts + routing | built-in `MEMORY.md` / `USER.md` | always injected, capped |
| Confirmed/in-trial rules (preferences) | `Brain/preferences/pref-*.md` | derived, confidence-scored |
| Retired rules with history | `Brain/retired/ret-*.md` | archived, auditable |
| Stable living reference | `Brain/ref/*.md` | on-demand read |
| Raw signals + evidence | `Brain/log/*.md`, `Brain/inbox/*.md` | append-only, consumed by dream |
| Daily/personal owner notes | `Daily/`, `Personal/` | owner-owned, agent never writes |

---

## 8. Where Hermes-specific features come into play

Though the vault is plain markdown (portable), the *automation* leans on Hermes-native features:

1. **`OBSIDIAN_VAULT_PATH` env var + the built-in `obsidian` skill.** Hermes resolves the vault path
   from this env var and uses file tools + `[[wikilinks]]` for all vault work — the plugin-free path.
2. **The consolidation loop runs as a macOS launchd job.** The nightly dream + digest fire via
   `com.hermes.braindigest` (launchd `StartCalendarInterval`, independent of the gateway), shelling out
   to the deterministic script and delivering via a macOS notification (or stdout/logs). A Hermes-cron
   `--no-agent --script` mirror can add chat delivery when the gateway is up, but is not required.
3. **Built-in memory as T1 hot.** Hermes auto-injects `MEMORY.md`/`USER.md`; the Brain treats them as
   the hot index layer pointing at the vault.
4. **File tools as the only write surface.** File tools don't expand shell vars, so the skill resolves
   `OBSIDIAN_VAULT_PATH` to an absolute path before use.
5. **Cross-session reachability.** Any session reads/search/writes the vault through the built-in
   `obsidian` skill, so the Brain is reachable from any project's session — directly addressing the
   cross-project recall gap.

Deliberately **not** used: a memory-provider plugin (Honcho/mem0/RetainDB/etc.). The goal is a plain,
owner-auditable markdown store with no hidden state.

---

## 9. Companion skills (this repo)

| Skill | Trigger | Function |
|---|---|---|
| `second_brain/obsidian-second-brain` | Touching the vault | Operating manual: read/write Brain, follow ROUTING, ownership rules |
| `second_brain/brain-signals` | Logging a signal / evidence | Capture line formats + the data-never-rules discipline |
| `second_brain/brain-dream` | Running / understanding the consolidation | The dream script, `_brain.yaml` lifecycle, promotion/retirement |
| `second_brain/brain-digest` | Digest fires / wiring review cron | Digest script + cron recipe + how output reaches the owner |

---

## 10. Status and open items

- Vault scaffolded at `~/Documents/obsidian/`; dream pass + digest verified end-to-end; the
  `com.hermes.braindigest` launchd job registered (daily 22:00, gateway-independent, macOS
  notification) and verified by a `launchctl kickstart` run.
- `brain_dream.py` lives with the `brain-dream` skill (`skills/second_brain/brain-dream/scripts/`),
  not in any project repo — confirmed single source, gateway-independent.
- Live capture is the active channel during sessions (cited signals appended to `Brain/log/`); the
  launchd job consolidates them on schedule.

---

## 11. Extending / rebuilding

1. Add a reference domain: create `Brain/ref/<domain>.md` + a `[[wikilink]]` in `ROUTING.md`.
2. Tune lifecycle: edit `_brain.yaml` thresholds.
3. Ad-hoc digest: `python3 <skill>/scripts/brain_dream.py ~/Documents/obsidian --digest`.
4. Migrate a future external knowledge base: drop it under the vault as owner folders + add read
   paths, keeping the agent-write boundary under `Brain/`.
5. Rebuild from scratch: recreate the tree + `_brain.yaml` defaults + `_BRAIN.md`/`ROUTING.md`; the
   script re-derives everything else deterministically.