"""Feed sources for the Senter Wiki FEED — real posts from integration APIs, emitted onto the bridge as
{bot:'<integration>', kind:'message', summary, url, feed:true, source, ts}. Poll every 5 min, dedupe on disk.

Sources (each only if credentialed — never guessed):
  github  — `gh` (authed): notifications + received_events for the authed login
  x       — `xurl` if installed AND `xurl auth status` reports an account (home timeline)
  rss     — `blogwatcher` CLI if installed AND it has blogs configured

Stdlib only; runs as a daemon thread inside server.py (same launchd unit). State: ~/.hermes/senter-bridge/feed-state.json
"""
import json, os, shutil, subprocess, threading, time
from pathlib import Path

POLL = 300
SEED_PER_SOURCE = 5          # first run: newest N only, so the feed isn't flooded with history
MAX_PER_TICK = 12
STATE = Path(os.path.expanduser("~/.hermes/senter-bridge/feed-state.json"))
_lock = threading.Lock()


# launchd starts the bridge with a minimal PATH — look in the usual install dirs too, never trust PATH alone
_BIN_DIRS = ["/opt/homebrew/bin", "/usr/local/bin", os.path.expanduser("~/.local/bin"), os.path.expanduser("~/go/bin"), os.path.expanduser("~/.cargo/bin"), "/usr/bin"]
def which(name):
    hit = shutil.which(name)
    if hit: return hit
    for d in _BIN_DIRS:
        c = Path(d) / name
        if c.is_file() and os.access(c, os.X_OK): return str(c)
    return None


def _run(cmd, timeout=25):
    exe = which(cmd[0])
    if not exe: return 127, "", f"{cmd[0]} not found"
    cmd = [exe] + list(cmd[1:])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout, r.stderr
    except Exception as e:
        return 1, "", str(e)


def _load():
    try:
        return json.loads(STATE.read_text())
    except Exception:
        return {"seen": {}, "sources": {}}


def _save(st):
    tmp = STATE.with_suffix(".tmp"); tmp.write_text(json.dumps(st)); tmp.replace(STATE)


# ----------------------------------------------------------------------------- github
def _gh_ok():
    if not which("gh"): return False, "gh not installed"
    rc, out, _ = _run(["gh", "api", "user", "-q", ".login"], 15)
    return (rc == 0 and out.strip() != ""), (out.strip() if rc == 0 else "gh not authed")


_title_cache = {}
def _pr_title(repo, num):
    """One cheap lookup per PR (cached for the process) so feed lines carry the title."""
    if not repo or not num: return ""
    k = f"{repo}#{num}"
    if k not in _title_cache:
        rc, out, _ = _run(["gh", "api", f"repos/{repo}/pulls/{num}", "-q", ".title"], 15)
        _title_cache[k] = out.strip()[:120] if rc == 0 else ""
        if len(_title_cache) > 400: _title_cache.pop(next(iter(_title_cache)))
    return _title_cache[k]


def _gh_items(login):
    items = []
    rc, out, _ = _run(["gh", "api", "notifications?per_page=30"], 30)
    if rc == 0:
        try:
            for n in json.loads(out):
                sub = n.get("subject") or {}; repo = (n.get("repository") or {}).get("full_name", "")
                api_url = sub.get("url") or ""; html = ""
                # notifications carry API urls; map issues/pulls to html without another call
                if "/pulls/" in api_url: html = api_url.replace("api.github.com/repos", "github.com").replace("/pulls/", "/pull/")
                elif "/issues/" in api_url: html = api_url.replace("api.github.com/repos", "github.com")
                elif "/commits/" in api_url: html = api_url.replace("api.github.com/repos", "github.com").replace("/commits/", "/commit/")
                else: html = f"https://github.com/{repo}" if repo else "https://github.com/notifications"
                items.append({"id": "ghn:" + str(n.get("id")), "ts": n.get("updated_at"),
                              "summary": f"{repo} · {sub.get('type','')} · {sub.get('title','')} · {n.get('reason','')}", "url": html})
        except Exception:
            pass
    rc, out, _ = _run(["gh", "api", f"users/{login}/received_events?per_page=30"], 30)
    if rc == 0:
        try:
            for e in json.loads(out):
                t = e.get("type", ""); repo = (e.get("repo") or {}).get("name", ""); p = e.get("payload") or {}; actor = (e.get("actor") or {}).get("login", "")
                if t in ("PullRequestEvent", "PullRequestReviewCommentEvent", "PullRequestReviewEvent"):
                    # received_events PR payloads are slim (no title/html_url) — build the html url from repo+number; title fetched lazily below
                    pr = p.get("pull_request") or {}; num = pr.get("number", ""); title = pr.get("title") or _pr_title(repo, num)
                    verb = {"PullRequestEvent": p.get("action", ""), "PullRequestReviewCommentEvent": "commented on", "PullRequestReviewEvent": "reviewed"}[t]
                    s = f"{actor} {verb} PR #{num} in {repo}" + (f": {title}" if title else ""); u = pr.get("html_url") or f"https://github.com/{repo}/pull/{num}"
                elif t in ("IssuesEvent", "IssueCommentEvent"):
                    it = p.get("issue") or {}; num = it.get("number", ""); verb = p.get("action", "") if t == "IssuesEvent" else "commented on"
                    s = f"{actor} {verb} #{num} in {repo}" + (f": {it.get('title')}" if it.get("title") else ""); u = it.get("html_url") or f"https://github.com/{repo}/issues/{num}"
                elif t == "PushEvent":
                    cs = p.get("commits") or []; s = f"{actor} pushed {len(cs)} commit(s) to {repo}" + (f": {cs[-1].get('message','').splitlines()[0][:90]}" if cs else ""); u = f"https://github.com/{repo}/commits"
                elif t == "ReleaseEvent":
                    rl = p.get("release") or {}; s = f"{actor} released {rl.get('tag_name','')} in {repo}"; u = rl.get("html_url", "")
                elif t in ("WatchEvent", "ForkEvent", "CreateEvent"):
                    s = f"{actor} {t.replace('Event','').lower()} {repo}"; u = f"https://github.com/{repo}"
                else:
                    continue
                items.append({"id": "ghe:" + str(e.get("id")), "ts": e.get("created_at"), "summary": s, "url": u})
        except Exception:
            pass
    return items


# ----------------------------------------------------------------------------- x (xurl)
def _x_ok():
    if not which("xurl"): return False, "xurl not installed"
    rc, out, err = _run(["xurl", "auth", "status"], 15)
    ok = rc == 0 and ("@" in out or "authenticated" in (out + err).lower()) and "no accounts" not in (out + err).lower()
    return ok, (out.strip()[:80] if ok else "xurl not authed")


def _x_items():
    rc, out, _ = _run(["xurl", "/2/users/me"], 20)
    try: uid = json.loads(out)["data"]["id"]
    except Exception: return []
    rc, out, _ = _run(["xurl", f"/2/users/{uid}/timelines/reverse_chronological?max_results=20&tweet.fields=created_at,author_id&expansions=author_id&user.fields=username"], 30)
    if rc != 0: return []
    try:
        j = json.loads(out); users = {u["id"]: u.get("username", "") for u in (j.get("includes") or {}).get("users", [])}
        return [{"id": "x:" + t["id"], "ts": t.get("created_at"), "summary": f"@{users.get(t.get('author_id'),'')}: {t.get('text','')[:240]}",
                 "url": f"https://x.com/{users.get(t.get('author_id'),'i')}/status/{t['id']}"} for t in j.get("data", [])]
    except Exception:
        return []


# ----------------------------------------------------------------------------- rss (blogwatcher)
def _rss_ok():
    exe = which("blogwatcher") or which("blogwatcher-cli")
    if not exe: return False, "blogwatcher not installed"
    rc, out, _ = _run([exe, "list", "--json"], 15)
    if rc != 0: rc, out, _ = _run([exe, "blogs"], 15)
    return (rc == 0 and out.strip() not in ("", "[]")), ("configured" if rc == 0 and out.strip() not in ("", "[]") else "no feeds configured")


def _rss_items():
    exe = which("blogwatcher") or which("blogwatcher-cli")
    rc, out, _ = _run([exe, "articles", "--json", "--limit", "20"], 40)
    if rc != 0: return []
    try:
        return [{"id": "rss:" + str(a.get("id") or a.get("url")), "ts": a.get("published") or a.get("date"), "summary": f"{a.get('blog') or a.get('source','')}: {a.get('title','')}", "url": a.get("url", "")} for a in json.loads(out)]
    except Exception:
        return []


SOURCES = {"github": (_gh_ok, _gh_items), "x": (_x_ok, _x_items), "rss": (_rss_ok, _rss_items)}


def tick(emit):
    """One poll of every source. Returns {source: {state, detail, new}} for /feed/status."""
    with _lock:
        st = _load(); seen = st.setdefault("seen", {}); report = {}
        for name, (ok_fn, items_fn) in SOURCES.items():
            ok, detail = ok_fn()
            if not ok:
                report[name] = {"state": "needs_login", "detail": detail, "new": 0}; continue
            items = items_fn(name == "github" and detail) if name == "github" else items_fn()
            items.sort(key=lambda i: i.get("ts") or "", reverse=True)
            src_seen = seen.setdefault(name, [])
            first_run = not src_seen
            fresh = [i for i in items if i["id"] not in src_seen]
            to_emit = fresh[:SEED_PER_SOURCE] if first_run else fresh[:MAX_PER_TICK]
            for i in reversed(to_emit):   # oldest first so the feed reads chronologically
                emit({"bot": name, "kind": "message", "feed": True, "source": name, "summary": i["summary"][:400], "url": i.get("url", ""), "posted_at": i.get("ts")})
            src_seen.extend(i["id"] for i in fresh)          # everything fetched counts as seen (seed skips history silently)
            del src_seen[:-500]
            report[name] = {"state": "connected", "detail": detail, "new": len(to_emit), "fetched": len(items)}
        st["sources"] = report; st["last_tick"] = time.time(); _save(st)
        return report


def start(emit, poll=POLL):
    def loop():
        time.sleep(3)
        while True:
            try: tick(emit)
            except Exception: pass
            time.sleep(poll)
    threading.Thread(target=loop, daemon=True, name="feed-sources").start()


def status():
    st = _load(); return {"last_tick": st.get("last_tick"), "sources": st.get("sources", {}), "poll": POLL}
