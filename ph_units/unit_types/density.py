# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MilligramsPerMeterCubed(Base_UnitType):
    """MG/M3 (Density)"""

    __symbol__ = "MG/M3"
    __aliases__ = ["MG/M³"]
    __factors__ = {
        "MG/M3": "{}*1",
        "G/M3": "{}*0.001",
        "KG/M3": "{}*0.000001",
        "LB/FT3": "{}*0.0000000624279606",
    }


class GramsPerMeterCubed(Base_UnitType):
    """G/M3 (Density)"""

    __symbol__ = "G/M3"
    __aliases__ = ["G/M³"]
    __factors__ = {
        "MG/M3": "{}*1000",
        "G/M3": "{}*1",
        "KG/M3": "{}*0.001",
        "LB/FT3": "{}*0.0000624279606",
    }


class KiloGramsPerMeterCubed(Base_UnitType):
    """KG/M3 (Density)"""

    __symbol__ = "KG/M3"
    __aliases__ = ["KG/M³"]
    __factors__ = {
        "MG/M3": "{}*1000000",
        "G/M3": "{}*1000",
        "KG/M3": "{}*1",
        "LB/FT3": "{}*0.0624279606",
    }


class PoundPerFootCubed(Base_UnitType):
    """LB/FT3 (Density)"""

    __symbol__ = "LB/FT3"
    __aliases__ = ["LB/FT³", "LB/CF"]
    __factors__ = {
        "MG/M3": "{}*16018463.4",
        "G/M3": "{}*16018.4634",
        "KG/M3": "{}*16.0184634",
        "LB/FT3": "{}*1",
    }
