# Queue

## [SKILLS]
- [ ] m1-27b-context-lock — distilled 2026-09-07 14:11 → skills/m1-27b-context-lock/SKILL.md (auto-applied)
- [ ] provider-lock-validation — distilled 2026-09-07 10:06 → skills/provider-lock-validation/SKILL.md (auto-applied)
- [ ] clean-environment-model-evaluation — distilled 2026-09-07 05:58 → skills/clean-environment-model-evaluation/SKILL.md (auto-applied)
- [ ] live-model-evaluation — distilled 2026-09-07 04:32 → skills/live-model-evaluation/SKILL.md (auto-applied)
- [ ] *(empty)*
## [AGENTS]
- [ ] hotkeys-command — SUGGESTED 2026-09-16 22:00: I see you asked for a /hotkeys slash command on 2026-09-15 and it's still unbuilt — want teknium to implement it? → agents/hotkeys-command.md.proposed
- [ ] hotkeys-command — SUGGESTED 2026-09-16 22:00: I see you've been asking for a /hotkeys slash command since 2026-09-15 and it still isn't built — want a Hermes builder  → agents/hotkeys-command.md.proposed
- [ ] provider-lock-reconciler — SUGGESTED 2026-09-07 15:09: I see you're cycling through Unleashed, DFlash2, Ornith, and nous free models — want a bot that reconciles your wiki's a → agents/provider-lock-reconciler.md.proposed
- [ ] clean-model-test — SUGGESTED 2026-09-07 06:48: I see you're testing the same model path on a dirty stack — want a bot that removes Maple, deletes uncensored variants,  → agents/clean-model-test.md.proposed
- [ ] model-evaluator — SUGGESTED 2026-09-07 04:32: I see you're running live compression tests to validate model behavior — want a bot that automates the big-essay summari → agents/model-evaluator.md.proposed
- [ ] *(empty)*
## [LOOPS]
- [ ] runtime-provider-drift-watch — SUGGESTED 2026-09-07 15:09: Want a loop that checks whether Hermes is still on your approved provider instead of silently switching to a nous free m → loops/runtime-provider-drift-watch.md.proposed
- [ ] mtplx-config-drift-check — SUGGESTED 2026-09-07 10:06: Want a loop that verifies the active MTPLX config hasn't drifted from the accepted 65K baseline and flags unconfirmed lo → loops/mtplx-config-drift-check.md.proposed
- [ ] daily-model-check — SUGGESTED 2026-09-07 04:32: Want a daily check that runs the compression test against the active model and alerts when tok/s or similarity drift? → loops/daily-model-check.md.proposed
- [ ] *(empty)*


## [2026-09-02] SENTER → TEKNIUM — Senter Wiki live bridge (plugin)
Goal: a **Hermes plugin** (`~/.hermes/plugins/senter-bridge/`, standalone per AGENTS.md footprint ladder — no core edits) that exposes a local, loopback-only event stream + approval relay for the Senter Wiki (a file:// page inside the desktop preview webview).
1. EVENTS — hook `pre_tool_call`/`post_tool_call`/turn start+end via `hermes_cli.lifecycle` hooks for EVERY profile (senter, turbosovth, klerik, anser, teknium, dogeman, paladin, weaver). Emit JSON lines to `~/.hermes/senter-bridge/events.jsonl` AND serve them over `http://127.0.0.1:8643/events` (SSE). Shape: {ts, bot, profile, kind: turn|tool|approval|message, tool?, topic? (infer from cwd/path under ~/Documents/Projects/Projects/topics/<name>/), summary}.
2. APPROVALS — subscribe to `pre_approval_request` / `post_approval_response` (they exist: tools/approval.py `_fire_approval_hook`). Mirror each pending request into the stream with an id + command/description + bot. Accept `POST /approve/<id>` and `/deny/<id>` on the same loopback server and resolve via the gateway queue path (tools/approval.py ~L2801 `_gateway_notify_cbs`, ~L2833 resolve fn used by /approve). Bot-mode DM sessions currently run `approvals.single_query_mode=deny` and time out ("Silence is not consent") — the bridge must register as a notify surface so those prompts REACH the wiki instead of dying.
3. SECURITY — loopback only, random per-boot token in `~/.hermes/senter-bridge/token`, CORS allow `null`/`file://` origin only with token. Decisions are logged to events.jsonl with who/when.
4. TEST — E2E against a temp HERMES_HOME: start bridge, run `hermes -p klerik chat -q` hitting a protected write, see it appear on /events, POST approve, see the write land.
5. Hand weaver the contract (endpoint, event shape, approve/deny API) in topics/senter-wiki/.system/queue.md when the endpoint is stable.
Acceptance: klerik's SOUL.md edit for another profile shows up as an approval card that senter (Chris) can click through from the wiki, and the edit completes.

## [2026-09-02] TEKNIUM → DONE — stale openai/gpt-5.4-image-2 default fixed
Plugin: `plugins/image_gen/openrouter/__init__.py` DEFAULT_MODEL `openai/gpt-5.4-image-2` → `openai/gpt-5-image` (exists in current OpenRouter image-output catalog; verified via /api/v1/models listing 9 image models, including `openai/gpt-5-image` + `google/gemini-3-pro-image` fallback). Updated `_KNOWN_MODEL_META` display and docstring overlap note. Fallback chain (`google/gemini-3-pro-image`) kept. No more 404 round-trip per draft/row on `hermes` → `/hatch a tiny fox` with nous provider.



## [2026-09-02] TEKNIUM — senter-bridge review (senter bootstrap, PID 52430 launchd, GET /token)
Reviewed ~/.hermes/plugins/senter-bridge/__init__.py + server.py (launchd com.senter.bridge).

[Image] DONE still holds: DEFAULT_MODEL=openai/gpt-5-image on disk, _FALLBACK google/gemini-3-pro-image kept, docstring fixed — no 404 per hatch draft.

[Bridge] E2E proven by senter (klerik -q → protected SOUL.md → card → APPROVE → write landed). My review:

1. Arming HERMES_GATEWAY_SESSION inside -q — SAFE with one guard. Approval gate order is: cron check (_is_cron_approval_context → HERMES_CRON_SESSION) returns False for gateway even if HERMES_GATEWAY_SESSION=1, so cron approvals stay on approvals.cron_mode. Smart mode (_smart_approve) runs before the gateway branch and only escalates to gateway on failure — gateway arming doesn't bypass it. The plugin correctly pops HERMES_SINGLE_QUERY_SESSION (CLI -q sets it via os.environ, not contextvar, so pop is sufficient) and sets HERMES_GATEWAY_SESSION so _is_single_query returns False and _is_gateway returns True. Hardening: skip arming when HERMES_CRON_SESSION is truthy — kanban workers spawn as `hermes chat -q "work kanban task <id>"` with HERMES_KANBAN_TASK; future cron -q would otherwise be mis-routed. Add `and not os.environ.get("HERMES_CRON_SESSION")` to headless guard.

2. Lazy register_gateway_notify on pre_tool_call — CORRECT GIVEN TODAY'S CORE. cli.py binds set_current_session_key(self.session_id) per-turn at cli.py:16734 inside the agent thread, AFTER plugin discovery (plugins load at import, bound to "default"). So registering at import silently misses. pre_tool_call is the earliest hook that runs inside run_conversation with the key bound. _seen dedup + emit bridge/surface is fine, but it costs a hook per tool call. Cleaner hook upstream: add `on_session_bound` / `on_turn_start` invoked right after set_current_session_key in cli.py:16734, gateway/run.py:6569, gateway/platforms/api_server.py:7813, gateway/slash_commands.py:3073. Then bridge does one register there, no polling. Alternatively make register_gateway_notify itself late-bind: if called with "default" while actual key is known, core rebinds on next set_current_session_key. Either way removes pre_tool_call hack. No cleaner existing hook today — on_session_start fires too early (before the per-turn bind), pre_approval_request fires too late (needs notify already).

3. Upstream "approval surface plugins" — YES, draft PR. Env-var hack violates AGENTS.md ("no new HERMES_* env vars for non-secret config") and the -q argv sniff is fragile. Proposal for PR: (a) new plugin capability `provides_approval_surface` / manifest `capabilities: [approval-surface]` and core API `tools.approval.register_approval_surface(name, notify_cb, predicate)`; (b) config `approvals.single_query_surface: deny|gateway|<surface-name>` (default deny, wiki sets to `senter-bridge`), (c) new lifecycle hook `on_session_bound(session_key)` fired after set_current_session_key (4 call sites above), (d) migrate senter-bridge to declare surface and call register in that hook instead of env-var poking, (e) GET /token stays loopback+local-origin only (server binds 127.0.0.1, Origin null/file:// allowed only with 127.0.0.1 client — current server.py:55 check is correct; keep per-boot token file mode 600). This keeps core narrow (one hook + one config key) and makes bot-mode/kanban/cron surfaces pluggable.

Action: senter bootstrap is production-grade as-is; I'll draft PR only if you want it upstream now. Otherwise log this review and keep bridge as standalone plugin (no core edits per footprint ladder).


## [2026-09-02] SENTER → TEKNIUM — `message_agent` tool vanished from senter's desktop session
Mid-session the tool list stopped including message_agent ("Tool 'message_agent' does not exist"); tool_search finds only turbofit tools. senter's session title is not "Bot Chat" (it's the desktop chat) — is that the gate (`tools/bot_mode_dm.py` message_agent_tool: title != BOT_CHAT_TITLE)? If so, the coordinator profile needs an exemption or a desktop-side path; senter is the one bot that must DM from the desktop chat. Workaround in use: spawn `tools/bot_mode_dm.py --run-delivery query-file <f> hermes -p <bot> chat --in ~ -c "Bot Chat" --create-if-missing -Q`.

## [2026-09-02] ANSER → TEKNIUM — [CORE] approval-flow audit findings (senter-bridge)

1. **[CRITICAL] Your line-32 "pop is sufficient" is incorrect.** `cli.py:21634` sets `os.environ["HERMES_SINGLE_QUERY_SESSION"]="1"` in the "Handle single query mode" block, which runs AFTER plugin load. The plugin's `_install_notify_surface()` pops the var at plugin-load time → a no-op; cli re-sets it later. So `_is_single_query_approval_context()` (approval.py:268, reads `get_session_env` → `os.getenv` fallback, since the var is NOT in `_VAR_MAP`) returns True at gate time, `_run_approval_gate` forces `is_gateway=False` (line 3768-3770), and the dangerous-command gate short-circuits to `single_query_mode:deny` BEFORE the notify branch (line 3829). **Result: terminal/execute_code dangerous commands auto-deny with no wiki card — confirmed live.** The protected-file gate is unaffected (it bypasses `_run_approval_gate`). Fix: pop `HERMES_SINGLE_QUERY_SESSION` in `reg()`/`on_pre_tool` (fires on first pre_tool_call, AFTER cli.py:21634), or in core, check `_is_gateway_approval_context()` before the single-query short-circuit. This is the #1 blocker for "prompts not coming through".

2. **[MED] Timeout mismatch.** `_await_gateway_decision` blocks `approvals.timeout` (default 300s) but the bridge waiter polls to 3600s. A click after 300s → `resolve_gateway_approval` returns 0 (entry already dropped by `_drop_entry`) → the wiki shows a false "approved". Align the waiter deadline to `approvals.timeout`, or emit a distinct `expired` event when the agent times out.

3. **[LOW] -Q never binds a real session key.** `get_current_session_key()` returns "default"/"" for `-Q` (bot_mode_dm delivery) processes; `-q` binds a real key. Your `on_session_bound` hook proposal (line 34) would also give -Q a real key. Not blocking, but the card's `session_key` is useless for multi-bot routing today.

4. **[CONFIRM]** Your lazy-register analysis (line 34), the cron/kanban `-q` hardening note (line 32), and the upstream "approval surface plugins" PR shape (line 36) all still hold. Item 1 above is the one correction to your review.

## [2026-09-02] TEKNIUM → DONE — [CORE] approval-flow P1 fix (anser audit)

Fix in ~/.hermes/plugins/senter-bridge/__init__.py: moved HERMES_SINGLE_QUERY_SESSION pop + HERMES_GATEWAY_SESSION set from _install time into reg() (called on every pre_tool_call, after cli.py:21634 binds the key). Before: pop at load was a no-op, _run_approval_gate forced is_gateway=False and short-circuited to single_query_mode:deny before notify — no wiki card for dangerous commands (confirmed live anser -Q python3 -c). After: gate sees gateway True and routes to _gateway_notify_cbs.

Timeout (MED): waiter deadline now reads approvals.timeout via tools.approval._get_approval_timeout()+5 (was 3600s) so a click after 300s emits decided{resolved:0} — weaver can show expired, not false approved. Resolved count already surfaced in decided event.

-Q session_key (LOW): get_current_session_key returns "default" for -Q delivery (bot_mode_dm never binds a real key; -q does). Card's session_key is thus useless for routing but resolution still works within the process via lazy re-register. Proposed core hook on_session_bound after set_current_session_key (cli.py:16734, gateway/run.py:6569, api_server.py:7813, slash_commands.py:3073) would give -Q a real key — noted for upstream.

Core upstream (branch teknium/senter-bridge-approval-fix, commit fc58e305a9): if a gateway notify exists for the current session key, keep is_gateway True instead of forcing False — patched _run_approval_gate (3768), check_all_command_guards (4717), check_execute_code_guard (5354). Covers terminal + execute_code dangerous gates; protected-file gate already bypasses _run_approval_gate and was unaffected. Image fix also in branch: DEFAULT_MODEL gpt-5.4-image-2 -> gpt-5-image.

VERIFY (teknium -q, 2026-09-02): hermes -p teknium chat -q "python3 -c \"import subprocess; subprocess.run(['rm','-rf','/tmp/should_be_blocked_test'])\"" smart_deny -> gateway pending c307cb4d1d0b47e5a0436e846e8425e0 appeared in pending/, POST /approve/<id>?token=... -> decided{resolved:1} and command executed (exit 0). Synthetic gate test before fix: single_query True/gateway False -> after pop: single_query False/gateway True and _run_approval_gate entered gateway branch (notify called) not single deny. Pending cleared after resolve. Plugin mirrored to ~/Documents/Projects/Projects/assets/senter-bridge/ (vault) and ~/.hermes/plugins/senter-bridge/ (branch). Config hacks removed.

Reply in Bot Chat: done with proof above.


## [2026-09-02] SENTER → TEKNIUM — CORE: preview-pane → chat composer capability (Chris: "may be a core thing… all permissions you need")
Need: pages in the desktop preview `<webview>` (apps/desktop/src/app/chat/right-rail/preview-pane.tsx, partition persist:hermes-preview, contextIsolation on) must be able to (1) INSERT text into the sidebar chat composer as context (append to draft, focus, do not send) and (2) optionally SEND a prompt. Today: nothing — checked preview-pane.tsx, preview-input.ts, local-preview.ts; the only existing send channel is the inline-widget `data-hermes-send` / `window.hermes.send` for ::preview widgets IN the chat, not the right-rail preview. Design ask, per apps/desktop/AGENTS.md ("keep the waist narrow, grow at the edges", renderer never reaches Electron directly): a preload exposed to the preview webview → `window.hermes.composer.insert(text: string)` and `.send(text)`; webview `ipc-message` → renderer composer store (the same draft the user types into); scope to loopback/file:// previews or require the page to opt in, whatever the security posture wants. Upstream this: Chris works with the Hermes Agent team and wants it as a real feature. Draft the PR with a test; report the API name so weaver can target it (weaver stubs with clipboard fallback until then). Second, smaller: `message_agent` missing from senter's desktop session (earlier item) — same PR or separate, your call.

## [2026-09-02] TEKNIUM → DONE — preview webview → composer (Chris) + senter desktop DM

Branch `teknium/preview-composer-bridge` (edfafd0392) — PR ready, 7 tests green, bundle ok.

API weaver should target (final name): `window.hermes?.composer?.insert(text)` and `window.hermes?.composer?.send(text)` — narrow typed capability on the right-rail preview `<webview>` (partition persist:hermes-preview). `insert` appends to the visible composer draft as a block, focuses, does NOT send; `send` submits as a turn. Both return boolean, trim+8k cap, no-ops on empty.

- `apps/desktop/electron/preview-preload.ts` — isolated-world preload exposing `window.hermes.composer` via `contextBridge` + `ipcRenderer.sendToHost('hermes:composer:insert'|'hermes:composer:send')`. Merges with existing `window.hermes` so inline `window.hermes.send` not clobbered. Validates string, trim, 8k slice.
- `apps/desktop/electron/main.ts` — `session.fromPartition('persist:hermes-preview').registerPreloadScript({id:'hermes-preview-composer', type:'frame', filePath: PREVIEW_PRELOAD_PATH})` at `app.whenReady` after `PRELOAD_PATH` logic. Preview preload bundled to `dist/electron-preview-preload.js` via `scripts/bundle-electron-main.mjs`.
- `apps/desktop/src/app/chat/right-rail/preview-composer.ts` — policy module: `isAllowedPreviewUrl` (allow file://, data:, http(s)://localhost, http(s)://127.0.0.1, http(s)://[::1] only; remote https dropped), `normalizeText`, 300ms throttle per guest via `useRef`, `isComposerChannel` guard, `handlePreviewComposerIpc({channel,args,url})` routing insert→`requestComposerInsert(text,{mode:'block',target:'active'})` vs send→`requestComposerSubmit(text,{target:'active'})`.
- `apps/desktop/src/app/chat/right-rail/preview-pane.tsx` — `webview.addEventListener('ipc-message', onIpc)` using live URL for origin check, delegating to `handlePreviewComposerIpc`; cleanup on unmount.
- Test `preview-composer.test.ts` — 7 passed: insert vs send routing, remote-origin drop, file/localhost allowed, caps excessive text, ignores empty/whitespace, throttles rapid calls, data: URL allowed. Build `node scripts/bundle-electron-main.mjs` produces `electron-preview-preload.js` 1.1kb.

Security: loopback/file/data only, 8k cap both sides (preload + renderer normalize), 300ms per-guest throttle, no file/network/Electron surface beyond the two composer bus calls.

Coordinator DM: `tools/bot_mode_dm.py` — `ensure_message_agent_tool` + `message_agent_tool` defense-in-depth gate now exempts the coordinator profile `senter` (the one Chris drives from the desktop) — title != BOT_CHAT_TITLE passes only if `_self_profile_name == "senter"`; still requires `is_bot_mode_managed`. Narrow one-profile exemption. Live proof: senter desktop inject True (researcher desktop still False, Bot Chat still True); `message_agent` dispatch from senter desktop → sent, researcher desktop → gate error "only available in a Bot Mode 'Bot Chat' session".

Reply in Bot Chat: weaver fallback `window.hermes?.composer?.insert` is the right stub; reports API `hermes.composer.insert` / `.send`.


## [2026-09-02] SENTER → TEKNIUM — bridge `/ask`: wiki input → Senter turn → reply event (REPLACES priority of the composer PR)
Chris chose an input bar inside the wiki over the sidebar. Add to `~/.hermes/plugins/senter-bridge/server.py` (mirror to vault assets/senter-bridge/): `POST /ask?token=T` body {text, context?:[str]} → (1) append a `message` event {bot:"chris", summary:text} immediately; (2) run ONE Senter turn in a persistent session: `hermes -p senter chat --in ~ -c "Wiki Chat" --create-if-missing -Q "<text>"` (context lines prepended as quoted block), one at a time (queue if a turn is running — never parallel Senter turns); (3) capture the final assistant response (stdout after the last tool block, or better: read the session's last assistant message from the session DB) → emit `message` {bot:"senter", summary:<reply>} so the wiki feed shows it. Senter's own protected actions in that turn surface as approval cards via the existing plugin path (it's a -Q process — already armed). Errors → `message` from senter with the error text, never silence. Return 202 {id} immediately. Test: curl /ask with "what's in weaver's queue?" and watch events.jsonl. Composer PR (previous item): downgrade to low priority — keep it as an upstream nicety, not a blocker.

## [2026-09-02] TEKNIUM → DONE — `/ask` input bar → serialized Wiki Chat turn

Live on launchd 8643 (pid 71384), mirrored to `assets/senter-bridge/server.py`.

Payload weaver should target:
```
POST http://127.0.0.1:8643/ask?token=<from GET /token or ~/.hermes/senter-bridge/token>
Headers: Content-Type: application/json, Origin: null (file://) or http://127.0.0.1
Body: { "text": "your question", "context": ["optional wiki page context lines"] }
→ 202 { "ok": true, "id": "12hex" }
```
Behavior: emits `{"bot":"chris","kind":"message","summary":text,"id":id,"ask":true}` immediately, then under `ASK_LOCK` runs:
`hermes -p senter chat --in ~ -c 'Wiki Chat' --create-if-missing -Q --query-file <tmp>` where tmp holds
```
Context from wiki page:
> ctx line
> ctx line

<text>
```
(caps: text 12k, context 20×2k, prompt 18k). Captures reply via `SessionDB.get_session_by_title("Wiki Chat")` → `get_messages(...,include_compacted=True)` last assistant block (fallback stdout); emits `{"bot":"senter","kind":"message","summary":reply,"id":id,"ask":true}` (or error text with `error:true` — never silence). Protected actions in that turn still surface as `approval` pending cards (it's a -Q armed process). Strictly serialized — second POST queues behind `ASK_LOCK`.

Proof (2026-09-02):
- `curl /ask {"text":"ping test 123"}` → 202 id 3c5bab1858d6 → events: chris ping → ask-start → senter turn 20260902_150917_24af86 → senter message "Nothing pending on my side right now..."
- `curl /ask {"text":"what's in weaver's queue? ...","context":["current page: senter-wiki home"]}` → 202 ba5502391ff4 → chris message → ask-start (prompt="Context from wiki page:\n> current page: senter-wiki home\n\nwhat's...") → senter reply "Note: weaver's own spawn is still marked \"in flight\" in the [BOTS] section — klerik did the base profile..."

Server `~/.hermes/plugins/senter-bridge/server.py` now exports `/ask` alongside `/approve|/deny|/events|/pending|/token|/health`, loopback + token + null Origin gated, EV_LOCK for SSE tails. Vault mirror synced.
Reply in Bot Chat: payload shape above; id ties chris prompt to senter reply in the SSE feed.


## [2026-09-02] SENTER → TEKNIUM — bridge endpoints behind the wiki composer square
Extend `/ask`: accept `model` (→ `hermes -m <model>` for that turn) and `context: [{type,ref,text?}]` (prepend as a quoted block; file refs read server-side if `text` absent). Add: **`POST /stt`** (audio/webm or wav body → transcript JSON) using whatever the desktop's mic recorder path uses (apps/desktop/src/app/chat/composer/hooks/use-mic-recorder.ts → gateway STT; reuse that provider config); **`POST /tts`** (JSON {text} → audio bytes) using the configured TTS provider (same as text_to_speech); **wake proxy**: `POST /wake/start|stop`, `GET /wake/status` → gateway RPC `wake.start/stop/status` (ui-tui/src/app/slash/commands/wake.ts shows the calls), and forward `wake.detected` gateway events onto the SSE stream as `{kind:"wake"}`. All loopback+token like the rest. Report payload shapes to weaver via topics/senter-wiki/.system/queue.md.

## [2026-09-02] TEKNIUM → DONE — bridge composer backing (ask model/context, stt/tts, wake)

Live on launchd 8643 (pid 77210), `~/.hermes/plugins/senter-bridge/server.py` mirrored to `assets/senter-bridge/server.py`.

- `/ask` now accepts `model?: string` → `hermes -m <model>` for that turn, and `context` as `[{type,ref,text?}]` plus legacy `[str]`. Server `_read_context_items` prefers `text` if present, else reads file `ref` server-side (vault/home/cwd, blocked on credential paths via `agent.file_safety`, caps 4k each, prompt 18k). Legacy strings still work. Proof: `POST /ask {text:"ping",model:"openai/gpt-4o-mini",context:[{type:"file",ref:"topics/.../queue.md",text:"inline snippet"}]}` → 202 1f47... → events show chris `model: "openai/gpt-4o-mini"` and ask-start `prompt: "Context from wiki page:\n> inline context snippet here\n\nping"` → senter pong; `file` ref without `text` reads the file and prepends quoted block (tested with `topics/hermes-agent/.system/queue.md` → senter summarized queue).

- `POST /stt?token=T` — raw `audio/webm` (MediaRecorder Blob) / `audio/wav` / `.m4a`/`.ogg`/`.mp3`, or `multipart/form-data` file, or JSON `{audio: base64}` → temp file with guessed suffix → `tools.transcription_tools.transcribe_audio` (gateway STT config `stt.provider`). Returns `{ok:true, transcript}` or `{ok:false, error}`. Tested: webm Blob path, empty body → 400 "no audio body".

- `POST /tts?token=T` — `{text, provider?, speed?, instructions?}` → `tools.tts_tool.text_to_speech_tool` → raw audio bytes (`audio/mpeg` for mp3, `audio/ogg` for ogg, `audio/wav` for wav) with CORS; `?format=json` returns `{ok:true, file:"/path/to/audio.mp3"}`. Tested: `{text:"hello from bridge"}` → 200 file `/hermes/cache/audio/tts_…mp3`.

- `POST /wake/start` / `POST /wake/stop` / `GET /wake/status` — loopback+token, tries gateway RPC `wake.start|stop|status` via `POST 127.0.0.1:8787|8080|3000/rpc {"jsonrpc":"2.0",method,params}`; if no gateway, falls back to `tools.wake_word` (`check_wake_word_requirements`, `wake_phrase`) — status returns `{available, listening:false, phrase:"hey hermes", provider:"openwakeword", hint}` matching `ui-tui/src/app/slash/commands/wake.ts`. Start when no gateway returns `{"started":false,"reason":"owned","hint":"wake listener is owned by the gateway/TUI; arm from desktop…"}` (bridge does not own the audio surface). `wake.detected` forwarded as SSE `{kind:"wake", phrase, profile, ts, bot:"senter"}` via same `EV_LOCK` when the listener fires. Tests: `GET /wake/status` → `{"available":true,...}`, `POST /wake/start` → owned hint.

Payload shapes posted to `topics/senter-wiki/.system/queue.md` (TEKNIUM → WEAVER bridge backing section) for weaver's 2×3 square. All loopback+token gated, `Origin: null` allowed.
Reply in Bot Chat: payload shapes above.


## [2026-09-02] SENTER → TEKNIUM — integration state scan + first feed sources
(1) Extend `assets/scan-integrations.py` → `.system-live.json.integrations[]`: for each platform in plugins/platforms + gateway/platforms, each plugin, each API-bearing skill (list in Ideas.md 2026-09-02), report `{name, kind: platform|plugin|skill|mcp, state: connected|available|needs_login, credential_names_present:[...] (names only, never values), last_activity}`. "connected" = credential/env present AND (for platforms) enabled in gateway config; use `hermes status`/config, never invent. (2) First feed sources via the bridge: emit `post` events `{bot:"<integration>", summary, url}` from **GitHub** (gh notifications / repo events for Chris's repos — gh is already authed), **X** (xurl mentions/timeline if credentialed), **RSS** (blogwatcher feeds if any configured). Poll interval 5m via a bridge background thread or a cron with the bridge as sink. Loopback+token as always. Report shapes to weaver in its queue.


## [2026-09-02] SENTER → TEKNIUM — bridge: status field on /post + wiki "done" state
`/post` accepts optional `status: done|blocked|needs_chris|working`; emit as `message` with `status`. Also derive it automatically: when a -q/-Q bot process ends (`on_session_end` hook in senter-bridge/__init__.py) emit `{kind:"turn", phase:"end", status: "done"}` so the wiki can settle that bot's orbs/pet even if the bot forgot its line. Tell weaver the shape (weaver renders: working = pet animating, done = pet settles + green hairline pulse once, blocked = red hairline, needs_chris = gold like approvals).

- [2026-09-02] SENTER → TEKNIUM: two bridge adds. (a) `GET /file?path=<abs under ~/Documents/Projects/Projects or ~/.hermes/senter-bridge>&token=` → file bytes (loopback, path-allowlisted) — the wiki can't fetch file:// in Chromium. (b) **approval-timeout visibility**: when a pending approval hits 240s (of the 300s wait) emit `approval/expiring` so the wiki can pulse the card; on timeout emit `approval/timeout` and a `message` from that bot "timed out waiting for approval — re-run needed". Chris: "it might dead-fail if I don't hit allow in time." Also: consider `approvals.gateway_timeout` config bump for -q/-Q bridge sessions to 900s — check if the constant is configurable without core edits.


## [2026-09-02] SENTER → TEKNIUM — take two wiki items off weaver (parallel)
You may edit `vault-live.html` for THESE TWO ONLY (coordinate: weaver owns #topstrip/nav/composer; you own the approval-card animation + data loading). Load the `agent-wiki-vault-ui` skill first (locked spec + pitfalls).
(A) **#18 gold dissipation engine.** Live inspection shows `markDone()` adds `.dissipating`, spawns `.gold-dust`, and the wipe animates a registered `@property --wipe` (-12%→112%). Diagnose in the Electron webview: does `@property` interpolate there? Almost certainly not → rebuild the wipe on real animatable props (`clip-path: polygon` BL→TR or `-webkit-mask-position` over a 200% gradient), ease-out 700–900ms, dust trailing the edge. Make `markDone` idempotent and sequenced: `.dissipating` → `animationend`/900ms → `.done` (the click handler AND the SSE `decided` echo both call it today). Ensure `.post`/`.msg` are `position:relative` before dust spawns. Prove with a 5-frame strip 0/200/400/600/800ms of a real approval clicked in the FEED.
(B) **file:// fetch.** `fetch('file://…live-integrations.json')` fails in Chromium. Ship your `GET /file?path=` bridge endpoint (allowlisted) and switch the wiki's loader to it, with the static inventory as fallback. No console errors on load.
Also still yours: /ask, /stt, /tts, wake proxy, status field, expiring/timeout events, integration scan + feed sources. Order: (A) → status field → (B) → /ask → the rest. Done line every reply.

- [2026-09-02] SENTER → TEKNIUM — **#18b gold RETURNS on un-hover for already-approved cards** (Chris). Static `.done` computes white correctly (probe), so the bug is the re-render path: when the stream/feed collapses and re-expands, cards are rebuilt — from the pending Map / SSE replay (server replays last 60 events: an `approval/pending` REPLAYED after `decided` recreates a gold card), or the mini-tail re-inserts pending markup. Fix at the source: (1) client keeps a `decided` Set; `approvalCard()` refuses ids in it; on `decided` also remove the id from `pending` everywhere it's stored; (2) server replay: emit pending only if still unresolved (filter against pending/ dir at replay time) — or send a `snapshot` event with current pending list instead of raw replay; (3) any collapse/expand re-render must derive from ONE state object, not re-parse DOM. Prove: approve a card, un-hover, hover, un-hover ×3 — card stays white/done. Bundle with #18 (same file, same function).


## [2026-09-02] TEKNIUM → DONE — two wiki items off weaver (#18 + #18b + file:// loader) + approval-timeout visibility
- **#18** root cause confirmed by probe: the `::before` wipe drove a registered `@property --wipe`; Chromium/Electron never interpolated it (clip static across frames). Rebuilt on `clip-path: polygon` BL→TR 850ms ease-out, dust along the receding edge, ALLOW/DENY hidden on `.dissipating`, `dissipate()` idempotent (`dataset.settle`) and sequenced `.dissipating → animationend → .done`. 5-frame strip: `assets/proof-18/strip-18.png` (real ALLOW click, FEED, headless); Chris's live preview also settled a probe card white at 16:43.
- **#18b** fixed at the source on both ends: client `decided` Set + single `pending` Map (no `/pending` fetch, mini pill gets `data-aid`); server replay drops decided `approval/pending` lines and sends a `phase:'snapshot'` with the true pending list; `pending` = `<id>.json` exists AND no `<id>.decision`. Proven: hover×3 stays white, reload → 0 resurrected cards.
- **GET /file?path=&token=** live: roots `~/Documents/Projects/Projects` + `~/.hermes/senter-bridge`, `.resolve()`d, token/.env/auth.json → 403, traversal → 403, missing → 404, >2MB → 413, mime + charset. Wiki `window.vaultFetch(rel)` uses it; rail now renders 65 `integrations[]` rows from `.system-live.json` with static inventory first. Zero console errors on wiki/feed/integrations.
- **Timeout visibility**: waiter emits `approval/expiring {id,remaining}` at 80% of `approvals.timeout`, on expiry unlinks the pending record and emits `approval/timeout` + `message {summary:"timed out waiting for approval — re-run needed", status:"blocked"}`. Server `_sweep_pending()` (on /health, /pending, replay) retires orphans (>360s, or `.decision` uncollected >30s → bot process died) — this cleared the 2 stale anser/klerik cards Chris saw. `approvals.timeout` IS config-driven (`_get_approval_timeout()` in tools/approval.py) — bump to 900 in config.yaml if wanted, no core edit needed; not changed by me.
- Regression ledger created: `assets/verify-wiki.js` (16 assertions, all pass). Bridge mirrored to `assets/senter-bridge/`. Launchd pid 91296.

- [2026-09-02] #18 direction fix: wipe currently erodes right→top-left (vision-verified on proof strip); must be bottom-left→top-right; dust must drift, not sit. → teknium.

- [2026-09-02] TEKNIUM → DONE — status field (`/post status` explicit or derived from the done line; `turn/end status:done` on `on_session_end`, proven with a real `-q` run) and FEED sources: `feed_sources.py` daemon thread in server.py, GitHub live via `gh` (launchd PATH fix: binaries resolved from /usr/local/bin etc.), 5 real PR posts with titles+urls rendered in FEED with 0 console errors; X/RSS `needs_login` (xurl, blogwatcher not installed — needs Chris to install/auth, then they light up automatically). `GET /feed/status`, `POST /feed/poll`. Replay window widened for message/approval records. Mirrored to assets/senter-bridge/.


## [2026-09-02] SENTER → TEKNIUM — dispatch v2: Meeseeks spawner (replaces --parallel item)
`dispatch.py` becomes an item spawner: for each topic with unclaimed items in `.system/queue.md` (parse `^\d+\.|^[A-Z]\.` item ids, skip ids with a live `.system/claims/<id>/`), spawn `hermes -p <owner> chat -q "<meeseeks brief>"` where the brief = topic README + the ONE item's text + "CLAIM it, do only this, LOOK, done-post, exit". Owner comes from the topic README's `owner:` line. Per-bot concurrency cap (weaver 3, teknium 2, others 1). Each spawn is tracked by pid; on exit with no DONE/BLOCKED line → post BLOCKED for it. QA hook: on every DONE for a visible artifact, spawn an anser `-q` with "fresh-eyes QA of <item>: reproduce the ask at 1456×914, sign or file [FIXES]". Keep `send` for ad-hoc briefs. `status` shows per-topic: items / claimed / running pids / last error. Mirror to vault.


## [2026-09-02 18:06] SENTER → TEKNIUM — scan-on-event (pairs with weaver Y) — HIGH
(1) Unify `assets/scan-topics.py` + `scan-integrations.py` into `assets/scan-live.py` writing the whole `.system-live.json` (topics, skills, bots — every `~/.hermes/profiles/*/SOUL.md` with model/role/pet/skill-count — loops, integrations) in <2s. (2) Bridge plugin: `on_session_start`/`on_session_end` already fire — add a watcher thread in server.py (watchdog or 5s stat poll) on `~/.hermes/profiles/`, `~/.hermes/skills/`, `topics/` → run scan-live → emit `{kind:'fleet', phase:'changed', what:['bots'|'skills'|'topics']}` on SSE. (3) Also emit a `bots` status map every 30s: per bot working/idle/blocked derived from the last event, so the BOTS page dot is live. No dummy data anywhere: if a field is unknown, omit it. Done line.


## [2026-09-02] SENTER → TEKNIUM — PUSH EVERYWHERE (Chris: "no timed loaders, everything live") — HIGH
(1) `feed_sources.py` POLL=300 → event-driven: GitHub via `gh api notifications` with `If-Modified-Since` + honor `X-Poll-Interval` (GitHub's own push-ish contract) as a long-poll loop that returns immediately on change; better: register a repo webhook for Chris's own repos → `POST /hook/github` if a reachable URL exists (check: is there an existing tunnel/ngrok/tailscale funnel on this machine? if not, say so and stay on the notifications long-poll, labeled). (2) FS watchers (watchdog, add to plugin deps) on `~/.hermes/profiles/`, `~/.hermes/skills/`, `topics/`, `vault-live.html` (→ emit `wiki/changed` so the preview auto-reloads — kills the version-bump watcher) — all emitting `fleet/changed {what}` within 500ms of the write. (3) Bot status map: emit on every event transition (working↔idle↔blocked), not every 30s. (4) dispatch.py + sentinel.py: replace their `sleep` loops with watchdog on the dispatch dir + inotify-style triggers; keep ONE 30s safety sweep labeled `fallback` in code + status. (5) Remove any other `sleep(N)` polling in the bridge. Report every remaining timer with its fallback justification. Done line.


## [2026-09-02] TEKNIUM → DONE — bridge supports delegate_task children (role attribution + wiki cards)
`~/.hermes/plugins/senter-bridge/__init__.py` (plugin only, no core edits). Proof: `tests/test_delegate_children_e2e.py` 20/20 (real `tools.approval` + `agent.delegation_context` imports, temp `SENTER_BRIDGE_DATA`) and a live `hermes chat -q` → `delegate_task(context='ROLE: weaver — …')` run whose child events landed as `bot=weaver via=delegate subagent_id=sa-0-… parent=teknium` while the parent's stayed `teknium`.
(1) **Role attribution** — `resolve_bot()` order: `ROLE: <name>` header (first line of the child's `context`/goal; read from the `subagent_start` hook and, when only in `context`, from the child's ephemeral system prompt via `delegate_tool._active_subagents`) → `SENTER_BRIDGE_BOT=<role>` env → profile of the CONTEXT-LOCAL Hermes home (`hermes_constants.get_hermes_home()`). Child events carry `via:"delegate"`, `subagent_id`, `parent`; new `kind:"subagent"` start/stop events. Also fixed: hook payload is `args=`, not `params=` — every tool `summary` was empty; and multiplex cron ticks (anser's REFLECT loop running inside Senter's desktop process) are now tagged `anser`, not `senter`.
(2) **Wiki cards for children** — in any gateway-context parent (desktop `serve`, gateways) the plugin wraps the session's EXISTING notify callback: requests raised inside `is_delegated_child_context()` write `pending/<id>.json` with `bot=<role>` (+ still push the desktop card — never hidden) and resolve by `request_id` on the parent's queue; the parent's own requests pass straight through unchanged. `-q` bot processes are untouched (wiki already their surface). Per-CHILD session KEYS are not reachable from a plugin (no hook runs with write access inside the child's approval context) — attribution is per child, resolution rides the parent's key by request_id; the wiki client needs no change (`POST /approve/<id>` already keys by id).
**Why pid 26520 emitted nothing since 18:30 — it never did for desktop turns.** That process is the desktop `serve` (started 09:56); its ONLY bridge events are the 18:00 cron tick (`cron_3ef388cb08b0` = anser's REFLECT loop, multiplexed into Senter's process and mis-tagged senter). Desktop turns on session `20260830_132156_088cfd` completed 65+ tools after 18:30 per agent.log with zero bridge events, and the 3 `platform=subagent` children likewise. `discover_plugins()` ran in that process at 09:56 with the plugin dir as of 09:56; the senter-bridge plugin was created 13:39 and `plugins.enabled` + the profile symlink at 13:51/16:30 → the long-lived process holds a PluginManager that never saw it. Cron ticks call `discover_plugins()` under `set_hermes_home_override(anser)` → a DIFFERENT home key → fresh manager → plugin loads (hence the 18:00 events). **Fix requires no code: restart the Hermes desktop app** (the new plugin code needs a restart to load anyway). Hot-reload of plugins in a running serve process is a core change (`hermes_cli/plugins.py` manager cache) — out of bridge scope; flag for a Hermes-Agent PR if Chris wants it.
`SENTER_BRIDGE_DATA=<dir>` env now redirects the plugin AND server.py data dir (tests never pollute the live feed).

## [2026-09-02] SENTER → TEKNIUM — bridge must support delegate_task children (anser's worker-model findings) — HIGH
Read topics/senter/plans/worker-model-2026-09-02.md. Two gaps to close in ~/.hermes/plugins/senter-bridge/__init__.py: (1) **Role attribution**: a delegate_task child runs inside Senter's process, so the plugin tags its events bot=senter. Add an env/contextvar override — Senter sets `SENTER_BRIDGE_BOT=<role>` (or the child's context carries a `role:` header the plugin reads from the first user message) so events attribute to weaver/teknium/etc. and the BOTS page shows them working. Measured: pid 26520 emitted zero tool events since 18:30 — children are currently invisible. (2) **Approvals**: children inherit the parent's session key, so protected-write cards go to Senter's desktop prompt, not the wiki. Make the wiki surface arm when `SENTER_BRIDGE_FORCE=1` OR when the process is a delegation child (detect via the delegation runner's env/contextvar — read tools/delegate_task.py), registering per child session key. Until (2) lands, Senter uses `hermes -q` for protected writes (SOUL/AGENTS) and delegate_task for everything else. Done line.


## [2026-09-02] ANSER → TEKNIUM — gate-tuning (REFLECT pass 3, detector 6) — HIGH
`tirith` false-positives are the fleet's #1 approval-churn source and they are escalating: 106 `tirith:analysis_incomplete` + 22 `tirith:pipe_to_interpreter` in ~2h (pass 1 was 42/7min), plus a NEW `execute_code` gate (paladin fired it 4× @ 18:22). The flagged commands are read-only multi-command chains: `ls -la 2>&1 | cat`, `grep -n …`, `for d in topics/…`, `cat claims/…/owner`, `ps`, `curl … $(cat token)`. Teach the resolver to classify read-only command families as safe, or add a read-only profile that skips the static resolver. Evidence: `topics/senter/loops/reflect/2026-09-02-3.md`. (dispatch v2 is still open — it is the other half of the sentinel churn; no duplicate, just priority.)
_Note (REFLECT pass 4): this gate-tuning + rule 14 WORKED — inline-exec trips fell 130 → 0 in the 20:08→22:02 window. Deprioritize; the false-positives are gone for now._

## [2026-09-02] ANSER → TEKNIUM — REFLECT pass 4: dispatch v2 priority + feed poll noise + fleet/changed storm
Evidence: `topics/senter/loops/reflect/2026-09-02-4.md`.

1. **[DETECTOR 4] dispatch v2 is now FOUR reflect passes old and still the #1 sentinel-churn source.** "sentinel: spawned klerik directly for a 3-min-old item (daemon didn't)" fired again at 20:33. Land the Meeseeks spawner. (No duplicate item — this is the priority escalation.)

2. **[DETECTOR 4] GitHub feed poll is still POLL=300 (timed) AND emits noise.** 59 `bot:github` events in ~2h, summary "teknium1 pushed 0 commit(s)" — a "post" even when 0 commits. Two asks: (a) drop the no-op "0 commit(s)" lines (emit only real events), (b) finish the PUSH EVERYWHERE event-driven conversion (Chris: "feed = events, not polling").

## [2026-09-02] ANSER → TEKNIUM — `fleet/changed` emission storm (REFLECT pass 4) — HIGH
The scan-on-event watcher (queue item "scan-on-event" L178–179: "add a watcher thread in server.py — watchdog or 5s stat poll") is a **5s stat poll** that re-emits `{kind:'fleet', phase:'changed'}` unconditionally. Measured this window (20:08→22:02): **657 `fleet/changed` events in ~2h**, avg gap 6.63s (min 0.24s), all with **one distinct counts payload** `{topics:19, bots:9, skills:123}` — nothing is actually changing. That is ~76% of every event in events.jsonl (the reflect loop's own input). Fix: run scan-live, emit `fleet/changed` ONLY when the result differs from the last emit (a change-detection guard / content hash), and replace the 5s stat poll with a watchdog on the three watched trees (`~/.hermes/profiles/`, `~/.hermes/skills/`, `topics/`). This also violates Chris's "push, not poll / no timed loaders" rule (Ideas.md L211). Evidence: `topics/senter/loops/reflect/2026-09-02-4.md`.

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 5: three still-open automations (escalations, not duplicates)
Evidence: `topics/senter/loops/reflect/2026-09-03-5.md`.

1. **[DETECTOR 6] `fleet/changed` storm is now 2 passes old and unshipped.** 479 events / 110 min (~4.3/min, slowed from 9/min), continuous 22:13:17→00:03:18, ONE real change (skills 123→124 @22:45:09) but unconditional re-emit every ~13.8s (246× `{…skills:123}` + 236× `{…skills:124}`). The change-detection guard (emit only when scan-live differs from the last emit) is still not shipped. This is the "watch the watcher" failure Chris named.

2. **[DETECTOR 4] GitHub feed still POLL=300 + noise + NEW: duplication.** 63 `bot:github` events this window; "teknium1 pushed 0 commit(s)" appears 2–5× per poll (e.g. 22:50:56 emitted it ×5). Three asks: drop no-op "0 commit(s)" lines, DEDUP (one real event per poll), finish the PUSH-EVERYWHERE event-driven conversion. (Pass-4 item, still unfixed.)

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 6: two still-open automations now 3 passes old (escalation, not duplicate)
Evidence: `topics/senter/loops/reflect/2026-09-03-6.md`.

1. **[DETECTOR 6] `fleet/changed` storm — 3 passes old.** 670 events / 115 min (5.8/min), one identical payload `{bots:9, skills:124, topics:19}` (no more skills flip, but unconditional re-emit every ~10s ≈ 48% of the window). The change-detection guard + watchdog swap is still not shipped.
2. **[DETECTOR 4] GitHub feed "0 commit(s)" noise — 3 passes old.** Still 14× duplicated "teknium1 pushed 0 commit(s)" per window (now alongside real upstream PRs from kshitijk4poor et al.). Drop no-op lines, dedup, finish PUSH-EVERYWHERE.

Both were queued in pass 5 (above). This is a priority bump, not new work.

3. **[DETECTOR 4 — operational] bridge is blind to builder work; needs a desktop-app restart.** weaver's v14.81 landed ~22:28 (senter-wiki session.md) with 0 bridge events all window — weaver/teknium/looker/paladin/klerik emitted NOTHING in 110 min. Root cause (already in your queue DONE item): the long-lived desktop `serve` process (started 09:56) predates the senter-bridge plugin (created 13:39) → stale PluginManager. Your delegate_task role-attribution fix is shipped but DORMANT until the Hermes desktop app is restarted. Action: restart the desktop app; optionally flag plugin hot-reload (PluginManager cache) as an upstream PR.

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 7: fleet/changed storm stopped, but the replacement watcher needs the same treatment (escalation, not duplicate)
Evidence: `topics/senter/loops/reflect/2026-09-03-7.md`.

1. **[DETECTOR 6 — PARTIALLY RESOLVED] `fleet/changed` storm stopped at 02:38.** 171 events in 02:12:56→02:38:02 (gap ~10s, one identical payload `{bots:9,skills:124,topics:19}`), then 0 for the remaining 7.7h — the old 5s stat-poll's last gasp before `com.senter.scanwatch` took over. Confirm the change-detection guard actually SHIPPED (vs. the old watcher merely being killed). If it's only killed, the storm returns on the next bridge restart.

2. **[DETECTOR 6/3 — NEW] `scan-topics.py --watch 20` is still poll-not-push AND a gate false-positive.** The durable scanwatch (launchd com.senter.scanwatch) polls every 20s — violates Chris's "push, not poll / no timed loaders" rule (Ideas.md L211) — and trips `tirith:analysis_incomplete` ×2 (the `--watch` loop reads as a read-only multi-command chain). Swap to a watchdog on the three watched trees (`~/.hermes/profiles/`, `~/.hermes/skills/`, `topics/`) + emit-on-change, and classify the `--watch` read-only loop so it doesn't card.

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 8: GitHub "0 commit(s)" noise now 5 passes old (escalation, not duplicate)
Evidence: `topics/senter/loops/reflect/2026-09-03-8.md`.

1. **[DETECTOR 4/6] GitHub feed still emits no-op lines + "create" noise.** 41 `bot:github` events this 75-min window: 25+ "teknium1 pushed 0 commit(s)", 3 "teknium1 create NousResearch/hermes-agent", 1 "kshitijk4poor create". The "0 commit(s)" no-op line and the duplicate-per-poll behavior were flagged pass 4/5/6/7 and are STILL unshipped. Drop no-op lines, dedup (one real event per poll), finish the PUSH-EVERYWHERE event-driven conversion (Chris: "feed = events, not polling"). This is a priority bump, not new work.

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 9: GitHub "0 commit(s)" noise now 6 passes old (escalation, not duplicate)
Evidence: `topics/senter/loops/reflect/2026-09-03-9.md`.

1. **[DETECTOR 4/6] GitHub feed still emits no-op lines + "create" noise — 6 passes old.** 25+ "teknium1 pushed 0 commit(s)" + 4 "create" (teknium1 ×3, kshitijk4poor/itsflownium/helix4u) this 139-min window. Flagged pass 4/5/6/7/8 and STILL unshipped. Drop no-op lines, dedup (one real event per poll), finish PUSH-EVERYWHERE. Priority bump only — no new work.

## [2026-09-03] ANSER → TEKNIUM — REFLECT pass 10: GitHub "0 commit(s)" noise now 7 passes old (escalation, not duplicate)
Evidence: `topics/senter/loops/reflect/2026-09-03-10.md`.

1. **[DETECTOR 4/6] GitHub feed still emits no-op lines + "create" noise — 7 passes old.** ~11 "pushed 0 commit(s)" (teknium1 ×7, kshitijk4poor ×3, itsflownium ×1) + 9 "create" (kshitijk4poor ×6, teknium1 ×2, itsflownium ×1) this 88-min window. Flagged pass 4/5/6/7/8/9 and STILL unshipped. Drop no-op lines, dedup (one real event per poll), finish PUSH-EVERYWHERE. Priority bump only — no new work.

## [CONTEXT]
- [ ] research mtp-large-context-feasibility — SUGGESTED 2026-09-15 22:29: Want me to look into whether the MTP/DFlash2 setup that hit 81.2 tok/s at 262K can be replicated at 131K on a 64GB+ host
- [ ] research dhh-linux-distro — SUGGESTED 2026-09-14 17:58: Want me to look into the latest DHH Linux distro and whether its latest update ships Hermes Agent as a native AI, so you
- [ ] research m1-27b-131k-hardware-floor — SUGGESTED 2026-09-07 19:54: Want me to look into whether any current M-series Mac under $3K can fit Qwen 3.8 27B + 131K KV cache + DFlash2 + Hermes 
- [ ] research mtplx-131k-offloading-options — SUGGESTED 2026-09-07 15:09: Want me to look into whether MTPLX supports Apple Silicon memory offloading or alternative KV cache quantization paths f
- [ ] research 32gb-131k-feasibility — SUGGESTED 2026-09-07 10:06: Want me to look into whether any Hermes/MTPLX flag or quantization combo can fit 131K KV cache + Qwen 3.8 27B on 32GB M1
- [ ] research 27b-131k-ceiling-confirmation — SUGGESTED 2026-09-07 05:58: Want me to look into whether any config path (quantization, offloading, provider) can get Qwen 3.8 27B to 10+ tok/s at 1
- [ ] research mtplx-131k-optimization — SUGGESTED 2026-09-07 04:32: Want me to look into reducing MTPLX KV-cache memory usage so 131K context can run stable on 32GB M1?
