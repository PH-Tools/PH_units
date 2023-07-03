# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterSquare(Base_UnitType):
    """Meter Square"""

    __symbol__ = "M2"
    __aliases__ = ["SM", "SQM", "SQ.M", "SQ-M", "SQ-METER", "SQ-METERS", "M²"]
    __factors__ = {"M2": "{}*1", "FT2": "{}*10.76391042"}


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
