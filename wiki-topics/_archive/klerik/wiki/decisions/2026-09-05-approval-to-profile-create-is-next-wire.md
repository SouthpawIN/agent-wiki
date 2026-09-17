---
title: Decision — approving a bot card must run `hermes profile create` via klerik (next wire)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, bot, infra, plan, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Approval → `hermes profile create` via klerik is the next wire

**What.** The next piece of Senter-wiki plumbing to build is the one that turns Chris approving a bot card into an actual `hermes profile create`, executed by klerik. ^[raw/inbox/2026-09-05.md]

**Why.** Today approval "still just renames the file" ^[raw/inbox/2026-09-05.md]. That leaves a gap between the product's promise (proposal → approval → bot exists) and reality (proposal → approval → a file has a new name). klerik's rule 1 says a bot only exists when its smoke turn emits `bridge/loaded`; a rename satisfies none of that.

**When.** Stated 2026-09-05 17:53, in the same breath as reporting that the wiki compile pipeline was live and reloading automatically — i.e. this was named as the immediate successor task once the read side worked. Not yet done at compile time.

**Evidence.** Single assistant-side message, sim 0.12. No Chris quote in the raw record confirms it directly, but it is consistent with his recorded stance that a fix he can't see is not done and that decisions come to him as wiki cards.

**Owner / route.** klerik executes (profile work is always klerik's); weaver owns the card UI that emits the approval; senter tracks. Full mechanics in [[wiki-topics/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]]; the failure mode it closes is laid out in [[wiki-topics/klerik/wiki/comparisons/rename-vs-real-spawn|Rename vs real spawn]].

**Status.** open — proposed, not built. Superseded in sequence by [[wiki-topics/klerik/wiki/decisions/2026-09-05-prove-apply-path-with-one-real-approval|Prove the apply path with one real approval]] (18:18), which widened the target from the bot-card wire to every proposal type's apply step.
