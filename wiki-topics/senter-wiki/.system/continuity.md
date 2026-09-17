# Continuity — senter-wiki (what the system currently understands)
_Spec: "Context's raw understanding from chat sessions." Watcher-maintained from 2026-09-05; Chris may correct any line — user
edits are never overwritten (mark with `<!-- chris -->`)._

## Purpose
A live-acting second brain. The UI is Cursor for markdown over agentic artifacts. Tempo is **per message**, not per session:
Chris talks, the wiki visibly moves, skills-capabilities/bots-profiles/loops get proposed all the time; he can hand-edit anything or say it.

## Roles (strict)
- **Sidebar** (Hermes desktop, default profile): conversation only. Yes-and, rubber-duck, extract context. Receives approvals.
  Never does tasks; must stay unencumbered and never be interrupted by work.
- **Watcher**: tails the Hermes message table directly (no hand-off), files each message into a topic, posts a card.
- **Topic workers**: one senter-like worker per topic, asynchronous; context → skills → (cluster) → bot → (workflow) → loop.
- **Umbrella senter**: opinionated about combining — topic merges/splits, cross-topic skill dedupe, promoting clusters to bots.
- **Approvals**: one card per proposal in the sidebar/feed; `hermes serve approval.*` is the target transport.

## Design law (abridged — full: rules.md)
Pure #000 + one paper white `--paper:#dfe8f5`; tiny-dots motif; active = hollow ring; no gray/translucency/gradients except the
invisible bottom fade; diagonal mask on the wallpaper; #FFE45A = attention only. Root-cause fixes only. Everything live.

## What Hermes already provides (Anser, verified)
`hermes sessions export` (transcripts) · `hermes cron` (loops) · `hermes kanban` / `kanban watch` (claims, dispatch) ·
`hermes serve` JSON-RPC `approval.pending/respond`, `file.attach` · dashboard :9119 `/api/profiles`, `/api/skills`,
`/api/audio/*`, `/api/files/read`, `/api/health` · `skills-capabilities/.usage.json` · `hermes profile create/describe`. Keep custom: file
watcher, TF-IDF similarity, topic locks.

## Known pains
Anser summarises unreliably (trust per-row citations); vision crops mislead at UI scale (use DOM); TCC blocks
`/usr/bin/python3` from ~/Documents under launchd (use venv python); `drive_preview` strips URL query/hash; Python splice
patches can eat a scheduling line silently (verify call site + runs counter).

## Open decisions
- Which profile hosts the sidebar SOUL rewrite (yes-and/rubber-duck)? Default profile is the candidate.
- `.proposed` file convention for unapproved artifacts vs a `proposals/` dir per topic.
- Merge `senter` + `senter-wiki` topics? Currently separate: senter = fleet/orchestration, senter-wiki = surface/memory.

## learned 2026-09-05 17:06 (worker, from 20 inbox blocks)
- Decision 2026-09-05: tempo is every message; ONE senter profile runs all loops for now (per-topic profiles only when a topic earns a bot); one card per proposal so the feed moves constantly.
- Sidebar SOUL (yes-and, rubber-duck, never does work, reads INDEX first) is drafted under agents/ and awaiting Chris's approval.
- GitHub API via curl is blocked on this host; raw.githubusercontent file pulls work.
- Watcher first real run processed the senter inbox: 36 blocks of Chris's actual messages.
- Volume rocker LOCK: no round knob — four 5px paper dots (top, cap-above, cap-below, bottom) joined by lines; the 10px gap IS the level; end caps anchored to #mVolTrack, never #mVolFill (fill collapses at 0). Knobs --volDot 5px, --volGap 10px.
- Rocker x-centre is DERIVED: midpoint of feed-card right edge (1128) and pane edge (1152) = 1140, not a hand nudge.
- Mute LOCK: 5px dot 14px left of the track at mid-height (--volMuteGap); muted = hollow ring + rocker dims; hover = #FFE45A; 26px invisible hitbox with soft paper glow on enter (--volMuteHit).
- Media hover zone: from EQ left edge (--eqLeft, written by the EQ placer so it tracks the wallpaper) to pane edge, top down to feed-stack top (~60vh); nothing drawn; click toggles mute, wheel moves level. Left of EQ above feed = dead zone → click toggles SPACE. Bottom corner = feed hover.

## learned 2026-09-05 17:13 (worker, from 5 inbox blocks)
- Proposals are visible as rows in the SKILLS/BOTS/LOOPS tables marked `proposed` (with their file paths) so Chris can watch them get proposed; 5 proposed rows were live as of 2026-09-05 17:12.
- Skill scanner covers BOTH `~/.hermes/**/skills` and vault topic `skills-capabilities/` dirs (spec's primary location) — topic skills were never rows before this fix.
- Open decision resolved: `.proposed` filename suffix IS the unapproved-artifact convention (not a `proposals/` dir).
- Bridge `/approve` endpoint does exactly two things and nothing else: drop the `.proposed` suffix (approve) or delete the file (reject); wiki cards carry APPROVE/REJECT buttons that call it.
- Umbrella senter first pass is kanban-free: it emits proposals only (merges/splits/dedupe as `.proposed` artifacts), same as every other worker; the probe used to test proposed rows was removed.

## learned 2026-09-05 17:18 (worker, from 2 inbox blocks)
- Umbrella first opinion (2026-09-05 17:13): merge senter-wiki → senter at similarity 0.65, AUTO-tier under the 09-02 locked thresholds; filed as a .proposed merge awaiting Chris, not auto-applied — the worker had kept them apart (senter = fleet/orchestration, senter-wiki = surface/memory).
- Merge veto convention: Chris blocks a proposed topic merge by writing the pair into wiki-topics/_global/.system/keep-separate.md.
- GitHub correction: `gh` CLI works and the GitHub API is reachable on this host; only `curl` to api.github.com is blocked. Both Hermes repos are cloned into the wiki as knowledge.
- topic-worker lives at assets/topic-worker.py, launchd every 5 min: one real `hermes -p senter` run per topic over the watcher inbox (GEPA collect → generate → evaluate → apply), writes .proposed files only.
- umbrella lives at assets/umbrella.py, every 30 min: topic merges/splits by locked similarity thresholds, cross-topic skill dedupe, bot promotion, stale reminders, _global catalogs + INDEX refresh.
- Umbrella first pass also proposed senter-wiki-bot (cluster of 4 skills, no agent file yet) and 2 cross-topic skill dedupes.
- Proposed-row rendering LOCK: hollow ring + PROPOSED tag in SKILLS/BOTS/LOOPS tables; pinned card carries APPROVE in attention yellow (#FFE45A) and REJECT.
- Pending Chris approval as of 2026-09-05 17:14: 5 skills, 1 bot (senter-wiki-bot), 1 merge (senter-wiki → senter), 2 dedupes.

## learned 2026-09-05 17:22 (worker, from 3 inbox blocks)
- Approval scope narrowed 2026-09-05 17:19: only BOT and LOOP proposals need Chris's approval card; skill proposals and wiki edits auto-apply (no .proposed wait). Supersedes 'one card per proposal' for skills.
- New-subject path: when the watcher files a message into a topic that did not exist, it immediately scaffolds the topic AND dispatches an existing bot to research it — no waiting for the 5-min worker tick.
- UI performance layer: a `wiki` event kind drives the surface — rows open, scroll, edit and close as fleet events arrive, so the wiki visibly acts out the fleet's work rather than just refreshing.
- Emitters for the `wiki` event kind: the watcher stages one event per filing, the topic worker stages one per edit/proposal, and the new-subject path stages the scaffold+dispatch; all wired to real events, never simulated.
- Source caveat: the 17:19–17:21 blocks are from the hermes session (assistant-side summaries of applied changes), not Chris's verbatim words — treat as implemented state pending Chris's confirmation.

## learned 2026-09-05 17:30 (worker, from 1 inbox blocks)
- Approval policy (2026-09-05 17:25): topics, edits, continuity lines and skills AUTO-APPLY — no cards; the topic-worker writes SKILL.md directly (5 pending skills were promoted). Only bots and loops remain `.proposed` with APPROVE/REJECT because they cost money and run unattended.
- Instant new-subject reaction: a substantive message that fits no topic makes the watcher scaffold wiki-topics/<slug>/ (README, .system, skills-capabilities/agents/loops) AND dispatch a research run to looker, which writes .system/research.md plus a Status line — no card, no waiting.
- Root cause of 'the wiki doesn't move': proposals were only files + feed cards; nothing told the wiki to animate until /stage existed.
- Spotify unblock is Chris-only: developer.spotify.com → create app → redirect URI http://127.0.0.1:43827/spotify/callback → `hermes auth spotify` and paste the ID. Control needs Premium; status/playlists/search work on Free.
- Still open as of 2026-09-05 17:25: kanban claims (lock files for now), sidebar SOUL rewrite (text proposed in agents/README.md), umbrella's senter-wiki → senter merge proposal.

## learned 2026-09-05 17:36 (worker, from 3 inbox blocks)
- Music is live, not demo: bridge exposes `/music/youtube/search` (no API key, parses the results page) and `/music/youtube/audio` (yt-dlp in the Hermes venv resolves the stream; bridge proxies it same-origin with Range support).
- EQ root cause fixed: a YouTube iframe gives the page no audio (EQ could only 'breathe'); now a real `<audio>` → Web Audio analyser → real levels; proof chain `playing/media/wired/analyser/running`, 40/42 cells lit on Godhood breakdown. Rocker and mute drive the real analyser.
- Player bar: typing a song name searches YouTube; a URL plays directly; queue is persisted but requires a play click after reload (browsers block autoplay).
- Z-layer LOCK: HUD (player, rocker, gear) z120; side chat z110 (z130 when open); settings z90; cards z70. Play button is the top hit at its own centre.
- Interaction law: clicking the player or feed never cancels the wiki's performance and never closes/swallows a card — only touching the wiki itself does.
- Feed verified 2026-09-05 17:33: watcher/worker/umbrella posts go through bridge `/post` and land in the sidebar feed alongside stage events and GitHub items (last window 43 senter posts, 17 stage events); verification is done against the events log, not by eye.
- Open as of 2026-09-05 17:34: Spotify client ID still needed; kanban claims; sidebar SOUL rewrite awaiting approval.

## learned 2026-09-05 17:42 (worker, from 1 inbox blocks)
- Media player bug 2026-09-05 17:36: `load()` never applied the rocker level to a newly created audio element, so tracks started at default loudness; fix is to set volume in `load()` itself. The Web Audio analyser chain is a passthrough and does not alter loudness.

## learned 2026-09-05 17:49 (worker, from 41 inbox blocks)
- The CONTEXT section of a wiki row renders the topic's full index.md (every page one line, wikilinked, with page/raw counts); the context orb count = wiki page count — not a 220-char summary.
- Compile loop com.senter.topic-wiki runs every 15 min: one senter bot run per topic over unprocessed raw items → pages created/updated → index rebuilt → feed card + wiki opens that topic. All 19 topics initialised; full session transcripts are NOT compiled per pass (too big) — grepped on demand.
- Approval policy changed 2026-09-05 17:19: topics, edits, continuity and skills auto-apply (topic-worker writes SKILL.md directly; 5 pending skills were promoted); only bots and loops stay .proposed with APPROVE/REJECT because they cost money and run unattended.
- New-subject path: a substantive message fitting no topic → watcher scaffolds wiki-topics/<slug>/ (README, .system, skills-capabilities/agents/loops) AND dispatches a research run to looker that writes .system/research.md + a Status line — no card, no waiting.
- load() must apply the rocker level to every new audio element — it previously never did, so new tracks ignored the volume.
- Feed verified receiving fleet posts via /post: 43 senter posts + 17 stage events in one window, plus GitHub items.
- Still open as of 17:42: kanban claims (lock files stand in), sidebar SOUL rewrite (text in agents/README.md), umbrella's senter-wiki → senter merge proposal.
