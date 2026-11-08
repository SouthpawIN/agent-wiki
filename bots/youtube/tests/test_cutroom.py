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

# ------------------------------------------------------------------ packaging

SEGMENTS = [
    {"id": "seg-01", "start": 0.0, "end": 340.0, "title": "Why local models win",
     "hook_line": "Local models are the only ones you can audit", "rank": 0.82,
     "terms": ["local", "models", "privacy"]},
    {"id": "seg-02", "start": 340.0, "end": 610.0, "title": "Discord moderation stories",
     "hook_line": "", "rank": 0.51, "terms": ["discord", "moderation"]},
    {"id": "seg-03", "start": 610.0, "end": 900.0, "title": "Kart racing in Unity",
     "hook_line": "", "rank": 0.44, "terms": ["unity", "games"]},
]


def test_timestamp_formats() -> None:
    assert cutroom.timestamp(0) == "0:00"
    assert cutroom.timestamp(65) == "1:05"
    assert cutroom.timestamp(3725) == "1:02:05"


def test_title_is_front_loaded_and_capped() -> None:
    assert cutroom.make_title(SEGMENTS) == "Local models are the only ones you can audit"
    long = [{"start": 0.0, "end": 10.0, "title": "x" * 120, "rank": 1.0}]
    assert len(cutroom.make_title(long)) <= 60


def test_chapters_start_at_zero_and_merge_short_segments() -> None:
    chapters = cutroom.make_chapters(SEGMENTS)
    assert chapters[0][0] == 0.0
    assert len(chapters) == 3

    cramped = [{"start": 0.0, "end": 5.0, "title": "a"},
               {"start": 5.0, "end": 9.0, "title": "b"},
               {"start": 60.0, "end": 90.0, "title": "c"}]
    merged = cutroom.make_chapters(cramped)
    assert [name for _, name in merged] == ["a", "c"], "sub-10s chapters are merged"


def test_tags_are_deduped_and_capped() -> None:
    tags = cutroom.make_tags(SEGMENTS, channel_defaults=("local", "nous"), limit=12)
    assert tags[0] == "local" and tags.count("local") == 1
    assert "nous" in tags and len(tags) <= 12


def test_package_writes_upload_md(tmp_path: Path) -> None:
    result = cutroom.package(SEGMENTS, tmp_path / "out", premise="Three rants from one session.")
    text = (tmp_path / "out" / "upload.md").read_text(encoding="utf-8")

    assert result["chapters"][0]["time"] == "0:00"
    assert result["visibility"] == "unlisted"
    assert "Recorded live in voice chat" in text
    assert "Chris publishes; Cutroom never does" in text
    assert "sovthpaw" in text


def test_package_refuses_a_private_name(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="must not contain"):
        cutroom.package(SEGMENTS, tmp_path / "out", title="Chris explains local models")


def test_cli_package_writes_the_sheet(tmp_path: Path) -> None:
    source = tmp_path / "segments.json"
    source.write_text(json.dumps(SEGMENTS), encoding="utf-8")
    out = tmp_path / "pkg"
    assert cutroom.main(["package", str(source), "--out", str(out), "--premise", "One session."]) == 0
    assert (out / "upload.md").exists()
