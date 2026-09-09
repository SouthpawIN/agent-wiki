---
title: People and bots around the Senter Wiki
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [person, bot]
sources:
  - raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
confidence: medium
---

# People and bots

## Chris (sovthpaw)
Owner. Steers the UI live by voice from the Hermes sidebar; co-author of the GOOP whitepaper (as *sovthpaw*, with Anser, 2026-07-04). Vocabulary he fixed:
**Agent** = the agentic harness (Hermes Agent); **Bot** = specialised sub-worker (a profile with SOUL.md); **sub-agents** = drones. Working style:
[[topics/senter-wiki/wiki/concepts/chris-ui-working-style|Chris's UI working style]]. ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

## Bots that touch this topic
| Bot | Role here | Evidence |
|---|---|---|
| **senter** | the one profile running all loops (watcher, worker, umbrella, compile) — *"one senter profile running the loops (per-topic profiles come later, when a topic earns a bot)"* | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **anser** | redundancy gate / "native before custom" oracle: `hermes -p anser -z "<q>…"`; hallucinates features → keep a "claimed but did not verify" list under `.system/anser/` | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| **looker** | receives the new-subject research dispatch; writes `.system/research.md` + Status | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **teknium** | noted 09-02 that `hermes auth spotify` was never run | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **weaver** | owns `verify-nightly` (loop page) and the wiki UI per memory | loops/verify-nightly.md |
| **klerik** | profile factory — the only bot allowed to edit other profiles (fleet rule) | system prompt |
| **senter-wiki-bot** (PROPOSED) | umbrella's promotion: 4 skills, no agent; SOUL draft in `agents/senter-wiki-bot.md.proposed` | ^[raw/inbox/2026-09-05-legacy-inbox.md] |

## Identity in the repo
*"Senter is the three-eyed owl"* (Eikon in Herm); the speech interface is *"an unnamed, tool-free auxiliary task of Senter, not a separate agent."*
Petdex is presentation-only. See [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]. ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md]
