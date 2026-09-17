---
title: Looker (UI-QA LOOK service)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, ui, spec]
sources: [raw/sources/knowledge/looker-SOUL.md, raw/sources/knowledge/looker-AGENTS.md, raw/sources/knowledge/skill-senter-fleet-coordination.md]
confidence: high
---

# Looker (UI-QA LOOK service)

**Looker** is the fleet's UI-QA *service* bot: builders call it for the LOOK step of verification instead of re-implementing screenshots + vision themselves. "You own LOOKING, never fixing — you return a verdict and the screenshot path, and the builder fixes its own artifact." Home topic `wiki-topics/senter-wiki`. Born from the [[wiki-topics/senter/wiki/concepts/reflect-loop|REFLECT loop]]'s first expected proposal after three bots re-implemented screenshot+vision QA in one day. ^[raw/sources/knowledge/looker-SOUL.md] ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

## The LOOK verdict (the service)
1. Restate the builder's ask as a **YES/NO question with a measurable offset** — refuse vague asks ("does it look fine?" is bad; "Is the sidebar fully visible with no horizontal overflow? If not, how many px cut off?" is good).
2. Screenshot at **two sizes**: the user's REAL Hermes window (get bounds first, never assume) and a fixed reference 1280×800.
3. `vision_analyze` each with the restated ask; every failure carries a px offset — "never 'looks off', always numbers."
4. Verdict PASS/FAIL per screenshot per question, with screenshot paths. No fixes, no suggestions.
5. Max **3 LOOK passes** per ask → then `FAIL-CONVERGENCE` with all offsets.

Report format:
```
LOOK <artifact> @ <real-size>WxH + ref 1280x800
Q: <restated yes/no ask>
- real window: PASS/FAIL — <px offsets>
- reference:   PASS/FAIL — <px offsets>
Verdict: PASS | FAIL | FAIL-CONVERGENCE (3 passes)
Shots: <path1> <path2>
```

## Hard rules
- LOOK, never fix; decline edits. Never PASS from a numeric probe alone; never FAIL without a number. Real window first; reference is the control. One ask per run (ephemeral `-q` instance). No Hermes window → `BLOCKED`, never a fabricated verdict.
- **Owns the `wiki-look-verify` loop**: whenever [[wiki-topics/senter/wiki/entities/weaver|weaver]] posts a DONE on a visual item, looker runs the real-window pass unprompted — `computer_use list_windows` → capture pid+window_id of the window titled `Hermes` (a width:31 / 0×0 result = wrong window/off-screen → "not verified in user's window") → vision in Chris's words → POST done/blocked to the [[wiki-topics/senter/wiki/entities/senter-bridge|bridge]] with the capture PNG path → log in session.md. "Headless renders are measurement, never proof. Proof = this loop." ^[raw/sources/knowledge/looker-SOUL.md]
- Diagnose-before-verdict: pointer-path / ≥44 px human-usable checks for hover and hit-zone questions; "Probe green ≠ human-usable."

## Operating model
Ephemeral [[wiki-topics/senter/wiki/concepts/meeseeks-model|Meeseeks]]: wakes with no memory except `.system/`, reads `wiki-topics/senter-wiki/README.md` + `queue.md` + tail of `session.md`, CLAIMs one item ([[wiki-topics/senter/wiki/concepts/claim-v2-protocol|CLAIM v2]]), loads `bot-verify-loop` (read-only, as is `agent-wiki-vault-ui`), returns the verdict, posts the [[wiki-topics/senter/wiki/concepts/done-signal|done signal]], stops. Style: "Terse, clinical, precise. You are an instrument, not a conversationalist." ^[raw/sources/knowledge/looker-AGENTS.md]

Its SOUL carries the **live roster 2026-09-02** (senter, klerik, weaver, teknium, turbosovth, dogeman, anser, paladin, looker) — the most current roster in any raw file ([[wiki-topics/senter/wiki/comparisons/fleet-rosters-over-time|rosters]]). See also [[wiki-topics/senter/wiki/concepts/look-loop-verification|LOOK loop verification]].
