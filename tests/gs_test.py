#!/usr/bin/env python3
"""GS-001..004 — a3ui-graphics-v0.1 gate. Stdlib only."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEVEL_DOCS = [
    "00-foundations.md",
    "01-micro-geometry.md",
    "02-motion.md",
    "03-micro-interactions.md",
    "04-system-chrome.md",
    "05-shaders-vfx.md",
    "06-audio.md",
    "07-haptic.md",
]

TOKEN_FILES = [
    "colors.json",
    "elevation.json",
    "surfaces.json",
    "motion.json",
    "audio.json",
    "haptic.json",
    "typography.json",
]

HEADINGS = ("## Rationale", "## Limiti", "## Fase")

PHASES = ("fase-1", "remainder-l2", "S-D2", "S-D3", "S-D4", "S-D5")


class Fail(Exception):
    pass


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise Fail(f"{path.relative_to(ROOT)}: JSON invalid: {e}") from e


def resolve(schema: dict, root: dict) -> dict:
    ref = schema.get("$ref")
    if not ref:
        return schema
    if not ref.startswith("#/"):
        raise Fail(f"unsupported $ref {ref}")
    node: object = root
    for part in ref[2:].split("/"):
        if not isinstance(node, dict) or part not in node:
            raise Fail(f"unresolved $ref {ref}")
        node = node[part]
    if not isinstance(node, dict):
        raise Fail(f"$ref {ref} is not an object")
    return node


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_number(value: object) -> bool:
    return is_int(value) or isinstance(value, float)


def check_schema(instance: object, schema: dict, root: dict, path: str) -> None:
    schema = resolve(schema, root)
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(instance, dict):
            raise Fail(f"{path}: expected object")
        for key in schema.get("required", []):
            if key not in instance:
                raise Fail(f"{path}: missing required {key}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(props)
            if extra:
                raise Fail(f"{path}: extra keys {sorted(extra)}")
        for key, value in instance.items():
            if key in props:
                check_schema(value, props[key], root, f"{path}.{key}")
        return
    if expected == "array":
        if not isinstance(instance, list):
            raise Fail(f"{path}: expected array")
        if "minItems" in schema and len(instance) < schema["minItems"]:
            raise Fail(f"{path}: minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            raise Fail(f"{path}: maxItems")
        item_schema = schema.get("items")
        if item_schema:
            for i, item in enumerate(instance):
                check_schema(item, item_schema, root, f"{path}[{i}]")
        return
    if expected == "string":
        if not isinstance(instance, str):
            raise Fail(f"{path}: expected string")
    elif expected == "boolean":
        if not isinstance(instance, bool):
            raise Fail(f"{path}: expected boolean")
    elif expected == "integer":
        if not is_int(instance):
            raise Fail(f"{path}: expected integer")
    elif expected == "number":
        if not is_number(instance):
            raise Fail(f"{path}: expected number")
    if "const" in schema and instance != schema["const"]:
        raise Fail(f"{path}: const {schema['const']!r} != {instance!r}")
    if "enum" in schema and instance not in schema["enum"]:
        raise Fail(f"{path}: {instance!r} not in enum")
    if expected in {"number", "integer"} and is_number(instance):
        if "minimum" in schema and instance < schema["minimum"]:
            raise Fail(f"{path}: minimum")
        if "maximum" in schema and instance > schema["maximum"]:
            raise Fail(f"{path}: maximum")


def gs001() -> None:
    required = [
        ROOT / "docs" / "roadmap.md",
        ROOT / "README.md",
        *[ROOT / "docs" / name for name in LEVEL_DOCS],
        *[ROOT / "tokens" / name for name in TOKEN_FILES],
        *[ROOT / "schemas" / name.replace(".json", ".schema.json") for name in TOKEN_FILES],
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
    if missing:
        raise Fail("missing: " + ", ".join(missing))


def gs002() -> None:
    for name in TOKEN_FILES:
        token_path = ROOT / "tokens" / name
        schema_path = ROOT / "schemas" / name.replace(".json", ".schema.json")
        data = load_json(token_path)
        schema = load_json(schema_path)
        check_schema(data, schema, schema, name)
        if data.get("version") != "0.1":
            raise Fail(f"{name}: version must be 0.1")
        doc = ROOT / data["doc"]
        if not doc.is_file():
            raise Fail(f"{name}: doc {data['doc']} missing")


def gs003() -> None:
    for name in LEVEL_DOCS:
        text = (ROOT / "docs" / name).read_text(encoding="utf-8")
        for heading in HEADINGS:
            if heading not in text:
                raise Fail(f"{name}: missing {heading}")
        if not re.search(r"\*\*Phase:\*\*\s*`([^`]+)`", text):
            raise Fail(f"{name}: missing **Phase:** code")


def gs004() -> None:
    roadmap = (ROOT / "docs" / "roadmap.md").read_text(encoding="utf-8")
    for inv in ("GR-001", "GR-002", "GR-003", "GR-004"):
        if inv not in roadmap:
            raise Fail(f"roadmap missing {inv}")
    for phase in PHASES:
        if phase not in roadmap:
            raise Fail(f"roadmap missing phase {phase}")
    for name in LEVEL_DOCS:
        if name not in roadmap:
            raise Fail(f"roadmap missing {name}")
        text = (ROOT / "docs" / name).read_text(encoding="utf-8")
        match = re.search(r"\*\*Phase:\*\*\s*`([^`]+)`", text)
        if not match:
            raise Fail(f"{name}: phase code")
        code = match.group(1).split()[0]
        if code not in roadmap:
            raise Fail(f"roadmap missing declared phase {code} from {name}")
    for i in range(1, 8):
        if not re.search(rf"\bL{i}\b|\b{i} ", roadmap):
            # levels are written as "L1" or "1 physicality" etc.
            if f"| {i} " not in roadmap and f"L{i}" not in roadmap:
                raise Fail(f"roadmap does not track level {i}")
    for name in TOKEN_FILES:
        data = load_json(ROOT / "tokens" / name)
        doc_text = (ROOT / data["doc"]).read_text(encoding="utf-8")
        if name not in doc_text and f"`tokens/{name}`" not in doc_text:
            raise Fail(f"{data['doc']} does not mention {name}")
        if data["phase"] not in roadmap:
            raise Fail(f"roadmap missing token phase {data['phase']} ({name})")


CHECKS = [
    ("GS-001", gs001),
    ("GS-002", gs002),
    ("GS-003", gs003),
    ("GS-004", gs004),
]


def main() -> int:
    failed = 0
    for name, fn in CHECKS:
        try:
            fn()
        except Fail as e:
            print(f"{name} FAIL  {e}")
            failed += 1
        else:
            print(f"{name} PASS")
    if failed:
        print(f"\n{failed} failed")
        return 1
    print("\nGS-001..004 PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
