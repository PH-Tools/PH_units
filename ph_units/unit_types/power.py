# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class Kilowatts(Base_UnitType):
    """KW"""

    __symbol__ = "KW"
    __aliases__ = []
    __factors__ = {
        "SI": "{}*1",
        "KW": "{}*1",
        "W": "{}*1000",
        "BTU/HR": "{}*3412.141156",
        "KBTU/HR": "{}*3.412141156",
    }


class Watts(Base_UnitType):
    """W"""

    __symbol__ = "W"
    __aliases__ = []
    __factors__ = {
        "SI": "{}*1",
        "KW": "{}*1",
        "BTU/HR": "{}*3.412141156",
        "KBTU/HR": "{}*0.003412141",
    }


class WattsPerMeterSquared(Base_UnitType):
    """W/M2"""

    __symbol__ = "W/M2"
    __aliases__ = []
    __factors__ = {
        "SI": "{}*1",
        "W/M2": "{}*1",
        "BTU/HR-FT2": "{}*0.316998286",
        "W/FT2": "{}*0.09290304",
    }


class WattsPerWatt(Base_UnitType):
    """W/W (SEER)"""

    __symbol__ = "W/W"
    __aliases__ = []
    __factors__ = {"SI": "{}*1", "W/W": "{}*1", "BTUHR/W": "{}*3.412141156"}


class WattsPerFootSquared(Base_UnitType):
    """W/FT2"""

    __symbol__ = "W/FT2"
    __aliases__ = []
    __factors__ = {
        "SI": "{}*10.76391042",
        "W/M2": "{}*10.76391042",
        "BTU/HR-FT2": "{}/3.412141156",
    }


class WattsPerFootCubedPerMinute(Base_UnitType):
    """W/CFM"""

    __symbol__ = "W/CFM"
    __aliases__ = []
    __factors__ = {"SI": "{}*0.588577779", "WH/M3": "{}*0.588577779"}


class BtuPerHourFootSquared(Base_UnitType):
    """BTU/HR-FT2"""

    __symbol__ = "BTU/HR-FT2"
    __aliases__ = ["BTUH/FT2", "BTU/H-SF", "BTU/H-FT2"]
    __factors__ = {
        "SI": "{}*3.154591186",
        "W/M2": "{}*3.154591186",
        "W/FT2": "{}*0.293071111",
    }


class BtuPerHour(Base_UnitType):
    """BTU/H"""

    __symbol__ = "BTUH"
    __aliases__ = ["BTU/HR", "BTU/H", "BTUHR"]
    __factors__ = {
        "SI": "{}*0.293071111",
        "KBTUH": "{}/1000",
        "W": "{}*0.293071111",
        "KW": "{}*0.000293071",
    }


class KiloBtuPerHour(Base_UnitType):
    """KBTU/H"""

    __symbol__ = "KBTUH"
    __aliases__ = ["KBTU/HR", "KBTU/H", "KBTUHR"]
    __factors__ = {
        "SI": "{}*0.293071111",
        "BTUH": "{}*1000",
        "W": "{}*293.0711111",
        "KW": "{}*0.293071111",
    }
