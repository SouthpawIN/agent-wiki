---
title: Decision — the watcher files raw inbox per message, "like Cursor"
created: 2026-09-05
updated: 2026-09-05
type: decision
tags: [decision, preference, infra, spec]
sources: [raw/inbox/2026-09-05-legacy-inbox.md, raw/inbox/2026-09-05.md]
confidence: high
---
# Per-message inbox filing ("per message, like Cursor")

**What.** The watcher that feeds each topic's `raw/inbox/` files one block per message, not per session or per summary. The inbox header records the instruction verbatim: `Filed by the watcher per message (Chris 2026-09-05: "per message, like Cursor")`. ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Chris's words.** "per message, like Cursor" — the only direct Chris quote in this compile's raw set. The Cursor reference is to how Cursor's chat keeps each turn as its own addressable unit rather than a merged transcript.

**How it shows up.** Each block carries `## <date> <time> · <sender> · <session id> · sim <score>` then the message body ^[raw/inbox/2026-09-05-legacy-inbox.md] ^[raw/inbox/2026-09-05.md]. The `sim` score is the watcher's similarity between the message and this topic; the three klerik blocks scored 0.09–0.16, i.e. weak matches that still got filed because per-message filing is deliberately inclusive — the topic loop "distils it". ^[raw/inbox/2026-09-05-legacy-inbox.md]

**Consequence for this wiki.** Low-sim, assistant-side blocks will keep landing here. Compile pages must therefore state sender and confidence honestly rather than attributing assistant text to Chris (this compile does so on every page — see [[wiki-topics/klerik/wiki/entities/klerik|klerik]]). The trade-off is accepted: better a noisy raw record than lost context, matching the [[wiki-topics/klerik/wiki/concepts/topic-build-out-spec|Topic build-out spec]]'s "all real" stance.
