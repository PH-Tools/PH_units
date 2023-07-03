# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubedPerSecond(Base_UnitType):
    """M3/S"""

    __symbol__ = "M3/S"
    __aliases__ = ["M3/SECOND", "M3/SEC", "CM/S", "M³/S"]
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
    __aliases__ = ["M3/MIN", "M3/MINUTE", "CM/M", "M³/MIN"]
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
    __aliases__ = ["CM/H", "CMH", "M3/H", "M³/H", "M³/HR"]
    __factors__ = {
        "M3/S": "({}/60)/60",
        "M3/M": "{}/60",
        "M3/HR": "{}*1",
        "CFM": "{}*0.588577779",
        "CFH": "({}*60)*0.588577779",
    }


class MeterCubedPerHourPerMeterSquared(Base_UnitType):
    """M3/HR-M2"""

    __symbol__ = "M3/HRM2"
    __aliases__ = [
        "M3/HR-M2",
        "M3/HRM2",
        "M3/HR-M^2",
        "M3/HRM^2",
        "M³/M²H",
        "M3/M2H",
        "M3/M²H",
        "M³/M²H",
    ]
    __factors__ = {"M3/HRM2": "{}*1", "CFM/FT2": "{}*0.054680665"}


# -- IP


class FootCubedPerMinute(Base_UnitType):
    """CFM"""

    __symbol__ = "CFM"
    __aliases__ = ["FT3/M", "FT3M", "FT³/M", "FT³M", "CF/M"]
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


class FootCubedPerMinutePerFootSqaure(Base_UnitType):
    """CFM/FT2"""

    __symbol__ = "CFM/FT2"
    __aliases__ = ["CFM/SF", "CFM/FT²", "CFM/SQFT", "CFM/SQFT"]
    __factors__ = {"CFM/FT2": "{}*1", "M3/HRM2": "{}*18.288"}
