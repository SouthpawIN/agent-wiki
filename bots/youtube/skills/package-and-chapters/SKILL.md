---
name: package-and-chapters
description: Build title, description, chapters, tags and thumbnail prompt for a cut.
version: 1.0.0
author: Cutroom
license: MIT
metadata:
  hermes:
    tags: [youtube, metadata, thumbnail, seo]
---

# Package and chapters

Input: `segments.json`, `render.mp4`. Output: `upload.md`. Never uploads.

## The tool

```bash
python bots/youtube/scripts/cutroom.py package segments.json --out out/ \
    --premise "One sentence on what this session is about" --visibility unlisted
```

It writes `out/upload.md` and prints the title, chapters, tags, and runtime. The
title comes from the highest-ranked segment's hook line, capped at 60 characters;
chapters always start at `0:00` and segments shorter than 10 s are merged into the
previous chapter. Packaging **fails** if a private name appears in the title or
premise — the public handle is `sovthpaw`.

## Procedure

1. **Title** — the hook line, compressed to ≤ 60 chars, front-loaded with the
   claim. No clickbait the video does not deliver; Chris's whole voice is that
   he says the thing plainly.
2. **Chapters** — from segment boundaries, rounded to the second. First chapter
   must be `0:00`. Minimum 3 chapters, each ≥ 10 s.
3. **Description** — three parts: one-sentence premise, chapter list, then
   credits/links. Say "recorded live in the Nous Research Discord" only if true
   for that session.
4. **Tags** — 8–12, from segment terms plus channel-level standards. No
   keyword stuffing; YouTube ignores most of it anyway.
5. **Thumbnail** — one dominant subject, ≤ 4 words of text, high contrast at
   320×180 legibility. Write the prompt; generate with `image_generate`; check
   the downscaled version before shipping.
6. **Write `upload.md`** with sections: Title / Description / Chapters / Tags /
   Thumbnail / Visibility (`unlisted` default) / "Needs Chris": one line.
7. **Public name check** — every name in the file is `sovthpaw` or a public
   handle. Fail the package if Chris's legal name appears anywhere.
