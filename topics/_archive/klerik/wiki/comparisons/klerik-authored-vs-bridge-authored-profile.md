---
title: Comparison — klerik-authored profile (first attempt) vs bridge-authored deterministic profile (re-run)
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [bot, infra, spec, decision]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# klerik-authored vs bridge-authored profile

The two ways a new bot's protected files can come into being, as they actually ran on 2026-09-05. Left column = the 18:20 prompt (`/tmp/apply-senter-wiki-bot-1788650447.md`); right = `_apply_approved` in `senter-bridge/server.py` after 18:42's "Re-run the approval through the new deterministic path" ^[raw/inbox/2026-09-05.md].

| | klerik authors SOUL/AGENTS (18:20 run) | Bridge writes, klerik finishes (deterministic) |
|---|---|---|
| Who writes SOUL.md / AGENTS.md | klerik, headless, 30 turns | bridge, from the card's `## SOUL.md (draft)`, role paragraph, `## First task` |
| Protected-file guard | **blocks** — no human in the session; result "half-made (default SOUL, no AGENTS)" | not hit — the bridge process is not a Hermes agent session |
| Content quality | rich, judgement-driven (fleet table, first-move rules, tightened voice) — but stranded in a handoff file | templated, predictable, shorter; exactly what Chris approved plus a fixed Voice block |
| klerik's remaining job | everything | voice/skin/tui/alias/describe + read-only gap report (15 turns, 600 s) |
| Failure mode | silent stall at the gate; "writing the SOUL now" looked true from outside | none observed yet; proof gate still `SOUL.md exists` (too weak) |
| Traceability | klerik wrote `## Status` + `## Applied` on the card and a handoff file | bridge writes `## Applied` with klerik's last line; feed cards attributed to `senter` |
| Matches Chris's rules | rule 7 kept (no routing around the gate) | root-cause fix; no hand edits |

**Reading.** The right column is the right *architecture* (authority for protected writes comes from Chris's approval, not from a bot) but its done-check is the same class of weakness the left column exposed — a file existing is not a bot running. Merge the two: bridge writes, klerik verifies with `-q` → `bridge/loaded`, and only then the card flips. Background: [[topics/klerik/wiki/concepts/protected-file-guard|Protected-file guard]]; the general pattern: [[topics/klerik/wiki/comparisons/rename-vs-real-spawn|Rename vs real spawn]]; the bot in question: [[topics/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]].
