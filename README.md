# a3ui-graphics — renderer-neutral visual tokens

![a3ui-graphics cover](docs/assets/cover.png)

## What it is

A renderer-neutral specification of visual tokens, schemas, rationale, limits, and implementation phases for A3UI consumers. `manifest.json` is the machine-readable index; only entries marked `consumabile: true` in phase 1 may be consumed.

## What it is not

It is not application code, not a second A3UI renderer, not a source of epistemic facts, and not permission to consume deferred phases. It does not make claims about physical display performance.

## Status

- **VERIFIED:** GS-001..GS-004 and CS-001..CS-006, token/schema consistency, manifest alignment, and phase-1 boundaries.
- **UNVERIFIED:** downstream visual fidelity and hardware-specific rendering.

## Get it

```bash
git clone https://github.com/valeriobitzone-png/a3ui-graphics.git
cd a3ui-graphics
# Requirements: Python 3
```

Structure: `manifest.json`, `tokens/`, `schemas/`, `docs/`, and `tests/`. Phase-1 entries currently cover colors, elevation, and surfaces; motion, typography, audio, and haptic remain deferred.

## Prove it

```bash
python3 tests/gs_test.py
python3 tests/consumer_test.py
```

Expected result: both gates pass and no deferred token is treated as consumable.

## Integrate it

Read `manifest.json`, consume only phase-1 entries, preserve the declared tag/version/path provenance, and validate your integration with `tools/valida_token.py` when available in your consumer repository. Never glob tokens or silently consume deferred phases.

## License

Specification, token, schema, and documentation assets are CC BY 4.0 (`LICENSE`).

## Provenance

Measured: schema checks, manifest/disc alignment, phase checks, and consumer tests. Visual quality on a particular device is downstream evidence and remains unverified until measured there.
