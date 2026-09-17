---
title: Dispatch — delegate_task children vs shell-spawned `hermes -q` Meeseeks
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [tool, infra, decision]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Dispatch — delegate_task children vs shell-spawned `hermes -q` Meeseeks

Chris: "don't queue tasks, don't make me wait several minutes for a task to start… many in parallel." Measured on 2026-09-02 across the same class of work (3-line CSS items on the 309 KB `vault-live.html`). ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

| Dimension | `hermes -q` shell Meeseeks | `delegate_task` child |
|---|---|---|
| Time to first tool call | 30–60 s | ~3 s |
| Per item | 20–33 min, 120–160 tool calls | 7–11 min, 19–24 calls |
| Identity in bridge | correct `bot=<name>` | attributes as `bot=senter` (gap for teknium) |
| Protected-file approvals | card in the wiki via bridge | desktop prompt, not the wiki (gap) |
| Second instance of a bot | DM runner refuses (`target_busy`); direct `HERMES_HOME=… hermes chat -q` works | native parallelism (≤10) |
| Steering | DM (may drop) | `action=steer` while live; finished child → new child |
| Brief hazards | empty brief if `$(cat path)` runs after rename | `<…>`/`{…}` placeholders reject the whole batch |
| Bot's own SOUL/AGENTS/skills | loaded automatically | must be INLINED in `context` ("You are acting as the bot WEAVER…") |

## Verdict (anser's council + measurement)
**Primary = `delegate_task`.** Brief shape: `context` = role + the bot's rules that matter (write_file/patch only, don't touch elements owned by parallel children, Playwright `require(process.env.PW)` path); `goal` = ask + proof steps + budget (≤8 min, ≤30 calls, verify-LIGHT per edit / FULL once) + "end with exactly one DONE/BLOCKED line"; `output_schema` with the 3–4 fields Senter will read. Same-element items → ONE child. **Exception:** SOUL/AGENTS (protected) writes still go `hermes -q` so the approval lands as a wiki card. Details: skill `references/delegation-model.md`.

## Caveats learned after switching
Same-file parallel children inflate each other's verify cost (one ran 13 min / 41 calls over budget) and may breach tooling rules under pressure; a child reporting BLOCKED "context lost" may have finished; `vision_analyze` latency (round 5) dominated child time until pinned. See [[topics-wiki/senter/wiki/concepts/meeseeks-model|Meeseeks model]], [[topics-wiki/senter/wiki/entities/senter-dispatch-and-sentinel|dispatch + sentinel]].
