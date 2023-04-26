# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubedPerSecond(Base_UnitType):
    """M3/S"""

    __symbol__ = "M3/S"
    __aliases__ = ["M3/SECOND", "M3/SEC", "CM/S"]
    __factors__ = {
        "M3/S": "{}*1",
        "M3/M": "{}*60",
        "M3/HR": "{}*60*60",
        "CFM": "({}*60*60)*0.588577779",
        "CFH": "({}*60*60*60)*0.588577779",
    }


class MeterCubedPerMinute(Base_UnitType):
    """M3/M"""

    __symbol__ = "M3/M"
    __aliases__ = ["M3/MIN", "M3/MINUTE", "CM/M"]
    __factors__ = {
        "M3/S": "{}/60",
        "M3/M": "{}*1",
        "M3/HR": "{}*60",
        "CFM": "({}*60)*0.588577779",
        "CFH": "({}*60*60)*0.588577779",
    }


class MeterCubedPerHour(Base_UnitType):
    """M3/HR"""

    __symbol__ = "M3/HR"
    __aliases__ = ["CM/H", "CMH", "M3/H"]
    __factors__ = {
        "M3/S": "({}/60)/60",
        "M3/M": "{}/60",
        "M3/HR": "{}*1",
        "CFM": "{}*0.588577779",
        "CFH": "({}*60)*0.588577779",
    }


# -- IP


class FootCubedPerMinute(Base_UnitType):
    """CFM"""

    __symbol__ = "CFM"
    __aliases__ = ["FT3/M", "FT3M"]
    __factors__ = {
        "M3/S": "(({}*1.699010796)/60)/60",
        "M3/M": "({}*1.699010796)/60",
        "M3/HR": "{}*1.699010796",
        "CFM": "{}*1",
        "CFH": "{}*60",
    }


class FootCubedPerHour(Base_UnitType):
    """CFH"""

    __symbol__ = "CFH"
    __aliases__ = ["FT3/H", "FT3/HR", "FT3H", "CF/HR"]
    __factors__ = {
        "M3/S": "(({}/60)*1.699010796)/60/60",
        "M3/M": "(({}/60)*1.699010796)/60",
        "M3/HR": "(({}/60)*1.699010796)",
        "CFM": "{}/60",
        "CFH": "{}*1",
    }
