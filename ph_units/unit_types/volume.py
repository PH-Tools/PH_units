# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubed(Base_UnitType):
    """Meter Cubed"""

    __symbol__ = "M3"
    __aliases__ = ["M³", "M3", "METERCUBED", "CUBICMETER", "METERS-3"]
    __factors__ = {
        "M3": "{}*1",
        "FT3": "{}*35.31466672",
        "IN3": "{}*61023.74409473229",
        "L": "{}*1000",
        "GA": "{}*264.1720524",
    }


class Liter(Base_UnitType):
    """Liter"""

    __symbol__ = "L"
    __aliases__ = ["LITER", "LITRE"]
    __factors__ = {
        "M3": "{}*0.001",
        "FT3": "{}*0.035314667",
        "IN3": "{}*61.02374409473229",
        "L": "{}*1",
        "GA": "{}*0.264172",
    }


class Gallon(Base_UnitType):
    """Gallon"""

    __symbol__ = "GA"
    __aliases__ = ["GALLON", "G", "GAL"]
    __factors__ = {
        "M3": "{}*0.003785411784",
        "FT3": "{}*0.13368055555555556",
        "IN3": "{}*231",
        "L": "{}*3.785411784",
        "GA": "{}*1",
    }


class FootCubed(Base_UnitType):
    """Foot Cubed"""

    __symbol__ = "FT3"
    __aliases__ = ["CF", "FT3", "FT³", "ft³", "CUBIC FOOT", "CUBIC FEET", "FEET-3"]
    __factors__ = {
        "M3": "{}*0.028316847",
        "FT3": "{}*1",
        "IN3": "{}*1728",
        "L": "{}*28.316846592",
        "GA": "{}*7.48051948051948",
    }


class InchCubed(Base_UnitType):
    """Inch Cubed"""

    __symbol__ = "IN3"
    __aliases__ = [
        "INCHCUBED",
        "INCHCUBIC",
        "INCH^3",
        "INCH^3",
        "INCHES-CUBED",
        "INCHES-3",
    ]
    __factors__ = {
        "M3": "{}*0.000016387064",
        "FT3": "{}*0.0005787037037037037",
        "IN3": "{}*1",
        "L": "{}*0.0163871",
        "GA": "{}*0.004329004329004329",
    }
