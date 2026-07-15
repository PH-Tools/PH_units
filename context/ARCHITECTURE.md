---
DATE: 2026-07-15
STATUS: CANONICAL
---

# PH-units — Architecture

## The pieces

```
"0.17 BTU/HR-FT2-F"  ──parser.parse_input──►  (0.17, "BTU/HR-FT2-F")
                                                      │
value + from_unit + to_unit  ──converter.convert──►  converted value
                                                      │
Unit(1.0, "M").as_a("FT")  ──unit_type.Unit──►  3.281 (FT)   (float subclass, keeps its unit)
```

- **`parser.py`** — `parse_input(text)` splits `"{value} {unit}"` into a numeric part and a unit string.
- **`converter.py`** — `convert(value, from_unit, to_unit)` looks up factors in `unit_types/` and returns the converted number.
- **`unit_type.py`** — `Unit`: subclasses `float`, retains the unit string, supports math + inversion, and serializes to/from JSON (and as a dataclass field).
- **`unit_types/`** — the registry. One module per dimension (`area.py`, `envelope.py`, `power.py`, `temperature.py`, …), each defining the conversion factors and the accepted aliases for its units. `_base.py` holds the shared base.

## How a conversion resolves

`convert()` normalizes the unit strings (via each dimension's alias table in `unit_types/`) and applies the factor. Aliases matter: `"FT"`, `"ft."`, and `'` all mean feet — the alias handling lives in the dimension module, not in the converter.

## Design constraints

- Pure Python, **no third-party deps**, IPy2.7-safe — because it loads inside Rhino. See `CODING_STANDARDS.md`.
- All conversion knowledge lives in `unit_types/`; `converter.py` stays generic.
