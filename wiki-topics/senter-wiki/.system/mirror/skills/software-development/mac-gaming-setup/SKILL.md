---
name: mac-gaming-setup
description: Use when installing Steam or games on a Mac.
---

# Mac Gaming Setup (Steam et al.)

## Installing Steam on macOS
1. Download the DMG from the link on https://store.steampowered.com/about/ (resolve it with `curl -sL https://store.steampowered.com/about/ | grep -oE 'https://[^\"]*\\.dmg'`) — hardcoded CDN URLs go stale/404.
2. Mount (`hdiutil attach -nobrowse`), `cp -R Steam.app /Applications/`, `xattr -dr com.apple.quarantine`.
3. **Apple Silicon: Steam's binary is Intel-only.** `open` fails with error -10669 until Rosetta 2 is installed: `softwareupdate --install-rosetta --agree-to-license`. First launch self-updates (bootstrap downloads ~1.2GB into `~/Library/Application Support/Steam/Steam.AppBundle`) — wait for that before diagnosing anything.

## Login
- Existing installs auto-login from `~/Library/Application Support/Steam/config/loginusers.vdf` (check `AutoLogin`, `AccountName`). Don't ask the user for credentials before checking this — the client often logs in silently.
- Steam Guard may email a code; the user must relay it. Never store passwords; recommend the user rotate any password shared in chat.

## Ghost-window problem (Steam running but invisible)
Symptoms: `open` succeeds, process runs, but no window; System Events shows the window at 1×1 or position -15000. Key insight: **Steam's real windows are owned by the `Steam Helper` process, not `steam_osx`** — query/capture/steer `Steam Helper`, not `steam_osx`. The window list via `CGWindowListCopyWindowInfo` (swift one-liner) may include offscreen junk (1×1 at -15000) — filter by size.
- Enumerate real windows: swift CoreGraphics window-list dump filtered to owner `Steam Helper` / `Steam`.
- Clicks: computer_use `app=` should be `Steam Helper`. AX tree is nearly empty (CEF-rendered UI) — click by pixel coordinate from a vision capture, scaling image→native coords (screenshots may be 1.077x native points; verify with window bounds from the CG list).
- `steam://` URL schemes are far more reliable than clicking: `steam://open/games`, `steam://open/downloads`, `steam://install/<appid>`, `steam://nav/library`. Use `open "steam://..."`.

## Installing the user's library
- Owned app IDs: scrape `~/Library/Application Support/Steam/appcache/librarycache/` directory names (each dir = appid), then resolve names via `https://store.steampowered.com/api/appdetails?appids=<id>&filters=basic` (some return no data — fine).
- Fire `open "steam://install/<appid>"` per game. Each pops an Install dialog (Install/Cancel) that normally auto-proceeds; keep 5-12s spacing.
- Verify via `steamapps/appmanifest_<id>.acf`: `StateFlags` 4 = fully installed (1026 = downloading). Check `du -sh steamapps/common/*` and `downloading/`. The Downloads page (`steam://open/downloads`) shows Completed/queue — trust manifests over screenshots.
- **Windows-only games fail with `"Invalid platform"` error dialogs.** These stack up and block the UI. macOS Steam often refuses to even queue them; don't loop retrying — collect which ones failed and report.
- Native-Mac-capable ≠ installed: check the store page's platform icons. Free-to-play titles (Destiny 2 etc.) still count as owned games but may be Windows-only.

## Windows-only games on Apple Silicon
Paths, best-first: CrossOver (paid, trial; best Where Winds Meet / NARAKA results), Whisky (free, unmaintained), Game Porting Toolkit, cloud (GeForce NOW/Boosteroid, needs owned game + 25 Mbps), MuMuPlayer for mobile ports. Anti-cheat titles (Destiny 2, GTA Online) are effectively cloud-only — say so instead of promising local play.

See references/steam-macos-session-notes.md for detailed pitfalls from a real run.