# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterPerDay(Base_UnitType):
    """Meter/Day"""

    __symbol__ = "M/DAY"
    __aliases__ = ["M/D", "METER/DAY", "METER/D", "M/DAY"]
    __factors__ = {
        "M/DAY": "{}*1",
        "FT/DAY": "{}*3.280839895",
        "M/S": "{}/24/60/60",
    }


class MeterPerSecond(Base_UnitType):
    """Meter/Second"""

    __symbol__ = "M/S"
    __aliases__ = ["METER/SEC", "METER/SECOND", "M/SECOND"]
    __factors__ = {
        "M/S": "{}*1",
        "M/DAY": "{}*24*60*60",
        "FT/S": "{}*3.280839895",
        "FT/DAY": "{}*3.280839895 * 24 * 60 * 60",
        "MPH": "{}/0.44704",
    }


class MilesPerHour(Base_UnitType):
    """MPH"""

    __symbol__ = "MPH"
    __aliases__ = []
    __factors__ = {
        "M/S": "{}*0.44704",
        "M/DAY": "{}*0.44704*60*60*24",
        "FT/S": "{}*1.466666667",
        "FT/DAY": "{}*1.466666667*60*60*24",
    }


class FeetPerSecond(Base_UnitType):
    """FT/Second"""

    __symbol__ = "FT/S"
    __aliases__ = []
    __factors__ = {"M/S": "{}*0.3048", "M/DAY": "{}*0.3048*60*60*24"}


class FeetPerDay(Base_UnitType):
    """FT/Day"""

    __symbol__ = "FT/DAY"
    __aliases__ = ["FT/D"]
    __factors__ = {
        "FT/DAY": "{}*1",
        "FT/S": "{}*1/24/60/60",
        "M/DAY": "{}*0.3048",
        "M/S": "{}*0.3048/24/60/60",
    }
