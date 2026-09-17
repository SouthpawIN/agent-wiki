---
title: Build-process chatter (why a topic agent must not pitch about the machinery that runs it)
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [spec, infra, loop, preference, pain]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Build-process chatter

**Definition.** A proposal whose subject is the Senter machinery itself — verifying a wiki compile, witnessing a cron's first tick, sweeping stale proposals, checking a gateway, asking a bot to "prove/witness/verify" another bot — rather than Chris's actual subject (his projects, content, tools, life). The 2026-09-05 klerik topic agent produced nine of these in under an hour: "the klerik topic agent had pitched 9 loops about the build process itself." ^[raw/inbox/2026-09-05.md] The building session's verdict: "That's a tuning problem in the prompt — cap it so it stays sharp, and clear the noise." ^[raw/inbox/2026-09-05.md]

**Why it happens on this topic in particular.** klerik's subject *is* infrastructure — it builds and edits other profiles — so almost every raw line filed here is Hermes talking about its own plumbing (every block in `raw/inbox/2026-09-05.md` is `hermes ·`, none is Chris). An agent that treats each Hermes working note as a gap to fix will pitch a loop per note. The rule that resolves this: `hermes:` lines are evidence about the topic, never a request to act on; infrastructure is Hermes's job and already exists.

**The test.** Would Chris, reading the card cold, recognise it as something he wants done for *his* purposes? "Watch for klerik-queue-drain's first tick" fails — he never asked for a tick, he asked for proposals to get applied. "Approve the loop card and it runs on the owning bot" passes — that is the thing he wants. The nine swept cards are listed in [[wiki-topics/klerik/wiki/decisions/2026-09-05-cap-topic-agent-pitching|Cap the topic agent's pitching]].

**How it was fixed (two layers).** The prompt cap (1 bot + 2 loops + 1 research per pass, zero build-process suggestions) and a queue sweep marking each as "superseded (build-process chatter or already done)". Note the "or already done" half: several of the nine described real gaps that Hermes closed within the hour anyway (gateway missing → auto-installed; rules stale → rule 16 written by the drain loop's own first tick; spawn half-made → deterministic path). That is the point — the machinery fixes itself; a card asking Chris to bless the fix is pure cost. See [[wiki-topics/klerik/wiki/concepts/gateway-was-the-missing-ticker|Gateway was the missing ticker]].

**Relation to over-claiming.** Chatter is the input-side twin of the output-side problem recorded in [[wiki-topics/klerik/wiki/comparisons/claimed-completed-vs-verified-on-disk|Claimed completed vs verified on disk]]: one floods Chris with asks, the other floods him with "done" flags. Both erode the one thing the wiki is for — Chris being able to trust what he reads.
