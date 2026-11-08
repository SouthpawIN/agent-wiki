---
name: printer-onboarding
description: Bring the shared Wi-Fi scanner online via CUPS + eSCL.
version: 1.0.0
author: Binder
license: MIT
metadata:
  hermes:
    tags: [scanner, cups, escl, sane, airport, setup, shared]
---

# Printer onboarding

One physical device serves two bots: `pocketshop` flatbeds cards, `ssi` scans
documents. This skill brings it online once, proves it with a real scan, and
pins the two presets so neither bot re-tunes the device mid-run.

Nothing here spends money, publishes, or sends anything external. All of it is
local, and every step is reversible.

## Inputs

- Printer model and IP (or hostname). Chris supplies both; a scan that cannot
  name the model is a guess, and guesses here cost a reinstall.
- Whether the box may print to it too, or scan only.

## Procedure

1. **Prove the host is reachable before touching drivers.**
   `ping -c 2 <ip>` then `avahi-browse -rt _ipp._tcp` and `_uscan._tcp`.
   No mDNS answer is normal on a segmented LAN — fall back to
   `ipp://<ip>:631/ipp/print` and `http://<ip>/eSCL/ScannerCapabilities`.
   Curling the eSCL capabilities URL returning XML is the single most useful
   signal that scan will work; a 404 means the model speaks WSD, not eSCL.
2. **Install the driverless path.** `sane-airscan` (eSCL/WSD over IPP) plus
   `cups` + `cups-client`. Driverless beats a vendor blob: no per-model .deb,
   nothing to re-break on upgrade. Vendor PPD only if the capabilities XML is
   absent.
3. **Register the queue.** `lpadmin -p <name> -E -v ipp://<ip>/ipp/print
   -m everywhere`. Then `lpstat -p <name>` must report idle, not "disabled".
4. **Confirm SANE sees it.** `scanimage -L` must list the device with a
   `airscan:e0:<name>` (or `escl:`) URI. If SANE is blind but CUPS is fine, the
   split is almost always `sane-airscan` missing — not the network.
5. **Scan for real, both presets, and keep the files as proof.**
   - Cards: `scanimage -d <dev> --mode Color --resolution 600 --format=png
     --output-file cards/<sku>.png` (600 dpi is the floor for collector-number
     OCR; 300 loses the number on dark borders).
   - Documents: `--resolution 300 --format=pnm` piped into `tiffcp`/`img2pdf`
     so `ssi` gets one multi-page PDF per document, not 40 PNGs.
   A scan that returns a black page means the flatbed was not initialised —
   re-run once before blaming the driver.
6. **Wire the card path back into the pipeline.** The saved PNG goes through
   `card_scanner.py` / `auto_card_processor.py` (crop, deskew) exactly as if it
   came from a phone photo; this skill never re-implements that crop.
7. **Publish the two presets** in `data/scanner.json`:
   `{device, card: {dpi: 600, mode: color, out: cards/},
     doc: {dpi: 300, mode: gray, out: scans/}}`. Both bots read the file, so a
   resolution change is one edit, not two.
8. **Hand the schedule to `ssi`.** Card batches take the flatbed in daylight
   hours; document scans take the evening. Neither bot may reconfigure the
   device (dpi, ADF, duplex) without a `[BOTS]` line in the fleet queue — a
   surprise ADF switch mid-card-batch silently crops half a card.

## Verification

- `scanimage -L` lists one device, `lpstat -p` says idle.
- Two files exist from step 5, and both open: a card at 600 dpi with a legible
  collector number, a document PDF at 300 dpi with a straight edge.
- `data/scanner.json` parses and names the same device URI as step 4.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| `scanimage -L` empty, CUPS idle | `sane-airscan` not installed | install it, `systemctl restart saned.socket` |
| eSCL capabilities 404 | WSD-only firmware | `sane-airscan` WSD path, or vendor PPD |
| Scan hangs at "warming up" | mDNS name resolve, not the scan | use the IP, never the `.local` name |
| PDF pages out of order | ADF duplex guess | force `--source Flatbed` for documents |
| Card number unreadable | 300 dpi | 600 dpi, colour, no auto-exposure |

## Not this skill's job

- Printing. If Chris wants print too, that is a second queue, not this one.
- Picking the device's IP statically — that is a router reservation, and it
  should be done once so the URI in `scanner.json` never rots.
