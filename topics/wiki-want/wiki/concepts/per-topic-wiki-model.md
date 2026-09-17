---
title: Per-topic wiki model
created: 2026-09-07
updated: 2026-09-07
type: concept
tags:
  - concept
  - plan
  - infra
  - bot
  - skill
  - loop
sources:
  - raw/inbox/2026-09-07.md
confidence: high
---

# Per-topic wiki model

Chris wants each topic to own its own wiki, skills, bots, and loops as a self-contained package. The context section currently used for the topic is expected to become a full wiki for that topic. This means a topic should be readable and steerable from its own wiki rather than from a separate context layer.

Chris also wants skills and bots proposed together whenever both are needed. That keeps the topic's build surface coherent: an idea becomes either a repeatable skill or a persisted bot, with a clear cutoff between them. He imagines a clean definition for when something is better as a skill and when it needs a bot, based on whether the work needs persistence and intelligence or can be added to existing intelligence, an existing bot, or to Hermes itself. He is also looking for filesystem simplification while keeping the backing GitHub repo as the stable backbone for the theories and structure behind this.

## Evidence

- "I want once again rename everything that is context into wiki ... each topic will have its own wiki, its own skills, its own bots and its own loops." ^[raw/inbox/2026-09-07.md]
- "I want the skills and the bots to be proposed simultaneously if both are needed." ^[raw/inbox/2026-09-07.md]
- "I want there to be a queer definition on the difference between what would make a good skill and what would make a good bot, you know, whether it's something that needs persistence and intelligence or if it's an ability that can be more efficiently added to existing intelligence, existing bot or to Hermes itself." ^[raw/inbox/2026-09-07.md]
- "Also I was thinking that we can probably simplify instead of a file system." ^[raw/inbox/2026-09-07.md]

## Related

- [[decisions/rename-context-to-wiki|Rename context to wiki]]
- [[decisions/skill-versus-bot-gate|Skill-versus-bot gate]]
