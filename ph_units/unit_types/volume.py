# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubed(Base_UnitType):
    """Meter Cubed"""

    __symbol__ = "M3"
    __aliases__ = []
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
    __aliases__ = ["GALLON", "G"]
    __factors__ = {"L": "{}*3.785411784"}


class FootCubed(Base_UnitType):
    """Foot Cubed"""

    __symbol__ = "FT3"
    __aliases__ = ["CF"]
    __factors__ = {
        "M3": "{}*0.028316847",
        "FT3": "{}*1",
    }
