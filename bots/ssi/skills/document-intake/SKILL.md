---
name: document-intake
description: Scan, name, read and file a benefits document so nothing is lost.
version: 1.0.0
author: Beacon
license: MIT
metadata:
  hermes:
    tags: [scan, intake, benefits, records, ocr]
---

# Document intake

Every page gets a name and a row before it gets read. Filing first is what makes
a 40-page notice survivable.

## Procedure

1. **Scan** 300 dpi, grayscale, PDF with a text layer (OCR at scan time if the
   scanner supports it; otherwise `ocrmypdf --skip-text in.pdf out.pdf`).
2. **Name** immediately: `YYYY-MM-DD_<ssa|hhsc|school|medical>_<doctype>_<initials>.pdf`.
   Unknown date → use the postmark date, never today's date.
3. **Extract the ask** into `cases/<initials>/intake.md`:
   - Who sent it (agency, office, address)
   - What they want (documents, interview, form, payment)
   - Due date, verbatim
   - Consequence of missing it, verbatim
   - Any case/reference number
4. **Update two tables**: `_programs.md` (status changed?) and `_deadlines.md`
   (new dated obligation). If neither changes, write `no action` in the timeline.
5. **Flag urgency**: hearing notice, denial with appeal rights, or a 10-day
   deadline → top of the deadline table and an immediate injection line.
6. **Never discard the original.** The scan is a copy; the paper stays in a
   physical folder labeled with the same date.

## Rules

- Never retype a number from a scan without confirming it twice — account and case
  numbers are the #1 source of mis-filed paperwork.
- Never summarize a denial into "denied". Copy the stated reason verbatim; the
  reason determines the appeal.
