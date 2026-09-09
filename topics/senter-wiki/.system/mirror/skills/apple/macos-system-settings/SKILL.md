---
name: macos-system-settings
description: Change macOS settings via defaults, restart, verify.
version: 1.0.0
author: hermes-curator
license: MIT
tags: [macos, defaults, system-settings, siri, widgets, dock, preferences]
metadata:
  hermes:
    tags: [macos, defaults, system-settings, siri, widgets, dock, preferences]
    related_skills: [computer-use, findmy, imessage]
---

# macOS System Settings from the Terminal

## When to Use

Use when the user wants a macOS system-level setting changed, disabled, or cleaned up —
desktop widgets, Siri, Dock behavior, Finder, screenshots, menu bar items, hot corners,
Stage Manager — and they'd rather you just do it than be walked through System Settings.

Trigger phrases: "get rid of the widgets", "turn off Siri", "how do I disable X",
"can you just do it", "do both". Also use it when a user hands you a *list* of machine
setup chores on a fresh Mac — work the list top-down and confirm each item with a read-back.

Covers the whole class: **read current state → write with `defaults` → restart the owning
service → read back and prove it took.**

## The core loop (never skip a step)

```bash
# 1. READ current state first — know what you're changing and confirm the claim
sw_vers                                        # macOS version matters; keys move between releases
defaults read com.apple.WindowManager          # whole domain
defaults read com.apple.Siri VoiceTriggerUserEnabled   # single key

# 2. WRITE
defaults write <domain> <Key> -bool true

# 3. RESTART the service that reads the domain (settings are cached in the running process)
killall Dock                  # Dock, Mission Control, Stage Manager, desktop widgets
killall SystemUIServer        # menu bar items
killall Finder                # Finder prefs
launchctl kickstart -k "gui/$(id -u)/com.apple.Siri.agent"   # Siri agent

# 4. VERIFY — read the keys back and show the user the actual values
defaults read com.apple.WindowManager StandardHideWidgets
```

Step 4 is the deliverable. Report the real read-back values, not "I applied the setting."

## Verified recipes

### Hide desktop widgets (macOS Sonoma 14+ through 26)
```bash
defaults write com.apple.WindowManager StandardHideWidgets -bool true      # on the desktop
defaults write com.apple.WindowManager StageManagerHideWidgets -bool true  # in Stage Manager
killall Dock
```
These hide desktop widgets. **Notification Center widgets are a separate surface** and are
NOT affected — mention this explicitly or the user will think it half-worked. Notification
Center widgets are removed per-widget from the panel itself (click date/time → Edit Widgets);
there is no clean single `defaults` key for them.

### Screenshots (save location, format, thumbnail)
```bash
mkdir -p ~/Pictures/Screenshots
defaults write com.apple.screencapture location -string "$HOME/Pictures/Screenshots"
defaults write com.apple.screencapture target -string "file"   # file | clipboard | preview
defaults write com.apple.screencapture show-thumbnail -bool true
defaults write com.apple.screencapture disable-shadow -bool false
killall SystemUIServer
```
Shortcuts themselves are `AppleSymbolicHotKeys` (28=⇧⌘3, 29/30=⇧⌘4, 31, 184=⇧⌘5). Verify
one is not disabled before assuming a keyboard problem:
```bash
/usr/libexec/PlistBuddy -c "Print :AppleSymbolicHotKeys:30:enabled" \
  ~/Library/Preferences/com.apple.symbolichotkeys.plist 2>/dev/null || echo "(unset = enabled)"
```
An absent entry means **default-enabled**, not broken.

### Disable Siri fully
```bash
defaults write com.apple.assistant.support "Assistant Enabled" -bool false   # Ask Siri (main switch)
defaults write com.apple.Siri VoiceTriggerUserEnabled -bool false            # "Hey Siri" listening
defaults write com.apple.Siri StatusMenuVisible -bool false                  # menu bar icon
defaults write com.apple.Siri LockscreenEnabled -bool false
defaults write com.apple.Siri TypeToSiriEnabled -bool false
launchctl kickstart -k "gui/$(id -u)/com.apple.Siri.agent"
killall SystemUIServer
```
Note the quoted key `"Assistant Enabled"` — it contains a space and breaks unquoted.

On recent macOS the pane is **System Settings → Apple Intelligence & Siri** (not the old
"Siri & Spotlight"). Tell the user that if the toggle ever reappears, flipping it off once
in that pane makes it stick, since System Settings can re-assert its own state over
`defaults`. Set the expectation up front rather than being surprised later.

## Desktop vs Dock — disambiguate first for new users

New Mac users often say "icon on desktop" when they mean the **Dock** (the bar at the bottom). Always clarify before acting:

```bash
# What's actually on the Desktop (background)?
ls -la ~/Desktop/

# What's in the Dock?
defaults read com.apple.dock persistent-apps 2>/dev/null | grep '"file-label"'
```

If the icon is in the **Dock** (not the Desktop):
- **GUI**: Drag it out of the Dock until "Remove" appears, then let go. Or right-click → Options → Remove from Dock.
- **Terminal**: Dock icon removal via `defaults` is fragile (must rebuild the full `persistent-apps` array). Prefer the GUI drag.

If the icon is on the **Desktop** (background):
- `computer_use(app='desktop')` does **NOT** work on macOS — it returns "no desktop/shell window found."
- `computer_use(app='screen')` returns a vision-only capture with **no interactable elements**.
- To click a Desktop icon: minimize other windows first (`cmd+m` won't work via `key` without a prior `capture`), then `click` by coordinate. Or just use `terminal`: `rm ~/Desktop/<file>` for files, or drag to Trash via Finder.

## Mounted DMG icons on the Desktop ("remove this from my desktop")

An icon like `AppName-1.2.3-universal` on the Desktop is usually a **mounted disk image**,
not a file. Check with `ls /Volumes/` and `hdiutil info` (gives the backing DMG path, e.g.
`~/Downloads/AppName-1.2.3.dmg`). Eject with:

```bash
hdiutil detach "/Volumes/AppName-1.2.3-universal"          # normal
hdiutil detach "/Volumes/..." -force                        # if "Resource busy" (Finder/Dock holding it)
```

`-force` only unmounts; it does not harm the DMG. Tell the user the DMG itself still lives
in Downloads and offer to delete it if the app is already installed.

**Corollary — "app is running slow/frozen/watcher broken"**: check `pgrep -fl` for
`AppTranslocation`. An app run from a mounted DMG is translocated (read-only sandbox),
which breaks file watching, saving preferences, and overall responsiveness. Fix: quit the
app, mount the DMG, `cp -R "/Volumes/.../AppName.app" /Applications/`, eject, then
`open -a AppName` from /Applications. Note `open -a Obsidian` fails with "Unable to find
application" while only the translocated copy is running — kill it first.

## Window layout for watching apps (HUD-style sessions)

When the user wants one app visible on top and the Hermes HUD docked at the bottom edge
(e.g. "put Obsidian on screen with Hermes along the bottom so I can watch edits live"):

1. `computer_use(app='Obsidian')` window matching often fails for Electron apps even when
   they're on screen ("no on-screen window found") — don't loop on it.
2. Use System Events via `osascript` instead (works after Accessibility is granted):
   - Position: `tell process "Obsidian" to set position of window 1 to {0, 25}` and
     `set size of window 1 to {1512, 600}` (top zone).
   - Hermes has TWO windows; the small one is the HUD: `position {0, 640} / size {1512, 230}`
     docks it along the bottom. List windows and match by size if unsure.
   - Raise with `set frontmost to true` / `perform action "AXRaise" of window 1`.
3. An osascript targeting System Events without Accessibility triggers a macOS
   "Accessibility Access" permission dialog — never click permission dialogs yourself;
   ask the user to grant, then retry. Unlike TCC screen-recording, the grant reached the
   already-running process fine in practice.
4. `computer_use` window bounds are in native desktop coordinates and can be scaled
   (~1.08x on this Retina panel) — use element bounds from captures, not screenshot pixels.

## Changing wallpapers

```bash
# Right-click desktop → Change Wallpaper
# Or: System Settings → Wallpaper

# Via terminal (applies to all desosascript -e 'tell application "System Events" to tell every desktop to set picture to "/path/to/image.jpg"'

# Built-in wallpapers live at:
ls /System/Library/Desktop\ Pictures/
```

Built-in categories: Dynamic Desktop (Solar Gradients, Big Sur, Sonoma), Landscapes, Abstract, Cityscapes, Space, Solid Colors.

## Pitfalls

- **"Screenshots don't work" is usually TCC, not the hotkey.** `screencapture -x /tmp/t.png`
  failing with `could not create image from display` means **Screen Recording** is not granted
  to the responsible process — the shortcuts are fine. Diagnose in this order: run the CLI
  capture (fastest proof), check the symbolic-hotkey enabled state, then look at whether any
  file was ever saved (`ls ~/Desktop/*.png`). An empty Desktop plus that error is a permission
  gate every time. Don't start reassigning keyboard shortcuts.
- **A newly granted TCC permission does not reach an already-running process.** macOS caches
  the grant per process, so a doctor/health check keeps reporting NOT granted even after the
  user genuinely flipped the toggle. Restart the *owning process* and re-probe before telling
  the user it didn't work — `killall <App>` then re-run the check. When a user says "check
  again, I just did it", this is almost always why the first probe still failed.
- **`TCC.db` is unreadable by design.** `sqlite3 ~/Library/Application Support/com.apple.TCC/TCC.db`
  returns `authorization denied` even as the owning user. Probe the *capability* (attempt the
  actual operation) instead of trying to read the grant table.
- **No restart = no visible change.** The user sees nothing happen, assumes it failed, and
  you look wrong. Always restart the owning service in the same batch.
- **Don't re-ask an approach the user already chose.** If they say "do both", "just do it",
  or "hit it via terminal", execute — do not come back with "GUI or terminal?". Being asked
  twice is what makes people repeat themselves. Offer the choice at most once, and only if
  they haven't already answered it.
- **Version-check before trusting a key.** `defaults` keys are renamed and dropped between
  macOS releases. Run `sw_vers` and read the domain first; if a key is absent, that's a
  signal, not a failure.
- **`defaults read` on a missing key exits non-zero.** Guard with `2>/dev/null` in
  verification blocks so one absent key doesn't abort the whole script.
- **Some domains are SIP/TCC-protected** and silently ignore writes (Full Disk Access,
  privacy toggles). If read-back doesn't match what you wrote, say so and route the user to
  the GUI pane — do not claim success.
- **Never disable security features** (Gatekeeper, SIP, FileVault, firewall) on a casual
  request. Confirm intent explicitly first.
- Prefer `killall Dock` over asking for a logout/reboot; reboots are rarely necessary.

## Fresh-Mac app installs without Homebrew (no `brew` on the machine)

When a setup chore needs a CLI/app and Homebrew isn't installed, don't route the user
through installing brew first — install direct from upstream:

- **gh CLI**: download the official release zip for the arch (`uname -m` → `arm64`),
  then copy the single binary — no package manager needed:
  ```bash
  curl -fsSL -o /tmp/gh.zip "https://github.com/cli/cli/releases/download/v<ver>/gh_<ver>_macOS_<arch>.zip"
  unzip -oq /tmp/gh.zip -d /tmp/ghx
  sudo mkdir -p /usr/local/bin && sudo cp /tmp/ghx/gh_*/bin/gh /usr/local/bin/
  ```
- **Tailscale on macOS**: prefer the Mac **App Store build** — but know both install
  variants and their failure modes (a machine can end up with BOTH registered):

  | Variant | Bundle ID | System Settings name | Needs admin password? |
  |---|---|---|---|
  | Standalone (zip / pkgs.tailscale.com) | `io.tailscale.ipn.macsys` | "Tailscale" | Yes — system extension install/repair prompts for it, and **loops** when given |
  | App Store | `io.tailscale.ipn.macos` | "Tailscale 2" | No — runs as a user-space `IPNExtension` network extension |

  - **Symptom: password prompt loops, CLI crashes with**
    `BundleIdentifiers.swift:47: Fatal error: The current bundleIdentifier is unknown to the registry`.
    The crash comes from `/usr/local/bin/tailscale` being a symlink to the *GUI app
    binary* (`/Applications/Tailscale.app/Contents/MacOS/Tailscale`), not a real CLI —
    diagnose with `ls -la /usr/local/bin/tailscale` and
    `defaults read /Applications/Tailscale.app/Contents/Info.plist CFBundleIdentifier`.
  - **Fix that needs no password** (verified): check for conflicting registrations with
    `scutil --nc list`, then start the App Store one directly:
    ```bash
    scutil --nc start "Tailscale 2"     # name as shown in scutil --nc list; may be "Tailscale 2" if both are registered
    ```
    Verify: `ifconfig` shows a `utunX` with a `100.x.y.z` address, and
    `ping -c 2 100.100.100.100` (MagicDNS responder) succeeds with 0% loss. The
    user-space daemon is `IPNExtension.appex` running as the user (`ps aux | grep IPNExtension`).
  - **Removal, verified end-to-end via GUI (no admin password needed)**: `scutil --nc` has NO
    remove command (only list/status/show/start/stop...). Real path: open the pane with
    `open "x-apple.systempreferences:com.apple.Network-Settings.extension"`, click the VPN row
    (in the right pane it's an unlabeled `AXButton` — the 2nd of 4, frame starts at y≈147),
    then the ⓘ info button of the stale entry (≈1236,94), then **Remove Configuration…**
    (≈709,526) → confirm in the sheet ("Are you sure… cannot be undone"). Verify with
    `scutil --nc list` and `networksetup -listallnetworkservices`. Leftovers that are fine to
    leave: the orphaned system-extension blob (`systemextensionsctl list` still lists it;
    purge with `sudo systemextensionsctl uninstall W5364U7YZB io.tailscale.ipn.macsys.network-extension`
    — never needs to be done in the same session).
  - `sudo -n` over messaging fails by default; the tip it prints says to add `SUDO_PASSWORD`
    to `~/.hermes/.env` — never enter the user's password into auth dialogs yourself, even
    if they paste it into chat.
  - **Listing tailnet peers from the Mac (no CLI available in the App Store variant):** there
    is no `tailscale status` equivalent. Best-effort enumeration: MagicDNS name probes
    (`dig +short <guess>.tailXXXXX.ts.net @100.100.100.100` — the tailnet name is in
    `scutil --nc status "Tailscale 2"` under DNSSearchDomains), PTR sweeps over the 100.64.0.0/10
    CGNAT space, and parallel ping sweeps of the local /24. Expect all three to miss devices
    that are offline/asleep (a phone will be). Zero hits does NOT prove a solo tailnet —
    when the user asks "is X on my tailnet", the definitive answer is the Machines page at
    `https://login.tailscale.com/admin/machines`; offer to read it from a browser pane
    instead of burning rounds on sweeps.
  - **Definitive LOCAL peer list: AX-walk the Tailscale GUI app.** The App Store app's main
    window has a Devices list with every peer's name and 100.x IP as AXStaticText — verified
    live, better than all DNS/ping sweeps (it shows offline devices too):
    ```bash
    osascript -e 'tell application "Tailscale" to activate'; sleep 3
    # then recursive System Events walk of process "Tailscale" window 1;
    # device name / IP pairs come back as consecutive AXStaticText nodes
    ```
    (Same recursive-AXFrame-walk pattern as the System Settings section below; on this class
    of app the window appears only after `activate`.) Do DNS/ping sweeps only to check
    reachability of specific peers afterwards (`ping -c 1 -W 2000 <100.x.y.z>` — an offline
    phone will not answer even though it is enrolled).

## Driving System Settings via AppleScript when clicks won't land

Ready-made helper: `scripts/ax-click.sh <x> <y>` — recursive AX walk + click (or `dump` mode
to list nearby buttons first). Same engine as the inline snippet below.

`computer_use` coordinate clicks on System Settings are unreliable (background delivery gets
refused for "minimized or hidden window"; foreground CGEvents often don't move the pointer;
`double_click` reported coordinates scaled ~1.43x from what was passed). Don't burn many
rounds on retries — switch to System Events directly. The reliable pattern is a **recursive
AX walk matching on AXFrame, then `click el`** (AppleScript `click` on an AX element works
even when synthetic mouse events don't):

```applescript
on walk(el, depth, tx, ty)
  tell application "System Events"
    try
      set r to role of el as string
    on error
      return ""
    end try
    if r is "AXButton" then
      try
        set f to value of attribute "AXFrame" of el
        if ((item 1 of f) as integer) is tx and ((item 2 of f) as integer) is ty then
          click el
          return "CLICKED"
        end if
      end try
    end if
    try
      set kids to UI elements of el
      repeat with k in kids
        set res to my walk(k, depth + 1, tx, ty)
        if res is "CLICKED" then return "CLICKED"
      end repeat
    end try
  end tell
  return ""
end walk
```

Workflow for System Settings panes:

1. Open the pane by URL: `open "x-apple.systempreferences:com.apple.Network-Settings.extension"`
   (Network; other panes: `com.apple.Siri-Settings.extension`, etc.). Confirm with
   `...tell process "System Settings" to get name of window 1`.
2. Enumerate before clicking — build a dump of roles + descriptions + AXFrames. Note panes
   show *two* nav systems: the left sidebar is `AXCell`s inside an `AXOutline`, and the right
   pane's rows are **unlabeled AXButtons** (disambiguate by frame; right-pane x starts ≈805).
3. AXFrame format is `x1, y1, x2, y2` (not x,y,w,h). Deep `entire contents` loops can
   silently return "" on error — a recursive `UI elements of el` walk is more robust.
4. When a confirmation sheet appears, its buttons are inside the window's element tree
   (not a separate `sheet 1` queryable in some macOS versions) — the same walk finds them.
5. Verify navigation actually happened after each click via the window *name* change
   (Network → VPN → back), and via static-text dumps of the pane.

Write AppleScript to a temp `.applescript` file and `osascript` it — heredoc/inline scripts
with embedded quotes get flagged or mangled; files don't.

## Voice / dictated sessions

The user may be dictating in the desktop app. Stray audio — a TV, a side conversation, a
half-finished thought — can arrive as a message that reads as nonsense or as an unrelated
topic. When that happens:

- Do **not** dump the whole prior context again or ask them to repeat themselves. Say in one
  line that it didn't land, and hold the thread where it was.
- If they ask "do I need to repeat everything?", the answer is no — restate the pending items
  compactly (one bullet each) and wait.
- Replies get cut off mid-sentence when they interrupt. Keep spoken-context answers
  front-loaded: the useful sentence first, caveats after.

## Reference

`references/verified-defaults-keys.md` — read-back-confirmed keys, domains, and the service each one requires restarting.

`references/new-mac-user-onboarding.md` — Desktop vs Dock disambiguation, `computer_use` macOS limitations, common fresh-Mac setup tasks.

`references/apple-silicon-local-llm-setup.md` — local LLM runtime bring-up on Apple Silicon (TurboFit case study): build order, memory-tier model selection, multi-agent branch workflow, failure signatures.
