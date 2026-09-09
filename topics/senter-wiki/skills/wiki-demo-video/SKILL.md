---
name: wiki-demo-video
description: Use when Chris asks for a demo/recording of the Senter wiki. Full-screen with the Hermes sidebar, driven through the REAL event pipeline, recorded after the visual state is approved.
version: 0.1.0
distilled: 2026-09-05
topic: senter-wiki
---
# wiki-demo-video

## Principle
Drive the real pipeline, never fake DOM. Re-add `window.__senterHandle=(e)=>handle(e);` right before `function handle(ev){` in the events IIFE (stripped at the MVP checkpoint) and feed scripted events.

## Script (append before `</body>`, tagged TEMP-DEMO)
- `setInterval(tick, 650)`: `message` every 2 ticks, `tool` start/end every 3, `skill` every 4, `approval` pending every 7 with `decided` 2–5s later (`choice:'once'|'session'|'always'`). Every event needs a distinct `ts` (dedupe key `ts|kind|id/tool/phase`).
- `window.hpEq.demo(sec)` for the headphone EQ (or play a real track via the bridge — the real analyser is better).
- `sweep(fromRow, count, 520ms)`: drawn SVG cursor glides row to row; each row gets `.demoHover` (must replicate the hover CSS — band/underline `width:100vw`, title `--hfs`, orbs at hover size; `:hover` can't be forced) + `mouseover` dispatch so the hero follows.
- `scrollTour(8000)` on `#view-wiki` (own scroll container), `openEditor(row)` / `closeEditor(false)`, SPACE round trip (`body.classList.add('space')`, reverse ~8s).
- Trigger = fixed `<button id="demoGo">` clicked via `drive_preview click selector=#demoGo` (URL flags are stripped).

## Record
```
rm -f ~/Desktop/senter-demo.mov
(screencapture -v -V 52 -x ~/Desktop/senter-demo.mov >/tmp/rec.log 2>&1 &); sleep 2
# drive_preview click #demoGo ; stay silent so the sidebar shows steady state
sleep 54; mdls -name kMDItemDurationSeconds ~/Desktop/senter-demo.mov
```
Full screen = Hermes sidebar left + wiki pane right ("cursor setup"). No ffmpeg on this Mac; the .mov (~200MB/50s) is the deliverable — state its absolute path.

## Rules
- Record AFTER the current visual state is approved (a take before the usage-chart fix had empty cells and was redone).
- Strip `TEMP-DEMO` script and the hook afterwards; `assert 'TEMP-DEMO' not in s`; `scripts/vault-live-check.py`.

## Evidence
> "take a demo video … show off all the animations … music playing so the visualizer goes … lots of bot activity, permissions arriving and getting accepted, scrolling through topics, stars lighting up … very lively, highly agentic."
> "it needs to show the Hermes sidebar too — the whole thing operates together like a cursor setup."
> "drag the mouse through a couple of tiles at medium speed (cascade), and show the editor opening."
