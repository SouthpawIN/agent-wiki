---
name: hermes-fleet-ops
description: Use when creating or orchestrating Hermes bot fleets.
version: 1.0.0
tags: [hermes, profiles, bots, fleet, orchestration]
---

# Hermes Fleet Ops

Class-level playbook for standing up and coordinating multi-bot Hermes fleets. Validated
2026-08-30 building the senter/klerik fleet on the Mac.

## Architectural pattern that landed (user-chosen)
- **One CENTER bot** the user talks to for everything (coordinator). It routes ideas to
  specialist bots, captures ideas verbatim to the vault `Ideas.md`, delegates — never does
  specialist work itself, and NEVER edits other profiles directly.
- **One FACTORY bot** (meta-agent) that creates/refines other profiles on delegation.
  Klerik (github.com/SouthpawIN/klerik) is the user's factory: surgical SOUL.md edits,
  DSPy+GEPA optimization, strict setup checklist.
- **Refine-before-create is a hard rule**: before spawning, search `hermes profile list`
  + vault `wiki-topics/` + `Ideas.md` for overlap; if an existing bot nearly covers the domain,
  delegate a refinement to the factory instead of spawning a sibling.
- Roles go in the bot's SOUL.md with the roster table inline (see
  `references/senter-soul-pattern.md`), and every fleet change is logged same-turn to the
  vault `log.md` + `catalogs/agent-roster.md` — markdown is the API.

## Creating a profile from a GitHub repo (validated sequence)
```bash
hermes profile create <name>
P=~/.hermes/profiles/<name>
ln -sf ~/.hermes/.env $P/.env                 # credential symlinks — skipping these starves the profile
ln -sf ~/.hermes/auth.json $P/auth.json
cp <repo>/SOUL.md $P/SOUL.md                  # keep an unmodified .orig copy before grafting roles
cp <repo>/AGENTS.md $P/AGENTS.md
mkdir -p $P/herm && cp <repo>/herm/tui.json $P/herm/   # klerik-repo profiles
for s in <repo>/skills-capabilities/*/; do [ -e "$P/skills-capabilities/$(basename $s)" ] || cp -R "$s" "$P/skills-capabilities/"; done
hermes profile alias <name>
hermes -p <name> config set display.skin <skin>        # orchestrator: poseidon/tokyonight
hermes -p <name> config set tts.edge.voice en-US-GuyNeural
hermes -p <name> config set agent.bot_mode_protocol true   # enables message_agent DMs
```
Verify: `hermes -p <name> chat -q "one sentence: who are you?"` — confirm it answers in-role.

## Voice/false-trigger tuning (desktop, noisy household)
- Wake word firing on TV/kids: lower `wake_word.sensitivity` (0.6 → 0.35) and raise
  `wake_word.confirmation_frames` (3 → 8) FIRST; if misfires persist, disable entirely
  (`hermes config set wake_word.enabled false`) and rely on push-to-talk (`voice.record_key`,
  default ctrl+b). User chose full disable — push-to-talk is the "only listen to me" answer.
- Barge-in cutting replies on background chatter: `voice.barge_in false`, grace 0.9s,
  `voice.silence_duration` 3.5s. All via `hermes config set`, never hand-edit config.yaml.

## Pitfalls
- `hermes profile create` makes an empty profile — a profile without the .env/auth symlinks
  inherits shell keys unreliably; symlink first thing.
- Grafted SOUL roles: append a clearly-marked part (originals keep a `.orig` copy) so the
  upstream persona stays intact — same surgical-edit principle the factory bot itself uses.
- Fleet descriptions live in profile Title/Description (Bot Mode roster reads them) — keep
  them in sync with the SOUL roster table so `message_agent` targeting stays accurate.
- Don't name bots after machines/sessions that will drift; the user keys on role words
  (senter='center').
