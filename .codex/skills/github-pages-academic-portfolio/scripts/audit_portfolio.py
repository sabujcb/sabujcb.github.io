#!/usr/bin/env python3
"""Run dependency-free structural checks for a Jekyll academic portfolio."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


FRONT_MATTER = re.compile(r"\A---\s*\n(?P<header>.*?)\n---\s*\n", re.DOTALL)
FIELD = re.compile(r"^(?P<key>[A-Za-z_][\w-]*):\s*(?P<value>.*?)\s*$")
ROOT_LINK = re.compile(r"(?:href=[\"']|\]\()(?P<path>/[^\"')#?\s]*)(?:#[^\"')\s]*)?")


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("missing YAML front matter")
    fields: dict[str, str] = {}
    for line in match.group("header").splitlines():
        field = FIELD.match(line)
        if field:
            fields[field.group("key")] = field.group("value").strip('"\'')
    return fields


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    root = args.repository.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    required = ("_config.yml", "Gemfile", "_pages", ".github/workflows/deploy.yml")
    for relative in required:
        if not (root / relative).exists():
            errors.append(f"missing required path: {relative}")

    pages: list[tuple[Path, dict[str, str]]] = []
    for path in sorted((root / "_pages").glob("*.md")):
        try:
            fields = front_matter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(root)}: {error}")
            continue
        pages.append((path, fields))
        if not fields.get("title"):
            errors.append(f"{path.relative_to(root)}: missing title")
        if not fields.get("permalink"):
            warnings.append(f"{path.relative_to(root)}: missing explicit permalink")

    permalinks = [fields.get("permalink") for _, fields in pages if fields.get("permalink")]
    for permalink, count in Counter(permalinks).items():
        if count > 1:
            errors.append(f"duplicate permalink {permalink!r} appears {count} times")

    nav_titles = [
        fields.get("title", "").casefold()
        for _, fields in pages
        if fields.get("nav", "").casefold() == "true"
    ]
    for title, count in Counter(nav_titles).items():
        if title and count > 1:
            errors.append(f"duplicate navigation title {title!r} appears {count} times")

    known_routes = set(permalinks)
    known_routes.add("/")
    for path, _ in pages:
        text = path.read_text(encoding="utf-8")
        for match in ROOT_LINK.finditer(text):
            route = match.group("path")
            if route.startswith("//") or "." in Path(route).name:
                continue
            normalized = route if route.endswith("/") else f"{route}/"
            if normalized not in known_routes:
                warnings.append(f"{path.relative_to(root)}: unresolved root-relative route {route}")

    profile = root / "assets/img/sabuj.jpg"
    if not profile.exists():
        warnings.append("expected profile image assets/img/sabuj.jpg was not found")

    for path in root.rglob("*.md"):
        if any(part in {".git", "node_modules", "tmp", "vendor"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace").casefold()
        if "lorem ipsum" in text or "[todo" in text:
            errors.append(f"placeholder content remains in {path.relative_to(root)}")

    for item in errors:
        print(f"ERROR: {item}")
    for item in sorted(set(warnings)):
        print(f"WARN: {item}")
    print(f"Audited {len(pages)} page files: {len(errors)} error(s), {len(set(warnings))} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
