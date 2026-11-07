---
type: loop
slug: nightly-ingest
bot: youtube
schedule: "0 2 * * *"
state: spec
skill: rant-segmentation
created: 2026-11-07
---

# nightly-ingest

02:00 daily. Ingest → transcribe → segment. No rendering (that is the weekly cut).

## Prompt

Run Cutroom's ingest and transcription for any new file in
`/opt/data/media/incoming/`. For each new session: remux, transcribe with
whisper.cpp large-v3-turbo (word timestamps), then run `rant-segmentation` and
write `segments.json`. Append one line to the bot log with hours ingested and
the top segment title. If nothing new, exit without writing.

## Stop condition

Stop if disk free < 40 GB or transcription fails twice on the same file; report
the file name and the error, do not retry a third time.
