---
title: Librarian (progressive discovery loop)
created: 2026-09-07
updated: 2026-09-07
type: entity
tags: [bot, loop, spec, idea]
sources: [raw/inbox/2026-09-07-from-hermes-agent.md]
confidence: medium
---

# Librarian (progressive discovery loop)

The **librarian** is [[topics/senter/wiki/entities/anser|anser]]'s REFLECT-loop proposal for a proactive watch/discovery loop over the whole vault. Chris, 2026-09-07 18:15: **\"We can use progressive disclosure just like how skills are discovered by first through the font matter and then it could dig deeper. We can have a librarian watching the whole thing and progressively discovering, wiki skills, bots, and loops.\"**

## What it adds to the existing model

- **Watch layer, not just read layer:** Same frontmatter-first ordering (INDEX → file → section) but also watches every topic and cross-topic signal.
- **Discovery order:** frontmatter → page → section → artifact, applied to skills, bots, and loops.
- **Outcome:** instead of flooding Chris with everything, proposes exactly one next artifact when its turn in the discovery chain matches.

## Ties to standing architecture

- [[topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|One agent per topic, no separation]] defines what a topic agent outputs; the librarian is the cross-topic coordinator for those outputs.
- [[topics/senter/wiki/entities/umbrella|umbrella]] already owns cross-topic governance; the librarian is the progressive-discovery view on top of umbrella output.
- [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]] is the artifact pipeline; the librarian decides which stage to surface next.

## Open questions

- Whether the librarian is a separate bot, a policy inside umbrella, or a loop on existing fleet bots.
- Whether discovery should also propose de-dupes or merges, not just new skills/bots/loops.

## Status

This is a **proposed** concept from the REFLECT loop (anser's 2h repetition detectors). It has not yet been spun up as a bot or loop. See [[topics/senter/wiki/concepts/librarian-progressive-discovery|Librarian as progressive discovery]] for the reframed view.