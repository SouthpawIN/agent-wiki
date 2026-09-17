# vault-live.html — tone / palette system ("paper") and the wallpaper girl

Chris's aesthetic: pure black background, ONE off-white for everything that is "white" — text, borders,
hollow rings, orbs, feed cards, AND the ink of the wallpaper girl. He compares them side by side and
reads any mismatch as a tint ("cream", "warm", "sad"). Grey is never a colour: fades are masks, state is
size/presence, opacity is not used for tone.

## The knob

```css
:root { --paper: color-mix(in srgb, #dfe8f5 var(--paperPct, 96%), #000); }   /* cool blue-white */
```
- Every palette role (`--text --muted --dim --border --accent --ok --warn --err --tool`) = `var(--paper)`.
- Every literal `#fff`/`#ffffff` inside `<style>` was rewritten to `var(--paper)` (regex over the style
  block only; keep the `:root` definition literal). Inline JS colours (canvas labels) are rare — leave them.
- "Dimmer" = lower `--paperPct`, NOT `filter:brightness` on `<html>`/containers: a filter (a) dims the star
  canvas and wallpaper too (Chris noticed the stars darkening), (b) creates a containing block that breaks
  `position:fixed` children (HUD, cards).
- `#FFE45A` attention yellow and the all-black EQ dots are exempt from the paper knob.
- Warm/cool requests: warm `#f2ede4`, neutral `#ececec`, cool `#e9ecef` (read as cream to him), blue-white
  `#dfe8f5` (accepted). He wanted "blue-ish off-white" — when he says cool, go visibly blue.

## The wallpaper girl must BE the paper colour

Her asset is white-on-black ink at only ~60% luminance (p99 = 153/255) and JPEG near-blacks. Three
approaches failed before the working one — the failure mechanisms are the lessons:

| Attempt | Why it looked wrong |
|---|---|
| `brightness(1.67)` on the image | 153→255 pure white, but UI became blue-white later → she read warm |
| `sepia()`/`hue-rotate` filters | approximate tints never match a hex; "still cream" |
| element `background:var(--paper)` + picture `mix-blend-mode:multiply` | (1) `filter` on the element runs AFTER its pseudo-children blend, so grayscale/brightness washed the tint back; (2) multiply(paper × 60% grey) is darker than paper → measured (176,176,176) neutral grey, which reads WARM beside blue-white text; (3) the element's bare paper background showed in the strip below the `contain`-fitted picture = the "gray bar along the bottom" (201,207,217) that three fade fixes couldn't remove |

Working (pixel-verified: her ink (192–200,192–200,208–216) vs UI text (200,200,216); bottom strip (0,0,0)):

```css
#wallBackdrop { background-image:none !important; background-color:#000 !important; filter:none; }
#wallBackdrop::before, #wallBackdrop::after { content:''; position:absolute; inset:0; background:var(--paper);
  pointer-events:none;
  -webkit-mask-image:var(--wallImg); -webkit-mask-size:contain; -webkit-mask-position:center;
  -webkit-mask-repeat:no-repeat; -webkit-mask-mode:luminance;
  mask-image:var(--wallImg); mask-size:contain; mask-position:center; mask-repeat:no-repeat; mask-mode:luminance; }
#wallBackdrop::after { z-index:1; opacity:var(--wallInk,1); }   /* two stacked masked layers: 0.6 ink → 0.84; --wallInk scales */
```
JS sets `bd.style.setProperty('--wallImg', "url('…')")` where it used to set `backgroundImage` (and `none` for
the "none" wall). The picture is used ONLY as a mask; the fill is flat paper → ink pixels are exactly
`--paper`, black stays black, nothing paints outside the picture.

## Measuring (do this before and after every tone change)

`screencapture -x /tmp/x.png`, decode with the stdlib PNG reader in `scripts/pixel-span-diff.py`, then:
- **Girl vs UI**: histogram `max(px)>90` pixels in her region and `>150` in the hero/title region; bucket to
  8-levels; compare the top buckets. Classify warm (`R>B+6`) / cool (`B>R+6`) / neutral — "warm" complaints
  were 17k neutral vs 1.4k cool pixels, i.e. grey, not warm.
- **Bottom strip**: sample 3 columns at y = h−50…h−150; anything non-(0,0,0) above the app chrome rows is
  a layer background, not the fade. The fade (`#fade`) is a pure-black gradient (`rgba(0,0,0,0)→#000`) and
  Chris wants it kept but invisible.
- Report the numbers to Chris; he distrusts vision verdicts and accepts pixel triples.

## Related knobs
- `--spaceGlow` — star canvas opacity behind the wiki (SPACE itself is always 1). Was dead until the JS
  inline `opacity:.22` on the canvas was removed. Chris settled at .46.
- `--wallInk` — her ink strength alone. `--ringW` — hollow-circle ring width (shared by active orb + gear).
