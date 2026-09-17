---
title: Librarian — progressive disclosure of wiki skills, bots, and loops
created: 2026-09-07
updated: 2026-09-07
type: concept
tags: [spec, skill, ui, preference]
sources:
  - raw/inbox/2026-09-07-from-senter.md
confidence: medium
aliases:
  - "Progressive disclosure for wiki entities"
  - "Wiki librarian"
---

# Librarian — progressive disclosure of wiki skills, bots, and loops

## The ask (Chris, 2026-09-07 18:15)
> "We can use progressive disclosure just like how skills are discovered by first through the font matter and then it could dig deeper. We can have a librarian watching the whole thing and progressively discovering, wiki skills, bots, and loops."

This extends the existing [[topics-wiki/senter-wiki/wiki/concepts/progressive-disclosure|progressive-disclosure]] reading protocol — INDEX -> file -> section — into the wiki surface itself: when browsing the SKILLS, BOTS, and LOOPS sections, reveal the front-matter summary first, then allow drilling deeper per item. The "librarian" is the metaphorical watcher that progressively discovers and surfaces wiki entities. ^[raw/inbox/2026-09-07-from-senter.md]

## What it maps to today
- [[topics-wiki/senter-wiki/wiki/entities/senter-wiki-skills|Topic skills]] are already discovered via front-matter (the scanner reads `topics-wiki/*/skills-capabilities/SKILL.md`) — see [[topics-wiki/senter-wiki/wiki/concepts/progressive-disclosure|progressive disclosure]].
- [[topics-wiki/senter-wiki/wiki/entities/fleet-bots|Fleet bots]] and [[topics-wiki/senter-wiki/wiki/entities/topic-wiki-compile-loop|topic-wiki compile loop]] (loops) currently surface as rows in the wiki; a librarian would progressively disclose each.
- [[topics-wiki/senter-wiki/wiki/concepts/approval-policy|Approval policy]]: skills auto-apply, bots-profiles/loops stay `.proposed` — the librarian would respect that boundary.

## Related
- [[topics-wiki/senter-wiki/wiki/concepts/progressive-disclosure|Progressive disclosure]]
- [[topics-wiki/senter-wiki/wiki/concepts/pane-driving-and-verification|Verification contract]]
- [[topics-wiki/senter-wiki/wiki/concepts/one-page-navigation-model|One-page navigation]]
