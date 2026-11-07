# Wiki Log

> Chronological record of all Agent Wiki actions. Append-only.

## 2026-11-07 — Bot-first reorganisation

Replaced the topic tree with a bot tree. One bot per topic; the bot owns its
context, skills, and loops. Added `BOT_SCHEMA.md`, the `_fleet` index, and a new
`bot` primitive in `senter_agent` (path inference for `bots/*/BOT.md`, skills, and
loops; bot proposals in the planner; `bots/<slug>/BOT.md` materialization).

Seeded nine bots: bot-wiki (Klerik), youtube (Cutroom), pocketshop (Binder),
turbofit (Fitment), kart-racer (Apex), ai-daw (Riff), anser, hermes (Mesh),
ssi (Beacon). 27 skills, 12 loops, one live.

Removed the standalone topic index; `catalogs/bot-roster.md` replaces it.

## [2026-07-07] create | Agent Wiki initialized
- Created repo: SouthpawIN/agent-wiki
- Spec: spec.md, README.md
- Catalogs: fleet-dashboard, agent-roster, skill-registry, loop-registry, topic-index
- Concepts: goop-whitepaper, goop-nesting
- Assets: 5 Nous-style concept images
- Structure: catalogs/, topics/_global/, assets/
