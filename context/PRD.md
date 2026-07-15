---
DATE: 2026-07-15
STATUS: CANONICAL PRD
---

# PH-units — Product Requirements

## 1. Goal

Give the PH-Tools ecosystem one dependable, dependency-free way to parse and convert the units Passive House work uses — U-values, R-values, energy intensities, flows, densities, temperatures — between IP and SI, and to carry unit information alongside a numeric value.

## 2. Who uses it

- **honeybee_ph**, **PHX**, and the **honeybee_grasshopper_ph** plugins — as a foundational dependency, at runtime inside Rhino/Grasshopper (IronPython 2.7) and in CPython.
- Any Python code needing PH unit handling (`pip install PH-units`).

## 3. What belongs here

- `convert()` and `parse_input()`.
- The `Unit` type (a `float` subclass carrying unit info, with math/inversion + JSON/dataclass serialization).
- The `unit_types/` registry: one module per dimension, holding conversion factors and accepted aliases.

## 4. Non-goals

- **No heavy dependencies.** This is a leaf library loaded into Rhino — it must stay pure-Python and IPy2.7-safe. No numpy/pandas.
- **No domain/model logic.** It converts numbers; it doesn't know about buildings.

## 5. Success criteria

- Correct round-trip conversions across all supported dimensions.
- Loads and runs under IronPython 2.7 (no import/syntax errors in Rhino).
- `Unit` serializes/deserializes cleanly, including as a dataclass field.
- Tests cover each dimension.

## 6. Direction

- Adding a unit dimension or alias is the common change — see `CODING_STANDARDS.md`.
