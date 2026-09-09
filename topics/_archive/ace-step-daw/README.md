---
title: ACE-Step-DAW
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/ACE-Step-DAW
status: dormant
tags: [repo]
---

# ACE-Step-DAW

> WIP...

**[Open on GitHub](https://github.com/SouthpawIN/ACE-Step-DAW)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** TypeScript
- **Stars / forks:** 0 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-21 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

ACE-Step DAW

  The AI-native DAW where every instrument knows what came before it.

  Quick Start &bull;
  What Makes It Different &bull;
  Features &bull;
  Architecture &bull;
  Contributing

> **Want a production-ready experience today?** Try [ACE Studio](http://acestudio.ai/) — our professional AI music creation platform with higher quality models and real-time collaboration.

## What Makes It Different

Most AI music tools generate a full song in one shot. ACE-Step DAW takes a fundamentally different approach — it builds songs **layer by layer**, where each new instrument is musically aware of everything generated before it.

### LEGO Pipeline — Context-Aware Sequential Generation

Generate drums first. Then bass that grooves with the drums. Then guitar that complements both. Then vocals that sit perfectly in the mix. Each layer "hears" the cumulative result of all previous layers through the ACE-Step 1.5 model.

```
Drums → Bass (hears drums) → Guitar (hears drums+bass) → Vocals (hears everything)
```

This isn't post-hoc mixing — the AI **composes** each part knowing the full musical context, producing arrangements that are coherent from the ground up.

### Strudel Live Coding — Algorithmic Composition as a Track Type

Write `s("[bd ]*2, [~ cp]*2")` and hear it instantly. ACE-Step DAW integrates [Strudel](https://strudel.cc) as a first-class track type alongside traditional timeline clips. Switch between visual editing and code-based pattern generation without leaving the DAW. Convert between MIDI and Strudel patterns freely.

### Agent-Native Architecture

Every feature is accessible via `window.__store.getState().actionName()`. The entire DAW state is scriptable, testable, and automatable. Built for a future where AI agents and humans collaborate on music production side by side.

## Quick Start

**Requirements:** Node.js 18+ and an [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5) API server (local or cloud).

```bash
git clone https://github.com/ace-step/ACE-Step-DAW.git
cd ACE-Step-DAW
npm install
npm run dev
```

Opens at [http://localhost:5174](http://localhost:5174). The dev server proxies `/api` to the ACE-Step 1.5 backend at `localhost:8001`.

**Cloud API:** Configure the backend URL in Settings → API URL: `https://api.acemusic.ai`

**Production build:**

```bash
npm run build && npm run preview
```

## Features

### AI Generation

| Feature | Description |
|---------|-------------|
| **LEGO Pipeline** | Sequential generation with cumulative context — drums → bass → guitar → vocals |

*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics/music/README|music]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
