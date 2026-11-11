---
name: faq-distill
description: Fold repeated answered questions into a pinned-FAQ draft for mods.
version: 1.0.0
author: Anser
license: MIT
metadata:
  hermes:
    tags: [faq, moderation, distillation, discord, citations]
---

# FAQ distill

Used weekly, and after any day with more than five repeats. It reads the answer
log, clusters questions that are the same question wearing different words, and
writes a **draft** for a mod to pin. Anser never pins its own answers: a pinned
FAQ is a public statement, and public statements are a human's call.

## Input contract

`bots/anser/data/answers/*.md`, one file per answered question, written by
`grounded-answer` step 8:

```markdown
---
question: What is Hermes's context window?
asked: 2026-11-02
confidence: high          # high | medium | low | none
sources: ["https://x.com/NousResearch/status/1 (2026-10-30)"]
---

128k tokens by default in the installed model config.
```

The distiller needs `question` and `asked`. `sources` and `confidence` decide
whether an entry may be drafted at all. A file missing `question` is skipped
silently; a file missing `sources` counts as unanswered.

## Procedure

1. Run the distiller from the repo root. It writes
   `bots/anser/data/faq/draft.md` and prints counts:

```bash
cd "$(git rev-parse --show-toplevel)" && python3 - <<'PY'
"""Fold data/answers/*.md into a pinned-FAQ draft for mods."""
import datetime as dt, re, sys
from pathlib import Path

STOP = set("a an the is are was do does did to of in on for and or my i you it "
           "what whats how when which can could will would should".split())
STALE_DAYS, MIN_ASKS, SAME, DISAGREE = 90, 2, 0.62, 0.55
NUMWORDS = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
            "eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,
            "fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,
            "nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,
            "seventy":70,"eighty":80,"ninety":90,"hundred":100,"thousand":1000}

def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip().lower()] = v.strip()
        body = m.group(2)
    return {"slug": path.stem, "question": meta.get("question", "").strip(),
            "asked": meta.get("asked", ""), "confidence": meta.get("confidence", "").lower(),
            "sources": re.findall(r'(https?://[^\s",\]]+)(?:\s*\((\d{4}-\d{2}-\d{2})\))?',
                                  meta.get("sources", "")),
            "answer": " ".join(body.split())}

def tokens(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1}

def sim(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0

def numbers(s):
    out = set()
    for w in s:
        if any(c.isdigit() for c in w):
            core = w[:-1] if w.endswith("k") and w[:-1].isdigit() else w
            try: out.add("#%d" % int(core.replace(",", "")))
            except ValueError: out.add(core)
        elif w in NUMWORDS:
            out.add("#%d" % NUMWORDS[w])
    return out

def conflict(a, b):
    ta, tb = tokens(a), tokens(b); na, nb = numbers(ta), numbers(tb)
    if na and nb and not (na & nb): return True
    if (ta and ta <= tb) or (tb and tb <= ta): return False
    if len(ta) < 8 or len(tb) < 8: return False
    return sim(ta, tb) < DISAGREE

def date(s):
    try: return dt.date.fromisoformat(s.strip()[:10])
    except ValueError: return None

def main(root):
    base = Path(root) / "data" / "answers"
    recs = [r for r in (parse(p) for p in sorted(base.glob("*.md"))) if r["question"]]
    if not recs:
        print("no answers under %s — nothing to distill" % base, file=sys.stderr); return 0
    clusters = []
    for rec in sorted(recs, key=lambda r: date(r["asked"]) or dt.date.min):
        sig = tokens(rec["question"])
        for c in clusters:
            if sim(sig, tokens(c[0]["question"])) >= SAME:
                c.append(rec); break
        else: clusters.append([rec])
    today = dt.date.today(); pinned, singles, unresolved, clashes = [], [], [], []
    for c in clusters:
        asks = sorted(c, key=lambda r: date(r["asked"]) or dt.date.min)
        good = [r for r in asks if r["confidence"] not in {"none", "low"} and r["sources"]]
        if not good: unresolved.append(asks[-1]); continue
        if len(asks) < MIN_ASKS: singles.append(asks[-1]); continue
        best = max(good, key=lambda r: date(r["asked"]) or dt.date.min)
        if any(conflict(best["answer"], r["answer"]) for r in good if r is not best):
            clashes.append((asks[0]["question"], [r["slug"] for r in good])); continue
        newest = max((date(d) for _, d in best["sources"] if d), default=None)
        cite = best["sources"][0]
        pinned.append({"question": asks[0]["question"], "variants": len(asks),
                       "first": asks[0]["asked"], "last": asks[-1]["asked"],
                       "answer": best["answer"], "cite": cite[0] + (" (%s)" % cite[1] if cite[1] else ""),
                       "stale": bool(newest and (today - newest).days > STALE_DAYS)})
    out = ["# FAQ draft", "",
           "Generated %s from %d logged answers (%d distinct questions). "
           "Draft only — a mod pins it." % (today.isoformat(), len(recs), len(clusters)),
           "", "## Pinned candidates (%d)" % len(pinned), ""]
    for p in sorted(pinned, key=lambda p: (-p["variants"], p["first"])):
        out += ["### %s" % p["question"],
                "asked %dx · %s → %s%s" % (p["variants"], p["first"], p["last"],
                                           " · **stale source**" if p["stale"] else ""),
                "", p["answer"], "", "Source: %s" % p["cite"], ""]
    out += ["## Not answerable yet (%d)" % len(unresolved), ""]
    out += ["- %s — asked %s; no public source. Escalate, do not draft."
            % (r["question"], r["asked"]) for r in unresolved]
    out += ["", "## Asked once (%d)" % len(singles), ""]
    out += ["- %s — %s" % (r["question"], r["asked"]) for r in singles] + [""]
    if clashes:
        out += ["## Conflicting answers (%d) — human decides" % len(clashes), ""]
        out += ["- %s — answers disagree: %s" % (q, ", ".join(s)) for q, s in clashes] + [""]
    dest = Path(root) / "data" / "faq" / "draft.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print("wrote %s: %d pinned, %d unresolved, %d singles, %d conflicts from %d answers"
          % (dest, len(pinned), len(unresolved), len(singles), len(clashes), len(recs)))
    return 0

raise SystemExit(main("bots/anser"))
PY
```

2. **Read the draft, then hand it over.** Post the pinned section in the mod
   channel as a draft, not as a pinned message, with one line: which entries need
   a fresh source. A mod pins it; Anser does not.
3. **Stale sources are rewritten before they are offered.** An entry marked
   `stale source` gets a fresh citation from the corpus
   (`python bots/anser/scripts/corpus.py pack "<question>"`) or it is dropped from
   the draft. A pinned answer with a two-year-old price is worse than no FAQ.
4. **Conflicts go to a human with both sides.** Never average them, never pick
   the newer one silently — that is how a wrong number becomes canonical.
5. **Unanswered repeats become an escalation, not a guess.** "Not answerable yet"
   means the question is being asked and the corpus is silent: tell the mods, ask
   Nous, and log it. Do not draft an answer to fill the section.
6. **Only questions asked twice or more are pinned.** Singles stay in the draft
   appendix until a second ask arrives — a FAQ of one-offs is a changelog.

## Gates

- No entry reaches the mod channel without a `Source:` line carrying a date.
- `confidence: low` or `none` never drafts, however often it is asked.
- The draft is regenerated, never hand-edited: edit the underlying `answers/*.md`
  and re-run, so the next run does not resurrect a deleted claim.
- Nothing here posts to Discord, pins, or DMs. Draft file plus one message to mods.

## Failure modes

- `no answers under data/answers` — the log is empty (fresh bot, or `grounded-answer`
  stopped logging). Fix the logging first; distilling nothing is not a result.
- Everything lands in "Asked once" — the answers are being logged with a different
  question wording each time, or `data/answers` is being pruned. Check three files
  before changing a threshold.
- A cluster keeps splitting — the question wording differs on the subject itself
  (e.g. "Hermes" vs "the Hermes app"). Add a synonym to `STOP`-adjacent normalizing,
  not a lower `SAME`; loose matching merges real distinct questions.
