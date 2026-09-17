---
title: Comparison — file-rename approval vs a real klerik spawn
created: 2026-09-05
updated: 2026-09-05
type: comparison
tags: [bot, infra, pain, spec]
sources: [raw/inbox/2026-09-05.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: medium
---
# File-rename approval vs a real klerik spawn

The two things "approving a bot card" can currently mean, side by side. Today it is the left column: "Approving a bot card still just renames the file" ^[raw/inbox/2026-09-05.md]. The right column is klerik's spawn checklist and the definition of done in authoring rule 1.

| | Rename-only (today) | Real spawn via klerik (target) |
|---|---|---|
| Trigger | Chris approves the card in the wiki | same |
| Filesystem | card file renamed (e.g. proposed → approved) | card renamed AND profile dir created under `~/.hermes/profiles/<name>/` |
| `hermes profile create` | not run | run, then `.env` + `auth.json` symlinked |
| SOUL / AGENTS | none | written from the card's role text; owns/neighbors named (rule 9) |
| Voice / skin / TUI theme | none | set per archetype table |
| Bridge | none | alias + token symlink + `plugins.enabled` |
| Proof the bot exists | none — file present ≠ usable (rule 8) | `hermes -p <name> -q` emits `bridge/loaded` (rule 1) |
| Logging | none | `.system/session.md` dated entry + roster row |
| What Chris sees | a card changed state; nothing else happens | the new bot answers; card shows running |

**Same shape, different artifact (added 18:18).** The loop branch reproduced the left column on 2026-09-05: `klerik-queue-drain` was approved, its `cron create` FAILED, and the file was still stamped `status: LIVE` — a flag set by the apply step instead of by proof. Generalised in [[topics-wiki/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]].

**Why the distinction is load-bearing.** The fleet already paid for this once: paladin "was 'spawned' twice before it existed" (rule 1's origin). The topic build-out note's insistence on "all real" ^[raw/inbox/2026-09-05-legacy-inbox.md] is the same principle applied to topics. Details: [[topics-wiki/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]]; the bot that performs the right column: [[topics-wiki/klerik/wiki/entities/klerik|klerik]].

**Third column appeared 18:42.** Between "rename only" and "real spawn via klerik" there is now a middle state observed in the wild — *half-made*: profile dir, config, skills, alias present; SOUL.md still the stock default; no AGENTS.md; card stamped "Profile created" ^[raw/inbox/2026-09-05.md]. It fails rule 8 (on disk ≠ connected) in a new way: most of the disk is right. Detailed in [[topics-wiki/klerik/wiki/comparisons/klerik-authored-vs-bridge-authored-profile|klerik-authored vs bridge-authored profile]] and [[topics-wiki/klerik/wiki/entities/senter-wiki-bot-spawn|senter-wiki-bot spawn]].
