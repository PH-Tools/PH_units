# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class MeterCubedPerHour(Base_UnitType):
    """M3/HR"""

    __symbol__ = "M3/HR"
    __aliases__ = ["FT3/H", "FT3H"]
    __factors__ = {"SI": "{}*1", "M3/HR": "{}*1", "CFM": "{}*0.588577779"}


class FootCubedPerMinute(Base_UnitType):
    """CFM"""

    __symbol__ = "CFM"
    __aliases__ = ["FT3/M", "FT3M"]
    __factors__ = {"SI": "{}*1.699010796", "M3/HR": "{}*1.699010796", "CFM": "{}*1"}
