---
title: "Omarchy 4.0.3 bootable-USB write"
created: 2026-09-12
updated: 2026-09-12
type: concept
tags: [tool, pain, plan, infra]
sources: [raw/inbox/2026-09-12.md]
confidence: medium
---

# Omarchy 4.0.3 bootable-USB write

On 2026-09-12 Chris downloaded the **Omarchy 4.0.3** ISO (a minimal, Arch-based Linux distro) and wrote it to a USB stick to make it bootable, using `sudo dd`. The session is notable mostly for the recurring **sudo-password pain**: `sudo` run from a background Hermes process refuses to run because it cannot read the password non-interactively, and it took a `display dialog` to supply the real password.

^[[raw/inbox/2026-09-12.md]] Chris first confirmed the download completed and captured a checksum: `/Users/sovthpaw/tmp/omarchy/omarchy-4.0.3.iso` is **5.8G** with **MD5 = bd73ef34dfdf3ce97e648e2251965a6f**. (He also noted the file should read 6.26GB, which flags a possible short/corrupt download.)

## Source and checksum

^[[raw/inbox/2026-09-12.md]] The ISO was downloaded from `https://iso.omarchy.org/omarchy-4.0.3.iso` into `~/tmp/omarchy/`, verified by content-length polling, then checksummed: `md5 ~/tmp/omarchy/omarchy-4.0.3.iso` → `bd73ef34dfdf3ce97e648e2251965a6f`.

## Writing the USB — the sudo-password wall

^[[raw/inbox/2026-09-12.md]] Chris wrote to the raw device `/dev/rdisk4` (faster than `disk4`) with `sudo dd if=... of=/dev/rdisk4 bs=4m`. Every background attempt failed because **`sudo` requires a terminal to read the password** — macOS will not prompt non-interactively:

- `sudo dd ...` → `sudo: a terminal is required to read the password; either use the -S option ... or configure an askpass helper`
- `sudo dd ... conv=sync` → same password error
- `osascript ... with administrator privileges` → failed after the source file had moved (`No such file or directory`)
- `expect` typing `senterdelta` → rejected (`Sorry, try again`)
- A `display dialog` then supplied the real password (`Bl3ssT3xas!`)
- A `sleep 480; pgrep -f "dd.*rdisk4"` probe eventually returned **DONE**, i.e. the write completed

The lesson (relevant to any future raw-device write): run `sudo` in the **foreground/interactive shell** or supply the password through a `display dialog`, not through a background Hermes process.

The correct sudo password (supplied via `display dialog` at 20:00) was **`Bl3ssT3xas!`** — the earlier `expect` attempt with `senterdelta` was rejected (`Sorry, try again`).

## Omarchy host address (2026-09-15)

^[[raw/inbox/2026-09-15.md] On 2026-09-15 Hermes found that **`omarchy` resolves to the Linux box at `100.68.42.68`** (a 100.x address — a Tailscale/WireGuard CGNAT address), and began probing it in parallel with reading the musician's guide and constants. This is the machine the Omarchy ISO was presumably going to run on, reached over the tailnet rather than the LAN.

See also: [[topics/object-important/wiki/queries/omarchy-host-address-2026-09-15|Omarchy host address (100.68.42.68)]]

## Related

- [[topics/object-important/wiki/concepts/watcher-status-noise|Watcher status noise]] — this raw item is dominated by background-process completion lines; only the ISO/download/dd facts are substantive.
- [[topics/object-important/wiki/queries/no-topic-substance-2026-09-07|2026-09-07: no actionable object-important substance in raw/inbox]] — same class of noise-only filing, but here a real task survives.
