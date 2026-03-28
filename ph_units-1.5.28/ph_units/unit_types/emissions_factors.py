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


# --- CO2 per Area ------------------------------------------------------------
class MetricTonsPerMeterSquared(Base_UnitType):
    """MT/M2"""

    __symbol__ = "MT/M2"
    __aliases__ = ["MT/M²", "METRIC-TON/M2", "METRIC-TONS/M2"]
    __factors__ = {
        "MT/M2": "{}*1",
        "KG/M2": "{}*1000",
        "G/M2": "{}*1000000",
    }


class KilogramsPerMeterSquared(Base_UnitType):
    """KG/M2"""

    __symbol__ = "KG/M2"
    __aliases__ = ["KG/M²"]
    __factors__ = {
        "MT/M2": "{}*0.001",
        "KG/M2": "{}*1",
        "G/M2": "{}*1000",
    }


class GramsPerMeterSquared(Base_UnitType):
    """G/M2"""

    __symbol__ = "G/M2"
    __aliases__ = ["G/M²"]
    __factors__ = {
        "MT/M2": "{}*0.000001",
        "KG/M2": "{}*0.001",
        "G/M2": "{}*1",
    }
