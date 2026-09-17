#!/usr/bin/env python3
"""hatch-pet.py — Senter Wiki pet pipeline (uses Hermes' built-in /hatch engine).

Generates a new petdex-style animated pet in the SAME style as the fleet's
existing pets (s0uthpaw / teknium / 123mikeyd are passed as style references),
installs it into ~/.hermes/pets/<slug>/, and cuts a 256px avatar PNG into the
vault (assets/avatars/<bot>.png) for the feed / stream / BOTS tab.

    python3 assets/hatch-pet.py --bot senter --slug senter-owl \
        "a wise three-eyed owl, dark feathers, small gold monocle"

    python3 assets/hatch-pet.py --bot anser --slug anser-goose "a skeptical grey goose auditor with a clipboard"

Options:
  --bot      fleet profile the pet belongs to (drives avatar filename)
  --slug     petdex slug to install under (default: slugified bot)
  --drafts   how many base looks to draft before picking (default 1 = take first)
  --pick     index of the draft to hatch (default 0)
  --no-avatar  skip cutting the vault avatar
Takes ~1–3 min of image-model calls. Requires a reference-capable image provider
(hermes tools → image generation). Style refs: existing fleet pets' idle frames.
"""
import argparse, json, os, sys, shutil
from pathlib import Path

HERMES_REPO = Path.home() / ".hermes/hermes-agent"
HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PETS = Path.home() / ".hermes/pets"                    # shared pet store (all profiles)
VAULT = Path.home() / "Documents/Projects/Projects"
AVATARS = VAULT / "assets/avatars"
STYLE_REFS = ["s0uthpaw", "teknium", "123mikeyd"]      # the fleet's existing look

sys.path.insert(0, str(HERMES_REPO))


def idle_frame_png(slug: str, out: Path, size=256):
    from PIL import Image
    im = Image.open(PETS / slug / "spritesheet.webp").convert("RGBA")
    fr = im.crop((0, 0, 192, 208))
    bb = fr.getbbox()
    if bb:
        fr = fr.crop(bb)
    s = max(fr.size)
    sq = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    sq.paste(fr, ((s - fr.size[0]) // 2, (s - fr.size[1]) // 2))
    sq.resize((size, size), Image.LANCZOS).save(out)
    return out


def ref_images() -> list[Path]:
    """Idle frames of existing fleet pets, written to /tmp as style references."""
    refs = []
    for slug in STYLE_REFS:
        if (PETS / slug / "spritesheet.webp").exists():
            refs.append(idle_frame_png(slug, Path(f"/tmp/petref-{slug}.png"), 192))
    return refs[:3]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("concept")
    ap.add_argument("--bot", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--drafts", type=int, default=1)
    ap.add_argument("--pick", type=int, default=0)
    ap.add_argument("--no-avatar", action="store_true")
    ap.add_argument("--base", help="reuse an approved base image; skips drafting (retry row pass)")
    ap.add_argument("--tries", type=int, default=3, help="row-pass attempts before giving up")
    a = ap.parse_args()

    from agent.pet import store
    from agent.pet.generate import orchestrate
    from agent.pet.generate.imagegen import GenerationError

    slug = store.slugify(a.slug or a.bot)
    display = a.bot.capitalize()
    concept = (a.concept + " — chibi pixel-art pet, same style as the reference sprites: "
               "big head, small body, clean outline, transparent background, "
               "compact upright silhouette with arms kept in and nothing held out wide (the row-slicer needs a narrow shape)")
    refs = ref_images()
    print(f"[hatch] {a.bot} ← '{a.concept}' as slug {slug!r}; {len(refs)} style refs")

    if a.base:
        base = Path(a.base)
    else:
        try:
            drafts = orchestrate.generate_base_drafts(concept, n=a.drafts, reference_images=refs or None,
                                                      on_draft=lambda i, p: print(f"  draft {i}: {p}"))
        except GenerationError as e:
            sys.exit(f"[hatch] base draft failed: {e}")
        if not drafts:
            sys.exit("[hatch] no drafts returned")
        base = drafts[min(a.pick, len(drafts) - 1)]
    print(f"[hatch] using base {base}")

    def prog(ev, detail):
        if ev == "row":
            print(f"  ┊ drawing {detail.split(':', 1)[0]}…")
        elif ev in ("compose", "save"):
            print(f"  ┊ {ev}…")

    res = None
    for attempt in range(1, a.tries + 1):
        try:
            res = orchestrate.hatch_pet(base_image=base, slug=slug, display_name=display,
                                        concept=a.concept, description=a.concept, on_progress=prog)
            break
        except GenerationError as e:
            print(f"[hatch] row pass {attempt}/{a.tries} failed: {e}")
    if res is None:
        sys.exit(f"[hatch] gave up after {a.tries} row passes (base kept: {base})")

    prof_dir = HERMES_HOME / "pets" / slug
    pet_dir = PETS / slug
    if prof_dir.exists() and prof_dir != pet_dir:
        shutil.copytree(prof_dir, pet_dir, dirs_exist_ok=True)
    print(f"[hatch] installed → {pet_dir}")

    if not a.no_avatar:
        AVATARS.mkdir(parents=True, exist_ok=True)
        out = idle_frame_png(slug, AVATARS / f"{a.bot}.png")
        print(f"[hatch] avatar → {out}")

    # vault record
    log = VAULT / "log.md"
    with log.open("a") as f:
        f.write(f"\n- pet hatched: **{a.bot}** ← `{slug}` — \"{a.concept}\" (style refs: {', '.join(STYLE_REFS)}); avatar assets/avatars/{a.bot}.png\n")
    print("[hatch] logged to log.md")


if __name__ == "__main__":
    main()
