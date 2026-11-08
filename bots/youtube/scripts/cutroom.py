#!/usr/bin/env python3
"""Cutroom — the deterministic half of the YouTube pipeline.

Everything here is ffmpeg + stdlib. No model weights, no API keys, so it can be
tested with synthetic media and still be the real renderer.

Subcommands:
    probe   <file>                          streams, duration, fps, CFR/VFR
    silences <file>                          pause gaps via ffmpeg silencedetect
    segments <file> [--transcript t.json]    build segments.json (fallback: silences)
    edl     <file> <segments.json>           build edl.json with lead-in / tail
    render  <edl.json> <out.mp4>             cut, concat, single loudnorm pass
    verify  <out.mp4> <edl.json>             duration / streams / peak checks
"""
from __future__ import annotations

import argparse
import json
import shutil
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

TARGET_LUFS = -14.0
TRUE_PEAK = -1.5
LEAD_IN = 0.6
TAIL = 0.8


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def require_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        raise RuntimeError("ffmpeg/ffprobe not found on PATH")


def probe(path: str | Path) -> dict:
    out = run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip() or f"ffprobe failed on {path}")
    data = json.loads(out.stdout)
    video = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in data["streams"] if s["codec_type"] == "audio"), None)
    fps = None
    if video and video.get("avg_frame_rate"):
        num, _, den = video["avg_frame_rate"].partition("/")
        if float(den or 1):
            fps = round(float(num) / float(den or 1), 3)
    return {
        "path": str(path),
        "duration": float(data["format"]["duration"]),
        "video": None if video is None else {
            "codec": video.get("codec_name"),
            "width": video.get("width"),
            "height": video.get("height"),
            "fps": fps,
            "pix_fmt": video.get("pix_fmt"),
        },
        "audio": None if audio is None else {
            "codec": audio.get("codec_name"),
            "sample_rate": audio.get("sample_rate"),
            "channels": audio.get("channels"),
        },
    }


def silences(path: str | Path, noise_db: float = -35.0, min_dur: float = 2.5) -> list[dict]:
    """Return pause gaps. A gap is a boundary candidate, not a cut."""
    out = run([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
        "-af", f"silencedetect=noise={noise_db}dB:d={min_dur}", "-f", "null", "-",
    ])
    text = out.stderr
    starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", text)]
    ends = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", text)]
    gaps = []
    for index, start in enumerate(starts):
        end = ends[index] if index < len(ends) else None
        gaps.append({"start": start, "end": end, "kind": "silence"})
    return gaps


def build_segments(
    media: str | Path,
    *,
    transcript: dict | None = None,
    min_seconds: float = 45.0,
    max_minutes: float = 25.0,
    drop_pauses: bool = True,
) -> list[dict]:
    """Segment a session into topic chunks.

    Dead air is dropped, not carried: a pause becomes a boundary pair
    (content ends at the pause, resumes when the pause ends). With a transcript,
    topic shifts add boundaries too; without one, pauses alone drive the split so
    the renderer can still be exercised end to end.
    """
    info = probe(media)
    duration = info["duration"]
    gaps = silences(media) if drop_pauses else []

    intervals: list[list[float]] = []
    cursor = 0.0
    for gap in gaps:
        end = gap.get("end")
        if end is None:
            break
        if gap["start"] - cursor >= 1.0:
            intervals.append([cursor, float(gap["start"])])
        cursor = max(cursor, float(end))
    if duration - cursor >= 1.0:
        intervals.append([cursor, duration])
    if not intervals:
        intervals = [[0.0, duration]]

    if transcript is not None:
        for boundary in _topic_boundaries(transcript, duration):
            intervals = _split_interval(intervals, boundary)

    merged: list[list[float]] = []
    for start, end in intervals:
        if merged and end - merged[-1][0] < min_seconds:
            merged[-1][1] = end
            continue
        merged.append([start, end])
    if len(merged) > 1 and merged[-1][1] - merged[-1][0] < min_seconds:
        merged[-2][1] = merged[-1][1]
        merged.pop()

    cap = max_minutes * 60.0
    final: list[list[float]] = []
    for start, end in merged:
        while end - start > cap:
            final.append([start, start + cap])
            start += cap
        final.append([start, end])

    return [
        {
            "id": f"seg-{index + 1:02d}",
            "start": round(start, 3),
            "end": round(end, 3),
            "duration": round(end - start, 3),
            "title": f"Segment {index + 1}",
            "hook_line": "",
            "rank": None,
            "source": str(media),
        }
        for index, (start, end) in enumerate(final)
    ]


def _split_interval(intervals: list[list[float]], boundary: float) -> list[list[float]]:
    out: list[list[float]] = []
    for start, end in intervals:
        if start < boundary < end:
            out.extend([[start, boundary], [boundary, end]])
        else:
            out.append([start, end])
    return out


def _topic_boundaries(transcript: dict, duration: float) -> list[float]:
    """Boundaries from word timestamps: prefer long pauses between topic shifts."""
    words = transcript.get("words") or []
    if not words:
        return []
    boundaries = []
    for previous, current in zip(words, words[1:]):
        gap = float(current.get("start", 0)) - float(previous.get("end", 0))
        if gap >= 2.5:
            boundaries.append(float(current.get("start", 0)))
    return [b for b in boundaries if 0 < b < duration]


def build_edl(segments: list[dict], *, total_duration: float | None = None) -> dict:
    parts = []
    for segment in sorted(segments, key=lambda item: item["start"]):
        start = max(0.0, float(segment["start"]) - LEAD_IN)
        end = float(segment["end"]) + TAIL
        if total_duration is not None:
            end = min(end, total_duration)
        parts.append({
            "src": segment.get("source", ""),
            "in": round(start, 3),
            "out": round(end, 3),
            "transition_in": "cut",
            "lower_third": None,
        })
    return {
        "segments": parts,
        "audio": {"target_lufs": TARGET_LUFS, "true_peak": TRUE_PEAK, "lra": 11},
        "expected_duration": round(sum(p["out"] - p["in"] for p in parts), 3),
    }


def render(edl: dict, out_path: str | Path, *, preset: str = "slow", crf: int = 18, fps: int = 60) -> dict:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    work = out_path.parent / (out_path.stem + ".parts")
    work.mkdir(parents=True, exist_ok=True)

    part_files = []
    for index, part in enumerate(edl["segments"]):
        part_file = work / f"part-{index:03d}.mp4"
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", f"{part['in']:.3f}", "-to", f"{part['out']:.3f}", "-i", part["src"],
            "-c:v", "libx264", "-preset", preset, "-crf", str(crf), "-r", str(fps),
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            str(part_file),
        ]
        result = run(cmd)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or f"cut failed for part {index}")
        part_files.append(part_file)

    concat_list = work / "concat.txt"
    concat_list.write_text("".join(f"file '{p.resolve()}'\n" for p in part_files), encoding="utf-8")
    joined = work / "joined.mp4"
    result = run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(joined),
    ])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "concat failed")

    loudness = edl.get("audio", {})
    result = run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(joined),
        "-af", f"loudnorm=I={loudness.get('target_lufs', TARGET_LUFS)}"
               f":TP={loudness.get('true_peak', TRUE_PEAK)}"
               f":LRA={loudness.get('lra', 11)}",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        str(out_path),
    ])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "loudnorm pass failed")

    return {
        "output": str(out_path),
        "parts": len(part_files),
        "expected_duration": edl.get("expected_duration"),
        "probe": probe(out_path),
    }


def verify(render_path: str | Path, edl: dict, *, tolerance: float = 1.0) -> dict:
    info = probe(render_path)
    expected = float(edl.get("expected_duration") or 0)
    problems = []
    if expected and abs(info["duration"] - expected) > tolerance:
        problems.append(f"duration {info['duration']:.2f}s != edl {expected:.2f}s")
    if info["video"] is None:
        problems.append("no video stream")
    if info["audio"] is None:
        problems.append("no audio stream")
    peak = run([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(render_path),
        "-af", "ebur128=peak=true", "-f", "null", "-",
    ]).stderr
    match = re.search(r"Peak:\s*(-?[\d.]+) dBFS", peak)
    peak_db = float(match.group(1)) if match else None
    if peak_db is not None and peak_db > -1.0:
        problems.append(f"true peak {peak_db} dBTP above -1.0")
    return {"ok": not problems, "problems": problems, "peak_dbfs": peak_db, "probe": info}


# ---------------------------------------------------------------- packaging

# Anything that must never appear in public metadata. Public name is sovthpaw.
FORBIDDEN_PUBLIC_NAMES = ("Chris", "Christopher")
PUBLIC_NAME = "sovthpaw"


def timestamp(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


def assert_public_names(text: str) -> None:
    """Fail the package rather than publish a private name."""
    for name in FORBIDDEN_PUBLIC_NAMES:
        if name.lower() in text.lower():
            raise ValueError(f"public metadata must not contain '{name}'; use '{PUBLIC_NAME}'")


def make_title(segments: list[dict], *, fallback: str = "Voice chat rant") -> str:
    """Front-load the claim, cap at 60 characters."""
    ranked = [s for s in segments if s.get("rank") is not None]
    pick = max(ranked, key=lambda s: s["rank"]) if ranked else (segments[0] if segments else {})
    base = (pick.get("hook_line") or pick.get("title") or fallback).strip()
    base = " ".join(base.split())
    if len(base) <= 60:
        return base
    cut = base[:59]
    return cut[: cut.rfind(" ")].rstrip(",;:") + "…"


def make_chapters(segments: list[dict], *, min_seconds: float = 10.0) -> list[tuple[float, str]]:
    """Chapters from segment starts. First is always 0:00; short ones are merged."""
    ordered = sorted(segments, key=lambda s: s["start"])
    chapters: list[tuple[float, str]] = []
    for segment in ordered:
        start = 0.0 if not chapters else float(segment["start"])
        title = (segment.get("title") or f"Part {len(chapters) + 1}").strip()
        if chapters and start - chapters[-1][0] < min_seconds:
            continue
        chapters.append((start, title))
    if not chapters:
        chapters = [(0.0, ordered[0].get("title", "Part 1") if ordered else "Part 1")]
    if chapters[0][0] != 0.0:
        chapters[0] = (0.0, chapters[0][1])
    return chapters


def make_tags(segments: list[dict], *, channel_defaults: tuple[str, ...] = (), limit: int = 12) -> list[str]:
    terms: list[str] = []
    for segment in segments:
        for term in segment.get("terms") or []:
            if term.lower() not in [t.lower() for t in terms]:
                terms.append(term)
    for term in channel_defaults:
        if term.lower() not in [t.lower() for t in terms]:
            terms.append(term)
    return terms[:limit]


def package(
    segments: list[dict],
    out_dir: str | Path,
    *,
    title: str | None = None,
    premise: str = "",
    channel_defaults: tuple[str, ...] = (),
    visibility: str = "unlisted",
    thumbnail_subject: str = "",
) -> dict:
    """Write upload.md. Never uploads, never schedules."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    resolved_title = title or make_title(segments)
    assert_public_names(resolved_title)
    assert_public_names(premise)

    chapters = make_chapters(segments)
    tags = make_tags(segments, channel_defaults=channel_defaults)
    chapter_lines = "\n".join(f"{timestamp(start)} {name}" for start, name in chapters)
    total = max((float(s["end"]) for s in segments), default=0.0)

    text = f"""# Upload sheet

**Title.** {resolved_title}

**Visibility.** {visibility} (Chris publishes; Cutroom never does)

## Description

{premise or '[[premise: one sentence on what this is about]]'}

Recorded live in voice chat. Chapters below.

## Chapters

{chapter_lines}

_Total runtime {timestamp(total)}._

## Tags

{', '.join(tags) if tags else '[[tags: none derived - add by hand]]'}

## Thumbnail

Prompt: a single dominant subject, {thumbnail_subject or '[[subject]]'}, high contrast,
at most four words of text, legible at 320x180. Generate with image_generate, then
check the downscaled version before shipping.

## Needs Chris

- Read the title and the first chapter: if the hook is not in the first 8 seconds
  of the cut, the title is a promise the video does not keep.
- Approve, then publish under **{PUBLIC_NAME}**.
"""
    path = out_dir / "upload.md"
    path.write_text(text, encoding="utf-8")
    return {
        "upload_md": str(path),
        "title": resolved_title,
        "title_length": len(resolved_title),
        "chapters": [{"time": timestamp(start), "title": name} for start, name in chapters],
        "tags": tags,
        "visibility": visibility,
        "runtime": timestamp(total),
    }


# ------------------------------------------------------- graphics + assembly

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CARD_SIZE = "1920x1080"


def _esc(text: str) -> str:
    """Escape a string for ffmpeg drawtext."""
    out = str(text).replace("\\", "").replace(":", "\\:").replace("'", "’")
    return out.replace("%", "\\%").replace(",", "\\,")


def make_card(text: str, out: str | Path, *, subtitle: str = "", duration: float = 3.0,
              size: str = CARD_SIZE, kind: str = "title", fps: int = 60) -> Path:
    """A title, chapter, or lower-third card. Generated, never hand-placed."""
    require_ffmpeg()
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    width, height = (int(v) for v in size.split("x"))
    if kind == "lower-third":
        box = (
            f"drawbox=x=0:y=h-160:w={int(width * 0.5)}:h=160:color=black@0.65:t=fill,"
            f"drawtext=fontfile={FONT}:text='{_esc(text)}':fontcolor=white:fontsize=52:"
            f"x=60:y=h-120"
        )
        base = f"color=c=black:s={size}:r={fps}:d={duration}:color=black@0.0,format=yuva420p"
    else:
        font = 96 if kind == "title" else 72
        y = "(h-th)/2" if not subtitle else "(h-th)/2-40"
        box = (
            f"drawtext=fontfile={FONT}:text='{_esc(text)}':fontcolor=white:fontsize={font}:"
            f"x=(w-tw)/2:y={y}"
        )
        if subtitle:
            box += (
                f",drawtext=fontfile={FONT}:text='{_esc(subtitle)}':fontcolor=white@0.8:"
                f"fontsize={font // 2}:x=(w-tw)/2:y=(h-th)/2+60"
            )
        base = f"color=c=#101014:s={size}:r={fps}:d={duration}"
    result = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi",
                  "-i", f"anullsrc=r=48000:cl=stereo", "-f", "lavfi", "-i", base,
                  "-shortest", "-vf", box, "-c:v", "libx264", "-pix_fmt", "yuv420p",
                  "-c:a", "aac", str(out)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:300] or f"card render failed: {out}")
    return out


def _geometry(path: str | Path) -> tuple[int, int]:
    info = probe(path)
    video = info.get("video") or {}
    return int(video.get("width") or 1920), int(video.get("height") or 1080)


def _normalize(path: str | Path, target: tuple[int, int], work: Path, *, fps: int = 60) -> Path:
    """Scale/pad a clip to the target geometry so xfade can join it."""
    width, height = target
    dest = work / f"_norm-{Path(path).stem}.mp4"
    result = run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(path),
        "-vf", (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
                f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps}"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "48000", str(dest),
    ])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:300] or f"normalize failed: {path}")
    return dest


def xfade_chain(parts: list[str | Path], out: str | Path, *,
                transition: str = "fade", duration: float = 0.5) -> Path:
    """Crossfade a list of clips into one. Overlaps are subtracted from the total.

    Every part is normalised to the first part's geometry first: xfade refuses
    mismatched sizes, and a 320x180 source has to join a 1920x1080 title card.
    """
    require_ffmpeg()
    if len(parts) < 2:
        shutil.copy2(str(parts[0]), str(out))
        return Path(out)
    work = Path(out).parent
    geometry = _geometry(parts[0])
    normalised = [_normalize(parts[0], geometry, work)]
    normalised += [_normalize(part, geometry, work) for part in parts[1:]]
    parts = normalised
    import subprocess as _sp
    current = Path(parts[0])
    for index, nxt in enumerate(parts[1:], start=1):
        target = Path(out).parent / f"_xfade-{index}.mp4"
        target.parent.mkdir(parents=True, exist_ok=True)
        # offset = length of the accumulated clip minus the overlap
        probe = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "csv=p=0", str(current)])
        offset = max(0.0, float(probe.stdout.strip()) - duration)
        result = _sp.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(current), "-i", str(nxt),
            "-filter_complex",
            f"[0:v][1:v]xfade=transition={transition}:duration={duration}:offset={offset:.3f}[v];"
            f"[0:a][1:a]acrossfade=d={duration}[a]",
            "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", str(target)], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip()[:300] or "xfade failed")
        if current != Path(parts[0]):
            current.unlink(missing_ok=True)
        current = target
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    current.replace(Path(out))
    return Path(out)


def group_by_topic(segments: list[dict]) -> list[tuple[str, list[dict]]]:
    """Group segments across sessions by topic, best topic first."""
    buckets: dict[str, list[dict]] = {}
    for segment in segments:
        topic = str(segment.get("topic") or segment.get("title") or "misc")
        buckets.setdefault(topic, []).append(segment)
    def best(items: list[dict]) -> float:
        ranks = [float(s.get("rank") or 0.0) for s in items]
        return max(ranks) if ranks else 0.0
    ordered = sorted(buckets.items(), key=lambda kv: (-best(kv[1]), kv[0]))
    return [(topic, sorted(items, key=lambda s: float(s.get("rank") or 0.0), reverse=True))
            for topic, items in ordered]


def assemble(sessions: list[dict], out_dir: str | Path, *, transition: str = "fade",
             transition_duration: float = 0.5, title: str | None = None,
             channel: str = "sovthpaw", max_minutes: float = 25.0) -> dict:
    """Raw sessions in, one organised video out.

    sessions: [{"source": path, "segments": [...]}, ...]
    Segments are grouped by topic across every session (so a rant that resumed
    after lunch lands with the rant it belongs to), ordered best-topic-first, and
    rendered as: title card -> chapter card -> cut -> cut -> ... with crossfades.
    """
    require_ffmpeg()
    out_dir = Path(out_dir)
    work = out_dir / "work"
    work.mkdir(parents=True, exist_ok=True)

    flat: list[dict] = []
    for session in sessions:
        for segment in session.get("segments", []):
            flat.append({**segment, "source": segment.get("source") or session.get("source", "")})

    grouped = group_by_topic(flat)
    cap = max_minutes * 60.0
    chosen: list[dict] = []
    total = 0.0
    for _, items in grouped:
        for segment in items:
            length = float(segment["end"]) - float(segment["start"])
            if total + length > cap:
                continue
            chosen.append(segment)
            total += length

    resolved_title = title or make_title(chosen)
    assert_public_names(resolved_title)

    parts: list[Path] = []
    parts.append(make_card(resolved_title, work / "card-title.mp4",
                           subtitle=channel, duration=3.0, kind="title"))
    ordered_topics: list[tuple[str, list[dict]]] = []
    for segment in chosen:
        topic = str(segment.get("topic") or segment.get("title") or "misc")
        if ordered_topics and ordered_topics[-1][0] == topic:
            ordered_topics[-1][1].append(segment)
        else:
            ordered_topics.append((topic, [segment]))

    lower_third_done = False
    for topic, items in ordered_topics:
        if not lower_third_done:
            parts.append(make_card(channel, work / f"card-lt-{len(parts)}.mp4",
                                   duration=2.0, kind="lower-third"))
            lower_third_done = True
        parts.append(make_card(topic, work / f"card-chapter-{len(parts)}.mp4",
                               duration=1.5, kind="chapter"))
        for segment in items:
            edl = build_edl([segment])
            part = work / f"cut-{len(parts):03d}.mp4"
            render(edl, part, preset="veryfast", crf=20, fps=60)
            parts.append(part)

    joined = work / "joined.mp4"
    xfade_chain(parts, joined, transition=transition, duration=transition_duration)
    final = out_dir / "render.mp4"
    result = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(joined),
                  "-af", f"loudnorm=I={TARGET_LUFS}:TP={TRUE_PEAK}:LRA=11",
                  "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                  "-movflags", "+faststart", str(final)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:300] or "final pass failed")

    packaged = package(chosen, out_dir, title=resolved_title,
                       premise=f"{len(ordered_topics)} topics from {len(sessions)} session(s).")
    return {"ok": True, "render": str(final), "title": resolved_title,
            "topics": [topic for topic, _ in ordered_topics], "segments": len(chosen),
            "runtime_s": round(probe(final)["duration"], 2), "upload_md": packaged["upload_md"]}


def _load(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cutroom", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("probe"); p.add_argument("file")
    p = sub.add_parser("silences"); p.add_argument("file")
    p.add_argument("--noise-db", type=float, default=-35.0)
    p.add_argument("--min-dur", type=float, default=2.5)
    p = sub.add_parser("segments"); p.add_argument("file")
    p.add_argument("--transcript"); p.add_argument("--out", default="segments.json")
    p = sub.add_parser("edl"); p.add_argument("file"); p.add_argument("segments")
    p.add_argument("--out", default="edl.json")
    p = sub.add_parser("render"); p.add_argument("edl"); p.add_argument("out")
    p.add_argument("--preset", default="slow"); p.add_argument("--crf", type=int, default=18)
    p = sub.add_parser("verify"); p.add_argument("render"); p.add_argument("edl")
    p = sub.add_parser("assemble"); p.add_argument("sessions")
    p.add_argument("--out", default="out"); p.add_argument("--title")
    p.add_argument("--transition", default="fade"); p.add_argument("--xfade", type=float, default=0.5)
    p = sub.add_parser("package"); p.add_argument("segments")
    p.add_argument("--out", default="out"); p.add_argument("--title")
    p.add_argument("--premise", default=""); p.add_argument("--visibility", default="unlisted")
    p.add_argument("--subject", default="")

    args = parser.parse_args(argv)
    try:
        if args.command == "probe":
            print(json.dumps(probe(args.file), indent=2)); return 0
        if args.command == "silences":
            print(json.dumps(silences(args.file, args.noise_db, args.min_dur), indent=2)); return 0
        if args.command == "segments":
            transcript = _load(args.transcript) if args.transcript else None
            segments = build_segments(args.file, transcript=transcript)
            Path(args.out).write_text(json.dumps(segments, indent=2) + "\n", encoding="utf-8")
            print(f"{len(segments)} segments -> {args.out}"); return 0
        if args.command == "edl":
            info = probe(args.file)
            edl = build_edl(_load(args.segments), total_duration=info["duration"])
            Path(args.out).write_text(json.dumps(edl, indent=2) + "\n", encoding="utf-8")
            print(f"{len(edl['segments'])} cuts, {edl['expected_duration']:.2f}s -> {args.out}"); return 0
        if args.command == "render":
            result = render(_load(args.edl), args.out, preset=args.preset, crf=args.crf)
            print(json.dumps(result, indent=2)); return 0
        if args.command == "assemble":
            data = _load(args.sessions)
            sessions = data.get("sessions", data) if isinstance(data, dict) else data
            result = assemble(sessions, args.out, title=args.title,
                              transition=args.transition, transition_duration=args.xfade)
            print(json.dumps(result, indent=2)); return 0
        if args.command == "package":
            data = _load(args.segments)
            segments = data.get("segments", data) if isinstance(data, dict) else data
            result = package(segments, args.out, title=args.title, premise=args.premise,
                             visibility=args.visibility, thumbnail_subject=args.subject)
            print(json.dumps(result, indent=2)); return 0
        if args.command == "verify":
            result = verify(args.render, _load(args.edl))
            print(json.dumps(result, indent=2)); return 0 if result["ok"] else 1
    except RuntimeError as exc:
        print(f"cutroom: {exc}", file=sys.stderr); return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
