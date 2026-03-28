# PH-Units:

A package for converting common Passive House unit types (IP | SI).

## Usage:

The most basic usage is a simple conversion from one known unit to another:

```python
>>> from ph_units.converter import convert
>>> # Convert 12.45 meters to feet...
>>> convert(12.45, "M", "FT") -> 40.85 # FT
```

The package also has a parser which can take simple text in the format: `"{value} {unit}"` and will split apart the text into a numeric part and a unit part:

```python
>>> from ph_units.parser import parse_input
>>> val, unit = parse_input("0.17 BTU/HR-FT2-F")
>>> val  # 0.17
>>> unit # 'BTU/HR-FT2-F'
```

The results of the parser can then be fed into the converter

```
>>> from ph_units.converter import convert
>>> convert(val, "W/MK", unit) -> 0.098 # BTU/HR-FT2-F
```

## Unit Types Supported:

- area (M2, FT2)
- density (KG/M3, LB/FT3)
- emissions factors (G/KWH)
- energy (Wh/M3, Wh/M2, kW/M2, kBtu/ft2, Btu/ft2)
- envelope (U-Value, R-Value)
- length (M, CM, MM, IN, FT)
- moisture vapor resistance (MNS/G, PERM-IN)
- power (kW, W, W/M2, W/ft2, W/cfm, Btu/h-ft2, Btu/h)
- speed (m/d, m/s, m/h, ft/s, ft/d)
- temperature (C, F)
- volume flow (M3/HR, CFM)
- volume (M2, FT3, LITER, GALLON)

## Adding New Units:

The conversion factors used are stored as types in the [`ph_units.unit_types`](https://github.com/PH-Tools/PH_units/tree/main/ph_units/unit_types) directory. Note that the types also allow for common 'alias' descriptions ie: 'feet' can be denoted as "FT", "ft." or even the symbol '

## The `Unit` Type:

The package also includes a new [`Unit`](https://github.com/PH-Tools/PH_units/blob/2d8a1fa6ed368b2410563a226f8ac180e103fcf9/ph_units/unit_type.py#L25) type which subclasses from `float` but also retains the unit-type information. This allows for easy conversion between units. For example:

```python
>>> from ph_units.unit_type import Unit
>>> a_meter_value = Unit(1.0, "M")
>>> print(a_meter_value)
>>> "1.0 (M)"
>>> a_foot_value = a_meter_value.as_a("FT")
>>> print(a_foot_value)
>>> "3.281(FT)"
```

This `Unit` type supports basic mathematical operations like addition and subtraction, as well as unit-related operations like 'inversion'.

The `Unit` type also supports serialization and deserialization to and from JSON. Additionally, the `Unit` type can be used as a `dataclass` field type and should serialize properly when dataclass `as_dict` is called on the parent object.

---

![Tests](https://github.com/PH-Tools/PHX/actions/workflows/ci.yaml/badge.svg)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
[![IronPython](https://img.shields.io/badge/ironpython-2.7-red.svg)](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/)
