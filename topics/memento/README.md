---
title: memento
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/memento
status: dormant
tags: [repo]
---

# memento

> No description

**[Open on GitHub](https://github.com/SouthpawIN/memento)** · DORMANT (since 2026-07-17) · last push 2026-07-17

## Facts
- **Language:** —
- **Stars / forks:** 0 / 0
- **License:** —
- **Fork of:** original work
- **Created:** 2026-07-28 · **Last push:** 2026-07-17
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-17)

## From the README

# MEMENTO

A live journal you talk to. Video/voice log entries and full-duplex agent
sessions, transcribed, indexed, and remembered: search & Ask, concept catalog,
mission calendar with day reports, weekly debriefs with narrated recap videos,
pins & time capsules, threads & rapport profile, Life Story program, visual
log, stats & starmap, morning briefings. Vision doc: [PLAN.md](PLAN.md);
this file is the operational reference.

## Screenshots

Every shot below is from a demo instance seeded with fictional data
(`memento_demo` — a telescope restoration, a trail-race block, and a sourdough
starter named Kepler). Nothing here is a real journal.

**Mission timeline** — the home feed: every log indexed, transcribed, and summarized.

**Live console** — full-duplex voice sessions with the agent (idle, ring presence).

**Mission calendar** — day reports, moods, and reminders at a glance.

**Stats** — streaks, logged time, mood strip, and what the log keeps returning to.

**Memory starmap** — every concept a star; shared entries draw the filaments.

**Operator profile** — open threads and the rapport model, fully user-editable.

**Life Story program** — a long-form interview conducted over weeks.

## Stack

- `web/` — Next.js 16 (port **8742**), Mission Log UI, API routes
- `worker/` — Python pipeline (polls Postgres): whisper transcription,
  embeddings, LLM extraction/reflection, vision pass, day/week reports,
  capsule delivery, recap videos
- `db/schema.sql` — Postgres 17 + pgvector (port **5433**)
- MinIO (S3) for raw media (API **9400**, console **9401**)
- `.env` — single shared config (web reads it via the `web/.env.local` symlink)

## Run

**Production (how it runs now):** everything is persistent — Docker services
restart themselves, and the web app + worker are systemd user services
(lingering enabled, so they start at boot and auto-restart on crash):

```bash
systemctl --user status memento-web memento-worker
journalctl --user -u memento-worker -f        # worker logs
# after changing web code: (cd web && npm run build) && systemctl --user restart memento-web
# after changing worker code: systemctl --user restart memento-worker
```

**Development:**

```bash
systemctl --user stop memento-web             # free port 8742 first
bash scripts/dev.sh                           # docker + migrate + worker + next dev
```

Open http://localhost:8742 — camera capture requires localhost or HTTPS
(over Tailscale, use `tailscale serve` for HTTPS or browse from the DGX itself).

**Install on your phone (PWA):** open the Tailscale HTTPS URL → Android

*…truncated — full README at repo link*
