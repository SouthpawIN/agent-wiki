#!/usr/bin/env python3
"""senter-watcher.py — the WATCHER (Chris, 2026-09-05): "watch the Hermes agent logs directly … sort all of those into the topics …
per message, like Cursor — a live-acting second brain."

Tails ~/.hermes/state.db `messages` (rowid cursor, WAL-safe), classifies every new user/assistant message against the live
topic corpus (same TF-IDF the wiki uses: README + .system knowledge, via .system-live.json `text`), and:
  • appends it to topics/<best>/.system/inbox.md  (dated, role, session, score) — the raw context, nothing summarised
  • posts a feed card (bridge /post) so the wiki visibly moves
  • when nothing fits (score < NEW_TOPIC_FLOOR) → a PROPOSAL card "new topic?" with the message's top terms, and the message
    is parked in topics/_inbox/unsorted.md until Chris approves (approval path = hermes serve approval.* — step 1 of the plan;
    until then the card is informational)
  • every N filed messages on one topic → PROPOSAL "skill candidate" listing the recurring imperative lines (the distil step
    the topic loop will take over)

Skips: cron sessions (they're the loops themselves), tool/system roles, the watcher's own bridge posts, messages < 20 chars.
State: ~/.hermes/senter-bridge/watcher.cursor (last rowid). Run: `python3 assets/senter-watcher.py --follow` (launchd
com.senter.watcher). One pass: no flag.
"""
import json, math, re, sqlite3, sys, time, os, collections, urllib.request, subprocess
from pathlib import Path

VAULT = Path.home() / "Documents/Projects/Projects"
HERMES = Path.home() / ".hermes"
DB = HERMES / "state.db"
LIVE = VAULT / ".system-live.json"
CURSOR = HERMES / "senter-bridge" / "watcher.cursor"
TOKEN = (HERMES / "senter-bridge" / "token")
BRIDGE = "http://127.0.0.1:8643"
NEW_TOPIC_FLOOR = 0.06     # cosine below this = no topic fits
SKILL_EVERY = 12           # filed messages per topic between skill-candidate proposals
STOP = set("the a an and or of to in on for with is are was were be been it this that these those i you we they he she my your our its as at by from not no yes do does did have has had will would can could should just like so if then than about into over under up down out very really also ok okay yeah".split())

def tok(t):
    return [w for w in re.findall(r"[a-z][a-z0-9_\-]{2,}", (t or "").lower()) if w not in STOP]

def _brief_aliases():
    """2026-09-05: aliases come from each topic's BRIEF.md (the pre-prompt Chris can edit), with a few hand seeds kept as fallback."""
    out = {}
    for d in (VAULT / "topics").iterdir():
        b = d / "BRIEF.md"
        if not b.is_file(): continue
        m = re.search(r"## Aliases[^\n]*\n([\s\S]*?)(\n## |\Z)", b.read_text(errors="replace"))
        if m: out[d.name] = [ln[2:].strip().lower() for ln in m.group(1).splitlines() if ln.startswith("- ") and ln[2:].strip()]
    return out

_SEED_ALIASES = {"senter-wiki": ["senter wiki", "the wiki", "vault-live", "wiki ui", "rocker", "eq", "feed", "media player", "hover card", "settings card"],
           "senter": ["senter", "sidebar", "watcher", "topic agent", "fleet", "umbrella"], "youtube": ["youtube", "video", "shorts", "channel"],
           "turbofit": ["turbofit", "gguf", "llama.cpp", "dflash"], "hermes-agent": ["hermes agent", "hermes-agent"], "klerik": ["klerik"], "anser": ["anser"],
           "music": ["music", "spotify", "playlist", "lo-fi", "lofi"], "evolutionary": ["evolutionary", "genetic"], "pocket-shop": ["pocket shop", "tcgplayer", "mtg"]}

def ALIASES_for(n):
    a = list(_SEED_ALIASES.get(n, [])) + list(_BRIEF.get(n, [])) or [n]
    return a
_BRIEF = _brief_aliases()

class Sim:
    def __init__(self, docs):            # docs: {name: text}
        self.names = list(docs); self.N = len(docs) or 1
        self.df = collections.Counter()
        self.tf = {}
        for n, t in docs.items():
            c = collections.Counter(tok(t)); self.tf[n] = c
            for w in c: self.df[w] += 1
        self.vec = {n: self._v(c) for n, c in self.tf.items()}
    def _v(self, c):
        v = {}; norm = 0.0
        for w, k in c.items():
            x = (1 + math.log(k)) * (math.log((self.N + 1) / (self.df.get(w, 0) + 1)) + 1)
            v[w] = x; norm += x * x
        return v, (math.sqrt(norm) or 1.0)
    def best(self, text):
        q, qn = self._v(collections.Counter(tok(text)))
        low = " " + re.sub(r"[^a-z0-9 ]", " ", text.lower()) + " "
        out = []
        for n in self.names:
            v, vn = self.vec[n]; dot = sum(x * v.get(w, 0) for w, x in q.items())
            sc = dot / (qn * vn)
            # explicit mention of the topic (or a name alias) binds hard — "turbofit", "youtube", "klerik" in the text = that topic
            for alias in ALIASES_for(n):
                if " " + alias + " " in low: sc += 0.25; break
            out.append((sc, n))
        out.sort(reverse=True); return out

def load_corpus():
    """Corpus per topic = README + all wiki pages + SCHEMA + last 2 inbox days, read from disk (not the snapshot, which lags), with the topic
    name repeated so name mentions bind hard. 2026-09-05: thin topics misfiled Chris's messages (kashik 0.08) because the snapshot text was stale/empty."""
    docs = {}
    for d in sorted((VAULT / "topics").iterdir()):
        if not d.is_dir() or d.name.startswith(("_", ".")): continue
        parts = [(d.name.replace("-", " ") + " ") * 6]
        for f in [d / "README.md", d / "SCHEMA.md", d / ".system/continuity.md"]:
            if f.is_file(): parts.append(f.read_text(errors="replace")[:20000])
        if (d / "wiki").is_dir():
            for f in sorted((d / "wiki").rglob("*.md"))[:80]: parts.append(f.read_text(errors="replace")[:4000])
        # inbox is NOT in the corpus: topics that hold everything Chris says (senter, senter-wiki) would swallow every message.
        docs[d.name] = "\n".join(parts)
    return docs, None

def post(bot, text, status=None, url=None):
    try:
        tok_ = TOKEN.read_text().strip()
        body = {"bot": bot, "text": text}
        if status: body["status"] = status
        if url: body["url"] = url
        req = urllib.request.Request(BRIDGE + "/post", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": tok_})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception as e:
        print("post failed:", e, file=sys.stderr)

def stage(act, **kw):
    """2026-09-05: visible echo — the wiki scrolls/opens/edits/closes the row this event touched."""
    try:
        body = {"act": act, "bot": "senter", **{k: v for k, v in kw.items() if v}}
        req = urllib.request.Request(BRIDGE + "/stage", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception: pass

def scaffold_topic(slug, text, terms):
    """2026-09-05 (Chris): "if I talk about a new subject then it should suggest maybe researching it or maybe scaffolding it" and
    "these are the things I don't want to have to give approval on". New subject → scaffold the topic NOW (README + .system, spec
    layout), file the message there, and dispatch a research run to an existing bot (research = looker if it exists, else senter).
    No approval: topics and edits are free; only bots and loops need Chris."""
    t = VAULT / "topics" / slug
    if t.exists(): return False
    (t / ".system").mkdir(parents=True); (t / "skills").mkdir(); (t / "agents").mkdir(); (t / "loops").mkdir()
    when = time.strftime("%Y-%m-%d %H:%M")
    (t / "README.md").write_text(f"# {slug}\n_Scaffolded by the watcher {when} from a new subject Chris raised in the sidebar. Terms: {' · '.join(terms)}._\n\n## What Chris said\n> {text.strip()[:600]}\n\n## Status\n- research dispatched (see .system/research.md when it lands)\n")
    (t / ".system/continuity.md").write_text(f"# Continuity — {slug}\n- New subject {when}: {text.strip()[:300]}\n")
    (t / ".system/queue.md").write_text(f"# Queue — {slug}\n\n## [CONTEXT]\n- [~] research — dispatched {when}\n\n## [SKILLS]\n\n## [AGENTS]\n\n## [LOOPS]\n")
    return True

def dispatch_research(slug, text):
    """One background bot run: research the new subject and write topics/<slug>/.system/research.md. Uses an existing profile."""
    prof = "looker" if (HERMES / "profiles/looker").is_dir() else "senter"
    q = Path(f"/tmp/research-{slug}.md"); q.write_text(f"""You are researching a NEW SUBJECT Chris just raised in the Senter sidebar, for the wiki topic `{slug}`.
He said: \"\"\"{text.strip()[:1500]}\"\"\"
Do a fast, honest first pass (web_search allowed, <= 8 calls): what it is, the 3-5 most relevant resources/repos/people, how it could
connect to Chris's existing projects (Senter fleet, Hermes Agent, TurboFit, the wiki), and 3 concrete next steps he could take.
Write the result as markdown to {VAULT}/topics/{slug}/.system/research.md (write_file). Then append one line to
{VAULT}/topics/{slug}/README.md under '## Status': '- research landed <time>: <one-line gist>'. No other files. Be concrete, cite URLs.""")
    log = HERMES / "senter-bridge" / f"research-{slug}.log"
    subprocess.Popen(["hermes", "chat", "-p", prof, "--query-file", str(q), "--oneshot", "-Q", "--max-turns", "12", "--yolo"], cwd=str(VAULT), stdout=log.open("w"), stderr=subprocess.STDOUT, start_new_session=True)
    return prof

def read_cursor():
    try: return int(CURSOR.read_text().strip())
    except Exception:
        # first run: start at the newest rowid so we don't replay history (history is already exported into the topics)
        con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
        r = con.execute("select coalesce(max(rowid),0) from messages").fetchone()[0]; con.close(); return r

def write_cursor(n): CURSOR.parent.mkdir(parents=True, exist_ok=True); CURSOR.write_text(str(n))

def file_message(topic, role, session, ts, text, score):
    # 2026-09-05 (Chris): topics are LLM wikis — the watcher writes the immutable raw layer: raw/inbox/<day>.md (llm-wiki skill, Layer 1)
    p = VAULT / "topics" / topic / "raw" / "inbox" / (time.strftime("%Y-%m-%d", time.localtime(ts)) + ".md")
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(f"---\ningested: {time.strftime('%Y-%m-%d', time.localtime(ts))}\nsource: hermes state.db messages (watcher)\n---\n# raw inbox — {topic} — {time.strftime('%Y-%m-%d', time.localtime(ts))}\n")
    when = time.strftime("%Y-%m-%d %H:%M", time.localtime(ts))
    with p.open("a") as f:
        f.write(f"\n## {when} · {role} · {session} · sim {score:.2f}\n{text.strip()}\n")

def park_unsorted(role, session, ts, text, top):
    p = VAULT / "topics" / "_inbox" / "unsorted.md"; p.parent.mkdir(parents=True, exist_ok=True)
    when = time.strftime("%Y-%m-%d %H:%M", time.localtime(ts))
    with p.open("a") as f:
        f.write(f"\n## {when} · {role} · {session} · best {top[0][1]} {top[0][0]:.2f}\n{text.strip()}\n")

def skill_candidates(topic):
    """recurring imperative / how-to lines in the topic inbox = the raw material of a skill"""
    p = VAULT / "topics" / topic / "raw" / "inbox"
    if not p.is_dir(): return []
    class _P:  # concat all inbox days
        def read_text(self_): return "\n".join(x.read_text() for x in sorted(p.glob("*.md")))
    p = _P()
    lines = [l.strip() for l in p.read_text().splitlines() if l.strip() and not l.startswith("#")]
    imp = [l for l in lines if re.match(r"^(make|use|never|always|when|run|check|set|keep|don'?t|if|every|before|after|open|click|read)\b", l, re.I) and 30 < len(l) < 220]
    c = collections.Counter(re.sub(r"\d+", "#", l.lower()) for l in imp)
    return [l for l, n in c.most_common(5)]

def process(rows, sim, counts):
    filed = 0
    for rowid, sid, role, content, ts in rows:
        filed += 1
        text = content or ""
        if role not in ("user", "assistant") or len(text) < 20: continue
        if sid.startswith("cron_"): continue
        if text.startswith("Senter Wiki ·") or "senter-watcher" in text[:200]: continue
        text = re.sub(r"```[\s\S]*?```", " ", text)[:4000]
        role_s = "chris" if role == "user" else "hermes"
        # 2026-09-05 (Chris): "the watcher … is just cutting out pieces that are by topic and sorting those into their topic."
        # A message that spans subjects is CUT: split into sentence-groups (~2-4 sentences), each classified on its own; consecutive
        # pieces that land on the same topic are re-joined so the cut follows the subject change, not the sentence count.
        pieces = cut(text, sim) if len(text) > 260 else [(text, sim.best(text))]
        for piece, top in pieces:
            score, topic = top[0]
            handle_piece(piece, top, score, topic, role, role_s, sid, ts, counts, text)
    return filed

def cut(text, sim):
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", text)
    groups = [" ".join(sents[i:i + 3]) for i in range(0, len(sents), 3)]
    out = []
    for g in groups:
        if len(g.strip()) < 20: continue
        top = sim.best(g)
        if out and out[-1][1][0][1] == top[0][1]: out[-1] = (out[-1][0] + " " + g, out[-1][1])
        else: out.append((g, top))
    return out or [(text, sim.best(text))]

def handle_piece(text, top, score, topic, role, role_s, sid, ts, counts, whole):
    """one topic-classified cut of a message → raw/inbox of its topic; a new subject → scaffold + immediate action pitch"""
    if score < NEW_TOPIC_FLOOR:
        terms = [w for w, _ in collections.Counter(tok(text)).most_common(6)]
        if role != "user" or len(text) < 80:   # only Chris's own substantive pieces open subjects; short/assistant misfits just park
            park_unsorted(role_s, sid, ts, text, top); return
        slug = "-".join(terms[:2]) or f"subject-{int(ts)}"
        if scaffold_topic(slug, text, terms):
            file_message(slug, role_s, sid, ts, text, score)
            prof = dispatch_research(slug, text)
            # 2026-09-05 (Chris): "when a subject is made, I want this to be very proactive … 'do you want to research this? do you want a bot…'"
            post("senter", f"New subject: {' / '.join(terms[:3])}. Want me to research it? ({prof} is already taking a first look) — topics/{slug}", status="needs_chris", url=f"topics/{slug}/README.md")
            post("senter", f"Want a bot for `{slug}`? Its agent will pitch one as soon as it has read this (next pass ≤5 min).", status="needs_chris", url=f"topics/{slug}/README.md")
            stage("open", topic=slug, text=f"new subject: {text[:160]}")
            counts[slug] += 1
        else:
            file_message(slug, role_s, sid, ts, text, score)
        return
    file_message(topic, role_s, sid, ts, text, score)
    counts[topic] += 1
    post("senter", f"→ {topic} ({score:.2f}) · {role_s}: {text[:110].replace(chr(10),' ')}", status="working", url=f"topics/{topic}/raw/inbox/")
    stage("edit", topic=topic, text=f"{role_s}: {text[:200]}")

def main(follow=False):
    def sig():
        try: return max([p.stat().st_mtime for p in (VAULT / "topics").glob("*/index.md")] + [p.stat().st_mtime for p in (VAULT / "topics").glob("*/README.md")] + [p.stat().st_mtime for p in (VAULT / "topics").glob("*/BRIEF.md")] + [0])
        except Exception: return 0
    docs, _ = load_corpus(); sim = Sim(docs); corpus_at = sig(); last_sig_check = time.time()
    cur = read_cursor(); counts = collections.Counter()
    print(f"watcher: {len(docs)} topics · cursor {cur} · follow={follow}")
    while True:
        if time.time() - last_sig_check > 30:
            last_sig_check = time.time(); cs = sig()
            if cs != corpus_at: docs, _ = load_corpus(); sim = Sim(docs); corpus_at = cs; globals()['_BRIEF'] = _brief_aliases(); print(f"corpus reloaded: {len(docs)} topics")
        con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
        rows = con.execute("select rowid, session_id, role, content, timestamp from messages where rowid>? order by rowid limit 200", (cur,)).fetchall()
        con.close()
        if rows:
            process(rows, sim, counts); cur = rows[-1][0]; write_cursor(cur)
        if not follow: break
        time.sleep(1.5)

if __name__ == "__main__":
    main(follow="--follow" in sys.argv)
