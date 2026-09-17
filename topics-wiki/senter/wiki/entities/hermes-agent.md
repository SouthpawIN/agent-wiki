---
title: Hermes Agent (the runtime)
created: 2026-09-05
updated: 2026-09-06
type: entity
tags: [tool, repo, infra]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-06.md, raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/sources/knowledge/anser-SOUL.md, raw/sources/knowledge/klerik-AGENTS.md]
confidence: high
---

# Hermes Agent (the runtime)

**Hermes Agent** (Nous Research; Chris's dictation: "Hermia's agent") is the runtime every fleet bot runs on. Each bot is a *profile* under `~/.hermes/profiles/<name>/` launched with `hermes -p <name>` (`HERMES_HOME=~/.hermes/profiles/<name>`). Chris works with the Hermes team and uses his own fork `SouthpawIN/hermes-agent` for immediate fixes ([[topics-wiki/senter/wiki/decisions/2026-09-02-upstream-pr-policy|PR policy]]). Docs: https://hermes-agent.nousresearch.com/docs; repo: https://github.com/NousResearch/hermes-agent. ^[raw/sources/knowledge/klerik-AGENTS.md] ^[raw/sources/knowledge/anser-SOUL.md]

## Chris's standing instruction: squeeze Hermes into the four lanes, don't re-implement
"look at my agent wiki github because that's the baseline for this … see what of Hermes we can squeeze into each one of these lanes into topics, [skills, bots, loops]. And: talk to [[topics-wiki/senter/wiki/entities/anser|anser]] at length to find what already exists." ^[raw/inbox/2026-09-05-legacy-inbox.md]

## Native Hermes pieces the Senter system maps onto (2026-09-05 mapping)
|| Senter part | Hermes native piece |
|||---|---|
|| Sidebar | the `senter` profile; SOUL = sidebar spec as of 18:58 |
|| [[topics-wiki/senter/wiki/entities/watcher|Watcher]] | fed by `hermes sessions export` / `agent.log` / bridge events; `on_session_finalize` hook for session end |
|| Topic loops | `hermes cron` per topic; workers = `hermes -p senter <topic>`; `hermes kanban` claims |
|| Skills / bots | `hermes skills` / `hermes profile create` + klerik review |
|| Approvals | `hermes serve` `approval.*` (Anser's #1) |
|| Filling the wiki | `hermes sessions export --format md` (Anser's WRAP verdict; no custom parsing) |
|| Profile setup | `hermes profile create/alias`, `config set tts.edge.voice`, `config set display.skin` |

## 19:06 — Chris makes it a decision; 19:12 — what is actually native now
Chris: "If there's a way that we can get this entire flow down to just built in Hermes commands and markdown, that would be great… the backend stuff could probably work to be a lot more efficient now that we know what the idea is for the intended flow" → [[topics-wiki/senter/wiki/decisions/2026-09-05-backend-as-builtin-hermes-plus-markdown|decision]]. Hermes's answer supersedes the 16:30 table above for the rows it touches: topic agent = `hermes chat -p senter`, loops = `hermes cron`, bots = `hermes profile`, wiki = `llm-wiki` layout; still custom = watcher (no per-message hook), bridge (SSE + file proxy), TF-IDF cutter. The 16:30 rows for `hermes kanban` claims and per-topic workers were replaced by the [[topics-wiki/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|one-agent-per-topic decision]]. Full ledger: [[topics-wiki/senter/wiki/comparisons/native-hermes-vs-custom-backend|native vs custom backend]]. ^[raw/inbox/2026-09-05.md]

## Hermes facts learned the hard way (from the skill)
- `delegate_task` rejects any `<…>`/`{…}` placeholder as an "unexpanded template marker" and nothing in the batch spawns; `action=steer` fails on a finished child ("No live subagent").
- `message_agent` is fire-and-forget (ack, not reply); the DM runner gives up after ~120 s `target_busy`.
- Profiles don't inherit root `auxiliary.vision` config — pin it in every profile.
- `desktop_preview` handles web URLs and local HTML/MD only; `open` STACKS tabs.
- `computer_use capture app=Hermes` can grab a 1456×31 title-bar sliver — pass pid + window_id of the window titled `Hermes`; `mode=ax` exposes the `AXWebArea` pane bounds ([[topics-wiki/senter/wiki/concepts/preview-pane-viewport|pane viewport]]).
- Approval gate classifies pattern FAMILIES (inline `-c`/`-e`, pipe-to-interpreter, heredoc-to-interpreter, shell appends) — each is a card Chris must click.
- Sanitized repo configs (`***`) crash YAML → silent fallback to defaults ("No inference provider configured").
- Built-ins vs the vault (anser's audit): memory = flat facts, skills = procedures, session_search = raw episodes, SOUL/AGENTS = fixed contracts; the vault = the structured growing self-model none provide ([[topics-wiki/senter/wiki/concepts/selfmodel-layer|Self-model layer]]).

## Config pitfalls — 2026-09-06 (model switching, TTS, vision)
- **`fallback_providers` ordering must list the user's picked model first** (not `stepfun/step-3.7-flash:free`). When the `turbofit` provider at the top of the chain is unavailable, the chain now falls to `z-ai/glm-5.3-flash`. Profiles don't inherit root config — each profile's fallback chain needs the user's preference ahead of free-tier defaults ([[topics-wiki/senter/wiki/concepts/model-fallback-chain|model fallback chain]], [[topics-wiki/senter/wiki/decisions/2026-09-06-model-picker-sticky-and-tts-gateway|decision]]).
- **`auxiliary.compression.provider: auto`** lets the context summarizer auto-select stepfun. Set explicitly to `nous` / `z-ai/glm-5.3-flash` to stay sticky.
- **`auxiliary.vision.provider: auto`** picks a free-tier model that times out and retries — pin a timed model (e.g. gemini-3.8-flash at 4.4 s) with a 45 s timeout in root config AND every profile config ([[topics-wiki/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch + sentinel round 5]]).
- **JWT-based entitlement cache for `managed_nous_tools_enabled()`** has a 60 s TTL and goes stale when credits are added — `resolve_managed_tool_gateway` must use `force_fresh=True` for TTS resolution ([[topics-wiki/senter/wiki/concepts/nous-managed-gateway|managed gateway]]).

Related: [[topics-wiki/senter/wiki/entities/teknium|teknium]] (Hermes builder), [[topics-wiki/senter/wiki/entities/senter-bridge|senter-bridge]] (plugin).
