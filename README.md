# PH_units:
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
>>>
>>> from ph_units.converter import convert
>>> convert(val, "W/MK", unit) -> 0.098 # BTU/HR-FT2-F
```

 - - -
 The conversion factors used are stored as types in the [`ph_units.unit_types`](https://github.com/PH-Tools/PH_units/tree/main/ph_units/unit_types) directory. Note that the types also allow for common 'alias' descriptions ie: 'feet' can be denoted as "FT", "ft." or even the symbol '


## Types:
* Length (m, cm, mm, in, ft)
* Area (m2, ft2)
* volume (m2, ft3, liters, gallons)