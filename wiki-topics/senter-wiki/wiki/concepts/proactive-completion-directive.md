---
title: Proactive completion directive — layout + budget, finish front and back end
created: 2026-09-09
updated: 2026-09-10
type: concept
tags: [preference, decision, infra, budget]
sources:
  - raw/inbox/2026-09-09-from-turbofit.md
  - raw/inbox/2026-09-10.md
confidence: high
---

# Proactive completion directive

> "I'll complete the Senter Wiki UI restoration now, including both frontend and backend coordination … please continue until the UI is restored to what I want (read through this session to find clues and specs), and finish both the front and back end for Senter Wiki entirely without needing my confirmation. Understand that we can undo choices you make easily, so do not be afraid to make them." — Chris, 2026-09-09 20:05 ^[raw/inbox/2026-09-09-from-turbofit.md]

**What.** Chris directed Hermes to complete the Senter Wiki UI restoration — front and back end — entirely without needing confirmation, using session history and existing specs as the guide. The directive was repeated on 2026-09-10 when Chris escalated frustration: *“Hey, I need you to fix the layout and fix the update. Don't do anything else just do those two because I've been asking you to keep getting stuck”* ^[raw/inbox/2026-09-10.md], then *“I've asked you several times all day today and all day yesterday … It's not take two days on this.”* ^[raw/inbox/2026-09-10.md]

## Key constraints
- **M1 MacBook 32GB unified memory** (`hw.memsize: 34359738368`) is the fixed hardware constraint. ^[raw/inbox/2026-09-09-from-turbofit.md]
- **Local model budget**: the local LM has a 500-hour limit. Chris forbade Hermes from using the local model for general wiki work — it must be reserved for local-model-as-deliverable cases only. General wiki work should not hit the local model. ^[raw/inbox/2026-09-09.md]
- **Undo-friendly**: *“we can undo choices you make easily, so do not be afraid to make them.”* ^[raw/inbox/2026-09-09-from-turbofit.md]
- **No music generation**: explicitly cancelled. ^[raw/inbox/2026-09-09-from-turbofit.md]
- **Priority**: layout + model first. ^[raw/inbox/2026-09-09-from-turbofit.md]

## What this overrides
This directive is a standing order for ALL wiki infra/UI work, not just the 2026-09-09 session — paired with *“we can undo choices easily, so do not be afraid to make them”* and *“priority: layout + model first.”* ^[raw/inbox/2026-09-09.md]

## Related
- [[wiki-topics/senter-wiki/wiki/decisions/2026-09-10-layout-and-update-fix|layout and update fix]]
- [[wiki-topics/senter-wiki/wiki/decisions/2026-09-09-local-lm-reserved-from-general-wiki-work|local LM reserved from general wiki work]]
- [[wiki-topics/senter-wiki/wiki/entities/vault-live-html|vault-live.html]]
- [[wiki-topics/senter-wiki/wiki/entities/senter-bridge|senter-bridge]]
- [[wiki-topics/senter-wiki/wiki/entities/scan-topics|scan-topics.py]]

^[raw/inbox/2026-09-09-from-turbofit.md]
^[raw/inbox/2026-09-10.md]
