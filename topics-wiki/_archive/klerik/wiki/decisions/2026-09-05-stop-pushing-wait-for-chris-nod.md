---
title: Decision — stop pushing on the approval re-run; wait for Chris's one nod (2026-09-05 18:47)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, bot, infra, preference]
sources: [raw/inbox/2026-09-05.md]
confidence: high
---
# Decision — stop pushing; wait for the nod

**What.** At 18:47 on 2026-09-05 the building session stopped trying to get the `senter-wiki-bot` approval through by machinery alone: "I'll stop pushing on that path and wait for you — it needs your nod once." ^[raw/inbox/2026-09-05.md] It then handed Chris a stand-up: a **Completed** list, and a **Blocked on you (one click each, not a decision)** list of three items — the senter-wiki-bot card, the vault `AGENTS.md`, and the Spotify client ID.

**Why.** Two attempts in 27 minutes hit the same wall from two sides: klerik's headless run (18:20–18:42, [[topics-wiki/klerik/wiki/concepts/protected-file-guard|protected-file guard]]) and the bridge's deterministic re-run (18:47, [[topics-wiki/klerik/wiki/concepts/approval-security-gate|approval security gate]]). Trying a third route would be routing around a guard that exists on purpose — the fleet's standing rule (klerik rule 7: never route around the gate) applies to the session as much as to klerik. The honest move was to name the click and stop.

**How it was framed to Chris.** Deliberately as "one click each, not a decision" — the decision (approve the bot) was already made when the card was approved the first time; what is left is a security confirmation. This matches Chris's standing approval ("act first; confirm only spending/deletion/publishing") — a SOUL write on a new profile is none of those, so the session treats the gate as friction to surface, not a question to re-ask.

**Tension with Chris's expectations (kept, dated).** Chris reads "routed/queued" as stalling and wants first action in seconds. A "blocked on you" list is a stall from his side of the screen even when it is the correct stopping point. The mitigation the session chose: make the click trivial (approve the card in the feed, or say "go") and be exact about what will happen when he does. Whether that lands well is not in the raw yet.

**What flips when he nods.** The bridge writes SOUL/AGENTS from the approved card text, klerik runs the narrow finish prompt, and [[topics-wiki/klerik/wiki/queries/did-the-deterministic-rerun-complete|Did the deterministic re-run complete?]] can be answered by proof (SOUL ≠ default, `-q` smoke emits `bridge/loaded`). Full list: [[topics-wiki/klerik/wiki/queries/what-is-blocked-on-chris|What is blocked on Chris?]].
