# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class Kilowatts(Base_UnitType):
    """KW"""

    __symbol__ = "KW"
    __aliases__ = []
    __factors__ = {
        "KW": "{}*1",
        "W": "{}*1000",
        "BTUH": "{}*3412.141156",
        "KBTUH": "{}*3.412141156",
    }


class Watts(Base_UnitType):
    """W"""

    __symbol__ = "W"
    __aliases__ = ["WATT", "WATTS"]
    __factors__ = {
        "W": "{}*1",
        "KW": "{}*0.001",
        "BTUH": "{}*3.412141156",
        "KBTUH": "{}*0.003412141",
    }


class WattsPerMeterSquared(Base_UnitType):
    """W/M2"""

    __symbol__ = "W/M2"
    __aliases__ = ["W/M²"]
    __factors__ = {
        "W/M2": "{}*1",
        "BTU/HR-FT2": "{}*0.316998286",
        "W/FT2": "{}*0.09290304",
    }


class WattsPerWatt(Base_UnitType):
    """W/W (SEER)"""

    __symbol__ = "W/W"
    __aliases__ = []
    __factors__ = {"W/W": "{}*1", "BTUHR/W": "{}*3.412141156"}


class WattsPerFootSquared(Base_UnitType):
    """W/FT2"""

    __symbol__ = "W/FT2"
    __aliases__ = ["W/SF", "W/FT²"]
    __factors__ = {
        "W/FT2": "{}*1",
        "W/M2": "{}*10.76391042",
        "BTU/HR-FT2": "{}*3.154591186",
    }


class WattsPerFootCubedPerMinute(Base_UnitType):
    """W/CFM"""

    __symbol__ = "W/CFM"
    __aliases__ = []
    __factors__ = {"W/CFM": "{}*0.588577779", "WH/M3": "{}*0.588577779"}


class BtuPerHourFootSquared(Base_UnitType):
    """BTU/HR-FT2"""

    __symbol__ = "BTU/HR-FT2"
    __aliases__ = ["BTUH/FT2", "BTU/H-SF", "BTU/H-FT2", "BTU/HRFT²"]
    __factors__ = {
        "BTU/HR-FT2": "{}*1",
        "W/M2": "{}*3.154591186",
        "W/FT2": "{}*0.293071111",
    }


class BtuPerHour(Base_UnitType):
    """BTU/H"""

    __symbol__ = "BTUH"
    __aliases__ = ["BTU/HR", "BTU/H", "BTUHR"]
    __factors__ = {
        "BTUH": "{}*1",
        "KBTUH": "{}/1000",
        "W": "{}*0.293071111",
        "KW": "{}*0.000293071",
    }


class KiloBtuPerHour(Base_UnitType):
    """KBTU/H"""

    __symbol__ = "KBTUH"
    __aliases__ = ["KBTU/HR", "KBTU/H", "KBTUHR"]
    __factors__ = {
        "KBTUH": "{}*1",
        "BTUH": "{}*1000",
        "W": "{}*293.0711111",
        "KW": "{}*0.293071111",
    }
