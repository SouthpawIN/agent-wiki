# Session — senter (canvas) · 2026-09-05 18:33

## State of the system (all LIVE, launchd user domain)
| Piece | Service | Does |
|---|---|---|
| Watcher = cutter | com.senter.watcher | tails state.db per message, cuts at subject changes, files to wiki-topics/<t>/raw/inbox/<day>.md, new subject → scaffold + research + "want a bot?" cards |
| Topic agent | com.senter.topic-agent (WatchPaths on every raw/inbox + 10m fallback) | ONE run per topic: raw → structured LLM wiki (wiki/, index.md) → pitches bots-profiles/triggers-loops/research (cards), skills auto-apply |
| Umbrella | com.senter.umbrella 30m | merge/dedupe at locked .35/.50, bot promotion, stale reminders, _global catalogs, INDEX, WatchPaths sync |
| Bridge | com.senter.bridge :8643 | /post /stage /approve (APPLIES: bot→klerik build or reuse · loop→hermes cron create · research→looker into the page) /music/youtube/search+audio |
| UI | vault-live.html | CONTEXT = full wiki index; proposed rows hollow + APPROVE/REJECT; STAGE performs fleet events; HUD z120 / chat z110-130 above all; real EQ from bridge audio |

## Proven today
- Compiles: senter 60 pages, senter-wiki 55 pages (decisions with provenance + contested flags).
- Approve → cron: klerik-queue-drain e6e20c22e1b9 live on klerik. Approve → bot: senter-wiki-bot building via klerik (in progress).
- Music: Godhood streamed via bridge, EQ 40/42 cells lit from the analyser.

## Open
- Spotify client id (Chris only). senter-wiki-bot build finishing. Watcher misfiles on thin topics until their wikis fill.
- Default desktop profile still the builder; `senter` profile SOUL is now the sidebar spec — switching the desktop sidebar to `senter` is Chris's call.
