---
title: Decision: hero orbs centred on the row-dot column, geometry never from lettering
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui]
sources:
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
confidence: high
---

# Centre-anchored hero orbs (2026-09-03, batch 9 — FINAL)

**What.** `.heroOrbs { left:var(--dotsc); transform:translateX(-50%) }`, `alignHero()` self-corrects on centres; `--heroNudge` retired; title mutations sync numbers only.
^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md]

**Chris's words.** *"I don't like them flush with the right side — centered, exploded, equal distance on both sides across the other dots."* / *"I'm worried the positioning is based
on the lettering … different titles are making the four dots move … I want those four dots fixed in the center of the screen."* ^[raw/sources/knowledge/skill-agent-wiki-vault.md]

**Why it took rounds.** A 48px disc column went 3→7→11px right with "still off" each time while measured edge Δ was 0.00 — he was aligning centres (22px = (48−4)/2).
Rule: when aligned elements differ in size, anchor the CENTRE of the group; a nudge constant is a patch on the wrong anchor. Supersedes batch 5/6 right-anchor.
See [[wiki-topics/senter-wiki/wiki/concepts/row-geometry-and-dot-column|row geometry]], [[wiki-topics/senter-wiki/wiki/concepts/verification-and-proof-methods|proof methods]].
