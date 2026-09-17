# restore-hdiutil — wiki index
> One line per page. The wiki row's CONTEXT section renders this file.
> Last updated: 2026-09-16 | Total pages: 7

## Entities
- [[topics/restore-hdiutil/wiki/entities/hdiutil|hdiutil / restore verb]] — `hdiutil` is macOS's disk-image command-line tool. Chris tried to use its **`restore`** verb to write the Omarchy ISO straight to a USB device (`/dev/rdisk4`) —
- [[topics/restore-hdiutil/wiki/entities/omarchy|Omarchy ISO (v4.0.3)]] — **Omarchy** is a Linux distro Chris is trying to install onto an **HP** machine by flashing a bootable USB. [^raw1]

## Concepts
- [[topics/restore-hdiutil/wiki/concepts/usb-instability|USB drive instability]] — While flashing the Omarchy ISO, Chris's USB drive exhibited hardware-level problems. [^raw1]

## Decisions
- [[topics/restore-hdiutil/wiki/decisions/omarchy-iso-flash|Omarchy ISO flash]] — **Goal:** write `~/tmp/omarchy/omarchy-4.0.3.iso` to a USB and boot it on an HP to install Omarchy v4.0.3. [^raw1]
- [[topics/restore-hdiutil/wiki/decisions/wiki-structure-rebuild|2026-09-16 wiki structure rebuild]] — The topic's wiki scaffolding was rebuilt on 2026-09-16 after hermes reported the structure was wrong. [^raw1]

## Comparisons
- [[topics/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods for the Omarchy ISO]] — Three ways to write the Omarchy image to a USB, and what the raw log says about each. [^raw1]

## Queries
- [[topics/restore-hdiutil/wiki/queries/why-does-hdiutil-restore-fail|Why does `hdiutil restore` fail here?]] — **Question:** Chris ran `hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4` and got `restore: verb not recognized` (exit 1), even though the 

