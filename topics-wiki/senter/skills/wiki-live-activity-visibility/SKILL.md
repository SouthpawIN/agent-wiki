---
name: wiki-live-activity-visibility
description: Use when any worker edits the vault while Chris is watching. Every edit must produce visible UI motion — topic open/edit/close in the pane and a side-feed line.
version: 0.1.0
distilled: 2026-09-05 17:24
topic: senter
---
# wiki-live-activity-visibility
# Wiki live activity visibility

## Principle
An edit Chris cannot see happening is not done. Motion is the proof-of-work surface.

## Steps (per worker action)
1. Before writing a file, emit an 'opening <topic>/<file>' event to the side feed.
2. Write the file; the pane must navigate to / highlight the edited topic and show the diff region.
3. After writing, emit 'closed <file> — <one-line change>' and return the pane to the hub.
4. Spread work across ALL active topics on each pass — never let activity concentrate in 1–2 topics while others sit idle.
5. Proposals (skills-capabilities/bots-profiles/loops) land as cards in the feed the moment they're generated, not batched.

## Verification
- Capture Chris's REAL window (AX preview pane) after a pass; confirm feed lines and topic transitions are visible. No capture = 'not verified in your window'.
- Check that music/transport and every topic route render correctly; broken routes count as invisible work.

## Pitfalls
- Silent background edits with no feed line.
- Working only in the senter topic.
- Describing motion instead of capturing it.

## Evidence
> I'm not seeing things move in the UI like I thought that I would Maybe it is maybe you're just in one or two topics
> I want to see this thing scrolling around and flying around and topics opening and being edited and being closed in the feet opening and and you're the side feet going and all that
> making all the Topics work as they're supposed to and when you're editing it and when you're working on it
