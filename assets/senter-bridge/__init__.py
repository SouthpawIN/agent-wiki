"""senter-bridge — Senter Wiki live bridge.

Runs INSIDE every Hermes process that loads plugins (each bot's `hermes -p <bot> chat -q` run,
the desktop session, gateways). Two jobs:

1. EVENTS — observe tool/turn/skill/approval lifecycle hooks and append JSON lines to
   ~/.hermes/senter-bridge/events.jsonl. (The SSE server — server.py — tails that file.)

2. APPROVALS — make bot-mode (single-query) sessions ASK instead of auto-deny:
   * export HERMES_GATEWAY_SESSION=1 so tools/approval.py takes the gateway branch;
   * register a per-session notify callback that writes the pending request to
     ~/.hermes/senter-bridge/pending/<id>.json and appends an `approval` event;
   * a background waiter polls pending/<id>.decision (written by server.py when Chris clicks
     APPROVE/DENY in the wiki) and resolves via tools.approval.resolve_gateway_approval.

Nothing here edits Hermes core. Loopback + token live in server.py.
"""
from __future__ import annotations
import json, os, threading, time, uuid
from pathlib import Path

HOME = Path(os.environ.get("HERMES_HOME") or os.path.expanduser("~/.hermes"))
# shared across profiles → always the ROOT hermes home, not a profile dir
ROOT = Path(os.path.expanduser("~/.hermes"))
BR = ROOT / "senter-bridge"; PEND = BR / "pending"; EV = BR / "events.jsonl"
BR.mkdir(parents=True, exist_ok=True); PEND.mkdir(exist_ok=True)
VAULT = Path(os.path.expanduser("~/Documents/Projects/Projects"))
_lock = threading.Lock()

def _profile() -> str:
    # profile dirs are ~/.hermes/profiles/<name>; default home → 'hermes'
    parts = HOME.parts
    if "profiles" in parts:
        return parts[parts.index("profiles") + 1]
    return os.environ.get("HERMES_PROFILE") or "hermes"

def _topic_from(*texts) -> str | None:
    """Infer the vault topic from any path-like text under topics/<name>/."""
    for t in texts:
        if not t: continue
        s = str(t)
        i = s.find("topics/")
        if i >= 0:
            rest = s[i + 7:].split("/")[0].split()[0].strip('"\'`)')
            if rest and (VAULT / "topics" / rest).exists():
                return rest
    return None

def emit(kind: str, **data) -> None:
    rec = {"ts": time.time(), "bot": _profile(), "kind": kind, **data}
    line = json.dumps(rec, ensure_ascii=False, default=str)
    with _lock:
        with EV.open("a") as f:
            f.write(line + "\n")

# ---------------------------------------------------------------- events
def _summ(v, n=160):
    s = v if isinstance(v, str) else json.dumps(v, default=str)
    return s if len(s) <= n else s[: n - 1] + "…"

def on_pre_tool(tool_name=None, params=None, **kw):
    if _rereg: _rereg()
    p = params or {}
    hint = p.get("path") or p.get("command") or p.get("workdir") or p.get("file_path") or ""
    emit("tool", tool=tool_name, phase="start", topic=_topic_from(hint, os.getcwd()), summary=_summ(hint))

def on_post_tool(tool_name=None, params=None, result=None, **kw):
    p = params or {}
    hint = p.get("path") or p.get("command") or p.get("workdir") or p.get("file_path") or ""
    ok = not (isinstance(result, str) and ('"error"' in result[:200] or result.startswith("Error")))
    emit("tool", tool=tool_name, phase="end", ok=ok, topic=_topic_from(hint, os.getcwd()), summary=_summ(hint))

def on_session_start(**kw):
    emit("turn", phase="start", topic=_topic_from(os.getcwd()), summary=_summ(kw.get("session_id") or ""))

def on_session_end(**kw):
    # status derived automatically so the wiki settles this bot's orbs/pet even if the bot forgot its DONE line
    emit("turn", phase="end", status="done", topic=_topic_from(os.getcwd()), summary="")

def on_skill(**kw):
    emit("skill", skill=kw.get("skill_name") or kw.get("name") or "", action=kw.get("event") or kw.get("action") or "", topic=_topic_from(os.getcwd()))

def on_pre_approval(command="", description="", pattern_key="", session_key="", surface="", **kw):
    emit("approval", phase="request", command=_summ(command, 400), description=description, pattern_key=pattern_key, session_key=session_key, surface=surface)

def on_post_approval(command="", description="", pattern_key="", session_key="", choice="", **kw):
    emit("approval", phase="response", command=_summ(command, 400), description=description, pattern_key=pattern_key, session_key=session_key, choice=choice)

# ------------------------------------------------------------- approvals
def _install_notify_surface():
    """Register the wiki as this session's approval surface (bot-mode sessions)."""
    try:
        from tools import approval as ap
    except Exception:
        return

    def notify(approval_data: dict) -> None:
        rid = approval_data.get("request_id") or uuid.uuid4().hex[:10]
        approval_data["request_id"] = rid
        sk = ap.get_current_session_key()
        rec = {"id": rid, "session_key": sk, "bot": _profile(), "ts": time.time(),
               "command": approval_data.get("command", ""), "description": approval_data.get("description", ""),
               "pattern_key": approval_data.get("pattern_key", "")}
        (PEND / f"{rid}.json").write_text(json.dumps(rec))
        emit("approval", phase="pending", id=rid, **{k: rec[k] for k in ("command", "description", "pattern_key", "session_key")})

        def wait():
            dec = PEND / f"{rid}.decision"
            # match approvals.timeout (default 300s) so a late click after the
            # agent has already timed out emits resolved=0 — the wiki can show
            # "expired" instead of a false "approved".
            try:
                from tools.approval import _get_approval_timeout
                tmo = int(_get_approval_timeout())
            except Exception:
                tmo = 300
            deadline = time.time() + tmo + 5
            warned = False
            while time.time() < deadline:
                if dec.exists():
                    d = json.loads(dec.read_text() or "{}")
                    choice = d.get("choice", "deny")
                    n = ap.resolve_gateway_approval(sk, choice, request_id=rid, reason=d.get("reason"))
                    emit("approval", phase="decided", id=rid, choice=choice, by=d.get("by", "chris"), resolved=n)
                    try: (PEND / f"{rid}.json").unlink(); dec.unlink()
                    except Exception: pass
                    return
                # Chris: "it might dead-fail if I don't hit allow in time" — pulse the card at 80% of the wait
                if not warned and time.time() > deadline - max(30, tmo * 0.2):
                    warned = True
                    emit("approval", phase="expiring", id=rid, remaining=int(deadline - time.time()))
                time.sleep(0.4)
            # timed out: the agent side has already given up; retire the card so replay never resurrects it
            try: (PEND / f"{rid}.json").unlink()
            except Exception: pass
            emit("approval", phase="timeout", id=rid)
            emit("message", summary="timed out waiting for approval — re-run needed", status="blocked", approval_id=rid)
        threading.Thread(target=wait, daemon=True).start()

    # The approval session key is bound per-turn by cli.py (set_current_session_key) AFTER plugins
    # register, so register lazily: on every pre_tool_call, (re)bind the notify cb to the LIVE key.
    _seen=set()
    def reg():
        # cli.py:21634 sets HERMES_SINGLE_QUERY_SESSION AFTER plugin load, so the pop must
        # happen here (post-bind), not at _install time. Flip to gateway surface so the
        # dangerous-command gate reaches _gateway_notify_cbs instead of short-circuiting
        # to single_query_mode:deny.
        try:
            os.environ["HERMES_GATEWAY_SESSION"] = "1"
            os.environ.pop("HERMES_SINGLE_QUERY_SESSION", None)
        except Exception:
            pass
        try:
            k=ap.get_current_session_key()
            if k not in _seen:
                ap.register_gateway_notify(k, notify); _seen.add(k)
                emit("bridge", phase="surface", session_key=k)
        except Exception:
            pass
    return reg

_rereg = None

def register(ctx):
    global _rereg
    ctx.register_hook("pre_tool_call", on_pre_tool)
    ctx.register_hook("post_tool_call", on_post_tool)
    ctx.register_hook("on_session_start", lambda **kw: (on_session_start(**kw), _rereg and _rereg()))
    ctx.register_hook("on_session_end", on_session_end)
    ctx.register_hook("on_skill_lifecycle", on_skill)
    ctx.register_hook("pre_approval_request", on_pre_approval)
    ctx.register_hook("post_approval_response", on_post_approval)
    # Bot-mode / -q processes have no human on stdin → the wiki becomes their approval surface.
    # The desktop app talks through tui_gateway (its own notify path) — the plugin never loads
    # HERMES_GATEWAY_SESSION into a process that already has an interactive prompt_toolkit callback.
    # Detection: `hermes chat -q` puts "-q"/"--query" in argv.
    import sys as _sys
    argv=" ".join(_sys.argv)+" "
    # -q/--query = single query; -Q = bot-mode DM delivery (tools/bot_mode_dm.py). Both are headless.
    headless = (" -q " in argv or " --query" in argv or " -Q " in argv or os.environ.get("HERMES_SINGLE_QUERY_SESSION"))
    if (headless or os.environ.get("SENTER_BRIDGE_FORCE")) and not os.environ.get("SENTER_BRIDGE_OFF"):
        _rereg = _install_notify_surface()
        emit("bridge", phase="surface-armed", argv=argv[:120])
    emit("bridge", phase="loaded", pid=os.getpid())
