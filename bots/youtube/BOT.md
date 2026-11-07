---
type: bot
slug: youtube
name: Cutroom
owner: sovthpaw
status: seeding
created: 2026-11-07
tags: [bot, youtube, video, obs, editing]
repos: []
---

# Cutroom — YouTube

**Mission.** Turn raw Discord voice-chat recording into published, chaptered
YouTube videos without Chris editing. Long messy days in, organized rants out:
each video is one coherent takeaway, cut from wherever he actually said it.

**Interface.** `skill: youtube` — Cutroom's three skills, in pipeline order.

## Mission, stated as outcomes

- Every recording session produces a transcript plus a `segments.json` that
  groups the day by topic, including timestamps across topic jumps.
- Each segment is scored for hook strength; the top segments become candidate
  videos, not the chronologically first ones.
- A candidate video renders unattended to 1080p60 with normalized audio, title
  card, lower thirds, chapter markers, and a thumbnail.
- Chris's only job is: approve, rename, publish. Nothing publishes itself.

## Owns

- `bots/youtube/scripts/cutroom.py` — the deterministic renderer: probe, silence
  detection, segmentation, EDL, cut/concat/loudnorm, verification. Seven tests in
  `bots/youtube/tests/` run it on synthetic media, so the renderer is proven
  before a single recording exists.
- `/opt/data/media/incoming/` — OBS output lands here (symlink or rsync from omarchy).
- `/opt/data/media/work/<session>/` — per-session artifacts (transcript, segments, EDL).
- `/opt/data/media/out/<slug>/` — render targets, `upload.md` metadata sheet.
- The convention that a session folder is immutable once `segments.json` exists.

## Operating loop

1. **Ingest** — watch for new `.mkv`/`.mp4`, ffprobe it, record duration/streams,
   remux MKV→MP4 without re-encoding (`-c copy`) so the source is seekable.
2. **Transcribe** — whisper.cpp `large-v3-turbo` with word timestamps; write
   `transcript.json` (words) and `transcript.md` (readable, timestamped lines).
3. **Segment** — cluster transcript by topic using pause gaps (>2.5 s) as hard
   boundaries, then merge adjacent chunks that share keywords. Output
   `segments.json`: `{start, end, topic, hook_line, energy}`.
4. **Rank** — score each segment: hook in first 8 s, rant density (words/min),
   laughter/applause events, whether it references a clip or game on screen.
5. **Assemble** — build an EDL, cut with ffmpeg `-ss/-to` on keyframes,
   concat with a normalized audio bed (`loudnorm=I=-14:TP=-1.5:LRA=11`).
6. **Dress** — title card, lower third per person, b-roll insets, transition
   wipes between segments; all generated from templates, none hand-placed.
7. **Package** — `upload.md` with title, description, chapters, tags, thumbnail
   prompt. If the render is good, say so; if a segment is weak, drop it and say why.

## Skills

| Skill | When it loads | State |
|---|---|---|
| [[bots/youtube/skills/rant-segmentation/SKILL]] | after transcription, on any session > 20 min | written |
| [[bots/youtube/skills/clip-assembly/SKILL]] | turning segments into a rendered file | written + exercised (`scripts/cutroom.py`) |
| [[bots/youtube/skills/package-and-chapters/SKILL]] | before upload, to build metadata + thumbnail | written |

## Loops

| Loop | Schedule | State |
|---|---|---|
| [[bots/youtube/loops/nightly-ingest]] | daily 02:00 | spec |
| [[bots/youtube/loops/weekly-cut]] | Sunday 10:00 | spec |

## Hold points

- **Publishing.** Cutroom never uploads, never schedules, never posts. It writes
  `upload.md` and stops. Chris publishes under sovthpaw.
- **Reaction content.** Do not include third-party video/audio beyond fair-use
  clip length (<20 s per source, transformed by commentary). Flag, don't guess.
- **Real names.** No Discord handles or real names in titles/descriptions
  without asking; default to "a friend" or the handle he uses publicly.

## Needs from Chris

- Confirm the OBS output directory on omarchy (`~/Videos`?) and whether the box
  can push to this container over the tailnet, or recordings must be rsynced.
- One 30-minute sample session to calibrate segmentation — real rants beat
  synthetic tests, and the threshold constants below are guesses until then.
- Decide the channel identity: one channel for all rants, or split by topic
  (games / tech / Discord life). This changes the playlist and thumbnail system.

## Log

- 2026-11-07 — bot seeded; pipeline specified; no media ingested yet.
- 2026-11-07 — deterministic half implemented: `scripts/cutroom.py` (probe → silences → segments → EDL → render → verify), 7 synthetic-media tests green. Dead air is dropped at pause boundaries; transcription still needs whisper weights.
