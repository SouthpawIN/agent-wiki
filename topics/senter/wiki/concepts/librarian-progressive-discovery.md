---
title: Librarian as progressive discovery (Chris, 2026-09-07)
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [idea, decision, skill, bot, loop, spec]
sources: [raw/inbox/2026-09-07.md]
confidence: high
---

# Librarian as progressive discovery (Chris, 2026-09-07)

On 2026-09-07 at 18:15, Chris reframed the existing progressive-discovery rule as a governance actor, not just a read-time policy: ^[raw/inbox/2026-09-07.md]

> "We can use progressive disclosure just like how skills are discovered by first through the font matter and then it could dig deeper. We can have a librarian watching the whole thing and progressively discovering, wiki skills, bots, and loops."

This turns [[topics/senter/wiki/concepts/progressive-disclosure|progressive disclosure]] from a passive read protocol into a watch loop that progressively surfaces actionable artifacts across the vault.

## What it adds to the existing model

- **Watch layer, not just read layer:** same frontmatter-first ordering, but the librarian also watches every topic and cross-topic signal.
- **Discovery order:** frontmatter → page → section → artifact, applied to skills, bots, and loops the way it already applies to wiki pages.
- **Outcome:** instead of flooding Chris with everything, the librarian proposes exactly one next artifact when its turn in the discovery chain matches.

## Ties to standing architecture

- [[topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|One agent per topic, no separation]] defines what a topic agent outputs; the librarian is the cross-topic coordinator for those outputs.
- [[topics/senter/wiki/entities/umbrella|umbrella]] already owns cross-topic governance; this concept positions the librarian as the progressive-discovery view on top of umbrella output.
- [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]] is the artifact pipeline; the librarian decides which stage to surface next.

## Open
- Whether the librarian is a bot, loop, or policy inside umbrella.
- Whether discovery should also propose de-dupes or merges, not just new skills/bots/loops.

## Related
- [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure (how the wiki is read)]]
- [[topics/senter/wiki/decisions/2026-09-05-preempt-decisions-complete-the-incomplete|Preempt decisions: complete the incomplete]]
