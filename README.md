# PH_units:
A simple package for converting common Passive House unit types (IP | SI).

# Usage:
```python
>>> from ph_units.converter import convert
>>> convert(12.45, "M", "FT") -> 40.85 # FT
```

````python
>>> from ph_units.parser import parse_input
>>> val, unit = parse_input("12.45 FT")
>>> val  # 12.45
>>> unit # 'FT'
>>>
>>> from ph_units.converter import convert
>>> convert(val, "M", unit) -> 40.85 # FT
```