"""Parse ordinary and all-caps GOOP markdown documents without executing them."""

import hashlib
import re
from pathlib import Path

from .model import GoopDocument, normalize_kind

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)|\[\[([^]]+)\]\]")
_KIND = re.compile(r"(?:type|kind|primitive)\s*:\s*([A-Za-z_-]+)", re.I)


def _sections(body: str) -> dict[str, str]:
    matches = list(_HEADING.finditer(body))
    result: dict[str, str] = {}
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        result[match.group(1).strip().lower()] = body[start:end].strip()
    return result


def parse_markdown(path: str | Path) -> GoopDocument:
    path = Path(path)
    raw = path.read_text(encoding="utf-8")
    front = _FRONTMATTER.match(raw)
    metadata = front.group(1) if front else ""
    body = raw[front.end():] if front else raw
    title_match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
    explicit = _KIND.search(metadata)
    explicit_kind = normalize_kind(explicit.group(1)) if explicit else None
    kind = explicit_kind or ("context" if path.stem.isupper() else "context")
    tags_match = re.search(r"tags\s*:\s*\[([^]]*)\]", metadata, re.I)
    tags = [x.strip().strip("'\"") for x in tags_match.group(1).split(",")] if tags_match else []
    links = [a or b for a, b in _LINK.findall(raw)]
    return GoopDocument(
        path=path,
        title=title,
        kind=kind,
        sections=_sections(body),
        tags=[x for x in tags if x],
        links=links,
        source_hash=hashlib.sha256(raw.encode()).hexdigest(),
        explicit_kind=explicit_kind,
    )


def parse_tree(root: str | Path) -> list[GoopDocument]:
    root = Path(root)
    return [parse_markdown(path) for path in sorted(root.rglob("*.md"))]
