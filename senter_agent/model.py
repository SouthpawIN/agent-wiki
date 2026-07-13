from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

PRIMITIVES = ("context", "skill", "agent", "loop")

@dataclass
class GoopDocument:
    path: Path
    title: str
    kind: str = "context"
    sections: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    source_hash: str = ""
    explicit_kind: Optional[str] = None

@dataclass
class Proposal:
    primitive: str
    slug: str
    reason: str
    source_documents: list[str]
    status: str = "proposed"

    def as_dict(self) -> dict:
        return {
            "primitive": self.primitive,
            "slug": self.slug,
            "reason": self.reason,
            "source_documents": self.source_documents,
            "status": self.status,
        }


def normalize_kind(value: str) -> str:
    value = value.strip().lower().rstrip("s")
    aliases = {"context": "context", "skill": "skill", "agent": "agent", "loop": "loop"}
    return aliases.get(value, "context")


def title_slug(title: str) -> str:
    import re
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled"
