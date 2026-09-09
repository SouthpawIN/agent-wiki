#!/usr/bin/env python3
"""
merge-topics.py — topic consolidation for the agent-wiki vault (paladin, v1.1.0)

Plan of record: topics/senter/plans/topic-consolidation-2026-09-02.md
Final table = anser's audit (2026-09-02), accepted in full by senter's re-confirm.
v1.1.0: Chris GO (2026-09-02, 'yes on everything') + rulings veiled -> music, aichess -> legacy-bots.

    python3 assets/merge-topics.py                 # DRY RUN (default): prints the diff summary
    python3 assets/merge-topics.py --post          # dry run + POST one-screen summary to the bridge
    python3 assets/merge-topics.py --execute --approved-by chris   # the real run (once Chris approves)

Hard rules (SOUL):
  * Nothing is deleted. Absorbed topics are MOVED to topics/_archive/<name>/.
  * Every target README gets a `## Absorbed` list (original name + date + prior status)
    and a `## Repos` table (one row per repo the topic now serves).
  * Each absorbed topic's .system/ contents land in the target's .system/session.md under
    `## 2026-09-02 — absorbed <name>`; the archive keeps the verbatim originals.
  * [[wikilinks]] across the vault are rewritten:
        [[topics/<absorbed>/README...]]  -> [[topics/<target>/README...]]
        [[topics/<absorbed>/<other>...]] -> [[topics/_archive/<absorbed>/<other>...]]
        [[<absorbed>]] / [[<absorbed>|    -> [[<target>]] / [[<target>|
    Files under topics/_archive/ are never touched.
  * index.md + catalogs/topic-index.md + catalogs/fleet-dashboard.md are regenerated after.
  * Execution refuses to run without --approved-by, and refuses if any archive dir already exists.
"""
from __future__ import annotations

import argparse, json, os, re, shutil, sys, tarfile, time, urllib.request
from datetime import date
from pathlib import Path

VERSION = "1.1.0"
VAULT = Path(__file__).resolve().parent.parent
TOPICS = VAULT / "topics"
ARCHIVE = TOPICS / "_archive"
CATALOGS = VAULT / "catalogs"
PLAN = "topics/senter/plans/topic-consolidation-2026-09-02.md"
TODAY = date.today().isoformat()
BRIDGE = "http://127.0.0.1:8643/post"
TOKEN_FILE = Path.home() / ".hermes/senter-bridge/token"

# --------------------------------------------------------------------------------------
# THE MANIFEST — anser's final table. target -> (purpose line, [absorbed...])
# New targets (no existing topics/<target>/) are created by the script.
# --------------------------------------------------------------------------------------
MERGES: dict[str, tuple[str, list[str]]] = {
    "pocket-shop": (
        "Automated MTG card shop (browser automation for Gmail, TCGPlayer, MTGStocks) and its pricing feature.",
        ["pocket-shop-pricing"]),
    "turbofit": (
        "TurboFit — hardware-aware adaptive Hermes runtime; the whole TurboHaul / hardware-fit lineage (sirvir = old bot name).",
        ["turbohaul-llmfit", "turbohaul-manager", "southpaw-turbohaul", "sirvir"]),
    "hermes-agent": (
        "Hermes Agent runtime, forks, Android builds, configs and test scaffolds.",
        ["hermes-android", "hermes-test-skill", "herm-sovth", "sovth-config", "nous-test", "test-bot", "openskills"]),
    "senter": (
        "The coordinator bot and its own history, tools and orchestration experiments.",
        ["senter-consolidation", "senter-archive", "senter-mcp-server", "senter-alignment-arxivddl", "dev-orch"]),
    "senter-wiki": (
        "The Senter Wiki product surface (vault-live.html) — weaver's topic; hermes-wiki-dashboard was its earlier name.",
        ["hermes-wiki-dashboard"]),
    "omnisenter-models": (
        "The OmniSenter / OmniStep model family: base models, fusion, multimodal expansion, training data and the model blog.",
        ["sovthpaw-omni-senter-3b", "sovthpaw-omnisenter-base-16b", "sovthpaw-omnistep-12a3b", "sovthpaw-omnistep-new",
         "sovthpaw-senter-omni-data", "omnistep-fusion", "multimodal-expansion", "omnisenter-blog"]),
    "evolutionary": (
        "Evolutionary ML research — model merging and training (the Darwin family).",
        ["evolutionary-model-merging", "evolutionary-training"]),
    "music": (
        "Generative music/audio products: DAW, terminal radio, music LoRA pipeline, lyric companion, evolution radio.",
        ["ace-step-daw", "jammit", "hermes-music-lora-pipeline", "llmc", "evolutionary-radio", "veiled"]),
    "nous-community": (
        "Nous community bots, Discord archive, style guide and companions.",
        ["nous-girl", "nous-girl-agent", "nous-discord-archive", "nous-style-guide", "discordsam", "jestur"]),
    "youtube": (
        "dogeman's content + publishing surfaces (YouTube, personal site, infographics).",
        ["southpawin-github-io", "benchmark-infographics"]),
    "dev-tooling": (
        "Coding-assistant experiments: coder/review agents, sidecar, niwa, minimal Claude-Code alternative.",
        ["dev-coder", "dev-review", "sidecar", "niwa", "flavored-nanocode"]),
    "legacy-bots": (
        "Retired bot profiles and dormant one-off projects with no product continuity (kept for history).",
        ["frieza", "chizul", "aichess"]),
}
# Explicitly kept as their own topics (anser pulled these out / never merged):
KEEP = ["anser", "klerik", "_global", "memento", "pirouette-framework-core-003", "crow", "kashik", "burner-phone"]
# v1.1.0: aichess + veiled (orphans of the dropped games-and-toys row) were ruled by Chris on
# 2026-09-02 ('yes on everything'): veiled -> music, aichess -> legacy-bots. Nothing is unassigned.
UNASSIGNED: list[str] = []

# --------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

def frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm

def readme_meta(topic: str) -> dict:
    """Pull the facts we need from a topic README (frontmatter + Facts + blockquote)."""
    text = read(TOPICS / topic / "README.md")
    fm = frontmatter(text)
    desc = ""
    m = re.search(r"^> (.+)$", text, re.M)
    entity = "idea-wiki/entities/" in text and "absorbed verbatim below" in text
    if m:
        desc = m.group(1).strip()
    elif entity:  # senter-consolidation entity page: describe by embedded title + source kind
        et = re.search(r"^title: (.+)$", text, re.M)
        src = re.search(r'sources: \["raw/([a-z]+)/', text)
        desc = f"idea-wiki entity `{et.group(1).strip() if et else topic}`" + (f" (from {src.group(1)})" if src else "")
    else:  # other non-repo READMEs: first non-heading prose line
        for line in text.splitlines():
            s = line.strip()
            if s and not s.startswith(("#", "---", "title:", "created:", "updated:", "type:", "tags:", "sources:", "confidence:", "repo:", "status:")):
                desc = s; break
    desc = re.sub(r"\*\*", "", desc)
    if len(desc) > 140:
        desc = desc[:137].rstrip() + "…"
    stars = re.search(r"\*\*Stars / forks:\*\* (\d+)", text)
    push = re.search(r"\*\*Last push:\*\* (\d{4}-\d{2}-\d{2})", text)
    status = re.search(r"\*\*Status:\*\* ([^\n]+)", text)
    st = status.group(1).strip() if status else fm.get("status", "").upper()
    if not st:
        st = "ENTITY (idea-wiki capture)" if entity else "NOTE (no repo)"
    return {
        "name": topic,
        "title": fm.get("title", topic),
        "repo": fm.get("repo", ""),
        "status_fm": fm.get("status", ""),
        "status": st,
        "stars": int(stars.group(1)) if stars else 0,
        "push": push.group(1) if push else "—",
        "desc": desc,
    }

def absorbed_block(target: str, names: list[str]) -> str:
    lines = [f"## Absorbed", f"_Consolidated {TODAY} per [[{PLAN[:-3]}|topic-consolidation-2026-09-02]]. Originals live verbatim under `topics/_archive/`._", ""]
    for n in names:
        m = readme_meta(n)
        d = f" — {m['desc']}" if m["desc"] else ""
        lines.append(f"- [[topics/_archive/{n}/README|{n}]]{d} (absorbed {TODAY}; was {m['status']})")
    return "\n".join(lines) + "\n"

def repos_block(target: str, names: list[str]) -> str:
    rows = []
    own = readme_meta(target) if (TOPICS / target / "README.md").exists() else None
    if own and own["repo"]:
        rows.append(f"| {target} | [repo]({own['repo']}) | {own['status']} | {own['stars']} |")
    for n in names:
        m = readme_meta(n)
        if m["repo"]:
            rows.append(f"| {n} | [repo]({m['repo']}) | {m['status']} | {m['stars']} |")
        else:
            rows.append(f"| {n} | _(no repo — {m['status'].lower()})_ | {m['status']} | — |")
    return "## Repos\n| Repo | Link | Status | ⭐ |\n|---|---|---|---|\n" + "\n".join(rows) + "\n"

def new_readme(target: str, purpose: str, names: list[str]) -> str:
    metas = [readme_meta(n) for n in names]
    active = any("ACTIVE" in m["status"] for m in metas)
    return (
        f"---\ntitle: {target}\nupdated: {TODAY}\ntype: topic\nstatus: {'active' if active else 'dormant'}\ntags: [topic, merged]\n---\n\n"
        f"# {target}\n\n> {purpose}\n\n"
        f"_Topic created {TODAY} by paladin (merge-topics.py v{VERSION}) — one continuity for the repos below._\n\n"
    )

def session_entry(name: str, target: str) -> str:
    """The dated heading + content that lands in the target's session.md."""
    sysdir = TOPICS / name / ".system"
    parts = [f"\n## {TODAY} — absorbed {name}\n",
             f"_Merged into `{target}` by merge-topics.py v{VERSION}. Verbatim originals: `topics/_archive/{name}/.system/`._\n"]
    sess = read(sysdir / "session.md").strip()
    if sess:
        parts.append(f"\n### session.md (from {name})\n\n{sess}\n")
    cont = read(sysdir / "continuity.md").strip()
    if cont:
        parts.append(f"\n### continuity.md (from {name})\n\n{cont}\n")
    q = read(sysdir / "queue.md")
    items = [l for l in q.splitlines() if l.strip().startswith("- [") and "*(empty)*" not in l]
    if items:
        parts.append(f"\n### open queue items (from {name})\n\n" + "\n".join(items) + "\n")
    return "".join(parts)

# --------------------------------------------------------------------------------------
# wikilink rewrite
# --------------------------------------------------------------------------------------
def link_rewrites(absorbed_to_target: dict[str, str]) -> list[tuple[re.Pattern, str]]:
    rules = []
    for a, t in absorbed_to_target.items():
        ea = re.escape(a)
        rules.append((re.compile(rf"\[\[topics/{ea}/README(?=[|\]#])"), f"[[topics/{t}/README"))
        rules.append((re.compile(rf"\[\[topics/{ea}/(?!README)"), f"[[topics/_archive/{a}/"))
        rules.append((re.compile(rf"\[\[{ea}(?=[|\]#])"), f"[[{t}"))
    return rules

def md_files_for_rewrite():
    for p in VAULT.rglob("*.md"):
        rel = p.relative_to(VAULT)
        if rel.parts[0] in ("assets", "node_modules") or rel.parts[:2] == ("topics", "_archive"):
            continue
        yield p

def plan_rewrites(rules) -> dict[Path, tuple[str, int]]:
    out = {}
    for p in md_files_for_rewrite():
        text = read(p); new = text; n = 0
        for rx, rep in rules:
            new, k = rx.subn(rep, new); n += k
        if n:
            out[p] = (new, n)
    return out

# --------------------------------------------------------------------------------------
# catalogs
# --------------------------------------------------------------------------------------
def status_rank(s: str) -> int:
    return 0 if "ACTIVE" in s else (2 if "ARCHIVED" in s else 1)

def live_topics() -> list[str]:
    return sorted(d.name for d in TOPICS.iterdir() if d.is_dir() and d.name != "_archive")

def regen_catalogs(planned_targets: set[str]) -> dict[Path, str]:
    """Return {path: new_text} for index.md, topic-index.md, fleet-dashboard.md."""
    rows = []
    for t in live_topics():
        m = readme_meta(t)
        readme = read(TOPICS / t / "README.md")
        repos = len(re.findall(r"^\| [^|]+ \| (\[repo\]|_\(no repo)", readme, re.M))
        absorbed = len(re.findall(r"^- \[\[topics/_archive/", readme, re.M))
        rows.append({**m, "repos": max(repos, 1 if m["repo"] else 0), "absorbed": absorbed})
    rows.sort(key=lambda r: (status_rank(r["status"]), -(int(r["push"].replace("-", "")) if r["push"] != "—" else 0)))
    n_topics = len(rows); n_active = sum(1 for r in rows if "ACTIVE" in r["status"])
    n_repos = sum(r["repos"] for r in rows); n_archived = len([d for d in ARCHIVE.iterdir() if d.is_dir() and not d.name.startswith(".")]) if ARCHIVE.exists() else 0

    ti = [f"---\ntitle: Topic Index\nupdated: {TODAY}\ntype: catalog\n---\n\n# Topic Index\n\n"
          f"{n_topics} topics (one continuity each) serving {n_repos} repos · {n_archived} originals archived under `topics/_archive/` on consolidation. Active first.\n\n"
          "| Topic | Purpose | Repos | Absorbed | Status | ⭐ |\n|---|---|---|---|---|---|"]
    for r in rows:
        ti.append(f"| [[topics/{r['name']}/README|{r['name']}]] | {r['desc'][:90]} | {r['repos']} | {r['absorbed']} | {r['status']} | {r['stars']} |")
    fd = [f"---\ntitle: Fleet Dashboard\nupdated: {TODAY}\ntype: catalog\n---\n\n# Fleet Dashboard\n\n"
          f"**{n_topics} topics · {n_active} active · {n_repos} repos · {n_archived} archived originals**\n\n"
          "| Topic | Last push | Status |\n|---|---|---|"]
    for r in rows:
        fd.append(f"| [[topics/{r['name']}/README|{r['name']}]] | {r['push']} | {r['status']} |")
    idx = read(VAULT / "index.md")
    idx = re.sub(r"\[\[catalogs/topic-index\|Topic Index\]\] — [^\n]*",
                 f"[[catalogs/topic-index|Topic Index]] — {n_topics} topics · {n_repos} repos", idx)
    idx = re.sub(r"^updated: .*$", f"updated: {TODAY}", idx, count=1, flags=re.M)
    if "## Consolidation" not in idx:
        idx = idx.rstrip("\n") + (f"\n\n## Consolidation ({TODAY})\n63 topic dirs → {n_topics} continuities per [[{PLAN[:-3]}|the consolidation plan]]. "
                                 f"Absorbed originals are archived verbatim under `topics/_archive/<name>/`; every merged README lists them under `## Absorbed`.\n")
    return {CATALOGS / "topic-index.md": "\n".join(ti) + "\n",
            CATALOGS / "fleet-dashboard.md": "\n".join(fd) + "\n",
            VAULT / "index.md": idx}

# --------------------------------------------------------------------------------------
# plan + execute
# --------------------------------------------------------------------------------------
def build_plan():
    problems = []
    a2t = {}
    # 2026-09-03 LOCKS (Chris: wiki LOCK pill): topics/<t>/.system/lock.json {"locked": true} protects a topic
    # from auto-merge — a locked source OR target turns the run into a PROBLEM (execution refuses).
    def is_locked(n):
        lf = TOPICS / n / ".system" / "lock.json"
        try:
            return lf.exists() and bool(json.loads(lf.read_text()).get("locked"))
        except Exception:
            return False
    for t, (_, names) in MERGES.items():
        if is_locked(t): problems.append(f"merge target LOCKED by Chris: topics/{t} (unlock or remove from plan)")
        for n in names:
            if n in a2t: problems.append(f"{n} listed twice ({a2t[n]}, {t})")
            a2t[n] = t
            if not (TOPICS / n).is_dir(): problems.append(f"absorbed topic missing: topics/{n}")
            if ARCHIVE.joinpath(n).exists(): problems.append(f"archive already exists: topics/_archive/{n}")
            if is_locked(n): problems.append(f"absorbed topic LOCKED by Chris: topics/{n} (unlock or remove from plan)")
    all_dirs = set(live_topics())
    accounted = set(a2t) | set(MERGES) | set(KEEP) | set(UNASSIGNED)
    unaccounted = sorted(all_dirs - accounted)
    if unaccounted: problems.append(f"topic dirs not in manifest: {unaccounted}")
    rules = link_rewrites(a2t)
    rewrites = plan_rewrites(rules)
    return a2t, rewrites, problems

def render_full(a2t, rewrites, problems) -> str:
    new_targets = [t for t in MERGES if not (TOPICS / t).is_dir()]
    n_dirs = len(live_topics())
    L = [f"# merge-topics.py v{VERSION} — DRY RUN {TODAY}", "",
         f"Plan: `{PLAN}` (anser audit signed · senter re-confirm ACCEPT · Chris GO 2026-09-02).",
         f"Topic dirs now: {n_dirs} → after: {n_dirs - len(a2t) + len(new_targets)} "
         f"({len(a2t)} absorbed, {len(new_targets)} new targets created, {len(KEEP)} kept, {len(UNASSIGNED)} unassigned).", ""]
    if problems:
        L += ["## ⚠️ PROBLEMS (execution would refuse)"] + [f"- {p}" for p in problems] + [""]
    L.append("## 1. Moves — `absorbed → target` (original goes to `topics/_archive/<absorbed>/`)")
    for t, (_, names) in MERGES.items():
        tag = " (NEW topic)" if t in new_targets else ""
        for n in names:
            L.append(f"- {n} → {t}{tag}")
    L += ["", f"Kept as own topics: {', '.join(KEEP)}",
          (f"UNASSIGNED (left untouched, need a ruling): {', '.join(UNASSIGNED)}" if UNASSIGNED
           else "Unassigned: none (Chris ruled veiled → music, aichess → legacy-bots)."), ""]
    total = sum(n for _, n in rewrites.values())
    regen = {CATALOGS / 'topic-index.md', CATALOGS / 'fleet-dashboard.md'}
    kept_rw = {p: v for p, v in rewrites.items() if p not in regen}
    L.append(f"## 2. Wikilinks rewritten: {total} in {len(rewrites)} files "
             f"({sum(n for _, n in kept_rw.values())} in hand-maintained files; the rest in catalogs that are regenerated anyway)")
    for p, (_, n) in sorted(rewrites.items(), key=lambda kv: -kv[1][1]):
        L.append(f"- {p.relative_to(VAULT)}: {n}{'  (regenerated)' if p in regen else ''}")
    L += ["", "## 3. `## Absorbed` blocks each target README gains"]
    for t, (purpose, names) in MERGES.items():
        L.append(f"\n### {t}{' — NEW: ' + purpose if t in new_targets else ''}")
        L.append("```")
        L.append(absorbed_block(t, names).rstrip())
        L.append(repos_block(t, names).rstrip())
        L.append("```")
    L += ["", "## 4. session.md moves (absorbed `.system/` → target `.system/session.md`, dated heading)"]
    for t, (_, names) in MERGES.items():
        for n in names:
            sysdir = TOPICS / n / ".system"
            has = [f for f in ("session.md", "continuity.md", "queue.md", "injections.md") if (sysdir / f).exists()]
            sess = len(read(sysdir / "session.md").splitlines())
            L.append(f"- {n} → topics/{t}/.system/session.md  `## {TODAY} — absorbed {n}`  "
                     f"(session.md {sess} lines{', + continuity' if 'continuity.md' in has else ''}; injections.md stays in archive)")
    L += ["", "## 5. After: regenerate index.md, catalogs/topic-index.md, catalogs/fleet-dashboard.md; "
          "append `## Archived` footer to each archived README pointing at its target.", ""]
    return "\n".join(L) + "\n"

def render_short(a2t, rewrites, problems) -> str:
    new_targets = [t for t in MERGES if not (TOPICS / t).is_dir()]
    n_dirs = len(live_topics())
    total = sum(n for _, n in rewrites.values())
    L = [f"paladin · merge-topics.py v{VERSION} DRY RUN — NEEDS-CHRIS approval to execute",
         f"{n_dirs} topic dirs → {n_dirs - len(a2t) + len(new_targets)} · {len(a2t)} absorbed → topics/_archive/ (nothing deleted) · {len(new_targets)} new topics · {total} wikilinks rewritten in {len(rewrites)} files"]
    for t, (_, names) in MERGES.items():
        L.append(f"  {t}{' [NEW]' if t in new_targets else ''} ← {', '.join(names)}")
    L.append(f"  kept: {', '.join(KEEP)}")
    if UNASSIGNED: L.append(f"  UNASSIGNED (untouched; ruling needed): {', '.join(UNASSIGNED)}")
    L.append("Each target README gains ## Absorbed + ## Repos; each absorbed .system/ → target session.md under a dated heading; index.md + catalogs regenerated after.")
    if problems:
        L.append("PROBLEMS: " + " | ".join(problems))
    L.append(f"Full diff: topics/senter/plans/topic-consolidation-2026-09-02.dryrun.md · run: python3 assets/merge-topics.py --execute --approved-by chris")
    return "\n".join(L)

def post_bridge(text: str, status: str = "needs_chris") -> bool:
    if not TOKEN_FILE.exists():
        print("[bridge] no token file; skipping post", file=sys.stderr); return False
    tok = TOKEN_FILE.read_text().strip()
    body = json.dumps({"bot": "paladin", "text": text, "status": status}).encode()
    req = urllib.request.Request(f"{BRIDGE}?token={tok}", data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return json.loads(r.read() or b"{}").get("ok", False)
    except Exception as e:
        print(f"[bridge] post failed: {e}", file=sys.stderr); return False

def execute(a2t, rewrites, problems, approved_by: str, snapshot: bool):
    if problems:
        sys.exit("REFUSING to execute — problems:\n  " + "\n  ".join(problems))
    log = VAULT / "assets" / "merge-topics.log.jsonl"
    def rec(**kw):
        with log.open("a") as f: f.write(json.dumps({"ts": time.time(), "v": VERSION, **kw}) + "\n")
    rec(event="start", approved_by=approved_by, absorbed=len(a2t))
    ARCHIVE.mkdir(exist_ok=True)
    if snapshot:
        snap_dir = ARCHIVE / ".snapshots"; snap_dir.mkdir(exist_ok=True)
        snap = snap_dir / f"{TODAY}-pre-merge-topics.tar.gz"
        if not snap.exists():
            with tarfile.open(snap, "w:gz") as tf:
                for p in (TOPICS, CATALOGS, VAULT / "index.md"):
                    tf.add(p, arcname=str(p.relative_to(VAULT)), filter=lambda ti: None if "/_archive/.snapshots" in ti.name else ti)
            rec(event="snapshot", path=str(snap.relative_to(VAULT)))
    # 1) wikilinks first (absorbed READMEs still in place for meta reads; archive is excluded anyway)
    for p, (new, n) in rewrites.items():
        p.write_text(new, encoding="utf-8"); rec(event="rewrite", file=str(p.relative_to(VAULT)), links=n)
    # 2) per target: README blocks + session.md, then move originals
    for t, (purpose, names) in MERGES.items():
        tdir = TOPICS / t; tsys = tdir / ".system"
        tsys.mkdir(parents=True, exist_ok=True)
        rd = tdir / "README.md"
        if not rd.exists():
            rd.write_text(new_readme(t, purpose, names), encoding="utf-8")
            for f, body in (("continuity.md", f"# Continuity — {t}\n\n{purpose}\n\nCreated {TODAY} by merge-topics.py; edit to correct my understanding.\n"),
                            ("queue.md", "# Queue\n\n## [SKILLS]\n- [ ] *(empty)*\n## [AGENTS]\n- [ ] *(empty)*\n## [LOOPS]\n- [ ] *(empty)*\n"),
                            ("injections.md", f"# Injections — {t}\n\n[UNREAD] {TODAY} topic created by consolidation (merge-topics.py v{VERSION}).\n")):
                if not (tsys / f).exists(): (tsys / f).write_text(body, encoding="utf-8")
            for sub in ("skills", "agents", "loops"): (tdir / sub).mkdir(exist_ok=True)
            rec(event="create_topic", topic=t)
        text = read(rd)
        text = re.sub(r"^updated: .*$", f"updated: {TODAY}", text, count=1, flags=re.M)
        text = text.rstrip("\n") + "\n\n" + absorbed_block(t, names) + "\n" + repos_block(t, names)
        rd.write_text(text, encoding="utf-8")
        sess = tsys / "session.md"
        if not sess.exists():
            sess.write_text(f"---\ntitle: session-state\nupdated: {TODAY}\ntype: session\n---\n\n# Session — {t}\n", encoding="utf-8")
        with sess.open("a", encoding="utf-8") as f:
            for n in names: f.write(session_entry(n, t))
        rec(event="target_updated", topic=t, absorbed=names)
        for n in names:
            src = TOPICS / n; dst = ARCHIVE / n
            shutil.move(str(src), str(dst))
            ar = dst / "README.md"
            with ar.open("a", encoding="utf-8") as f:
                f.write(f"\n\n## Archived\nArchived {TODAY} — absorbed into [[topics/{t}/README|{t}]] by merge-topics.py v{VERSION}. Nothing here was deleted or rewritten.\n")
            rec(event="archive", topic=n, target=t, to=str(dst.relative_to(VAULT)))
    # 3) catalogs
    for p, txt in regen_catalogs(set(MERGES)).items():
        p.write_text(txt, encoding="utf-8"); rec(event="regen", file=str(p.relative_to(VAULT)))
    rec(event="done", topics_after=len(live_topics()))
    print(f"EXECUTED. topics now: {len(live_topics())}; archived: {len(a2t)}; log: {log.relative_to(VAULT)}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--execute", action="store_true", help="perform the merge (default is dry-run)")
    ap.add_argument("--approved-by", default="", help="required with --execute (e.g. chris)")
    ap.add_argument("--post", action="store_true", help="POST the one-screen summary to the bridge")
    ap.add_argument("--no-snapshot", action="store_true", help="skip the pre-run tar.gz snapshot")
    ap.add_argument("--out", default=str(VAULT / "topics/senter/plans/topic-consolidation-2026-09-02.dryrun.md"),
                    help="where to write the full dry-run report")
    a = ap.parse_args()
    a2t, rewrites, problems = build_plan()
    full = render_full(a2t, rewrites, problems)
    short = render_short(a2t, rewrites, problems)
    if a.execute:
        if not a.approved_by:
            sys.exit("REFUSING: --execute requires --approved-by <name> (Chris approves the run once).")
        execute(a2t, rewrites, problems, a.approved_by, snapshot=not a.no_snapshot)
        if a.post:
            post_bridge(f"DONE — merge-topics.py v{VERSION} executed (approved by {a.approved_by}): {len(a2t)} topics archived, {len(live_topics())} continuities remain; index + catalogs regenerated.", "done")
        return
    Path(a.out).write_text(full, encoding="utf-8")
    print(full)
    print("=" * 78); print(short)
    if a.post:
        ok = post_bridge(short, "needs_chris")
        print(f"[bridge] posted: {ok}")

if __name__ == "__main__":
    main()
