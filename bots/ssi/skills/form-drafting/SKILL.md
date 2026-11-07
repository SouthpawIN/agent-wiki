---
name: form-drafting
description: Fill a benefits form from verified facts, leaving explicit blanks.
version: 1.0.0
author: Beacon
license: MIT
metadata:
  hermes:
    tags: [forms, ssi, medicaid, drafting, review]
---

# Form drafting

Output is a filled form plus a one-page review sheet. Never a submission.

## Procedure

1. **Identify the exact form and revision.** `SSA-8000-BK`, `SSA-3820-BK`,
   `SSA-827`, or the current HHSC application. Pull the current version from the
   agency site each time — forms and form numbers change, and an outdated revision
   gets returned.
2. **Build a fact sheet first**: names, DOBs, SSNs (last 4 only in working notes),
   address history, household members, income by source and month, resources,
   diagnoses with provider and date, school services. Every fact carries a source
   document path.
3. **Answer only from the fact sheet.** Anything not on it becomes
   `[[CONFIRM: what is needed]]`. A guessed date or dollar figure is out of bounds.
4. **Filled PDF via overlay**, not retyping into a new document — keep the
   agency's layout so a reviewer sees a normal form:
   ```bash
   python - <<'PY'
   from pypdf import PdfReader, PdfWriter
   # overlay a generated text layer onto the official blank form
   PY
   ```
   Alternatively fill the AcroForm fields directly when the PDF has them.
5. **Review sheet** (`review.md`, one page):
   - Form name + revision + page count
   - Facts used and where each came from
   - Every `[[CONFIRM]]` in a numbered list, with the easiest way to get it
   - Enclosures checklist (IDs, proof of income, medical records, releases)
   - Delivery method + address/fax/portal + the date it must go out
   - Signature lines Chris must sign, named by page
6. **Never sign, never submit.** Print-and-sign for paper, or a signature page if
   the agency accepts a scanned signature — his choice, his hand.
7. **Log** the draft in the case timeline with the date prepared.

## Escalate rather than draft

- A denial with a hearing deadline → draft the appeal AND name legal aid / a
  disability advocate in the review sheet.
- Anything asking about immigration status, custody orders, or a guardianship →
  stop and ask; wrong answers here have consequences beyond a returned form.
