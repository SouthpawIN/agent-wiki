"""Roster derivation from the NRCU bible. Offline: fixtures stand in for GitHub."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import roster as r  # noqa: E402

DIRECTORY = """
# All Nous characters

- [Cthulhu](./cthulhu.md)
- [FatCat](./fatcat.md)
- [Turbo Fit / Sovthpaw](./sovthpaw.md)
- [index](./README.md)
"""

PROFILES = {
    "cthulhu": "---\ntags: [eldritch, dragon]\n---\n\n# Cthulhu\n\nA colossal dragon priest sleeping beneath the sea, waking hungry.\n",
    "fatcat": "---\ntags: [cat, small]\n---\n\n# FatCat\n\nA tiny cat with a big opinion about every kart on the track.\n",
    "sovthpaw": "---\ntags: [turbofit, racer]\n---\n\n# Turbo Fit / Sovthpaw\n\nThe driver who tunes the engine mid-race and still wins on the last lap.\n",
}


def seed_cache(cache: Path) -> Path:
    """Populate a cache dir the way `fetch` would, so build() runs offline."""
    cache.mkdir(parents=True, exist_ok=True)
    (cache / r.cache_key(f"{r.RAW}/characters/README.md")).write_text(DIRECTORY, encoding="utf-8")
    for slug, profile in PROFILES.items():
        (cache / r.cache_key(f"{r.RAW}/characters/{slug}.md")).write_text(profile, encoding="utf-8")
    return cache


def test_parse_directory_skips_the_index() -> None:
    parsed = dict(r.parse_directory(DIRECTORY))
    assert set(parsed) == {"cthulhu", "fatcat", "sovthpaw"}
    assert parsed["sovthpaw"] == "Turbo Fit / Sovthpaw"


def test_weight_class_comes_from_the_profile_not_a_guess() -> None:
    assert r.weight_class(PROFILES["cthulhu"], "Cthulhu")[0] == "heavy"
    assert r.weight_class(PROFILES["fatcat"], "FatCat")[0] == "light"
    weight, reason = r.weight_class(PROFILES["sovthpaw"], "Turbo Fit / Sovthpaw")
    assert weight == "medium" and "no build hint" in reason


def test_stats_are_deterministic_and_bounded() -> None:
    first = r.derive_stats("cthulhu", "heavy")
    assert first == r.derive_stats("cthulhu", "heavy")
    assert set(first) == {"speed", "accel", "handling", "weight"}
    assert all(1 <= value <= 10 for value in first.values())
    assert first["weight"] >= r.derive_stats("cthulhu", "medium")["weight"]


def test_build_offline_produces_a_valid_roster(tmp_path: Path) -> None:
    seed_cache(tmp_path / "cache")
    built = r.build(cache_dir=tmp_path / "cache", offline=True)

    assert built["count"] == 3
    assert built["unresolved"] == []
    assert r.validate(built) == []

    by_slug = {c["slug"]: c for c in built["characters"]}
    assert by_slug["cthulhu"]["weight"] == "heavy"
    assert by_slug["fatcat"]["weight"] == "light"
    assert "sovthpaw" in json.dumps(by_slug["sovthpaw"]).lower()
    assert by_slug["sovthpaw"]["portrait"] == "Roster/Portraits/sovthpaw.webp"
    assert by_slug["cthulhu"]["tags"] == ["eldritch", "dragon"]
    assert by_slug["fatcat"]["bio_hook"].startswith("A tiny cat")


def test_locked_entries_are_never_overwritten(tmp_path: Path) -> None:
    seed_cache(tmp_path / "cache")
    existing = {"cthulhu": {"slug": "cthulhu", "display": "Cthulhu (hand-tuned)",
                            "portrait": "Roster/Portraits/cthulhu.webp", "weight": "heavy",
                            "stats": {"speed": 2, "accel": 2, "handling": 2, "weight": 10},
                            "credit": r.CREDIT_NOTE, "source_note": "tuned by hand",
                            "locked": True}}
    built = r.build(cache_dir=tmp_path / "cache", offline=True, existing=existing)
    tuned = next(c for c in built["characters"] if c["slug"] == "cthulhu")
    assert tuned["display"] == "Cthulhu (hand-tuned)"
    assert tuned["stats"]["weight"] == 10


def test_a_missing_profile_is_a_finding_not_a_crash(tmp_path: Path) -> None:
    cache = seed_cache(tmp_path / "cache")
    (cache / r.cache_key(f"{r.RAW}/characters/fatcat.md")).unlink()
    built = r.build(cache_dir=cache, offline=True)
    assert built["count"] == 3, "the character still ships, flagged"
    assert any("fatcat" in item for item in built["unresolved"])


def test_validate_catches_the_ways_a_roster_go_wrong() -> None:
    good = {"characters": [{"slug": "sovthpaw", "display": "Turbo Fit / Sovthpaw",
                            "portrait": "p.webp", "weight": "medium",
                            "stats": {"speed": 5, "accel": 5, "handling": 5, "weight": 5},
                            "credit": r.CREDIT_NOTE}]}
    assert r.validate(good) == []

    assert r.validate({"characters": []}) == ["roster is empty"]

    no_credit = json.loads(json.dumps(good))
    no_credit["characters"][0]["credit"] = ""
    assert any("missing credit" in p for p in r.validate(no_credit))

    dupes = {"characters": good["characters"] + good["characters"]}
    assert any("duplicate slugs" in p for p in r.validate(dupes))

    no_southpaw = {"characters": [{**good["characters"][0], "slug": "cthulhu",
                                   "display": "Cthulhu"}]}
    assert any("Turbo Fit / Sovthpaw" in p for p in r.validate(no_southpaw))

    bad_stats = json.loads(json.dumps(good))
    bad_stats["characters"][0]["stats"]["speed"] = 42
    assert any("stats must be ints" in p for p in r.validate(bad_stats))


def test_cli_build_then_validate(tmp_path: Path, capsys) -> None:
    seed_cache(tmp_path / "cache")
    out = tmp_path / "roster.json"
    assert r.main(["build", "--out", str(out), "--cache-dir", str(tmp_path / "cache"), "--offline"]) == 0
    assert "3 characters" in capsys.readouterr().out
    assert r.main(["validate", str(out)]) == 0
    assert "ok" in capsys.readouterr().out
