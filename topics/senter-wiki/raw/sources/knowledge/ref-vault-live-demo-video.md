# vault-live demo video recipe (validated 2026-09-03)

Chris: "take a demo video … show off all the animations … music playing so the visualizer goes …
lots of bot activity, permissions arriving and getting accepted, scrolling through topics, stars
lighting up … very lively, highly agentic." Then: "it needs to show the Hermes sidebar too — the
whole thing operates together like a cursor setup." Then: "drag the mouse through a couple of tiles
at medium speed (cascade), and show the editor opening."

## Principle
Drive the REAL pipeline, never fake DOM. Everything the page does on a bridge event goes through
`handle(ev)` in the events IIFE — expose it once (`window.__senterHandle=(e)=>handle(e);` right
before `function handle(ev){`) and feed scripted events.

## Event shapes `handle()` accepts
- `{kind:'message', bot, summary, topic}` → feed card + orb light + star pulse
- `{kind:'tool', phase:'start'|'end', bot, topic, tool, summary}`
- `{kind:'skill', bot, topic, summary}`
- `{kind:'approval', phase:'pending', id, bot, description, command}` → yellow approval card;
  later `{kind:'approval', phase:'decided', id, choice:'once'|'session'|'always', by}` → accepted
- `{kind:'bridge', phase:'surface', bot}`
All need `ts` (seconds); dedupe key is `ts|kind|id/tool/phase`, so vary ts.

## Script skeleton (append before `</body>`, remove after)
```js
setInterval(tick, 650)  // msg every 2, tool every 3, skill every 4, approval every 7 (decided 2–5s later)
window.hpEq.demo(sec)   // headphone EQ
sweep(fromRow, count, 520ms)  // drawn SVG cursor (fixed div) glides row to row; each row gets
                              // .demoHover (same CSS as hover) + dispatch mouseover → hero follows
scrollTour(8000)        // ease scrollTop of #view-wiki to bottom, then smooth back to 0
openEditor(row) / closeEditor(false)   // both top-level functions
document.body.classList.add('space'); showView('senter')  // SPACE; reverse after ~8s
```
Trigger = fixed `<button id="demoGo">` (URL flags are stripped by the pane) →
`drive_preview click selector=#demoGo`.

## Recording
```
rm -f ~/Desktop/senter-demo.mov
(screencapture -v -V 52 -x ~/Desktop/senter-demo.mov >/tmp/rec.log 2>&1 &); sleep 2
# then drive_preview click #demoGo; stay silent so the sidebar shows steady state
sleep 54; mdls -name kMDItemDurationSeconds ~/Desktop/senter-demo.mov
```
Full-screen capture = Hermes chat sidebar left + wiki pane right, as Chris uses it. No ffmpeg on
this Mac; the .mov is the deliverable (3024×1964, ~200 MB/50 s).

## Gotchas
- Record AFTER the current visual state is approved; a demo shot before the usage-chart fix had
  empty chart cells and had to be redone.
- `.demoHover` must replicate the hover CSS (band/underline `width:100vw`, title `--hfs`, orbs
  32px) — `:hover` can't be forced from JS.
- Keep the demo `<script>` and the `__senterHandle` hook marked `TEMP-DEMO` and strip both.
