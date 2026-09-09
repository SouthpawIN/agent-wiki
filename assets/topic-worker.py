#!/usr/bin/env python3
"""topic-worker.py — one asynchronous worker for ONE topic (Chris 2026-09-05: "one senter copy per topic … context → skills →
bot → loop suggestion … each topic asynchronously"). GEPA shape from SENTER.md: Collect → Generate → Evaluate → Apply.

  Collect   new `##` blocks in topics/<t>/.system/inbox.md since .system/worker.cursor (+ continuity.md, existing skills)
  Generate  ONE real bot run: `hermes chat -p senter --query-file … --oneshot -Q` returns JSON proposals (skills / bot / loop /
            continuity deltas). The bot never writes files — this script does.
  Evaluate  drop proposals that duplicate an existing skill (name or ≥.6 token overlap), require ≥2 evidence blocks per skill,
            cap 3 skills per pass. Bot proposal requires ≥3 related skills (existing + proposed). Loop requires a bot.
  Apply     write `.proposed` artifacts only:
              topics/<t>/skills/<slug>/SKILL.md.proposed · agents/<slug>.md.proposed · loops/<slug>.md.proposed
            append continuity deltas to .system/continuity.md under "## learned <date>" (never touch <!-- chris --> lines)
            append queue items ([SKILLS]/[AGENTS]/[LOOPS] `- [ ]`) · injections [UNREAD] · ONE feed card per proposal
Approval (Chris) = rename away `.proposed` (UI card button later); rejection = delete. Concurrency: `hermes kanban claim` on a
per-topic task when a board exists; otherwise a lock file .system/worker.lock (stale > 20 min ignored).
Run: python3 assets/topic-worker.py <topic> [--dry]  · all topics with new inbox: --all
"""
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"
BRIDGE = "http://127.0.0.1:8643"; TOKEN = Path.home() / ".hermes/senter-bridge/token"
PROFILE = os.environ.get("SENTER_WORKER_PROFILE", "senter")
MAX_SKILLS = 3; MIN_EVIDENCE = 2; BOT_MIN_SKILLS = 3

def post(text, status="working", url=None):
    try:
        body = {"bot": "senter", "text": text, "status": status}
        if url: body["url"] = url
        req = urllib.request.Request(BRIDGE + "/post", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception as e: print("card failed:", e, file=sys.stderr)

def stage(act, **kw):
    try:
        body = {"act": act, "bot": "senter", **{k: v for k, v in kw.items() if v}}
        req = urllib.request.Request(BRIDGE + "/stage", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception: pass

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48] or "item"
def toks(s): return set(re.findall(r"[a-z][a-z0-9]{2,}", s.lower()))

def collect(t: Path):
    cur = t / ".system/worker.cursor"; days = sorted((t / "raw/inbox").glob("*.md")) if (t / "raw/inbox").is_dir() else []
    legacy = t / ".system/inbox.md"
    text = ("\n".join(d.read_text() for d in days)) + ("\n" + legacy.read_text() if legacy.is_file() else "")
    if not text.strip(): return [], None
    seen = cur.read_text().strip() if cur.exists() else ""
    blocks = re.split(r"\n(?=## )", text)
    blocks = [b for b in blocks if b.startswith("## ")]
    if seen and seen in [b.split("\n", 1)[0] for b in blocks]:
        idx = [b.split("\n", 1)[0] for b in blocks].index(seen); blocks = blocks[idx + 1:]
    return blocks, (blocks[-1].split("\n", 1)[0] if blocks else None)

def existing_skills(t: Path):
    out = {}
    for p in list(t.glob("skills/*/SKILL.md")) + list((Path.home() / ".hermes/skills").glob("*/SKILL.md")):
        try: out[p.parent.name] = p.read_text()[:1500]
        except Exception: pass
    return out

PROMPT = """You are the topic worker for the Senter wiki topic "{topic}". You are the GENERATE+EVALUATE step of a GEPA cycle.
Read the NEW CONTEXT (raw chat, filed per message by the watcher) and the CONTINUITY (what the system already understands).
Return ONLY a JSON object — no prose, no code fence — with this shape:
{{
 "continuity": ["one-line facts/decisions/preferences learned that are NOT already in continuity", ...],
 "skills": [{{"name": "kebab-slug", "description": "Use when <trigger>. <one-line behaviour>.", "body": "markdown SKILL body: steps, rules, pitfalls — imperative, evidence-based", "evidence": ["quote 1 from new context", "quote 2"]}}],
 "bot": null | {{"name": "kebab-slug", "role": "one line", "skills": ["existing or proposed skill names"], "soul": "SOUL.md draft", "why": "why a separate intelligence is warranted"}},
 "loop": null | {{"name": "kebab-slug", "cadence": "cron-ish", "agent": "bot name", "prompt": "what it does each tick", "why": "which stable workflow this automates"}}
}}
Rules (SENTER.md): skills emerge from REPEATED evidence (>=2 quotes) — never from a capability mentioned once. Propose a bot only
if a coherent cluster of >= {botmin} related skills exists (list them). Propose a loop only if a bot has a stable repeatable
workflow. Prefer fewer, sharper proposals. Never duplicate EXISTING SKILLS (listed by name). Quote Chris verbatim in evidence.

EXISTING SKILLS: {skills}

CONTINUITY:
{continuity}

NEW CONTEXT ({n} blocks):
{context}
"""

def generate(topic, blocks, cont, skills, dry):
    q = PROMPT.format(topic=topic, botmin=BOT_MIN_SKILLS, skills=", ".join(sorted(skills))[:3000], continuity=cont[:6000], n=len(blocks), context="\n\n".join(blocks)[:24000])
    qf = Path(f"/tmp/topic-worker-{topic}.md"); qf.write_text(q)
    if dry: print(q[:1500]); return None
    r = subprocess.run(["hermes", "chat", "-p", PROFILE, "--query-file", str(qf), "--oneshot", "-Q", "--max-turns", "1"], capture_output=True, text=True, timeout=600, cwd=str(VAULT))
    out = r.stdout.strip()
    m = re.search(r"\{[\s\S]*\}", out)
    if not m: print("no JSON from bot:", out[:400], r.stderr[:400], file=sys.stderr); return None
    try: return json.loads(m.group(0))
    except Exception as e: print("bad JSON:", e, out[:400], file=sys.stderr); return None

def evaluate(res, skills):
    ok = {"continuity": [c for c in (res.get("continuity") or []) if isinstance(c, str) and 12 < len(c) < 300][:8], "skills": [], "bot": None, "loop": None}
    have = {n: toks(b) for n, b in skills.items()}
    for s in (res.get("skills") or [])[:MAX_SKILLS * 2]:
        if not isinstance(s, dict) or len(s.get("evidence") or []) < MIN_EVIDENCE: continue
        n = slug(s.get("name", "")); body = toks(s.get("body", "") + s.get("description", ""))
        if n in have: continue
        dup = any(len(body & hb) / max(1, len(body | hb)) >= .6 for hb in have.values())
        if dup: continue
        ok["skills"].append({**s, "name": n})
        if len(ok["skills"]) >= MAX_SKILLS: break
    b = res.get("bot")
    if isinstance(b, dict):
        names = set(b.get("skills") or []); pool = set(skills) | {s["name"] for s in ok["skills"]}
        if len(names & pool) >= BOT_MIN_SKILLS: ok["bot"] = {**b, "name": slug(b.get("name", ""))}
    l = res.get("loop")
    if isinstance(l, dict) and ok["bot"] and slug(l.get("agent", "")) == ok["bot"]["name"]: ok["loop"] = {**l, "name": slug(l.get("name", ""))}
    return ok

def apply(topic, t: Path, ok, blocks):
    date = time.strftime("%Y-%m-%d %H:%M"); made = []
    def add_queue(kind, line):
        q = t / ".system/queue.md"; s = q.read_text() if q.exists() else f"# Queue — {topic}\n"
        hdr = f"## [{kind}]"
        if hdr not in s: s += f"\n{hdr}\n"
        i = s.index(hdr) + len(hdr); s = s[:i] + f"\n- [ ] {line}" + s[i:]
        q.write_text(s)
    def inject(line):
        p = t / ".system/injections.md"; s = p.read_text() if p.exists() else f"# Injections — {topic}\n\n## [UNREAD]\n\n## [READ]\n"
        s = s.replace("## [UNREAD]\n", f"## [UNREAD]\n{line}\n", 1); p.write_text(s)
    if ok["continuity"]:
        c = t / ".system/continuity.md"; s = c.read_text() if c.exists() else f"# Continuity — {topic}\n"
        c.write_text(s.rstrip() + f"\n\n## learned {date} (worker, from {len(blocks)} inbox blocks)\n" + "\n".join(f"- {x}" for x in ok["continuity"]) + "\n")
        made.append("continuity"); stage("edit", topic=topic, text="continuity: " + ok["continuity"][0][:180])
    for s in ok["skills"]:
        # 2026-09-05 (Chris): "These are the things that I don't want to have to give approval on" — skills and wiki edits AUTO-APPLY.
        # A skill is just markdown in the topic; Chris can edit or delete it in the wiki. Only bots and loops stay .proposed.
        p = t / "skills" / s["name"] / "SKILL.md"; p.parent.mkdir(parents=True, exist_ok=True)
        ev = "\n".join(f"> {e}" for e in s["evidence"])
        p.write_text(f"---\nname: {s['name']}\ndescription: {s['description']}\nversion: 0.1.0\ndistilled: {date}\ntopic: {topic}\n---\n# {s['name']}\n{s['body'].strip()}\n\n## Evidence\n{ev}\n")
        add_queue("SKILLS", f"{s['name']} — distilled {date} → skills/{s['name']}/SKILL.md (auto-applied; edit or delete freely)")
        inject(f"[SKILLS] new skill `{s['name']}` in {topic}: {s['description']}")
        post(f"SKILL · `{s['name']}` distilled into {topic} — {s['description'][:120]}", "done", f"topics/{topic}/skills/{s['name']}/SKILL.md")
        stage("edit", topic=topic, text=f"+ skill {s['name']}: {s['description'][:140]}"); made.append("skill:" + s["name"])
    b = ok["bot"]
    if b:
        p = t / "agents" / f"{b['name']}.md.proposed"; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\ntype: agent\nname: {b['name']}\nproposed: {date}\ntopic: {topic}\nskills: {json.dumps(b.get('skills'))}\n---\n# {b['name']}\n{b.get('role','')}\n\n## Why a separate intelligence\n{b.get('why','')}\n\n## SOUL.md (draft)\n{b.get('soul','')}\n")
        add_queue("AGENTS", f"{b['name']} — PROPOSED {date} → agents/{b['name']}.md.proposed (approve → hermes profile create via klerik)")
        inject(f"[AGENTS] proposed bot `{b['name']}` for {topic}: {b.get('role','')}")
        post(f"PROPOSAL · bot `{b['name']}` for {topic} — {b.get('role','')[:120]}", "needs_chris", f"topics/{topic}/agents/{b['name']}.md.proposed"); made.append("bot:" + b["name"])
    l = ok["loop"]
    if l:
        p = t / "loops" / f"{l['name']}.md.proposed"; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\ntype: loop\nname: {l['name']}\nproposed: {date}\n---\n# {l['name']}\nowner: {l.get('agent')} · cadence: {l.get('cadence')} · status: PROPOSED\n{l.get('why','')}\n\n## Prompt\n{l.get('prompt','')}\n")
        add_queue("LOOPS", f"{l['name']} — PROPOSED {date} → loops/{l['name']}.md.proposed (approve → hermes cron create)")
        inject(f"[LOOPS] proposed loop `{l['name']}` ({l.get('cadence')}) for {topic}")
        post(f"PROPOSAL · loop `{l['name']}` every {l.get('cadence')} for {topic}", "needs_chris", f"topics/{topic}/loops/{l['name']}.md.proposed"); made.append("loop:" + l["name"])
    return made

def promote_proposed_skills():
    """policy change 2026-09-05: skills no longer need approval → any SKILL.md.proposed becomes SKILL.md."""
    for p in VAULT.glob("topics/*/skills/*/SKILL.md.proposed"):
        p.rename(p.with_name("SKILL.md")); print("promoted", p.parent.name)

def run(topic, dry=False):
    t = VAULT / "topics" / topic
    lock = t / ".system/worker.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < 1200: print(topic, "locked"); return
    lock.parent.mkdir(parents=True, exist_ok=True); lock.write_text(str(os.getpid()))
    try:
        blocks, last = collect(t)
        if not blocks: print(topic, "nothing new"); return
        cont = (t / ".system/continuity.md").read_text() if (t / ".system/continuity.md").exists() else ""
        skills = existing_skills(t)
        post(f"WORKER {topic} · distilling {len(blocks)} new inbox blocks", "working", f"topics/{topic}/.system/inbox.md")
        res = generate(topic, blocks, cont, skills, dry)
        if dry or res is None:
            if res is None and not dry: post(f"WORKER {topic} · bot returned no usable JSON — skipped", "blocked")
            return
        ok = evaluate(res, skills); made = apply(topic, t, ok, blocks)
        (t / ".system/worker.cursor").write_text(last)
        with (VAULT / "log.md").open("a") as f: f.write(f"{time.strftime('%Y-%m-%d %H:%M')}: topic-worker {topic} · {len(blocks)} blocks → {', '.join(made) or 'no proposals'}\n")
        post(f"WORKER {topic} · done — {', '.join(made) or 'no proposals (evidence too thin)'}", "done")
        print(topic, made)
    finally:
        lock.unlink(missing_ok=True)

if __name__ == "__main__":
    promote_proposed_skills()
    a = sys.argv[1:]; dry = "--dry" in a; a = [x for x in a if not x.startswith("--")]
    if "--all" in sys.argv:
        for t in sorted((VAULT / "topics").iterdir()):
            if t.is_dir() and not t.name.startswith("_") and (t / ".system/inbox.md").exists(): run(t.name, dry)
    else: run(a[0], dry)
