---
title: Orb label rename completion — mkTopic + all downstream refs renamed
created: 2026-09-09
updated: 2026-09-09
type: decision
tags:
  - ui
  - decision
  - rename
confidence: high
sources:
  - raw/inbox/2026-09-08.md
  - raw/inbox/2026-09-09.md
---

Decision 2026-09-09 — orb rename completion (mkTopic + all downstream refs)
What
The orb terminology rename from `context/ctx` to `wiki` and from `agents` to `bots` was completed as a paired fix: the mkTopic factory array and all downstream render call sites were changed together.

Root cause/why paired
Earlier passes had renamed some keys but left stale references in `mkTopic()` and `renderBots()`. Because the static baked rows and dynamic JS factory must match, partial rename produced mismatched orb counts/labels.

Changes
- `mkTopic()` array: `['ctx','skills','agents','loops']` → `['wiki','skills','bots','loops']`.
- Three `renderBots()` call sites renamed `ctx` → `wiki` and `agents` → `bots` where those row shapes create orb objects.
- Four downstream references updated to the new keys where counts/labels are rendered.
- One stale comment changed from "botActivity marks agents" to "botActivity marks bots".

Outcome
- Static rows, dynamic factory, hover/peek labels, and row metadata all read the same keys.
- No partial rename residue remains in the documented rename surface.

See also
[[topics-wiki/senter-wiki/wiki/entities/orb-label-renaming|orb label renaming]]
[[topics-wiki/senter-wiki/wiki/decisions/2026-09-09-orb-fix-completion|2026-09-09 orb fix completion]]

^[raw/inbox/2026-09-08.md]
^[raw/inbox/2026-09-09.md]
