---
title: Approval security gate (why the deterministic re-run also stopped — rename + POST that writes SOUL reads as a protected-file write)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [infra, bot, pain, decision, spec]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Approval security gate

**Definition.** The second layer that stopped the `senter-wiki-bot` spawn on 2026-09-05. The first layer was the [[topics-wiki/klerik/wiki/concepts/protected-file-guard|protected-file guard]] inside klerik's own headless session (it could not write another profile's SOUL/AGENTS). The fix was the [[topics-wiki/klerik/wiki/concepts/deterministic-apply-path|deterministic apply path]] — let the bridge write SOUL/AGENTS itself. At 18:47 the *building session's* security gate blocked that too: "The security gate is now blocking the approval re-run (it sees a rename + a POST that writes SOUL files as a protected-file write). I'll stop pushing on that path and wait for you — it needs your nod once." ^[raw/inbox/2026-09-05.md]

**What it saw.** The re-run is one shell command: `mv topics-wiki/senter-wiki/agents/senter-wiki-bot.md … senter-wiki-bot.md.proposed && python3 -c "<POST /approve to the bridge>"`. The bridge's approve handler writes `~/.hermes/profiles/senter-wiki-bot/SOUL.md` and `AGENTS.md`. The gate reasons about the *effect* of the command, not the process boundary, so "a rename plus a request that ends in a SOUL.md write" is classed as a protected-file write and needs a human OK in that session — exactly the same rule that stopped klerik. The bridge feed records the terminal call with `ok: false` (events.jsonl, ts 1788652103) and the card is now sitting as `senter-wiki-bot.md.proposed` again, i.e. the rename half of the command ran and the approve half did not. The card is therefore back to *pending* in the wiki feed.

**Why this is the same root cause, not a new bug.** Both layers enforce one rule: *no Hermes process writes a profile's SOUL.md / AGENTS.md without a human nod in the session that does the write*. Moving the write from klerik to the bridge changed who holds the pen, not whether the gate applies. The deterministic path is still correct (it removes LLM authoring from the protected step and makes the content the exact approved card text); what it cannot remove is one click from Chris.

**Where the one click lives.** Two doors, both listed under "Blocked on you (one click each, not a decision)": approve the card in the wiki feed, or say "go" ^[raw/inbox/2026-09-05.md]. Approving in the wiki is the intended door — that is the whole point of cards being approvals ([[topics-wiki/klerik/wiki/concepts/bot-card-approval-wire|Bot-card approval wire]]). Whether the wiki-feed approval itself triggers a gate prompt somewhere is untested; the bridge runs under launchd, not inside a CLI session, so it may not.

**Consequence for klerik.** klerik never sees this gate — it stopped authoring protected files at 18:42. Its lane is now: after the bridge has written SOUL/AGENTS (post-nod), run voice/skin/tui/alias/describe and the read-only gap report. Until the nod, klerik has nothing to do on this card. See [[topics-wiki/klerik/wiki/queries/what-is-blocked-on-chris|What is blocked on Chris?]] and the decision record [[topics-wiki/klerik/wiki/decisions/2026-09-05-stop-pushing-wait-for-chris-nod|Stop pushing; wait for Chris's nod]].
