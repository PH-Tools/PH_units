# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterSquare(Base_UnitType):
    """Meter Square"""

    __symbol__ = "M2"
    __aliases__ = ["SM", "SQM", "SQ.M", "SQ-M", "SQ-METER", "SQ-METERS", "M²"]
    __factors__ = {
        "M2": "{}*1",
        "CM2": "{}*10_000",
        "MM2": "{}*1_000_000",
        "FT2": "{}*10.76391042",
    }


class CentimeterSquare(Base_UnitType):
    """Centimeter Square"""

    __symbol__ = "CM2"
    __aliases__ = ["SQCM", "SQ.CM", "SQ-CM", "SQ-CENTIMETER", "SQ-CENTIMETERS", "CM²"]
    __factors__ = {"MM2": "{}*100", "CM2": "{}*1", "M2": "{}*0.0001", "FT2": "{}*1"}


class MillimeterSquare(Base_UnitType):
    """Millimeter Square"""

    __symbol__ = "MM2"
    __aliases__ = ["SQMM", "SQ.MM", "SQ-MM", "SQ-MILLIMETER", "SQ-MILLIMETERS", "MM²"]
    __factors__ = {"MM2": "{}*1", "CM2": "{}*0.01", "M2": "{}*0.000001", "FT2": "{}*1"}


class FootSquare(Base_UnitType):
    """Foot Square"""

    __symbol__ = "FT2"
    __aliases__ = [
        "SFT",
        "SF",
        "SQFT",
        "SQ.FT",
        "SQ-FT",
        "SQ-FOOT",
        "FT²",
    ]
    __factors__ = {"M2": "{}*0.09290304", "FT2": "{}*1"}


class FootSquarePerPerson(Base_UnitType):
    """Foot Square Per Person"""

    __symbol__ = "FT2/PERSON"
    __aliases__ = [
        "FT2-PERSON",
        "FT²/PERSON",
    ]
    __factors__ = {"M2/PERSON": "{}*0.09290304", "FT2/PERSON": "{}*1"}
