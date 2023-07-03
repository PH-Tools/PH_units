# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class GramsPerKiloWattHour(Base_UnitType):
    """G/KWH"""

    __symbol__ = "G/KWH"
    __aliases__ = []
    __factors__ = {
        "G/KWH": "{}*1",
        "G/BTU": "{}*0.000293071",
        "G/KBTU": "{}*0.293071",
    }


class GramsPerBtu(Base_UnitType):
    """G/BTU"""

    __symbol__ = "G/BTU"
    __aliases__ = []
    __factors__ = {
        "G/BTU": "{}*1",
        "G/KBTU": "{}*1000",
        "G/KWH": "{}*3412.14",
    }


class GramsPerKiloBtu(Base_UnitType):
    """G/KBTU"""

    __symbol__ = "G/KBTU"
    __aliases__ = []
    __factors__ = {
        "G/BTU": "{}*0.001",
        "G/KBTU": "{}*1",
        "G/KWH": "{}*3.4121416",
    }
