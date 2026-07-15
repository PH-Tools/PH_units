---
DATE: 2026-07-15
STATUS: CANONICAL
---

# PH-units — Tech Stack

## Runtime

- **IronPython 2.7** (loaded into Rhino/Grasshopper via `honeybee_ph` and the GH plugins) **and** CPython ≥ 3.10. Written to the intersection.

## Dependencies

- **None at runtime** — deliberately. This is a leaf library; keep it dependency-free so it stays loadable in Rhino.
- Dev extras: `black`, `coverage`, `pytest`, `pytest-cov`.

## Packaging

- setuptools + wheel; single package `ph_units`. Published to PyPI as **`PH-units`**.

## Testing

- **pytest** — `python -m pytest`. Tests are per-dimension (`test_areas.py`, `test_envelope.py`, `test_hvac.py`, `test_converter.py`, `test_as_a.py`, …). Coverage via `pytest-cov`.

## Formatting

- **Black** (line length per `pyproject.toml`).

## Versioning & release

- `bump-my-version` (`[tool.bumpversion]`) updates the version in `pyproject.toml`; tags `v{version}`.
- CI: `.github/workflows/ci.yml` (pytest + build/publish).

## Docs

- `docs/` is a **spoke** in the ph-docs Astro hub (docs.passivehousetools.com) — `index.md`, `nav.yml`, `getting-started.md`, `packages.md`. API reference is generated from docstrings at build time. Do not restructure `docs/`; keep `docs/nav.yml` current. See `docs/.instructions.md`.

## Housekeeping

- The repo root has accumulated some stray build artifacts (`UNKNOWN.egg-info/`, `htmlcov/` + `_coverage_html/`, a stray `ph_units-1.5.28/`). These are generated/leftover, gitignored where relevant, and are **not** part of the package — ignore them (and don't index them).
