#!/usr/bin/env python3
"""Validate the FOURFOLD community marketplace catalogue and data packs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "marketplace" / "catalog.json"
PACK_DIR = ROOT / "marketplace" / "packs"
CATEGORIES = {"creature", "dimension", "weapon", "vehicle", "quest", "expansion", "settlement", "dungeon", "survival"}
COLLECTIONS = {"items", "creatures", "dimensions", "weapons", "vehicles", "quests", "recipes", "lore"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,48}$")
CONTENT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{1,48}$")
FORBIDDEN_KEYS = {"script", "code", "html", "srcdoc"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def reject_executable_fields(value: object, where: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = str(key).lower()
            if lowered in FORBIDDEN_KEYS or (lowered.startswith("on") and lowered[2:].isalpha()):
                fail(f"{where}: forbidden executable field {key!r}")
            reject_executable_fields(child, f"{where}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_executable_fields(child, f"{where}[{index}]")


def main() -> None:
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Cannot read marketplace/catalog.json: {exc}")

    if not isinstance(catalog, list) or not catalog:
        fail("Marketplace catalogue must be a non-empty JSON array.")

    seen: set[str] = set()
    for index, entry in enumerate(catalog):
        where = f"catalog[{index}]"
        if not isinstance(entry, dict):
            fail(f"{where} must be an object.")
        pack_id = entry.get("id")
        if not isinstance(pack_id, str) or not ID_RE.fullmatch(pack_id):
            fail(f"{where} has an invalid pack ID.")
        if pack_id in seen:
            fail(f"Duplicate catalogue ID: {pack_id}")
        seen.add(pack_id)

        if entry.get("category") not in CATEGORIES:
            fail(f"{where} has an unsupported category.")
        download = entry.get("download")
        if not isinstance(download, str) or not download.startswith("./marketplace/packs/"):
            fail(f"{where} must use a local marketplace pack URL.")
        relative = download.removeprefix("./")
        pack_path = (ROOT / relative).resolve()
        if PACK_DIR.resolve() not in pack_path.parents or not pack_path.is_file():
            fail(f"{where} points to a missing or out-of-folder pack: {download}")

        try:
            pack = json.loads(pack_path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{pack_path.relative_to(ROOT)} is not valid JSON: {exc}")
        if not isinstance(pack, dict):
            fail(f"{pack_path.relative_to(ROOT)} must contain a JSON object.")
        if pack.get("id") != pack_id:
            fail(f"{where} ID does not match manifest ID in {download}.")
        for field in ("name", "version", "author", "icon", "description"):
            if not isinstance(pack.get(field), str) or not pack[field]:
                fail(f"{download} is missing a valid {field} field.")
        if len(pack["name"]) > 72 or len(pack["icon"]) > 8:
            fail(f"{download} has an overlong name or icon.")

        content = pack.get("content")
        if not isinstance(content, dict):
            fail(f"{download} has no content object.")
        unknown = set(content) - COLLECTIONS
        if unknown:
            fail(f"{download} contains unsupported collections: {sorted(unknown)}")

        reject_executable_fields(content, pack_id)
        for collection, items in content.items():
            if not isinstance(items, list) or len(items) > 80:
                fail(f"{download}: {collection} must be an array with at most 80 entries.")
            for item_index, item in enumerate(items):
                if not isinstance(item, dict):
                    fail(f"{download}: {collection}[{item_index}] must be an object.")
                if collection in {"items", "creatures", "dimensions", "weapons", "vehicles", "quests"}:
                    item_id = item.get("id")
                    if not isinstance(item_id, str) or not CONTENT_ID_RE.fullmatch(item_id):
                        fail(f"{download}: invalid {collection} content ID at index {item_index}.")
                for field in ("name", "label", "description", "desc", "title", "text", "icon"):
                    if field in item and (not isinstance(item[field], str) or len(item[field]) > 500):
                        fail(f"{download}: invalid {field} in {collection}[{item_index}].")

    print(f"Validated {len(catalog)} marketplace packs successfully.")


if __name__ == "__main__":
    main()
