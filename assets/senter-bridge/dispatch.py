#!/usr/bin/env python3
"""senter-dispatch — reliable bot handoffs. Never drops a message. Never fails silently.

  dispatch.py send <bot> "<message>"       queue a DM (idempotent id by hash)
  dispatch.py run [--parallel N]            daemon: deliver up to N queued DMs per bot
                                            concurrently (builders default 2, others 1);
                                            retry on target_busy/429; emit bridge events.
  dispatch.py status                       daemon health, LAST EXCEPTION (+timestamp),
                                            stale re-queues, per-bot queued/delivering/sent
  dispatch.py --parallel N ...             N = int (all bots) or "weaver=2,teknium=2" (per-bot)

Queue: ~/.hermes/senter-bridge/dispatch/<bot>/<ts>-<id>.txt ; delivered → .sent/ ; failed → .failed/
In-flight marker: <item>.txt.inflight (JSON: started, daemon_pid, child_pid) — on disk so that
  (1) a half-filled capacity tick never re-dispatches an item already being delivered, and
  (2) the STALE DETECTOR can see deliveries that outlived their process: any item marked
      delivering > STALE_SECS with no live child pid AND no live `hermes -p <bot> chat` process is
      re-queued (marker removed, item stays in queue) and a bridge post is emitted.
State: ~/.hermes/senter-bridge/dispatch/.state.json — daemon pid/heartbeat, last_error
  {ts, where, bot, item, error, traceback}, recent stale re-queues. `status` prints it.

The bot may run parallel deliveries; each item is dispatched independently (kanban cards own
locking/reclaim via the dispatcher). A bot is considered "busy" for
dispatch ONLY when it already has N deliveries in flight, NEVER merely because some hermes process
exists. That lets two weavers work two claimed items in parallel instead of serialising on pgrep.

SPAWN POLICY (2026-09-05, topics/senter/process/spawn-policy.md): the kanban dispatcher is the
PRIMARY fleet spawn path — deliver() routes every queued item through `hermes kanban create`
(item text becomes the card body; the worker is spawned by the gateway dispatcher, not here).
Direct `hermes -p <bot> chat` delivery is the documented EMERGENCY HATCH only: gateway down,
dispatcher stranding work, or protected-file approval context. Enable per-run with
SENTER_EMERGENCY_SPAWN=1; the default (unset) is dispatcher.
"""
import sys, os, time, json, hashlib, subprocess, glob, urllib.request, threading, traceback, signal
HOME=os.path.expanduser("~/.hermes"); Q=f"{HOME}/senter-bridge/dispatch"
PY=f"{HOME}/hermes-agent/venv/bin/python"; DM=f"{HOME}/hermes-agent/tools/bot_mode_dm.py"
TOKEN=lambda: open(f"{HOME}/senter-bridge/token").read().strip()

BUILDERS={"weaver","teknium"}          # claim-capable builder bots default to 2 concurrent deliveries
LIMITS={}                              # per-bot override (from --parallel bot=N,...)
GLOBAL=None                            # from --parallel N (applies to every bot)
STALE_SECS=600                         # delivering this long with no live pid → re-queue
DELIVER_TIMEOUT=3600

# module-level in-flight counter (thread-safe) so busy()/status() can read capacity without a pgrep
_inflight={}; _lock=threading.Lock()

def state_path(): return f"{Q}/.state.json"

def parse_parallel(args):
    """Extract --parallel from argv. Supports '--parallel N' (space) and '--parallel=N' (equals).
    Returns (remaining_args, spec-or-None)."""
    rest=[]; spec=None; i=0
    while i < len(args):
        a=args[i]
        if a=="--parallel":
            if i+1 < len(args): spec=args[i+1]; i+=2; continue
            i+=1; continue
        elif a.startswith("--parallel="):
            spec=a.split("=",1)[1]; i+=1; continue
        else:
            rest.append(a); i+=1
    return rest, spec

def apply_parallel(spec):
    global GLOBAL, LIMITS
    if spec is None: return
    spec=spec.strip()
    if "," in spec or "=" in spec:
        for kv in spec.split(","):
            k,_,v=kv.partition("=")
            if k.strip() and v.strip().isdigit(): LIMITS[k.strip()]=int(v.strip())
    elif spec.isdigit():
        GLOBAL=int(spec)

def limit(bot):
    if bot in LIMITS: return LIMITS[bot]
    if GLOBAL is not None: return GLOBAL
    return 2 if bot in BUILDERS else 1

def busy(bot):
    """Busy only when N deliveries are already in flight for this bot (N = its limit).
    The presence of a hermes process is NOT busy — parallel instances are the point."""
    with _lock: return _inflight.get(bot,0) >= limit(bot)

def running_count(bot):
    """Display/stale-check: how many hermes processes are actually running for this bot (not a dispatch gate)."""
    try:
        r=subprocess.run(f"pgrep -f 'hermes.*-p {bot} chat'", shell=True, capture_output=True, text=True)
        return len([l for l in r.stdout.splitlines() if l.strip()])
    except Exception: return 0

def pid_alive(pid):
    if not pid: return False
    try: os.kill(int(pid), 0); return True
    except ProcessLookupError: return False
    except PermissionError: return True
    except Exception: return False

# ---------- state file: heartbeat + last error + stale log (what `status` reads) ----------
def load_state():
    try: return json.load(open(state_path()))
    except Exception: return {}

def save_state(mut):
    """Apply mut(state)->None and write atomically. Never raises (state must not take the daemon down)."""
    try:
        os.makedirs(Q, exist_ok=True)
        st=load_state(); mut(st); st["updated"]=time.time()
        tmp=state_path()+".tmp"; json.dump(st, open(tmp,"w"), indent=1); os.replace(tmp, state_path())
    except Exception as e:
        print("state write error", e, file=sys.stderr, flush=True)

def record_error(where, exc, bot=None, item=None):
    """Last exception → state file + stderr + bridge post. Called from every except: in the daemon."""
    tb=traceback.format_exc() if sys.exc_info()[0] else ""
    ent={"ts": time.time(), "when": time.strftime("%Y-%m-%d %H:%M:%S"), "where": where, "bot": bot,
         "item": os.path.basename(item) if item else None, "error": f"{type(exc).__name__}: {exc}",
         "traceback": tb[-4000:]}
    def mut(st):
        st["last_error"]=ent; st["error_count"]=st.get("error_count",0)+1
        st.setdefault("recent_errors",[]).append({k:ent[k] for k in ("when","where","bot","item","error")})
        st["recent_errors"]=st["recent_errors"][-10:]
    save_state(mut)
    print(f"{ent['when']} ERROR {where} bot={bot} item={ent['item']}: {ent['error']}", flush=True)
    if tb: print(tb, flush=True)
    emit("senter", f"dispatch error in {where}" + (f" → {bot}" if bot else "") + f": {ent['error'][:160]}", "blocked")

def heartbeat():
    save_state(lambda st: st.update({"daemon_pid": os.getpid(), "last_tick": time.time(),
                                     "limits": {b: limit(b) for b in sorted(set(list(LIMITS)+list(BUILDERS)))}}))

# ---------- in-flight markers ----------
def marker(path): return path+".inflight"

def read_marker(path):
    try: return json.load(open(marker(path)))
    except Exception: return None

def write_marker(path, **kw):
    kw.setdefault("started", time.time()); kw.setdefault("daemon_pid", os.getpid())
    json.dump(kw, open(marker(path),"w"))

def clear_marker(path):
    try: os.remove(marker(path))
    except FileNotFoundError: pass

def inflight_items(bot):
    """[(path, marker_dict)] for items of this bot that carry an in-flight marker."""
    out=[]
    for m in sorted(glob.glob(f"{Q}/{bot}/*.txt.inflight")):
        p=m[:-len(".inflight")]
        if os.path.exists(p): out.append((p, read_marker(p) or {}))
        else:
            try: os.remove(m)          # orphan marker (item already moved) — clean up
            except OSError: pass
    return out

def is_stale(bot, mk, now=None):
    """Stale = delivering > STALE_SECS AND no live child pid AND no live hermes process for that bot."""
    now=now or time.time()
    if now - mk.get("started", now) < STALE_SECS: return False
    if pid_alive(mk.get("child_pid")): return False
    if running_count(bot) > 0: return False
    return True

def emit(bot, text, status="working"):
    try:
        req=urllib.request.Request(f"http://127.0.0.1:8643/post?token={TOKEN()}", data=json.dumps({"bot":bot,"text":text,"status":status}).encode(), headers={"Content-Type":"application/json"})
        urllib.request.urlopen(req, timeout=3).read()
    except Exception: pass

def send(bot, msg):
    os.makedirs(f"{Q}/{bot}", exist_ok=True)
    h=hashlib.sha1(msg.encode()).hexdigest()[:8]
    if glob.glob(f"{Q}/{bot}/*-{h}.txt") or glob.glob(f"{Q}/{bot}/.sent/*-{h}.txt"): print("dup, skipped", h); return
    p=f"{Q}/{bot}/{int(time.time())}-{h}.txt"; open(p,"w").write("Message from 🤖 senter (@senter): "+msg); print("queued", p)
    emit("senter", f"queued → {bot} ({h})", "working")

def emergency_spawn(): return os.environ.get("SENTER_EMERGENCY_SPAWN") == "1"

def deliver(bot, path):
    """Deliver one queued item.

    PRIMARY (default): create a kanban card for the item — the gateway kanban
    dispatcher spawns the worker (spawn-policy.md §1). Success = the dispatcher
    accepted the card; the worker's own bridge POSTs carry attribution.
    EMERGENCY HATCH (SENTER_EMERGENCY_SPAWN=1): run the DM delivery as a child
    directly (spawn-policy.md §2); record its pid in the in-flight marker so the
    stale detector (this daemon or a restarted one) can tell a live delivery
    from a dead one."""
    log=path+".log"
    if not emergency_spawn():
        msg=open(path).read()
        title=msg.strip().splitlines()[0][:120] if msg.strip() else os.path.basename(path)
        with open(log,"w") as lf:
            r=subprocess.run([f"{HOME}/hermes-agent/venv/bin/hermes","kanban","create",title,
                              "--body",msg,"--assignee",bot,"--json"],
                             stdout=lf, stderr=subprocess.STDOUT, timeout=60)
        out=open(log).read()
        if r.returncode==0 and '"id"' in out:
            return "ok"
        emit("senter", f"kanban create failed for {bot} ({os.path.basename(path)}) — emergency hatch is the manual fallback: SENTER_EMERGENCY_SPAWN=1. last: {out[-160:]}","blocked")
        return "unknown"
    with open(log,"w") as lf:
        p=subprocess.Popen([PY,DM,"--run-delivery","query-file",path,"hermes","-p",bot,"chat","--in","~","-c","Bot Chat","--create-if-missing","-Q"],
                           stdout=lf, stderr=subprocess.STDOUT, cwd="/tmp")
        mk=read_marker(path) or {}
        write_marker(path, bot=bot, child_pid=p.pid, started=mk.get("started", time.time()))
        try: rc=p.wait(timeout=DELIVER_TIMEOUT)
        except subprocess.TimeoutExpired:
            p.kill(); p.wait(); return "timeout"
    out=open(log).read()
    if "target_busy" in out: return "busy"
    if "429" in out and "Rate limit" in out: return "ratelimited"
    if "DONE" in out or "BLOCKED" in out or "NEEDS-CHRIS" in out or rc==0: return "ok"
    return "unknown"

def log_tail(path, n=3):
    try: return " | ".join(l.strip() for l in open(path+".log").read().splitlines()[-n:] if l.strip())[:300]
    except Exception: return ""

def requeue_stale(bot, path, mk, reason="stale"):
    """Marker gone → item is plain queued again; kill any lingering child; tell the bridge + state."""
    h=os.path.basename(path).split("-")[-1][:-4]; age=int(time.time()-mk.get("started", time.time()))
    if pid_alive(mk.get("child_pid")):
        try: os.kill(int(mk["child_pid"]), signal.SIGTERM)
        except Exception: pass
    clear_marker(path)
    if mk.get("daemon_pid")==os.getpid():
        with _lock:
            _inflight[bot]=_inflight.get(bot,0)-1
            if _inflight[bot]<=0: _inflight.pop(bot,None)
    ent={"when": time.strftime("%Y-%m-%d %H:%M:%S"), "bot": bot, "item": os.path.basename(path), "age_s": age,
         "child_pid": mk.get("child_pid"), "reason": reason, "log_tail": log_tail(path)}
    save_state(lambda st: st.update({"stale_requeues": (st.get("stale_requeues",[])+[ent])[-10:]}))
    print(f"{ent['when']} STALE {bot} {h} delivering {age}s, no live pid → re-queued", flush=True)
    emit(bot, f"stale delivery re-queued ({h}, {age//60}m in flight, no live pid)" + (f" — last: {ent['log_tail'][:120]}" if ent["log_tail"] else ""), "blocked")

def sweep_stale(bots):
    """Per tick: re-queue every stale in-flight item. Errors here are recorded, never fatal."""
    for bot in bots:
        for path, mk in inflight_items(bot):
            try:
                if is_stale(bot, mk): requeue_stale(bot, path, mk)
            except Exception as e: record_error("sweep_stale", e, bot, path)

def run():
    print("senter-dispatch on  limits=" + (",".join(f"{b}={limit(b)}" for b in sorted(set(list(LIMITS)+list(BUILDERS)))) or "default"), flush=True)
    # any exception escaping a worker thread lands in the state file, not just stderr
    threading.excepthook=lambda a: record_error("thread:"+(a.thread.name if a.thread else "?"), a.exc_value)
    save_state(lambda st: st.update({"daemon_pid": os.getpid(), "started": time.time(), "started_at": time.strftime("%Y-%m-%d %H:%M:%S")}))
    backoff={}
    def work(bot, path, h, more):
        emit("senter", f"delivering → {bot} ({h}) · {more} more queued", "working")
        try: res=deliver(bot, path)
        except Exception as e: res="unknown"; record_error("deliver", e, bot, path)
        with _lock:
            if res=="ok":
                try:
                    os.makedirs(f"{Q}/{bot}/.sent",exist_ok=True)
                    if os.path.exists(path): os.rename(path, f"{Q}/{bot}/.sent/{os.path.basename(path)}")
                    if os.path.exists(path+".log"): os.rename(path+".log", f"{Q}/{bot}/.sent/{os.path.basename(path)}.log")
                except OSError as e: record_error("move_sent", e, bot, path)
                emit("senter", f"delivered → {bot} ({h})", "done")
            elif res=="busy": backoff[bot]=time.time()+20
            elif res=="ratelimited": backoff[bot]=time.time()+90; emit(bot, "rate-limited (429) — retrying in 90s", "blocked")
            elif res=="timeout":
                backoff[bot]=time.time()+30
                record_error("deliver", TimeoutError(f"delivery exceeded {DELIVER_TIMEOUT}s, child killed"), bot, path)
            else:
                backoff[bot]=time.time()+30
                emit("senter", f"delivery → {bot} ({h}) ended without DONE/BLOCKED — retry in 30s. last: {log_tail(path)[:160]}", "blocked")
            clear_marker(path)
            _inflight[bot]=_inflight.get(bot,0)-1
            if _inflight[bot]<=0: _inflight.pop(bot,None)
        print(time.strftime("%H:%M:%S"), bot, h, res, flush=True)
    while True:
        try:
            bots=[b for b in (sorted(os.listdir(Q)) if os.path.isdir(Q) else []) if not b.startswith(".")]
            sweep_stale(bots)
            for bot in bots:
                with _lock:
                    if busy(bot) or backoff.get(bot,0)>time.time(): continue
                    # items already carrying a marker are in flight (this daemon or a previous one) — never re-dispatch
                    items=[p for p in sorted(glob.glob(f"{Q}/{bot}/*.txt")) if not os.path.exists(marker(p))]
                    if not items: continue
                    # dispatch up to the bot's remaining capacity this tick
                    cap=limit(bot)-_inflight.get(bot,0)
                    for path in items[:cap]:
                        _inflight[bot]=_inflight.get(bot,0)+1
                        write_marker(path, bot=bot, child_pid=None)
                        h=path.split("-")[-1][:-4]
                        threading.Thread(target=work, args=(bot,path,h,len(items)-1), daemon=True, name=f"deliver-{bot}-{h}").start()
            heartbeat()
        except Exception as e:
            record_error("main_loop", e)
        time.sleep(5)

def status():
    st=load_state(); now=time.time()
    dp=st.get("daemon_pid"); alive=pid_alive(dp)
    tick=st.get("last_tick"); age=f"{int(now-tick)}s ago" if tick else "never"
    print(f"daemon     pid={dp} {'alive' if alive else 'NOT RUNNING'} last_tick={age}" + (f" started={st.get('started_at')}" if st.get("started_at") else ""))
    if alive and tick and now-tick > 60: print(f"           WARNING: daemon alive but no heartbeat for {int(now-tick)}s (hung?)")
    le=st.get("last_error")
    if le:
        print(f"last_error {le.get('when')} in {le.get('where')}" + (f" → {le.get('bot')}" if le.get("bot") else "") + (f" [{le.get('item')}]" if le.get("item") else ""))
        print(f"           {le.get('error')}  (errors total: {st.get('error_count',0)})")
        tbl=[l for l in (le.get("traceback") or "").splitlines() if l.strip().startswith("File ")]
        if tbl: print(f"           at {tbl[-1].strip()}")
    else: print("last_error none")
    for s in st.get("stale_requeues",[])[-3:]:
        print(f"stale      {s['when']} {s['bot']} {s['item']} after {s['age_s']}s (child_pid={s.get('child_pid')})")
    bots=sorted(os.listdir(Q)) if os.path.isdir(Q) else []
    for bot in bots:
        if bot.startswith("."): continue
        infl=inflight_items(bot)
        q=len([p for p in glob.glob(f"{Q}/{bot}/*.txt") if not os.path.exists(marker(p))]); s=len(glob.glob(f"{Q}/{bot}/.sent/*.txt"))
        d=" ".join(f"{os.path.basename(p).split('-')[-1][:-4]}:{int(now-mk.get('started',now))//60}m{'!' if is_stale(bot,mk,now) else ''}" for p,mk in infl)
        print(f"{bot:10s} queued={q} delivering={len(infl)} sent={s} limit={limit(bot)} running={running_count(bot)}" + (f"  [{d}]" if d else ""))

if __name__=="__main__":
    a=sys.argv[1:]
    if "--parallel" in a or any(x.startswith("--parallel=") for x in a):
        a,spec=parse_parallel(a); apply_parallel(spec)
    if a and a[0]=="send": send(a[1], a[2])
    elif a and a[0]=="run": run()
    else: status()
