#!/usr/bin/env python3
"""Regenerate LIVE_SKILLS / LIVE_BOTS inside vault-live.html from the real ~/.hermes tree.

Usage:  python3 scan-live-data.py [--dry]
  --dry  print counts + JSON size, don't touch the HTML.

What it does (Senter Wiki v10 contract):
  * skills  = union of ~/.hermes/skills/**/SKILL.md and ~/.hermes/profiles/*/skills/**/SKILL.md,
              deduped by skill name, grouped by category dir, with the list of profiles carrying it.
  * bots    = every ~/.hermes/profiles/<name>/: SOUL.md description, model.default from config.yaml,
              skill count, and its fleet color.
  * splices `const LIVE_SKILLS=[...]; const LIVE_BOTS=[...];` between the markers
    `/* skills + bots` and `/* fleet chat */` in vault-live.html, then asserts the file did not shrink.

Re-run whenever Chris says "refresh senter wiki data" (until the file-watcher exists).
"""
import glob, json, os, re, sys

HERMES = os.path.expanduser("~/.hermes")
VAULT = os.path.expanduser("~/Documents/Projects/Projects")
HTML = os.path.join(VAULT, "vault-live.html")
COLORS = {"turbosovth": "#9ece6a", "klerik": "#b4f9f8", "senter": "#e0af68", "anser": "#c0caf5",
          "teknium": "#f7768e", "dogeman": "#bb9af7", "paladin": "#73daca", "weaver": "#82aaff"}


def frontmatter(path):
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def scan_skills():
    roots = [("default", os.path.join(HERMES, "skills"))]
    for p in sorted(glob.glob(os.path.join(HERMES, "profiles", "*"))):
        if os.path.isdir(os.path.join(p, "skills")):
            roots.append((os.path.basename(p), os.path.join(p, "skills")))
    skills = {}
    for owner, root in roots:
        for f in glob.glob(os.path.join(root, "**", "SKILL.md"), recursive=True):
            rel = os.path.relpath(os.path.dirname(f), root)
            parts = rel.split(os.sep)
            name = parts[-1]
            cat = "/".join(parts[:-1])   # "" = uncategorized → the UI shows it under FLEET (never "root")
            fm = frontmatter(f)
            s = skills.setdefault(name, {"name": name, "cat": cat, "desc": fm.get("description", ""), "by": [], "src": f})
            if owner not in s["by"]:
                s["by"].append(owner)
            if not s["desc"] and fm.get("description"):
                s["desc"] = fm["description"]
    return sorted(skills.values(), key=lambda s: (s["cat"], s["name"]))


# W (v14.43): the wiki opens SOUL.md / AGENTS.md / SKILL.md in its editor, but the senter-bridge GET /file
# allowlist is the vault only — so mirror those markdown files INTO the vault. The HTML tries the real
# ~/.hermes path first (works once the bridge allowlist grows) and falls back to this mirror.
MIRROR = os.path.join(VAULT, "topics", "senter-wiki", ".system", "mirror")


def mirror(skills, bots):
    import shutil
    n = 0
    for s in skills:
        dst = os.path.join(MIRROR, "skills", *( [s["cat"]] if s["cat"] else [] ), s["name"], "SKILL.md")   # same shape as the row's data-path
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(s["src"], dst); n += 1
    for b in bots:
        for fn in ("SOUL.md", "AGENTS.md"):
            src = os.path.join(HERMES, "profiles", b["name"], fn)
            if os.path.exists(src):
                dst = os.path.join(MIRROR, "bots", b["name"], fn)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst); n += 1
    return n


def scan_bots():
    bots = []
    for p in sorted(glob.glob(os.path.join(HERMES, "profiles", "*"))):
        if not os.path.isdir(p):
            continue
        name = os.path.basename(p)
        soul = os.path.join(p, "SOUL.md")
        desc = frontmatter(soul).get("description", "")
        if not desc and os.path.exists(soul):
            body = re.sub(r"^---.*?---\s*", "", open(soul, errors="ignore").read(), flags=re.S)
            first = next((l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#")), "")
            desc = first[:160]
        model = ""
        cfg = os.path.join(p, "config.yaml")
        if os.path.exists(cfg):
            m = re.search(r"^model:\s*\n(?:[ \t]+.*\n)*?[ \t]+default:\s*([^\n#]+)", open(cfg, errors="ignore").read(), re.M)
            if m:
                model = m.group(1).strip().strip('"')
        nskills = len(glob.glob(os.path.join(p, "skills", "**", "SKILL.md"), recursive=True))
        bots.append({"name": name, "desc": desc, "model": model, "skills": nskills,
                     "color": COLORS.get(name, "#b8b8b8")})
    return bots


def splice(skills, bots):
    c = open(HTML, encoding="utf-8").read()
    before = len(c)
    a = c.find("/* skills + bots")
    b = c.find("/* fleet chat */")
    assert a != -1 and b != -1 and a < b, "markers missing in vault-live.html"
    seg = c[a:b]
    # the HTML destructures ARRAYS: skills [name,cat,desc,by], bots [name,desc,model,skills,color]
    sk = [[s["name"], s["cat"], s["desc"], s["by"]] for s in skills]
    bo = [[x["name"], x["desc"], x["model"], x["skills"], x["color"]] for x in bots]
    seg = re.sub(r"const LIVE_SKILLS=\[.*?\];\n", lambda m: "const LIVE_SKILLS=" + json.dumps(sk, separators=(",", ":")) + ";\n", seg, count=1, flags=re.S)
    seg = re.sub(r"const LIVE_BOTS=\[.*?\];\n", lambda m: "const LIVE_BOTS=" + json.dumps(bo, separators=(",", ":")) + ";\n", seg, count=1, flags=re.S)
    assert "LIVE_SKILLS=" in seg and "LIVE_BOTS=" in seg, "LIVE_* declarations not found inside segment"
    c = c[:a] + seg + c[b:]
    for tok in ("topnav", "view-feed", "view-editor", "FLEET STREAM"):
        assert tok in c, f"sentinel {tok} missing after splice"
    if len(c) < before * 0.8:
        sys.exit(f"refusing to write: file shrank {before} -> {len(c)}")
    open(HTML, "w", encoding="utf-8").write(c)
    return before, len(c)


if __name__ == "__main__":
    skills, bots = scan_skills(), scan_bots()
    print(f"skills={len(skills)} categories={len({s['cat'] for s in skills})} bots={len(bots)}")
    for b in bots:
        print(f"  {b['name']:<12} {b['model']:<28} skills={b['skills']:<3} desc={'yes' if b['desc'] else 'EMPTY'}")
    if "--dry" in sys.argv:
        print("dry run; json bytes:", len(json.dumps(skills)) + len(json.dumps(bots)))
    else:
        bef, aft = splice(skills, bots)
        print(f"spliced into vault-live.html ({bef} -> {aft} chars)")
    if "--no-mirror" not in sys.argv:
        print(f"mirrored {mirror(skills, bots)} markdown files into {MIRROR}")
