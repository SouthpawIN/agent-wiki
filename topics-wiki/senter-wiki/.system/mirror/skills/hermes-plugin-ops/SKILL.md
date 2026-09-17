---
name: hermes-plugin-ops
description: "Use when building Hermes plugins or fixing defaults."
version: 0.1.0
author: Teknium (teknium), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, plugins, bridge, approvals, image-gen, openrouter]
    related_skills: [hermes-agent]
---

# Hermes Plugin Ops

Standalone Hermes plugins (no core edits) for live bridges and provider-default maintenance. Covers loopback SSE + approval relay and stale image-model defaults that 404 before falling back.

## When to Use

- Building a standalone plugin under `~/.hermes/plugins/<name>/` that hooks lifecycle for every profile and serves a local HTTP endpoint
- Bridging bot-mode `approvals.single_query_mode=deny` ("Silence is not consent") to an external UI via `register_gateway_notify` / `resolve_gateway_approval`
- Fixing a stale `DEFAULT_MODEL` in `plugins/image_gen/*` (e.g. `openai/gpt-5.4-image-2` → current catalog) while keeping fallback chain
- Verifying `openai/gpt-image` / `google/gemini-3-pro-image` routing or `agent/pet/generate/imagegen.py` hatch pipeline
- Don't use for: core edits to `hermes_cli/*` or `tools/approval.py` — keep bridge as plugin

## Prerequisites

- `HERMES_HOME` resolves via `get_hermes_home()`; plugin dir is `$HERMES_HOME/plugins/<name>/` + `plugin.yaml` (`name`, `version`, `kind: standalone|bridge`)
- Hooks available in `hermes_cli.plugins.VALID_HOOKS`: `pre_tool_call`, `post_tool_call`, `on_session_start`, `on_session_end`, `on_skill_lifecycle`, `pre_approval_request`, `post_approval_response`
- Approval internals: `tools/approval.py` — `_fire_approval_hook` (~L108), `register_gateway_notify` (~L2801), `resolve_gateway_approval` (~L2833), `submit_pending`, `list_gateway_approvals`
- Loopback server: `127.0.0.1:8643`, per-boot token at `~/.hermes/senter-bridge/token` (600), CORS allow `null`/`file://` only with token

## Quick Reference

- Plugin discovery: `PluginManager(get_hermes_home())._collect_directory_manifests()`; enable via `hermes config set plugins.enabled` or `~/.hermes/config.yaml` `plugins.enabled: [turbofit, senter-bridge]`
- Debug: `HERMES_PLUGINS_DEBUG=1 hermes plugins list`
- Catalog check: `curl -s https://openrouter.ai/api/v1/models -o /tmp/or_models.json` then grep `output_modalities` containing `"image"`
- Health: `GET /health` (token via `?token=` or `X-Senter-Token`), `GET /events?token=` (SSE replay + `approval/snapshot` + tail), `GET /pending?token=`, `POST /approve/<id>?token=`, `POST /deny/<id>?token=`, `POST /post` (`status` field), `GET /file?path=` (allowlisted vault files for file:// pages), `POST /ask`, `/stt`, `/tts`, `/wake/*`, `GET /feed/status`, `POST /feed/poll` — full contract in `references/bridge-approval-relay.md`
- Canonical restart: `launchctl bootout gui/$(id -u)/com.senter.bridge; launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.senter.bridge.plist` then `curl /health` and confirm the pid changed (`pkill -f server.py` races and leaves the old pid)
- Wiki-side behaviour proof: `PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-approval.js` (vault) — real click, 5-frame capture, replay check, console-error count; static ledger `node assets/verify-wiki.js`

## Procedure

### A) Live bridge plugin (senter-bridge pattern)

1. Scaffold `~/.hermes/plugins/senter-bridge/plugin.yaml` (6 lines) + `__init__.py` + `server.py`. Completion: `hermes plugins list` shows enabled.
2. In `register(ctx)`: `ctx.register_hook` for `pre_tool_call`, `post_tool_call`, `on_session_start`, `on_session_end`, `on_skill_lifecycle`, `pre_approval_request`, `post_approval_response`. Emit every hook via `emit(kind="tool"|"turn"|"skill"|"approval", ts, bot=_profile(), topic=_topic_from(...), summary)` to `~/.hermes/senter-bridge/events.jsonl` + in-memory SSE fanout. Completion: `events.jsonl` appends under lock.
3. Topic inference: scan texts for `topics-wiki/<name>/`, verify `(VAULT / "topics" / rest).exists()` where `VAULT=~/Documents/Projects/Projects`. Completion: `topic` field present only when path under vault.
4. Approval notify surface: register LAZILY from `pre_tool_call` (cli.py binds the session key per turn AFTER plugins load — import-time registration binds "default" and misses). In that hook set `HERMES_GATEWAY_SESSION=1`, pop `HERMES_SINGLE_QUERY_SESSION`, call `register_gateway_notify(session_key, notify_cb)` once per key (`_seen` set). `notify_cb` writes `pending/<request_id>.json`, emits `approval phase=pending`, spawns a waiter polling `pending/<id>.decision` every 0.4s for `_get_approval_timeout()+5` (NOT 3600 — a late click after the agent gave up must emit `resolved=0`), emits `approval phase=expiring {remaining}` at 80% of the wait, and on expiry unlinks the pending record + emits `approval phase=timeout` and a `message {status:"blocked"}`. Completion: `POST /approve/<id>` writes `.decision` and resolves without "Silence is not consent" timeout.
4b. Server-side orphan sweep (`_sweep_pending()` on `/health`, `/pending`, replay): the waiter lives in the BOT process, so if that process dies the `pending/*.json` stays forever and the UI shows a gold card for hours. Retire records older than `approvals.timeout+60s` (emit `timeout`, `swept:true`) and records whose `.decision` sat uncollected >30s. "Pending" = `<id>.json` exists AND no `<id>.decision`.
5. Server: `ThreadingHTTPServer(("127.0.0.1", PORT), Handler)` — token generated via `secrets.token_urlsafe(24)` if missing, `PORT=SENTER_BRIDGE_PORT|8643`, `_ok_origin` allows `None/""/"null"` or `127.0.0.1/localhost/file://` only with valid token. Completion: `curl -s http://127.0.0.1:8643/health` returns `{"ok": true}`.
5b. SSE replay must be STATE-AWARE, not a raw tail: (a) drop `approval/pending` lines whose id is no longer pending — a raw replay after `decided` recreates the card in every reconnecting client; (b) after replay send one `{kind:"approval", phase:"snapshot", pending:[...]}` so the client derives its pending map from a single authoritative event and never needs a second `/pending` fetch; (c) keep TWO windows — last 60 events of any kind PLUS the last 40 `message`/`approval` records — because one agent turn emits dozens of `tool start/end` lines that otherwise push every feed post and approval out of the reload window.
5c. Serving files to a `file://` page: Chromium refuses `fetch(file://…)` from file pages, so ship `GET /file?path=` — `Path(...).resolve()` then `relative_to()` against an allowlist of roots (vault dir + bridge data dir), refuse the token file / `.env` / `auth.json` by name, 2 MB cap, mime via `mimetypes`. Test traversal (`../../.hermes/config.yaml` → 403), token path → 403, missing → 404, no token → 401.
5d. Daemon threads inside the bridge (feed pollers etc.) run under launchd's MINIMAL PATH — `shutil.which("gh")` returns None even though `gh` works in your shell. Resolve binaries through a fallback list (`/opt/homebrew/bin`, `/usr/local/bin`, `~/.local/bin`, `~/go/bin`, `~/.cargo/bin`) before declaring a source uncredentialed; "connected" must come from a real auth probe (`gh api user`), never from the binary merely existing.
6. No core edits — bridge lives entirely in user plugins. Completion: `git -C ~/.hermes/hermes-agent diff --stat` shows only intended provider default change.

### B) Stale image default fix

1. Locate default: `search_files(pattern="gpt-5.*image", path="plugins/image_gen")` → `plugins/image_gen/openrouter/__init__.py` `DEFAULT_MODEL`. Completion: exact line identified.
2. Verify live catalog: `curl https://openrouter.ai/api/v1/models` → count `"output_modalities":["image"` variants (9+2). Confirm intended replacement exists (e.g. `openai/gpt-5-image`). Completion: grep confirms id present.
3. Swap `DEFAULT_MODEL = "openai/gpt-5-image"`, keep `_FALLBACK_MODEL = "google/gemini-3-pro-image"`, `_DEFAULT_MODEL_CHAIN = (DEFAULT_MODEL, _FALLBACK_MODEL)`, update `_KNOWN_MODEL_META[DEFAULT_MODEL]["display"]` and docstring overlap note (~L33). Completion: `grep -n DEFAULT_MODEL` shows new value, `grep -n gpt-5.4-image` returns 0 for default.
4. Log fix in `topics-wiki/hermes-agent/.system/queue.md` and contract (if bridge) in `topics-wiki/senter-wiki/.system/queue.md`. Completion: queue diff shows DONE entry.

## Pitfalls

- `~/.hermes/senter-bridge/` (data) ≠ `~/.hermes/plugins/senter-bridge/` (code) — `ls` the wrong one gives "No such file".
- `TypeError: unsupported operand type(s) for |: 'type' and 'type'` under Python 3.9 when importing `hermes_constants.py` with `X | Y` syntax — `sys.path.insert(0, repo)` reproduces, not a plugin bug.
- Security scan blocks `cat | python3` pipes — use `write_file` + `read_file` instead of piping to interpreter.
- `single_query_mode=deny` + no gateway surface = every dangerous command times out; bridge must set `HERMES_GATEWAY_SESSION=1` before registering notify.
- Moving chat defaults to Image API (`/images/generations`) changes reference-image handling (3 vs 16) — keep `_CHAT_ONLY_MODELS` pinned to chat unless explicitly migrating.
- Docstring at ~L33 mentions overlap models — update it when swapping DEFAULT_MODEL or review flags stale comment.
- Cross-checking `.system-live.json` sources: synthetic credential tags like `AUTH_PROVIDER:x` / `CREDENTIAL_POOL:custom:y` contain `:` — skip them when substring-matching env names to integrations or every plugin looks credentialed.
- `received_events` PR payloads from the GitHub Events API are slim (`title`/`html_url` null) — build `https://github.com/<repo>/pull/<n>` yourself and fetch the title with one cached `gh api repos/<repo>/pulls/<n> -q .title`.
- Every avatar `<img>` that misses its `.png` logs a console `ERR_FILE_NOT_FOUND` even when the `onerror` svg swap works — when a "zero console errors" contract is in force, ship the png (Playwright `page.setContent(svg)` + `screenshot` converts svg→png with no extra tooling).
- Chris's status vocabulary: `done|blocked|needs_chris|working`; derive it from a leading `DONE —`/`BLOCKED —`/`NEEDS-CHRIS —` line when the poster omits `status` so the fleet-standard done line lights the right UI state without changing the bots.

## Verification

- `grep -rn DEFAULT_MODEL plugins/image_gen/openrouter/__init__.py` shows new model; fallback chain intact
- `HERMES_PLUGINS_DEBUG=1 hermes plugins list | grep senter-bridge` present
- `curl -s http://127.0.0.1:8643/health -H "X-Senter-Token: $(cat ~/.hermes/senter-bridge/token)"` → `ok:true`, `pending: N`
- E2E: temp `HERMES_HOME=/tmp/test_bridge_home` → start bridge → `hermes -p klerik chat -q` hitting protected write → `GET /events?token=` shows `kind=approval phase=pending` → `POST /approve/<id>` → write lands, `events.jsonl` logs `decided`
- Queue files contain contract + DONE entries; `git diff` shows only provider + queue changes

## References

- `references/bridge-approval-relay.md` — SSE/pending file contract, token/CORS, gateway queue wiring
- `references/image-provider-catalog.md` — catalog verification + fallback-chain preservation recipe
- `references/wiki-client-patterns.md` — the client side of the bridge contract (decided Set + snapshot, `vaultFetch`, approval-card animation on real animatable props, feed-post rendering) and the Playwright proof recipe
