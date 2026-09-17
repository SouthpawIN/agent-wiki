---
title: Wiki diff-mode card probe (19:10–19:20, 2026-09-05 — card edge 684 vs chat 698, 64 pages, badge +3 −1, 256 headings, gap 4px)
created: 2026-09-05
updated: 2026-09-05
type: entity
tags: [ui, infra, timeline, spec]
sources: [raw/inbox/2026-09-05.md]
confidence: medium
---
# Wiki diff-mode card probe (19:10 → 19:20)

**What it is.** A short run of numeric verification passes against the Senter wiki's live view, done by a Hermes session in the ten minutes after the klerik close-out. Four blocks landed in klerik's inbox (three `hermes ·`, one `chris ·`) even though the subject is the wiki UI, not klerik — they scored 0.06–0.09 similarity, the lowest of the day ^[raw/inbox/2026-09-05.md]. Recorded here as evidence; the UI itself is weaver's, and the Chris ruling it produced is in [[wiki-topics/klerik/wiki/decisions/2026-09-05-close-side-chat-content-gap|Decision — close the side-chat ↔ content gap]].

**Timeline (all 2026-09-05).**

| time | who | what was measured / said |
|---|---|---|
| 19:10 | hermes | "Card right edge 684 < chat left 698 ✓, wiki mounted with 64 pages, title badge `+3 −1` ✓. The diff block itself had already settled by the time I sampled (6s) — check faster:" ^[raw/inbox/2026-09-05.md] |
| 19:11 | hermes | "Proof: 1 page block in diff mode with 2 green added lines and 1 red removed line, card open. Remove the probe, record, and reload:" ^[raw/inbox/2026-09-05.md] |
| 19:18 | **chris** | Veto of "highlighting the first stop" (would shift everything right); wants the space between side chat and expanded content closed up, content "a little bit wider." ^[raw/inbox/2026-09-05.md] |
| 19:20 | hermes | "256 rendered headings (189 h2), 404 list items, only 3 real code blocks, gap 4px. Now verify the orb anchoring numerically:" ^[raw/inbox/2026-09-05.md] |
| 19:26 | hermes | "Proof: third dot centre x=562 before and after bloom." and "**Gap** to the side chat 14 → 4px." ^[raw/inbox/2026-09-05.md] — the orb-anchoring probe announced at 19:20 passed (bloom does not move the dot column), and the side-chat gap is stated as before/after. |

**What the numbers say.**
- *Layout invariant checked:* the open card must not overlap the side chat — right edge 684 < chat left 698 passed. Chris then said the resulting gap is too big; the machine check measured non-overlap, not "looks right." That is the recurring gap between numeric ✓ and Chris's eye.
- *Diff mode:* the wiki renders a page's change as a diff block (green added / red removed) with a title badge summarising it (`+3 −1`). The block "settled" within 6 s, so the probe had to sample faster to catch it in diff state; the 19:11 proof caught 2 added + 1 removed lines on one page block ^[raw/inbox/2026-09-05.md].
- *Probe hygiene:* the probe was temporary — "Remove the probe, record, and reload" — i.e. no probe code left in the UI, result recorded, then a clean reload. Consistent with the fleet rule that `desktop_preview open` stacks tabs, so reload = close all, open one.
- *Content shape (19:20):* 64 pages mount as 256 headings (189 of them h2), 404 list items, only 3 real code blocks — a mostly-prose vault, which is why heading/list styling matters far more than code styling. Gap reading 4 px.
- *Orb anchoring (19:26):* "third dot centre x=562 before and after bloom" ^[raw/inbox/2026-09-05.md] — the locked rule that orbs are static/column-aligned and only the hover stage grows them held numerically: bloom (the 22 → 38 px hover growth) does not shift the column. Same caveat as every number here: DOM measurement, not a capture of Chris's window.
- *Gap closed (19:26):* "14 → 4px" — the change Chris asked for at 19:18, applied and measured; whether 4 px is what his eye wants is his call ([[wiki-topics/klerik/wiki/decisions/2026-09-05-close-side-chat-content-gap|Decision — close the side-chat ↔ content gap]]).
- *Misroute class named (19:26):* the same block introduces `BRIEF.md` anti-scope routing with the test "'hover over the third dot' → senter-wiki .32" — i.e. precisely this probe's subject now has a rule sending it to senter-wiki, not here ([[wiki-topics/klerik/wiki/concepts/brief-pre-prompting-layer|BRIEF.md pre-prompting layer]]).

**Relevance to klerik.** None directly; klerik's own build finished at 18:58 ([[wiki-topics/klerik/wiki/comparisons/18-47-standup-vs-18-58-closeout|18:47 vs 18:58]]). The value of this page is (a) preserving Chris's one dictated ruling of the day, and (b) a concrete misroute sample for [[wiki-topics/klerik/wiki/concepts/watcher-corpus-rebuild|Watcher corpus rebuild]].
