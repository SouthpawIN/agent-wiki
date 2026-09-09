# Anser brief — "what is already built into Hermes that Senter should use instead of replicating?"
Date: 2026-09-03. Asked by: Chris via Hermes (default profile). Format: multi-turn, one capability area per turn.

## What Senter / the Senter wiki does today (custom code, all in ~/Documents/Projects/Projects)
| Capability | Current implementation | Question for Anser |
|---|---|---|
| Fleet of bot profiles (senter, klerik, anser, paladin, looker, teknium, weaver, dogeman, turbosovth) | `~/.hermes/profiles/*` + hand-written SOUL/AGENTS | Is `hermes profile` + `distribution.yaml` + `hermes profile describe` the intended registry? Kanban orchestrator reads descriptions — should Senter's dispatch use `hermes kanban`? |
| Scanner: walks topics/skills/bots/loops, writes `.system-live.json` every change | `assets/scan-topics.py --watch` under launchd `com.senter.scanwatch` | Does Hermes have a file-watch / hook mechanism (hooks, plugins, `hermes serve`) that should host this? |
| Usage heat chart: mentions per item per day | direct SQL on `~/.hermes/state.db` `messages_fts` | Is there a supported API (`hermes sessions`, `insights`, `memory-graph`, `dump`) instead of raw SQLite? Any schema-stability promise? |
| Bridge: `127.0.0.1:8643` `/health /file /post /write /ask /events /pending` — feed events, approval cards, file writes from the page | custom Python plugin `~/.hermes/plugins/senter-bridge/server.py` | Should this be `hermes serve` / `hermes webhook` / `hermes gateway` / a desktop plugin instead? What do `hermes approvals` and the gateway expose for pending approvals? |
| Feed: bot messages → bottom-corner cards | bridge SSE `/events` + cron `senter-fleet-feed` every 2m | `hermes send`, `hermes peer`, `hermes portal`, `hermes monitoring` — which is the intended inter-agent message bus? |
| Loops (reflect, verify-nightly, sentinel…) | `topics/*/loops/*.md` prompts + `hermes cron` | Is `hermes cron` + `hermes learning` + `hermes curator` the right home? What does `curator` actually do? |
| Similarity / ranking (TF-IDF over full texts) | in-page JS | `hermes memory-graph` / `insights` — is there an embedding or graph API we should use? |
| Locks: protect a topic from auto-summarization | `.system/lock.json` per topic | Anything native (memory pinning, `checkpoints`)? |
| Skills registry: 124 skills across profiles, "carried by" | scanner reads every `SKILL.md` | `hermes skills` / `bundles` — what do they list/manage? Can Senter read skill metadata from one command? |
| Sharing a page (context/skills/bots/loops bundle) to Hermes | `hermes.send` from the page into the composer | `hermes send`, `hermes dump`, `hermes import-agent` — better paths? |
| Self-documentation: log.md / session.md / queue.md per turn | hand-written by the agent | `hermes journey`, `hermes checkpoints`, `hermes insights` — do any of these produce what the wiki needs? |
| Verification evidence (looker) | `verification_evidence.db` in anser profile? | What writes `verification_evidence.db`? Is `hermes verify` the tool for the LOOK loop? |

## Output wanted from Anser
For EACH row: (a) the Hermes-native feature (exact CLI/tool/plugin name, one-line what it does, how to verify it exists on this install), (b) verdict REPLACE / WRAP / KEEP-CUSTOM with one sentence why, (c) the first concrete command to try. Plain text, no MEDIA attachments.
