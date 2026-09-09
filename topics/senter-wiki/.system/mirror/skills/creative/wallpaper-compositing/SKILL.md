---
name: wallpaper-compositing
description: Composite line art over dark plates into wallpapers.
version: 1.0.0
author: hermes-curator
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [wallpaper, compositing, pillow, line-art, desktop, retina, image-generate]
    related_skills: [macos-system-settings, comfyui, p5js]
---

# Wallpaper & Art Compositing (Pillow)

## When to Use

Use when the user wants a **desktop wallpaper or composite image** built from existing
artwork rather than generated whole — "overlay these patterns on a dark galactic image",
"put that figure over slate rock", "make it moody and dark themed", "use the art from
<site> as a wallpaper".

The giveaway is that `image_generate` alone is the wrong tool: the user wants *specific
existing art* preserved, with a generated or supplied backdrop behind it. Generate the
**backdrop**, composite the **art**. Never try to prompt a model into reproducing artwork
you already have.

## The workflow

1. **Harvest the real assets.** Scrape the source page for image URLs rather than guessing
   filenames — they're usually content-hashed:
   ```bash
   curl -s <url> | grep -oE '(src|href)="[^"]*\.(png|jpg|jpeg|webp|avif|svg)"' | sort -u
   ```
2. **Probe every source before compositing** (see Pitfalls — this is the step that saves
   the most rework). Use `scripts/probe_art.py`.
3. **Generate backdrops** with `image_generate`. Ask for *extremely* dark, low-key,
   no-subject, no-text abstract backgrounds — a mid-bright backdrop kills the glow effect.
4. **Composite at 2× the panel** so it stays sharp on Retina. Get the panel with
   `system_profiler SPDisplaysDataType | grep Resolution`.
5. **Verify with `vision_analyze` and ask a critical question** — "is there a leftover white
   box? is it a flat silhouette or real line art?" A neutral "describe this" prompt will
   happily describe a broken composite as pleasant art.
6. **Set it, then confirm the read-back:**
   ```bash
   osascript -e 'tell application "System Events" to tell every desktop to set picture to POSIX file "/abs/path.png"'
   osascript -e 'tell application "System Events" to get picture of every desktop'
   ```

Deliver downscaled JPEG previews (`sips -Z 1400 -s format jpeg`), not the 20–30 MB PNGs —
inline delivery of a full-size wallpaper is unusable in chat.

## Environment

Pillow/numpy are frequently absent from system python3 but present in the Hermes venv.
Use it directly rather than installing anything:

```bash
~/.hermes/hermes-agent/venv/bin/python build.py
```

Write scripts to a **file** and run them. Long `python -c "..."` one-liners trip the
security scanner's nested-executable check and can block on approval.

## Source-art sourcing: check local work FIRST, site second

If the user references an existing folder of prior wallpaper work (`~/Pictures/<name>/`
with a `src/` subdir), **read it before generating anything**. A prior session may have
already harvested the real site assets + build script; regenerating with `image_generate`
when real source art exists on disk is a hard correction ("NO — find the images from the
website I am talking about and actually download and use them"). Build on the existing
`build.py`, add new art files, and rebuild.

This correction can come late — a user may accept a first batch of generated images,
then point at the real folder when asking for MORE variants ("like the ones in this
folder"). Re-read the folder at every continuation, not just the first request. Also:
"the ones from before" / "the first three" refers to the PRIOR session's composites
(there named `hermes-slate/galactic/ember.png`), not anything generated this turn —
check `@folder:` attachments and `~/Pictures/` before guessing.

"Use different images from the sites" means harvest MORE real assets from the site and
composite those (same build pipeline, new art files, new accent palettes) — never
hand-prompt a generator to imitate the art style.

To pull fresh art from a site: `web_extract` the page, grep the markdown for
`web-assets.*\.(webp|png)` URLs (they're content-hashed), then `curl -fsS -o` each into
`src/`. Verify what each asset actually is with `vision_analyze` before compositing.

## The alpha-vs-luminance trap (the core lesson)

Line art arrives in one of **four** shapes, and the correct ink mask differs for each.
Getting it wrong produces a plausible-looking but wrong result:

| Source shape | Correct mask | Wrong-mask symptom |
|---|---|---|
| Ink on **opaque white**, no alpha | luminance key: `1 - lum` | — |
| **Alpha cutout**, ink fills the shape | `alpha` | luminance key drags in a bright **rectangular box** |
| **Alpha cutout** with ink on white paper *inside* it | `alpha × (1 - lum)` | alpha alone → flat **silhouette**; luminance alone → white box |
| **White/cyan engraving on dark blue field** (site feature art) | luminance key on **bright** pixels, then suppress blue-dominant pixels and **feather edges** | pasting/screening whole image → visible blue square panel |

The third case is common in real web assets and is the one that burns a rework cycle.
The fourth is the signature of Nous-style feature art (`feature-*.webp`, `badge.webp`):
a deep royal-blue background with white halftone engraving. For it:

```python
lum = 0.2126*r + 0.7152*g + 0.0722*b
ink = np.clip((lum - ink_thresh) / ink_range, 0, 1)      # bright engraving -> 1
blue_dom = b - 0.5*(r + g)
ink *= np.clip(1.0 - np.clip(blue_dom - 0.15, 0, 1) * 4, 0, 1)   # kill blue bg
mask = feather_edges(mask, frac=0.06)                    # fade border to zero
```

Always resolve the shape from probe data (`scripts/probe_art.py`), not from the filename.

```python
ink = np.clip((1.0 - lum - 0.10) / 0.60, 0, 1)   # ink -> ~1, paper -> 0
if alpha is not None:
    ink *= alpha / 255.0                          # AND with the cutout
```

## Making it read as "moody"

- `darken(mul, gamma)` — gamma **first**, then multiply, so shadows compress instead of clip.
- `vignette` — radial falloff ~0.7 strength pulls the eye to the subject.
- `grain` — a few units of gaussian noise kills digital flatness and banding.
- **Screen, don't paste.** `ImageChops.screen` makes light art glow over a dark plate;
  pasting gives you a sticker.
- **Bloom under, crisp ink over.** A gaussian-blurred tinted copy screened first, then the
  sharp ink screened on top, is what produces the neon-sign look.
- **Recolor the ink.** Tint the *mask*, don't reuse the source's original color — dark blue
  source ink screened over a dark plate adds nearly nothing. Lift it to a bright tint.

## Pitfalls

- **Probe before you composite.** Print mode, size, corner pixels, luminance min/max, and
  alpha min/max + transparent fraction for every source. Three passes were wasted in one
  session by assuming "line art on white" for an asset that was actually an alpha cutout
  with white paper inside it. `scripts/probe_art.py` does this.
- **Not every source can be de-paneled.** Art whose engraving fills the entire frame edge
  to edge (full-bleed op-art, app screenshots) will always read as a pasted rectangle —
  no threshold/feather trick hides it. Verify with vision, then **drop the variant**
  rather than shipping a panel-edged result. Deleting a failed variant is the right call.
- **Feather the mask border** for any extracted-from-a-field mask (`frac≈0.06` ramp to
  zero at the edges) — otherwise the source rectangle's boundary still reads as a panel.
- **Ink threshold is per-asset.** Full-frame ray/texture art needed the top ~2%
  luminance (`thresh≈0.90, range≈0.10`); typical halftone portraits work at
  `thresh≈0.35, range≈0.65`. Tune per asset from percentile stats.
- **Some site art is already composited** (light-background screenshots, e.g.
  `showcase.webp`) — screen-blending those washes the whole plate. Skip them or
  extract only the dark UI ink.
- **Ask vision a critical, falsifiable question.** "Is anything washed out or broken? Any
  leftover white box? Is it real line art or a flat silhouette?" — not "describe this image".
  A vision model asked neutrally will praise a broken composite.
- **Generated backdrops come back small** (often ~1024×576). Upscale with LANCZOS to 2× the
  panel; don't composite at the generated size.
- **`sips` cannot composite** — it only scales/converts. Use Pillow for any layering.
- Save wallpapers somewhere durable and user-visible (`~/Pictures/<name>/`), keep the sources
  and build script in a `src/` subdir so the set can be rebuilt or retinted later.

## Supporting files

- `scripts/probe_art.py` — dump mode/alpha/luminance stats for source art; run FIRST.
- `templates/build_wallpaper.py` — working composite pipeline (cover, darken, vignette,
  grain, ink mask, screen-glow, place). Copy and retune the palette per job.

## Reference build: Nous/Hermes site wallpapers (validated 2026-08-29)

A full production run of this skill lives at `~/Pictures/HermesWalls/` — `src/build.py`
implements every technique above (dual ink extractors, edge feathering, per-asset
thresholds, build+drop verification loop) against real nousresearch.com / hermes site
assets (`portal-figure.webp`, `badge.webp`, `feature-*.webp`). Reuse it as the starting
point before writing a new pipeline: it already encodes the alpha-vs-luminance table,
the blue-bg suppressor, feathering, and the "build → vision-verify → delete failures"
discipline. New site art goes in `src/`, new `build()` calls at the bottom, rerun.

Site asset URLs are content-hashed under `web-assets.nousresearch.com/nousnet-web/img/...`
— harvest via web_extract + grep, don't guess filenames. Note fresh-Mac gotcha:
`python3 -m venv .venv && .venv/bin/pip install pillow numpy` in the project dir works;
system python3 has neither module.
