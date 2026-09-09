---
title: Fleet bots touching senter-wiki
aliases:
  - People and bots around the Senter Wiki
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [bot, person]
sources:
  - raw/sources/knowledge/skill-agent-wiki-vault.md
  - raw/inbox/2026-09-05-legacy-inbox.md
  - raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md
  - raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md
  - raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md
confidence: medium
---

# Fleet bots touching senter-wiki

Senter's fleet as it appears in this topic's sources (roster of 9 on 2026-09-05; bots, not "agents"). ^[raw/inbox/2026-09-05-legacy-inbox.md]

| Bot | Role seen here | Notes |
|---|---|---|
| **senter** | coordinator; the ONE profile running the topic loops for now ("per-topic profiles come later, when a topic earns a bot") | [[topics/senter-wiki/wiki/decisions/2026-09-05-per-message-watcher-one-profile-one-card|decision]] ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **anser** | redundancy gate / "native before custom": asked what Hermes already ships, then VERIFY read-only — "Anser hallucinates features". `hermes -p anser -z "<q>. Plain text, no MEDIA, no TL;DR — internal fleet conversation."` (~15 s); SOUL forces Discord TL;DR+MEDIA otherwise. Co-author of the GOOP whitepaper. | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md] |
| **looker** | UI-QA / research: receives the instant research dispatch when a new subject scaffolds a topic | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **klerik** | profile factory; example BOTS row hovered in the editor verification (`#bots/klerik`, SOUL.md loaded) | ^[raw/sources/knowledge/ref-vault-live-ui-2026-09-03.md] |
| **teknium** | Hermes builder; 09-02 note that `hermes auth spotify` was never run | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **weaver** | wiki UI owner (memory) | — |
| **senter-wiki-bot** | PROPOSED by the [[topics/senter-wiki/wiki/entities/umbrella|umbrella]]: 4 skills, no agent | awaiting Chris ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **sidebar** (proposed SOUL) | see [[topics/senter-wiki/wiki/entities/sidebar-agent|sidebar agent]] | awaiting approval ^[raw/inbox/2026-09-05-legacy-inbox.md] |

Per the concept page, Bot = "specialised sub-worker of that Agent (a profile with SOUL.md)". ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

Roster rendering: the BOTS section of [[topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]] sorts bots by SOUL role text, not title ([[topics/senter-wiki/wiki/concepts/similarity-ranking|similarity and ranking]]).

## Folded from `people-and-bots-in-this-topic`

### Chris (sovthpaw)
Owner. Steers the UI live by voice from the Hermes sidebar; co-author of the GOOP whitepaper (as *sovthpaw*, with Anser, 2026-07-04). Vocabulary he fixed:
**Agent** = the agentic harness (Hermes Agent); **Bot** = specialised sub-worker (a profile with SOUL.md); **sub-agents** = drones. Working style:
[[topics/senter-wiki/wiki/concepts/chris-ui-working-rules|Chris's UI working style]] (now [[topics/senter-wiki/wiki/concepts/chris-ui-working-rules|Chris's UI working rules]]). ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md] ^[raw/sources/knowledge/ref-vault-live-concept-2026-09-03.md]

### Extra roster detail (evidence column)
| Bot | Role here | Evidence |
|---|---|---|
| **senter** | the one profile running all loops (watcher, worker, umbrella, compile) — *"one senter profile running the loops (per-topic profiles come later, when a topic earns a bot)"* | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **anser** | hallucinates features → keep a "claimed but did not verify" list under `.system/anser/` | ^[raw/sources/knowledge/skill-agent-wiki-vault.md] |
| **looker** | receives the new-subject research dispatch; writes `.system/research.md` + Status | ^[raw/inbox/2026-09-05-legacy-inbox.md] |
| **weaver** | owns `verify-nightly` (loop page) and the wiki UI per memory | loops/verify-nightly.md |
| **klerik** | profile factory — the only bot allowed to edit other profiles (fleet rule) | system prompt |
| **senter-wiki-bot** (PROPOSED) | umbrella's promotion: 4 skills, no agent; SOUL draft in `agents/senter-wiki-bot.md.proposed` | ^[raw/inbox/2026-09-05-legacy-inbox.md] |

### Identity in the repo
*"Senter is the three-eyed owl"* (Eikon in Herm); the speech interface is *"an unnamed, tool-free auxiliary task of Senter, not a separate agent."*
Petdex is presentation-only. See [[topics/senter-wiki/wiki/entities/agent-wiki-repo|agent-wiki repo]]. ^[raw/sources/knowledge/agent-wiki-repo/goop-whitepaper.md]

## Absorbed
- `entities/people-and-bots-in-this-topic` — 2026-09-05 → archived at `topics/_archive/wiki-dedupe/senter-wiki/entities/people-and-bots-in-this-topic.md`
