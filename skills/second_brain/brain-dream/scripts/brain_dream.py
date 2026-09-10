#!/usr/bin/env python3
"""brain_dream.py — deterministic nightly consolidation pass for the Obsidian Brain.

Pure stdlib, no deps. Reads signals (Brain/log/*.md + Brain/inbox/*.md), counts
same-sign same-topic hits, and applies the preference lifecycle from _brain.yaml.
No LLM. Compute only. Idempotent.

Usage:
  python3 brain_dream.py <vault> [--dry-run] [--window N]
  python3 brain_dream.py <vault> --digest [--since ISO]   # render summary only
"""
import sys, os, re, glob, datetime, json, tarfile, argparse
from collections import defaultdict

VAULT = ""   # set in main() before any path use
CFG = {}
# signal line: `- <date> <time> | topic: <slug> | kind: <k> | <text> | ref: <...>`
SIG_RE = re.compile(
    r"^\s*-\s+(?P<date>\d{4}-\d{2}-\d{2})\s+\S+\s+\|\s+topic:\s*(?P<topic>[a-z0-9-]+)\s+\|\s+kind:\s*(?P<kind>expected|unexpected-positive|unexpected-negative)\s*\|(?P<rest>.*)$"
)
# apply/violate line: `- <date> <time> | pref: pref-<slug> | apply|violate | <text> | ref:`
EVID_RE = re.compile(
    r"^\s*-\s+(?P<date>\d{4}-\d{2}-\d{2})\s+\S+\s+\|\s+pref:\s*pref-(?P<slug>[a-z0-9-]+)\s+\|\s+(?P<action>apply|violate)\s*\|(?P<rest>.*)$"
)

def load_cfg():
    p = os.path.join(VAULT, "Brain", "_brain.yaml")
    cfg = {"candidate_threshold": 3, "same_sign_window_days": 30,
           "trial_days": 14, "unconfirmed_until_days": 30, "confirm_on_apply": True,
           "stale_evidence_days": 90, "rebuttal_threshold": 2, "low_max_applied": 3,
           "confidence": {"low": 1, "medium": 5, "high": 10},
           "snapshot_on_dream": True, "snapshot_keep": 7,
           "retired_keep_days": 365, "max_active_preferences": 100}
    try:
        import yaml
        with open(p) as f:
            loaded = yaml.safe_load(f) or {}
        for k in cfg:
            if k in loaded and loaded[k] is not None:
                cfg[k] = loaded[k]
        if isinstance(loaded.get("confidence"), dict):
            cfg["confidence"].update(loaded["confidence"])
    except Exception as e:
        print(f"warn: could not read {p}: {e}; using defaults", file=sys.stderr)
    return cfg

def parse_iso(d):
    try: return datetime.datetime.strptime(d, "%Y-%m-%d")
    except Exception: return None

def now(): return datetime.datetime.now()

def today_str(): return now().strftime("%Y-%m-%d")

def read_lines_in(paths):
    for p in paths:
        if not os.path.exists(p): continue
        try:
            with open(p) as f:
                for ln in f: yield ln
        except Exception: pass

def collect_signals(window_days):
    """-> {(topic, kind): [lines]} within window"""
    cutoff = now() - datetime.timedelta(days=window_days)
    inbox = glob.glob(os.path.join(VAULT, "Brain", "inbox", "sig-*.md"))
    logs = glob.glob(os.path.join(VAULT, "Brain", "log", "*.md"))
    groups = defaultdict(list)
    for ln in read_lines_in(inbox + logs):
        m = SIG_RE.match(ln)
        if not m: continue
        d = parse_iso(m.group("date"))
        if not d: continue
        if d.date() < cutoff.date(): continue
        groups[(m.group("topic"), m.group("kind"))].append(ln.strip())
    return groups

def collect_evidence():
    """-> {slug: {'apply': n, 'violate': n, last_date}}"""
    logs = glob.glob(os.path.join(VAULT, "Brain", "log", "*.md"))
    ev = defaultdict(lambda: {"apply": 0, "violate": 0, "last": None})
    for ln in read_lines_in(logs):
        m = EVID_RE.match(ln)
        if not m: continue
        d = parse_iso(m.group("date"))
        act = m.group("action")
        ev[m.group("slug")][act] += 1
        if d and (ev[m.group("slug")]["last"] is None or d.date() > ev[m.group("slug")]["last"]):
            ev[m.group("slug")]["last"] = d.date()
    return ev

def pref_paths():
    d = os.path.join(VAULT, "Brain", "preferences")
    return {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(os.path.join(d, "pref-*.md"))}

def read_pref(slug):
    p = os.path.join(VAULT, "Brain", "preferences", f"pref-{slug}.md")
    if not os.path.exists(p): return None
    with open(p) as f: return f.read()

def write_pref(slug, body):
    p = os.path.join(VAULT, "Brain", "preferences", f"pref-{slug}.md")
    with open(p, "w") as f: f.write(body)
    return p

def retire(slug, reason):
    src = os.path.join(VAULT, "Brain", "preferences", f"pref-{slug}.md")
    dst = os.path.join(VAULT, "Brain", "retired", f"ret-{slug}.md")
    if os.path.exists(src):
        with open(src) as f: content = f.read()
        content = re.sub(r"(?m)^status:.*$", f"status: retired_{reason}", content, count=1)
        content += f"\nretired_at: {today_str()}\nretired_reason: {reason}\n"
        with open(dst, "w") as f: f.write(content)
        os.remove(src)

def confidence(applied, violated):
    c = CFG["confidence"]
    return min(c["high"], c["low"] + applied - violated)

def frontmatter(slug, status, topic, confidence, created):
    return (f"---\nslug: {slug}\ntopic: {topic}\nstatus: {status}\nconfidence: {confidence}\n"
            f"created: {created}\n---\n")

def snapshot():
    snap_dir = os.path.join(VAULT, "Brain", ".snapshots")
    os.makedirs(snap_dir, exist_ok=True)
    if not CFG.get("snapshot_on_dream"): return
    name = os.path.join(snap_dir, f"dream-{now().strftime('%Y%m%d-%H%M%S')}.tar.gz")
    brain = os.path.join(VAULT, "Brain")
    with tarfile.open(name, "w:gz") as tf:
        tf.add(brain, arcname="Brain")
    # prune old
    snaps = sorted(glob.glob(os.path.join(snap_dir, "dream-*")))
    keep = int(CFG.get("snapshot_keep", 7))
    for old in snaps[:-keep]:
        try: os.remove(old)
        except Exception: pass

def process_signal_groups(groups, evidence, dry):
    """Core dream logic -> returns list of human-readable digest lines."""
    lines = []
    existing = pref_paths()
    # create unconfirmed prefs from new signal groups
    for (topic, kind), sigs in groups.items():
        if kind == "expected":   # no rule from 'as expected' — it confirms nothing new
            continue
        n = len(sigs)
        if n < int(CFG["candidate_threshold"]):
            continue
        slug = topic
        if slug in existing:
            continue
        body = frontmatter(slug, "unconfirmed", topic, 0, today_str())
        body += f"\n# {topic}\n\n**Status:** unconfirmed (trial {CFG['trial_days']}d)\n\n**Signals ({n}):**\n"
        for s in sigs:
            body += f"{s}\n"
        body += "\n**Evidence:** apply raises confidence; violate lowers / quarantines.\n"
        if not dry:
            write_pref(slug, body)
        lines.append(f"new-unconfirmed: {slug} (topic={topic}, {n} signals)")
    return lines

def process_evidence(prefs, evidence, dry):
    lines = []
    for slug, ev in evidence.items():
        body = read_pref(slug)
        if body is None:
            continue
        applied, violated = ev["apply"], ev["violate"]
        status_m = re.search(r"(?m)^status:\s*(\S+)", body)
        status = status_m.group(1) if status_m else "unconfirmed"
        created_m = re.search(r"(?m)^created:\s*(\S+)", body)
        created = created_m.group(1) if created_m else today_str()
        last = ev["last"]
        age_days = (now().date() - (last or now().date())).days if last else 0
        # lifecycle
        if status == "unconfirmed":
            if CFG.get("confirm_on_apply") and applied >= 1:
                body = re.sub(r"(?m)^status:.*$", f"status: confirmed", body, count=1)
                body = re.sub(r"(?m)^confidence:.*$", f"confidence: {confidence(applied, violated)}", body, count=1)
                if not dry: write_pref(slug, body)
                lines.append(f"confirmed: {slug} (first apply)")
            elif last and age_days > int(CFG["unconfirmed_until_days"]):
                if not dry: retire(slug, "expired-unconfirmed")
                lines.append(f"retired: {slug} (expired-unconfirmed)")
        elif status == "confirmed":
            # quarantine if violations dominate below low_max_applied
            if violated >= applied and applied <= int(CFG["low_max_applied"]) and violated > 0:
                body = re.sub(r"(?m)^status:.*$", "status: quarantine", body, count=1)
                if not dry: write_pref(slug, body)
                lines.append(f"quarantine: {slug} (violations>=applied, low base)")
            elif applied > violated:
                conf = confidence(applied, violated)
                body = re.sub(r"(?m)^confidence:.*$", f"confidence: {conf}", body, count=1)
                if not dry: write_pref(slug, body)
                if conf >= int(CFG["confidence"]["high"]) and applied >= int(CFG["confidence"]["high"]):
                    lines.append(f"confidence-shift: {slug} -> high (applied {applied}, violated {violated})")
            # stale
            if last and age_days > int(CFG["stale_evidence_days"]):
                if not dry: retire(slug, "stale-no-evidence")
                lines.append(f"retired: {slug} (stale-no-evidence)")
            # rebuttal
            if violated >= int(CFG["rebuttal_threshold"]) and violated >= applied:
                if not dry: retire(slug, "rebutted")
                lines.append(f"retired: {slug} (rebutted)")
        elif status == "quarantine":
            if applied > violated:
                body = re.sub(r"(?m)^status:.*$", "status: confirmed", body, count=1)
                if not dry: write_pref(slug, body)
                lines.append(f"recovered: {slug} -> confirmed (applied {applied} > violated {violated})")
            else:
                if not dry: retire(slug, "quarantine-violated")
                lines.append(f"retired: {slug} (quarantine-violated)")
    return lines

def digest_lines():
    cfg = CFG
    signals = collect_signals(int(cfg["same_sign_window_days"]))
    evidence = collect_evidence()
    new_l = process_signal_groups(signals, evidence, dry=False)
    ev_l = process_evidence(pref_paths(), evidence, dry=False)
    return new_l + ev_l

def render_digest(lines, since=None):
    out = [f"# Brain digest — {today_str()}"]
    if not lines:
        out.append("\nNo changes.")
        return "\n".join(out)
    out.append("")
    for ln in lines:
        out.append(f"- {ln}")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--window", type=int, default=None)
    ap.add_argument("--digest", action="store_true")
    ap.add_argument("--since", default=None)
    ap.add_argument("--silent-if-empty", action="store_true")
    a = ap.parse_args()
    global VAULT, CFG
    VAULT = a.vault
    CFG = load_cfg()
    if a.window: CFG["same_sign_window_days"] = a.window
    if a.digest:
        lines = digest_lines()
        if a.silent_if_empty and not lines:
            sys.exit(2)   # no changes -> empty stdout + nonzero exit (cron treats as no-op)
        print(render_digest(lines, a.since))
        return
    # full pass
    snapshot()
    signals = collect_signals(int(CFG["same_sign_window_days"]))
    evidence = collect_evidence()
    new_l = process_signal_groups(signals, evidence, a.dry_run)
    ev_l = process_evidence(pref_paths(), evidence, a.dry_run)
    all_lines = new_l + ev_l
    if a.dry_run:
        print("[DRY RUN]")
    for ln in all_lines:
        print(ln)
    if not all_lines:
        print("no changes")

if __name__ == "__main__":
    main()
