# Senter Timeline (2026-08-27 → 2026-09-10)

Filed query: "what happened when?" across all raw items. Times are CDT where given. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## Pre-history
- **Undated (legacy)** — `SouthpawIN/senter` repo: Discord/Kanban triage orchestrator; fleet chizul/klerik/anser/kashik/crow/frieza/nous-girl ([[topics/senter/wiki/entities/senter-repo|senter repo]]).
- **2026-08-27** — earliest Senter/wiki session later exported into `topics/senter-wiki`.
- **2026-08-28** — the `senter` Linux workstation absorbed over SSH into topic `senter-consolidation` ([[topics/senter-wiki/wiki/concepts/remote-absorption-ssh|remote absorption]]).

## 2026-08-30 — coordinator day
- Senter's coordinator role assigned; [[topics/senter/wiki/decisions/2026-08-30-conversation-first-operating-model|conversation-first model]] locked; [[topics/senter-wiki/wiki/decisions/2026-08-30-standing-approval|standing approval]] granted.
- anser onboarded as redundancy gate; paladin briefed (working name "Stanzo" → "name it Paladin"); [[topics/senter-wiki/wiki/concepts/companion-bot-doctrine|companion-bot doctrine]] set; Sirvir → TurboSouth rename; turbosovth's TurboFit branch verified locally (43 failed / 559 passed).
- Channel failures proven: DM bodies dropped → vault as transport.

## 2026-08-31 — vault UI + self-model
- anser's config.yaml `***` crash fixed; [[topics/senter/wiki/concepts/selfmodel-layer|self-model layer]] built per anser's 5 rules.
- North star "Cursor for Obsidian"; `vault-live.html` chosen over `obsidian://`; style corrected three times → [[topics/senter-wiki/wiki/concepts/vault-ui-style-contract|white on black, list not cards]]; floating chat pattern approved.

## 2026-09-02 — the fleet grows up (one very long day)
- [[topics/senter/wiki/entities/senter-bridge|senter-bridge]] built; weaver spawned via klerik with cards approved FROM THE WIKI; paladin properly created by klerik; [[topics/senter-wiki/wiki/decisions/2026-09-02-senter-never-builds|Senter never builds]].
- Delivery failures → [[topics/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch daemon, then sentinel (v1→v3)]]; the five "slow again" rounds; `delegate_task` becomes primary.
- LOOK loop instituted; `wiki-look-verify` skill; [[topics/senter-wiki/wiki/entities/looker|looker]] created (REFLECT's first proposal); lessons 26–28 on crops and the [[topics/senter-wiki/wiki/concepts/preview-pane-viewport|preview pane 1151×834]].
- 63→19 topic merge (anser audit, paladin run); [[topics/senter-wiki/wiki/decisions/2026-09-02-governance-thresholds-calibrated|thresholds .35/.50 locked]]; CLAIM v2.
- Decisions: [[topics/senter-wiki/wiki/decisions/2026-09-02-fleet-decisions-as-wiki-cards|wiki cards]], [[topics/senter-wiki/wiki/decisions/2026-09-02-process-artifacts-are-the-product|process is the product]], [[topics/senter-wiki/wiki/decisions/2026-09-02-upstream-pr-policy|PR ledger]], "live live live — no timed loaders", no baked collections, rule 14 (96 approval cards).
- Backdrop saga (four "proven" rounds, stale stacked tabs); orb saga; gold-dust wipe; composer inventory from Lucide source; in-wiki input row replaces sidebar-composer route.

## 2026-09-04 — media player session (15:10–15:27)
- Volume rocker redesigned as two dot-capped segments with gap as slider; mute moved to inner side; hit zones by headphones/face geometry; z-order root cause fixed ([[topics/senter-wiki/wiki/concepts/media-player-controls|media player controls]]). ^[raw/inbox/2026-09-05-legacy-inbox.md]

## 2026-09-05 — the memory layer
- **16:22** "basically a memory layer for Hermes agent… all of it" → [[topics/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|decision]].
- **16:26** 7.4 MB exported into `senter-wiki`; SOULs/AGENTS/skill into `senter`; `build-index.py` → `.system/INDEX.md` for [[topics/senter/wiki/concepts/progressive-disclosure|progressive disclosure]]; the `agent-wiki-vault` skill carries "if it isn't in the wiki it isn't remembered."
- **16:29** Chris's full brief: [[topics/senter-wiki/wiki/concepts/cursor-for-markdown|Cursor for markdown]], rubber-duck sidebar, watcher, per-topic loops, flywheel, approvals to sidebar. **16:30** Hermes plays it back → [[topics/senter-wiki/wiki/concepts/five-part-architecture|five-part architecture]], `architecture.md`.
- **16:35** "per message, just like when you talk to cursor… live acting second brain" → [[topics/senter-wiki/wiki/decisions/2026-09-05-per-message-watcher|decision]]. **17:53** [[topics/senter-wiki/wiki/entities/watcher|watcher]] live.
- **18:16** [[topics/senter-wiki/wiki/decisions/2026-09-05-no-approvals-for-wiki-edits|no approval for wiki edits; bots trigger sooner]]; "I'm not seeing things move in the UI." **17:23** stage probe works; Spotify hookup next.
- **18:53** Hermes: senter agent "keeps pitching 'governance has no owner' — because the wiki (its memory) says the umbrella was deleted, when in fact it still runs. Fix the record, not the pitch" → [[topics/senter-wiki/wiki/entities/umbrella|umbrella]], [[topics/senter-wiki/wiki/concepts/fix-the-record-not-the-pitch|fix the record]]; `topic-governance-rehome` loop proposal superseded. Also: approvals APPLY ([[topics/senter-wiki/wiki/concepts/approval-apply-paths|apply paths]]).
- **18:58** Hermes: topic-agent prompt capped (1 bot / 2 loops / 1 research; zero infra pitches; `hermes:` lines are evidence) → [[topics/senter-wiki/wiki/concepts/topic-agent-pitch-caps|pitch caps]]; 13 self-referential proposals pruned, 2 approved; vault `AGENTS.md` written; `senter` SOUL = sidebar spec; canvas files current.
- **19:06** Chris: "If there's a way that we can get this entire flow down to just built in Hermes commands and markdown, that would be great" → [[topics/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]].
- **19:09** bridge `/file` allowlist had to be widened to serve `topics/*/wiki/*` so the wiki pane can open the pages the topic agents write.
- **19:12** "Proof: 1 block diffing, 2 green, 1 red"; inventory native vs custom — native: topic agent (`hermes chat -p senter`), loops (`hermes cron`), bots (`hermes profile`), wiki (`llm-wiki`); custom: watcher (no per-message hook), bridge (SSE + file proxy), TF-IDF cutter → [[topics/senter-wiki/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]].
- **19:23** Hermes: "Now the pre-prompting layer — each topic declares what belongs to it and how to think about it, and the cutter/agent read it" → `BRIEF.md` in every topic → [[topics/senter-wiki/wiki/concepts/topic-brief-pre-prompting|topic BRIEF pre-prompting]].
- **19:51** Hermes: dot bloom clamped, diffs update in-place with one-liner to feed, never auto-open editor or jam text → **misrouted to senter-wiki**.

## 2026-09-06 — runtime config crises
- **01:35** Chris delegates subagent: "Look for backups (Obsidian file recovery LevelDB, desktop caches, Hermes file checkpoints), NOT modify live file." Result: `vault-live.html` is **damaged** (missing `</style>`); best reconstruction from `/tmp/vault-live.before.html` (Sept 5 HTML) + `/tmp/vc139.js` (Sept 5). → **misrouted to senter-wiki**.
- **01:51** Chris: "my model keeps switching the step 3.7 flash And that keeps screwing out my project. If I pick a model from The model picker that it should stay with that model until it needs to fall back. Also, the TTS is failing."
- **02:20–02:35** Hermes diagnosis:
  - Model switching — `fallback_providers` has `turbofit` at top with `stepfun/step-3.7-flash:free` as first fallback; user's default `z-ai/glm-5.3-flash` not in chain. Fix: `z-ai/glm-5.3-flash` first; `auxiliary.compression` set explicit not `auto`.
  - TTS — `tts.provider: nous` → managed Nous gateway → 60s TTL JWT cache stale after credits added. Fix: `force_fresh=True` in `resolve_managed_tool_gateway` for TTS.
  - Vision — out of credits; `auxiliary.vision.provider: auto` picks free-tier retry model.
- **02:30** Confirmed: a main-model switch only takes effect in a new session; the current session stays on its current model.
- **22:43** YouTube raw re-route filed the same 02:30 JWT/`force_fresh=True` evidence and the 03:50 vision-fix confirmation into `raw/inbox/2026-09-06-from-youtube.md`; no new decisions, only reconfirmed state.
- **03:53–21:53** Deep TurboFit session (Maple MLX via stamsam fork, DFlash2 Metal build, MTPLX Mac profile, context compression timeouts at 262k on 32 GB M1, Maple OOMs, deepgrove-ai MLX, final: Unleashed main :11606 + Maple aux :11612 at 131k, 12.4 tok/s MTP). → **misrouted to turbofit**.
- **15:27** Hermes: "Wiki — done, reload and verify" — dot bloom, hover anchor, diff badges, row order, chat gutter, markdown rendering, boot crash fixed, vision switched to free StepFun. → **misrouted to senter-wiki**.

## 2026-09-07 — config + inference runtime
- **00:35** Anser surfaces: "Use Nous cloud fallback for contexts >65K". Treated as senter domain (Hermes config/fallback), not misrouted. ^[raw/inbox/2026-09-07-from-anser.md]
- **00:43** File `raw/inbox/2026-09-07-from-anser.md` ingested by watcher from anser reroute.
- **00:51** MTPLX warmup, generation, and memory-guard events observed. **Misrouted to turbofit** — local inference runtime, not senter. ^[raw/inbox/2026-09-07.md]
- **05:38–05:42** Three async delegation batch completion notices (`deleg_a5be7b3b`, `deleg_92f9c264`, `deleg_e76115bb`) arrive without task summaries. No new decision/entity/action extracted; filed as background process noise. ^[raw/inbox/2026-09-07.md]
- **05:51, 14:28** Repeated runtime messages state context compression timed out without dropping messages; evidence points to `auxiliary.compression` rather than a new vendor issue. ^[raw/inbox/2026-09-07-from-anser.md]
- **11:19** Port-conflict message from `memento` arrives ("Let me kill everything and restart fresh."). **Misrouted to memento.** ^[raw/inbox/2026-09-07-from-memento.md]
- **18:10** Hermes summarized **still-likely gaps** in the event-driven path: topic-agent trigger (still on timer), governance orphans (wiki said umbrella deleted), settings page/path issues (DOM-proving needed).
- **18:15** Chris reframed progressive disclosure as active watch/discovery loop → librarian concept. [[topics/senter/wiki/entities/librarian|librarian]] created for anser's proposed progressive discovery loop.
- **18:16** Hermes proposed: rename "context" to "wiki", update topic anatomy, add skill/bot/loop criteria.
- **18:23** Chris: "We need to be simultaneously understanding, using and building the center wiki and other projects with the center wiki."
- **18:27** Hermes: The UI work (09:21–09:49) is misrouted to senter-wiki — **antiscope violation**. The UI restoration is a senter-wiki task, not senter architecture.
- **18:28** Chris: "please continue until the UI is restored to what I want... finish both the front and back end for Senter Wiki entirely without needing my confirmation. Understand that we can undo choices you make easily, so do not be afraid to make them."
- **Ongoing 18:28–19:00** Hermes investigation of scan-topics.py, bridge server, topic-agent trigger path (09:22–09:56 local time next day).

## 2026-09-08 — autonomous completion authorized
- **08:45** Chris: "please continue until the UI is restored to what I want... finish both the front and back end for Senter Wiki entirely without needing my confirmation. Underestand that we can undo choices you make easily, so do not be afraid to make them."
- **08:46** Chris: "At the same time this center wiki still needs to be finished and in fact a few steps were even reverted so there are some things we even need to fix to get back to where we were. So we need to be simultaneously understanding, using and building the center wiki and other projects with the center wiki."
- **Standing approval extended**: Chris authorizes autonomous completion of Senter Wiki front and backend with standing approval (extend for this task).

### Open items (2026-09-08)
- **Senter Wiki UI restoration**: [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] needs restoration to Chris's exact preferences; verify live preview state
- **senter-wiki-bot topic folder**: Missing; needs creation with proper structure (wiki/, skills/, bots/, loops/) — see [[topics/senter/wiki/decisions/2026-09-08-senter-wiki-bot-topic-folder-missing|decision]]
- **Event-driven topic-agent trigger**: Landed state unclear; see [[topics/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|query]]
- **Context fallback threshold**: Requires `auxiliary.compression` pin before >65K threshold works; see [[topics/senter/wiki/decisions/2026-09-08-context-fallback-threshold|decision]]
- **Vault agents vs profile bots**: Clarify distinction between proposed vault specs and live profile bots; see [[topics/senter/wiki/concepts/vault-agents-vs-profile-bots|concept]]

^[raw/inbox/2026-09-07.md]

## 2026-09-09 — continuation authorized, pipeline verified
- **08:45** Chris: "Goal: please continue until the UI is restored to what I want (read through this session to find clues and specs), and finish both the front and back end for Senter Wiki entirely without needing my confirmation. Undertand that we can undo choices you make easily, so do not be afraid to make them. Continue working toward this goal." — re-activates the 2026-09-08 autonomous completion authorization without resetting fleet progress. See [[topics/senter/wiki/decisions/2026-09-09-autonomous-senter-wiki-completion-continuation|decision]].
- **13:15–13:17** Hermes: gh-sync repo structure identified — `agent-wiki` (main repo), `klerik`, `senter` as separate repos; working directory `~/Documents/Projects/Projects` relationship to agent-wiki unresolved (symlink/clone/worktree).
- **13:17** Hermes: "The Projects folder is NOT a git repository" — root cause of "updates keep failing"; git initialized to fix.
- **13:32** Hermes: "Live Data Pipeline Verified — Bridge server is running and healthy; `/system-live.json` is served correctly via `/file` endpoint; Data shows: 35 topics, 69 bots, 201 skills, 81 loops; senter-wiki topic now properly populated." See [[topics/senter/wiki/decisions/2026-09-09-live-data-pipeline-verification|decision]].

### Open items (carried from 2026-09-08 + new, still active)
- **Layout inspection (bot/sessions visibility)**: Chris 13:01 asks how running bots/sessions appear in the Hermes Desktop layout; Hermes 13:02 DOM inspection blocked ("browser isn't running"); 13:33 plans to inspect desktop preview + vault-live view-switching paths. Data contract verified (7bridge serves 69 bots); UI rendering in vault-live.html belongs to senter-wiki. See [[topics/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|decision]].
- **Senter Wiki UI restoration**: [[topics/senter/wiki/entities/senter-wiki-ui|Senter Wiki UI]] needs restoration to Chris's exact preferences; verify live preview state — now in active continuation
- **Event-driven topic-agent trigger**: Landed state unclear; see [[topics/senter/wiki/queries/event-driven-trigger-gaps-2026-09-08|query]]
- **Context fallback threshold**: Requires `auxiliary.compression` pin before >65K threshold works; see [[topics/senter/wiki/decisions/2026-09-08-context-fallback-threshold|decision]]
- **Vault-to-repo link**: Whether `~/Documents/Projects/Projects` is a git worktree, symlink, or clone of the `agent-wiki` repo — unresolved

^[raw/inbox/2026-09-09.md] ^[raw/inbox/2026-09-09-from-senter-wiki.md]

## 2026-09-09 20:00–20:33 — bridge snapshot debugging (scan-topics.py)
- **20:02** Chris re-issues the continuation directive: finish both Senter Wiki front and back end without confirmation. See [[topics/senter/wiki/decisions/2026-09-09-autonomous-senter-wiki-completion-continuation|decision]]. ^[raw/inbox/2026-09-09.md]
- **20:03** Hermes pivots to live Hermes Desktop DOM/CSS inspection and bot/session visibility patches. ^[raw/inbox/2026-09-09.md]
- **20:05–20:08** Hermes inspects bridge config (`BASE`/token), then notices bot names in the `senter` topic still carry `.md` suffixes in `.system-live.json`. Traces it to `scan-topics.py` naming logic: topic-level `scan_topics()` bots lack a `model` field; `snapshot()` merging profile-level and vault bots can leave mixed `skills` types; bridge `vaultFetch()`/`loadLive()` data paths confirmed. ^[raw/inbox/2026-09-09.md]
- **20:10** Hermes identifies the merge bug: `scan_bots()` returns profile bots with `model`, but `scan_topics()` creates topic bots without `model`, and `snapshot()` prints assuming all bots have it. ^[raw/inbox/2026-09-09.md]
- **20:11–20:16** Follow-on fix attempts: `scan_vault_agents()` skills type coercion, duplicate `skills` keys, stale `/Users/sovthpaw/Documents/Projects/Projects/.system-live.json` vs bridge-served path investigation. ^[raw/inbox/2026-09-09.md]
- **20:17** Confirmed bridge serves `.system-live.json` via `/file` from `FILE_ROOTS`; Hermes Desktop `loadLive()` fetches `http://127.0.0.1:8643/.system-live.json`. ^[raw/inbox/2026-09-09.md]
- **20:23–20:33** Bridge health confirmed running; curl/token access timeouts observed; investigation of why a vault bot (`senter-wiki-readme-live`) still shows `skills=[]` after patch attempted. Session ends mid-debug. ^[raw/inbox/2026-09-09.md]

### Open items (2026-09-09 20:33)
- `scan-topics.py` snapshot normalization: confirm whether `scan_topics()` bots need `model`; confirm patch application to all three scan paths (`scan_topics`, `scan_vault_agents`, loop scan); verify which `.system-live.json` the wiki UI is reading.
- Bot/sessions layout visibility in Hermes Desktop — still unresolved; data contract is live (69 bots served), UI rendering path under inspection. See [[topics/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|decision]].
- Vault-to-repo relationship (`~/Documents/Projects/Projects` ↔ `gh-sync/agent-wiki`) — still unresolved.

^[raw/inbox/2026-09-09.md]

## 2026-09-10 — continuation of scan-topics.py debugging
- **10:23** Hermes: "The update mechanism is the git repository. The git repo is there. Let me verify the current JSON file has the correct structure by checking if the bridge can serve it:" ^[raw/inbox/2026-09-10.md]
- **10:29** Hermes: "Let me check the bots section of the JSON file for the senter-wiki-readme-live bot:" ^[raw/inbox/2026-09-10.md]
- **10:30** Hermes: "The issue might be that the Hermes Desktop is showing old data because the bridge might be serving a cached version, or there's something wrong with how the BOTS view renders in vault-live.html. Let me check the vault-live.html to see if there are any issues with the renderBots function:" ^[raw/inbox/2026-09-10.md]

The 2026-09-10 raw items (1335 b + 1189 b) are Hermes working output from the same debugging session — no new Chris decisions. They continue evidence on the scan-topics.py schema debugging and the bot/sessions visibility path.

### Status: schema fix landed in committed code

The committed `assets/scan-topics.py` now has uniform bot schemas across all three scan functions:
- `scan_topics()` line 143: `{"name": ..., "role": ..., "model": "", "skills": 0}`
- `scan_vault_agents()` line 227: `{"name": ..., "role": ..., "model": "", "skills": 0, ...}`
- `scan_bots()` line 185: `{"name": ..., "role": ..., "model": model, "skills": nskills, ...}`

All bot objects now have `model` (string) and `skills` (integer). The `snapshot()` print lines 408/410 work against uniform objects. The schema normalization bug from the 2026-09-09 debug session is **resolved** in committed code.

### Open items (carried from 2026-09-09 20:33 + 2026-09-10)
- **Bot/sessions layout visibility** in Hermes Desktop — still unresolved; data contract is live (69 bots served via bridge), UI rendering path in `vault-live.html` belongs to senter-wiki per BRIEF anti-scope. See [[topics/senter/wiki/decisions/2026-09-09-bot-sessions-layout-inspection|decision]].
- **Vault-to-repo link**: Whether `~/Documents/Projects/Projects` is a git worktree, symlink, or clone of `agent-wiki` — unresolved (confirmed NOT a symlink; git initialized, remote = `SouthpawIN/agent-wiki`).
- **Event-driven topic-agent trigger**: Still on 5-min timer; WatchPaths event-driven firing not confirmed landed. See [[topics/senter/wiki/queries/event-driven-topic-agent-trigger|query]].

^[raw/inbox/2026-09-10.md] ^[raw/inbox/2026-09-10-from-legacy-bots.md]