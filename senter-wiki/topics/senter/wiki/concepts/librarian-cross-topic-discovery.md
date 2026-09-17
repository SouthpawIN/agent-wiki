---
title: Librarian as cross-topic discovery, not only read-time policy
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [spec, bot, loop, idea, decision]
sources: [raw/inbox/2026-09-07-from-hermes-agent.md, raw/inbox/2026-09-07-from-turbofit.md, raw/inbox/2026-09-07.md]
confidence: medium
---

# Librarian as cross-topic discovery, not only read-time policy

Chris, 2026-09-07 18:15: **"We can use progressive disclosure just like how skills are discovered by first through the font matter and then it could dig deeper. We can have a librarian watching the whole thing and progressively discovering, wiki skills, bots, and loops."** ^[raw/inbox/2026-09-07-from-hermes-agent.md]

## What changed
- Earlier progressive disclosure was framed mainly as a **read protocol** — INDEX first, then file, then one section [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure (how the wiki is read)]].
- This 2026-09-07 statement redefines the librarian as an **active watch/discovery loop** across the whole vault, not a read-time helper.

## What the librarian would cover
- wiki sections
- skills
- bots
- loops

## Where it sits in current architecture
- [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure]] supplies the human-style read path.
- [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]] is the artifact pipeline; the librarian decides which stage to surface next.
- [[topics/senter/wiki/entities/umbrella|umbrella]] already owns cross-topic governance; this concept positions the librarian as the discovery/surfacing view on top of umbrella output, not necessarily a replacement.

## Open questions
- Is the librarian a separate bot, a policy inside umbrella, or a loop on existing fleet bots?
- How does it prevent duplicate pitching when one topic agent and umbrella both see the same signal?
