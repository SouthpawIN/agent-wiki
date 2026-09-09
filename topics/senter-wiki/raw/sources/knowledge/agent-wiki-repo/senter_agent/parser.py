"""Parse ordinary and all-caps GOOP markdown documents without executing them."""

import hashlib
import os
import re
from pathlib import Path

from .model import GoopDeclaration, GoopDocument, normalize_kind

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


def _items(section: str) -> list[str]:
    """Return only declarative Markdown list items, never arbitrary prose."""
    return [m.group(1).strip() for m in re.finditer(r"^\s*[-*]\s+(.+?)\s*$", section, re.M)]


def _declaration(path: Path, sections: dict[str, str]) -> GoopDeclaration:
    values = {key: _items(value) for key, value in sections.items()}
    return GoopDeclaration(
        name=path.stem,
        purpose=values.get("purpose", []),
        allowed=values.get("allowed", []),
        forbidden=values.get("forbidden", []),
        approvals=values.get("approval", values.get("approvals", [])),
        skills=values.get("skills", []),
        agents=values.get("agent", values.get("agents", [])),
        loops=values.get("loop", values.get("loops", [])),
        secret_refs=values.get("secret references", values.get("secrets", [])),
    )


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
    sections = _sections(body)
    declaration = _declaration(path, sections) if path.stem.isupper() else GoopDeclaration(name=path.stem)
    return GoopDocument(
        path=path,
        title=title,
        kind=kind,
        sections=sections,
        tags=[x for x in tags if x],
        links=links,
        source_hash=hashlib.sha256(raw.encode()).hexdigest(),
        explicit_kind=explicit_kind,
        declaration=declaration.__dict__,
    )


def parse_tree(root: str | Path, sources: list[str | Path] | None = None) -> list[GoopDocument]:
    root = Path(root)
    if sources is None:
        value = os.environ.get("SENTER_GOOP_SOURCES")
        sources = [item.strip() for item in value.split(",") if item.strip()] if value else None
    roots = [root / Path(source) for source in sources] if sources else [root]
    ignored = {".git", "node_modules", "__pycache__", ".pytest_cache", "dist", "build"}
    paths = []
    for base in roots:
        if not base.exists():
            continue
        paths.extend(
            path for path in base.rglob("*.md")
            if not any(part.startswith(".") or part in ignored for part in path.relative_to(root).parts)
        )
    return [parse_markdown(path) for path in sorted(set(paths))]
