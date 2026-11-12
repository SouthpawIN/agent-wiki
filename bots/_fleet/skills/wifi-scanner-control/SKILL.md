---
name: wifi-scanner-control
description: The shared protocol for driving the one flatbed scanner both bots use.
version: 1.0.0
author: Klerik
license: MIT
metadata:
  hermes:
    tags: [scanner, saned, escl, cups, shared, pocketshop, ssi]
---

# wifi-scanner control

One physical scanner, two bots that want it: **Binder** (`pocketshop`) scans cards
at 600 dpi colour, **Beacon** (`ssi`) scans documents at 300 dpi to multi-page
PDF. Setup is not this skill's job — `pocketshop/skills/printer-onboarding` owns
bringing the device online and writing the presets. This skill is the **runtime
contract**: how either bot takes the device, scans, and gives it back without
cropping the other's batch.

Nothing here prints, spends money, publishes, or leaves the machine.

## The shared state file

`data/scanner.json` is the single source of truth, written once by
`printer-onboarding` and edited only through a `[BOTS]` line in the fleet queue:

```json
{"device": "airscan:e0:<name>",
 "card": {"dpi": 600, "mode": "Color", "out": "cards/"},
 "doc":  {"dpi": 300, "mode": "Gray",  "out": "scans/"}}
```

Read it, never hard-code a URI or a dpi in a bot's script. A device URI that
appears in two places is a bug the day the router hands out a new lease.

## Taking the flatbed

1. **Confirm the device before locking anything:**
   `scanimage -L` names exactly one device matching `scanner.json`. Two lines
   means an mDNS duplicate (`airscan:e0:` and `escl:`) — pick the `airscan` one
   and record the other as noise, do not delete the queue.
2. **Take the exclusive lock.** One flatbed serves one batch at a time:

   ```bash
   exec 9>data/scanner.lock
   flock -n 9 || { echo "device busy: $(cat data/scanner.owner 2>/dev/null)"; exit 3; }
   echo "<bot> <job-id> $(date -Is)" > data/scanner.owner
   ```

   `flock -n` failing is a normal outcome, not an error: report who holds it and
   move to the next queue item. Never `flock -w` for more than 120 s — a card
   batch that legitimate-takes 20 minutes will look like a hang otherwise.
3. **Scan with the preset, never with an improvised resolution:**

   ```bash
   # cards — one PNG per card, 600 dpi is the floor for collector numbers
   scanimage -d "$DEV" --source Flatbed --mode "$MODE" --resolution 600 \
             --format=png --output-file "cards/${sku}.png"
   # documents — one PDF per document, pages in feed order
   scanimage -d "$DEV" --source Flatbed --mode Gray --resolution 300 \
             --format=pnm | img2pdf -o "scans/${doc}.pdf"
   ```

   Cards are always `--source Flatbed`: an ADF batch on a card stack eats the
   corner with the set symbol. Documents may use the ADF only when the job names
   a page count and `--batch` is given an explicit `--batch-count`.
4. **Verify the scan before releasing the lock.** A 0-byte file or a
   uniformly black page is a failed scan, not a bad card:
   `pngcheck -q cards/<sku>.png` (or `identify -format '%[mean]'` — a mean under
   ~2000 on an 8-bit scan means the flatbed was not initialised). Re-run **once**;
   a second failure is a device fault, so release the lock and file it.
5. **Release and hand off:** `rm -f data/scanner.owner; exec 9>&-`. Append one
   line to the bot's own ledger naming job, count, and device URI, so the other
   bot can see the last clean scan without opening a file.

## Collision policy

| Window (local) | Owner | Job |
|---|---|---|
| 07:00–19:00 | `pocketshop` | card batches, 600 dpi colour |
| 19:00–07:00 | `ssi` | documents, 300 dpi PDF |

The window is a default, not a gate: a deadline-bound document outranks cards at
any hour (`ssi/loops/deadline-watch` wins), and a card batch already holding the
lock is never interrupted mid-sheet. Neither bot changes `scanner.json` (dpi,
mode, source, ADF) without a `[BOTS]` line — a silent ADF switch mid-batch
crops half a card and the loss is invisible until grading.

## Verification

- One device listed by `scanimage -L`, matching `scanner.json`.
- The scan exists, is non-zero, and opens; a card PNG shows a legible collector
  number, a document PDF has straight edges and pages in order.
- `data/scanner.owner` is gone after the job; a second bot can take the lock
  immediately afterwards.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| `flock -n` fails | other bot holds the flatbed | read `owner`, skip this job, retry next tick |
| `scanimage: open of device failed: Invalid argument` | stale URI after DHCP moved the device | re-read `scanner.json`; if the URI is old, file a `[BOTS]` line, do not edit it |
| Black page | lid not initialised, or `--source ADF` with empty feeder | re-run once with `--source Flatbed` |
| Pages reversed in PDF | ADF duplex guess | print `--source Flatbed`, one page per call |
| Collector number unreadable | 300 dpi | 600 dpi colour, no auto-exposure |

## Not this skill's job

- Driver install, CUPS queue creation, preset authoring → `printer-onboarding`.
- Card cropping, deskew, OCR → `pocketshop`'s `card_scanner.py`; this skill hands
  it a flat 600 dpi PNG and nothing else.
- Document classification, deadline math → `ssi`'s `document-intake`.
- Printing. A print queue is a second `lpadmin` device, not a mode of this one.
