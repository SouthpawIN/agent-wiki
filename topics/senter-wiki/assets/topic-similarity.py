#!/usr/bin/env python3
"""topic-similarity.py — group topics by likeness; feed the auto-merge governance.

paladin v1.2.0 (2026-09-02). Spec: topics/senter/plans/similarity-governance-2026-09-02.md
Chris: "this might be a good way to set the governance for what should be auto-merged."

v1.2.0: tfidf thresholds LOCKED by Chris (0.50 auto / 0.35 propose / name-stem rule); THRESHOLDS carries
        locked/locked_by/locked_on; a CLI override un-locks that run only; --post sends a DONE card
        (status done) when locked instead of the needs_chris proposal card.
v1.1.0: thresholds are PER METHOD (THRESHOLDS[method]) and carry their calibration source;
        .similarity gets `calibrated_against`; the report keeps hand-written sections appended
        after the generated block; `--compare OLD.json` prints a before/after top-N table
        (for the tfidf → embeddings switch).

For every topics/<t>/ (skips ., _ prefixed dirs) build one text:
    README.md (front-matter + repo-template boilerplate stripped)
  + .system/queue.md headings and item titles
  + skills/ names + agents/ names + loops/ names
  + repo names (front-matter `repo:` and `## Repos` rows)
  + the topic name's own dash-tokens (weighted x3 so the name matters)
Embed → pairwise cosine → average-linkage agglomerative clusters → write
`.system-live.json` key "similarity" (all other keys preserved):
  { "generated", "method", "thresholds": {auto, propose, cluster, method, calibrated,
                                            calibrated_against, calibrated_by, calibrated_on,
                                            locked, rule},
    "calibrated_against": "<merge-table path>", "n_topics",
    "clusters": [ {"id", "hue", "label", "members":[...]} ],
    "topics":   { "<t>": {"cluster", "hue"} },
    "pairs":    [ {"a","b","score","tier","stem"} ]  # tier: auto|propose|group|none
  }

Embedding providers (--provider):
  tfidf   (default, stdlib, deterministic; no credential)  — log-tf * idf, L2, cosine
  openai  any OpenAI-compatible /v1/embeddings: HERMES_EMBED_URL, HERMES_EMBED_MODEL,
          HERMES_EMBED_KEY (optional). Falls back to tfidf on any failure and says so.
NOTE: tfidf cosines run LOWER than dense-embedding cosines; the spec's 0.92/0.80 were
written on the embedding scale. `--post` shows the real distribution so Chris locks numbers.

Usage:
  topic-similarity.py            # compute + write .system-live.json.similarity + report .md
  topic-similarity.py --dry      # compute + print, write nothing
  topic-similarity.py --post     # also post the needs_chris threshold card to the bridge
  --auto F --propose F --cluster F   override THRESHOLDS[method] for this run only
  --compare OLD.json   before/after top-N vs an older .system-live.json (or bare similarity dict)
  --top N (20)  --provider tfidf|openai  --vault PATH
Stdlib only.
"""
import json, math, os, re, sys, time, urllib.request
from pathlib import Path

VERSION = "1.2.0"
VAULT = Path.home() / "Documents/Projects/Projects"
BRIDGE = "http://127.0.0.1:8643/post"
TOKEN = Path.home() / ".hermes/senter-bridge/token"
REPORT = "topics/senter/plans/similarity-governance-2026-09-02.report.md"
REPORT_END = "<!-- end generated — hand-written sections below survive re-runs -->"

# Governance: thresholds are per METHOD. Changing a number here is a paladin task with a card.
# tfidf numbers = senter's calibration (2026-09-02) against anser's SIGNED merge table:
#   every human-merged pair ≥0.50; human merges extend down to 0.39; kept-apart pairs top out at 0.46.
#   LOCKED by Chris 2026-09-02 ('yes on everything', via senter): 0.50 auto / 0.35 propose / name-stem rule.
#   A locked set only changes with a new Chris ruling (post a needs_chris card; --auto/--propose CLI
#   overrides still work for a single exploratory run and are reported as such).
# openai (dense) numbers = the spec's original draft; NOT calibrated, NOT locked — re-run --compare when a path lands.
MERGE_TABLE = "topics/senter/plans/topic-consolidation-2026-09-02.md#anser-audit"
THRESHOLDS = {
    "tfidf":  {"auto": 0.50, "propose": 0.35, "cluster": 0.30, "calibrated": True,
               "calibrated_against": MERGE_TABLE, "calibrated_by": "chris (approved senter's calibration run)",
               "calibrated_on": "2026-09-02", "locked": True, "locked_by": "chris", "locked_on": "2026-09-02"},
    "openai": {"auto": 0.92, "propose": 0.80, "cluster": 0.60, "calibrated": False,
               "calibrated_against": None, "calibrated_by": None, "calibrated_on": None,
               "locked": False, "locked_by": None, "locked_on": None},
}

STOP = set("""a an the and or of to in on for with by from as at is are was were be been being this that these those
it its into over under about via not no yes if then than so such can could may might will would shall should
we you they he she i me my our your their them his her us also all any each both more most other some
has have had having do does did done use used using uses one two new own same just only very
md readme topic topics repo repos github com https http www status facts open on last push created updated
type tags title dormant active archived license mit stars forks fork issues language original work
since none n/a true false""".split())

STEM_MIN_TOKENS = 2   # names sharing their first 2 dash-tokens are "same stem" (sovthpaw-omnistep-*)

# ----------------------------------------------------------------------------- text
def strip_front(text):
    if text.startswith("---"):
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if m: return m.group(1), text[m.end():]
    return "", text

BOILER = re.compile(r"^\s*(?:-\s*)?(?:\*\*)?(?:Language|Stars\s*/\s*forks|License|Fork of|Created|Open issues|Status)(?:\*\*)?\s*:.*$|"
                    r"^\s*\*\*\[Open on GitHub\].*$|^##\s*(?:Facts|From the README)\s*$", re.I | re.M)

def tokens(text):
    text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", r" \1 ", text)     # wikilinks → target
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    out = []
    for w in re.findall(r"[A-Za-z][A-Za-z0-9]+", text.lower()):
        if len(w) < 3 or w in STOP or w.isdigit(): continue
        out.append(w)
    return out

def name_tokens(name):
    return [t for t in name.lower().split("-") if t and t not in STOP]

def topic_text(d):
    """Return (tokens, meta) for topics/<d>."""
    parts, repos = [], []
    rd = (d / "README.md")
    if rd.is_file():
        fm, body = strip_front(rd.read_text(errors="replace"))
        m = re.search(r"(?m)^repo:\s*(\S+)", fm)
        if m: repos.append(m.group(1).rstrip("/").rsplit("/", 1)[-1])
        body = BOILER.sub(" ", body)
        parts.append(body)
        for m in re.finditer(r"(?ms)^## Repos\s*\n(.*?)(?=^## |\Z)", body):
            for ln in m.group(1).splitlines():
                mm = re.search(r"github\.com/[^/\s]+/([^/\s|)]+)", ln) or re.search(r"\|\s*([a-z0-9._-]+)\s*\|", ln)
                if mm: repos.append(mm.group(1))
    q = d / ".system/queue.md"
    if q.is_file():
        for ln in q.read_text(errors="replace").splitlines():
            s = ln.strip()
            if s.startswith("#") or re.match(r"^- \[[ x]\] \*\*", s):
                parts.append(re.sub(r"^- \[[ x]\]\s*", "", s.split("—")[0]))
    names = []
    for sub in ("skills", "agents", "loops"):
        p = d / sub
        if p.is_dir():
            names += [c.stem if c.is_file() else c.name for c in p.iterdir() if not c.name.startswith(".")]
    toks = tokens("\n".join(parts))
    for n in names + repos:
        toks += name_tokens(n) * 2
    toks += name_tokens(d.name) * 3
    return toks, {"repos": sorted(set(repos)), "n_tokens": len(toks), "has_readme": rd.is_file()}

# ----------------------------------------------------------------------------- embed
def embed_tfidf(docs):
    """docs: {name: tokens} → {name: {term: weight}} L2-normalized."""
    N = len(docs); df = {}
    for toks in docs.values():
        for t in set(toks): df[t] = df.get(t, 0) + 1
    idf = {t: math.log((N + 1) / (c + 1)) + 1.0 for t, c in df.items()}
    vecs = {}
    for name, toks in docs.items():
        tf = {}
        for t in toks: tf[t] = tf.get(t, 0) + 1
        v = {t: (1 + math.log(c)) * idf[t] for t, c in tf.items() if df[t] < N}   # drop terms in every doc
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs[name] = {t: x / norm for t, x in v.items()}
    return vecs

def cos_sparse(a, b):
    if len(a) > len(b): a, b = b, a
    return sum(x * b.get(t, 0.0) for t, x in a.items())

def embed_openai(docs):
    url = os.environ.get("HERMES_EMBED_URL", "").rstrip("/")
    model = os.environ.get("HERMES_EMBED_MODEL", "")
    if not url or not model: raise RuntimeError("HERMES_EMBED_URL / HERMES_EMBED_MODEL not set")
    key = os.environ.get("HERMES_EMBED_KEY", "not-needed")
    names = list(docs); inputs = [" ".join(docs[n])[:8000] for n in names]
    req = urllib.request.Request(url + "/embeddings", data=json.dumps({"model": model, "input": inputs}).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=120) as r: data = json.load(r)["data"]
    data.sort(key=lambda x: x["index"])
    out = {}
    for n, item in zip(names, data):
        v = item["embedding"]; norm = math.sqrt(sum(x * x for x in v)) or 1.0
        out[n] = [x / norm for x in v]
    return out

def cos_dense(a, b): return sum(x * y for x, y in zip(a, b))

# ----------------------------------------------------------------------------- cluster
def shared_stem(a, b):
    ta, tb = a.lower().split("-"), b.lower().split("-")
    if len(ta) >= 1 and tb[:len(ta)] == ta and len(tb) > len(ta): return True   # pocket-shop / pocket-shop-*
    if len(tb) >= 1 and ta[:len(tb)] == tb and len(ta) > len(tb): return True
    return len(ta) >= STEM_MIN_TOKENS and len(tb) >= STEM_MIN_TOKENS and ta[:STEM_MIN_TOKENS] == tb[:STEM_MIN_TOKENS]

def name_contains(a, b):
    """One topic's FULL name is a token-run inside the other's (pocket-shop ⊂ pocket-shop-pricing; turbohaul-manager ⊃ turbohaul).
    Chris 2026-09-03 recalibration: these must score HIGH in a context-similarity search — the name overlap IS the context signal.
    Deliberately NOT matching turbohaul↔turbofit (only a shared 'turbo' token — different things, must stay apart)."""
    ta, tb = a.lower().split("-"), b.lower().split("-")
    short, long = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    if len(short) == len(long) or len(short) < 1: return False
    for i in range(len(long) - len(short) + 1):
        if long[i:i + len(short)] == short: return True
    return False

def agglomerate(names, sim, threshold):
    """Average-linkage; merge while best inter-cluster mean similarity ≥ threshold."""
    clusters = [[n] for n in names]
    def link(c1, c2): return sum(sim[(a, b)] for a in c1 for b in c2) / (len(c1) * len(c2))
    while len(clusters) > 1:
        best, bi, bj = -1.0, -1, -1
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                s = link(clusters[i], clusters[j])
                if s > best: best, bi, bj = s, i, j
        if best < threshold: break
        clusters[bi] = clusters[bi] + clusters[bj]; del clusters[bj]
    clusters.sort(key=lambda c: (-len(c), c[0]))
    return clusters

def label_of(members, vecs, dense):
    if dense or len(members) == 1: return members[0]
    agg = {}
    for m in members:
        for t, x in vecs[m].items(): agg[t] = agg.get(t, 0.0) + x
    top = sorted(agg.items(), key=lambda kv: -kv[1])[:3]
    return " · ".join(t for t, _ in top)

# ----------------------------------------------------------------------------- main
def run(vault, provider, overrides, top):
    """overrides: {auto?, propose?, cluster?} from the CLI; everything else comes from THRESHOLDS[method]."""
    T = vault / "topics"; docs = {}; meta = {}
    for d in sorted(T.iterdir()):
        if not d.is_dir() or d.name.startswith((".", "_")): continue
        docs[d.name], meta[d.name] = topic_text(d)
    names = sorted(docs); method = provider; note = ""
    # 2026-09-03 LOCKS (Chris: hover-LOCK on the wiki title — "lock that title so it can't be deleted by auto-summarization").
    # topics/<t>/.system/lock.json {"locked": true} written by the vault-live.html LOCK pill via the bridge /write route.
    # A locked topic is never auto-merged: its pairs downgrade auto → propose (Chris still sees them, nothing runs silently).
    locked = set()
    for nm in names:
        lf = T / nm / ".system" / "lock.json"
        try:
            if lf.exists() and json.loads(lf.read_text()).get("locked"): locked.add(nm)
        except Exception: pass
    if locked: note = (note + "; " if note else "") + "locked topics (never auto-merged): " + ", ".join(sorted(locked))
    dense = False
    if provider == "openai":
        try: vecs = embed_openai(docs); dense = True
        except Exception as e:
            note = f"openai embed failed ({e.__class__.__name__}: {e}); fell back to tfidf"; method = "tfidf"; vecs = embed_tfidf(docs)
    else:
        vecs = embed_tfidf(docs)
    # thresholds follow the method that ACTUALLY ran (fallback re-selects), CLI overrides win for this run
    th = dict(THRESHOLDS[method]); th["method"] = method
    th["overridden"] = sorted(k for k in ("auto", "propose", "cluster") if k in overrides)
    th.update(overrides)
    # a CLI override is an exploratory run, never the locked set
    th["locked"] = bool(THRESHOLDS[method].get("locked")) and not th["overridden"]
    th["rule"] = "shared name-stem is always >= propose"
    th_auto, th_prop, th_cluster = th["auto"], th["propose"], th["cluster"]
    cos = cos_dense if dense else cos_sparse
    sim = {}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            s = round(cos(vecs[a], vecs[b]), 4)
            if name_contains(a, b): s = max(s, 0.65)  # 2026-09-03 recalibration: full-name containment = strong signal (above auto)
            sim[(a, b)] = sim[(b, a)] = s
    clusters = agglomerate(names, sim, th_cluster)
    multi = [c for c in clusters if len(c) > 1]
    n_h = max(8, min(12, len(multi)))            # 8–12 hues per spec; singletons get hue=None (no tint)
    cl_out, topic_out = [], {}
    for i, mem in enumerate(clusters):
        hue = int(round((i % n_h) * (360 / n_h))) if len(mem) > 1 else None
        cl_out.append({"id": i, "hue": hue, "label": label_of(mem, vecs, dense), "members": mem})
        for m in mem: topic_out[m] = {"cluster": i, "hue": hue}
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            s = sim[(a, b)]; stem = shared_stem(a, b)
            tier = "auto" if s >= th_auto else "propose" if s >= th_prop else "group" if topic_out[a]["cluster"] == topic_out[b]["cluster"] else "none"
            if stem and tier in ("group", "none"): tier = "propose"
            if tier == "auto" and (a in locked or b in locked): tier = "propose"  # LOCKED: never auto-merge without Chris
            if tier != "none" or s >= 0.15:
                pairs.append({"a": a, "b": b, "score": s, "tier": tier, "stem": stem})
    pairs.sort(key=lambda p: (-p["score"], p["a"]))
    # 2026-09-03 (Chris): the hero orbs are FILTERS — "everything underneath it will be the other topics listed in order of how contextually
    # similar they are". That ranking needs EVERY topic's score to the anchor, not just the ≥0.15 pairs, so the full matrix ships in the snapshot.
    matrix = {a: {b: round(sim[(a, b)] if (a, b) in sim else sim[(b, a)], 4) for b in names if b != a} for a in names}
    scores = sorted((p["score"] for p in pairs), reverse=True)
    result = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "version": VERSION, "method": method, "note": note,
        "calibrated_against": th["calibrated_against"],
        "n_topics": len(names), "n_pairs_total": len(names) * (len(names) - 1) // 2,
        "thresholds": th,
        "clusters": cl_out, "topics": topic_out, "pairs": pairs, "matrix": matrix,
        "meta": meta,
    }
    return result

def report_md(res, top):
    L = [f"# Topic similarity — {res['generated']} (method: {res['method']}, v{res['version']})", ""]
    if res["note"]: L += [f"> {res['note']}", ""]
    th = res["thresholds"]
    cal = (f"calibrated by {th['calibrated_by']} on {th['calibrated_on']} against `{th['calibrated_against']}`"
           if th.get("calibrated") else "NOT calibrated (spec draft numbers)")
    L += [f"{res['n_topics']} topics · {res['n_pairs_total']} pairs · {len(res['clusters'])} clusters (link ≥ {th['cluster']})",
          f"Thresholds for method `{th['method']}` ({'LOCKED by ' + str(th.get('locked_by')) + ' ' + str(th.get('locked_on')) if th['locked'] else 'not locked'}; {cal}): "
          f"auto ≥ {th['auto']} · propose {th['propose']}–{th['auto']} · {th['rule']}"
          + (f" · CLI override this run: {th['overridden']}" if th.get("overridden") else ""), ""]
    counts = {}
    for p in res["pairs"]: counts[p["tier"]] = counts.get(p["tier"], 0) + 1
    L += ["Tier counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())), "",
          f"## Top {top} pairs", "", "| # | a | b | score | tier | stem |", "|--:|---|---|------:|------|:----:|"]
    for i, p in enumerate(res["pairs"][:top], 1):
        L.append(f"| {i} | {p['a']} | {p['b']} | {p['score']:.3f} | {p['tier']} | {'✓' if p['stem'] else ''} |")
    L += ["", "## Clusters", ""]
    for c in res["clusters"]:
        if len(c["members"]) > 1:
            L.append(f"- **c{c['id']}** hue {c['hue']}° — _{c['label']}_ — {', '.join(c['members'])}")
    singles = [c["members"][0] for c in res["clusters"] if len(c["members"]) == 1]
    L.append(f"- singletons (no tint, hue=null): {len(singles)} — {', '.join(singles)}")
    L += ["", "## Score distribution (all pairs ≥ 0.15 kept)", ""]
    for lo, hi in ((0.92, 1.01), (0.80, 0.92), (0.60, 0.80), (0.50, 0.60), (0.40, 0.50), (0.35, 0.40), (0.30, 0.35), (0.15, 0.30)):
        n = sum(1 for p in res["pairs"] if lo <= p["score"] < hi)
        L.append(f"- {lo:.2f}–{min(hi,1.0):.2f}: {n}")
    L += ["", REPORT_END]
    return "\n".join(L) + "\n"

def write_report(path, md):
    """Regenerate the block above REPORT_END; keep whatever humans/bots appended below it."""
    tail = ""
    if path.exists():
        old = path.read_text()
        if REPORT_END in old:
            tail = old.split(REPORT_END, 1)[1]
        else:   # v1.0.0 report: everything after the generated distribution list is hand-written
            m = re.search(r"(?m)^- 0\.15–0\.30: \d+\s*\n", old)
            tail = old[m.end():] if m else ""
    path.write_text(md + tail)

def compare(old, new, top):
    """Before/after top-N: rank + score + tier in each run, for the same pairs. old/new = similarity dicts."""
    def index(res):
        return {(p["a"], p["b"]): (i + 1, p["score"], p["tier"]) for i, p in enumerate(res["pairs"])}
    oi, ni = index(old), index(new)
    keys = [k for k in list(ni)[:top]]
    for k in list(oi)[:top]:
        if k not in keys: keys.append(k)
    L = [f"## Before/after — {old['method']} v{old.get('version','?')} ({old['generated']}) → {new['method']} v{new['version']} ({new['generated']})", "",
         f"top-{top} union = {len(keys)} pairs · Δ = new − old score",
         "", "| a | b | old # | old score | old tier | new # | new score | new tier | Δ |",
         "|---|---|------:|----------:|----------|------:|----------:|----------|---:|"]
    for k in sorted(keys, key=lambda k: -(ni.get(k, (0, -1))[1])):
        o, n = oi.get(k), ni.get(k)
        oc = f"{o[0]} | {o[1]:.3f} | {o[2]}" if o else "– | – | –"
        nc = f"{n[0]} | {n[1]:.3f} | {n[2]}" if n else "– | – | –"
        d = f"{n[1]-o[1]:+.3f}" if o and n else "–"
        L.append(f"| {k[0]} | {k[1]} | {oc} | {nc} | {d} |")
    return "\n".join(L) + "\n"

def post(text, status):
    tok = TOKEN.read_text().strip()
    req = urllib.request.Request(f"{BRIDGE}?token={tok}", data=json.dumps({"bot": "paladin", "text": text, "status": status}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r: return r.status

def card(res, top):
    th = res["thresholds"]
    if th["locked"]:
        L = [f"DONE — similarity thresholds LOCKED by {th['locked_by']} ({th['locked_on']}) — method {res['method']}; {res['n_topics']} topics, {len(res['clusters'])} clusters.",
             f"Locked: auto-merge ≥ {th['auto']} · propose {th['propose']}–{th['auto']} · color-group only below · shared name-stem always ≥ propose."]
    else:
        L = [f"NEEDS-CHRIS — lock similarity thresholds on real numbers (method {res['method']}; {res['n_topics']} topics, {len(res['clusters'])} clusters).",
             f"Proposed: auto-merge ≥ {th['auto']} · propose {th['propose']}–{th['auto']} · color-group only below · shared name-stem always ≥ propose."]
    if res["note"]: L.append(res["note"])
    if th.get("calibrated"): L.append(f"Calibrated by {th['calibrated_by']} ({th['calibrated_on']}) against {th['calibrated_against']}.")
    L.append(f"Top {top} pairs (score tier stem):")
    for p in res["pairs"][:top]:
        L.append(f"  {p['score']:.3f} {p['tier']:<7} {'STEM ' if p['stem'] else '     '}{p['a']} ↔ {p['b']}")
    n_auto = sum(1 for p in res["pairs"] if p["tier"] == "auto"); n_prop = sum(1 for p in res["pairs"] if p["tier"] == "propose")
    n_stem = sum(1 for p in res["pairs"] if p["tier"] == "propose" and p["stem"])
    L.append(f"At these thresholds: {n_auto} auto-merge candidates, {n_prop} proposals ({n_stem} via the name-stem rule).")
    if res["method"] == "tfidf" and not th.get("calibrated"):
        sc = [p["score"] for p in res["pairs"]]
        L.append(f"CAVEAT: tfidf cosines run lower than dense-embedding cosines (max here {max(sc):.3f}; 0 pairs ≥ 0.80); these numbers are uncalibrated.")
    if not th["locked"]: L.append("Reply with numbers to lock (or GO for the proposed set).")
    return "\n".join(L)

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(flag, default, cast=float):
        return cast(a[a.index(flag) + 1]) if flag in a else default
    vault = Path(opt("--vault", VAULT, str)); provider = opt("--provider", "tfidf", str)
    if provider not in THRESHOLDS: sys.exit(f"unknown --provider {provider}; known: {sorted(THRESHOLDS)}")
    overrides = {k: opt(f"--{k}", None) for k in ("auto", "propose", "cluster")}
    overrides = {k: v for k, v in overrides.items() if v is not None}
    top = opt("--top", 20, int)
    res = run(vault, provider, overrides, top)
    md = report_md(res, top)
    print(md)
    cmp_md = ""
    if "--compare" in a:
        old = json.loads(Path(opt("--compare", "", str)).read_text())
        old = old.get("similarity", old)
        cmp_md = compare(old, res, top); print(cmp_md)
    if "--dry" in a: sys.exit(0)
    out = vault / ".system-live.json"; live = {}
    if out.exists():
        try: live = json.loads(out.read_text())
        except Exception as e: print(f"WARN existing .system-live.json unparsable ({e}); preserving nothing", file=sys.stderr)
    live["similarity"] = res
    out.write_text(json.dumps(live, ensure_ascii=False, indent=2))
    rep = vault / REPORT
    write_report(rep, md)
    if cmp_md:
        with rep.open("a") as f: f.write("\n" + cmp_md)
    print(f"wrote {out} ({out.stat().st_size} bytes, keys={list(live.keys())})\nwrote {rep}")
    if "--post" in a:
        print("bridge:", post(card(res, top), "done" if res["thresholds"]["locked"] else "needs_chris"))
