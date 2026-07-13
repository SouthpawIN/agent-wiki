# Android STS Surface Prototype

This is a browser-executable prototype of the agreed Senter Android interaction contract. It is source-controlled in the Agent Wiki sandbox because the pinned `hermes-android` repository currently contains a prebuilt APK and Termux scripts, not Android source.

## Run

```bash
python3 -m http.server 8765 --directory sandbox/android-surface
```

Open `http://localhost:8765`.

## Implemented prototype behavior

- Side button opens compact STS mode.
- Tap action icon sends input to the canvas.
- Double-tap action icon requests a screenshot and displays the permission-gated status.
- Drag action icon upward opens the expanded canvas.
- Expanded view has input, conversation canvas, building-block sidebar, and drag/drop blocks.
- Default blocks include `SESSIONS.md`, `CHAT.md`, `SENTER.md`, current topic, proposal queue, and Kanban status.

This prototype is not the Android APK and does not perform screenshots or phone operations. Those remain permission-gated platform capabilities for the future source-bearing Android client.

## Contract

See `../goop/ANDROID_SURFACE.json` and `../goop/validate_android_surface.py`.
