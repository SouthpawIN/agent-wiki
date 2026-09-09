---
name: macos-gaming-setup
description: Use when installing Steam, games, or Wine layers on a Mac.
---

# macOS Gaming Setup

Install and recover gaming stacks (Steam, Wine layers, game libraries) on macOS machines.

## Core workflow: install Steam on macOS

1. Get the DMG from the store page link, NOT a guessed URL:
   - `curl -sL https://store.steampowered.com/about/ | grep -oE 'https://[^"]*\.dmg'` → currently `https://cdn.akamai.steamstatic.com/client/installer/steam.dmg`. The cloudflare CDN URL returns a 146-byte 404 stub — verify with `file` (should be `lzfse encoded, lzvn compressed`) before mounting.
2. `hdiutil attach <dmg> -nobrowse -quiet`, `cp -R "/Volumes/Steam/Steam.app" /Applications/`, detach, then `xattr -dr com.apple.quarantine /Applications/Steam.app`.
3. On Apple Silicon, the Steam binary is **x86_64-only** — install Rosetta first (`softwareupdate --install-rosetta --agree-to-license`) or `open` fails with error **-10669**.
4. First launch bootstraps ~1.2 GB into `~/Library/Application Support/Steam/Steam.AppBundle`. The client then runs as `steam_osx` under **Rosetta** (the visible process is `Steam Helper`, not `steam_osx` — window capture/list tools must target `Steam Helper`).
5. Login: existing users auto-login via `config/loginusers.vdf` (AutoLogin=1) — the password is NOT needed for a returning account. Verify login by `steamid`/`AccountName` in that file and cloud-sync lines in `logs/cloud_log.txt`.

## Installing the user's game library

- **Use `steam://` URL protocols instead of clicking the UI** — Steam-window clicks are unreliable (CEF coordinates, stale windows): `open "steam://install/<appid>"` per app, `steam://open/games` for library, `steam://open/downloads` for the downloads page, `steam://nav/library`.
- Verify installs on disk, not via screenshots: `~/Library/Application Support/Steam/steamapps/appmanifest_<appid>.acf` with `"StateFlags" "4"` = fully installed; check `steamapps/common/` sizes too. Progress reads: `du -sh .../steamapps/downloading`.
- Owned-app app IDs can be recovered from `appcache/librarycache/` directory names (they are app IDs) → map names via `https://store.steampowered.com/api/appdetails?appids=<id>&filters=basic`.
- **"Invalid platform" install failures = Windows-only game, not an error to fix.** Expect ~half of a typical library to fail this way on macOS. There may also be a stuck modal *Failure* dialog; dismissing it is unreliable — quitting and relaunching Steam clears it. Failed games remain listed in the library (greyed).
- Fire install URLs for Mac-native games FIRST, Windows-only ones last — each Windows-only failure pops a modal dialog that interferes with subsequent automation.

## UI automation without AX access

Steam's UI exposes almost nothing over AX (buttons render as unlabeled `AXButton`/`missing value`). Working pattern:
- Drive via `steam://` URLs and keyboard (osascript `key code 53` Escape, `keystroke return`) first; clicks only as last resort.
- For clicks: find window bounds via a Swift CGWindowList one-liner (owners: `Steam Helper`), then post CGEvents via ctypes (`CGEventCreateMouseEvent` + `CGEventPost`) at computed coordinates. Verify EVERY click with `screencapture -x -D 1` + `vision_analyze` — background CGEvent posts are unverified by the driver.
- If screenshots come back solid black, the display is asleep/locked: `caffeinate -u -t 5` to wake. A locked screen blocks all UI work — ask the user to unlock; app windows still exist behind it (visible via CGWindowList).
- Known Steam quirk: on some launches the main NSWindow spawns 1×1 at (-15000,15981) (offscreen). Deleting `~/Library/Saved Application State/com.valvesoftware.steam.savedState` and relaunching does not always fix it; windows may still be live under `Steam Helper` and clickable by absolute coordinate from CGWindowList bounds.

## Windows-only games on Mac (Wine layers)

See `references/windows-games-wine-mac.md` for the tooling landscape and `references/steam-mac-install-log.md` for a validated session record. Key durable facts:
- **Original Whisky (isaacmarovitz) is dead**: archived April 2025; its WhiskyWine runtime download endpoint returns **404**, so the first-run "Dependencies Setup" wizard can never complete. Do not waste time retrying it.
- The maintained path is the **`frankea/Whisky` fork** (signed/notarized, Wine 11, can migrate original-Whisky bottles in place via File → Migrate). Bottles live in `~/Library/Containers/com.isaacmarovitz.Whisky/Bottles/` (same container as original).
- Cloud gaming (GeForce NOW / Boosteroid) is the fallback for anti-cheat titles (CS2, Valorant, most kernel-anti-cheat FPS) — Wine cannot run those at all.
- CrossOver (paid) is the best-tested route for Steam-under-Wine; Wine ≤11.6 breaks Steam login (bcrypt opaque-key export unimplemented — auth fails locally with `Failed to poll auth session. Result 2`).

### Gatekeeper "damaged" loop (seen live)
A downloaded app can get stuck: every `open` re-raises *"X is damaged and can't be opened. You should move it to the Trash."* even after `xattr -cr`, when `spctl -a -t exec -vv` says *accepted*. Provenance records key on app NAME+path, so stale records survive re-copy to the same path. Escalating fixes, in order: copy to a NEW filename (`mv` → new bundle name → `lsregister -f` → relaunch); launch the inner binary directly (`/Applications/X.app/Contents/MacOS/Binary`); last resort ad-hoc re-sign (`codesign --force --deep -s -`) — note that breaks the notarization that spctl accepted, so try the rename first.
