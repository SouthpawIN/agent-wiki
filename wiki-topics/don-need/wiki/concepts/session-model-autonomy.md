---
title: "Session model autonomy — running as 'auto' on a custom provider"
created: 2026-09-15
updated: 2026-09-15
type: concept
tags: [infra, question, pain]
sources: [raw/inbox/2026-09-15.md]
confidence: high
---

# Session model autonomy — running as "auto" on a custom provider

Chris's session on 2026-09-15 is running as **"auto"** on a **custom provider**, and Hermes does not expose the underlying model name in the session metadata. He flagged this as something he noticed about the session itself.

The practical upshot, in his words: *"I'm running as 'auto' on a custom provider — Hermes doesn't expose the underlying model name in this session's metadata."*

This sits alongside his earlier 2026-09-13 insistence that TurboFit should "think of itself" and fall back to a main model when a configured one is missing [[wiki-topics/don-need/wiki/concepts/turbofit-model-fallback|TurboFit missing-model fallback preference]] — a recurring thread that he wants the agent to be self-sufficient about which model it is, rather than silently failing or asking him. Here it surfaces as a gap in the other direction: he wants visibility into exactly which model is running, because "auto" hides it.

Cross-ref: the same session also carried the terminal-work-autonomy line — the agent should do the SSH/terminal work itself rather than pushing commands back to Chris [[wiki-topics/don-need/wiki/concepts/terminal-work-autonomy|Terminal-work autonomy]].

## 2026-09-15 18:12 — can't see the available models
Hours later Chris looked at the session's model list directly and reported what he could and couldn't see: *"I see auto and I see the local teal coder, but I don't see the available…"* (truncated in the record). Two things land here:

- **"the local teal coder"** is Chris's name for the local model in the list — Cyber-Tiel-Coder, the Ornith variant (the teal-coloured local model). He recognises it by colour/name rather than full id.
- He sees **`auto`** and the local teal coder, but the available-model list is **incomplete or unhelpful** — the trailing "I don't see the available…" reads as him expecting more models to be listed than actually appear.

The thread tightens: he wants the real model name surfaced (not hidden as "auto"), and he wants the available models to actually show up. Same instinct as the 09-13 TurboFit line [[wiki-topics/don-need/wiki/concepts/turbofit-model-fallback|TurboFit missing-model fallback preference]] — the agent should know and be able to name its own model without him having to dig.

## Provenance
- *"I'm running as 'auto' on a custom provider — Hermes doesn't expose the underlying model name in this session's metadata."* ^[raw/inbox/2026-09-15.md]
- *"Okay, so I see auto and I see the local teal coder, but I don't see the available…"* ^[raw/inbox/2026-09-15.md]
