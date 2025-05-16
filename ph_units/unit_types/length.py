# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class Meter(Base_UnitType):
    """Meter"""

    __symbol__ = "M"
    __aliases__ = ["METER", "METERS"]
    __factors__ = {
        "M": "{}*1",
        "CM": "{}*100",
        "MM": "{}*1000",
        "FT": "{}*3.280839895",
        "IN": "{}*39.3701",
        "MIL": "{}*39370.07874",
    }


class Centimeter(Base_UnitType):
    """Centimeter"""

    __symbol__ = "CM"
    __aliases__ = ["CENTIMETER", "CENTIMETERS"]
    __factors__ = {
        "M": "{}*0.01",
        "CM": "{}*1",
        "MM": "{}*10",
        "FT": "{}*0.0328",
        "IN": "{}*0.3937",
        "MIL": "{}*393.7007874",
    }


class Millimeter(Base_UnitType):
    """Millimeter"""

    __symbol__ = "MM"
    __aliases__ = ["MILLIMETER", "MILLIMETERS"]
    __factors__ = {
        "MM": "{}*1",
        "M": "{}*0.001",
        "CM": "{}*0.1",
        "FT": "{}*0.003280842",
        "IN": "{}*0.039370100",
        "MIL": "{}*39.37007874",
    }


class Inch(Base_UnitType):
    """Inch"""

    __symbol__ = "IN"
    __aliases__ = ['"', "IN.", "INCH", "INCHES"]
    __factors__ = {
        "M": "{}*0.0254",
        "CM": "{}*2.54",
        "MM": "{}*25.4",
        "FT": "{}/12",
        "IN": "{}*1",
        "MIL": "{}*1000",
    }


class Foot(Base_UnitType):
    """Foot"""

    __symbol__ = "FT"
    __aliases__ = ["'", "FT.", "FEET", "FOOT"]
    __factors__ = {
        "M": "{}*0.3048",
        "CM": "{}*30.48",
        "MM": "{}*304.8",
        "FT": "{}*1",
        "IN": "{}*12",
        "MIL": "{}*12000",
    }


class Mil(Base_UnitType):
    """Mil"""

    __symbol__ = "MIL"
    __aliases__ = ["MIL", "MILS"]
    __factors__ = {
        "M": "{}*0.0000254",
        "CM": "{}*0.00254",
        "MM": "{}*0.0254",
        "FT": "{}*0.0000833333",
        "IN": "{}*0.001",
        "MIL": "{}*1",
    }