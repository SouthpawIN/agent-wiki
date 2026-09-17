---
name: windows-games-on-mac
description: Use when installing Windows Steam games on a Mac via Wine.
---

# Running Windows Steam Games on macOS (Wine/Whisky)

Proven end-to-end path for getting Windows-only Steam games (Palworld, AC6, Where Winds Meet, etc.) working on an Apple Silicon Mac.

## Key facts

- **Original Whisky is dead** (archived 2025): its runtime download endpoint returns 404, so "Dependencies Setup" hangs at `WhiskyWine not installed` forever. Log signature: `response_status=404` in Whisky process logs.
- **Use the maintained fork**: `frankea/Whisky` (https://github.com/frankea/Whisky/releases) — signed/notarized DMG, downloads WhiskyWine fine, supports `File → Migrate from the Original Whisky`.
- Gatekeeper may show a stale **"app is damaged"** alert for a properly notarized app after a first failed launch — the LS/provenance record is stuck. Fix: quit app, delete, re-extract with `ditto` from the DMG, `xattr -cr`, `lsregister -f`, rename the .app (new LS identity), relaunch.
- Mac Steam itself is Intel-only → needs **Rosetta 2** (`softwareupdate --install-rosetta --agree-to-license`).
- Some Steam library games are Windows-only: install attempts fail with `Invalid platform` dialog on Mac Steam. This is expected, not a bug.

## Setup outline

1. Download fork DMG, `ditto` to /Applications, `xattr -cr`, launch.
2. Setup wizard → Next → WhiskyWine downloads (~330 MB, works on fork).
3. Create bottle (name e.g. "Games", Windows 10).
4. Install Windows Steam: download `SteamSetup.exe` (https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe), install into the bottle. **Silent install works reliably**: run `wine64 SteamSetup.exe /S` from terminal with WINEPREFIX set (see below) instead of fighting the Whisky Run... dialog.
5. Launch `wine64 steam.exe` from the bottle's `Program Files (x86)/Steam` — it self-updates then shows login. Account login carries over if "Remember me" was set elsewhere.

## The reliable technique: terminal-driven Wine

Whisky's GUI (wine has **no AX windows** — System Events sees zero; computer-use clicks land unreliably on its CEF dialog). For anything deterministic, bypass the GUI:

```bash
export WINEPREFIX="$HOME/Library/Containers/com.isaacmarovitz.Whisky/Bottles/<UUID>"
export WINEESYNC=1 WINEMSYNC=1
WINE="$HOME/Library/Application Support/com.franke.Whisky/Libraries/Wine/bin/wine"
cd "$WINEPREFIX/drive_c/Program Files (x86)/Steam"
"$WINE" steam.exe -silent &          # launch client
"$WINE" SteamSetup.exe /S &          # silent installer
```

Run these as `terminal(background=true)` — wine processes are long-lived.

## Best trick: pre-seed appmanifest to skip install dialogs

Clicking the install dialog's **Install** button via synthetic clicks frequently misses/fails. Instead, when Steam is quit:

1. Write a minimal `appmanifest_<appid>.acf` into the bottle's `steamapps/` with `StateFlags "1026"` (update-required), `BytesDownloaded 0`, correct `installdir` and `LastOwner` (user's SteamID3 from their Mac-Steam loginusers.vdf).
2. Relaunch `steam.exe -silent`. Steam sees the app as needing install/update and downloads **without any dialog**.
3. Completion check: `StateFlags "4"` in the manifest + `downloading/` folder at 0 bytes.

Get appids from the bottle's `appcache/librarycache/` (numeric dirs) or the owned-games list; verify names via `store.steampowered.com/api/appdetails?appids=<id>&filters=basic`.

## Gotchas

- Bottle prefix materializes **only on first Wine run** — a fresh bottle with just Metadata.plist is normal until wineboot/first launch.
- Wine windows may exist but be offscreen/1x1 — enumerate with a `CGWindowListCopyWindowInfo` Swift one-liner (System Events can't see them).
- `screencapture -x -D 1` returns an all-black image when the display is asleep/locked — `caffeinate -u -t 5` first.
- Vision-model coordinate estimates on scaled screenshots are ±; convert with the actual scale (native px / screenshot px) and expect retries.
- Steam's own self-update can hang at "Installing update..." — kill steam.exe/wineserver and relaunch; it resumes and completes.
- Disk space: these games are huge (Palworld 38 GB, AC6 52 GB, Where Winds Meet 177 GB). Check free space before starting.

## Status conventions

- StateFlags: 4 = fully installed, 1026 = update/download pending.
- Cloud saves sync per-account; the same Steam account can be logged in on Mac Steam and bottle Steam simultaneously.
