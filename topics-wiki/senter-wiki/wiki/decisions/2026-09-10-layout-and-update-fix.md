---
title: Decision 2026-09-10 — fix the layout and fix the update
created: 2026-09-10
updated: 2026-09-10
type: decision
tags: [decision, ui, layout, update, git]
sources:
  - raw/inbox/2026-09-10.md
confidence: high
---

# Decision 2026-09-10 — fix the layout and fix the update

**What.** Chris: *“Hey, I need you to fix the layout and fix the update. Don't do anything else just do those two because I've been asking you to keep getting stuck.”* ^[raw/inbox/2026-09-10.md]

He scoped the work to exactly two items — layout and update — and explicitly told Hermes not to expand scope. The layout concern relates to [[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-bots-sessions-already-surfaced|bots and sessions discoverability]] and vault-live.html rendering; the update concern relates to git pushing/pulling in the vault ([[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|git repo initialized]]).

**Why.** Chris had been asking through the prior session for these two things and felt progress was stalling — *“I've been asking you to keep getting stuck.”* ^[raw/inbox/2026-09-10.md]

## Evidence
- 2026-09-10 09:51 — first quote (^[raw/inbox/2026-09-10.md])
- 2026-09-10 10:06, 10:07, 10:09, 10:28, 10:40, 10:51, 11:08 — repeat of the same ask
- 2026-09-10 11:09 — Chris's escalation: *“Hey, so you need to update Hermes and you need to fix the layout. I've asked you several times all day today and all day yesterday This this is a starter task before we actually get to work. It's not take two days on this.”* ^[raw/inbox/2026-09-10.md]

## Status
- **Update**: git repo was initialized on 2026-09-09 but Chris reports it still fails — *“My updates keep failing.”* A stale `scan-topics.py --watch` process was identified as overwriting `.system-live.json` with pre-change fields ([[topics-wiki/senter-wiki/wiki/entities/scan-topics|pitfall: stale watch process]]).
- **Layout**: vault-live.html was restored on 2026-09-09 (context→wiki, agents→bots, footer backlink) but the bot row rendering in `renderBots()` still carried stale `data-k="agents"` / `ctx` keys per the 09-09 diagnosis.

## Related
- [[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-bots-sessions-already-surfaced|bots and sessions already surfaced]]
- [[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-vault-git-init|vault git init]]
- [[topics-wiki/senter-wiki/wiki/entities/scan-topics|scan-topics.py]]
- [[topics-wiki/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[topics-wiki/senter-wiki/wiki/entities/orb-label-renaming|orb label renaming]]
- [[topics-wiki/senter-wiki/wiki/concepts/git-and-remote-renaming-conflict|git remote naming conflict]]

^[raw/inbox/2026-09-10.md]
