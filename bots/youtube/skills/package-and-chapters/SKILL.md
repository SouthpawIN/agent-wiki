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
