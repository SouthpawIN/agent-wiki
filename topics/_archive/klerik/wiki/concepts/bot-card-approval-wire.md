---
title: Bot-card approval wire (card → hermes profile create)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [bot, ui, infra, plan, pain]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Bot-card approval wire

**The idea.** In the Senter wiki a proposed bot appears as a *card*. Chris approving that card is supposed to be the moment the bot gets made. The wire is the path from that approval to a real, running Hermes profile — which is klerik's job.

**Current state (2026-09-05).** The wire is not connected: "Approving a bot card still just renames the file; the actual `hermes profile create` via klerik is the next wire." ^[raw/inbox/2026-09-05.md] Approval today is a filesystem rename of the card; nothing spawns. In the same message the compile pipeline was described as working ("senter entities already landing: chris, anser, klerik … the corpus reloads automatically") ^[raw/inbox/2026-09-05.md] — so the read side of the wiki is live, the act side is not.

**Why this is a pain, not a nit.** Chris's standing expectation is that a fix he can't see isn't done, and that "routed/queued" reads as stalling. An approval that only renames a file is exactly the "described but not run" failure klerik's authoring rule 1 exists to prevent: *a bot is spawned when it runs, not when its files exist* (paladin was "spawned" twice before it existed). See [[topics/klerik/wiki/comparisons/rename-vs-real-spawn|Rename vs real spawn]].

**What the wire has to do.** Approval event → klerik runs the spawn checklist ([[topics/klerik/wiki/entities/klerik|klerik]] README): `hermes profile create <name>`, symlink `.env` + `auth.json`, write SOUL/AGENTS from the card's role text, set voice + skin, alias + bridge token + `plugins.enabled`, smoke `-q` until `bridge/loaded`, log to `.system/session.md`, update the roster. Decision record: [[topics/klerik/wiki/decisions/2026-09-05-approval-to-profile-create-is-next-wire|Approval → profile create is the next wire]]. Skill draft: `topics/klerik/skills/bot-card-approval-spawn/SKILL.md`.

**Update 18:18 (2026-09-05).** The session moved to testing: "approve the ones that are clearly what Chris described, and prove the apply path with one real approval." ^[raw/inbox/2026-09-05.md] The bot-card branch itself was not the one tested — the loop branch was, and its `cron create` FAILED while the file was marked LIVE. The bot-card wire is one branch of the wider [[topics/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]]; result tracked in [[topics/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]].

**Update 18:20–18:42 (2026-09-05) — the wire ran, and found its real obstacle.** The card → `hermes profile create` step now exists in the bridge and fired for `senter-wiki-bot`. It got as far as a profile dir, config, skills and alias, then "the protected-file guard blocked it" and the result was "half-made (default SOUL, no AGENTS)" ^[raw/inbox/2026-09-05.md]. Wire v2 ("the new deterministic path") has the bridge write SOUL/AGENTS from the approved card and leaves klerik the unprotected finish — [[topics/klerik/wiki/concepts/deterministic-apply-path|Deterministic apply path]], root cause [[topics/klerik/wiki/concepts/protected-file-guard|Protected-file guard]]. The paragraph "What the wire has to do" above is therefore partly superseded: SOUL/AGENTS are no longer klerik's to write.
