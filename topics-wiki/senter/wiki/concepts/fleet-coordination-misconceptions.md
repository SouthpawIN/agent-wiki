---
title: Fleet-coordination misconceptions (contested)
created: 2026-09-08
updated: 2026-09-08
type: concept
tags: [concept, pain, policy]
sources: [raw/inbox/2026-09-07.md]
confidence: high
contested: true
---

# Fleet-coordination misconceptions (contested)

This page records misunderstandings about how the Senter fleet works that have been corrected in the wiki. The `contested: true` flag indicates this is a living record of things that were once believed but were corrected.

## The "librarian as passive reader" misconception

**Wrong belief (2026-09-07 18:10):** The librarian was only a read-time progressive disclosure feature.

**Correction (2026-09-07 18:15):** Chris reframed the librarian as an **active watch/discovery loop** over the whole vault that progressively discovers wiki skills, bots, and loops. It is NOT only a passive read-time policy.

- [[topics-wiki/senter/wiki/concepts/librarian-progressive-discovery|Librarian as progressive discovery]] captures the corrected view.
- [[topics-wiki/senter/wiki/concepts/progressive-disclosure|Progressive disclosure]] remains the read protocol, but with an active watch layer added.

## The "governance orphaned" misconception

**Wrong belief (recorded in wiki at 18:53):** The umbrella script was deleted, so governance had no owner.

**Correction (2026-09-05 18:53):** The [[topics-wiki/senter/wiki/entities/umbrella|umbrella]] was never deleted; it still runs every 30 minutes. The wiki record was wrong because it inferred deletion from the worker/compiler collapse.

- The "governance has no owner" pitch was the agent repeating the wrong memory.
- Fixed by [[topics-wiki/senter/wiki/concepts/fix-the-record-not-the-pitch|fixing the record]].
- [[topics-wiki/senter/wiki/concepts/verify-apply-paths-and-watchpaths-landed|Verify apply paths and WatchPaths landed]] tracks whether the WatchPaths event mechanism has fully landed.

## Key lesson

When a fleet bot pitches the same thing repeatedly, check the wiki pages it's drawing from. The wiki IS the agent's memory. A false statement in a page is not a bug—it is a recurring wrong card to Chris, on every run, until the page is corrected.

## Related

- [[topics-wiki/senter/wiki/concepts/fix-the-record-not-the-pitch|Fix the record, not the pitch]]
- [[topics-wiki/senter/wiki/decisions/2026-09-05-wiki-is-hermes-memory-layer|Wiki is Hermes's memory layer]]
- [[topics-wiki/senter/wiki/entities/topic-agent|topic agent]]