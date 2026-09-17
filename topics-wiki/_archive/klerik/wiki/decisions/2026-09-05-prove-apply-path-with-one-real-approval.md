---
title: Decision — approve the clearly-described proposals and prove the apply path with ONE real approval
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, plan, infra, bot, loop, timeline]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Prove the apply path with one real approval

**What.** At 18:18 on 2026-09-05 the working session moved from *building* klerik's topic to *exercising* it: "Now the pending proposals — approve the ones that are clearly what Chris described, and prove the apply path with one real approval." ^[raw/inbox/2026-09-05.md] Two rules are packed into that line: (1) proposals that plainly restate something Chris already asked for do not need a fresh decision card — approve them; (2) the approval → apply mechanics are unproven until at least one approval produces a real artifact, so run one for real.

**Why.** The 17:53 message had just named the gap — "Approving a bot card still just renames the file" ^[raw/inbox/2026-09-05.md] — and it is the same gap anser's REFLECT passes escalate ("the reflect loop is producing proposals nobody applies"). Proving the path with one approval is the smallest test that separates a renamed file from a working pipeline. See [[topics-wiki/klerik/wiki/concepts/proposal-apply-path|Proposal apply path]].

**When / who.** Stated 2026-09-05 18:18 by the assistant-side `hermes` sender (sim 0.12 — a weak-similarity filing, assistant text, not Chris's words). It is nonetheless consistent with Chris's recorded standards: a fix he cannot see is not done; "all real", no dummy data.

**What actually happened (observed on disk at compile time, same minute).** The one real approval chosen was the `klerik-queue-drain` loop. `triggers-loops/klerik-queue-drain.md` records `## Applied 2026-09-05 18:18` → "`hermes -p klerik cron create "every 30m" --name klerik-queue-drain` → FAILED", yet the same file's header says `status: LIVE`. `hermes -p klerik cron list` at compile time returns "No scheduled jobs." So the apply path was exercised and it **failed** — which is exactly the information the test was meant to produce. Details and the contested status are in [[topics-wiki/klerik/wiki/entities/klerik-queue-drain-loop|klerik-queue-drain loop]] and [[topics-wiki/klerik/wiki/queries/has-the-apply-path-been-proven|Has the apply path been proven?]].

**Status.** decided and attempted; the proof is negative so far (apply path is broken at the loop → cron step). Successor of [[topics-wiki/klerik/wiki/decisions/2026-09-05-approval-to-profile-create-is-next-wire|Approval → profile create is the next wire]].
