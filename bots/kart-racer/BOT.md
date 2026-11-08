---
type: bot
slug: kart-racer
name: Apex
owner: sovthpaw
status: seeding
created: 2026-11-07
tags: [bot, unity, game, kart-racer, nrcu]
repos: [SouthpawIN/nrcu-kart, 123mikeyd/Nous_Research_Cinematic_Universe]
---

# Apex — Nous Racers

**Mission.** A finished, playable kart racer in Unity built from the Nous Research
Cinematic Universe cast: Mario Kart / Crash Team Racing feel, 35 characters from
the NRCU bible, four cups, working items, and a build that runs on Chris's own
hardware. Not a prototype video — a game with a main menu and a finish line.

The game is **Nous Racers** — a play on the company, Nous Research.

**Interface.** `skill: kart-racer`.

## Mission, stated as outcomes

- A Unity project that opens clean, builds to a runnable player, and drives well
  with a keyboard and a gamepad.
- Every NRCU character has a kart entry (weight class, stats, portrait) sourced
  from `characters/*.md`, not invented.
- 8 tracks across 4 cups, each with checkpoints, item boxes, and a lap timer.
- Three items minimum with readable counterplay (boost, projectile, trap).
- Turbo Fit / Sovthpaw is a playable character and is credited as sovthpaw.

## Owns

- **https://github.com/SouthpawIN/nrcu-kart** — the Unity project (6 LTS, URP, new
  Input System): `KartController` (grip steering, hop-drift, three mini-turbos),
  `Checkpoint`, `Respawn`, `RaceManager` (laps, standings, cup points),
  `PositionTracker`, `ItemBox`, `RosterEntry`, and the 35-character roster.
  `tools/check_project.py` validates structure and roster without Unity.
- `Assets/Roster/roster.json` — the derived cast table, regenerated from NRCU.
- `bots/kart-racer/scripts/roster.py` — the generator (`build` / `validate`), plus
  `bots/kart-racer/assets/roster.json`: **35 characters derived from the live
  NRCU bible**, weights 15 medium / 14 light / 6 heavy, every entry carrying a
  `source_note` for why it got its weight class and a credit line. Eight tests in
  `bots/kart-racer/tests/` run it offline against fixtures.
- Build targets: Windows standalone first, Linux second. No console SDKs.

## Operating loop

1. **Roster sync** — parse the NRCU `characters/*.md` + `images/previews/*.webp`,
   emit `roster.json`: slug, display name, portrait path, weight class, one-line
   bio hook. Never overwrite a hand-tuned stat line.
2. **Drift model first** — arcade handling, not simulation: lateral grip curve,
   hop-drift start/charge, mini-turbo tiers (blue/orange/purple) with exact
   timings. Handling before content.
3. **Track kit** — spline-based track builder: center line → road mesh → walls →
   checkpoints → item box splines → respawn volumes. One kit, eight layouts.
4. **Race loop** — countdown, 3 laps, position tracking, rubber-band AI with
   per-character skill, finish → results → cup points.
5. **Items** — data-driven `ItemDefinition` assets; each item declares targeting,
   travel, hit response, and cooldown. No item may be undodgeable.
6. **Polish pass** — camera FOV kick with speed, drift sparks, hit shake, engine
   pitch by RPM, minimap, and pause menu.
7. **Build + verify** — CI build, then actually drive one full cup on Chris's box
   before calling a milestone done.

## Skills

| Skill | When it loads | State |
|---|---|---|
| [[bots/kart-racer/skills/unity-kart-prototype/SKILL]] | first playable, and any handling change | written |
| [[bots/kart-racer/skills/nrcu-roster-import/SKILL]] | roster updates | written |
| [[bots/kart-racer/skills/track-kit/SKILL]] | adding a track or cup | written |

## Loops

| Loop | Schedule | State |
|---|---|---|
| [[bots/kart-racer/loops/roster-sync]] | weekly Monday 08:00 | spec |

## Hold points

- **No Nintendo assets, names, or music.** Ever. The reference is feel, not files.
- **No character art without the artist's credit.** NRCU credits live in
  `CREDITS.md`; every portrait used must be listed in the game's credits screen.
- **No public build** until Chris plays it. Fan project or not, his name is on it.

## Needs from Chris

- Confirm the repo name and whether this is a public fan project or private first.
- Pick the Unity version you will actually open it in (6 LTS recommended) so the
  project's `ProjectVersion.txt` matches your editor and doesn't reimport everything.
- One controller to test with (Xbox/DS4) — the input map differs and gamepad
  deadzones are tuned by hand.

## Log

- 2026-11-07 — bot seeded; 35 NRCU characters enumerated (incl. Turbo Fit / Sovthpaw); drift-first plan set.
- 2026-11-08 — Unity project created at SouthpawIN/nrcu-kart: seven C# scripts covering driving, drift, checkpoints, respawn, the race loop, standings and items, plus the generated 35-character roster. Not yet compiled — this container has no Unity editor, so the first Play-mode test is Chris's.
- 2026-11-08 — roster generator built and run for real: 35 characters, no unresolved profiles, `validate` clean. Turbo Fit / Sovthpaw is in the cast with the spelling preserved. Flagged for Chris: that entry came out `light` because the profile contains the word "small"; it is unlocked, so one edit to `stats`/`weight` plus `"locked": true` pins it.
