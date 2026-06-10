"""Obsidian vault memory.

Safety model (matches Smart OS rules):
- Reads/indexing: allowed anywhere in the vault, metadata + content of .md only.
- Writes: ONLY inside the "SmartOS" subfolder of the vault (inbox pattern).
  Writes anywhere else must go through a pending action / approval.
- Never touches non-markdown files. Never follows paths outside the vault.

Vault path comes from SMARTOS_VAULT env var or configure_vault().
"""

import os
import re
from datetime import datetime, timezone
from pathlib import Path

SAFE_SUBDIR = "SmartOS"

_vault: Path | None = None


def configure_vault(path: str | None = None) -> Path | None:
    global _vault
    raw = path or os.environ.get("SMARTOS_VAULT")
    _vault = Path(raw).resolve() if raw else None
    return _vault


def get_vault() -> Path:
    if _vault is None:
        configure_vault()
    if _vault is None or not _vault.is_dir():
        raise FileNotFoundError(
            "Obsidian vault not configured. Set SMARTOS_VAULT to your vault path.")
    return _vault


def _parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta


def index_vault(max_files: int = 5000) -> list[dict]:
    """Walk the vault and return note metadata (no secrets, .md only)."""
    vault = get_vault()
    notes = []
    for path in sorted(vault.rglob("*.md")):
        if len(notes) >= max_files:
            break
        rel = path.relative_to(vault)
        if any(part.startswith(".") for part in rel.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        meta = _parse_frontmatter(text)
        tags = re.findall(r"(?<!\S)#([\w/-]+)", text)
        notes.append({
            "path": str(rel),
            "title": meta.get("title") or path.stem,
            "tags": sorted(set(tags))[:20],
            "frontmatter": meta,
            "chars": len(text),
            "modified": datetime.fromtimestamp(
                path.stat().st_mtime, tz=timezone.utc).isoformat(),
        })
    return notes


def read_note(rel_path: str) -> str:
    vault = get_vault()
    target = (vault / rel_path).resolve()
    if not target.is_relative_to(vault):
        raise PermissionError("path escapes the vault")
    if target.suffix != ".md":
        raise PermissionError("only markdown notes can be read")
    return target.read_text(encoding="utf-8", errors="ignore")


def _safe_write_path(rel_path: str) -> Path:
    vault = get_vault()
    target = (vault / SAFE_SUBDIR / rel_path).resolve()
    safe_root = (vault / SAFE_SUBDIR).resolve()
    if not target.is_relative_to(safe_root):
        raise PermissionError("writes are restricted to the SmartOS folder")
    if target.suffix != ".md":
        raise PermissionError("only markdown notes can be written")
    return target


def write_note(rel_path: str, content: str) -> str:
    """Write a note inside the SmartOS inbox folder. Safe by construction."""
    target = _safe_write_path(rel_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return str(target.relative_to(get_vault()))


def append_daily_log(entry: str, now: datetime | None = None) -> str:
    """Append a timestamped line to today's log in SmartOS/Daily Logs/."""
    now = now or datetime.now(timezone.utc)
    rel = f"Daily Logs/{now:%Y-%m-%d}.md"
    target = _safe_write_path(rel)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text(f"# Daily Log {now:%Y-%m-%d}\n\n", encoding="utf-8")
    with target.open("a", encoding="utf-8") as f:
        f.write(f"- {now:%H:%M} {entry.strip()}\n")
    return str(target.relative_to(get_vault()))
