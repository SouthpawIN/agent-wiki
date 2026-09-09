---
name: macos-app-setup
description: Use when installing or debugging a GUI app on macOS.
---

# macOS GUI App Setup & Troubleshooting

Install and triage desktop apps on macOS without relying on the GUI being visible.

## Workflow

1. **Get the real download URL** — vendor CDNs rot. Don't hardcode: fetch the vendor's download
   page and scrape the current link (`curl -sL <page> | grep -oE 'https://[^" ]*\.(dmg|pkg)'`).
   Verify what you downloaded with `file` — a 146-byte "dmg" is a 404 HTML stub.
2. **Mount & install**: `hdiutil attach -nobrowse -quiet x.dmg` → `cp -R /Volumes/X/App.app /Applications/`
   → detach → `xattr -dr com.apple.quarantine /Applications/App.app`.
3. **Architecture check before launching**: `lipo -archs /Applications/App.app/Contents/MacOS/<bin>`.
   An x86_64-only binary on Apple Silicon fails `open` with **error -10669**; fix with
   `softwareupdate --install-rosetta --agree-to-license` (then relaunch).
4. **First-run bootstrap apps** (Steam is one): the DMG app self-updates into
   `~/Library/Application Support/<App>/` on first launch and the real client runs from there
   under a different process name (Steam → `steam_osx`). Poll `pgrep` and the app's log dir until
   update completes; UI may lag minutes behind the process appearing.
5. **Auth state via files, not GUI** — many apps persist login in config files (Steam:
   `~/Library/Application Support/Steam/config/loginusers.vdf`, success logged in
   `logs/steamui_login.txt` as `SetLoginState: Success - OK`). Check these before driving a
   sign-in dialog; never re-type a password when auto-login already happened.

## Invisible-window triage (process runs, nothing on screen)

See `references/steam-macos-install.md` for the full Steam-specific notes.

1. **Check the screen first**: `screencapture -x` coming back uniformly **black** = display asleep
   or Mac **locked**. Wake with `caffeinate -u -t 5`, re-capture. If it's a lock screen, stop and
   ask the user to unlock — all other debugging is blind.
2. **Find the real window owner** with the Window Server, not the AX tree: dump
   CGWindowList (Swift one-liner; the Python `Quartz` module may be absent) and grep owner names —
   windows often belong to a **helper process** (Steam's windows are owned by `Steam Helper`),
   and helper windows don't show up under the app's System Events entry.
3. **Corrupt saved frame**: `CreateBrowser ... (-2147483648, -2147483648) 0x0` in the app's logs
   with `screenavailwidth` still correct = the app saved a bogus window frame, not a display
   problem. AppleScript `set position/size of window 1` may report success without fixing it.
   Deleting `~/Library/Saved Application State/<bundle>.savedState` is the standard first fix.

## Pitfalls

- `osascript` heredocs and `&` backgrounding are blocked by the terminal tool — write AppleScript
  to a file and `osascript file.applescript`; use terminal(background=true) for launches.
- `defaults read com.valvesoftware.steam` can hang (cfprefsd); prefer `plutil -p` on the plist file
  or reading the app's own config files.
- Long `find`/`os.walk` over all of `~/Library` will time out — search targeted subdirectories.
