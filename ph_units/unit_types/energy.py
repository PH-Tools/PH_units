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
    __aliases__ = ["KWH/YR", "KWH/A", "KWH/M", "KWH/MONTH"]
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
    __aliases__ = ["KWH/M²MONTH", "KWH/M²A", "KWH/M²"]
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
    __aliases__ = ["KBTU/SF", "KBTU/FT²MONTH", "KBTU/FT²YR", "KBTU/FT²A", "KBTU/FT²"]
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
    __aliases__ = ["BTU/SF", "BTU/FT²"]
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
    __aliases__ = ["WH/M³"]
    __factors__ = {"WH/M3": "{}*1", "W/CFM": "{}*1.699010796"}


class MegaJoulePerMeterCubedKelvin(Base_UnitType):
    """MJ/M3K"""

    __symbol__ = "MJ/M3K"
    __aliases__ = []
    __factors__ = {"MJ/M3K": "{}*1", "BTU/FT3F": "{}*14.91066014"}


class BtuPerFootCubedDegreeFarenheirt(Base_UnitType):
    """BTU/FT3F"""

    __symbol__ = "BTU/FT3F"
    __aliases__ = ["BTU/FT3°F"]
    __factors__ = {"MJ/M3K": "{}*0.067066112", "BTU/FT3F": "{}*1"}


# ----------------- Energy Per Mass -----------------


class JoulePerKilogramDegreeKelvin(Base_UnitType):
    """J/KG-K"""

    __symbol__ = "J/KGK"
    __aliases__ = ["J/KG-K"]
    __factors__ = {"J/KGK": "{}*1", "BTU/LBF": "{}*0.000238846"}


class BtuPerPoundDegreeFarenheirt(Base_UnitType):
    """BTU/LB-F"""

    __symbol__ = "BTU/LBF"
    __aliases__ = ["BTU/LB-F", "BTU/LB°F"]
    __factors__ = {"J/KGK": "{}*4186.800585", "BTU/LBF": "{}*1"}


class WattHoursPerFootSquaredDegreeFarenheirt(Base_UnitType):
    """WH/FT2F"""

    __symbol__ = "WH/FT2F"
    __aliases__ = ["WH/FT2-F", "WH/FT2°F", "WH/FT²F"]
    __factors__ = {
        "WH/M2K": "{}*19.37503875",
        "WH/FT2F": "{}*1",
        "BTU/FT2F": "{}*3.412141156",
    }


class WattHoursPerMeterSqauredPerDegreeKelvin(Base_UnitType):
    """WH/M2K"""

    __symbol__ = "WH/M2K"
    __aliases__ = ["WH/M2K", "WH/M²K"]
    __factors__ = {
        "WH/M2K": "{}*1",
        "WH/FT2F": "{}*0.0516128",
        "BTU/FT2F": "{}*0.1761102",
    }


class BtuPerSquareFootDegreeFarenheirt(Base_UnitType):
    """BTU/FT2-F"""

    __symbol__ = "BTU/FT2F"
    __aliases__ = ["BTU/FT2-F", "BTU/FT2°F", "BTU/FT²F"]
    __factors__ = {
        "BTU/FT2F": "{}*1",
        "WH/FT2F": "{}*0.293071111",
        "WH/M2K": "{}*5.678264134",
    }


# ----------------- Primary Energy Factors -----------------


class KiloWattHourPerKiloWattHour(Base_UnitType):
    """KWH/KWH"""

    __symbol__ = "KWH/KWH"
    __aliases__ = ["KWH/KWH"]
    __factors__ = {"KWH/KWH": "{}*1", "BTU/BTU": "{}*3412.14"}


class BtuPerBtu(Base_UnitType):
    """BTU/BTU"""

    __symbol__ = "BTU/BTU"
    __aliases__ = ["BTU/BTU"]
    __factors__ = {"KWH/KWH": "{}*0.000293071", "BTU/BTU": "{}*1"}
