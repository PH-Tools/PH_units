# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class WattHoursPerMeterCubed(Base_UnitType):
    """WH/M3"""

    __symbol__ = "WH/M3"
    __aliases__ = []
    __factors__ = {"WH/M3": "{}*1", "W/CFM": "{}*1.699010796"}


class WattHoursPerKilometerSquared(Base_UnitType):
    """WH/KM2"""

    __symbol__ = "WH/KM2"
    __aliases__ = []
    __factors__ = {"WH/KM2": "{}*1", "BTU/FT2": "{}*0.000000317"}


class WattHoursPerMeterSquared(Base_UnitType):
    """WH/M2"""

    __symbol__ = "WH/M2"
    __aliases__ = []
    __factors__ = {
        "WH/M2": "{}*1",
        "WH/FT2": "{}*0.092903",
        "KWH/M2": "{}*0.001",
        "KWH/FT2": "{}*0.000092903",
        "BTU/FT2": "{}*0.316998",
        "KBTU/FT2": "{}*0.000316998",
    }


class WattHoursPerFootSquared(Base_UnitType):
    """WH/FT2"""

    __symbol__ = "WH/FT2"
    __aliases__ = []
    __factors__ = {
        "WH/M2": "{}*10.7639",
        "WH/FT2": "{}*1",
        "KWH/M2": "{}*0.0107639",
        "KWH/FT2": "{}*0.001",
        "BTU/FT2": "{}*3.413",
        "KBTU/FT2": "{}*0.003413",
    }


class KiloWattHoursPerFootSquared(Base_UnitType):
    """KWH/FT2"""

    __symbol__ = "KWH/FT2"
    __aliases__ = ["KWH/SF"]
    __factors__ = {
        "WH/M2": "{}*10763.9",
        "WH/FT2": "{}*1000",
        "KWH/M2": "{}*10.7639",
        "KWH/FT2": "{}*1",
        "BTU/FT2": "{}*3413",
        "KBTU/FT2": "{}*3.413",
    }


class KilowattHoursPerMeterSquared(Base_UnitType):
    """KWH/M2"""

    __symbol__ = "KWH/M2"
    __aliases__ = []
    __factors__ = {
        "WH/M2": "{}*1000",
        "WH/FT2": "{}*92.903",
        "KWH/M2": "{}*1",
        "KWH/FT2": "{}*0.092903040",
        "BTU/FT2": "{}*316.998",
        "KBTU/FT2": "{}*0.316998286",
    }


class KBtuPerFootSquared(Base_UnitType):
    """KBTU/FT2"""

    __symbol__ = "KBTU/FT2"
    __aliases__ = ["KBTU/SF"]
    __factors__ = {
        "WH/M2": "{}*3154.59",
        "WH/FT2": "{}*293.071",
        "KWH/M2": "{}*3.15459",
        "KWH/FT2": "{}*0.293071",
        "BTU/FT2": "{}*1000",
        "KBTU/FT2": "{}*1",
    }


class BtuPerFootSquared(Base_UnitType):
    """BTU/FT2"""

    __symbol__ = "BTU/FT2"
    __aliases__ = ["BTU/SF"]
    __factors__ = {
        "WH/M2": "{}*3.15459",
        "WH/FT2": "{}*0.293071",
        "KWH/M2": "{}*0.00315459",
        "KWH/FT2": "{}*0.000293071",
        "BTU/FT2": "{}*1",
        "KBTU/FT2": "{}*0.001",
    }


class MegaJoulePerMeterCubedKelvin(Base_UnitType):
    """MJ/M3K"""

    __symbol__ = "MJ/M3K"
    __aliases__ = []
    __factors__ = {"MJ/M3K": "{}*1", "BTU/FT3-F": "{}*14.91066014"}
