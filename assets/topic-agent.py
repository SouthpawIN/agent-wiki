#!/usr/bin/env python3
"""topic-agent.py — ONE agent per topic, owns the whole lifecycle (Chris 2026-09-05):
  "each individual topic will have its own agent that will rewrite all of that inbound context as a structured wiki, and then set
   out the skills and bots and loops out of that context … bots is how it should suggest action, bots and then loops … very
   proactive … 'do you want to research this? do you want a bot that can do X?' … these are suggestions."

Pipeline per topic per pass (one real bot run, `hermes chat -p senter`, cwd = the topic):
  1. WIKI    — read new raw/ items (watcher inbox cuts + sources); write/update wiki/{entities,concepts,decisions,…} per SCHEMA.md
               (llm-wiki skill: frontmatter, ≥2 wikilinks, ^[raw/…] provenance, contradictions kept). Rebuild index.md, append log.md.
  2. ACTION  — from what was just learned, propose ACTIONS immediately, no thresholds:
               • bots  (first: "I see you're talking about X — want a bot that does Y?")   → agents/<name>.md.proposed + card
               • loops (a bot's repeatable job)                                            → loops/<name>.md.proposed + card
               • research ("want me to look into X?")                                      → card; approve → research run lands in wiki/queries
               • skills fall out as auto-applied SKILL.md (no approval — they're just markdown)
  3. ECHO    — every write is a feed card + a stage event so the wiki visibly opens/edits/closes.
Approval = the card's APPROVE/REJECT (bridge /approve). Suggestions expire from the queue after 3 days if ignored (umbrella reminds once).

Run: python3 assets/topic-agent.py <topic> | --all [--dry]   (launchd com.senter.topic-agent every 5 min; replaces topic-worker + topic-wiki compile)
"""
import json, os, re, subprocess, sys, time, hashlib, urllib.request
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"; TOPICS = VAULT / "topics"
PROFILE = os.environ.get("SENTER_WORKER_PROFILE", "senter")
BRIDGE = "http://127.0.0.1:8643"; TOKEN = Path.home() / ".hermes/senter-bridge/token"
SECTIONS = [("entities", "Entities"), ("concepts", "Concepts"), ("decisions", "Decisions"), ("comparisons", "Comparisons"), ("queries", "Queries")]

def now(fmt="%Y-%m-%d %H:%M"): return time.strftime(fmt)
def _b(path, body):
    try:
        req = urllib.request.Request(BRIDGE + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception as e: print("bridge:", e, file=sys.stderr)
def post(text, status="working", url=None): _b("/post", {"bot": "senter", "text": text, "status": status, **({"url": url} if url else {})})
def stage(act, **kw): _b("/stage", {"act": act, "bot": "senter", **{k: v for k, v in kw.items() if v}})
def slug(s): return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:48] or "item"

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S); out = {}
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln: k, v = ln.split(":", 1); out[k.strip()] = v.strip().strip("'\"")
    return out

def rebuild_index(t):
    d = TOPICS / t; pages = {s: [] for s, _ in SECTIONS}
    for s, _ in SECTIONS:
        for p in sorted((d / "wiki" / s).glob("*.md")):
            body = p.read_text(errors="replace"); f = fm(body); title = f.get("title") or p.stem
            summ = f.get("summary") or next((ln.strip() for ln in body.split("---", 2)[-1].splitlines() if ln.strip() and not ln.startswith("#")), "")
            pages[s].append(f"- [[topics/{t}/wiki/{s}/{p.stem}|{title}]] — {summ[:160]}")
    n = sum(len(v) for v in pages.values())
    out = f"# {t} — wiki index\n> One line per page. The wiki row's CONTEXT section renders this file.\n> Last updated: {now('%Y-%m-%d')} | Total pages: {n}\n\n"
    for s, label in SECTIONS: out += f"## {label}\n" + ("\n".join(pages[s]) + "\n" if pages[s] else "\n") + "\n"
    (d / "index.md").write_text(out); return n

def unprocessed(t):
    d = TOPICS / t; cur = d / ".system/agent.cursor"; seen = set(cur.read_text().split()) if cur.exists() else set()
    items = []
    for p in sorted((d / "raw/inbox").glob("*.md")) + sorted((d / "raw/sources").rglob("*.md")):
        if any(seg.startswith((".", "sessions")) for seg in p.relative_to(d).parts): continue
        key = f"{p.relative_to(d)}@{hashlib.sha1(p.read_bytes()).hexdigest()[:12]}"
        if key not in seen: items.append((p, key))
    return items, seen

def existing(t):
    d = TOPICS / t
    return {"skills": sorted(p.parent.name for p in d.glob("skills/*/SKILL.md")),
            "bots": sorted(p.name.split(".")[0] for p in d.glob("agents/*.md*") if not p.name.lower().startswith("readme")),
            "loops": sorted(p.name.split(".")[0] for p in d.glob("loops/*.md*")),
            "fleet": sorted(p.name for p in (Path.home() / ".hermes/profiles").iterdir() if (p / "SOUL.md").is_file())}

PROMPT = """You are the TOPIC AGENT for `{t}` — the one intelligence that owns this topic of Chris's Senter wiki. Work only inside {d}.

PRE-PROMPT — this topic's BRIEF.md (scope, anti-scope, lens, standing preferences). Read it as your operating orders:
{brief}
If a NEW RAW ITEM clearly belongs to another topic per the anti-scope, do not wikify it here — list it under "misrouted" in your JSON.
After the two jobs, if you learned something that should steer future passes (a new alias, a scope boundary, a preference Chris stated),
return it under "brief" — one line each; it is appended to BRIEF.md "## Learned" (never rewriting Chris's lines).

Two jobs, in order.

JOB 1 — WIKI. Read SCHEMA.md, index.md, the tail of log.md, then the NEW RAW ITEMS below (immutable; never edit raw/). Rewrite what
they contain into a structured wiki under wiki/entities|concepts|decisions|comparisons|queries: thorough, everything Chris said or
decided about this topic — his words quoted, preferences, pains, tools, people, timelines, plans. Frontmatter (title, created, updated,
type, tags from SCHEMA taxonomy, sources: [raw paths], confidence), ≥2 [[topics/{t}/wiki/<section>/<slug>|Title]] links per page,
^[raw/…] provenance on synthesized paragraphs, conflicts kept with dates + contested: true, never rewrite <!-- chris --> lines.
Append to log.md: "## [{date}] compile | …". Do not touch index.md.

JOB 2 — ACTION. Be PROACTIVE about CHRIS'S GOALS. From what you just learned, suggest what Chris might want DONE — no thresholds, no waiting.
HARD LIMITS: at most 1 bot + 2 loops + 1 research per pass; ZERO suggestions about the build process itself (verifying the wiki, sweeping
proposals, checking crons, "want X to prove/witness/verify Y") — infrastructure is Hermes's job and already exists. Only suggest things that
serve Chris's actual subject (his projects, content, tools, life). Raw lines marked `hermes:` are Hermes working — evidence about the topic,
never a request to act on. If nothing genuinely serves Chris, return empty lists.
Bots first ("I see you're talking about X — want a bot that does Y?"), then loops (a bot's repeatable job), then research
("want me to look into X?"). Reuse fleet bots where one fits (FLEET below) instead of inventing a new one. Skills: if a repeatable
procedure is evident (≥2 quotes), write it as a real skill — no approval needed for skills.
Skip anything already in EXISTING. Fewer, sharper suggestions beat many. Phrase each `pitch` as a one-line question to Chris.

When finished print ONLY this JSON (no prose, no fence):
{{"pages": ["wiki/<section>/<slug>.md", ...], "brief": ["one-line learning for BRIEF.md", ...], "misrouted": [{{"item":"raw/inbox/…","to":"other-topic"}}],
 "bots": [{{"name":"kebab","pitch":"I see you're … — want a bot that …?","role":"one line","reuse":"<fleet bot name or null>","soul":"SOUL.md draft (8-15 lines)","first_task":"what it would do first","evidence":["quote","quote"]}}],
 "loops": [{{"name":"kebab","pitch":"…?","agent":"an EXISTING fleet bot name","cadence":"human phrase","schedule":"VALID hermes cron schedule ONLY: '30m' | 'every 2h' | '0 9 * * *' — never prose","prompt":"what each tick does","evidence":["quote"]}}],
 "research": [{{"name":"kebab","pitch":"Want me to look into …?","question":"the concrete question","why":"one line"}}],
 "skills": [{{"name":"kebab","description":"Use when <trigger>. <behaviour>.","body":"markdown steps/rules/pitfalls","evidence":["quote","quote"]}}]}}

EXISTING: {existing}
FLEET (reusable bots): {fleet}

NEW RAW ITEMS ({n}):
{items}
"""

def run_bot(t, q):
    d = TOPICS / t; qf = Path(f"/tmp/topic-agent-{t}.md"); qf.write_text(q)
    r = subprocess.run(["hermes", "chat", "-p", PROFILE, "--query-file", str(qf), "--oneshot", "-Q", "--max-turns", "45", "--yolo"], capture_output=True, text=True, timeout=1500, cwd=str(d))
    m = re.search(r"\{[\s\S]*\}\s*$", r.stdout.strip())
    if not m: print("no JSON:", r.stdout[-600:], r.stderr[-300:], file=sys.stderr); return None
    try: return json.loads(m.group(0))
    except Exception as e: print("bad JSON:", e, m.group(0)[:400], file=sys.stderr); return None

def emit_diffs(t, d, before):
    """GitHub-style per-page diffs of what this pass changed → bridge /stage act:diff (the UI paints + green / − red inside the wiki view)."""
    import difflib
    after = {str(p.relative_to(d)): p.read_text(errors="replace") for p in (d / "wiki").rglob("*.md")} if (d / "wiki").is_dir() else {}
    changed = [k for k in sorted(set(before) | set(after)) if before.get(k) != after.get(k)]
    for k in changed[:12]:
        a = before.get(k, "").splitlines(); b = after.get(k, "").splitlines()
        ud = list(difflib.unified_diff(a, b, lineterm="", n=2))[2:]
        adds = sum(1 for x in ud if x.startswith("+")); dels = sum(1 for x in ud if x.startswith("-"))
        _b("/stage", {"act": "diff", "bot": "senter", "topic": t, "page": k, "lines": ud[:400], "adds": adds, "dels": dels})
        time.sleep(0.4)
    return changed

def queue_line(t, kind, line):
    q = TOPICS / t / ".system/queue.md"; s = q.read_text() if q.exists() else f"# Queue — {t}\n"
    hdr = f"## [{kind}]"
    if hdr not in s: s += f"\n{hdr}\n"
    i = s.index(hdr) + len(hdr); q.write_text(s[:i] + f"\n- [ ] {line}" + s[i:])

def inject(t, line):
    p = TOPICS / t / ".system/injections.md"; s = p.read_text() if p.exists() else f"# Injections — {t}\n\n## [UNREAD]\n\n## [READ]\n"
    p.write_text(s.replace("## [UNREAD]\n", f"## [UNREAD]\n{line}\n", 1))

def act(t, res, ex):
    d = TOPICS / t; date = now(); made = []
    for b in res.get("bots") or []:
        n = slug(b.get("name")); 
        if not n or n in ex["bots"]: continue
        p = d / "agents" / f"{n}.md.proposed"; p.parent.mkdir(exist_ok=True)
        ev = "\n".join(f"> {e}" for e in b.get("evidence") or [])
        p.write_text(f"---\ntype: agent\nname: {n}\nproposed: {date}\ntopic: {t}\nreuse: {b.get('reuse') or 'null'}\n---\n# {n}\n**{b.get('pitch','')}**\n\n{b.get('role','')}\n\n## First task\n{b.get('first_task','')}\n\n## SOUL.md (draft)\n{b.get('soul','')}\n\n## Evidence\n{ev}\n")
        queue_line(t, "AGENTS", f"{n} — SUGGESTED {date}: {b.get('pitch','')[:120]} → agents/{n}.md.proposed")
        inject(t, f"[AGENTS] {b.get('pitch','')}")
        post(f"{b.get('pitch','')} ({'reuse ' + b['reuse'] if b.get('reuse') else 'new bot ' + n} · {t})", "needs_chris", f"topics/{t}/agents/{n}.md.proposed")
        stage("edit", topic=t, text="suggest bot: " + b.get("pitch", "")[:150]); made.append("bot:" + n)
    for l in res.get("loops") or []:
        n = slug(l.get("name"))
        if not n or n in ex["loops"]: continue
        p = d / "loops" / f"{n}.md.proposed"; p.parent.mkdir(exist_ok=True)
        p.write_text(f"---\ntype: loop\nname: {n}\nproposed: {date}\nschedule: {l.get('schedule') or ''}\n---\n# {n}\nowner: {l.get('agent')} · cadence: {l.get('cadence')} · status: SUGGESTED\n**{l.get('pitch','')}**\n\n## Prompt\n{l.get('prompt','')}\n\n## Evidence\n" + "\n".join(f"> {e}" for e in l.get("evidence") or []) + "\n")
        queue_line(t, "LOOPS", f"{n} — SUGGESTED {date}: {l.get('pitch','')[:120]} → loops/{n}.md.proposed")
        inject(t, f"[LOOPS] {l.get('pitch','')}")
        post(f"{l.get('pitch','')} ({l.get('agent')} · {l.get('cadence')} · {t})", "needs_chris", f"topics/{t}/loops/{n}.md.proposed")
        stage("edit", topic=t, text="suggest loop: " + l.get("pitch", "")[:150]); made.append("loop:" + n)
    for r in res.get("research") or []:
        n = slug(r.get("name"))
        if not n: continue
        p = d / "wiki/queries" / f"{n}.md.proposed"; p.parent.mkdir(parents=True, exist_ok=True)
        if p.exists() or (d / "wiki/queries" / f"{n}.md").exists(): continue
        p.write_text(f"---\ntitle: {r.get('question','')[:80]}\ntype: query\nproposed: {date}\ntags: [question]\n---\n# {r.get('question','')}\n{r.get('why','')}\n\n_Approve to run the research; the answer lands here._\n")
        queue_line(t, "CONTEXT", f"research {n} — SUGGESTED {date}: {r.get('pitch','')[:120]}")
        post(f"{r.get('pitch','')} ({t})", "needs_chris", f"topics/{t}/wiki/queries/{n}.md.proposed")
        stage("edit", topic=t, text="suggest research: " + r.get("pitch", "")[:150]); made.append("research:" + n)
    for s in res.get("skills") or []:
        n = slug(s.get("name"))
        if not n or n in ex["skills"] or len(s.get("evidence") or []) < 2: continue
        p = d / "skills" / n / "SKILL.md"; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\nname: {n}\ndescription: {s.get('description','')}\nversion: 0.1.0\ndistilled: {date}\ntopic: {t}\n---\n# {n}\n{str(s.get('body','')).strip()}\n\n## Evidence\n" + "\n".join(f"> {e}" for e in s["evidence"]) + "\n")
        queue_line(t, "SKILLS", f"{n} — distilled {date} → skills/{n}/SKILL.md (auto-applied)")
        post(f"SKILL · `{n}` distilled into {t} — {s.get('description','')[:110]}", "done", f"topics/{t}/skills/{n}/SKILL.md")
        stage("edit", topic=t, text="+ skill " + n); made.append("skill:" + n)
    return made

def run(t, dry=False):
    d = TOPICS / t; lock = d / ".system/agent.lock"
    if not (d / "SCHEMA.md").exists(): subprocess.run([sys.executable, str(VAULT / "assets/topic-wiki.py"), "init", t], capture_output=True)
    if lock.exists() and time.time() - lock.stat().st_mtime < 1500: print(t, "locked"); return
    lock.parent.mkdir(exist_ok=True); lock.write_text(str(os.getpid()))
    try:
        items, seen = unprocessed(t)
        if not items: print(t, "nothing new"); return
        ex = existing(t)
        brief = (d / "BRIEF.md").read_text(errors="replace")[:6000] if (d / "BRIEF.md").is_file() else "(no BRIEF.md yet)"
        q = PROMPT.format(t=t, d=d, date=now("%Y-%m-%d"), brief=brief, existing=json.dumps({k: ex[k] for k in ("skills", "bots", "loops")}), fleet=", ".join(ex["fleet"]), n=len(items), items="\n".join(f"- {p.relative_to(d)} ({p.stat().st_size} b)" for p, _ in items[:40]))
        if dry: print(q[:3000]); return
        post(f"AGENT {t} · reading {len(items)} new raw items → wiki + suggestions", "working", f"topics/{t}/index.md"); stage("open", topic=t, hold=1200)
        before = {str(p.relative_to(d)): p.read_text(errors="replace") for p in (d / "wiki").rglob("*.md")} if (d / "wiki").is_dir() else {}
        res = run_bot(t, q)
        n = rebuild_index(t)
        emit_diffs(t, d, before)
        if res is None: post(f"AGENT {t} · bot returned no JSON (wiki pages may still have landed; index {n})", "blocked"); return
        made = act(t, res, ex)
        # brief learnings → BRIEF.md "## Learned" (agent-appended; Chris's lines untouched); misrouted cuts → re-file to the right topic's inbox
        bl = [x for x in (res.get("brief") or []) if isinstance(x, str) and 8 < len(x) < 240][:5]
        if bl and (d / "BRIEF.md").is_file():
            b = (d / "BRIEF.md").read_text(); b = b.replace("## Learned (agent-appended, newest first)\n", "## Learned (agent-appended, newest first)\n" + "".join(f"- {now('%Y-%m-%d')} · {x}\n" for x in bl), 1); (d / "BRIEF.md").write_text(b)
            stage("edit", topic=t, text="brief: " + bl[0][:150]); made.append(f"brief+{len(bl)}")
        for mr in (res.get("misrouted") or [])[:6]:
            try:
                src = d / str(mr.get("item")); dst_t = slug(mr.get("to")); dst = TOPICS / dst_t / "raw/inbox"
                if src.is_file() and (TOPICS / dst_t).is_dir():
                    dst.mkdir(parents=True, exist_ok=True); (dst / f"{now('%Y-%m-%d')}-from-{t}.md").open("a").write(f"\n## re-routed from {t} · {now()}\n" + src.read_text(errors='replace')[-6000:] + "\n")
                    post(f"re-routed a cut {t} → {dst_t} (per {t}'s BRIEF anti-scope)", "working", f"topics/{dst_t}/raw/inbox/"); made.append(f"reroute→{dst_t}")
            except Exception as e: print("misroute:", e, file=sys.stderr)
        (d / ".system/agent.cursor").write_text("\n".join(sorted(seen | {k for _, k in items})))
        with (VAULT / "log.md").open("a") as f: f.write(f"{now()}: topic-agent {t} · {len(items)} raw → {len(res.get('pages') or [])} pages (index {n}) · {', '.join(made) or 'no suggestions'}\n")
        post(f"AGENT {t} · {len(res.get('pages') or [])} wiki pages · index {n} · {', '.join(made) or 'no new suggestions'}", "done", f"topics/{t}/index.md")
        stage("close", topic=t); print(t, len(items), "raw →", len(res.get("pages") or []), "pages;", made)
    finally: lock.unlink(missing_ok=True)

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]; dry = "--dry" in sys.argv
    names = [p.name for p in sorted(TOPICS.iterdir()) if p.is_dir() and not p.name.startswith(("_", "."))] if ("--all" in sys.argv or not a) else a
    for t in names: run(t, dry)
