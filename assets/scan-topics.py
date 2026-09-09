#!/usr/bin/env python3
"""scan-topics.py — the UNIFIED live scan (item Y, v14.48): snapshots topics + bots + skills into .system-live.json.

vault-live.html has NO baked collections any more: one `loadLive()` reads this file (via the senter-bridge
GET /file) and every view — WIKI rows' hover cards, SKILLS, BOTS, loops, the model picker — renders from it.
The integrations key is written by assets/scan-integrations.py (slow: shells out to hermes) and is PRESERVED here.

Keys written:
  "topics": { "<t>": { "summary": [<=6 lines], "skills": [name…], "bots": [{"name","role"}…],
                       "loops": [{"name","cadence"}…], "updated": iso } }
  "bots":   [ {"name","role","desc","model","skills","color","avatar":bool}… ]   — every ~/.hermes/profiles/<p>/ WITH a SOUL.md
  "skills": [ {"name","cat","desc","profiles":[…],"path"}… ]                      — union of ~/.hermes/skills + profiles/*/skills
  "scanned": iso, "counts": {...}

Usage:
  scan-topics.py            one pass, write
  scan-topics.py --dry      one pass, print only
  scan-topics.py --watch [SECS]   EVENT-DRIVEN (AG, v14.53): filesystem watch on ~/.hermes/profiles, ~/.hermes/skills and
                            topics/ via `watchdog` (FSEvents on macOS; installed in the hermes venv). A change → 250ms
                            debounce → rescan → if the snapshot differs: rewrite the JSON AND append
                            {"kind":"fleet","phase":"changed","what":[bots|skills|topics…]} to ~/.hermes/senter-bridge/events.jsonl,
                            so the bridge's SSE tail pushes it to the wiki (< 2s end-to-end; the page has NO timers).
                            // fallback: if `watchdog` is not importable, polls every SECS (default 20) — the ONLY clock, and it
                            names itself on stdout ("poll fallback").
Run with the hermes venv python (watchdog); any python3 works for one-shot / poll fallback.
"""
import glob, json, os, re, sys, time
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"
OUT = VAULT / ".system-live.json"
TOPICS = VAULT / "topics"
HERMES = Path.home() / ".hermes"
EVENTS = HERMES / "senter-bridge" / "events.jsonl"
WATCH_ROOTS = [HERMES / "profiles", HERMES / "skills", TOPICS]   # bots+skills, default skills, topics (skills/agents/loops dirs + READMEs)
COLORS = {"turbosovth": "#9ece6a", "klerik": "#b4f9f8", "senter": "#e0af68", "anser": "#c0caf5",
          "teknium": "#f7768e", "dogeman": "#bb9af7", "paladin": "#ff9e64", "weaver": "#7dcfff"}
PALETTE = ["#c0caf5", "#9ece6a", "#e0af68", "#bb9af7", "#7aa2f7", "#f7768e", "#ff9e64", "#7dcfff", "#b4f9f8"]

def strip_front(text):
    if text.startswith("---"):
        m = re.match(r"^---\n.*?\n---\n", text, re.S)
        if m: return text[m.end():]
    return text

def frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def summary(readme, n=6):
    out = []
    for ln in strip_front(readme).splitlines():
        s = ln.strip()
        if not s or s.startswith("<!--"): continue
        s = re.sub(r"^#+\s*", "", s)              # headings → plain
        s = re.sub(r"^>\s*", "", s)               # blockquote
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)    # bold
        s = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", s)  # links → text
        s = s.replace("`", "")
        if s.lower() in ("facts",): continue
        out.append(s[:160])
        if len(out) >= n: break
    return out

def name_of(p):
    return p.stem if p.is_file() else p.name

def cadence(md):
    m = re.search(r"(?im)^\s*(?:\*\*)?(?:schedule|cadence|every|runs)(?:\*\*)?\s*:\s*(.+)$", md)
    if m: return m.group(1).strip().strip("*`")[:80]
    m = re.search(r"`((?:[\d*/,-]+\s+){4}[\d*/,-]+)`", md)  # a cron line
    if m: return m.group(1)
    return ""

def role(md):
    body = strip_front(md)
    m = re.search(r"(?im)^\s*(?:role|description)\s*:\s*(.+)$", md)
    if m: return m.group(1).strip()[:120]
    for ln in body.splitlines():
        s = ln.strip()
        if s and not s.startswith("#"): return re.sub(r"[*_`>]", "", s)[:120]
    return ""

def soul_role(md):
    """First PARAGRAPH of SOUL.md after the title (frontmatter description wins) — the bot's role line."""
    fm = frontmatter(md)
    if fm.get("description"): return fm["description"][:220]
    para, body = [], strip_front(md)
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith("#") or s.startswith("|") or s.startswith("<!--"):
            if para: break
            continue
        if not s:
            if para: break
            continue
        para.append(re.sub(r"[*_`>]", "", s))
    return " ".join(para)[:220]

def repos_of(readme):
    """Repo names for a topic's README: frontmatter `repo:` + `## Repos` table rows + absorbed-topic rows."""
    repos = []
    if not readme: return repos
    fm = frontmatter(readme)
    if fm.get("repo"): repos.append(fm["repo"].rstrip("/").rsplit("/", 1)[-1])
    for m in re.finditer(r"(?ms)^## Repos\s*\n(.*?)(?=^## |\Z)", readme):
        for ln in m.group(1).splitlines():
            mm = re.search(r"github\.com/[^/\s]+/([^/\s|)]+)", ln) or re.search(r"\|\s*([a-z0-9._-]+)\s*\|", ln)
            if mm and mm.group(1).strip("-") : repos.append(mm.group(1))  # skip the |---|---| divider row
    for m in re.finditer(r"(?m)^- \[\[topics/_archive/([^/|\]]+)/README", readme):
        repos.append(m.group(1))  # absorbed topics count as repos too (pocket-shop-pricing etc.)
    out, seen = [], set()
    for r in repos:
        k = r.lower()
        if k in seen: continue
        seen.add(k); out.append(r)
    return out

def scan_topics():
    topics = {}
    if not TOPICS.is_dir(): return topics
    for d in sorted(TOPICS.iterdir()):
        if not d.is_dir() or d.name.startswith((".", "_")): continue
        readme = (d / "README.md")
        rd = readme.read_text(errors="replace") if readme.is_file() else ""
        skills = sorted(name_of(p) for p in (d / "skills").iterdir()) if (d / "skills").is_dir() else []
        skills = [s for s in skills if not s.startswith(".")]
        bots = []
        if (d / "agents").is_dir():
            for p in sorted((d / "agents").iterdir()):
                if p.name.startswith("."): continue
                md = p.read_text(errors="replace") if p.is_file() else ((p / "README.md").read_text(errors="replace") if (p / "README.md").is_file() else "")
                bots.append({"name": name_of(p), "role": role(md)})
        loops = []; seen = set()
        if (d / "loops").is_dir():
            for p in sorted((d / "loops").iterdir(), key=lambda p: (p.is_dir(), p.name)):  # reflect.md wins over reflect/ (run dir)
                if p.name.startswith(".") or name_of(p) in seen: continue
                seen.add(name_of(p))
                md = p.read_text(errors="replace") if p.is_file() else ((p / "README.md").read_text(errors="replace") if (p / "README.md").is_file() else "")
                loops.append({"name": name_of(p), "cadence": cadence(md)})
        # 2026-09-03 (Chris): "consider the context of the ENTIRE topic … the entire file for each one of them" → the full README plus
        # the topic's .system knowledge files (concept/rules/context/continuity — the durable ones, not session/queue logs which are
        # huge and churn), capped so the snapshot stays small enough for the page.
        sys_dir = d / ".system"; extra = ""
        for fn in ("concept.md", "rules.md", "context.md", "continuity.md", "hermes-native-map.md"):
            f = sys_dir / fn
            if f.is_file():
                extra += "\n\n## " + fn + "\n" + f.read_text(errors="replace")
        # 2026-09-05 (Chris): "the context section should be entire thorough wikis on each individual thing" — a topic is an LLM wiki
        # (assets/topic-wiki.py). `wiki_index` = index.md verbatim (rendered as the row's CONTEXT), `wiki_pages` = count, corpus adds pages.
        idx = d / "index.md"; wiki_index = idx.read_text(errors="replace") if idx.is_file() else ""
        pages = sorted((d / "wiki").rglob("*.md")) if (d / "wiki").is_dir() else []
        wiki_text = "".join("\n\n## " + str(p.relative_to(d)) + "\n" + p.read_text(errors="replace")[:6000] for p in pages[:60])
        full = rd + extra + "\n\n" + wiki_index + wiki_text
        topics[d.name] = {"summary": summary(rd), "skills": skills, "bots": bots, "loops": loops, "repos": repos_of(rd), "text": full[:120000],
                          "wiki_index": wiki_index[:30000], "wiki_pages": len(pages),
                          "raw_items": (len(list((d / "raw").rglob("*"))) if (d / "raw").is_dir() else 0)}  # 40k: senter hit the 20k cap once the .system knowledge files were folded in (2026-09-04)
    return topics

def scan_bots():
    """Every ~/.hermes/profiles/<p>/ that has a SOUL.md is a bot. No SOUL → not a bot (scratch dirs are skipped)."""
    bots = []
    for p in sorted((HERMES / "profiles").glob("*/")) if (HERMES / "profiles").is_dir() else []:
        soul = p / "SOUL.md"
        if not p.is_dir() or not soul.is_file(): continue
        name = p.name
        md = soul.read_text(errors="replace")
        model = ""
        cfg = p / "config.yaml"
        if cfg.is_file():
            m = re.search(r"^model:\s*\n(?:[ \t]+.*\n)*?[ \t]+default:\s*([^\n#]+)", cfg.read_text(errors="replace"), re.M)
            if m: model = m.group(1).strip().strip('"')
        nskills = len(glob.glob(str(p / "skills" / "**" / "SKILL.md"), recursive=True))
        r = soul_role(md)
        bots.append({"name": name, "role": r, "desc": r, "model": model, "skills": nskills, "text": md[:12000],  # full SOUL for context similarity
                     "color": COLORS.get(name) or PALETTE[sum(map(ord, name)) % len(PALETTE)],
                     "avatar": (VAULT / "assets" / "avatars" / f"{name}.png").is_file(),
                     "agents_md": (p / "AGENTS.md").is_file()})
    return bots

def scan_skills():
    roots = [("default", HERMES / "skills")]
    for p in sorted((HERMES / "profiles").glob("*/")):
        if (p / "skills").is_dir(): roots.append((p.name, p / "skills"))
    # 2026-09-05: topics/<t>/skills/ is the agent-wiki spec's home for skills ("skills scoped to this topic") — first-class rows,
    # owner = the topic (prefixed "topic:" so the profiles list stays honest). Was never scanned before → topic skills were invisible.
    for tp in sorted(TOPICS.glob("*/skills")):
        if tp.is_dir() and not tp.parent.name.startswith("_"): roots.append(("topic:" + tp.parent.name, tp))
    skills = {}
    for owner, root in roots:
        if not root.is_dir(): continue
        # 2026-09-05 (Chris): "skills and bots and loops getting proposed all the time" — topic-worker writes SKILL.md.proposed;
        # they are first-class rows flagged proposed=True until Chris approves (drops the suffix) or deletes.
        for f in (Path(x) for x in glob.glob(str(root / "**" / "SKILL.md"), recursive=True) + glob.glob(str(root / "**" / "SKILL.md.proposed"), recursive=True)):  # glob.glob follows symlinked dirs (pathlib.glob does not → the `turbofit` plugin symlink was invisible; V)
            rel = f.parent.relative_to(root).parts
            name = rel[-1] if rel else root.name
            cat = "/".join(rel[:-1])
            body = f.read_text(errors="replace"); fm = frontmatter(body)
            s = skills.setdefault(name, {"name": name, "cat": cat, "desc": fm.get("description", ""), "profiles": [],
                                         "path": "/".join(rel), "text": body[:8000], "proposed": f.name.endswith(".proposed"),
                                         "file": str(f)})  # full SKILL.md for context similarity
            if owner not in s["profiles"]: s["profiles"].append(owner)
            if not s["desc"] and fm.get("description"): s["desc"] = fm["description"]
    return sorted(skills.values(), key=lambda s: (s["cat"], s["name"]))

def scan_vault_agents(bots):
    """2026-09-05: topics/<t>/agents/<a>.md(.proposed) — the spec's Agents primitive. A proposed bot is a BOT row flagged proposed
    until Chris approves (→ hermes profile create via klerik) or deletes."""
    have = {b["name"].lower() for b in bots}
    for md in sorted(list(VAULT.glob("topics/*/agents/*.md")) + list(VAULT.glob("topics/*/agents/*.md.proposed"))):
        if md.name.lower().startswith("readme") or md.parent.parent.name.startswith("_"): continue
        name = md.name.split(".md")[0]
        if name.lower() in have: continue
        try: txt = md.read_text(errors="replace")
        except Exception: continue
        fm = frontmatter(txt); role = re.search(r"^#\s*.+\n+(.+)$", txt, re.M)
        bots.append({"name": name, "role": (role.group(1).strip() if role else fm.get("role", ""))[:300], "text": txt[:8000], "skills": [],
                     "topic": md.parent.parent.name, "path": str(md.relative_to(VAULT)), "proposed": md.name.endswith(".proposed"), "source": "vault"})
        have.add(name.lower())
    return bots

def scan_loops():
    """LOOPS (Chris 2026-09-03: "Loops should show all of the Crons/WebHooks, and other ways to automate the Bots and what Bots are in automating").
    Sources: ~/.hermes/cron/jobs.json (default profile) + ~/.hermes/profiles/<p>/cron/jobs.json. A loop = one scheduled job; `bot` = the profile
    that runs it (the automated bot); `targets` = other bots named in the job's name/prompt (what it automates)."""
    loops = []
    files = [(HERMES / "cron" / "jobs.json", "default")]
    for p in sorted((HERMES / "profiles").glob("*/")) if (HERMES / "profiles").is_dir() else []:
        if (p / "cron" / "jobs.json").is_file(): files.append((p / "cron" / "jobs.json", p.name))
    known = {p.name for p in (HERMES / "profiles").glob("*/")} if (HERMES / "profiles").is_dir() else set()
    for f, prof in files:
        try: d = json.loads(f.read_text(errors="replace"))
        except Exception: continue
        for j in (d.get("jobs") if isinstance(d, dict) else d) or []:
            if not isinstance(j, dict): continue
            sch = j.get("schedule") or {}
            cadence = (sch.get("display") if isinstance(sch, dict) else str(sch)) or j.get("schedule_display") or ""
            text = f"{j.get('name','')} {j.get('prompt','') or ''}"
            targets = sorted({b for b in known if b != prof and re.search(rf"\b{re.escape(b)}\b", text, re.I)})
            loops.append({"name": j.get("name") or j.get("id") or "loop", "id": j.get("id"), "bot": prof, "cadence": cadence,
                          "kind": (sch.get("kind") if isinstance(sch, dict) else "cron") or "cron", "enabled": bool(j.get("enabled", True)),
                          "script": bool(j.get("script")), "no_agent": bool(j.get("no_agent")), "targets": targets,
                          "desc": (j.get("prompt") or j.get("script") or "").strip()[:400], "deliver": j.get("deliver") or "",
                          "source": "cron"})
    # 2026-09-04 (Chris): "see what of Hermes we can squeeze into each lane — topics, skills, bots, loops". Vault-defined loops
    # (topics/<t>/loops/*.md — the agent-wiki spec's Loops primitive: "cron jobs and workflows that run over time") are LOOP rows too,
    # whether or not a cron is registered yet. `bot` = "(owner: <bot>" in the H1 if present; cadence = "## Cadence" first line; status line kept.
    seen = {l["name"].lower() for l in loops}
    for md in sorted(list(VAULT.glob("topics/*/loops/*.md")) + list(VAULT.glob("topics/*/loops/*.md.proposed"))):  # .proposed = topic-worker proposal (2026-09-05)
        if md.parent.parent.name.startswith("_"): continue
        try: txt = md.read_text(errors="replace")
        except Exception: continue
        h1 = re.search(r"^#\s*(?:Loop:\s*)?(.+)$", txt, re.M)
        name = (h1.group(1) if h1 else md.stem).split("(")[0].strip() or md.stem
        if name.lower() in seen: continue
        own = re.search(r"owner:\s*([a-z0-9_-]+)", txt, re.I)
        cad = re.search(r"^##\s*Cadence\s*\n+(.+)$", txt, re.M)
        st = re.search(r"^##\s*Status\s*\n+(.+)$", txt, re.M)
        text = txt
        targets = sorted({b for b in known if re.search(rf"\b{re.escape(b)}\b", text, re.I) and (not own or b != own.group(1).lower())})
        loops.append({"name": name, "id": None, "bot": (own.group(1).lower() if own else md.parent.parent.name), "cadence": (cad.group(1).strip() if cad else ""),
                      "kind": "vault", "enabled": not bool(st and "QUEUED" in st.group(1)), "script": False, "no_agent": False, "targets": targets,
                      "desc": txt.strip()[:400], "deliver": "", "source": "vault", "topic": md.parent.parent.name, "path": str(md.relative_to(VAULT)),
                      "status": (st.group(1).strip() if st else ""), "proposed": md.name.endswith(".proposed")})
        seen.add(name.lower())
    return loops

def scan_usage(topics, bots, skills, days=98):
    """2026-09-03 (Chris): "a usage chart like the GitHub usage chart … almost like a diffusion map" in every row. One number per DAY per item =
    how many Hermes messages that day mentioned it (state.db messages_fts, all sessions). 98 days = 14 weeks × 7, oldest→newest."""
    import sqlite3, datetime
    db = HERMES / "state.db"
    out = {"days": days, "end": datetime.date.today().isoformat(), "topics": {}, "bots": {}, "skills": {}}
    if not db.is_file(): return out
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        since = (datetime.date.today() - datetime.timedelta(days=days - 1)).isoformat()
        def series(term):
            q = '"' + term.replace('"', '') + '"'
            rows = con.execute("select date(m.timestamp,'unixepoch','localtime') d, count(*) from messages m "
                               "where m.rowid in (select rowid from messages_fts where messages_fts match ?) and d >= ? group by d", (q, since)).fetchall()
            by = dict(rows); base = datetime.date.fromisoformat(since)
            return [by.get((base + datetime.timedelta(days=i)).isoformat(), 0) for i in range(days)]
        for n in topics: out["topics"][n] = series(n)
        for b in bots: out["bots"][b["name"]] = series(b["name"])
        for s in skills: out["skills"][s["name"]] = series(s["name"])
        con.close()
    except Exception as e:
        out["error"] = str(e)
    return out

def snapshot():
    t, b, s = scan_topics(), scan_vault_agents(scan_bots()), scan_skills()
    lp = scan_loops()
    # 2026-09-05 (Chris): the wiki is Hermes's MEMORY LAYER; the side chat reads it by progressive disclosure. Every scan
    # refreshes topics/<t>/.system/INDEX.md (1 line per file + H2 outline with line numbers) so an agent goes
    # row → INDEX → file → section without loading the whole topic. Cheap (text only), so it runs on every pass.
    try:
        import subprocess, sys as _sys
        subprocess.run([_sys.executable, str(VAULT / "assets" / "build-index.py")], capture_output=True, timeout=60)
    except Exception: pass
    return {"topics": t, "bots": b, "skills": s, "loops": lp, "usage": scan_usage(t, b, s),
            "counts": {"topics": len(t), "bots": len(b), "skills": len(s), "loops": len(lp)}}

def write(snap):
    live = {}
    if OUT.exists():
        try: live = json.loads(OUT.read_text())
        except Exception: live = {}
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    for k, v in snap["topics"].items(): v["updated"] = now
    live.update(snap); live["scanned"] = now
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(live, ensure_ascii=False, indent=2)); os.replace(tmp, OUT)  # atomic: the bridge never serves a half-written file
    return live

def emit_changed(snap, delta, what=None):
    try:
        EVENTS.parent.mkdir(parents=True, exist_ok=True)
        with open(EVENTS, "a") as f:
            f.write(json.dumps({"ts": time.time(), "bot": "senter", "kind": "fleet", "phase": "changed",
                                "summary": "fleet changed · " + delta, "counts": snap["counts"],
                                "what": what or ["topics", "bots", "skills"]}) + "\n")
    except Exception as e:
        print("emit failed:", e, file=sys.stderr)

def diff_what(prev, cur):
    """Which collections changed between two snapshots → the `what` list the wiki uses to re-render only that view."""
    return [k for k in ("topics", "bots", "skills", "loops", "usage") if json.dumps(prev.get(k), sort_keys=True) != json.dumps(cur.get(k), sort_keys=True)]

def on_change(prev_snap, snap):
    what = diff_what(prev_snap, snap)
    pb, cb = {x["name"] for x in prev_snap["bots"]}, {x["name"] for x in snap["bots"]}
    delta = " ".join(["+" + n for n in sorted(cb - pb)] + ["-" + n for n in sorted(pb - cb)]) or "/".join(what or ["topics/skills"])
    write(json.loads(json.dumps(snap))); emit_changed(snap, delta, what)   # write() stamps topics[*].updated on its arg — hand it a copy so `prev` stays comparable
    print(time.strftime("%H:%M:%S"), "changed", delta, "what=", what, "·", describe(snap), flush=True)

def watch_events(prev_snap, debounce=0.25):
    """AG: filesystem events → rescan. Returns False if watchdog is unavailable (caller falls back to polling)."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except Exception:
        return False
    import threading
    lock = threading.Lock(); pending = {"t": None}
    state = {"prev": prev_snap}
    def rescan():
        with lock:
            pending["t"] = None
        snap = snapshot()
        if json.dumps(snap, sort_keys=True) != json.dumps(state["prev"], sort_keys=True):
            on_change(state["prev"], snap); state["prev"] = snap
    class H(FileSystemEventHandler):
        def on_any_event(self, ev):
            p = getattr(ev, "src_path", "") or ""
            if "/.system/" in p or p.endswith((".tmp", ".swp", "~")) or "/__pycache__/" in p or "/.git/" in p: return
            with lock:
                if pending["t"]: pending["t"].cancel()
                pending["t"] = threading.Timer(debounce, rescan); pending["t"].daemon = True; pending["t"].start()
    obs = Observer()
    n = 0
    for r in WATCH_ROOTS:
        if r.is_dir(): obs.schedule(H(), str(r), recursive=True); n += 1
    obs.start()
    print("watch (fs events via watchdog) roots=", n, "·", describe(prev_snap), flush=True)
    try:
        while True: time.sleep(3600)   # the thread only sleeps; all work is event-driven
    except KeyboardInterrupt:
        obs.stop()
    obs.join()
    return True

def describe(snap):
    b = ", ".join(x["name"] for x in snap["bots"])
    return f"topics={snap['counts']['topics']} bots={snap['counts']['bots']} [{b}] skills={snap['counts']['skills']}"

if __name__ == "__main__":
    if "--watch" in sys.argv:
        i = sys.argv.index("--watch"); secs = int(sys.argv[i + 1]) if len(sys.argv) > i + 1 and sys.argv[i + 1].isdigit() else 20
        first = snapshot(); write(json.loads(json.dumps(first)))
        if "--poll" not in sys.argv and watch_events(first):
            sys.exit(0)
        # fallback: poll every SECS — only when `watchdog` is missing (or --poll forced). Names itself so nobody mistakes it for the live path.
        prev = json.dumps(first, sort_keys=True); print("watch · POLL FALLBACK (no watchdog)", secs, "s ·", describe(first), flush=True)
        while True:
            time.sleep(secs)
            snap = snapshot(); cur = json.dumps(snap, sort_keys=True)
            if cur != prev:
                on_change(json.loads(prev), snap); prev = cur
        sys.exit(0)
    snap = snapshot()
    print(describe(snap))
    for k, v in snap["topics"].items():
        if v["skills"] or v["bots"] or v["loops"]:
            print(f"  {k:<24} skills={v['skills']} bots={[b['name'] for b in v['bots']]} loops={[(l['name'], l['cadence']) for l in v['loops']]}")
    for b in snap["bots"]:
        print(f"  BOT {b['name']:<12} {b['model']:<36} skills={b['skills']:<3} pet={'yes' if b['avatar'] else 'no '} role={b['role'][:70]!r}")
    if "--dry" in sys.argv: sys.exit(0)
    live = write(snap)
    if "--emit" in sys.argv: emit_changed(snap, "rescan")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, keys={list(live.keys())})")
