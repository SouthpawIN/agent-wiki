#!/usr/bin/env python3
"""wiki-dedupe.py v1.0.0 — paladin's within-topic wiki page dedupe (loop: wiki-dedupe-sweep).

Folds same-subject page pairs inside one wiki section of one topic into a single slug.

  scan     <topic> [--json]          list candidate pairs (slug-token overlap + shared sources), with winner/loser + link counts
  plan     <topic> --pairs FILE      write a dry-run manifest (.dryrun.md) for the pairs listed in FILE (one "section/a.md section/b.md" per line)
  execute  <topic> --pairs FILE --approved-by NAME
           for each pair: REQUIRE every ^[raw/…] citation and every <!-- chris --> line of the loser to already be present in
           the winner (the bot folds content BEFORE execute; this script refuses otherwise) → archive loser to
           topics/_archive/wiki-dedupe/<topic>/<section>/<slug>.md (nothing is deleted) → rewrite every [[…/loser|…]] wikilink
           vault-wide to the winner → append "## Absorbed" to the winner → rebuild index.md → log "## [date] dedupe | …" in
           the topic's log.md and the vault log.md → post one feed card per topic.

Winner rule (fixed): most inbound wikilinks from OTHER pages (index.md excluded — it links both once); tie → dated decision
slug beats undated; tie → the slug more other topics link to; tie → older file (created); tie → longer body.
"""
import argparse, json, re, shutil, sys, time, urllib.request
from pathlib import Path

VERSION = "1.0.1"
PINNED = False  # set by --winner-first
ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"
ARCHIVE = TOPICS / "_archive" / "wiki-dedupe"
BRIDGE = "http://127.0.0.1:8643"
TOKEN = Path.home() / ".hermes/senter-bridge/token"
SECTIONS = [("entities", "Entities"), ("concepts", "Concepts"), ("decisions", "Decisions"), ("comparisons", "Comparisons"), ("queries", "Queries")]
STOP = {"the", "and", "a", "of", "in", "is", "to", "for", "vs", "on", "as", "with", "not", "one", "this", "that", "into", "what", "how", "why", "md"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
CITE_RE = re.compile(r"\^\[(raw/[^\]]+)\]")
CHRIS_RE = re.compile(r"^.*<!--\s*chris\s*-->.*$", re.M)
LINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]")


def now(fmt="%Y-%m-%d %H:%M"): return time.strftime(fmt)


def post(bot, text, status="working", url=None):
    try:
        body = {"bot": bot, "text": text, "status": status, **({"url": url} if url else {})}
        req = urllib.request.Request(BRIDGE + "/post", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json", "X-Senter-Token": TOKEN.read_text().strip()})
        urllib.request.urlopen(req, timeout=3).read(); return True
    except Exception as e:
        print("bridge:", e, file=sys.stderr); return False


def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S); out = {}
    if m:
        cur = None
        for ln in m.group(1).splitlines():
            if re.match(r"^\s*-\s", ln) and cur:
                out.setdefault(cur, []); out[cur] = (out[cur] if isinstance(out[cur], list) else []) + [ln.split("-", 1)[1].strip().strip("'\"")]
            elif ":" in ln:
                k, v = ln.split(":", 1); cur = k.strip(); v = v.strip()
                if v.startswith("[") and v.endswith("]"): out[cur] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                else: out[cur] = v.strip("'\"")
    return out


def body_of(text):
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def tokens(slug):
    return {t for t in re.split(r"[^a-z0-9]+", DATE_RE.sub("", slug).lower()) if t and t not in STOP and not t.isdigit()}


def page_link(t, s, slug): return f"topics/{t}/wiki/{s}/{slug}"


def all_md(root):
    for p in root.rglob("*.md"):
        if any(seg.startswith(".") or seg == "_archive" for seg in p.relative_to(root).parts): continue
        yield p


def inbound(t, s, slug):
    """(links from other wiki pages in this topic, links from files outside this topic)."""
    target = page_link(t, s, slug); own = 0; other = 0
    for p in all_md(TOPICS):
        if p.name == "index.md" and p.parent == TOPICS / t: continue
        txt = p.read_text(errors="replace")
        n = sum(1 for m in LINK_RE.finditer(txt) if m.group(1).strip() == target)
        if not n: continue
        rel = p.relative_to(TOPICS)
        if rel.parts[0] == t and rel.parts[1] == "wiki" and p.stem != slug: own += n
        elif rel.parts[0] != t: other += n
    return own, other


def rank_key(t, s, p):
    own, other = inbound(t, s, p.stem)
    dated = 1 if DATE_RE.match(p.stem) else 0
    text = p.read_text(errors="replace"); f = fm(text)
    created = f.get("created") or "9999"
    return (own, dated if s == "decisions" else 0, other, -len(created), -1 if created == "9999" else 0, len(body_of(text)))


def decide(t, s, a, b):
    if PINNED:  # pairs file order is authoritative: first column = winner (decided at plan time, before folding adds cross-links)
        return a, b, {"own": (inbound(t, s, a.stem)[0], inbound(t, s, b.stem)[0]), "other": (0, 0)}
    if s == "decisions" and bool(DATE_RE.match(a.stem)) != bool(DATE_RE.match(b.stem)):  # hard rule: undated decision folds into the dated one
        win, lose = (a, b) if DATE_RE.match(a.stem) else (b, a)
        return win, lose, {"own": (inbound(t, s, a.stem)[0], inbound(t, s, b.stem)[0]), "other": (0, 0)}
    ka, kb = rank_key(t, s, a), rank_key(t, s, b)
    # created: older wins → compare as string ascending; encode by picking lexicographically smaller created
    fa, fb = fm(a.read_text(errors="replace")).get("created", ""), fm(b.read_text(errors="replace")).get("created", "")
    ka = ka[:3] + ((fa <= fb) * 1,) + ka[5:]; kb = kb[:3] + ((fb < fa) * 1,) + kb[5:]
    win, lose = (a, b) if ka >= kb else (b, a)
    return win, lose, {"own": (ka[0], kb[0]), "other": (ka[2], kb[2])}


def scan(t, as_json=False):
    d = TOPICS / t / "wiki"; out = []
    for s, _ in SECTIONS:
        pages = sorted((d / s).glob("*.md")) if (d / s).is_dir() else []
        meta = {p: (tokens(p.stem), set(fm(p.read_text(errors="replace")).get("sources") or [])) for p in pages}
        for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                a, b = pages[i], pages[j]; ta, sa = meta[a]; tb, sb = meta[b]
                if not ta or not tb: continue
                inter = ta & tb; jac = len(inter) / len(ta | tb)
                contained = ta <= tb or tb <= ta
                src = len(sa & sb) / max(1, len(sa | sb))
                score = max(jac, 0.6 if contained else 0) + 0.25 * src
                if score >= 0.45 or (contained and len(inter) >= 2):
                    out.append({"section": s, "a": a.name, "b": b.name, "slug_jaccard": round(jac, 2), "contained": contained, "shared_sources": round(src, 2)})
    if as_json: print(json.dumps(out, indent=1))
    else:
        for r in out: print(f"{r['section']}/{r['a']}  ~  {r['section']}/{r['b']}   jac={r['slug_jaccard']} contained={r['contained']} src={r['shared_sources']}")
    return out


def read_pairs(t, path):
    pairs = []
    for ln in Path(path).read_text().splitlines():
        ln = ln.split("#", 1)[0].strip()
        if not ln: continue
        a, b = ln.split()
        pa, pb = TOPICS / t / "wiki" / a, TOPICS / t / "wiki" / b
        if pa.parent != pb.parent: sys.exit(f"pair crosses sections: {ln}")
        if not pa.is_file() or not pb.is_file(): sys.exit(f"missing page in pair: {ln}")
        pairs.append((pa.parent.name, pa, pb))
    return pairs


def check_fold(win, lose):
    """Everything the loser carries that we must never drop must already be in the winner."""
    wt, lt = win.read_text(errors="replace"), lose.read_text(errors="replace")
    missing_cites = sorted({c for c in CITE_RE.findall(lt)} - {c for c in CITE_RE.findall(wt)})
    missing_chris = [ln for ln in CHRIS_RE.findall(lt) if ln.strip() not in wt]
    lsrc = set(fm(lt).get("sources") or []); wsrc = set(fm(wt).get("sources") or [])
    return missing_cites, missing_chris, sorted(lsrc - wsrc)


def plan(t, pairs_file):
    pairs = read_pairs(t, pairs_file); lines = [f"# wiki-dedupe DRY-RUN · {t} · {now()} · v{VERSION}", "", f"{len(pairs)} pairs. Nothing written.", ""]
    ok = True
    for s, a, b in pairs:
        win, lose, k = decide(t, s, a, b)
        mc, mch, ms = check_fold(win, lose)
        state = "READY" if not (mc or mch or ms) else "NEEDS FOLD"
        if state != "READY": ok = False
        lines.append(f"- [{state}] {s}: KEEP `{win.stem}` (in-links own={k['own'][0 if win is a else 1]} other={k['other'][0 if win is a else 1]}) ← ARCHIVE `{lose.stem}` (own={k['own'][1 if win is a else 0]} other={k['other'][1 if win is a else 0]})")
        for c in mc: lines.append(f"    - missing citation in winner: ^[{c}]")
        for c in mch: lines.append(f"    - missing chris line in winner: {c.strip()[:100]}")
        for c in ms: lines.append(f"    - missing frontmatter source in winner: {c}")
    out = TOPICS / t / ".system" / "wiki-dedupe.dryrun.md"; out.parent.mkdir(exist_ok=True); out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines)); print(f"\n→ {out}")
    return ok


def rewrite_links(old, new):
    n = 0
    for p in all_md(TOPICS):
        txt = p.read_text(errors="replace")
        def sub(m):
            nonlocal n
            if m.group(1).strip() != old: return m.group(0)
            n += 1; return f"[[{new}{m.group(2) or ''}{m.group(3) or ''}]]"
        new_txt = LINK_RE.sub(sub, txt)
        if new_txt != txt: p.write_text(new_txt)
    for p in [ROOT / "index.md", *(ROOT / "catalogs").glob("*.md")] if (ROOT / "catalogs").is_dir() else [ROOT / "index.md"]:
        if p.is_file():
            txt = p.read_text(errors="replace"); new_txt = txt.replace(f"[[{old}|", f"[[{new}|").replace(f"[[{old}]]", f"[[{new}]]")
            if new_txt != txt: p.write_text(new_txt); n += 1
    return n


def rebuild_index(t):
    d = TOPICS / t; pages = {s: [] for s, _ in SECTIONS}
    for s, _ in SECTIONS:
        for p in sorted((d / "wiki" / s).glob("*.md")):
            body = p.read_text(errors="replace"); f = fm(body); title = f.get("title") or p.stem
            summ = f.get("summary") or next((ln.strip() for ln in body_of(body).splitlines() if ln.strip() and not ln.startswith("#")), "")
            pages[s].append(f"- [[topics/{t}/wiki/{s}/{p.stem}|{title}]] — {summ[:160]}")
    n = sum(len(v) for v in pages.values())
    out = f"# {t} — wiki index\n> One line per page. The wiki row's CONTEXT section renders this file.\n> Last updated: {now('%Y-%m-%d')} | Total pages: {n}\n\n"
    for s, label in SECTIONS: out += f"## {label}\n" + ("\n".join(pages[s]) + "\n" if pages[s] else "\n") + "\n"
    (d / "index.md").write_text(out); return n


def execute(t, pairs_file, approved_by):
    pairs = read_pairs(t, pairs_file)
    # gate: every pair must be READY
    bad = []
    for s, a, b in pairs:
        win, lose, _ = decide(t, s, a, b); mc, mch, ms = check_fold(win, lose)
        if mc or mch or ms: bad.append((lose.stem, mc, mch, ms))
    if bad:
        for b in bad: print("REFUSED — fold incomplete:", b, file=sys.stderr)
        sys.exit(2)
    merged = []; links_rewritten = 0
    for s, a, b in pairs:
        win, lose, _ = decide(t, s, a, b)
        dest = ARCHIVE / t / s / lose.name; dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists(): dest = dest.with_name(f"{lose.stem}.{now('%H%M%S')}.md")
        shutil.move(str(lose), str(dest))
        links_rewritten += rewrite_links(page_link(t, s, lose.stem), page_link(t, s, win.stem))
        wt = win.read_text(errors="replace")
        absorbed = f"- `{s}/{lose.stem}` — {now('%Y-%m-%d')} → archived at `{dest.relative_to(ROOT)}`"
        if "## Absorbed" in wt: wt = wt.rstrip("\n") + "\n" + absorbed + "\n"
        else: wt = wt.rstrip("\n") + "\n\n## Absorbed\n" + absorbed + "\n"
        wt = re.sub(r"^updated: .*$", f"updated: {now('%Y-%m-%d')}", wt, count=1, flags=re.M)
        win.write_text(wt); merged.append((s, win.stem, lose.stem))
    n = rebuild_index(t)
    summary = ", ".join(f"{s}/{l} → {w}" for s, w, l in merged)
    entry = f"\n## [{now()}] dedupe | {len(merged)} pairs folded by paladin (wiki-dedupe v{VERSION}, approved: {approved_by}) · {links_rewritten} wikilinks rewritten · index rebuilt ({n} pages) | {summary}\n"
    with (TOPICS / t / "log.md").open("a") as f: f.write(entry)
    with (ROOT / "log.md").open("a") as f: f.write(f"{now()}: paladin dedupe {t} · {len(merged)} pairs folded, losers archived under topics/_archive/wiki-dedupe/{t}/ · {links_rewritten} links rewritten · index {n} | {summary}\n")
    (ARCHIVE / t / "ABSORBED.md").parent.mkdir(parents=True, exist_ok=True)
    with (ARCHIVE / t / "ABSORBED.md").open("a") as f:
        f.write(f"## {now()} (v{VERSION}, approved: {approved_by})\n" + "".join(f"- {s}/{l} → {s}/{w}\n" for s, w, l in merged) + "\n")
    print(entry); print(json.dumps({"topic": t, "merged": merged, "links_rewritten": links_rewritten, "index_pages": n}))
    return merged, links_rewritten, n


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", choices=["scan", "plan", "execute"]); ap.add_argument("topic")
    ap.add_argument("--pairs"); ap.add_argument("--approved-by"); ap.add_argument("--json", action="store_true"); ap.add_argument("--post", action="store_true")
    ap.add_argument("--winner-first", action="store_true", help="pairs file order is authoritative: first column = winner")
    a = ap.parse_args()
    global PINNED; PINNED = a.winner_first
    if not (TOPICS / a.topic).is_dir(): sys.exit(f"no topic {a.topic}")
    if a.cmd == "scan": scan(a.topic, a.json)
    elif a.cmd == "plan":
        if not a.pairs: sys.exit("--pairs required")
        ok = plan(a.topic, a.pairs); sys.exit(0 if ok else 3)
    else:
        if not (a.pairs and a.approved_by): sys.exit("--pairs and --approved-by required")
        merged, links, n = execute(a.topic, a.pairs, a.approved_by)
        if a.post and merged:
            post("paladin", f"DEDUPE {a.topic} · {len(merged)} pairs folded: " + "; ".join(f"{l}→{w}" for _, w, l in merged) + f" · losers archived, {links} links rewritten, index {n}", "done", f"topics/{a.topic}/index.md")


if __name__ == "__main__": main()
