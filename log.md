# Wiki Log

> Chronological record of all Agent Wiki actions. Append-only.

## [2026-11-07] fix | turbofit bot is TurboSouth
- Callsign corrected: Fitment → TurboSouth, from the TurboSouth support project
- Mission realigned: install → verify a real completion → upstream PR, with the fit
  matrix as the data that answers "will it run on my machine"
- New skill `support-verify`; 28 skills total

## [2026-11-07] rename + rewrite | agent-wiki → bot-wiki
- Repo renamed `SouthpawIN/agent-wiki` → `SouthpawIN/bot-wiki` (GitHub redirects old URLs)
- README rewritten from the original concept (Senter, four primitives, flywheel, markdown-as-API)
  to the current organisation (one bot per topic, BOT.md as the unit, Hermes profile per bot)
- No structural changes: bots/, catalogs/, BOT_SCHEMA.md unchanged

## 2026-11-07 — Bot-first reorganisation

Replaced the topic tree with a bot tree. One bot per topic; the bot owns its
context, skills, and loops. Added `BOT_SCHEMA.md`, the `_fleet` index, and a new
`bot` primitive in `senter_agent` (path inference for `bots/*/BOT.md`, skills, and
loops; bot proposals in the planner; `bots/<slug>/BOT.md` materialization).

Seeded nine bots: bot-wiki (Klerik), youtube (Cutroom), pocketshop (Binder),
turbofit (TurboSouth), kart-racer (Apex), ai-daw (Riff), anser, hermes (Mesh),
ssi (Beacon). 27 skills, 12 loops, one live.

Removed the standalone topic index; `catalogs/bot-roster.md` replaces it.

## [2026-07-07] create | Agent Wiki initialized
- Created repo: SouthpawIN/agent-wiki
- Spec: spec.md, README.md
- Catalogs: fleet-dashboard, agent-roster, skill-registry, loop-registry, topic-index
- Concepts: goop-whitepaper, goop-nesting
- Assets: 5 Nous-style concept images
- Structure: catalogs/, topics/_global/, assets/
