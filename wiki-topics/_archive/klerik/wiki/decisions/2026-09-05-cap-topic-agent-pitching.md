---
title: Decision — cap the klerik topic agent's pitching and clear the noise (2026-09-05 18:53)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, infra, loop, pain, spec]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Decision — cap the topic agent's pitching; clear the noise

**What.** At 18:53 on 2026-09-05 the building session ruled that this topic's agent was producing too many proposals: "The klerik agent is over-pitching (9 loops from one topic). That's a tuning problem in the prompt — cap it so it stays sharp, and clear the noise:" ^[raw/inbox/2026-09-05.md] Two actions follow from one sentence: (1) change the agent prompt so it cannot emit that volume again — a hard cap; (2) sweep the nine already-pitched loop cards out of the queue.

**Why.** The nine loops were all about the build machinery, not about klerik's subject — see [[wiki-topics/klerik/wiki/concepts/build-process-chatter|Build-process chatter]]. The 18:58 close-out names the fault plainly: "Signal over noise: the klerik topic agent had pitched 9 loops about the build process itself." ^[raw/inbox/2026-09-05.md] Chris's standing expectation is that decisions reach him as wiki cards and that repeated or hollow asks make him furious; nine cards that each ask him to approve a watcher-of-the-watcher are the opposite of "fewer, sharper".

**What was cleared (verified in `.system/queue.md` at 19:07).** All nine are ticked `[x]` and stamped "superseded 2026-09-05 (build-process chatter or already done)": first-tick-witness, one-click-nod-card, klerik-rules-sync, spawn-proof-gate, agents-md-veto-to-soul, thin-topic-compile-sweep, gateway-up-first-tick, klerik-queue-drain-fix, apply-path-verifier. Their `triggers-loops/*.md.proposed` files are gone from `triggers-loops/` — only `klerik-queue-drain.md` remains. The one loop that survived is the one that serves klerik's actual job: [[wiki-topics/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain]].

**The cap as it now reads (this agent's own prompt).** At most 1 bot + 2 loops + 1 research per pass; zero suggestions about the build process (verifying the wiki, sweeping proposals, checking crons, "want X to prove/witness/verify Y"); reuse fleet bots; "Fewer, sharper suggestions beat many." Raw lines marked `hermes:` are evidence, never requests. This page is written under that cap.

**Consequence for klerik.** The 18:53 ruling is a second tuning of the same loop that anser's REFLECT passes already flagged from the other side ("the reflect loop is producing proposals nobody applies"): too many proposals in, none applied, is noise; a few proposals in, each applied and proven, is the product. Compare with the earlier over-claiming problem in [[wiki-topics/klerik/wiki/comparisons/claimed-completed-vs-verified-on-disk|Claimed completed vs verified on disk]] — both are the same failure of signal, once on the input side and once on the output side.
