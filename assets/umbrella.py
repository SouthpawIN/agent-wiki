#!/usr/bin/env python3
"""umbrella.py — the opinionated pass over ALL topics (Chris 2026-09-05: "an umbrella one over all of it that is also combining
topics … very very automated … opinionated in what it combines together"). Proposals only; every proposal is a card + a
`.proposed` file / queue line. Never merges, deletes or renames anything itself.

Per pass:
  1. Topic similarity (from .system-live.json `similarity`, the wiki's own TF-IDF): pairs ≥ MERGE_AT → PROPOSAL merge
     (topics/_global/.system/proposals.md + card). Pairs in the .system/keep-separate.md list are skipped (Chris's veto persists).
  2. Skill dedupe across topics + ~/.hermes/skills: name collision or ≥ .6 body-token Jaccard → PROPOSAL dedupe (keep A, fold B).
  3. Bot promotion: a topic with ≥ BOT_MIN approved skills and no agents/*.md → PROPOSAL bot (agents/<topic>-bot.md.proposed).
  4. Stale proposals: *.proposed older than STALE_DAYS → one reminder card per topic.
  5. Catalog refresh: topics/_global/{README, .system/topic-index, agent-roster, skill-registry, loop-registry}.md + every
     topic INDEX.md via assets/build-index.py.
Run: python3 assets/umbrella.py  (launchd com.senter.umbrella every 30 min)
"""
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"; LIVE = VAULT / ".system-live.json"
TOKEN = Path.home() / ".hermes/senter-bridge/token"; BRIDGE = "http://127.0.0.1:8643"
BOT_MIN = 3; STALE_DAYS = 3  # merge threshold comes from the LOCKED calibration in .system-live.json similarity.thresholds.propose (Chris approved 2026-09-02)
G = VAULT / "topics/_global"; PROPS = G / ".system/proposals.md"; KEEP = G / ".system/keep-separate.md"

def post(text, status="needs_chris", url=None):
    try:
        body = {"bot": "senter", "text": text, "status": status}
        if url: body["url"] = url
        req = urllib.request.Request(BRIDGE + "/post", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception as e: print("card failed:", e, file=sys.stderr)

def toks(s): return set(re.findall(r"[a-z][a-z0-9]{2,}", (s or "").lower()))
def now(): return time.strftime("%Y-%m-%d %H:%M")

def load_props():
    if not PROPS.exists(): return set(), ""
    t = PROPS.read_text(); return set(re.findall(r"^- \[[ ~]\] (\S+ · \S+)", t, re.M)), t

def add_prop(key, line, existing, buf):
    if key in existing: return buf, False
    return buf + f"- [ ] {key} — {line} ({now()})\n", True

def main():
    L = json.loads(LIVE.read_text()); topics = {k: v for k, v in L.get("topics", {}).items() if not k.startswith("_")}
    S = L.get("similarity") or {}; sim = S.get("matrix") or {}; MERGE_AT = float((S.get("thresholds") or {}).get("propose", 0.35))
    keep = set(re.findall(r"^\s*-\s*(\S+)\s*[·x×]\s*(\S+)", KEEP.read_text(), re.M)) if KEEP.exists() else set()
    keep = {tuple(sorted(p)) for p in keep}
    existing, buf = load_props()
    if not buf: buf = "# Umbrella proposals (topics/_global) — approve by acting, veto merges in .system/keep-separate.md\n\n"
    cards = 0

    # 1) merges
    pairs = []
    names = list(topics)
    for i, a in enumerate(names):
        row = sim.get(a) or {}
        for b in names[i + 1:]:
            sc = row.get(b) if isinstance(row, dict) else None
            if sc is None and isinstance(sim.get(b), dict): sc = sim[b].get(a)
            if sc is not None and sc >= MERGE_AT and tuple(sorted((a, b))) not in keep: pairs.append((sc, a, b))
    for sc, a, b in sorted(pairs, reverse=True)[:5]:
        big, small = (a, b) if len((topics[a].get("text") or "")) >= len((topics[b].get("text") or "")) else (b, a)
        tier = "AUTO-tier" if sc >= float((S.get("thresholds") or {}).get("auto", .5)) else "propose-tier"
        buf, new = add_prop(f"merge · {small}→{big}", f"similarity {sc:.2f} ({tier}); fold `{small}` into `{big}` (keep {big}'s README, move skills/agents/loops, archive {small}). Veto: add `- {a} · {b}` to keep-separate.md", existing, buf)
        if new: post(f"PROPOSAL · merge topics `{small}` → `{big}` (similarity {sc:.2f}, {tier}). Opinion: they are one subject. Veto in topics/_global/.system/keep-separate.md", url=f"topics/{small}/README.md"); cards += 1

    # 2) skill dedupe
    sk = L.get("skills") or []; sk = sk if isinstance(sk, list) else list(sk.values())
    bodies = [(s["name"], toks(s.get("text") or s.get("desc")), s.get("profiles") or [], s.get("proposed")) for s in sk if not s.get("proposed")]
    seen = set()
    for i, (na, ta, pa, _) in enumerate(bodies):
        for nb, tb, pb, _ in bodies[i + 1:]:
            if not ta or not tb or (na, nb) in seen: continue
            j = len(ta & tb) / len(ta | tb)
            if j >= .6:
                seen.add((na, nb)); keepn, fold = (na, nb) if len(ta) >= len(tb) else (nb, na)
                buf, new = add_prop(f"dedupe · {fold}→{keepn}", f"body overlap {j:.2f}; fold `{fold}` ({', '.join(pb)}) into `{keepn}` ({', '.join(pa)})", existing, buf)
                if new: post(f"PROPOSAL · skills `{fold}` and `{keepn}` overlap {j:.0%} — fold {fold} into {keepn}"); cards += 1

    # 3) bot promotion
    for t, v in topics.items():
        td = VAULT / "topics" / t
        approved = [p.parent.name for p in td.glob("skills/*/SKILL.md")]
        has_agent = any(x.suffix == ".md" and not x.name.lower().startswith("readme") for x in (td / "agents").glob("*")) if (td / "agents").is_dir() else False
        if len(approved) >= BOT_MIN and not has_agent:
            p = td / "agents" / f"{t}-bot.md.proposed"
            if not p.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(f"---\ntype: agent\nname: {t}-bot\nproposed: {now()}\ntopic: {t}\nskills: {json.dumps(approved)}\n---\n# {t}-bot\nOwns the `{t}` topic: runs its skills, answers for it, proposes its loops.\n\n## Why a separate intelligence\n{len(approved)} approved skills cluster here with no agent hosting them (umbrella rule BOT_MIN={BOT_MIN}).\n\n## SOUL.md (draft)\nYou are {t}-bot. You serve the `{t}` topic of the Senter wiki. Read topics/{t}/.system/INDEX.md first. Load only these skills: {', '.join(approved)}. Propose, never apply, changes outside your topic.\n")
                post(f"PROPOSAL · bot `{t}-bot` — {len(approved)} approved skills in `{t}` with no agent: {', '.join(approved[:4])}", url=f"topics/{t}/agents/{t}-bot.md.proposed"); cards += 1
                buf, _ = add_prop(f"bot · {t}-bot", f"{len(approved)} skills, no agent → agents/{t}-bot.md.proposed", existing, buf)

    # 4) stale proposals
    cutoff = time.time() - STALE_DAYS * 86400
    for t in topics:
        stale = [p for p in (VAULT / "topics" / t).rglob("*.proposed") if p.stat().st_mtime < cutoff]
        if stale: post(f"REMINDER · {len(stale)} proposal(s) in `{t}` waiting > {STALE_DAYS}d: {', '.join(p.name.split('.')[0] if p.parent.name in ('agents','loops') else p.parent.name for p in stale[:4])}", url=f"topics/{t}/.system/queue.md")

    PROPS.parent.mkdir(parents=True, exist_ok=True); PROPS.write_text(buf)

    # 4b) keep the topic-agent WatchPaths in sync with the topic list (new topics scaffolded by the watcher fire instantly after this)
    try:
        import plistlib, subprocess as _sp
        home = str(Path.home()); pp = f"{home}/Library/LaunchAgents/com.senter.topic-agent.plist"
        with open(pp, "rb") as f: pl = plistlib.load(f)
        want = sorted(str(p) for p in (VAULT / "topics").glob("*/raw/inbox") if p.is_dir() and not p.parent.parent.name.startswith("_"))
        if sorted(pl.get("WatchPaths", [])) != want:
            pl["WatchPaths"] = want
            with open(pp, "wb") as f: plistlib.dump(pl, f)
            uid = os.getuid(); _sp.run(["launchctl", "bootout", f"gui/{uid}/com.senter.topic-agent"], capture_output=True); _sp.run(["launchctl", "bootstrap", f"gui/{uid}", pp], capture_output=True)
            post(f"umbrella · topic-agent now watches {len(want)} inboxes", "done")
    except Exception as e: print("watchpaths:", e, file=sys.stderr)

    # 5) catalogs + INDEX
    bots = L.get("bots") or []; bots = bots if isinstance(bots, list) else list(bots.values()); lp = L.get("loops") or []
    def g(v, *ks):
        for k in ks:
            if isinstance(v, dict) and v.get(k): return str(v[k])
        return ""
    (G / "README.md").write_text(f"# Fleet dashboard (umbrella · {now()})\nTopics {len(topics)} · Bots {len(bots)} ({sum(1 for b in bots if b.get('proposed'))} proposed) · Skills {len(sk)} ({sum(1 for s in sk if s.get('proposed'))} proposed) · Loops {len(lp)} ({sum(1 for l in lp if l.get('proposed'))} proposed)\n- [[topics/_global/.system/topic-index]] · [[topics/_global/.system/agent-roster]] · [[topics/_global/.system/skill-registry]] · [[topics/_global/.system/loop-registry]] · [[topics/_global/.system/proposals]]\n")
    (G / ".system/topic-index.md").write_text("# Topic index\n| topic | summary |\n|---|---|\n" + "\n".join(f"| [[topics/{k}/README|{k}]] | {' '.join((v.get('summary') or [''])[:1])[:140]} |" for k, v in sorted(topics.items())))
    (G / ".system/agent-roster.md").write_text("# Agent roster\n| bot | role | state |\n|---|---|---|\n" + "\n".join(f"| {b.get('name')} | {g(b,'role','summary','desc')[:120]} | {'PROPOSED' if b.get('proposed') else 'live'} |" for b in sorted(bots, key=lambda b: b.get('name',''))))
    (G / ".system/skill-registry.md").write_text("# Skill registry\n| skill | owners | description | state |\n|---|---|---|---|\n" + "\n".join(f"| {s.get('name')} | {', '.join(s.get('profiles') or [])} | {g(s,'desc','description')[:100]} | {'PROPOSED' if s.get('proposed') else 'live'} |" for s in sorted(sk, key=lambda s: s.get('name',''))))
    (G / ".system/loop-registry.md").write_text("# Loop registry\n| loop | owner | cadence | status |\n|---|---|---|---|\n" + "\n".join(f"| {l.get('name')} | {l.get('bot') or l.get('owner','')} | {l.get('cadence','')} | {'PROPOSED' if l.get('proposed') else (l.get('status') or ('on' if l.get('enabled', True) else 'off'))} |" for l in lp))
    subprocess.run([sys.executable, str(VAULT / "assets/build-index.py")], capture_output=True)
    with (VAULT / "log.md").open("a") as f: f.write(f"{now()}: umbrella pass · {cards} proposal cards · {len(pairs)} merge pairs ≥{MERGE_AT} · catalogs+INDEX refreshed\n")
    print(f"umbrella: {cards} cards, {len(pairs)} merge pairs, {len(seen)} dedupes")

if __name__ == "__main__": main()
