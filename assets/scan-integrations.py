#!/usr/bin/env python3
"""Scan Hermes Agent integration state for Senter Wiki INTEGRATIONS + FEED rail.

Writes:
  - .system-live.json (vault root) integrations[] : {name, kind, state, credential_names_present, last_activity}
    (preserves existing skills/bots)
  - topics/senter-wiki/.system/live-integrations.json (legacy rows + new object with integrations for vault-live.html)
Usage: hermes venv python assets/scan-integrations.py [--dry]
"""
import json, os, re, subprocess, sys, time, datetime
from pathlib import Path

HERMES = Path.home() / ".hermes"
VAULT = Path.home() / "Documents/Projects/Projects"
OUT_LEGACY = VAULT / "topics/senter-wiki/.system/live-integrations.json"
OUT_LIVE = VAULT / ".system-live.json"
HERMES_AGENT = HERMES / "hermes-agent"

# Inventory from Ideas.md 2026-09-02 — single source, never invented beyond this + filesystem enumeration
INV_PLATFORMS = [
    "discord","slack","telegram","whatsapp","whatsapp_cloud","signal","email","sms","teams",
    "google_chat","matrix","mattermost","irc","line","feishu","dingtalk","wecom","weixin",
    "qqbot","yuanbao","bluebubbles","homeassistant","ntfy","simplex","photon","raft","buzz","a2a","webhook","api_server"
]
INV_PLUGINS = [
    "spotify","google_meet","teams_pipeline","browser","image_gen","video_gen","web","kanban",
    "observability","hermes-achievements","memory","context_engine","model-providers","cron_providers",
    "senter-bridge","turbofit"
]
# API-bearing skills — each key maps to one or more skill dirs
INV_SKILLS = {
    "github": ["github/codebase-inspection","github/github-auth","github/github-code-review","github/github-issue-to-pr","github/github-issues","github/github-pr-workflow","github/github-repo-management"],
    "xurl": ["social-media/xurl"],
    "himalaya": ["email/himalaya"],
    "google-workspace": ["productivity/google-workspace"],
    "notion": ["productivity/notion"],
    "airtable": ["productivity/airtable"],
    "box": ["productivity/box"],
    "youtube-content": ["media/youtube-content"],
    "gif-search": ["media/gif-search"],
    "apple": ["apple/apple-notes","apple/apple-reminders","apple/findmy","apple/imessage"],
    "openhue": ["smart-home/openhue"],
    "maps": ["productivity/maps"],
    "arxiv": ["research/arxiv"],
    "blogwatcher": ["research/blogwatcher"],
    "huggingface-hub": ["mlops/huggingface-hub"],
    "weights-and-biases": ["mlops/weights-and-biases"],
}

# credential env var mapping (names only, never values)
SKILL_CRED_MAP = {
    "github": ["GITHUB_TOKEN","GH_TOKEN"],
    "xurl": ["X_BEARER_TOKEN","TWITTER_BEARER_TOKEN","X_CONSUMER_KEY"],
    "himalaya": ["HIMALAYA","IMAP_HOST","SMTP_HOST"],
    "google-workspace": ["GOOGLE_CLIENT_ID","GOOGLE_API_KEY","GOOGLE_CREDENTIALS"],
    "notion": ["NOTION_API_KEY","NOTION_TOKEN"],
    "airtable": ["AIRTABLE_API_KEY","AIRTABLE_TOKEN"],
    "box": ["BOX_CLIENT_ID","BOX_API_KEY"],
    "youtube-content": ["YOUTUBE_API_KEY","YT_API_KEY"],
    "gif-search": ["TENOR_API_KEY","GIPHY_API_KEY"],
    "apple": [],
    "openhue": ["HUE_BRIDGE_IP","OPENHUE"],
    "maps": ["MAPS_API_KEY","ORS_API_KEY","OPENROUTE"],
    "arxiv": [],
    "blogwatcher": [],
    "huggingface-hub": ["HF_TOKEN","HUGGINGFACE_TOKEN","HUGGING_FACE_HUB_TOKEN"],
    "weights-and-biases": ["WANDB_API_KEY","WANDB_TOKEN"],
}
PLATFORM_CRED_HINT = {
    "telegram": ["TELEGRAM_BOT_TOKEN","TELEGRAM_TOKEN"],
    "discord": ["DISCORD_TOKEN","DISCORD_BOT_TOKEN"],
    "slack": ["SLACK_BOT_TOKEN","SLACK_TOKEN"],
    "whatsapp": ["WHATSAPP_TOKEN"],
    "whatsapp_cloud": ["WHATSAPP_CLOUD","WHATSAPP_CLOUD_TOKEN"],
    "signal": ["SIGNAL"],
    "email": ["EMAIL","SMTP","IMAP"],
    "sms": ["TWILIO","SMS_"],
    "teams": ["TEAMS","MSGRAPH"],
    "google_chat": ["GOOGLE_CHAT"],
    "matrix": ["MATRIX_TOKEN"],
    "mattermost": ["MATTERMOST"],
    "irc": ["IRC_"],
    "line": ["LINE_"],
    "feishu": ["FEISHU"],
    "dingtalk": ["DINGTALK"],
    "wecom": ["WECOM"],
    "weixin": ["WEIXIN"],
    "qqbot": ["QQBOT","QQ_"],
    "yuanbao": ["YUANBAO"],
    "bluebubbles": ["BLUEBUBBLES"],
    "homeassistant": ["HOMEASSISTANT_TOKEN","HASS_TOKEN"],
    "ntfy": ["NTFY"],
    "simplex": ["SIMPLEX"],
    "photon": ["PHOTON"],
    "raft": ["RAFT"],
    "buzz": ["BUZZ"],
    "a2a": ["A2A"],
    "webhook": ["WEBHOOK"],
    "api_server": ["API_SERVER_TOKEN","GATEWAY_TOKEN"],
}

def run(cmd, timeout=5):
    try:
        r=subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return (r.stdout or "") + (r.stderr or "")
    except Exception:
        return ""

def load_env_names():
    names=set()
    env_path = HERMES / ".env"
    if env_path.exists():
        for line in env_path.read_text(errors="ignore").splitlines():
            line=line.strip()
            if not line or line.startswith("#"): continue
            if "=" in line:
                k=line.split("=",1)[0].strip()
                v=line.split("=",1)[1].strip().strip('"').strip("'")
                if k and v and not v.startswith("your_") and v not in ("", "***", "changeme"):
                    names.add(k)
    # also check process env for runtime-injected tokens
    for k,v in os.environ.items():
        if v and k.isupper() and len(k)>3 and "_" in k and not k.startswith("HERMES_"):
            # avoid huge noise: only keep plausible credential-ish keys
            if any(x in k for x in ("TOKEN","API_KEY","SECRET","PASSWORD","CRED","AUTH","BEARER","CLIENT")):
                names.add(k)
    # auth.json providers -> credential names
    auth = HERMES / "auth.json"
    if auth.exists():
        try:
            j=json.loads(auth.read_text())
            for prov in list(j.get("providers",{}).keys()):
                names.add(f"AUTH_PROVIDER:{prov}")
            for prov in list(j.get("credential_pool",{}).keys()):
                names.add(f"CREDENTIAL_POOL:{prov}")
        except: pass
    return names

def load_config():
    cfg_path = HERMES / "config.yaml"
    txt=cfg_path.read_text(errors="ignore") if cfg_path.exists() else ""
    enabled_plugins=[]
    m=re.search(r"plugins:\s*\n\s*enabled:\s*\n((?:\s*- [^\n]+\n)+)", txt)
    if m:
        for line in m.group(1).splitlines():
            mm=re.search(r"-\s*(\S+)", line)
            if mm: enabled_plugins.append(mm.group(1).strip())
    # gateway platforms enabled? look for gateway_state platforms
    gw_state_path = HERMES / "gateway_state.json"
    gw_platforms={}
    gw_updated=None
    if gw_state_path.exists():
        try:
            j=json.loads(gw_state_path.read_text())
            gw_platforms=j.get("platforms",{}) or {}
            gw_updated=j.get("updated_at")
        except: pass
    return txt, enabled_plugins, gw_platforms, gw_updated

def is_gh_authed():
    out=run("gh auth status 2>&1", timeout=5)
    return "Logged in" in out and "SouthpawIN" in out

def is_xurl_authed():
    if not any(Path(p).exists() for p in [Path("/opt/homebrew/bin/xurl"), Path("/usr/local/bin/xurl"), Path.home()/".local/bin/xurl"]):
        # also check via which
        if "xurl" not in run("which xurl 2>&1"):
            return False
    out=run("xurl auth status 2>&1", timeout=4)
    # xurl prints apps/tokens when authed; when not, says no apps or not logged in
    if "No apps" in out or "not logged" in out.lower() or not out.strip():
        return False
    return "app" in out.lower() or "token" in out.lower()

def is_blogwatcher_configured():
    out=run("blogwatcher-cli blogs 2>&1", timeout=4)
    if "command not found" in out or "not found" in out.lower() and "blogwatcher" in out.lower():
        return False
    if "Tracked blogs" in out:
        return True
    return False

def iso_from_mtime(p: Path):
    try:
        if p.exists():
            ts=p.stat().st_mtime
            return datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc).isoformat().replace("+00:00","Z")
    except: pass
    return None

def scan():
    env_names=load_env_names()
    cfg_txt, enabled_plugins, gw_platforms, gw_updated = load_config()
    gh_authed=is_gh_authed()
    xurl_authed=is_xurl_authed()
    bw_configured=is_blogwatcher_configured()

    integrations=[]

    # --- discover filesystem platforms (union, filtered) ---
    EXCLUDE_PLATFORMS={"_http_client_limits","helpers","media_cache","signal_format","signal_rate_limit","msgraph_webhook","whatsapp_common","yuanbao_media","yuanbao_proto","yuanbao_sticker","webhook_filters","base","api_server"}
    # Note: api_server is real (inventory uses api_server) but gateway file is api_server.py - keep it via inventory, exclude helper-named duplicates filtered by set
    # We'll allow inventory to re-add it; filter only helpers
    HELPER_FILTER={"_http_client_limits","helpers","media_cache","signal_format","signal_rate_limit","msgraph_webhook","whatsapp_common","yuanbao_media","yuanbao_proto","yuanbao_sticker","webhook_filters","base"}
    fs_platforms=set()
    for d in (HERMES_AGENT / "plugins/platforms").iterdir() if (HERMES_AGENT/"plugins/platforms").exists() else []:
        if d.is_dir(): 
            if d.name not in HELPER_FILTER:
                fs_platforms.add(d.name)
        elif d.is_file() and d.suffix==".py" and not d.name.startswith("_") and d.name!="__init__.py":
            if d.stem not in HELPER_FILTER:
                fs_platforms.add(d.stem)
    for p in (HERMES_AGENT / "gateway/platforms").glob("*.py"):
        if p.name in ("__init__.py",): continue
        if p.stem in HELPER_FILTER: continue
        fs_platforms.add(p.stem)
    # add inventory platforms to ensure coverage even if file naming differs (e.g. wecom vs weixin)
    all_platform_names=sorted(set(INV_PLATFORMS) | fs_platforms)

    # helper to find credential names present for a platform
    def creds_for_platform(name):
        hints=PLATFORM_CRED_HINT.get(name, [name.upper()])
        present=[]
        for h in hints:
            # prefix match: any env name contains hint substring before '_' or full
            for en in env_names:
                if ":" in en: continue
                if h.rstrip("_").upper() in en.upper():
                    present.append(en)
        # gh/xurl etc not relevant for gateway platforms; auth provider check
        # also check config contains gateway.<name>
        if re.search(rf"\b{name}\b", cfg_txt, re.I):
            # if config mentions the platform, treat as credential-adjacent only if token env present; don't add pseudo
            pass
        return sorted(set(present))

    # platforms -> integrations
    for name in all_platform_names:
        kind="platform"
        creds=creds_for_platform(name)
        # for platforms, connected = credential present AND enabled in gateway/platforms (gw_platforms or enabled_plugins check)
        # plugin-provided platforms (a2a, homeassistant) are enabled via plugins.enabled? but gateway_state platforms is canonical for gateway-run platforms
        enabled_in_gw = name in gw_platforms
        # also check config gateway.* enabled via plugin list? a2a/homeassistant appear in hermes status as plugin platforms; treat plugins.enabled as enabled for those
        if name in ("a2a","homeassistant","buzz") and name in enabled_plugins:
            enabled_in_gw=True
        # treat gh? no
        has_cred = len(creds) > 0
        # special: github etc not platform; for gateway platforms, no cred means needs_login
        if has_cred and enabled_in_gw:
            state="connected"
        elif has_cred and not enabled_in_gw:
            # credential present but gateway not running/enabled -> still available (could connect)
            state="available"
        elif not has_cred and enabled_in_gw:
            state="needs_login"
        else:
            # no credential and not enabled -> needs_login if platform typically needs credential, else available
            # assume all gateway platforms need credential except maybe api_server/webhook
            if name in ("webhook","api_server"):
                state="available"
            else:
                state="needs_login"
        # last_activity: gateway updated_at if enabled, else file mtime of platform file
        last=None
        if enabled_in_gw and gw_updated:
            last=gw_updated
        else:
            # try platform file mtime
            cand = HERMES_AGENT / "gateway/platforms" / f"{name}.py"
            if not cand.exists():
                cand = HERMES_AGENT / "plugins/platforms" / name
            last=iso_from_mtime(cand) if cand.exists() else None
        integrations.append({"name":name, "kind":kind, "state":state, "credential_names_present":creds, "last_activity":last})

    # --- plugins ---
    plugins_dir = HERMES_AGENT / "plugins"
    fs_plugins=[]
    if plugins_dir.exists():
        for d in plugins_dir.iterdir():
            if d.is_dir() and ((d/"plugin.yaml").exists() or (d/"__init__.py").exists()):
                if d.name != "platforms" and not d.name.startswith("__"):
                    fs_plugins.append(d.name)
    all_plugin_names=sorted(set(INV_PLUGINS) | set(fs_plugins))
    for name in all_plugin_names:
        kind="plugin"
        # credential check: does env contain plugin name? (real env vars only, not synthetic AUTH_PROVIDER:CRED_POOL tags)
        creds=[]
        for en in env_names:
            if ":" in en: continue
            if name.upper().replace("-","_") in en.upper().replace("-","_"):
                creds.append(en)
        # also check plugin.yaml for credential hint? skip
        is_enabled = name in enabled_plugins
        # plugins that are local-only (senter-bridge) have no credential needed
        if name in ("senter-bridge","turbofit"):
            state="connected" if is_enabled else "available"
        else:
            if is_enabled:
                state="connected"
            elif creds:
                state="available"
            else:
                state="available"
        # last_activity: plugin dir mtime
        pdir = plugins_dir / name
        last=iso_from_mtime(pdir) if pdir.exists() else None
        integrations.append({"name":name, "kind":kind, "state":state, "credential_names_present":sorted(set(creds)), "last_activity":last})

    # --- API-bearing skills ---
    for skill_name, skill_paths in INV_SKILLS.items():
        kind="skill"
        # credential detection
        hints=SKILL_CRED_MAP.get(skill_name, [skill_name.upper()])
        creds=[]
        for h in hints:
            if not h: continue
            for en in env_names:
                if h.rstrip("_").upper() in en.upper():
                    creds.append(en)
                elif h.upper() == en.upper():
                    creds.append(en)
        creds=sorted(set(creds))
        # special cases: github via gh auth
        if skill_name=="github" and gh_authed:
            if "GITHUB_TOKEN" not in creds and "GH_TOKEN" not in creds:
                creds.append("GITHUB_TOKEN (gh:keyring)")
            state="connected"
        elif skill_name=="xurl" and xurl_authed:
            state="connected"
        elif skill_name=="xurl" and not xurl_authed:
            state="needs_login"
        elif skill_name=="blogwatcher" and bw_configured:
            state="connected"
        elif skill_name=="blogwatcher" and not bw_configured:
            # blogwatcher without feeds is still available (no login required)
            state="available"
        elif skill_name in ("arxiv","apple","maps"):
            # no credential required; mark available always
            state="available"
        else:
            if creds:
                state="connected"
            elif hints and any(h for h in hints):
                # requires credential but none present
                state="needs_login"
            else:
                state="available"
        # last_activity: newest skill dir mtime among paths
        last=None
        newest=0
        for sp in skill_paths:
            sd = HERMES_AGENT / "skills" / sp
            if sd.exists():
                try:
                    ts=sd.stat().st_mtime
                    if ts>newest: newest=ts
                except: pass
        if newest:
            last=datetime.datetime.fromtimestamp(newest, tz=datetime.timezone.utc).isoformat().replace("+00:00","Z")
        else:
            # fallback to gh repo activity for github
            if skill_name=="github" and gh_authed:
                # use latest repo updated_at as activity
                out=run("gh api users/SouthpawIN/repos?sort=updated&per_page=1 2>&1", timeout=6)
                try:
                    j=json.loads(out)
                    if isinstance(j, list) and j:
                        last=j[0].get("updated_at")
                except: pass
        integrations.append({"name":skill_name, "kind":kind, "state":state, "credential_names_present":creds, "last_activity":last})

    # --- MCP ---
    mcp_out=run("hermes mcp list 2>&1", timeout=5)
    if "No MCP servers" in mcp_out:
        integrations.append({"name":"mcp", "kind":"mcp", "state":"available", "credential_names_present":[], "last_activity":None})
    else:
        # parse configured servers? crude: count lines with url
        creds=[]
        for en in env_names:
            if "MCP" in en.upper():
                creds.append(en)
        integrations.append({"name":"mcp", "kind":"mcp", "state":"connected", "credential_names_present":sorted(set(creds)), "last_activity":iso_from_mtime(HERMES / "mcp.json")})

    # sort: connected first, then available, then needs_login, then alphabetical
    order={"connected":0,"available":1,"needs_login":2}
    integrations.sort(key=lambda x: (order.get(x["state"],9), x["kind"], x["name"]))

    # --- legacy rows for vault-live.html (keep for backward compat) ---
    rows=[]
    # keep 6 legacy summary rows as before for vault-live.html INTEGRATIONS tab
    # MCP
    rows.append(["MCP SERVERS","mcp","No MCP servers configured · add with hermes mcp add <name> --url <endpoint>","—","Plugins provide tools; MCP provides external tool bridges"])
    # plugins enabled count
    enabled_cnt=len([i for i in integrations if i["kind"]=="plugin" and i["state"]=="connected"])
    rows.append(["ENABLED PLUGINS","plugins",f"{enabled_cnt} enabled · {len(all_plugin_names)} available (browser-use, browserbase, firecrawl, chronos, basic)","enabled" if enabled_cnt else "not enabled","hermes plugins list"])
    # messaging platforms
    connected_plats=[i["name"] for i in integrations if i["kind"]=="platform" and i["state"]=="connected"]
    if connected_plats:
        rows.append(["MESSAGING PLATFORMS","gateway",", ".join(connected_plats),"connected","hermes gateway run"])
    else:
        rows.append(["MESSAGING PLATFORMS","gateway","Gateway not running · no platforms configured","offline","hermes gateway run"])
    # credentials summary
    auth = HERMES / "auth.json"
    provs=[]
    if auth.exists():
        try:
            j=json.loads(auth.read_text())
            provs=list(j.get("providers",{}).keys()) or list(j.get("credential_pool",{}).keys())
        except: pass
    if provs:
        rows.append(["CREDENTIALS","credentials",", ".join(provs)+": OAuth present · names only, never values",f"{len(provs)} provider(s)","auth.json"])
    else:
        rows.append(["CREDENTIALS","credentials","No credentials","none","auth.json"])
    # turbofit
    cfg = HERMES / "config.yaml"
    if cfg.exists():
        txt2=cfg.read_text(errors="ignore")
        mm=re.search(r"providers:\s*\n\s*turbofit:.*?default_model:\s*([^\n]+)",txt2,re.S)
        lane=mm.group(1).strip().strip('"').strip("'") if mm else "turbofit"
        rows.append(["TURBOFIT LANE","turbofit",f"TurboFit active · {lane} · providers turbofit + fallback nous",lane[:24],"config.yaml"])
    else:
        rows.append(["TURBOFIT LANE","turbofit","TurboFit not configured","—","config.yaml"])
    # bridge
    health=run("curl -s http://127.0.0.1:8643/health 2>&1", timeout=3)
    try:
        j=json.loads(health)
        if j.get("ok"):
            rows.append(["SENTER-BRIDGE","bridge",f"senter-bridge live on 127.0.0.1:8643 · {j.get('pending',0)} pending","live","server.py"])
        else:
            rows.append(["SENTER-BRIDGE","bridge","senter-bridge unreachable","offline","server.py"])
    except:
        rows.append(["SENTER-BRIDGE","bridge","senter-bridge health unknown","unknown","server.py"])

    return integrations, rows

if __name__=="__main__":
    integrations, rows = scan()
    # summary
    from collections import Counter
    c=Counter(i["state"] for i in integrations)
    print(f"integrations={len(integrations)} connected={c['connected']} available={c['available']} needs_login={c['needs_login']}")
    for i in integrations:
        creds=",".join(i["credential_names_present"]) if i["credential_names_present"] else "—"
        print(f"  {i['name']:<20} {i['kind']:<10} {i['state']:<12} {creds[:60]}")
    if "--dry" in sys.argv:
        print(f"dry run; integrations json {len(json.dumps(integrations))} bytes")
    else:
        # update .system-live.json (preserve skills/bots, add integrations)
        OUT_LIVE.parent.mkdir(parents=True, exist_ok=True)
        live={}
        if OUT_LIVE.exists():
            try: live=json.loads(OUT_LIVE.read_text())
            except: live={}
        live["integrations"]=integrations
        # keep skills/bots if missing generate? preserve
        OUT_LIVE.write_text(json.dumps(live, ensure_ascii=False, indent=2))
        print(f"wrote {OUT_LIVE} ({len(json.dumps(live))} bytes)")

        # legacy + new for vault-live.html: write object with both
        OUT_LEGACY.parent.mkdir(parents=True, exist_ok=True)
        # also write legacy rows as top-level array for old viewer, and object with integrations for new code
        # we write legacy array to live-integrations.json (old path) and also write .system-live shape if needed
        # For new weaver code that checks .system-live.json integrations, that's primary; for old vault-live that fetches live-integrations.json, keep array fallback but also embed integrations
        # Write legacy rows as JSON array (backward compat)
        OUT_LEGACY.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
        # also write integrations mirror next to it for new code that fetches that url and handles object
        alt = OUT_LEGACY.with_name("live-integrations-v2.json")
        alt.write_text(json.dumps({"integrations": integrations, "rows": rows}, ensure_ascii=False, indent=2))
        print(f"wrote {OUT_LEGACY} ({len(json.dumps(rows))} bytes) + {alt}")
