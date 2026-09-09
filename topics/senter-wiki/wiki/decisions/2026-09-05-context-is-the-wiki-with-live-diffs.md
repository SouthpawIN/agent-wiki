---
title: "Decision 2026-09-05 19:06: CONTEXT is the wiki itself, edited live with GitHub-style diffs — no counts, no index list"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, ui, preference, spec]
sources:
  - raw/inbox/2026-09-05.md
confidence: high
contested: true
---

# Decision 2026-09-05 19:06: CONTEXT is the wiki itself, watched being edited

## What Chris said
Twenty minutes after the first compiles landed and the CONTEXT section began rendering `index.md`, Chris rejected that view:

> "So I'm not crazy about how the content looks when it comes in. I see the entries that you're putting in and then there's the wiki below it. What I would rather see is next to the title see the diff like the plus-minus lines in the red and green like what you would see on like Github. See the diff numbers and then see which lines are being added to the wiki highlighted in green and which lines are being deleted, highlighted in red, and just actually watch the wiki get edited. I don't want any numbers indicating what's in the wiki, I want to just see the wiki. So then we can organize this by sections and command and make this very easy to wire." (19:06) ^[raw/inbox/2026-09-05.md]

Hermes restated it in one line: *"the CONTEXT view is the wiki itself with GitHub-style diffs — `+N −M` by the title, added lines green, removed lines red, watched live as the agent edits. No counts."* ^[raw/inbox/2026-09-05.md]

## What changed (19:12, "Done, DOM-proven")
- **CONTEXT is the wiki** — *"no counts, no index list. The card renders the topic's actual pages by section (ENTITIES / CONCEPTS / DECISIONS / COMPARISONS / QUERIES), each page's title and rendered markdown, loaded through the bridge when the card opens (64 pages for senter)."* ^[raw/inbox/2026-09-05.md]
- **Live diffs** — the topic agent snapshots the wiki before its run and diffs every changed page after; each diff is an event the UI paints (details in [[topics/senter-wiki/wiki/entities/context-card-live-diff|context card live diff]]). ^[raw/inbox/2026-09-05.md]
- Same message fixed the card's width: [[topics/senter-wiki/wiki/decisions/2026-09-05-content-card-stops-at-side-chat|content card stops at the side chat]].

## Why
Chris wants to *watch* the second brain think, not read a table of contents about it. The earlier fix ("CONTEXT renders the full `index.md` — every page, one line each, wikilinked — with page/raw counts; the context orb = page count", 17:43) was right about depth and wrong about form: it showed him *entries* plus a wiki *below* them, i.e. a list about the wiki instead of the wiki. This continues the standing expectation in [[topics/senter-wiki/wiki/concepts/ui-performs-the-fleet|the UI performs the fleet]] — fleet work must be visible as it lands — and his GitHub instinct already seen in the [[topics/senter-wiki/wiki/entities/usage-strip|usage strip]] ("GitHub usage chart … tiny dots"). ^[raw/inbox/2026-09-05.md]

## Supersedes / conflict (kept with dates)
- **17:43** — [[topics/senter-wiki/wiki/decisions/2026-09-05-every-topic-is-an-llm-wiki|CONTEXT renders index.md; context orb = page count]].
- **19:06** — CONTEXT renders the pages themselves; **"I don't want any numbers indicating what's in the wiki."** The page-count orb number and the `CONTEXT · 60 WIKI PAGES · 26 RAW` header are therefore contested: the raw at 19:12 confirms "no counts" in the card but does not say what the context orb now shows. Marked `contested: true` until Chris or the DOM settles the orb.

## Follow-ups Chris attached (19:18)
- *"I want to make sure that all of the markdown actually renders — so the title is actually pop up as titles on this stuff within the context and everything."* Hermes began checking *"what `md()` handles versus what the wiki pages use"* (19:19). Open. ^[raw/inbox/2026-09-05.md]
- *"So then we can organize this by sections and command and make this very easy to wire."* — sectioned rendering is in; "command" organisation is unspecified. Open.
- His overall direction for the whole card: *"ideally, I would like all of this to be as markdown and built in Hermes stuff as possible"* → [[topics/senter-wiki/wiki/concepts/collapse-toward-hermes-native|collapse toward Hermes-native]].
