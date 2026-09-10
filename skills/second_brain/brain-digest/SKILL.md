---
name: brain-digest
description: Periodic review surface for the Obsidian Brain — the launchd daily consolidation job, macOS notification, delta catch-up, and how to read the digest.
---

# Brain Digest — Periodic Review

Use when the daily Brain consolidation runs, when wiring/reviewing the consolidation job, or when
reading a digest to decide what the owner should act on. This is the automated "periodic review point"
of the second brain.

Siblings: `obsidian-second-brain` (operating manual), `brain-signals` (capture),
`brain-dream` (consolidation).

## The launchd job

The consolidation loop runs as **`com.hermes.braindigest`**, a macOS launchd job independent of the
Hermes gateway (runs even with the gateway off; survives reboots).

- **Plist:** `~/Library/LaunchAgents/com.hermes.braindigest.plist`
- **Schedule:** daily at **22:00** (`StartCalendarInterval`: Hour=22, Minute=0).
- **Script:** `~/.hermes/scripts/brain-digest.sh` — runs the dream pass, then renders the digest.
- **Env:** `OBSIDIAN_VAULT_PATH` baked into the plist. The script pins the Framework Python 3.13
  (`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`) because system `/usr/bin/python3`
  lacks `pyyaml`.
- **Logs:** `~/.hermes/logs/brain-digest.{out,err}.log`.
- **Notification:** when there is a digest to report, fires a **macOS notification** (`osascript`
  banner, title "Brain digest — <date>", subject = first change line). Silent when nothing changed.

## Manage it

```bash
launchctl load ~/Library/LaunchAgents/com.hermes.braindigest.plist     # install/register
launchctl list | grep braindigest                                      # registered: `- 0 com.hermes.braindigest`
launchctl kickstart -k gui/$(id -u)/com.hermes.braindigest             # run once / verify
cat ~/.hermes/logs/brain-digest.{err,out}.log                          # inspect last run
```

## Delta behavior (missed runs are not lost)

launchd does not queue a run missed while the machine is off — it waits for the next scheduled time.
**Nothing is lost**, because the dream pass re-scans signals within `same_sign_window_days` (default 30
days) on every run. A machine off for N days consolidates the whole N-day delta on its next successful
run; recovery is not locked to "yesterday." Live capture during sessions is independent of this job
entirely.

## The digest output

```
# Brain digest — <date>

- new-unconfirmed: <slug> (topic=<topic>, N signals)
- confirmed: <slug> (first apply)
- quarantine: <slug> (violations>=applied, low base)
- recovered: <slug> -> confirmed
- retired: <slug> (stale-no-evidence / expired-unconfirmed / rebutted / quarantine-violated)
- confidence-shift: <slug> -> high (applied N, violated N)
```

## Reading it as the owner/reviewer

- **New unconfirmed** — rules in a 14-day trial; glance at cited signals, decide whether to keep or
  reject (`user_rejected`).
- **Confirmed** — a rule now shapes behavior; worth a sanity check.
- **Retired** — memory freed; check for any that shouldn't have been.
- **Confidence shifts** — rising/falling confidence on a rule you care about.

The digest is opt-in automation: it reports changes; the owner decides what to act on.

## Optional Hermes-cron chat delivery

A `brain-digest-nightly` Hermes cron (`--no-agent --script --deliver local`) can mirror the launchd job
for chat delivery on days the gateway is up. It is NOT the authoritative runner — the launchd job is
(delivery-agnostic, gateway-independent).

## Verification

`launchctl list | grep braindigest` shows it registered. `launchctl kickstart -k
gui/$(id -u)/com.hermes.braindigest` runs it once; a non-empty digest in `~/.hermes/logs/brain-digest.out.log`
with an empty error log confirms it works end-to-end.