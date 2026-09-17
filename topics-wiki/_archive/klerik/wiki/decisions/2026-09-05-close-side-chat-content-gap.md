---
title: Decision — close the remaining gap between the side chat and the expanded content; make the content wider; don't "highlight the first stop" (Chris, 2026-09-05 19:18)
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, ui, spec]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
contested: true
---
# Decision — close the side-chat ↔ content gap, widen the content (Chris, 19:18)

**What.** At 19:18 on 2026-09-05 Chris — dictating, the only `chris ·` block this topic has received all day — gave two UI rulings about the Senter wiki's expanded-content view:

> "Just highlighting the first stop would shift everything to the right. And one more thing when this expands, when the full content expands, there's still a little more space that I would like closed up between the side chat and the content. You can make that a little bit wider." ^[raw/inbox/2026-09-05.md]

Read as two decisions:

1. **Rejected approach:** whatever "highlighting the first stop" was (see [[topics-wiki/klerik/wiki/queries/what-is-the-first-stop|Query — what is "the first stop"?]]), Chris vetoed it because it "would shift everything to the right." Layout stability wins over the highlight — a highlight that moves the content is not acceptable.
2. **Requested change:** in the *full-content expanded* state, there is "still a little more space" between the side chat and the content; Chris wants it "closed up" by making the content "a little bit wider." The direction is explicit — widen the content pane toward the chat, not move the chat. ^[raw/inbox/2026-09-05.md]

**Why it is worded this way.** This is Chris tuning in micro-increments after seeing a render: "a little more", "a little bit wider" are his normal iteration units; the exact pixel value is his to lock once he sees it. It follows the 19:10 probe reading in which the card's right edge sat at 684 against a chat left edge of 698 — a 14 px gap that passed the machine check ("✓") but which Chris, looking at the real window, judged as too much space ^[raw/inbox/2026-09-05.md] (see [[topics-wiki/klerik/wiki/entities/wiki-diff-mode-card-probe|Wiki diff-mode card probe]]).

**When / owner.** 19:18, 2026-09-05. This is Senter-wiki UI work; the owning bot is weaver, not klerik. The block landed in klerik's inbox at similarity 0.09 — a mis-cut (see [[topics-wiki/klerik/wiki/concepts/watcher-corpus-rebuild|Watcher corpus rebuild]] for the contested "5/5 routes correctly" claim). The decision is recorded here so it is not lost; the canonical home is `topics-wiki/senter-wiki/`.

**Contested.** `contested: true` because the referent of "the first stop" is unresolved and because the 19:20 hermes block that follows reports "gap 4px" ^[raw/inbox/2026-09-05.md] — which may be the fix already applied (14 → 4 px) or a different measurement entirely. No capture of Chris's window confirming the change is in raw.

**Update 19:26 — the gap change is stated as applied.** The 19:26 hermes block reports "**Gap** to the side chat 14 → 4px." ^[raw/inbox/2026-09-05.md] — resolving the ambiguity above: the 19:20 "gap 4px" was the fix, and the 14 px reading from 19:10 was the before. So decision 2 (close up the space) has a numeric after-state. Still `contested: true` on the *proof* standard: the number is a DOM/probe measurement, not a capture of Chris's window, and Chris's phrasing was "a little more … a little bit wider" — 4 px is Hermes's pick, not a value Chris has locked. Decision 1 (no first-stop highlight) remains open on referent ([[topics-wiki/klerik/wiki/queries/what-is-the-first-stop|Query — what is "the first stop"?]]).

**Evidence.** raw/inbox/2026-09-05.md, 19:18 `chris ·` block; context blocks 19:10, 19:11, 19:20, 19:26.
