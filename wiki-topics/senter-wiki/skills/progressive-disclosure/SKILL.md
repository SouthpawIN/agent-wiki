---
name: progressive-disclosure
description: Use before answering anything about a Senter topic. Read the wiki memory layer INDEX → file → section, never whole files.
version: 1.0.0
---
# progressive-disclosure — reading the memory layer
Chris (2026-09-05): the wiki is Hermes's memory layer; topics hold EVERYTHING (full transcripts, specs, source). Nobody loads
5 MB. Read like skills are discovered:

1. **Row** — the wiki list / `.system-live.json` gives topic name + summary lines.
2. **`wiki-topics/<t>/.system/INDEX.md`** — one line per file (size, gist) + heading outline with line numbers (built by
   `assets/build-index.py`, refreshed by the scanner on every pass).
3. **File** — pick the one file whose gist matches.
4. **Section** — `read_file(path, offset=<heading line>, limit=<next heading − offset>)`.

Rules
- Never `cat` a session transcript; grep it (`search_files pattern path=wiki-topics/<t>/.system/sessions`) then read the hit ±40 lines.
- Prefer `continuity.md` for "what does the system think", `queue.md` for "what's pending", `inbox.md` for "what did Chris just say".
- Write-back: anything learned that isn't in the wiki goes into the topic (inbox or continuity), otherwise it is not remembered.
