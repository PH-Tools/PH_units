# PH-units

Unit parsing and conversion for Passive House workflows — convert common PH unit types between IP and SI, parse `"{value} {unit}"` text, and carry unit info on a `float` subclass. Published on PyPI as `PH-units`. Source: https://github.com/PH-Tools/PH_units

> **Runtime constraint:** must run under **IronPython 2.7** (it is imported into Rhino/Grasshopper by `honeybee_ph` and the GH plugins) as well as CPython 3.10+. See `context/CODING_STANDARDS.md`.

## What this repo is

A single package, `ph_units`:

- `converter.py` — `convert(value, from_unit, to_unit)`.
- `parser.py` — `parse_input("0.17 BTU/HR-FT2-F") -> (value, unit)`.
- `unit_type.py` — the `Unit` type: subclasses `float`, retains unit info, supports math, inversion, and JSON/dataclass serialization.
- `unit_types/` — one module per dimension (area, density, energy, envelope, power, temperature, volume_flow, …) holding conversion factors and unit aliases.

## Where things live — read before working

| Working on… | Read |
|-------------|------|
| Scope, what belongs here | `context/PRD.md` |
| How converter/parser/`Unit`/`unit_types` fit together | `context/ARCHITECTURE.md` |
| IPy2.7 rules, adding a unit type, testing | `context/CODING_STANDARDS.md` |
| Deps, packaging, CI, release | `context/TECH_STACK.md` |
| Current / in-flight work | `planning/STATUS.md` |
| The public docs site (autodoc spoke — do not restructure) | `docs/.instructions.md` |

Full context index: `context/README.md`.

## Hard rules

1. **IronPython 2.7 compatibility is mandatory.** No f-strings, no `pathlib`/modern stdlib; comment-style type hints; guard `typing` imports. This package is loaded into Rhino — breaking IPy2.7 breaks the whole GH toolchain.
2. **Add a new unit by adding to `unit_types/`.** Each dimension module holds the factors and the accepted aliases (e.g. `"FT"`, `"ft."`, `'`). Don't hardcode conversions elsewhere.
3. **`Unit` must stay serialization-safe.** It round-trips to/from JSON and works as a dataclass field — preserve that when changing it.
4. **Verify before closeout:** `python -m pytest` (tests are per-dimension, e.g. `test_areas.py`, `test_envelope.py`).

## Ecosystem

Consumed by **honeybee_ph**, **PHX**, and the **honeybee_grasshopper_ph** plugins — a small, foundational dependency. Keep it minimal and dependency-free.
