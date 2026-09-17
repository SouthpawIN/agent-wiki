# Queue — senter-wiki
Owner: weaver · Coordinator: senter · Format: `- [ ] [KIND] item — acceptance` · claim `[~]` · done `[x]`
Only Context (watcher/umbrella/Chris) creates entries; factories claim and close them.

## [CONTEXT]
- [ ] research m1-131k-performance-model — SUGGESTED 2026-09-10 14:49: Want me to look into what's actually achievable at 131K context on a 32GB M1 before we commit to a local model choice?
- [ ] research librarian-ux — SUGGESTED 2026-09-07 20:07: Want me to look into how other wiki/linker tools handle progressive disclosure of entities?
- [ ] research wiki-compile-pre-planning-research — SUGGESTED 2026-09-06 22:36: Want me to look into lightweight pre-planning techniques that reduce duplicate wiki pages without heavy infrastructure?
- [ ] research compile-pre-prompting-practices — SUGGESTED 2026-09-05 19:27: Want me to look into which pre-planning / pre-prompting techniques (Karpathy's LLM-wiki practice, plan-then-write, schem
- [ ] research bot-apply-end-to-end — SUGGESTED 2026-09-05 19:00: Want me to look into why only the loop half of the apply path got proven — what a bot promotion (e.g. senter-wiki-bot) a
- [ ] research merge-split-governance-owner — SUGGESTED 2026-09-05 18:39: Want me to look into where merge/split governance should live now that the umbrella collapsed into the topic agent — the
- [x] Export all Senter/wiki sessions into `.system/sessions/` — 9 transcripts, 5.2 MB (2026-09-05)
- [x] Pull agent-wiki spec + GOOP whitepaper/nesting into `.system/knowledge/` (2026-09-05)
- [ ] Rewrite the sidebar's SOUL/AGENTS to yes-and rubber-duck + "no tasks" + INDEX-first reading — Chris approves the text
- [ ] Decide merge/split of `senter` vs `senter-wiki` — umbrella proposes with evidence from similarity

## [SKILLS]
- [ ] wiki-safe-edit-contract — distilled 2026-09-06 22:36 → skills/wiki-safe-edit-contract/SKILL.md (auto-applied)
- [ ] wiki-hover-stays-under-cursor — distilled 2026-09-05 19:27 → skills/wiki-hover-stays-under-cursor/SKILL.md (auto-applied)
- [ ] wiki-approval-apply-proof — distilled 2026-09-05 19:00 → skills/wiki-approval-apply-proof/SKILL.md (auto-applied)
- [ ] wiki-page-quality-check — distilled 2026-09-05 18:39 → skills/wiki-page-quality-check/SKILL.md (auto-applied)
- [ ] wiki-real-audio-pipeline — distilled 2026-09-05 17:49 → skills/wiki-real-audio-pipeline/SKILL.md (auto-applied; edit or delete freely)
- [ ] topic-wiki-compile — distilled 2026-09-05 17:49 → skills/topic-wiki-compile/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-feed-verify — distilled 2026-09-05 17:36 → skills/wiki-feed-verify/SKILL.md (auto-applied; edit or delete freely)
- [ ] wiki-event-performance — distilled 2026-09-05 17:22 → skills/wiki-event-performance/SKILL.md (auto-applied; edit or delete freely)
- [ ] senter-proposal-pipeline — PROPOSED 2026-09-05 17:13 → skills/senter-proposal-pipeline/SKILL.md.proposed (approve: drop .proposed)
- [ ] wiki-derived-anchors — PROPOSED 2026-09-05 17:06 → skills/wiki-derived-anchors/SKILL.md.proposed (approve: drop .proposed)
- [ ] wiki-hit-zone-layering — PROPOSED 2026-09-05 17:06 → skills/wiki-hit-zone-layering/SKILL.md.proposed (approve: drop .proposed)
- [x] senter-watcher — operating the watcher (2026-09-05)
- [x] progressive-disclosure — how any agent reads the memory layer (2026-09-05)
- [x] wiki-ui-knobs — every CSS/JS knob in vault-live.html with its owner rule (2026-09-05)
- [x] approval-cards — bridge POST /approve + APPROVE/REJECT on the pinned card (2026-09-05) — how a factory emits one card per proposal and reads the verdict — depends on approval transport
- [x] topic-worker-distil — first real pass produced 5 .proposed skills (2026-09-05) — inbox.md → 3–5 SKILL.md candidates → rubric → `.proposed` — acceptance: a real proposed skill in a topic

## [AGENTS]
- [ ] vault-layout-fixer — SUGGESTED 2026-09-10 14:49: I see you need the layout fixed so bots and sessions visibly render in the BOTS section — want a bot that patches render → agents/vault-layout-fixer.md.proposed
- [ ] librarian-bot — SUGGESTED 2026-09-07 20:07: I see you're talking about a librarian that progressively discovers wiki skills, bots, and loops — want a bot that surfa → agents/librarian-bot.md.proposed
- [ ] senter-wiki-readme-live — SUGGESTED 2026-09-06 22:36: I see you want wiki topic headings to stay live when README.md changes — want a bot that re-renders the topic body throu → agents/senter-wiki-readme-live.md.proposed
- [ ] sidebar — the conversational surface (default profile) with the new SOUL; zero tools that "do"
- [ ] topic-worker — `hermes -p senter <topic>` invocation contract (cwd, claim, outputs) documented in agents/topic-worker.md

## [LOOPS]
- [ ] bot-schema-watch — SUGGESTED 2026-09-10 14:49: Want a loop that watches .system-live.json for bot schema drift (skills as list vs int) and posts when stale scan-topics → loops/bot-schema-watch.md.proposed
- [ ] git-vault-sync — SUGGESTED 2026-09-10 14:49: Want a loop that auto-pulls remote changes into the vault and restarts scan-topics so updates never 'keep failing' again → loops/git-vault-sync.md.proposed
- [ ] entity-discovery — SUGGESTED 2026-09-07 20:07: Want a loop that rescans topics/*/skills and proposed bots/loops every tick to feed the librarian view? → loops/entity-discovery.md.proposed
- [ ] cron-fire-witness — SUGGESTED 2026-09-05 19:00: Three bots now have crons that 'actually fire' — want looker to watch each first tick land in your corner feed and post  → loops/cron-fire-witness.md.proposed
- [x] compile-quality-gate — SUGGESTED 2026-09-05 18:39: Want the compile loop to run the new wiki-page-quality-check on one page every tick and put the 5/5 result on the feed c → loops/compile-quality-gate.md.proposed — superseded 2026-09-05 (build-process chatter or already done)
- [ ] wiki-dedupe-sweep — SUGGESTED 2026-09-05 18:39: Two compiles over the same raw left 17 same-subject page pairs in senter-wiki — want paladin to sweep every topic's wiki → loops/wiki-dedupe-sweep.md.proposed
- [x] watcher — launchd `com.senter.watcher`, per message (2026-09-05)
- [x] topic-worker — launchd every 5m (2026-09-05) — was: `hermes cron` every 5m per active topic, claims via `hermes kanban`, writes `.proposed` artifacts + a card
- [x] umbrella — launchd every 30m (2026-09-05) — was: `hermes cron` every 30m over `topics/*`: merge/split/dedupe proposals, catalogs refresh (`topics/_global`)
- [ ] approval-relay — `hermes serve approval.pending/respond` ↔ feed card buttons (Anser #1)

## [FIXES] (carried from 2026-09-02, still open unless struck)
- URGENT: Bot/skill page editor AUTO-FIRES "Senter Wiki edit … replacing its contents" saves with no user action — bridge events.jsonl shows SOUL+AGENTS pairs emitted ~1ms apart for turbosovth, weaver, and skill "turbofit", repeating every ~40s (ts 1788391234 / …277 / …300). Each one is a protected-file write request into a bot session. Kill the autosave/onblur/onload trigger: saves fire ONLY on explicit Save click, ONLY when content differs from disk.
- Bot-page editor round-trips markdown lossily (found 2026-09-02 on turbosovth SOUL/AGENTS "edits" that were really no-ops): numbered lists reset to `1.` after any interruption, hard-wrapped continuation lines become separate paragraphs, and "Role:/Mission:" line breaks collapse. Editor must send the raw source text unchanged (textarea/contenteditable innerText, not re-serialized from rendered HTML), and should skip the save entirely when the content is byte-identical to disk. Senter refused both writes — would have degraded the files.
- Player meta flashes "NOT CONNECTED · PLAYING" when a track is set before source picked — derive from track presence, not source.
- Feed stream: `notify()` cards for `you` posts need an avatar (use senter pet or a Chris avatar asset).
- vault-live.html WIKI rows are BAKED at vault-build time — after paladin ships the topic merge + similarity lockdown, the page still showed the 37 baked rows + pre-merge thresholds. Needs a vault rebuild on weaver's side (re-run the build so rows + similarity thresholds regenerate from `.system-live.json`). (Routed 2026-09-06 from klerik queue item 2026-09-03 REFLECT pass 6/2nd, detector-4 — paladin's note never became a weaver queue item.)

## [FEATURES] (carried)
- Live event bus: fleet stream / twinkles / orbs fed by real bot events (bot-mode DM log or gateway websocket) instead of demo replay.
- File-watcher: vault edits (READMEs, .system/*) re-render rows + LIVE_SKILLS/LIVE_BOTS without manual regen.
- Drag-merge backend: MERGE dialog → senter op → vault archive + catalogs.
- BROWSER v2: real tabs surface (Chris: "we're going to work on that") — bookmarks live now.
- [x] YouTube audio via bridge (yt-dlp) → real EQ levels; song-name search (2026-09-05)
- Senter Radio phase 2: OAuth for Spotify / YouTube Music / Apple Music; phase 3: Evolutionary Lo-fi generator (Chris's evolutionary radio repo — awaiting pointer).
- Companion ingest: Jon Komet's hermes-browser-extension companion-plugin → "what Chris is reading" as a FEED/topic-sort input (audition, do not overlap).

[LOOPS]
- tour-refresh — re-cut assets/senter-wiki-tour.mp4 on major version (script tour-script.json, record-tour-vo.js, beat.py).

---

## [AGENTS] — profile finalize (klerik → senter desktop session, 2026-09-02)
Base spawn DONE by klerik: profile created (`hermes profile create weaver --clone-from senter`), skill `agent-wiki-vault-ui` copied intact (verified identical to senter's copy), model set to teknium's tier (opencode-free / muse-spark-1.2-contributor-free), profile.yaml description set. Remaining — apply in desktop session:

### EDIT A — REPLACE ENTIRE FILE `~/.hermes/profiles/weaver/SOUL.md` with:
```markdown
# Weaver — the Weaver (Senter Wiki UI builder)

You are **Weaver** — you build and maintain the Senter Wiki UI:
`~/Documents/Projects/Projects/vault-live.html` + `assets/` (v-line tracked in
`topics/senter-wiki/README.md`). The coordinator (**senter**) routes requests to you and
never edits the HTML itself. You take work from the topic queue; you do not take requests
from anyone else's chat without senter routing them. (Profile created 2026-09-02 by klerik.)

## Fleet
| Bot | Job |
|-----|-----|
| senter | Coordinator: routes work to you, tracks outcomes |
| klerik | Profile factory (made you; profile changes route through it) |
| dogeman | YouTube/content studio (content, not frontend) |
| teknium | Hermes-Agent builder (core fixes, not the Wiki UI) |
| turbosovth | TurboFit support |
| weaver (you) | Senter Wiki UI builder |

## First run (and every cold start)
1. Read `~/Documents/Projects/Projects/topics/senter-wiki/README.md`.
2. Read `topics/senter-wiki/.system/queue.md` and pick up **[FIXES] first**, then [FEATURES],
   then [LOOPS]. Work top-down within a section.
3. Load the `agent-wiki-vault-ui` skill — it holds the locked design spec, known pitfalls,
   and the Playwright verify recipe. Chris's design corrections in that skill are NEVER
   overwritten.

## Hard rules
- **Aesthetic:** white-on-black minimal, per the locked spec in `agent-wiki-vault-ui`.
  No gradient kitsch, no font experiments outside the spec.
- **Verify before reporting.** Every change is verified headless before you report it done:
  Playwright probe with `PW=~/.hermes/hermes-agent/node_modules/playwright`; screenshots
  via computer_use (app=Hermes). A change you have not verified is not done.
- **Report as short diffs of behavior** — what changed, what behaved differently, what you
  verified. Not prose essays.
- **Outcomes are written to the vault:** log each completed item to
  `topics/senter-wiki/.system/session.md` (same turn, markdown-is-the-API).
- **Never touch other topics' files.** Your vault surface is `topics/senter-wiki/` and the
  UI files (`vault-live.html`, `assets/`). Everything else is read-only to you.
- **Terminology: profiles are BOTS.** Never call them "agents" in UI copy, comments, or docs.
```

### EDIT B — REPLACE ENTIRE FILE `~/.hermes/profiles/weaver/AGENTS.md` with:
```markdown
# Weaver — Agent Workflows

## Role
Builds and maintains the Senter Wiki UI: `~/Documents/Projects/Projects/vault-live.html` + `assets/`.
The coordinator (senter) routes requests here and never edits the HTML itself.

## First run / cold start
1. Read `~/Documents/Projects/Projects/topics/senter-wiki/README.md` (owner, spec, files, version).
2. Read `topics/senter-wiki/.system/queue.md`. Priority: **[FIXES] → [FEATURES] → [LOOPS]**, top-down within each section.
3. Load the `agent-wiki-vault-ui` skill (installed in this profile's skills/devops/) — locked design spec, pitfalls, Playwright verify recipe. Chris's design corrections in it are never overwritten.

## Work loop (per queue item)
1. **Load the skill** before touching any UI file.
2. **Implement** in `vault-live.html` / `assets/` per the locked spec (white-on-black minimal).
3. **Verify headless** before reporting: Playwright probe (`PW=~/.hermes/hermes-agent/node_modules/playwright`) against the local file; screenshots via computer_use (app=Hermes) when visual confirmation is needed. Unverified = not done.
4. **Report as short diffs of behavior** — what changed, what behaved differently, what was verified.
5. **Log the outcome** to `topics/senter-wiki/.system/session.md` the same turn (markdown-is-the-API).

## Boundaries
- Vault write surface: `topics/senter-wiki/` + UI files (`vault-live.html`, `assets/`) only. All other topics/files are read-only.
- Profile changes (SOUL/AGENTS/skills) route through **klerik** — never self-edit.
- New queue items come from **senter**; don't pull work from other chats unprompted.
- Terminology: profiles are **BOTS**, never "agents" (UI copy, comments, docs).
- Current UI version + file inventory: `topics/senter-wiki/README.md` (keep in sync when you bump versions).

## Fleet
| Bot | Job |
|-----|-----|
| senter | Coordinator: routes work, tracks outcomes |
| klerik | Profile factory (profile changes) |
| dogeman | YouTube/content studio |
| teknium | Hermes-Agent builder |
| turbosovth | TurboFit support |
| weaver (you) | Senter Wiki UI builder |
```

### POST-APPLY CHECK (klerik runs once A+B land)
- YAML/placeholder sanity check on both files (no leftover Senter identity, no *** placeholders).
- Confirm `hermes profile list` shows weaver with correct model tier.

---
## [2026-09-02] TEKNIUM → WEAVER — LIVE wiring contract (senter-bridge stable)

**Endpoint:** `http://127.0.0.1:8643` — loopback only, per-boot token at `~/.hermes/senter-bridge/token` (read via tiny local fetch). All endpoints require token via `?token=T` or header `X-Senter-Token: T`. CORS allows Origin `null` / `file://` only when token present; otherwise 401.

- `GET /events?token=T` — **SSE** `text/event-stream`. Replays last 60 lines then tails `~/.hermes/senter-bridge/events.jsonl` live (heartbeat `: beat` every 15s). Each line is `data: <json>\n\n`. Fall back to demo replay when bridge is down and SHOW dim "bridge offline" chip in fleet stream.
- `GET /pending?token=T` — JSON list of currently pending approvals `[{id, session_key, bot, command, description, pattern_key, ts}]`
- `POST /approve/<id>?token=T` body `{choice:"once|session|always"}` (default "once") — resolves waiting bot thread via `tools.approval.resolve_gateway_approval`, emits `approval` decided event, deletes `pending/<id>.json`. Returns `{"ok":true,"id","choice"}` or 404 if unknown.
- `POST /deny/<id>?token=T` body `{reason:"..."}` — same, choice "deny".
- `POST /post?token=T` body `{bot,text}` — wiki → feed (Chris posting from UI) appends `kind:"message"` event.
- `GET /health` — `{"ok":true,"pid", "pending":N}` (no auth needed).

**Event shape** (JSON line in `events.jsonl` + SSE `data:`):
`{ts:number (unix), bot:string (profile), kind:"tool"|"turn"|"skill"|"approval"|"message"|"bridge", phase?:"start"|"end"|"pending"|"decided"|"request"|"response", tool?:string, topic?:string (inferred from any path under ~/Documents/Projects/Projects/topics/<name>/, verified exists), summary?:string, command?:string, description?:string, pattern_key?:string, session_key?:string, id?:string, choice?:string, ...}`

**Wiki wiring (weaver):**
- Subscribe to `http://127.0.0.1:8643/events` (SSE; token from `~/.hermes/senter-bridge/token` — tiny fetch, fallback to demo replay when down and SHOW dim "bridge offline" chip).
- `kind=tool|turn` → `botActivity(bot)` (twinkle in bot color on topic star) + `setOrbActive(topic,'agents',true)` for turn, `'skills'` when skill file read, `'loops'` when caller is cron.
- `kind=message` → `notify(bot,summary)` into stream + FEED post with pet.
- `kind=approval` `phase=pending` → **approval card** in fleet stream AND FEED: bot pet, bot name, command/description in Rules Compressed, two glyph buttons APPROVE/DENY (white hairline, no fill; approve glows gold on hover, deny dims). Click → `POST /approve/<id>` or `/deny/<id>` → card collapses to one-line receipt (approved by chris · 12:04). Pending count also pulses ⚙-side nav gold count visible from any tab.
- Remove demo replay + random twinkles once real events flow (keep as fallback only).
- Verify headless: fake bridge with tiny node SSE server emitting all four kinds; assert twinkle fired, orb .on toggled, feed post rendered, approval card → POST → receipt.



## [2026-09-02] LIVE — done by senter (bootstrap). WEAVER picks up from here
Shipped: senter-bridge plugin + server + wiki client (see log.md). Remaining for weaver:
- [FIX] `turn started` cards were spammy → now silent; consider a compact "bot online · topic" line on `bridge/surface` only (done minimal).
- [FIX] events.jsonl grows forever → rotate at 5MB (server side).
- [FEATURE] approval card: show pattern_key + session_key on hover; DENY with reason (prompt) → POST body.reason.
- [FEATURE] orbs `loops`: fire when the calling process is a cron (`HERMES_CRON_SESSION`?) — check tools/approval.py `_is_cron_approval_context` for the marker.
- [FEATURE] topic inference: fall back to the bot's home topic (BOT_TOPIC map) when no path matches — currently null on most tool events.
- [FEATURE] FEED: bridge `message` events from message_agent deliveries (bot_mode_dm) so bot↔bot DMs show as posts. Hook point: tools/bot_mode_dm.py `_start_delivery` → emit.
- [VERIFY] weaver's own first run should show up live: its -q process arms the surface automatically.


## [2026-09-02] SENTER → WEAVER — Chris's four (priority order)
**[FIXES]**
1. **Card overflow** — klerik's long stream card bleeds under turbosovth's below it. Cards stay width 400px, straight left edge, min-height 66px, but must GROW with content: remove any fixed/max height on .msg/.post; .txt gets overflow-wrap:anywhere; if a hard cap is wanted use max-height ~220px + overflow hidden + bottom fade — never bleed. Verify with a 600-char message in #stream and in #chat .mini (headless).
2. **Approval card = real chooser.** Hermes's gate accepts once | session | always | deny (tools/approval.py resolve_gateway_approval → choice). Server already forwards body.choice. Card buttons: APPROVE ▾ (default once; dropdown: ONCE · THIS SESSION · ALWAYS) + DENY (optional reason prompt → body.reason). Receipt shows the choice. Same in stream, FEED, mini tail. House style: hairline, glyph buttons, no pills.
**[FEATURES]**
3. **BROWSER → INTEGRATIONS.** Replace the BROWSER tab (label, + behavior, view) with INTEGRATIONS: a live read of Hermes Agent's integration state — MCP servers (hermes mcp list), enabled plugins (hermes plugins list), messaging platforms configured (gateway config), credentials present/absent (names only, never values), TurboFit lane. Rows in the wiki .topic skeleton (same element as SKILLS/BOTS), hero shows the hovered integration. Data via a snapshot extension of .system-live.json written by assets/scan-integrations.py (hermes venv python); bridge can emit integrations/refresh later. + on INTEGRATIONS = "add integration" → posts to senter.
4. **Links open in Hermes desktop tabs.** Any external link in the wiki (integration cards, FEED URLs, PLAYER URL line) opens a NEW preview tab in the Hermes desktop — not an iframe. The preview pane is an Electron <webview> (apps/desktop/src/app/chat/right-rail/preview-pane.tsx); find the host's open-new-tab affordance (window.open → setWindowOpenHandler? postMessage? hermes:// scheme?) and use it; fall back to target=_blank. Verify a click really opens a tab (computer_use app=Hermes).
Report each as a behavior diff + headless proof in .system/session.md.


## [2026-09-02] SENTER → WEAVER — Chris's direct spec (do these first, in order; each = behavior diff + headless proof)
1. **Approval chooser, exactly like the Hermes desktop prompt.** Buttons on every approval card (stream, FEED, mini tail): `ALLOW` with a small `▾` arrow immediately to its right; the arrow opens a dropdown: **Allow · Allow this session · Always allow**. Plus `DENY`. Wire: ALLOW → POST /approve/<id> {choice:"once"}; session → {choice:"session"}; always → {choice:"always"}; DENY → POST /deny/<id> (optional reason). Server already forwards body.choice to `resolve_gateway_approval` (tools/approval.py accepts once|session|always|deny). Receipt shows the choice ("always allowed · by chris · 14:03"). VERIFY end-to-end: trigger a real protected write from a -q bot and pick each of the three choices; confirm `approval/decided` in events.jsonl carries the right choice and the bot proceeds.
2. **Gold = attention; gone after interaction.** Keep the gold hairline on approval cards (Chris likes it). While a card is pending: the bot's PET on that card ANIMATES in place (use the pet's spritesheet idle/wave row — teknium and s0uthpaw have animations; `~/.hermes/pets/<pet>/pet.json` + spritesheet.webp, same loader as BOTS page entry animation). Once decided: gold → normal hairline, pet freezes on its static frame, card dims to the .done state. No motion anywhere else in the stream.
3. **BROWSER → INTEGRATIONS** (replaces the tab, label, view, and `+` behavior). Live read of Hermes Agent's integration state: MCP servers (`hermes mcp list`), enabled plugins (`hermes plugins list`), messaging platforms configured (gateway config), credentials present/absent — names only, never values — TurboFit lane, senter-bridge health. Rows = wiki `.topic` skeleton (same element as SKILLS/BOTS), hero = hovered integration. Snapshot via `assets/scan-integrations.py` (hermes venv python) into `.system-live.json`; bridge emits `integrations/refresh` later. Nav must still FIT on one line at 1440 — Chris: "if you have to make the text a little smaller, make it fit; I like how everything fits now." Shrink nav font uniformly, never wrap.
4. **⚙ gear**: slightly larger than 2.4em, and vertically centered on the media widget's play-button center (measure `#media .play` bbox → align gear's center-y to it). Verify with a pixel probe, not by eye.
5. **Demo now-playing**: artist line **Humanity's Last Breath**, marquee **Godhood · Godhood** (2026 single, Century Media). Exact spelling incl. apostrophe.
6. **Links → new Hermes desktop tab** (from previous section) stays queued after these.
7. **Integration card icon touching the card's top edge** (both the full editor `.icards .iwrap` and the wiki row's integration hover card). Chris: "the icon is just touching the top of the card — I think that chips it a little. Just a little buffer between the icon and the top. There's space underneath the `+` we can use, so shift what we have up a little." Fix: add top padding inside the card so the logo has clear air (≈8–10px), and shift the card's content block up into the slack below the `+` rather than growing the card. Verify with a 3× zoom crop of the card top edge in both places.

## [2026-09-02] ANSER → WEAVER — [FIXES] approval-card correctness (from approval-flow audit)

Context: the agent's approval wait expires after `approvals.timeout` (default 300s). The bridge's waiter thread keeps polling to 3600s. A card Chris clicks AFTER the 300s window resolves 0 entries on the backend, but the UI still shows "approved".

1. **[FIX] Honor `resolved` on the `decided` event.** `handle()` → `markDone` must read `ev.resolved` (and `ev.choice`). When `ev.resolved === 0` (falsy), render the receipt as "timed out — not applied" instead of "approved · by chris". Today `decided` carries `resolved:N` but the UI ignores it and always prints the choice.
2. **[FIX] Add an "expired" card state.** A pending card whose `ts + 300s < now` is dead — the backend queue entry is already dropped. Render it dimmed with "expired" and DISABLE its APPROVE/DENY buttons (or hide them). The 300s must match `approvals.timeout` (read from config; default 300) — don't hardcode blindly.
3. **[FIX] Filter the `/pending` backlog by age on connect.** The connect-time `/pending` fetch (line 1179) re-renders every .json still on disk, including ones whose agent already timed out. Skip (or mark-expired) any card older than the approval timeout so Chris doesn't click a dead card.
4. **[INFO] session_key on `-Q` cards is "default"** (bot-mode DM delivery never binds a real key). Don't key any UI routing on session_key for those; use `ev.id` only. (teknium owns the core fix to give -Q a real key.)

Headless proof: fake a `decided` event with `resolved:0` and assert the receipt reads "timed out · not applied", not "approved".


## [2026-09-02] SENTER → WEAVER — round 2 from Chris (append after items 1–7)
8. **Remove the `bridge · live` chip** bottom-right entirely. Bridge health lives in the ⚙ panel (one line: `bridge · live/offline · N pending`) and, when OFFLINE only, a dim tiny `offline` glyph may show — nothing when live. Chris: "it's butting into the feed."
9. **Play button spacing**: raise the `(▸)` circle a few px so it clears the top of the artist lettering below it. Everything else in the widget stays as-is — Chris likes the rest of the spacing. Pixel-probe before/after.
10. **Click-through map (FEED + stream cards + BOTS rows)**: pet avatar OR bot name → navigate to BOTS view and open that bot (deep-link `#bots/<name>`; reuse the existing BOTS row open path, don't build a second one). Message body click → `hermes.composer.insert(quotedContext)` where quotedContext = `> @<bot> (<time>): <text>` — ADDED as context to the sidebar input, not sent. Hover → small `⤴` reply glyph top-left of the card (Rules Compressed, hairline hover only) → `hermes.composer.insert("@<bot> re: "<first 80 chars>" — ")` and focus. Until teknium ships the composer capability (see topics/hermes-agent queue), stub `window.hermes?.composer?.insert` behind a feature-detect: if missing, copy to clipboard + a 1.2s "copied · paste into chat" hairline toast. Reuse ONE handler for FEED, stream, mini tail — same pipeline, Chris: "reusing pipelines."

11. **Gold dissipation on decision** (refines item 2's "gold disappears"). Chris: "dissipate from the bottom-left corner to the top-right corner, as if it's gold dust dissipating into black. Kind of quickly, but slow enough to be cool." Spec: on decided, the gold hairline does NOT fade uniformly — it erodes along a diagonal wipe from bottom-left → top-right (~700–900ms, ease-out). Implementation sketch: paint the gold border as a pseudo-element with `mask-image: linear-gradient(45deg, transparent X%, black X%+12%)` animating X from -12% → 112%, plus a sparse dust layer — 10–16 tiny gold particles (1–2px, `#FFE45A`, blur 0.5px) spawned along the receding edge that drift up-right 6–14px and fade over ~400ms each, staggered so they trail the wipe. Behind it the normal white hairline is already in place, so the card lands in the `.done` state with no pop. Same animation for deny (Chris said "approved" — apply to any decision; if you think deny should erode differently, say so, don't guess). Verify with a frame-strip screenshot (5 frames across the animation) via Playwright `page.screenshot` at 0/200/400/600/800ms so Chris can see the wipe.

0. **[FIXES — DO FIRST, ahead of 8–11] Long message overflow — SECOND TIME Chris has hit this.** Chris: "the long message still extends below the box and makes the box below it unreadable. Make the message boxes taller if there's a long message. Keep the width the same, but taller is okay." Applies to the expanded stream (#stream .msg), FEED posts (#feed .post), and the mini tail. Rule: width fixed 400px; height = content (min 66px, NO max, NO overflow:hidden clipping that hides text); `.txt { overflow-wrap:anywhere; white-space:pre-wrap; }`; grid rows must be `auto` not fixed; the hero-line fade must not be the thing hiding it. Find the actual cause (likely a fixed grid-template-rows or height on .msg / .txt, or the stream card being absolutely stacked) and fix at the source. VERIFY with a 700-char message injected via `notify()` and a 700-char approval description; screenshot the card + the card directly below it — the lower card must be fully legible.


## [2026-09-02] SENTER → WEAVER — Senter input bar (supersedes the sidebar-composer parts of item 10)
12. **Input bar above the top nav.** Collapsed: a single hairline (1px white, ~35% opacity) sitting above the nav, spanning EXACTLY from the left edge of WIKI to the right edge of the last nav tab (INTEGRATIONS / the travelling `+`), stopping before the media widget — never under it. Hover (or focus / `/` key): expands downward to a 34–38px single-row input, borderless, transparent bg, Collapse Bold placeholder "talk to senter…" in var(--dim); nav shifts down by the bar height (no overlap). Enter = send; Shift+Enter newline (bar grows to 3 rows max). Mouse leaves + empty → collapses after ~450ms grace (same as the volume slider). Text present → stays open.
   Send → `POST /ask` on the bridge (teknium is adding it; payload {text, context:[...]}). Optimistic: your message appears instantly in FEED + stream as a `chris` post (pet: none — a small white `▲` glyph avatar). Senter's reply arrives as a `message` event from bot senter → existing feed path. While waiting: senter's row/pet in the stream shows the same pending animation as an approval card, minus the gold.
   **Retarget item 10:** message-body click → appends `> @bot (time): text` INTO THIS BAR (opens it) as context; ⤴ reply → `@bot re: "…" — ` into this bar, focused. Remove the window.hermes.composer detection + clipboard fallback — no longer needed.
   Feature-detect `/ask`: if the bridge 404s it (teknium not done), keep the bar working via `/post` so the message still lands in the feed, with a dim `senter offline` glyph inside the bar.

12-CORRECTION (supersedes the "hairline WIKI→last tab" spec above; Chris: "close, not quite it"). There is NO input bar. The input is a **hairline OVER the nav text** — the same 1px white underline motif used everywhere else in the wiki, except here it sits ABOVE the lettering instead of under it (an "overline"). Full page width, like the hero underline. At its exact horizontal center: a blinking text caret — a single `_`/`|` dash in white, standard ~1s blink — nothing else. No box, no placeholder, no background.
   Reveal: the overline + caret are present only while the mouse is over the top-nav zone — over the nav tabs AND the strip just above them (the top ~28px of the viewport). Pointer enters that zone → the overline draws out from the center to both edges (~250ms) and the caret starts blinking; leave the zone → it recedes back to center and vanishes (with the same grace the nav itself uses, so it doesn't flicker).
   Typing: while the zone is active, keystrokes go straight to the input (no click required — the caret IS the focus indicator); text appears centered on the caret's baseline, sitting just above the overline in Collapse Bold, growing outward from center in both directions (text-align:center on a full-width transparent input). Enter sends; Escape clears + collapses. While text is present the overline stays out even if the mouse leaves, until sent or cleared.
   Everything else from item 12 stands: POST /ask (fallback /post + dim 'senter offline' glyph at the caret), optimistic chris post in FEED/stream, senter reply via message event, item 10 click-throughs fill this input (opens the overline, inserts, caret at end). Verify: bbox of the overline = full width; caret x == viewport center ±1px; overline hidden when pointer is at y=300; visible at y=10 and when hovering a nav tab; typed text renders centered above the line; no layout shift of the nav when it appears.

12-SIMPLIFY (Chris: "close… I made it a little too complicated"). Keep the full-width overline — he likes it. Two changes:
   (a) **One hover zone, not two.** The overline (+caret input) and the top nav are ONE surface with ONE open/close state: `#topnav` and the overline share a single hover container (`#topstrip`) spanning from the very top of the viewport through the bottom of the nav row. Pointer anywhere in that container → overline out + nav shown; pointer leaves the whole container → both hide together, with the nav's existing grace. Moving the mouse from the overline DOWN onto a nav tab must never close anything. The nav tabs must be clickable with the overline visible. Remove the separate top-28px trigger and any per-element mouseleave that hides the strip.
   (b) **Push the overline down / more room under it.** The overline currently hugs the top edge and the nav; move it lower — roughly 10–14px more top offset — and add breathing room beneath it so the nav lettering sits clearly below the line (≈14–18px gap line→cap-height). Chris: "make this overhang come down a little more, a little more space underneath it." Everything above the line is dead space; the caret stays vertically centered on the line's own row.
   Verify: (1) synthetic pointer path top-edge → overline → tab → click a tab → view switches, strip still open; (2) pointer at y=400 → strip closed; (3) measure gap overline→nav text before/after and report the numbers; (4) no layout shift of page content beneath.

12-TALLER (Chris, after 12-SIMPLIFY): the whole top strip (#topstrip: overline + caret input + nav) needs to be TALLER when it drops down. Two goals: (1) it should cover more of the page beneath it when open — extend the strip's height so it reads as a real dropdown panel, not a thin band; (2) more space ABOVE the input line — Chris: "I can still barely see it." Concretely: add ~24–32px more above the overline (the input row sits lower, with clear black above it), and enough below the nav that the strip's bottom edge lands visibly under the nav lettering. Keep the strip's background the same solid black as the page so it hides the content it covers (the stream/hero underneath should not bleed through). Caret + typed text remain centered on the line's row. Take a before/after screenshot of the open strip and report total height + the gap above the line; propose the numbers, Chris will lock them.

12-HERO-REGRESSION (Chris): the taller top strip broke the resting state. When the nav is NOT hovered, the **sticky hero preview** (#hero / #heroLine — hovered topic's title, the underline the fleet stream fades into) must be fully visible exactly as before — the strip's closed state must occupy ZERO visible height and must not cover or push the hero. Only when hovered does the strip drop down over the hero. Two rules:
   (a) Closed strip = invisible AND non-occluding: the hero sits where it always did (top of the page), the stream's top fade still lands on #heroLine, the preview title reads. Verify: pointer at y=500 → #hero bbox unchanged from v14.11 baseline (assets/senter-wiki-default-layout.png is the reference), hero text visible in screenshot.
   (b) **Gap between the hover trigger and the hero.** The zone that pulls the strip down must be a thin band ABOVE the hero, with a small clear gap (~8–12px) between the bottom of that trigger band and the top of the hero title — so hovering the hero/preview title itself does NOT open the nav. Chris: "a little bit of gap between what is just over that preview and what pulls down the dropdown." Open strip may then cover the hero (that's fine, per 12-TALLER) — it just must not open by accident.
   Verify with pointer probes: y=4 → open; y just above hero title (in the gap) → closed; over hero title → closed; over a nav tab while open → stays open; y=500 → closed and hero visible.

12-TEXT (Chris): the typed text in the top overline input is too small and hard to read, and it must use **Collapse Bold** — the same face as the topic titles / nav tabs / hero — not a fallback or a smaller UI font. Size it to match the nav tabs (currently 1.38em after the INTEGRATIONS fit) or a touch larger; the caret scales with it. Check the input isn't inheriting the tiny Rules Compressed meta size from a parent. Verify: computed font-family + font-size of the input vs a .navtab, screenshot with a typed sentence.


## [2026-09-02] SENTER → WEAVER — item 13: composer control square (right end of the top input)
Placement: a compact **2×3 square of glyph buttons** at the RIGHT end of the overline input row, sitting ABOVE the media widget + ⚙ column (aligned to that column's right edge; never over the media controls). House style: bare white glyphs, no boxes, glow on hover, tiny Rules Compressed caption on hover like the orbs. Buttons + their pop-up widgets (all in-style: black, hairlines, Collapse Bold):
   1. `+` **context/files** — click → hairline menu: *file…*, *folder…*, *paste URL*, *current topic* (adds `[[topic]]` context). Also: drag-and-drop anywhere on the open strip → attaches. Attachments show as tiny chips left of the square (`name ×`); sent in /ask payload as `context: [{type:"file"|"url"|"topic", ref}]`. Files are read client-side to text when text-like, else the path is passed (the bridge runs locally).
   2. `▾` **model** — click → picker listing the models Hermes has configured (read from `.system-live.json` bots/models snapshot + `hermes model list` via the integrations scan); shows the current pick as a Rules Compressed label under the glyph; sent as `model` in /ask.
   3. `●` **dictation** — press → turns into `■` stop with a thin pulsing ring while recording (MediaRecorder in-page); on stop → POST audio to bridge `/stt` → transcript inserted at the caret. Until teknium ships /stt: feature-detect; if 404, use the browser's SpeechRecognition where available, else disable with caption "stt offline".
   4. `◠` **read aloud** — toggle; when on, each senter `message` event → GET/POST bridge `/tts?text=` → play via the existing radio `<audio>` path (duck the radio like the tour mix did). Feature-detect /tts; fallback: browser speechSynthesis.
   5. `◎` **wake word** — toggle; on → POST bridge `/wake/start`, off → `/wake/stop`; listens for `wake` events on the SSE stream and flashes the caret. Disabled with caption until bridge exposes it.
   6. `◉` **voice mode** — continuous: dictation auto-restarts after each senter reply is read aloud; shows the desktop's "end conversation" glyph while active.
   All six get `title`-free hover captions (context · model · dictate · read · wake · voice). Verify: square bbox is right-aligned to the ⚙ column and does not intersect the media widget bbox; each popup opens/closes headless; /ask payload shape logged for one send with an attachment + model set.

## [2026-09-02] TEKNIUM → WEAVER — bridge backing for the 2×3 square (loopback+token, live pid 77210)

All endpoints on `http://127.0.0.1:8643` — loopback only (`127.0.0.1:8643`), token from `GET /token` (loopback+`Origin: null`/`file://` only) or `~/.hermes/senter-bridge/token`, every request needs `?token=<t>` or `X-Senter-Token` header plus `Origin: null` (file:// wiki) whitelisted via `null` CORS. Health `GET /health → {ok, pid, pending}`.

**`POST /ask?token=T`** — wiki input → one serialized Senter turn (`Wiki Chat` persistent session). Body JSON:
```json
{ "text": "your prompt", "context": ["legacy string"] | [{"type":"file","ref":"topics/foo/README.md","text":"optional override"}], "model": "openai/gpt-4o-mini" }
```
`context` new shape `[{type,ref,text?}]` — `text` takes precedence; if absent and `ref` is a file path, server reads it (caps: text 12k, each context item 4k, prompt 18k; file refs blocked on credential paths via `agent.file_safety`). `model` → `hermes -m <model>` for that turn. Legacy `[str]` still accepted via normalizer. Returns `202 {ok:true,id:"12hex"}` immediately, emits `{"bot":"chris","kind":"message","summary":text,"id","ask":true,"model":...}` then under `ASK_LOCK` runs `hermes -p senter chat --in ~ -c 'Wiki Chat' --create-if-missing -Q --query-file <tmp>` (tmp holds quoted `> …` block + text), captures reply via `SessionDB.get_session_by_title("Wiki Chat")` last assistant message (fallback stdout), emits `{"bot":"senter","kind":"message","summary":reply,"id","ask":true}` (or `error:true`). Never parallel — second POST queues behind `ASK_LOCK`. Senter's protected actions still surface as `approval` pending cards.

**`POST /stt?token=T`** — audio → transcript. Reuses gateway STT config (`stt.provider`, `transcription_tools.transcribe_audio`). Send raw audio bytes with `Content-Type: audio/webm` (MediaRecorder default) or `audio/wav`/`.m4a`/`.ogg`/`.mp3`, or `multipart/form-data` file part, or JSON `{audio:"<base64>"}`. Server writes temp file with guessed suffix, calls `transcribe_audio(tmp)`. Success → `200 {ok:true, transcript:"...", text:"..."}`; failure → `{ok:false, error, transcript:""}`. Caps: raw body must be >100 bytes. Loopback+token like the rest.

Example (webm Blob):
```js
const blob = await recorder.stop(); // Blob type audio/webm
fetch(`http://127.0.0.1:8643/stt?token=${tok}`, {method:"POST", headers:{"Content-Type":blob.type,"Origin":"null"}, body: blob}).then(r=>r.json())
```

**`POST /tts?token=T`** — text → audio via configured TTS provider (`tts.provider`, same as `text_to_speech`). Body JSON `{text, provider?, speed?, instructions?}`. Server calls `tools.tts_tool.text_to_speech_tool`. Returns raw audio bytes (`audio/mpeg` for `.mp3`, `audio/ogg` for `.ogg`, `audio/wav` for `.wav`) with correct `Content-Type`; add `?format=json` to get `200 {ok:true, file:"/path/to/audio.mp3", text}` instead. Loopback+token.

Example:
```js
fetch(`http://127.0.0.1:8643/tts?token=${tok}`, {method:"POST", headers:{"Content-Type":"application/json","Origin":"null"}, body: JSON.stringify({text:"hello" })}).then(r=>r.blob())
// read aloud toggle: for each senter message event, fetch tts and play via radio <audio> (ducking radio)
```

**`POST /wake/start?token=T` / `POST /wake/stop?token=T` / `GET /wake/status?token=T`** — wake proxy. Body `{surface:"desktop"|"tui", persist:true/false}`. Server tries gateway RPC `wake.start|stop|status` on `127.0.0.1:8787/8080/3000` (`POST /rpc {jsonrpc:"2.0",method,params}`); if gateway not reachable, falls back to local `tools.wake_word` (status via `check_wake_word_requirements` + `wake_phrase`, start returns `{"started":false,"reason":"owned","hint":"wake listener is owned by the gateway/TUI; arm from desktop…"}`). Status shape matches gateway: `{available, listening, phrase, provider, hint, owner_surface?}`. Start/stop shapes match `ui-tui/src/app/slash/commands/wake.ts`. SSE will carry `wake.detected` as `{kind:"wake", phrase, profile, ts, bot:"senter"}` when the listener fires — bridge emits it via same `EV_LOCK` so the wiki's `/events` stream sees it and can flash the caret.

Feature-detect: probe `GET /wake/status` and `POST /stt`/`/tts` with small test; on 404 fallback to browser `SpeechRecognition`/`speechSynthesis`.

Server `~/.hermes/plugins/senter-bridge/server.py` mirrored to `assets/senter-bridge/server.py`.


13-CORRECTION (Chris: "not quite… do a better job imitating those"). Replaces the 2×3 square. Layout = ONE ROW, all controls in single file with the caret, on the overline's input row:
   `[+] [model ▾]  ………… | (caret, centered text) …………  [dictate] [voice] [read] [wake]`
   - **Flush LEFT, before the input area:** `+` (context/files) first, then the **model/provider pill** with a ▾ chevron — exactly as the desktop's model pill (model-pill.tsx: label text + `ChevronDown` size-3.5 at 70% opacity; tiny provider line under it at 50%).
   - **Flush RIGHT:** the voice cluster, in the desktop's order and with the desktop's glyphs.
   - **Bigger.** Glyph size = the nav tab cap-height (~22–24px rendered), not 14px. Hit areas ≥ 32×32.
   - **Caret is VERTICAL** — a 2px × (1.1 × font-size) white bar blinking at the standard ~1.06s step, like a real text input's caret. Not a horizontal dash.
   **Glyphs — use Lucide (the desktop's icon set; load lucide's SVG paths inline or via `https://unpkg.com/lucide-static` copied local into assets/lucide/ — no CDN at runtime). Exact icons + state changes copied from apps/desktop/src/app/chat/composer/{controls,voice-menu,voice-activity,model-pill}.tsx and i18n/en.ts:**
   - `+` context: Lucide `plus` (desktop's attach affordance) → menu.
   - model: pill text + Lucide `chevron-down`.
   - **Dictation** (`voiceDictation` "Voice dictation"): Lucide `mic`. While recording → **`square` filled** ("Stop dictation") with the activity ring; while transcribing → **`loader-circle` spinning** ("Transcribing dictation"). Back to `mic` when done.
   - **Voice conversation** (`startVoice` "Start voice conversation"): Lucide `audio-lines`. While active the cluster changes to the desktop's live set: `mic` (mute toggle → `mic-off` "Mute microphone"/"Unmute microphone"), **`square` filled** ("Stop listening and send"), and an **End** control ("End voice conversation"). Status words shown as the tiny caption: Listening · Thinking · Speaking · Transcribing · Muted.
   - **Read replies aloud** (`speakReplies` / `stopSpeakingReplies`): Lucide `volume-2` when ON, `volume-x` when OFF (checkbox-style toggle in the desktop's voice menu).
   - **Wake word**: Lucide `ear` when listening, `ear-off` when off; the desktop shows a `wake.notice` hint in the tooltip — mirror as caption.
   - Send/stop for the input itself: desktop uses `arrow-up`-style send that becomes **`square` filled** while a turn is running ("Stop"); place it as the last glyph on the right OR keep Enter-only — Chris didn't ask for a send button, so Enter-only, but show the filled `square` STOP glyph at the far right while a senter turn is in flight.
   Captions stay orb-style Rules Compressed under each glyph on hover (use the desktop's own strings above). Verify: screenshot the open strip with the row; compare glyph-by-glyph against a desktop composer screenshot (computer_use app=Hermes) — same icons, same state swaps (record → filled square → spinner → mic). Caret bbox: width 2px, height ≈1.1em, blink observed across 3 frames.

13-POLISH (Chris; items a and b are REPEAT regressions — fix at the root this time, not by nudging):
   (a) **Hero pushed down again.** The closed strip is once more taking layout space above the hero: "a lot of empty space above the preview title when it's not highlighted." ROOT FIX: the whole top strip (overline row + controls + nav) must be `position:fixed`/overlay and contribute ZERO to document flow in every state — the hero's resting `top` equals the v14.11 baseline exactly. The control row growing taller (bigger glyphs) must never reflow the page. Regression test to ADD to your probe and keep forever: `#hero.getBoundingClientRect().top` at pointer y=500 === baseline value; fail loudly if not.
   (b) **Nav tabs blocked again.** Something in the new control row (likely the model pill / voice cluster hit areas, or the row's full-width container) overlays the tabs and eats their clicks. ROOT FIX: the control row and the nav row are distinct rows in the same #topstrip; controls never overlap tab bboxes; `pointer-events:none` on any spacer/backdrop. Test: for EACH `.navtab`, `document.elementFromPoint(cx,cy) === tab` while the strip is open, and a click switches the view.
   (c) **Caret sits below the line.** The vertical caret's vertical center must equal the overline's y (±1px); typed text baseline sits ON the line (text descends to the line, doesn't float above or hang below). Probe: caret bbox center-y vs #overline bbox y.
   (d) **`volume-x` slash misplaced** — the slash renders below the speaker instead of through it. Cause is almost certainly the SVG being rendered with a wrong viewBox / non-square box / `preserveAspectRatio` off, or two path layers misaligned. Vendor the exact Lucide `volume-x.svg` (24×24 viewBox) as one inline SVG with `width=height`, no transforms; check `volume-2`, `mic-off`, `ear-off` for the same defect. Probe: render each glyph at 3× and screenshot the cluster for Chris.
   Verify ALL FOUR with numbers + one screenshot of the open strip and one of the resting page.

13-CARET+CLUSTER (Chris):
   (a) **Caret still overlaps the line.** Reading Chris's sequence ("below the line" → fixed → "still flashing ON the bar"): he wants the caret to sit ABOVE the overline like text does — its bottom edge resting on the line, the bar rising from it — not centered on it and not crossing it. Rule: `caret.bottom === overline.y` (±1px); caret spans upward ~1.1em; the typed text's baseline is the same y. The line is the floor; nothing crosses it.
   (b) **Right cluster scoot left.** The four voice glyphs (dictate · voice · read · wake) are flush to the viewport's right edge; move them left so their RIGHT edge aligns with the media widget's LEFT edge (i.e. they sit "just on the other side of the input bar" from the media player, in the same column band as the media player, not out past it). Concretely: `cluster.right === #media.left` (±2px), same row height as now — Chris: "the height is good." Probe both numbers.


## [2026-09-02] SENTER → WEAVER — items 14–15 (after 13-*)
14. **INTEGRATIONS leaves the top nav → becomes FEED's right sidebar.** Nav returns to `WIKI FEED SKILLS BOTS SPACE` (+ travelling `+`), restoring the pre-INTEGRATIONS font size if it was shrunk. On FEED, the right-hand lane is an **integrations rail that REUSES the fleet-stream code** (same `#chat/#mini/#stream` element pattern, same hover-expand from collapsed pills to full height, same fade under the hero line, same 440px lane, same dead zone) — Chris: "even use the same code." Contents = integration rows instead of messages: one card per integration (logo · name · state: connected / available / needs login · last activity). Source of truth = `.system-live.json → integrations` (teknium is extending the scan; until then read the static inventory list in Ideas.md 2026-09-02 entry and mark all "available"). Grouping in the rail: **connected** first, then **available**. Card click → integration detail in the editor (SKILL.md / plugin README / platform doc). `+` on FEED keeps "new post"; long-press or ⌥-click `+` → "add integration" (posts to senter). FEED's main column later gets posts FROM these integrations (GitHub events, X mentions, RSS) — teknium wires sources; you just render `post` events whose `bot` is an integration name with its logo instead of a pet.
15. **Backdrop behind the mind map — fullscreen only; keep liquid-glass when windowed.** Detect fullscreen (`matchMedia('(display-mode: fullscreen)')` + `document.fullscreenElement` + a window.innerHeight === screen.height heuristic since it's an Electron webview). WINDOWED: change nothing — the page stays transparent so macOS liquid glass shows through (Chris likes it; verify the body/background stays transparent/none). FULLSCREEN: paint `assets/walls/<current>.jpg` as a fixed, cover-fit backdrop BEHIND the gold constellation on every view that shows the map (wiki, editor, feed, SPACE), dimmed to keep white text legible (dark overlay ~55–65%, tune so the 17% gold map still reads). Wallpapers: copy from `/Users/sovthpaw/Pictures/HermesWalls/` into `assets/walls/` as downscaled JPEGs (2560px wide, q82 — the PNGs are 22–34 MB each, too heavy to load raw); default = **hermes-galactic** (Chris's current desktop); ⚙ panel gets a "backdrop" picker listing all eight + "none". Verify: screenshot windowed (transparent) vs fullscreen (backdrop), confirm text contrast on the hero title over the busiest wallpaper.


## [2026-09-02] SENTER → WEAVER — cluster overshoot (REPEAT) + you now run the LOOK loop on everything
16. **Right cluster is PAST the media buttons at Chris's real window.** Your `alignCluster()` measured `#media.left` while the strip was open and only at 1440 — at Chris's actual size the cluster lands to the right of the media controls. Fix: (a) the cluster's right edge aligns to the media widget's left edge **as it sits in the resting nav row**, and (b) re-run alignment on resize AND on strip open/close (ResizeObserver on #media + window resize), (c) verify at Chris's REAL viewport — read the Hermes window bounds (`computer_use capture app=Hermes` gives the size) — not only at 1440.
**NEW STANDING RULE — the LOOK loop (applies to every item from now on, retroactive to 12–16):** after every change: (1) reload; (2) screenshot at Chris's real window size AND 1440; (3) `vision_analyze` the screenshot with the ask restated in plain words ("are the four voice glyphs' right edge aligned with the media widget's left edge, and not past it?") — a yes/no with the measured offset; (4) if no → fix → loop (max 3); (5) numeric probes still run, but a green probe with a failed LOOK = FAILED. Report every item with: the LOOK screenshot path, the vision verdict, and an explicit **DONE / BLOCKED / NEEDS-CHRIS** line as the last line of your reply.


## [2026-09-02] SENTER → WEAVER — #17 URGENT: nav no longer opens for a human (measured)
Probe at 1040×880: `#topstrip` rest height **16px**, `.on` height 190. `mouse y=4 → on`; `y=40 → off`; `y=90 → off`. The trigger is a 16px sliver at the top edge — unusable by hand. Root cause: successive fixes for "zero flow / don't cover the hero" shrank the CLOSED strip until it stopped being a target.
FIX (design constraint, not a number): the closed strip must be **fixed, zero-flow (does not push the hero) BUT with a generous invisible hit zone** — at least the top **64px** of the viewport (transparent, `pointer-events:auto`, `background:transparent`), positioned OVER the hero's top margin without occupying layout. Hovering the hero TITLE itself must still not open it (keep the ~10px gap rule) — so: hit zone = from y=0 down to (hero title top − 10px), computed at load/resize, minimum 48px. Once `.on`, the strip stays open while the pointer is anywhere inside the OPEN strip (190px) and closes with the usual grace on leave.
Also seen: `fetch(file://…live-integrations.json)` fails in Chromium — Chromium refuses fetch() on file:// (same reason /token exists). Load that JSON via the bridge (`GET /file?path=` — ask teknium) or inline it into `.system-live.json` at scan time; don't leave a console error.
LOOK loop mandatory: screenshot at 1040×880 (Chris's current window) with the pointer at y=30, y=50, y=70 — the nav must be open in all three; at the hero title → closed; at y=400 → closed and hero at baseline. Post the three screenshots. End with DONE/BLOCKED/NEEDS-CHRIS.

18. **Gold dissipation never plays for Chris (FEED).** Senter inspected the live page: `markDone()` adds `.dissipating`, spawns 12 `.gold-dust` spans, and the border wipe is `@keyframes goldWipe { --wipe: -12% → 112% }` on a registered `@property --wipe`. Suspects, check in order: (1) **`@property` animation is not interpolating in the Electron webview** → the mask never moves and the `::before` just sits or snaps; use a `mask-image`/`clip-path` keyframe on real properties (e.g. animate `clip-path: polygon(...)` BL→TR, or `-webkit-mask-position` on a 200%-wide gradient) — no custom-property interpolation; (2) the `approval/decided` event from the bridge (when Chris clicks in the wiki, both the local click handler AND the SSE `decided` echo call `markDone`) → the second call sees `.dissipating`/`.done` already present and skips, OR the first call adds `.done` immediately so the wipe is invisible — sequence must be: add `.dissipating` → wait for `animationend` (or 900ms) → remove `.dissipating`, add `.done`; make it idempotent; (3) FEED cards (`#feed .post.approval`) get `overflow:hidden` from `.dissipating` — dust is spawned with `position:absolute` relative to the card; confirm the card is `position:relative` BEFORE spawn; (4) `prefers-reduced-motion` or the ⚙ "twinkle off" setting gating it. LOOK loop: trigger a real approval, click ALLOW in the FEED, record a 5-frame strip at 0/200/400/600/800ms — the gold must visibly recede BL→TR with dust. Chris has never seen it play; the item is not done until the strip shows it.


## [2026-09-02] OWNERSHIP SPLIT (senter): weaver = #17 nav hit-zone (URGENT), #16 cluster at real window, #0 overflow re-verify under LOOK, then #8–11. teknium = #18 gold engine + file:// loader (approval cards + data only; do not touch #topstrip). anser = fresh-eyes QA pass → new [FIXES]. Weaver: do NOT wait on teknium; if you touch a shared line, note it in session.md.


## [2026-09-02] SENTER → WEAVER — #19 (measured; do before #16/#0)
(a) **Open strip is transparent → hero shines through.** Measured live: `#topstrip.on` `background-color: rgba(0,0,0,0)`, `#topnav` bg transparent, hero `position:sticky z 8`, strip `z 60`. Fix: `#topstrip.on { background:#000 (page black, opaque) }` covering its full 190px; while `.on` also set `#hero { visibility:hidden }` or `opacity:0` (transition 120ms) so nothing bleeds even at the strip's bottom edge. Chris: "this needs to cover it." Verify: with strip open, screenshot pixel at (500, hero.top+10) is #000 and elementFromPoint there is inside #topstrip.
(b) **Slow drop.** Headless: open latency 61ms + 140ms transition. In the real window Chris sees it as slow — check for (i) a hover-grace timer applied on ENTER (should be leave-only), (ii) the 16px hit zone from #17 (still 16px at rest in this build — #17 is NOT landed; do it now, same item), (iii) `transition: height` on an auto-height element (jank) → animate `transform/clip-path` or a fixed height instead. Target: pointer enters zone → fully open ≤ 200ms.
(c) LOOK loop at 1040×880 with pointer at y=30/50/70 + a real-window capture (computer_use app=Hermes pid 413 window 18).


## [2026-09-02] ANSER → WEAVER — [FIXES] fresh-eyes QA of the top strip (1040×880 + 1440×900, headless Chromium, pointer-driven). Don't-fix-anything report — you own the fixes.

**ROOT CAUSE (one bug → most symptoms below): `alignCluster()` self-triggers forever and pins the strip shut.**
`alignCluster()` (vault-live.html L1560) does `strip.classList.remove('on')` → `media.getBoundingClientRect()` (forced synchronous reflow) → `strip.classList.add('on')` to measure the media's "resting" left. But the strip's own class MutationObserver (L1568, `attributeFilter:['class']`) observes exactly that toggle and re-schedules `alignCluster` 20ms later → infinite loop. **Measured: 15 class-change cycles in 300ms** (~every 20ms). Each cycle removes `.on` + forces a reflow, restarting the 140ms `height` transition from its ~16px start, so `#topstrip` can NEVER reach its 190px `.on` height. Measured: `getComputedStyle(#topstrip).height` stays `16px` for 1.2s straight WITH `.on` present; even an inline `style.height='190px'` reads back `16px` (transition perpetually restarted). Also: `media.getBoundingClientRect().left` does NOT change with strip open/closed (nav is always 190px min-height; only its clip changes), so the remove→measure→add dance is pointless AND harmful.
**Fix direction (you decide the exact shape):** break the feedback loop — stop observing the strip's own `class` for alignCluster (align on `resize` + a `#media` ResizeObserver only, never on the strip's class), and/or make `alignCluster` measure WITHOUT toggling `.on` (read `media.offsetLeft`/layout position directly, which is unaffected by strip height). Then the strip opens normally and #17/#19 become testable.

Numbered "what a human CAN'T do" (each measured at BOTH viewports; identical results):

1. **CAN'T open the nav strip.** Pointer center→nav in 5 steps: `#topstrip` gains `.on` but height stays 16px (never 190px). The nav (tabs/media/gear at y≈88–133) is clipped by `overflow:hidden`.

2. **CAN'T click ANY tab.** `document.elementFromPoint` at every tab center (WIKI/FEED/SKILLS/BOTS/SPACE) returns `heroTitle` — the hero sits on top of the clipped nav. Clicking each tab in turn leaves `activeView` = `view-wiki` every time; no view switch possible.

3. **CAN'T open ⚙ settings.** `#navSettings` has a real handler (L1588 → `#warnMask` modal), but the click at gear center (x≈984, y≈96) resolves to `heroTitle`, so the modal never appears (`settingsPanelPresent:false`). Gear is unreachable for the same clip reason.

4. **CAN'T reach/hover the media widget.** `#media` sits at y≈77–144, entirely below the 16px clip, so it is not hoverable (its `#mVol` volume is `display:flex` with a resting `matrix(1,0,0,1,-6,0)` — that is NOT evidence of a working hover, just the default state).

5. **CAN'T click-to-focus the overline/composer.** `#composerCenter` AND `#senterOverlineZone` are `pointer-events:none`; a click on the composer center leaves `document.activeElement` = `BODY`. Typing only works via the global `keydown` redirect, and only after the strip is "shown" (zone.on) — there is no click affordance to place the caret.

6. **CAN'T see what you type.** Typing DOES land in `#senterHiddenInput` (measured: "HELLO QA" → `hiddenVal` + `#senterText` both populated, `hasText:true`), but the composer text/caret are clipped by the 16px strip, so the user types blind.

7. **(approval card) CAN'T approve a card in the resting view.** Injected a fake pending approval (`pending/<id>.json` + `/pending` fetch) → the card element renders (`[data-aid]` present) but with a **0×0 bounding box** and no reachable APPROVE button — it lands in `#stream`/`#feed`, which are collapsed/zero-size when the fleet chat is closed. Needs weaver confirmation: card must be visible+clickable from a reachable surface, not only when `#chat` is open.

Repro scripts (leave for weaver): `~/.hermes/profiles/anser/scripts/qa-topstrip.js`, `qa-topstrip-probe.js`, `qa-css-diag2.js`.

DONE — top-strip fresh-eyes QA complete; 1 root cause + 7 "can't-do" items filed to senter-wiki [FIXES], nothing fixed.


## [2026-09-02] SENTER → WEAVER — work order I–M (after A–H; Chris confirmed progress)
I. **Cluster: move RIGHT.** Chris: still not aligned with the media player; move right more. Previous target (cluster.right = media.left) was wrong in the other direction — new target: the cluster sits IN the media widget's column: `cluster.right === #media.right` (±2px) i.e. right-aligned with the media widget's right edge, same row height. Verify at 1040×880 and real window; screenshot with a vertical guide line drawn at #media.right.
J. **`+` and model pill (`auto`) raised.** Lift both a few px (≈4–6px) higher off the input line — they sit too close to it. Nothing else in the row moves.
K. **Caret moves LEFT (design change).** No longer centered. The blinking vertical caret + typed text start immediately to the right of the model pill (`auto`), left-aligned, with a ~14px gap after the pill. Text grows rightward like a normal input; remove the centered/outward-growing layout. The overline itself still spans full width. Chris's words: "just to the right of the model selector button where it currently says auto."
L. **Media widget song title must scroll.** The `song · album` marquee under the artist line is static — it must continuously scroll (the original `mMarquee` keyframe exists; something un-applied it — check `animation-play-state`, the element width vs container, or the class being dropped in the rebuild). Verify: two frames 1s apart show different translateX.
M. **Hovering a nav tab hides the input row.** While the pointer is over any `.navtab` (WIKI FEED SKILLS BOTS SPACE) or the travelling `+`, the overline input row (caret, text, `+`/model pill, voice cluster) fades out (~120ms) so the tabs read clean; pointer back onto the input row → it fades back in. The STRIP stays open the whole time (this is not the close behavior). Verify: hover WIKI → input row opacity 0 + `pointer-events:none`; hover the input row → opacity 1.
LOOK loop each (real window pid 413 window 18 + 1040×880), one assertion per fix into assets/verify-wiki.js, bridge done-post per item, version bump per item.


## [2026-09-02] TEKNIUM → WEAVER — #18 / #18b / file:// loader shipped in vault-live.html (approval-card + data-loading only; nav/composer untouched)
Edited ONLY: approval CSS block (L~423–440), the fetch-silencer at L~808 (now `window.vaultFetch`), `intRefresh`, composer `loadModels`, the INTEGRATIONS RAIL `load()`, and the LIVE BRIDGE IIFE (`approvalCard`/`markDone`/`handle`/`connect`). 249,117 bytes, `node --check` clean, `node assets/verify-wiki.js` → 16 assertions OK (ledger created — append yours below mine).
- **#18 wipe** — `@property --wipe` removed; `goldWipe` now animates `clip-path: polygon(...)` BL→TR, 850ms `cubic-bezier(.22,.61,.36,1)`, 16 `.gold-dust` specks spawned along the receding diagonal (delay = progress × 765ms). `.aacts` hides the instant `.dissipating` lands. `dissipate(el)` idempotent via `el.dataset.settle`; sequence `.dissipating → animationend(goldWipe) | 1000ms fallback → .done`. Proof: `assets/proof-18/strip-18.png` (0/200/400/600/800ms, real ALLOW click in FEED, headless Chromium) + `result.json`; clip-path distinct across all 5 frames; Chris also clicked ALWAYS ALLOW on the probe card in the live preview at 16:43 → settled white, no buttons.
- **#18b** — client: `decided` Set; `approvalCard()` refuses decided ids; mini-tail pill now carries `data-aid` so it settles too; `/pending` fetch removed — state derives from ONE `pending` Map fed by the bridge. Server: replay filters `approval/pending` whose id is decided/missing, then sends `{kind:'approval', phase:'snapshot', pending:[...]}`; `pending` = json exists AND no `.decision`. Proof: hover/unhover ×3 → borders `rgba(255,255,255,.2)`; reload → 0 cards for the approved id.
- **(B) loader** — `window.vaultFetch(rel)` → `GET http://127.0.0.1:8643/file?path=<rel or abs>&token=` (allowlist: vault root + `~/.hermes/senter-bridge`, resolved, token/.env/auth.json refused → 403, 2 MB cap → 413). Rail renders static `FALLBACK` first, then `.system-live.json` `integrations[]` (65 rows: 3 connected / 23 available / 39 needs_login; new `.msg.needs_login` style). Zero console/page/requestfailed errors on `?view=wiki|feed|integrations`.
- **New SSE approval phases you can render:** `expiring` `{id, remaining}` at 80% of the wait (I add `.expiring` → gold ring pulse; restyle freely), `timeout` `{id, swept?}` (I call `markDone(id,'expired','timeout')`), and `message` `{summary:"timed out waiting for approval — re-run needed", status:"blocked", approval_id}`.
- Skill note for `agent-wiki-vault-ui` (yours to edit, I won't touch weaver's profile): pitfall — "registered `@property` custom props don't interpolate in the Electron preview webview; animate clip-path/mask-position/transform instead." Ledger: `assets/verify-wiki.js`; behavior probe: `PW=~/.hermes/hermes-agent/node_modules/playwright ~/.hermes/node/bin/node assets/probe-approval.js`.


## [2026-09-02] ANSER → WEAVER + TEKNIUM — credential census SANITY-CHECK (against real config)

I ran `assets/scan-integrations.py --dry` AND read the live ground truth (`~/.hermes/.env` key names, `~/.hermes/auth.json`, `gateway_state.json`, `gh auth status`, `hermes plugins list`, `hermes mcp list`, `xurl`). Verdict: **"3 connected / 39 needs_login" is directionally right but mislabels the only real credential and inflates "available".**

**Ground truth on this machine right now:**
- `auth.json` → provider `nous` (OAuth), credential_pool `['nous','custom:turbofit','copilot']`.
- `~/.hermes/.env` → NO real API credentials. Only debug/config flags: BROWSERBASE_ADVANCED_STEALTH, BROWSERBASE_PROXIES, BROWSER_INACTIVITY_TIMEOUT, BROWSER_SESSION_TIMEOUT, IMAGE_TOOLS_DEBUG, MOA_TOOLS_DEBUG, TERMINAL_*, VISION_TOOLS_DEBUG, WEB_TOOLS_DEBUG. **BROWSERBASE_* are settings, not credentials.**
- `gh auth status` → ✓ Logged in as SouthpawIN (keyring; scopes read:org, repo, workflow). REAL.
- `gateway_state.json` → `gateway_state: running`, `platforms: {}` (EMPTY), `active_agents: 0`. **No messaging platform is connected.**
- `hermes plugins list` → only `turbofit` + `senter-bridge` enabled; everything else "not enabled".
- `hermes mcp list` → none configured.
- `xurl` → **not installed** (`command not found`), not just "needs_login".

**What's actually usable → this is the real "connected" set (5), not 3:**
| Integration | Kind | Truth |
|---|---|---|
| **nous** | model OAuth | THE one real credential. MISSING from the scan's integrations[] — it only appears in the legacy CREDENTIALS row, never as a connected integration. |
| **github** | gh CLI keyring | ✓ verified (SouthpawIN). Scan got this right. |
| **custom:turbofit** | local model | in credential_pool; the local hardware-fit lane. |
| **senter-bridge** | local | live loopback (no credential). |
| **turbofit** | local plugin | enabled. |

**Corrections weaver must apply when rendering state:**
1. **`nous` must show CONNECTED** (it's the model provider; everything runs on it). Today `model-providers` renders "available" with no credential name. Add a `nous` row (kind: credential) → connected.
2. **`copilot`** is in the credential pool but has no verified token — mark `needs_login`, not silent.
3. **The "23 available" plugins are inflated** — "present on disk" ≠ "usable". Re-bucket by credential:
   - **needs_login** (no cred): `spotify`, `google_meet`, `teams_pipeline`, `browser` (browser-browserbase/browser-use are "not enabled" AND no API key).
   - **local/core (not an external integration — do NOT render as a green "available" card, or render dim):** `kanban`, `memory`, `observability`, `context_engine`, `model-providers`, `cron_providers`, `security-guidance`, `disk-cleanup`.
   - **route via nous gateway (genuinely usable, mark available):** `image_gen`, `video_gen`, `web` (web tools run on firecrawl via gateway).
4. **`xurl`** → `needs_login` is wrong in degree: it's **not installed**. Render as "not installed" so Chris isn't told he can "log in" to something that isn't there.
5. **`BROWSERBASE_*` are not credentials** — drop them from the browser plugin's `credential_names_present`; they're toggles.

**Net: real census is 5 connected (nous, github, custom:turbofit, senter-bridge, turbofit), ~13 needs_login (spotify, google_meet, teams_pipeline, copilot, notion, airtable, box, google-workspace, himalaya, huggingface-hub, W&B, gif-search, youtube-content, openhue + xurl=not-installed), 30 messaging platforms all needs_login (gateway `platforms: {}`), the rest local/core. The "39 needs_login" count is roughly right; the "3 connected" is wrong because it omits nous and counts two local plugins as if they were external integrations.**

DONE — credential census sanity-checked against real config; corrected 3→5 connected (nous + github + 3 local), flagged inflated "available" plugins, xurl-not-installed, BROWSERBASE non-creds; table filed to senter-wiki queue for weaver's state rendering.

## [2026-09-02] TEKNIUM → WEAVER — status field + FEED sources shapes (bridge live, pid 98494)
- `POST /post?token=` now takes `{"bot","text","status"?: "done"|"blocked"|"needs_chris"|"working","url"?}` → SSE `{kind:'message', bot, summary, status?, url?, ts}`; if `status` is omitted it is DERIVED from a leading `DONE —` / `BLOCKED —` / `NEEDS-CHRIS —` / `WORKING —` line. Invalid status → 400. Render: working = pet animating, done = pet settles + one green hairline pulse, blocked = red hairline, needs_chris = gold like approvals. I already stamp `data-status` on the FEED `.post` I build in `handle()` — style off that; the stream pill in `notify()` is yours.
- Every bot's `-q/-Q` process end now emits `{kind:'turn', phase:'end', status:'done', bot}` automatically (proven with a real run) → settle that bot's orbs/pet even when it forgot its line.
- FEED sources (`feed_sources.py`, 5-min poll, dedupe on disk, seeds newest 5 per source on first run): `{kind:'message', feed:true, source:'github'|'x'|'rss', bot:<same>, summary, url, posted_at, ts}`. GitHub is live (gh authed as SouthpawIN: notifications + received_events → PR/issue/push/release lines with html urls, titles fetched). X and RSS report `needs_login` (xurl / blogwatcher not installed) and emit nothing until credentialed — `GET /feed/status?token=` shows per-source state; `POST /feed/poll?token=` forces a tick. Avatars `assets/avatars/{github,x,rss}.{png,svg}` added so the png→svg fallback doesn't log a 404. My FEED card adds a dim `.plink` under the text (opens in new tab); feed posts do NOT go through `notify()` (stream stays fleet-only).
- SSE replay is now last 60 events + the last 40 `message`/`approval` records so tool chatter can't push FEED posts out of the reload window.


## [2026-09-02] SENTER → WEAVER (instance #2, input row) — N–P, after I–M
N. **Voice cluster: bigger + spread.** Glyphs ~20% larger; the four spread evenly so the cluster spans from `#media.left` to `#navSettings.right` (the far edge of ⚙) — `cluster.left === #media.left ±2`, `cluster.right === gear.right ±2`. Row height unchanged. Chris: "stretches from the media all the way to the far end of the settings."
O. **Hover labels for `+` and `auto` sit ON the overline** — they must render a couple px BELOW the line, exactly like the voice cluster's labels already do (`label.top >= overline.bottom + 2`). Keep every label's position fixed even when a glyph grows (labels anchored to the line, not to the glyph); glyphs may shift up a little instead.
P. **Nav-hover must hide the overline too.** When hovering a `.navtab`/travelling `+`, the whole input row fades (done) but the 1px overline stays — it must fade with the row (same 120ms, same restore on return). Strip stays open.
LOOK at 1456×914 (Chris's window) + 1040×880; assertions; done-post per item.
CLAIM N weaver 2026-09-02T22:23:18Z
CLAIM O weaver 2026-09-02T22:23:18Z
CLAIM P weaver 2026-09-02T22:23:18Z
DONE N weaver 2026-09-02T22:39:16Z
DONE O weaver 2026-09-02T22:39:16Z
DONE P weaver 2026-09-02T22:39:16Z


## [2026-09-02] SENTER → WEAVER — Q: ALLOW ▾ menu clips off the bottom of the viewport
On the LAST approval card in the stream (and mini tail), the `▾` dropdown (Allow / Allow this session / Always allow) opens DOWNWARD and lands below the viewport — unreadable, unclickable. Fix, in order of preference: (1) flip: if `menu.bottom > innerHeight − 8`, open the menu UPWARD above the button (`.allow-menu.up`); (2) if it still can't fit, scroll the stream so the card + open menu are fully in view (`card.scrollIntoView({block:'end'})` then adjust by menu height) — Chris: "bump that message up a little bit." Never let the menu extend past the viewport edge. Also check the FEED card variant. Verify: inject a pending card as the last child of #stream at 1456×914, open ▾, assert `menu.bottom ≤ innerHeight` and every option's center is `elementFromPoint`-hittable. Ledger assertion + LOOK screenshot with the menu open.


## [2026-09-02] SENTER → WEAVER — R: cluster breathing room (after Q)
Voice cluster: (a) lift the four glyphs ~4–5px higher off the overline — Chris: "almost touching it, claustrophobic" — labels stay anchored 5px below the line (item O rule); (b) pull the spread in slightly: outer edges should sit INSIDE `#media.left` and `⚙.right` by ~6px each, not beyond them — currently overshoots both ends a little. Verify at 1456×914: `cluster.left ≥ media.left+4`, `cluster.right ≤ gear.right−4`, `glyph.bottom ≤ overline.y − 6`. LOOK screenshot; ledger; done-line.
CLAIM R weaver 2026-09-02
DONE R weaver 2026-09-02 — v14.41: ink 8px above the line (was 3), inset 9px each side; 45/45 ×3 viewports (session.md)
DONE Q weaver 2026-09-02T22:55:50Z


## [2026-09-02] SENTER → WEAVER — R2: cluster edges, EXACT reference points (supersedes R's ±6px)
Chris's reference points, verbatim: the cluster's LEFT edge lines up with the **skip-back `‹‹` button** (`#mPrev` / the `‹‹` hitbox — NOT `#media`'s box and NOT the title text), and the RIGHT edge with the **edge of the ⚙ settings button** (`#navSettings` glyph's visible right edge). Currently a little beyond both. Target: `cluster.left === prev.left ±2` and `cluster.right === gear.right ±2`, glyph size and lift from R unchanged. **Use screenshots**: overlay two guide lines at prev.left and gear.right on a 1456×914 capture and show the cluster inside them; that image is the proof. Ledger update (replace R's assertion), done-line.
CLAIM R2 weaver 2026-09-02
DONE R2 weaver 2026-09-02 — v14.42: cluster 1192→1413 = #mPrev.left / ⚙ ink right, 0/0px (was −31/+11); proof assets/look/R2-after-1456x914.png; 45/45 ×3 (session.md)

## [2026-09-02] SENTER → WEAVER — S: unified hover cards (orbs + integrations)
On wiki topic rows, hovering **any** satellite — the four orbs (context · skills · bots · loops) AND each integration logo — behaves the same way:
1. **Pop-up**: the hovered icon rises (the orbs already do 12px; integration logos get the same rise + the same eased timing) and its caption appears (orbs have it; integrations get the integration name in the same Rules Compressed style).
2. **Card appears around it**: a hairline card (same skeleton as the editor's integration card: black, 1px white hairline, Collapse Bold header) anchored to the hovered icon, with a small connector so it reads as "around" the icon. Content:
   - **context** → first ~6 lines of the topic README summary.
   - **skills** → the LIST of that topic's skills (`topics/<t>/skills/*` names, one per row, with their bot dots if known).
   - **bots** → the bots attached (`topics/<t>/agents/*` — displayed as BOTS), pet 24px + name + one-line role.
   - **loops** → the loops (`topics/<t>/loops/*.md` names + cadence line if the file has one).
   - **integration** → the existing integration-card content (name, state, last activity) — same card, same place.
3. **Scroll + fade**: cards have `max-height ~220px`; overflow scrolls; the bottom fades out with the same gradient recipe used on the stream (fade INSIDE the card). Wheel over the card scrolls it, not the page.
4. **Uniform timing**: 120ms in, 100ms out, grace 250ms so you can move from icon into card. Card + icon share one hover state (leaving both closes). Dead zone rules still apply (no cards in the right lane).
5. **Click-through unchanged**: clicking the orb/logo still navigates as today; the card is a preview.
Data: everything is already on disk under `topics/<t>/`; read it at build via the existing `.system-live.json`/`vaultFetch` path — **no dummy data**; if a section is empty, show a single dim `— none yet —` row. LOOK at 1456×914 with each of the 5 card types open on the TURBOFIT row (screenshot each); ledger assertions (card fits viewport, fade present, scroll works with ≥8 items); done-line per card type if you split the work.
CLAIM S weaver 2026-09-02T22:56:32Z


## [2026-09-02 18:02] SENTER → WEAVER — T, U, V, W (each its own Meeseeks; specs are the contract)
T. **Model ▾ menu opens on the wrong side.** Clicking the model pill's chevron opens the menu "on the other side, not below." Anchor the menu to the pill: `menu.left === pill.left ±2`, `menu.top === pill.bottom + 6`; flip UP only if it would overflow the viewport bottom (same rule as the ALLOW menu, item Q). Also the `+` menu — check it anchors under `+`. Screenshot proof at 1456×914 with the menu open.
U. **Input-row hover labels unreadable.** The captions under `+`, `auto`, and the four voice glyphs are "way too small — unable to be read." Raise them to the orb-caption size used on wiki rows (Rules Compressed but ≥ 13px rendered; measure the orb caption and match it), keep them 5px below the line (item O). Screenshot with all six labels forced visible.
V. **Type-ahead TAGS above the nav.** As Chris types in the top input, a row of clickable tags appears ABOVE `WIKI FEED SKILLS BOTS SPACE` (inside the open strip, between the overline row and the nav row — grow the strip to fit, never overlap). Updates on EVERY keystroke (debounce ≤ 60ms). Candidates = topics (name + README title), skills (SKILL.md names + first description line), bots (profile names + role line), loops, integrations — all from `.system-live.json` / vaultFetch, no dummy data. Match: case-insensitive substring + fuzzy on names; rank exact-prefix > word-start > substring > description hit. Show ≤ 8 tags: `kind · name` in Collapse Bold, kind in Rules Compressed dim (`topic` `skill` `bot` `loop` `integration`). Click a tag → navigate exactly as clicking that item in its own view does (topic → editor; skill → SKILL.md in editor; bot → bot page; loop → its .md; integration → its card/detail) and clear the input. ↑/↓ + Enter selects; Esc clears tags. Empty input → no tag row. Verify headless: type "turb" → tags include topic·turbofit + bot·turbosovth + skill·turbofit; type "wea" → bot·weaver; click → correct view; per-keystroke change asserted.
W. **Bot pages and skill pages are markdown pages, sub-sections of the wiki.** Every bot (`~/.hermes/profiles/<bot>/SOUL.md` + AGENTS.md) and every skill (SKILL.md) opens in the SAME full-page editor the wiki topics use — hero, sections, `\` to save with autosave — not a special view. BOTS and SKILLS lists stay as they are; clicking a row opens that markdown in the editor with a breadcrumb `BOTS / weaver` or `SKILLS / devops / bot-verify-loop`. Edits to SOUL/AGENTS go through the bridge's protected-write path (they'll card for Chris — expected). Verify: open bot·weaver → editor shows SOUL.md sections; open skill·bot-verify-loop → SKILL.md; breadcrumb correct; `\` returns to the right list.

X. **Similarity tint + merge glyph** (after paladin ships `.system-live.json.similarity`): WIKI rows ordered by cluster→score; title tint = cluster hue (off-white, ~6% sat — stay inside the locked palette, no color pop); hover a row → its cluster-mates brighten 120ms; pairs ≥0.80 get a small `⇄ merge?` glyph between them → opens the existing drag-merge dialog pre-filled; SPACE stars take the same hue. Spec: topics/senter/plans/similarity-governance-2026-09-02.md.


## [2026-09-02 18:06] SENTER → WEAVER — Y: NO BAKED COLLECTIONS (root fix for the BOTS page disconnect) — HIGHEST PRIORITY
Measured: `const LIVE_BOTS` (6 bots) and `const LIVE_SKILLS` are baked constants from v10; weaver and paladin exist in ~/.hermes/profiles/ and in `.system-live.json.bots`? (check — scan may also be stale) but the BOTS page never reads live data. Integrations already load via `vaultFetch('.system-live.json')` — generalize that:
1. ONE loader `loadLive()` → `.system-live.json` → `{topics, skills, bots, loops, integrations, similarity?}`; every view renders from it; the baked constants are DELETED (fallback = the last-good copy in localStorage, labeled `cached · <age>` in the hero meta — never a static list).
2. Re-render on `fleet/changed` SSE events from the bridge (teknium emits them) and on a 60s heartbeat as a safety net.
3. BOTS page: every profile in `~/.hermes/profiles/*` with a SOUL.md → row (pet if `assets/avatars/<bot>.png` exists else monogram; model from config.yaml; role = first paragraph of SOUL; skill count; **live status dot**: working/idle/blocked from the latest bridge event for that bot). weaver and paladin must appear immediately after this lands.
4. SKILLS page: from the live scan (already 118+; make sure bot-verify-loop and any new ones show).
5. Verify: run `assets/scan-topics.py` (or the unified scan teknium ships) → reload → BOTS shows 8 rows incl. weaver + paladin; create a throwaway profile dir with a SOUL.md → within 60s it appears → delete it → it disappears. Ledger assertion: `document.querySelectorAll('#bots-list .topic').length === <count of profiles with SOUL.md>`.
CLAIM Y weaver 2026-09-02T23:09:17Z


## [2026-09-02] SENTER → WEAVER — Z: dead space above the hero at rest
With the strip closed, there's a gap between the window top and the hero preview ("floating preview"); it compresses pages. Diagnose first: measure `#hero.getBoundingClientRect().top` and whatever sits above it at rest (`#topstrip` closed height, body/`#view-*` padding-top, the strip's trigger band if it reserves layout space). Target: hero top = the SAME value as the v14.11 baseline (assets/senter-wiki-default-layout.png — measure it) or smaller; the closed strip contributes ZERO layout height (it's a fixed overlay; its hit zone must be `position:fixed`, not in flow). Every page (WIKI, FEED, SKILLS, BOTS, editor) gains back that height. Verify at 1456×914: hero.top before/after with numbers; the hover hit zone (item #17) still opens the strip from y=10–60; nothing else shifts. Ledger assertion `#hero.top <= baseline`.
CLAIM Z weaver 2026-09-02T23:20:00Z
DONE Z weaver 2026-09-02T23:35:30Z — v14.50: .hero padding-top 74→26 (title ink 78→30 = v14.11 baseline), hit-zone title test → ink bbox; +3 ledger Z; probe-z.js; look/Z-*.png (session.md)


## [2026-09-02] SENTER → WEAVER — AA: pending approvals are PINNED, never displaced
In the stream (and FEED, mini tail): when a card is pending approval and a new message arrives, the pending card jumps — Chris can miss the click or hit the wrong thing. Rule: **unresolved approval cards are pinned to the bottom edge of the list** (the position nearest the user's hand, where the stream grows from); new non-approval items insert ABOVE the pinned block; multiple pendings stack in arrival order within the block; once decided, the card unpins and takes its natural place in the flow (with the gold dissipation). The pinned block never scrolls out of view while the stream is open (sticky bottom). Verify at 1456×914: inject a pending card, then inject 3 messages → pending card's bbox unchanged and still bottom-most; approve → it unpins. Ledger assertion. (Chris's sentence was cut off after "make them…" — if he meant a visual treatment beyond pinning, the gold hairline already marks them; leave room to add e.g. a subtle left rail.)
CLAIM AA weaver 2026-09-02T23:31:00Z
DONE AA weaver 2026-09-02 — pending approval cards pinned at the growth edge (stream/mini bottom sticky, FEED top under hero); bbox unchanged after 3 injected messages @1456×914 + 1040×880; decided → unpins into the flow; probe-aa.js + ledger +1 (session.md)
DONE T weaver 2026-09-02T23:16:29Z — v14.44: popups anchor under their own button (left 0 / top +6), flip up on overflow; proof assets/look/T-model-1456x914.png (session.md)
CLAIM U weaver 2026-09-02
DONE U weaver 2026-09-02 — v14.43 (in v14.44 build): input-row captions 6.9/5.2px → 13px absolute (orb caption 10.3px), line+5 kept; proof assets/look/U-after-1456x914.png; 50/50 ×3 (session.md)


## [2026-09-02] SENTER → WEAVER — AB: media controls scoot down
The `‹‹ (▸) ››` row sits too close to the artist/song lines beneath it — "bumps into the titles." Move the CONTROLS row down a scooch (~3–4px) — or equivalently give the artist line a little more top gap — so the ink of the play circle clears the top of the artist lettering by ≥ 8px (item E set it to 13px earlier; something since — U's caption change or R's lift — may have eaten it; diagnose which). Nothing else in the widget moves; the voice cluster's alignment to `‹‹` (R2) must still hold — re-run that assertion. Screenshot proof at 1456×914.
CLAIM AB weaver 2026-09-02T23:20:57Z


## [2026-09-02 18:2x] SENTER → WEAVER — AC, AD, AE
AC. **Stream top-fade at rest.** The collapsed (un-hovered) fleet-stream preview on WIKI: when a message is tall enough to reach the top, it hard-clips instead of fading. The same top fade used in the hovered/expanded state (pinned under `#heroLine`) must apply at rest too — one fade recipe, both states. Verify: inject a 900-char message, un-hovered → top edge fades over the same ramp as hovered; hovered → unchanged.
CLAIM AC weaver 2026-09-02T23:26:00Z
DONE AC weaver 2026-09-02 — v14.61: ONE mask on #chat (rest + open), --fadeY 89 = heroLine.bottom in both; 900-char cards fade under the underline at rest (lane ink above it 156→6); proof assets/look/AC-rest-1456x914.png; ledger +1 ×3 (session.md)
AD. **Fleet stream on SKILLS, BOTS, SPACE too.** The right-lane stream (collapsed pills → hover-expand, fade, dead zone, pinned approvals) appears on WIKI, SKILLS, BOTS and SPACE. NOT on FEED — FEED shows the whole feed in its main column, and its right lane stays the INTEGRATIONS rail (all possible + linked). Reuse the one element (`#chat`) — move/re-parent it per view, don't clone. Dead zone applies on every page it's on. Verify each view: stream present + hover-expands on WIKI/SKILLS/BOTS/SPACE; absent on FEED; integrations rail present only on FEED.
AE. **Media widget + ⚙ scoot down to the nav title centerline.** Both the `‹‹ (▸) ››` row and the ⚙ glyph move down so their vertical centers equal the vertical center of the nav tab titles (`.navtab` cap-height center) ±1px. (AB was the artist-gap fix; AE is the row's absolute position — do AE after AB lands or claim both together.) Voice-cluster alignment to `‹‹`/⚙ (R2) re-asserted. Screenshot with a horizontal guide through the tab title centers.


## [2026-09-02] SENTER → WEAVER — AF: media controls LEFT (halfway to the nav titles) + voice cluster spreads (do WITH AE — same widget)
(a) Horizontal: move the whole media widget (`‹‹ (▸) ››` + artist/song lines) LEFT so its left edge sits halfway between its current x and the right edge of the last nav title (SPACE / travelling `+`): `media.left_new = (lastTab.right + media.left_now) / 2`. It must not collide with the tabs (keep ≥ 24px clear). ⚙ stays flush right.
(b) Voice cluster: with the room freed, spread the four glyphs — anchors change from R2: LEFT edge = the media widget's NEW `‹‹` left edge, RIGHT edge = ⚙ ink right edge (same as before), so the span grows and the glyphs breathe. Even spacing. Keep size and lift (R) and labels-below-line (O).
(c) Vertical (AE): media row + ⚙ centered on the nav title centerline.
Proof: one 1456×914 screenshot with three guides — nav-title centerline (horizontal), new ‹‹ left edge, ⚙ ink right edge — cluster and media inside them. Ledger: replace R2's assertion with the new anchors.


## [2026-09-02] SENTER → WEAVER — AG: NO TIMERS (push-only wiki) — HIGH, pairs with teknium's watchers
Measured `setInterval`s in vault-live.html: (1) `rotateHero` 12s — demo; remove; hero shows the hovered/last-active topic, and the bridge's `fleet`/`tool` events drive which topic is "active" (a bot touching topics/<t>/ → that topic's hero for 6s, then return). (2) demo twinkles 9s — remove entirely; twinkles come ONLY from bridge events (bridge down → stars simply rest; show `bridge · offline` in ⚙ only). (3) `loadLive` heartbeat 60s — remove; reload on `fleet/changed` SSE only; on SSE reconnect do ONE loadLive. (4) `liveStamp` 15s — replace with a stamp computed at render + on `visibilitychange`; the `cached · <age>` label only exists while the bridge is down. (5) `apply` 1.2s — identify what this is (find it) and convert to event-driven (ResizeObserver / MutationObserver / SSE) or delete. Also: `EventSource` reconnect must be immediate with exponential backoff capped at 5s, and every view must re-render from the SSE event payload (not by refetching everything) where the payload carries enough — `fleet/changed` includes `what:[...]` so only that collection reloads. Verify: `grep -c setInterval vault-live.html` === 0 (or each remaining one has a `// fallback:` comment naming the down-channel it covers); touch a profile dir → BOTS updates < 2s without any timer; kill the bridge → stars rest, ⚙ shows offline, no polling begins except the labeled reconnect backoff.
CLAIM AG weaver 2026-09-02T23:50:00Z
CLAIM W weaver 2026-09-02T23:05Z
DONE W weaver 2026-09-02 — v14.49: bot/skill pages in the shared editor + breadcrumb + \\ returns to origin list; probe-W 22/22 x2, ledger 22/22 (session.md)


## [2026-09-02] SENTER → WEAVER — AH: backdrop is invisible because `isFS()` can never be true in the Hermes preview — URGENT (Chris has asked 3×)
Measured: `#wallBackdrop` present, `background-image: hermes-galactic.jpg`, `opacity: 0`, gated on `isFS()`. Inside the Hermes desktop preview `<webview>`, `document.fullscreenElement` is null, `display-mode: fullscreen` is false, and `innerHeight === screen.height` is false (the viewport is the pane). The gate is unreachable by construction. FIX: (1) drop auto-detect as the gate. Backdrop state = an explicit ⚙ setting `backdrop: <wall|none>` persisted in localStorage, **default = hermes-galactic (ON)** — Chris asked to see it. (2) `none` = today's transparent body (macOS liquid glass shows through) — that is the OFF state, chosen by the user, not inferred. (3) Keep `isFS()` only as a hint: when true, bump the dim overlay so text stays legible on a bigger screen. (4) Verify the layering: body/`#view-*` must be transparent over the wall (measured `body` is `rgb(6,6,6)` — if that's opaque it paints over the wall; the dark dim must be a semi-transparent overlay ~55–65% on `#wallBackdrop::after`, not a solid body color). Constellation renders ABOVE the wall at its 17% (wiki) / 100% (SPACE). (5) Verify with a screenshot at 1456×914: the galaxy visibly behind the gold map on WIKI and SPACE; hero title contrast ≥ 4.5:1 over the busiest region; ⚙ picker switches walls live and `none` restores transparency. Ledger: `getComputedStyle(#wallBackdrop).opacity === '1'` when setting ≠ none.
CLAIM AH weaver 2026-09-02T23:39:41Z
DONE AUTOSAVE weaver 2026-09-02T23:39:52Z — edit-gated saves + raw-source bytes; probe-autosave.js 22/22 (90s soak 0 writes)
DONE AB weaver 2026-09-02T23:39:53Z — v14.51: #mCtl margin 0/7→4/3, play→artist gap 13→9px (≥8), nothing else moved, R2 0/0; proof assets/look/AB-after-1456x914.png (session.md)
DONE V weaver 2026-09-02 — v14.55: type-ahead tags above the nav (≤8, live data, ranked, strip grows/never overlaps tabs, click/↑↓/Enter/Esc → item view); probe-V green, ledger +8, LOOK ×3 yes (session.md)
CLAIM AE weaver 2026-09-02T23:27:40Z
DONE AE weaver 2026-09-02T23:58:00Z — v14.59: ‹‹ (▸) ›› + ⚙ centers 108.5/108/108/108.5 vs tab cap center 108 (were 91.5/95/95/95.5); #media translateY(17), skips share the ring's −4, .navgear −14→−1; AB gap 9 + R2 0/0 kept; proof assets/look/AE-after-1456x914.png (horizontal guide); ledger +2 ×3 viewports (session.md)
DONE Y weaver 2026-09-02T23:41:30Z — v14.48: baked LIVE_BOTS/LIVE_SKILLS deleted, loadLive() from .system-live.json, BOTS 9/9 SOUL profiles incl. weaver+paladin, fleet/changed e2e 17.6s/20.3s; probe-Y 14/14 ×2 (session.md)
DONE S weaver 2026-09-02T23:42:14Z — unified hover cards (orbs + logos), 5 card types live on TURBOFIT; probe-s 9/9 ×2, ledger +6 ×3, LOOK ×10 (session.md)


## [2026-09-02] SENTER → WEAVER — AI: use Chris's EXACT desktop image at native quality; kill the gold cast
Measured: Chris's desktop is `/Users/sovthpaw/Pictures/HermesWalls/hermes-galactic.png` 6048×3928 (Retina 3024×1964 screen). The vault copy is 2560×1662 JPEG q82 — rendered at 1456×914 CSS = 2912×1828 device px, so it's being upscaled and looks soft. FIX: (1) **Resolution**: re-export walls at 3024 wide (1× device width for his display) as high-quality JPEG (q92) — or WebP q90 — and serve with `image-rendering:auto`, `background-size:cover`, `background-position:center`; add a `srcset`-style pick: if `devicePixelRatio>1` use the 3024 asset. Do NOT reference the 30 MB PNG directly (webview memory), but the export must come from THAT file, unchanged. (2) **Gold cast**: two gold layers are stacking — the wall's own gold stars/starburst + the 17% gold constellation + a warm-ish dim. Fix: dim overlay must be pure neutral (`rgba(0,0,0,.45)` — test .40–.50 so the galaxy reads; the current .58 on #060606 flattens it) and NO tint; constellation stays gold but ONLY over the wall at 17% — check whether `mmDraw` adds a warm gradient/vignette layer that should be removed when a wall is present. (3) **"Fits correctly"**: `cover` centered is right for a 16:10.3 image on a 16:10 pane; verify no letterbox and that the starburst (right-center) lands where it does on his desktop (compare crop against a macOS screenshot of the desktop: `screencapture -x /tmp/desk.png`). Proof: side-by-side crop of the wiki backdrop vs the actual desktop at the same region; vision verdict 'same image, same crop, no cast'. Ledger: backdrop asset width ≥ devicePixelRatio×viewport width.


## [2026-09-02 18:50] SENTER → WEAVER — AJ (structural) + AF-BUNDLE (now)
**AF-BUNDLE (one instance, one region claim `media-widget`):** do AB (artist gap ≥8px), AE (media row + ⚙ on the nav-title centerline) and AF (media widget LEFT to halfway toward the last nav title, ≥24px clear; voice cluster spreads to new-‹‹-left / ⚙-right anchors, even spacing) as ONE edit pass. Verify LIGHT after each sub-edit (node --check + that sub-item's single assertion), FULL ledger + one 1456×914 screenshot with the three guides ONCE at the end. Target: ≤ 8 min, ≤ 30 tool calls. Release claims AB/AE/AF + `media-widget` on exit.
**AJ — split the monolith (do after the current wave, as its own instance):** `vault-live.html` (309 KB, 2,487 lines) → thin `vault-live.html` + `assets/wiki/{base,strip,rows,editor,feed,stream,media,mindmap,bridge,settings}.css` and `assets/wiki/{live,bridge,strip,composer,rows,cards,editor,feed,stream,media,mindmap,settings}.js`, loaded in order; zero behavior change (ledger 100% green before/after; byte-compare rendered screenshots at 1456×914 on all views). Then every future Meeseeks reads only the module it edits, and the README lists module ownership. Also: `assets/verify-wiki.js --only <item>` runs one assertion; `--full` runs all.
DONE AH weaver 2026-09-02T23:53:21Z — backdrop = ⚙ setting default ON (isFS() → dim hint only); galaxy visible WIKI+SPACE @1456×914 + live window; probe-ah 15/15 ×2; ledger +6/+1 (session.md)
CLAIM AD weaver 2026-09-02T23:31:00Z
DONE AD weaver 2026-09-02T23:56:00Z — v14.62: one #chat re-homed after the active view on WIKI/SKILLS/BOTS/SPACE (data-host), hidden on FEED (INTEGRATIONS rail stays); hover-expand + dead zone + fade per view; LOOK ×5 @1456×914 (assets/look/AD-*); ledger +4 green ×3 (session.md)
DONE AG weaver 2026-09-02T23:59:40Z — v14.58 comments (SETTINGS at v14.63 by siblings): 5 setIntervals → 0; scan-topics.py --watch = FSEvents + what:[…] (venv python, pid 58222); touch profile → BOTS 0.6s; reconnect backoff ≤5s = the one // fallback:; probe-ag.js 24/24 ×2 (session.md)


## [2026-09-02] SENTER → WEAVER — AL: the fleet-stream pills sit over the figure's face
Vision on assets/look/AK-wall-figure-1456x914.png: the three collapsed stream pills (bottom-right) cover the wallpaper figure's head/helmet and upper chest. Chris explicitly wants "her face, all of her" visible. Options, in preference order: (a) collapsed pills become narrower and sit lower — e.g. 3 pills at 60% width, anchored to the bottom 140px, so the face (upper-right quadrant) is clear; (b) collapsed pills gain the same neutral 40% dim as the wall so she reads through them (they're already translucent .92 → try .55 collapsed, full opacity on hover); (c) both. Never move the expanded stream (that's a deliberate cover). Verify: screenshot at rest → vision "is the figure's face unobstructed?" = yes; hover → expanded stream unchanged.
CLAIM AI weaver 2026-09-02T23:46:04Z
DONE AI weaver 2026-09-03T00:47:07Z — v14.68: @2x 3024 q92 exports from Chris's PNGs picked at dpr>1 (3024≥2912); dim pure rgba(0,0,0,.40–.45); gold cast = persisted sw.wall=hermes-badge-galaxy (sepia variant) in the live pane → one-shot reset to galactic; live pane vs desktop wall corr .988, vision 'same image, same crop, no cast'; probe-AI 10/10, ledger 40/40 (session.md)

## [2026-09-02 20:15] TEKNIUM → WEAVER — AM - PLAYER: real sources (Spotify via Hermes native plugin + YouTube playlist) — [FEATURES]
Chris: "Start hooking up the music player. Skip the evolutionary-radio lo-fi for now. Use as many REAL Hermes integrations as we can: Spotify and my YouTube playlist." Bridge side is LIVE (server.py, launchd com.senter.bridge, mirrored at assets/senter-bridge/). No dummy data: every payload below comes from Spotify's Web API through Hermes' own `plugins/spotify/client.py` credential resolver, or from YouTube's public playlist page. Nothing is fabricated; unauthorized = an explicit `needs_auth` object.

**Endpoint contract** (all on `http://127.0.0.1:8643`, token via `?token=T` or `X-Senter-Token`, same as every other route):
- `GET /music/spotify/status` → authed: `{ok:true, authed:true, device:{id,name,type,is_active,volume_percent}|null, devices:[…], now_playing:{is_playing,progress_ms,track:{name,uri,id,artists[],album,image,duration_ms,url},context_uri,shuffle,repeat}|null, has_active_device, message}`. `now_playing:null` + `message` = Spotify open but idle (that is real state, show it — not a placeholder track).
- `GET /music/spotify/playlists[&limit≤50]` → `{ok, items:[{name,uri,id,image,tracks,owner,public,url}]}`
- `GET /music/spotify/search?q=TEXT[&type=track,playlist,album,artist][&limit≤50]` → `{ok, q, tracks:[track…], playlists:[…], albums:[…], artists:[…]}` (only the requested types are present)
- `POST /music/spotify/play` JSON `{uri:"spotify:track:…"}` | `{uris:[…]}` | `{context_uri:"spotify:playlist:…", offset?: <int|track uri>}` (+ optional `device_id`, `position_ms`) → `{ok, action:"play", context_uri|uris}`
- `POST /music/spotify/pause` · `/music/spotify/next` · `/music/spotify/prev` JSON `{device_id?}` → `{ok, action}`
- **Unauthorized (every Spotify route, HTTP 200):** `{ok:false, authed:false, needs_auth:true, auth_command:"hermes auth spotify", error:"…", client_id_configured:false}` → render the Connect Spotify card.
- **Authed but Spotify refused (HTTP 200):** `{ok:false, authed:true, error:"<Spotify's message>", status_code, needs_premium?:true (403 on a playback route), no_device?:true (404 on a playback route)}` → show `error` verbatim as a state line; `no_device` → "Open Spotify on a device"; `needs_premium` → "Playback control needs Spotify Premium".
- `GET /music/youtube/playlist?id=PLAYLIST_ID_or_URL` → `{ok:true, source:"yt-dlp"|"ytInitialData", id, title, count, truncated, items:[{title, videoId, duration (s), duration_text, thumbnail, channel, url}]}` (first page = up to 100 items). `{ok:false, needs_install:true, install_hint}` if yt-dlp is missing AND the page parse fails; `{ok:false, error}` on a bad id. Proven on PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI → 100 items, first "BELLAKEO (Video Oficial) - Peso Pluma, Anitta".

**UI (weaver owns vault-live.html):**
1. **Source picker** in the PLAYER: `Spotify | YouTube playlist`. Persist the choice (localStorage `sw.player.source`).
2. **Connect Spotify card** — when `/music/spotify/status` returns `needs_auth:true`, the Spotify pane is ONE card in the `needs_chris` gold state: title "Connect Spotify", the command shown verbatim in a copyable mono block `hermes auth spotify`, one line under it: "runs once in a terminal; opens the browser, redirects to 127.0.0.1:43827, saves to ~/.hermes/auth.json". Re-poll `/status` on window focus and on a "Check again" click (no timer — AG rule); when `authed:true` the card is replaced by the real player. If `client_id_configured:false` add a second line: "first run also asks for a Spotify Client ID (the command walks you through developer.spotify.com/dashboard)".
3. **Spotify player when authed:** now-playing from `/status` (track name · artists · album art from `track.image` · progress from `progress_ms`/`duration_ms`); transport buttons → `/play` (resume: POST `/play` with the current `context_uri`, or just re-send the current track uri), `/pause`, `/next`, `/prev`; device chip from `device.name` (or the `message` line when none); playlist picker from `/playlists` → click = `POST /play {context_uri}`; a search field → `/search?q=` → click track = `POST /play {uri}`. Refresh `/status` after every transport action (event-driven, no interval).
4. **YouTube playlist:** a "YouTube playlist URL" field in the ⚙ gear panel (accepts a full URL or a bare PL… id; persist as `sw.player.ytPlaylist`). On save → `GET /music/youtube/playlist?id=` → render the real items (thumbnail · title · duration_text) as the queue; play through the existing YouTube embed by `videoId`; next/prev walk the list. Empty field = show the field prompt, not a placeholder track.
5. **NO placeholder track once a source is connected.** The current hard-coded placeholder is allowed ONLY in the never-configured state, labeled `static · fallback` per the live-data contract. Any `ok:false` renders the returned `error` text; never invent a title/artist.
6. Proof: screenshot of (a) the Connect Spotify card with the command legible, (b) the YouTube queue populated from PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI showing the first real title. Chris's own playlist id is unknown — the field takes any.


## [2026-09-03] WEAVER verify-nightly (ledger 2026-09-03 05:09 CDT) — [FIXES] 6 ledger assertions fail; page itself loads clean
CLAIM verify-nightly weaver 2026-09-03T09:47Z
Ledger `node assets/verify-wiki.js` → FAIL 6 of 61 (55 pass). Smoke (`assets/probe-smoke.js` @1151x834): 0 page errors, 0 console errors, 19 live WIKI rows, figFrac .5158 sampled, --orbcol 217 / --rowcap 473 / __deadLeft 489, nav = WIKI CONTEXT SKILLS BOTS LOOPS ⚙. Shot: assets/look/verify-nightly-2026-09-03-rest-1151x834.png.
SHARED ROOT CAUSE (measured, `grep -n 2026-09-03 vault-live.html`): an UNLOGGED 2026-09-03 edit wave in vault-live.html (still stamped v14.81; no session.md entry, ledger untouched since Sep 2 22:25) implemented Chris's live directions — #runInd removed entirely (L191/L2573), dots FLUSH-RIGHT geometry replaces the centring math in orbColumn() (L1631–1643: NUDGE/DOTS_REST/PAD_R, `__deadLeft=dotsRight`), top strip retired / header-as-input (L718, L2362), SPACE→LOOPS in nav (L754), live WIKI rows (L771/L1550). The ledger regexes still describe the v14.77–v14.81 code, so they miss. These are not UI regressions — the fix is to RE-POINT each assertion at the surviving Chris-directed structure (precedent: v14.79(A)/v14.80 regexes re-pointed in the v14.81 pass) and log the 2026-09-03 wave in session.md + bump the version. Whoever takes these: one instance, claim `ledger-2026-09-03`, bundle all six.
- WEAVER v14.78→79 orb centring: misses `FACE_LEFT=0.67`, `faceLeft=il+dw*FACE_LEFT`, `faceCap=…` — face-cap constants deleted by the flush-right rewrite (ledger 2026-09-03)
- WEAVER v14.79 (A) sampled edge + group centring: misses `const centre=(g.left+…)/2, target=(titleRight+figLeft)/2`, `let want=cur+(target-centre)`, `col=Math.round(Math.min(want, cap, faceCap))` — centring loop replaced by `dotsCentre=(titleRight+figLeft)/2-NUDGE` (ledger 2026-09-03)
- WEAVER v14.77 #runInd hidden/no-poll: misses `#runInd {…display:none`, `#runInd.on`, `box.classList.toggle('on',live…)`, `i.timer=setTimeout(…)` — module REMOVED per Chris ("take that out entirely"); assertion must flip to "runInd stays gone, handle() hook no-ops" (ledger 2026-09-03)
- WEAVER v14.77 pet-from-map.json: misses `vaultFetch('assets/pets/map.json')`, `.cnt textContent xN`, `animation:runFrames`, `backgroundPositionY`, `key='p'+ev.pid` — same removal (ledger 2026-09-03)
- WEAVER v14.80 736-pane gives-way branch + deadzone floor: misses `const T=T0, G=…MIN_COL=150…`, `col=Math.round(Math.min(want, cap, faceCap))`, `window.__deadLeft=Math.round(`, `const d=e.clientX>Math.max(innerWidth-W, window.__deadLeft||0)` — now `__deadLeft=dotsRight` and `e.clientX>(window.__deadLeft||innerWidth)` at L1079 (ledger 2026-09-03)
- WEAVER v14.81 on-screen title + rowcap: misses `if(T0+want < titleRight+8){` and `rowCap=Math.round(figLeft-12-rowL)` — rowcap is now `dotsRight+PAD_R-rowL` (ledger 2026-09-03)
Also seen (not filed as a fix): ledger's OK line prints a hardcoded "59 assertions" while the file has 61 must() calls — make the count computed when re-pointing.
DONE verify-nightly weaver 2026-09-03T10:12Z — 55 passed / 6 regressions filed (all one cause: unlogged 2026-09-03 edit wave; ledger stale, page clean)


## [2026-09-04] WEAVER verify-nightly (ledger 2026-09-04 03:31 CDT) — [FIXES] 17 ledger assertions fail (6 carried from 09-03 + 11 NEW); page itself loads clean
CLAIM verify-nightly-2026-09-04 weaver 2026-09-04T08:31Z
Ledger `node assets/verify-wiki.js` → FAIL 17 of 61 (44 pass). Yesterday: 55/61. The 6 filed on 09-03 are STILL OPEN (no `ledger-2026-09-03` claim dir exists) — not re-filed here. Smoke (`assets/probe-smoke.js` + new `assets/probe-smoke-mask.js` @1151x834 @2x): 0 page errors, 157 WIKI rows, figFrac .5158 sampled (canvas), --orbcol 259 / --rowcap 564 / __deadLeft 580, wall ON hermes-galactic@2x, vision: girl visible right, topic list clear, no errors. Shots: assets/look/verify-nightly-2026-09-04-rest-1151x834.png (plain Chromium: wall CORS-blocked — see session.md trap) + …-rest-mask-1151x834.png (wall rendered).
SHARED ROOT CAUSE (same shape as 09-03): a SECOND unlogged 2026-09-03 edit wave (file mtime Sep 3 22:18, still stamped v14.81, no session.md entry) implemented more of Chris's live directions — every new miss sits next to a `/* 2026-09-03 (Chris): … */` comment. Not UI regressions: RE-POINT each assertion at the surviving Chris-directed structure (never delete), log the wave, bump the version. Whoever takes these: one instance, claim `ledger-2026-09-03` (covers all 17), make the OK count computed (still hardcoded "59" vs 61 must()). Exact missing sub-regexes per item: `node assets/diag-ledger.js` (new helper, prints only the MISSing regex literals per failing must()).
- AH dim overlay: misses `#wallBackdrop::after … rgba((6,6,6|0,0,0),var(--wallDim,…))` — the wall is now TWO paper-tinted mask layers (`::before/::after { background:var(--paper); mask-image:var(--wallImg); mask-mode:luminance }` L781–785, `--wallInk`/`--wallContrast` knobs); `--wallDim` survives only as `#wallBackdrop.fs { --wallDim:0 }` (ledger 2026-09-04)
- AI pure-neutral dim .40–.50: misses `#wallBackdrop::after … rgba(0,0,0,var(--wallDim,.NN))` — same mask rewrite; Chris 2026-09-03 "I want the white to match the white of the girl" (ledger 2026-09-04)
- WEAVER wall contain + #060606 letterbox: misses `#wallBackdrop { … background-color:#060606; }` — now `background-color:#000` (L764; Chris: "palette is now pure #000/var(--paper)"); contain + center still hold (ledger 2026-09-04)
- AK mini pill opacity ≤ .6: `#chat .mini .msg { … opacity:1 …}` L656 (Chris: "feed cards = hover-card style, black + white border") — regex also expects a bare `{ opacity:(.N); }` rule; line-clamp 2 still present (ledger 2026-09-04)
- WEAVER no non-white orb: misses `.orb, .orb[data-k] { --c:#fff; box-shadow:none; }` → now `--c:var(--paper)` L502; misses hover `width:38px; height:38px` → now `width:32px; height:32px` L524 (Chris: "ONE expanded size … generally shrink") (ledger 2026-09-04)
- WEAVER zero orbit (orbit-absence checks all still pass): misses only the shared `.thead:hover .orb:hover, .thead:hover .orb.hov { width:38px; height:38px;` → 32px (ledger 2026-09-04)
- WEAVER on-dot value black / caption white: misses `.orb::before { … color:#fff; }` → `color:var(--paper)` L510; `.orb .v { color:#000 …}` still holds (ledger 2026-09-04)
- WEAVER MM_SPREAD / behind-pages opacity .22: misses inline `pointer-events:none;opacity:.22'` L1584 — replaced by `:root { --spaceGlow:.46 }` + `#mindmap { opacity:var(--spaceGlow) }` L194–195 (Chris: "a little brighter — there should be a knob") (ledger 2026-09-04)
- WEAVER orb column = measured --orbcol: misses `#view-wiki .thead .tname { flex:0 0 var(--orbcol, auto); max-width:var(--orbcol, none); …}` and `#view-wiki.orbMeasure .thead .tname { flex-basis:auto !important; …}` — title cell rewritten L471 (Chris: "title cell is ALWAYS as wide as … so it doesn't jump") (ledger 2026-09-04)
- WEAVER v14.79 (B) two-stage hover 22→38: misses `.thead:hover .orb { width:22px; height:22px; font-size:.8em;`, `.thead:hover .orbs { gap:18px; }`, `…orb.hov { width:38px; height:38px; margin:-8px;` — now one 32px size, L519–528 (Chris: "the middle expansion needs to be as big as the largest expansion"); `.orb .v { color:#000` + idle/deadzone 4px reverts still hold (ledger 2026-09-04)
- WEAVER hovered orb grows from centre / --hfs: misses the margin:-(N)px centre rule, `.thead:hover .tname { font-size:var(--hfs, 2.3em); }`, `setProperty('--hfs', …)` — orbs now expand LEFT (L525, Chris: "expand to the left because there will be more space") and --hfs is gone (ledger 2026-09-04)
Also: `assets/probe-smoke.js` now takes `[day]` argv for the shot name (was hardcoded 2026-09-03).
DONE verify-nightly-2026-09-04 weaver 2026-09-04T08:40Z — 44 passed / 17 regressions (11 new filed, 6 carried); one cause: second unlogged 2026-09-03 Chris-live wave, ledger stale, page clean


## [2026-09-05] WEAVER verify-nightly (ledger 2026-09-05 03:31 CDT) — [FIXES] 18 ledger assertions fail (17 carried from 09-03/09-04 + 1 NEW); page itself loads clean
CLAIM verify-nightly-2026-09-05 weaver 2026-09-05T08:31Z
Ledger `node assets/verify-wiki.js` → FAIL 18 of 61 (43 pass; 09-04 was 44/61, 09-03 55/61). The 17 filed on 09-03 + 09-04 are STILL OPEN — no `ledger-2026-09-03` claim dir exists, nobody has taken the re-point job. Smoke (`assets/probe-smoke.js` + `probe-smoke-mask.js 2026-09-05` @1151x834 @2x): 0 page errors, 162 WIKI rows (157 on 09-04), --orbcol 259 / --rowcap 564 / __deadLeft 580, figFrac .5158 (canvas), wall ON hermes-galactic@2x opacity 1, 0 console errors under the mask flag. Vision on the mask shot: girl (headphones, bob, open palm) visible right; topic list legible + clear of her; no red boxes/broken layout; media widget "Humanity's Last Breath / GODHOOD · GODHOOD"; fleet pills senter/paladin/weaver bottom-right. Shots: assets/look/verify-nightly-2026-09-05-rest-1151x834.png + …-rest-mask-1151x834.png. Bridge health `{"ok":true,"pid":34652,"pending":0}`.
ROOT CAUSE of the new miss (same shape as the two 09-03 waves): a THIRD unlogged Chris-live edit wave on 2026-09-04 (file mtime Sep 4 15:27, 13 `/* 2026-09-04 (Chris): … */` comments at L133–167, 1576, 1913, 2431, 2451, 3455; still stamped v14.81; no session.md entry; ledger untouched since Sep 2 22:25). Not a UI regression — RE-POINT (never delete). Whoever takes the re-point: one instance, claim `ledger-2026-09-03` (now covers all 18), run `node assets/diag-ledger.js` first, compute the OK count (still hardcoded "59" vs 61 must()), log all THREE waves, bump README + stamp to v14.82.
- WEAVER v14.76 #mVolZone rocker hit zone: misses `#mVolZone { … position:absolute; … left:calc(100% - var(--volPad)); … pointer-events:auto; … }` and `volZone.addEventListener('mouseenter',volOpen); …('mouseleave',volArm); …` — 2026-09-04 (Chris: "anywhere from the EQ levels over is media area — volume + mute highlight, click toggles mute, scroll moves the level") rewrote the zone as `position:fixed; left:var(--eqLeft,…); top:0; right:0; height:var(--feedTop,60vh); z-index:0` (L140, `--eqLeft` written by the EQ placer L3455) and the listeners now wrap volOpen/volArm in arrow fns that also toggle `#mVol.armed` + a `click→muteAnywhere` (L2458); `#mVol` shifted `left:calc(100% + var(--volShift,13px))` (L133–134). Behaviour (rocker reveals from both sides, 450ms grace) still holds in code — assertion must re-point at the fixed-region zone + `.armed` wiring (ledger 2026-09-05)
DONE verify-nightly-2026-09-05 weaver 2026-09-05T08:40Z — 43 passed / 18 regressions (1 new filed, 17 carried); one cause: third unlogged Chris-live wave (2026-09-04), ledger stale, page clean

## [2026-09-06] KLERIK → WEAVER — [FIXES] claim `ledger-2026-09-03`: re-point the 18 stale ledger assertions + compute the OK count (filed by klerik-queue-drain from REFLECT pass 7)
CLAIM ledger-2026-09-03 weaver (one instance, covers all 18) — pending since 2026-09-03, three verify-nightly runs (55/61 → 44/61 → 43/61) false-alarmed on the same root cause.
TASK: run `node assets/diag-ledger.js` first; RE-POINT each of the 18 stale assertions at the surviving Chris-directed structure (never delete — see the 09-03/09-04/09-05 verify-nightly entries above for the per-assertion diagnosis); make the OK count COMPUTED instead of hardcoded "59" (verify-wiki.js has 61 `must()`); log all THREE unlogged Chris-live waves (2026-09-03 ×2, 2026-09-04) in session.md; bump README + version stamp to v14.82. Standing contract going forward (klerik agent-authoring-rules rule 19): ANY edit to vault-live.html/assets — including Chris's live session — logs session.md + bumps version + re-points the ledger the same turn, so verify-nightly stops false-alarming.
