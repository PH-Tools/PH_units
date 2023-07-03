# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubed(Base_UnitType):
    """Meter Cubed"""

    __symbol__ = "M3"
    __aliases__ = ["M³", "M3", "METERCUBED", "CUBICMETER"]
    __factors__ = {
        "M3": "{}*1",
        "FT3": "{}*35.31466672",
        "L": "{}*1000",
        "GA": "{}*264.1720524",
    }


class Liter(Base_UnitType):
    """Liter"""

    __symbol__ = "L"
    __aliases__ = ["LITER", "LITRE"]
    __factors__ = {
        "L": "{}*1",
        "GA": "{}*0.264172",
        "FT3": "{}*0.035314667",
        "M3": "{}*0.001",
    }


class Gallon(Base_UnitType):
    """Gallon"""

    __symbol__ = "GA"
    __aliases__ = ["GALLON", "G", "GAL"]
    __factors__ = {
        "GA": "{}*1",
        "L": "{}*3.785411784",
        "M3": "{}*0.003785411784",
        "FT3": "{}*0.13368055555555556",
    }


class FootCubed(Base_UnitType):
    """Foot Cubed"""

    __symbol__ = "FT3"
    __aliases__ = ["CF", "FT3", "FT³", "CUBIC FOOT", "CUBIC FEET"]
    __factors__ = {
        "M3": "{}*0.028316847",
        "FT3": "{}*1",
        "L": "{}*28.316846592",
        "GA": "{}*7.48051948051948",
    }
