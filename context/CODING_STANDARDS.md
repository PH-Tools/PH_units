---
DATE: 2026-07-15
STATUS: CANONICAL ENGINEERING STANDARD
---

# PH-units — Coding Standards

## 1. IronPython 2.7 compatibility (mandatory)

The generic dual-runtime rules (banned syntax and modules, comment-style type
hints, guarded `typing` imports, defensive third-party imports, and the lint
settings they imply) live in the **ironpython-27-compatibility** skill. Apply it
before editing anything on the Rhino load path. Only this repo's specifics are
recorded below.

This package is imported into Rhino/Grasshopper. The whole package is on the
load path; there is no CPython-only zone.

**No third-party runtime dependencies.** Keep it a pure-Python leaf.

## 2. Adding a unit type / dimension

- Conversion factors and aliases live in `ph_units/unit_types/<dimension>.py` (extend an existing module or add a new one following `_base.py`).
- Register all accepted spellings as **aliases** (e.g. `"FT"`, `"ft."`, `'`), so the parser/converter accept what users actually type.
- Never hardcode a conversion in `converter.py` — it stays generic and reads from `unit_types/`.

## 3. The `Unit` type

`Unit` subclasses `float`, keeps its unit string, and must remain serialization-safe: JSON round-trip and use as a dataclass field. Preserve these when editing `unit_type.py`.

## 4. Formatting

- **Black** (line length per `pyproject.toml`).

## 5. Testing

- **pytest** — `python -m pytest`.
- Tests are organized per dimension. A new dimension or alias needs a matching `test_<dimension>.py` case (and `test_converter.py` / `test_as_a.py` coverage where relevant).

## Closeout checklist

- [ ] IPy2.7-safe (no f-strings/pathlib; guarded `typing`; comment-style hints; no new deps).
- [ ] New units added via `unit_types/` with all aliases; `converter.py` untouched-and-generic.
- [ ] `Unit` still JSON/dataclass serialization-safe if changed.
- [ ] `python -m pytest` passes; new dimension/alias has a test.
- [ ] black clean.
