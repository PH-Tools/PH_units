# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class WattHour(Base_UnitType):
    """Wh"""

    __symbol__ = "WH"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*1",
        "KWH": "{}*0.001",
        "BTU": "{}*3.41214",
        "KBTU": "{}*0.00341214",
        "MJ": "{}*0.0036",
        "KJ": "{}*3.6",
    }


class KiloWattHour(Base_UnitType):
    """KWH"""

    __symbol__ = "KWH"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*1000",
        "KWH": "{}*1",
        "BTU": "{}*3412.14",
        "KBTU": "{}*3.41214",
        "MJ": "{}*3.6",
        "KJ": "{}*3600",
    }


class BTU(Base_UnitType):
    """BTU"""

    __symbol__ = "BTU"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*0.293071",
        "KWH": "{}*0.000293071",
        "BTU": "{}*1",
        "KBTU": "{}*0.001",
        "MJ": "{}*0.00105506",
        "KJ": "{}*1.05506",
    }


class KiloBTU(Base_UnitType):
    """KBTU"""

    __symbol__ = "KBTU"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*293.071",
        "KWH": "{}*0.293071",
        "BTU": "{}*1000",
        "KBTU": "{}*1",
        "MJ": "{}*1.05506",
        "KJ": "{}*1055.06",
    }


class MegaJoule(Base_UnitType):
    """MJ"""

    __symbol__ = "MJ"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*277.778",
        "KWH": "{}*0.277778",
        "BTU": "{}*947.817",
        "KBTU": "{}*0.947817",
        "MJ": "{}*1",
        "KJ": "{}*1000",
    }


class KiloJoule(Base_UnitType):
    """KJ"""

    __symbol__ = "KJ"
    __aliases__ = []
    __factors__ = {
        "WH": "{}*0.277778",
        "KWH": "{}*0.000277778",
        "BTU": "{}*0.947817",
        "KBTU": "{}*0.000947817",
        "MJ": "{}*0.001",
        "KJ": "{}*1",
    }


# ----------------- Energy Per Area -----------------


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


# ----------------- Energy Per Volume -----------------


class WattHoursPerMeterCubed(Base_UnitType):
    """WH/M3"""

    __symbol__ = "WH/M3"
    __aliases__ = []
    __factors__ = {"WH/M3": "{}*1", "W/CFM": "{}*1.699010796"}


class MegaJoulePerMeterCubedKelvin(Base_UnitType):
    """MJ/M3K"""

    __symbol__ = "MJ/M3K"
    __aliases__ = []
    __factors__ = {"MJ/M3K": "{}*1", "BTU/FT3-F": "{}*14.91066014"}
