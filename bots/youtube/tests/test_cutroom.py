"""Exercises the Cutroom renderer on synthetic media — no recordings, no models."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

import cutroom  # noqa: E402


def synth(path: Path, *, seconds: float, tone: int, colour: str, silent_tail: float = 0.0) -> Path:
    """A tiny A/V clip: colour bars + a sine tone, optional trailing silence."""
    audio = f"sine=frequency={tone}:duration={seconds - silent_tail}"
    if silent_tail:
        audio = (
            f"sine=frequency={tone}:duration={seconds - silent_tail},"
            f"apad=pad_dur={silent_tail}"
        )
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "lavfi", "-i", f"color=c={colour}:s=320x180:r=30:d={seconds}",
            "-f", "lavfi", "-i", audio,
            "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-ar", "48000", str(path),
        ],
        check=True,
    )
    return path


@pytest.fixture()
def session(tmp_path: Path) -> Path:
    """12 s: 4 s speech-ish, 3 s pause, 5 s speech-ish."""
    speech_a = synth(tmp_path / "a.mp4", seconds=4, tone=220, colour="navy")
    pause = tmp_path / "p.mp4"
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "lavfi", "-i", "color=c=black:s=320x180:r=30:d=3",
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-t", "3", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(pause),
        ],
        check=True,
    )
    speech_b = synth(tmp_path / "b.mp4", seconds=5, tone=330, colour="darkgreen")
    concat = tmp_path / "concat.txt"
    concat.write_text("".join(f"file '{p}'\n" for p in (speech_a, pause, speech_b)), encoding="utf-8")
    out = tmp_path / "session.mp4"
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
         "-i", str(concat), "-c", "copy", str(out)],
        check=True,
    )
    return out


def test_probe_reports_streams_and_duration(session: Path) -> None:
    info = cutroom.probe(session)
    assert info["duration"] == pytest.approx(12, abs=0.3)
    assert info["video"]["width"] == 320
    assert info["audio"]["sample_rate"] == "48000"


def test_silence_detection_finds_the_pause(session: Path) -> None:
    gaps = cutroom.silences(session, noise_db=-40, min_dur=1.5)
    assert gaps, "the 3 s pause should be detected"
    start = min(g["start"] for g in gaps)
    assert 3.5 <= start <= 4.5


def test_segments_split_on_pause_without_a_transcript(session: Path) -> None:
    segments = cutroom.build_segments(session, min_seconds=2.0)
    assert len(segments) == 2
    first, second = segments
    assert first["start"] == 0
    assert first["end"] == pytest.approx(4.0, abs=0.3), "dead air is dropped"
    assert second["start"] == pytest.approx(7.0, abs=0.3), "resumes when the pause ends"
    assert second["end"] == pytest.approx(12, abs=0.5)


def test_segments_absorb_a_short_tail(session: Path) -> None:
    segments = cutroom.build_segments(session, min_seconds=50.0)
    assert len(segments) == 1, "a short session collapses to one segment"
    assert segments[0]["end"] == pytest.approx(12, abs=0.5)


def test_edl_pads_cuts_and_clamps_to_source(session: Path) -> None:
    segments = cutroom.build_segments(session, min_seconds=2.0)
    edl = cutroom.build_edl(segments, total_duration=12)
    assert edl["segments"][0]["in"] == 0.0, "lead-in cannot go below zero"
    assert edl["segments"][1]["out"] == pytest.approx(12, abs=0.001), "tail clamped"
    assert edl["expected_duration"] == pytest.approx(
        sum(p["out"] - p["in"] for p in edl["segments"]), abs=0.001
    )


def test_render_and_verify_round_trip(session: Path, tmp_path: Path) -> None:
    segments = cutroom.build_segments(session, min_seconds=2.0)
    edl = cutroom.build_edl(segments, total_duration=cutroom.probe(session)["duration"])
    out = tmp_path / "out" / "render.mp4"
    result = cutroom.render(edl, out, preset="ultrafast", crf=28, fps=30)

    assert out.exists() and out.stat().st_size > 0
    assert result["parts"] == len(edl["segments"])
    assert result["probe"]["video"]["width"] == 320

    check = cutroom.verify(out, edl)
    assert check["ok"], check["problems"]
    assert check["peak_dbfs"] is None or check["peak_dbfs"] <= -1.0


def test_cli_segments_writes_an_artifact(session: Path, tmp_path: Path) -> None:
    target = tmp_path / "segments.json"
    assert cutroom.main(["segments", str(session), "--out", str(target)]) == 0
    data = json.loads(target.read_text())
    assert len(data) >= 1 and {"id", "start", "end"} <= set(data[0])
