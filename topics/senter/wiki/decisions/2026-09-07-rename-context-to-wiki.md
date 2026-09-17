---
title: Rename 'context' references to 'wiki' (proposed 2026-09-07)
created: 2026-09-07
updated: 2026-09-07
type: decision
tags: [decision, infra, preference]
sources: [raw/inbox/2026-09-07.md]
confidence: medium
---

# Rename 'context' references to 'wiki' (proposed 2026-09-07)

During the 2026-09-07 18:10–18:16 state review, Hermes proposed renaming every "context" reference to "wiki" in the vault and Senter docs, and updating topic anatomy to `wiki/` + `skills/` + `bots/` + `loops/`, with pitches bundled. ^[raw/inbox/2026-09-07.md]

Hermes proposed four concrete renames/structure changes:

1. Rename every "context" reference to "wiki" in the vault and Senter docs.
2. Update topic anatomy so each topic is `wiki/` + `skills/` + `bots/` + `loops/`, with pitches bundled.
3. Add explicit skill-vs-bot-vs-loop decision criteria to the architecture and topic-agent.
4. Further detail not visible in this raw item.

## What the wiki already does

- The five-part architecture already calls the topic's knowledge layer a **wiki** (`topics/<t>/`), while "context" appears in older docs as the broader conversation/raw material.
- [[topics/senter/wiki/concepts/context-to-skills-to-bots-to-loops|Context → skills → bots → loops]] preserves the older "context" stage name; this decision would rename that stage to "wiki" or make "wiki" the inclusive layer above it.
- [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure]] already routes discovery through wiki files rather than raw context.

## Why this matters

- "Wiki" is the umbrella term Chris uses for the live knowledge artifact itself.
- "Context" is now overloaded: raw conversations, topic state, and the final compiled artifact.
- A rename reduces ambiguity in bot prompts, loop wording, and new-topic scaffolding.

## Record state

- Proposed by Hermes on Chris's behalf.
- Chris has not yet approved or rejected this rename in the captured raw item.

## Related
- [[topics/senter/wiki/concepts/progressive-disclosure|Progressive disclosure (how the wiki is read)]]
- [[topics/senter/wiki/decisions/2026-09-05-one-agent-per-topic-no-separation|One agent per topic, no separation]]
