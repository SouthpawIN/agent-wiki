---
title: Profile setup checklist (what "spawned" means)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, bot, tool]
sources: [raw/sources/knowledge/klerik-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/paladin-SOUL.md]
confidence: high
---

# Profile setup checklist (what "spawned" means)

[[topics-wiki/senter/wiki/entities/klerik|Klerik]]'s mandatory setup for every profile it creates or reviews, plus the completion criteria the fleet learned the hard way. ^[raw/sources/knowledge/klerik-AGENTS.md]

## Klerik's base order
```
hermes profile create <name>
ln -sf ~/.hermes/.env ~/.hermes/profiles/<name>/.env
ln -sf ~/.hermes/auth.json ~/.hermes/profiles/<name>/auth.json
# write SOUL.md and AGENTS.md
hermes -p <name> config set tts.edge.voice <voice>
hermes -p <name> config set display.skin <skin>
mkdir -p ~/.hermes/profiles/<name>/herm   # tui.json: theme + eikon
hermes profile alias <name>
```
- **TTS voice by archetype**: warm/creative feminine → `en-US-JennyNeural`; caring feminine → `en-US-AvaNeural`; strong masculine or calm editorial → `en-US-GuyNeural`; neutral → `en-US-AriaNeural` (default).
- **CLI skin**: creative → `daylight`/`warm-lightmode`/`default`; dev → `ares`/`slate`/`charizard`; orchestrator → `poseidon`/`slate`; editorial → `mono`.
- **Herm TUI** `herm/tui.json` (`mouse`, `targetFps 30`, `theme`, `eikonPath`): creative → `default.eikon` + `lucent-orng`/`catppuccin`; dev → `ares.eikon` + `orng`/`monokai`; orchestrator → `mono.eikon` + `tokyonight`/`nord`/`vercel`; editorial → `mono.eikon` + `mono`/`slate`.
- Pitfalls: credential starvation (missing `.env`/`auth.json` symlinks); skipping TTS/skin/eikon.

## Fleet-learned additions (filed on klerik's checklist)
1. **Bridge wiring** (2026-09-02, weaver was the case): symlink `profiles/<bot>/plugins/senter-bridge` + `plugins.enabled` entry — a clone made before the plugin existed has neither, so its first turn runs invisible to the wiki. ([[topics-wiki/senter/wiki/entities/senter-bridge|bridge]])
2. **Smoke turn = completion criterion**: `HERMES_HOME=~/.hermes/profiles/<bot> hermes chat -q 'say ready'` must emit `bridge/loaded` + `turn end` in events.jsonl (~7 s). "A bot is spawned when it RUNS, not when its directory exists" — [[topics-wiki/senter/wiki/entities/paladin|paladin]] was "spawned" twice as an AGENTS.md + 33-byte config.
3. **Post-install sanity** (2026-08-31, anser): `grep -c '\*\*\*' config.yaml` — sanitized `***` values crash YAML → silent default config → "No inference provider configured." Replace with `null`, validate with the hermes venv python. config.yaml is not protected, so Senter may patch it directly.
4. **Audit stale routing** in installed SOUL/AGENTS (dead fleet members, creation chains through departed agents).
5. **Pin `auxiliary.vision`** (provider + timed model + 45 s timeout) — profiles don't inherit root config.
6. Install the shared skills: `bot-verify-loop`, `wiki-look-verify` (builders/QA), the topic's design skill read-only where relevant.
7. Roster/pet entry + `catalogs/agent-roster.md` only after the smoke turn passes.
8. Definition per skill: SOUL + AGENTS + model + bridge symlink + `plugins.enabled` + skills on disk AND the smoke turn. ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

Related: [[topics-wiki/senter/wiki/concepts/routing-rules|Routing rules]] (spawn only on white space).
