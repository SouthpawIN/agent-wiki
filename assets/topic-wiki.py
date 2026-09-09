#!/usr/bin/env python3
"""topic-wiki.py — make every topic a real LLM Wiki (Karpathy pattern via the `llm-wiki` skill). Chris 2026-09-05:
"the context section should be entire thorough wikis on each individual thing … all of everything collected about that topic
with that user and all of the inputs they put into it … a funnel for all the context for everything the user cares about."

Layout inside topics/<t>/ (additive — existing files stay where they are):
  SCHEMA.md            conventions + tag taxonomy for THIS topic
  index.md             sectioned catalog: one line per wiki page (the CONTEXT section of the row renders this)
  log.md               append-only actions
  raw/                 Layer 1, immutable: sources/ (transcripts, exports, specs), inbox/ (watcher filings per day)
  wiki/                Layer 2, agent-owned: entities/ concepts/ decisions/ comparisons/ queries/
  .system/             machine coordination (unchanged: continuity, queue, injections, INDEX, locks)

Commands
  init <topic>|--all         create SCHEMA/index/log/raw/wiki if missing; move existing .system/{sessions,knowledge} → raw/sources (symlink back)
  compile <topic>            ONE bot run over unprocessed raw/ (inbox + new sources): write/refresh wiki pages (entities/concepts/decisions),
                             cross-link, update index.md + log.md. Provenance markers ^[raw/…]. Never edits raw/.
  index <topic>|--all        rebuild index.md from wiki/ frontmatter (no LLM)
"""
import json, os, re, subprocess, sys, time, hashlib, shutil
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"; TOPICS = VAULT / "topics"
PROFILE = os.environ.get("SENTER_WORKER_PROFILE", "senter")
BRIDGE = "http://127.0.0.1:8643"; TOKEN = Path.home() / ".hermes/senter-bridge/token"
SECTIONS = [("entities", "Entities"), ("concepts", "Concepts"), ("decisions", "Decisions"), ("comparisons", "Comparisons"), ("queries", "Queries")]

def now(): return time.strftime("%Y-%m-%d")
def post(text, status="working", url=None):
    try:
        import urllib.request
        body = {"bot": "senter", "text": text, "status": status}
        if url: body["url"] = url
        req = urllib.request.Request(BRIDGE + "/post", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception: pass
def stage(act, **kw):
    try:
        import urllib.request
        body = {"act": act, "bot": "senter", **{k: v for k, v in kw.items() if v}}
        req = urllib.request.Request(BRIDGE + "/stage", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception: pass

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln: k, v = ln.split(":", 1); out[k.strip()] = v.strip().strip("'\"")
    return out

def init(t):
    d = TOPICS / t
    if not d.is_dir(): print("no topic", t); return
    for sub in ("raw/sources", "raw/inbox", *[f"wiki/{s}" for s, _ in SECTIONS]): (d / sub).mkdir(parents=True, exist_ok=True)
    # move bulk knowledge into raw/sources (immutable layer), symlink old paths so nothing breaks
    for old in ("sessions", "knowledge"):
        src = d / ".system" / old
        if src.is_dir() and not src.is_symlink():
            dst = d / "raw/sources" / old
            if dst.exists(): shutil.rmtree(dst)
            shutil.move(str(src), str(dst)); src.symlink_to(Path("..") / "raw/sources" / old)
    if not (d / "SCHEMA.md").exists():
        (d / "SCHEMA.md").write_text(f"""# Wiki Schema — {t}
## Domain
Everything Chris has said, built, decided or worried about regarding **{t}** — his inputs verbatim in `raw/`, compiled understanding in `wiki/`.

## Conventions (llm-wiki skill)
- `raw/` is immutable. `raw/inbox/YYYY-MM-DD.md` = the watcher's per-message filings; `raw/sources/` = transcripts, exports, specs, source code.
- `wiki/` pages: lowercase-hyphen filenames, YAML frontmatter (title, created, updated, type, tags, sources, confidence), ≥2 `[[wikilinks]]`, provenance `^[raw/…]` on synthesized paragraphs.
- Every page is listed in `index.md`; every action appended to `log.md`. Pages > 200 lines split. Contradictions noted with dates, `contested: true`.
- Chris's corrections win: lines marked `<!-- chris -->` are never rewritten.

## Tag taxonomy
person, tool, repo, bot, skill, loop, decision, preference, pain, idea, plan, spec, ui, infra, music, money, health, family, timeline, question

## Page thresholds
Create when an entity/concept appears in 2+ raw items or is central to one. Decisions get a page each (what/why/when/evidence). Passing mentions go into an existing page.
""")
    if not (d / "index.md").exists():
        (d / "index.md").write_text(f"# {t} — wiki index\n> One line per page. The wiki row's CONTEXT section renders this file.\n> Last updated: {now()} | Total pages: 0\n\n" + "".join(f"## {label}\n\n" for _, label in SECTIONS))
    if not (d / "log.md").exists():
        (d / "log.md").write_text(f"# Wiki Log — {t}\n\n## [{now()}] create | wiki initialized (topic-wiki.py init)\n")
    # today's inbox → raw/inbox/<date>.md (the watcher appends there from now on; old inbox.md becomes a source)
    ib = d / ".system/inbox.md"
    if ib.is_file() and not ib.is_symlink() and ib.stat().st_size > 0:
        shutil.copy(str(ib), str(d / "raw/inbox" / f"{now()}-legacy-inbox.md"))
    print("init", t)

def rebuild_index(t):
    d = TOPICS / t; pages = {s: [] for s, _ in SECTIONS}
    for s, _ in SECTIONS:
        for p in sorted((d / "wiki" / s).glob("*.md")):
            f = fm(p.read_text(errors="replace")); title = f.get("title") or p.stem
            body = p.read_text(errors="replace"); summ = f.get("summary") or next((ln.strip() for ln in body.split("---", 2)[-1].splitlines() if ln.strip() and not ln.startswith("#")), "")
            pages[s].append(f"- [[topics/{t}/wiki/{s}/{p.stem}|{title}]] — {summ[:160]}" + (f" _(updated {f['updated']})_" if f.get("updated") else ""))
    n = sum(len(v) for v in pages.values())
    out = f"# {t} — wiki index\n> One line per page. The wiki row's CONTEXT section renders this file.\n> Last updated: {now()} | Total pages: {n}\n\n"
    for s, label in SECTIONS: out += f"## {label}\n" + ("\n".join(pages[s]) + "\n" if pages[s] else "\n") + "\n"
    (d / "index.md").write_text(out); return n

def unprocessed(t):
    d = TOPICS / t; cur = d / ".system/wiki.cursor"; seen = set(cur.read_text().split()) if cur.exists() else set()
    items = []
    for p in sorted((d / "raw/inbox").glob("*.md")) + sorted((d / "raw/sources").rglob("*.md")):
        if any(seg.startswith((".", "sessions")) for seg in p.relative_to(d).parts): continue  # full transcripts are grepped on demand, not compiled per pass
        h = hashlib.sha1(p.read_bytes()).hexdigest()[:12]; key = f"{p.relative_to(d)}@{h}"
        if key not in seen: items.append((p, key))
    return items, seen

PROMPT = """You are compiling the LLM WIKI for topic `{t}` (Karpathy pattern; the `llm-wiki` skill rules apply). Work ONLY inside {d}.
Read SCHEMA.md, index.md, and the tail of log.md first. Then read the NEW RAW ITEMS listed below (they are immutable — never edit raw/).
For everything in them that meets the page thresholds, CREATE or UPDATE pages under wiki/entities|concepts|decisions|comparisons|queries
(frontmatter: title, created, updated, type, tags from SCHEMA taxonomy, sources: [raw paths], confidence). Be THOROUGH: this wiki must
hold everything Chris said or decided about this topic — his words quoted, his preferences, his pains, timelines, tools, people, plans.
Every page: ≥2 [[wikilinks]] to other pages in this topic (use [[topics/{t}/wiki/<section>/<slug>|Title]]), provenance ^[raw/…] on
synthesized paragraphs. Never rewrite lines marked <!-- chris -->. When facts conflict, keep both with dates and set contested: true.
Then append one entry to log.md: "## [{date}] compile | <n> raw items → pages created/updated: <list>". Do NOT edit index.md (rebuilt
programmatically). Do not write outside wiki/ and log.md. Use write_file/read_file/search_files only. When finished, print the list of
files you created or updated, one per line, nothing else.

NEW RAW ITEMS:
{items}
"""

def compile_(t, dry=False):
    d = TOPICS / t
    if not (d / "SCHEMA.md").exists(): init(t)
    items, seen = unprocessed(t)
    if not items: print(t, "nothing new"); return
    lst = "\n".join(f"- {p.relative_to(d)} ({p.stat().st_size} bytes)" for p, _ in items[:40])
    q = Path(f"/tmp/wiki-compile-{t}.md"); q.write_text(PROMPT.format(t=t, d=d, date=now(), items=lst))
    if dry: print(q.read_text()); return
    post(f"WIKI {t} · compiling {len(items)} raw items into wiki pages", "working", f"topics/{t}/index.md"); stage("open", topic=t, hold=1500)
    r = subprocess.run(["hermes", "chat", "-p", PROFILE, "--query-file", str(q), "--oneshot", "-Q", "--max-turns", "40", "--yolo"], capture_output=True, text=True, timeout=1500, cwd=str(d))
    files = [ln.strip() for ln in r.stdout.splitlines() if ln.strip().endswith(".md") and "wiki/" in ln]
    n = rebuild_index(t)
    (d / ".system/wiki.cursor").write_text("\n".join(sorted(seen | {k for _, k in items})))
    with (VAULT / "log.md").open("a") as f: f.write(f"{time.strftime('%Y-%m-%d %H:%M')}: topic-wiki compile {t} · {len(items)} raw → {len(files)} pages touched · index {n} pages\n")
    post(f"WIKI {t} · {len(files)} pages written/updated · index now {n} pages", "done", f"topics/{t}/index.md")
    for f_ in files[:6]: stage("edit", topic=t, text="wiki: " + f_.split("wiki/")[-1])
    print(t, len(items), "raw →", len(files), "pages; index", n); print(r.stdout[-1200:] if not files else "\n".join(files))

if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a[0] if a else "index"; tgt = a[1] if len(a) > 1 else "--all"
    names = [p.name for p in sorted(TOPICS.iterdir()) if p.is_dir() and not p.name.startswith(("_", "."))] if tgt == "--all" else [tgt]
    for t in names:
        if cmd == "init": init(t); rebuild_index(t)
        elif cmd == "index": print(t, rebuild_index(t))
        elif cmd == "compile": compile_(t, "--dry" in a)
