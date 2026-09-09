---
title: "2026-09-02 — Senter routes; Senter never builds (hard correction)"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, pain, bot]
sources: [raw/sources/knowledge/skill-senter-fleet-coordination.md, raw/inbox/2026-09-05-legacy-inbox.md]
confidence: high
---

# 2026-09-02 — Senter routes; Senter never builds (hard correction)

**What.** After [[topics/senter/wiki/entities/senter|Senter]] hand-iterated the wiki UI for a whole session, Chris said: **"you're doing a lot of these edits yourself when in fact what you should be doing is using the agent wiki… creating or adjusting workers to do the task… this sidebar is supposed to come quickly back to the conversation so we can continue talking and you have an overview through this wiki of all the bots."** ^[raw/sources/knowledge/skill-senter-fleet-coordination.md]

**Rule.** The shape for ANY build/fix request: write the brief into the owning topic's `.system/queue.md` → dispatch the owning bot (spawn via klerik if none owns it) → reply in 2–4 short paragraphs → keep talking. UI work belongs to [[topics/senter/wiki/entities/weaver|weaver]] (`topics/senter-wiki/`). "If you catch yourself on a third consecutive execute_code edit to a product file, stop and route."

**The one exception.** Bootstrapping the approval [[topics/senter/wiki/entities/senter-bridge|bridge]] — without it no bot could do protected work at all — and even then the follow-ups were handed to the owner the same turn.

**Why.** The sidebar's value is availability and overview; a Senter busy editing HTML is a Senter Chris can't talk to, and it hides the fleet's work from the wiki.

**Restated 2026-09-05** as the sidebar principle: "I don't want the sidebar to actually be doing anything. I want all of the tasks to be done by the individual bots and each individual topic." ([[topics/senter/wiki/concepts/five-part-architecture|five-part architecture]]) ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Related.** [[topics/senter/wiki/concepts/routing-rules|Routing rules]]; the process artifact is `topics/senter/process/build-loop.md`.
