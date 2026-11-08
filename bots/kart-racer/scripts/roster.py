#!/usr/bin/env python3
"""Derive the playable cast from the Nous Research Cinematic Universe bible.

Source of truth: 123mikeyd/Nous_Research_Cinematic_Universe
  characters/README.md   - the alphabetical directory (slug + display name)
  characters/<slug>.md   - the profile (tags, role, build)
  images/previews/*.webp - the portrait art

The output is Assets/Roster/roster.json. Stats are derived deterministically so a
re-run never reshuffles a character; an entry marked `"locked": true` is
hand-tuned and is never overwritten.

Usage:
    python roster.py build --out roster.json [--cache-dir .cache] [--offline]
    python roster.py validate roster.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from dataclasses import dataclass, asdict, field
from datetime import date
from pathlib import Path
from typing import Any

REPO = "123mikeyd/Nous_Research_Cinematic_Universe"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
CREDIT_NOTE = "Character and art credits per NRCU CREDITS.md"

# Weight class from the profile's own words. Order matters: first hit wins, and
# the reason is recorded so a human can audit why a character is heavy.
HEAVY_HINTS = ("colossus", "colossal", "giant", "hulking", "titan", "dragon", "cthulhu",
               "ogre", "behemoth", "massive", "tank", "mech", "golem", "kaiju")
LIGHT_HINTS = ("tiny", "small", "cat", "kitten", "fairy", "sprite", "bee", "bird",
               "mouse", "kid", "child", "pixie", "imp", "sneaky", "agile")

LINK = re.compile(r"\[([^\]]+)\]\(\./([a-z0-9._-]+)\.md\)")


@dataclass
class Character:
    slug: str
    display: str
    portrait: str
    weight: str
    stats: dict[str, int]
    credit: str
    source_note: str
    locked: bool = False
    bio_hook: str = ""
    tags: list[str] = field(default_factory=list)


def cache_key(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:16] + ".txt"


def fetch(url: str, cache_dir: Path | None = None, *, offline: bool = False) -> str:
    cached = (cache_dir / cache_key(url)) if cache_dir is not None else None
    if cached is not None and cached.exists():
        return cached.read_text(encoding="utf-8")
    if offline:
        raise FileNotFoundError(f"offline and no cache for {url}")
    with urllib.request.urlopen(url, timeout=30) as response:  # noqa: S310 - fixed https host
        text = response.read().decode("utf-8", errors="replace")
    if cached is not None:
        cached.parent.mkdir(parents=True, exist_ok=True)
        cached.write_text(text, encoding="utf-8")
    return text


def parse_directory(markdown: str) -> list[tuple[str, str]]:
    """(display name, slug) pairs from the alphabetical character directory."""
    seen: dict[str, str] = {}
    for display, slug in LINK.findall(markdown):
        if slug.lower() in ("readme",):
            continue
        seen.setdefault(slug, display.strip())
    return sorted(seen.items(), key=lambda item: item[1])


def weight_class(profile: str, display: str) -> tuple[str, str]:
    text = (profile + " " + display).lower()
    for hint in HEAVY_HINTS:
        if hint in text:
            return "heavy", f"build hint '{hint}' in the profile"
    for hint in LIGHT_HINTS:
        if hint in text:
            return "light", f"build hint '{hint}' in the profile"
    return "medium", "no build hint in the profile; medium is the default"


def derive_stats(slug: str, weight: str) -> dict[str, int]:
    """Deterministic 1-10 stats, biased by weight class. Same slug, same numbers."""
    digest = hashlib.sha256(slug.encode()).digest()
    base = [3 + (byte % 6) for byte in digest[:4]]  # 3..8
    names = ("speed", "accel", "handling", "weight")
    stats: dict[str, int] = {name: int(value) for name, value in zip(names, base)}
    if weight == "heavy":
        stats["weight"] = min(10, stats["weight"] + 2)
        stats["speed"] = max(1, stats["speed"] - 1)
    elif weight == "light":
        stats["accel"] = min(10, stats["accel"] + 2)
        stats["weight"] = max(1, stats["weight"] - 2)
    return stats


def extract_tags(profile: str) -> list[str]:
    front = re.search(r"^tags:\s*\[([^\]]*)\]", profile, re.M | re.I)
    if front:
        return [t.strip().strip("'\"") for t in front.group(1).split(",") if t.strip()]
    return [m.group(1).strip().lower() for m in re.finditer(r"^-\s*\*\*Tag\*\*:\s*(.+)$", profile, re.M)][:6]


def first_line(profile: str) -> str:
    for line in profile.splitlines():
        text = line.strip().lstrip("#> ").strip()
        if len(text) > 40 and not text.startswith(("|", "-", "!", "[", "<")):
            return text[:160]
    return ""


def build(*, cache_dir: Path | None = None, offline: bool = False,
          existing: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    directory = parse_directory(fetch(f"{RAW}/characters/README.md", cache_dir, offline=offline))
    locked = {slug: entry for slug, entry in (existing or {}).items() if entry.get("locked")}
    characters: list[dict[str, Any]] = []
    missing: list[str] = []

    for slug, display in directory:
        if slug in locked:
            characters.append(locked[slug])
            continue
        try:
            profile = fetch(f"{RAW}/characters/{slug}.md", cache_dir, offline=offline)
        except Exception as exc:  # a missing profile is a finding, not a crash
            missing.append(f"{slug}: {exc}")
            profile = ""
        weight, reason = weight_class(profile, display)
        characters.append(asdict(Character(
            slug=slug,
            display=display,
            portrait=f"Roster/Portraits/{slug}.webp",
            weight=weight,
            stats=derive_stats(slug, weight),
            credit=CREDIT_NOTE,
            source_note=reason,
            bio_hook=first_line(profile),
            tags=extract_tags(profile),
        )))

    return {
        "schema": "nrcu-kart.roster/v1",
        "generated_at": date.today().isoformat(),
        "source": f"https://github.com/{REPO}",
        "credit": CREDIT_NOTE,
        "count": len(characters),
        "characters": characters,
        "unresolved": missing,
    }


def validate(roster: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    characters = roster.get("characters") or []
    if not characters:
        return ["roster is empty"]
    slugs = [c.get("slug") for c in characters]
    if len(set(slugs)) != len(slugs):
        duplicates = sorted({s for s in slugs if slugs.count(s) > 1})
        problems.append(f"duplicate slugs: {duplicates}")
    for entry in characters:
        for field_name in ("slug", "display", "portrait", "weight", "stats", "credit"):
            if not entry.get(field_name):
                problems.append(f"{entry.get('slug', '?')}: missing {field_name}")
        if entry.get("weight") not in ("light", "medium", "heavy"):
            problems.append(f"{entry.get('slug')}: bad weight class {entry.get('weight')!r}")
        stats = entry.get("stats") or {}
        if set(stats) != {"speed", "accel", "handling", "weight"}:
            problems.append(f"{entry.get('slug')}: stats must be speed/accel/handling/weight")
        if any(not isinstance(v, int) or not 1 <= v <= 10 for v in stats.values()):
            problems.append(f"{entry.get('slug')}: stats must be ints 1-10")
    sov = [c for c in characters if "sovthpaw" in str(c.get("slug", "")).lower()
           or "sovthpaw" in str(c.get("display", "")).lower()]
    if not sov:
        problems.append("no entry for Turbo Fit / Sovthpaw - the roster is incomplete")
    for entry in sov:
        if "sovthpaw" not in json.dumps(entry).lower():
            problems.append("the sovthpaw entry must credit sovthpaw by that spelling")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("build"); p.add_argument("--out", default="roster.json")
    p.add_argument("--cache-dir"); p.add_argument("--offline", action="store_true")
    p = sub.add_parser("validate"); p.add_argument("roster")

    args = parser.parse_args(argv)
    if args.command == "build":
        out = Path(args.out)
        existing = {}
        if out.exists():
            existing = {c["slug"]: c for c in json.loads(out.read_text(encoding="utf-8")).get("characters", [])}
        roster = build(cache_dir=Path(args.cache_dir) if args.cache_dir else None,
                       offline=args.offline, existing=existing)
        out.write_text(json.dumps(roster, indent=2) + "\n", encoding="utf-8")
        problems = validate(roster)
        print(f"{roster['count']} characters -> {out}")
        if roster["unresolved"]:
            print(f"unresolved profiles: {len(roster['unresolved'])}")
        for problem in problems:
            print(f"  ! {problem}")
        return 1 if problems else 0
    if args.command == "validate":
        problems = validate(json.loads(Path(args.roster).read_text(encoding="utf-8")))
        for problem in problems:
            print(f"! {problem}")
        print("ok" if not problems else f"{len(problems)} problem(s)")
        return 1 if problems else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
