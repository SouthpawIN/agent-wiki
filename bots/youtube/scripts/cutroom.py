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
        if args.command == "verify":
            result = verify(args.render, _load(args.edl))
            print(json.dumps(result, indent=2)); return 0 if result["ok"] else 1
    except RuntimeError as exc:
        print(f"cutroom: {exc}", file=sys.stderr); return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
