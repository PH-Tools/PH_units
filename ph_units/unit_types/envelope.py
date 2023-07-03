# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class WattsPerMeterSquaredKelvin(Base_UnitType):
    """W/M2K (U-Value)"""

    __symbol__ = "W/M2K"
    __aliases__ = ["U-SI", "W/M²K"]
    __factors__ = {
        "W/M2K": "{}*1",
        "M2K/W": "(1/{})",
        "BTU/HR-FT2-F": "{}*0.176110159",
        "HR-FT2-F/BTU": "(1/{})*5.678264134",
    }


class BtuPerHourFootSquaredFahrenheit(Base_UnitType):
    """BTU/HR-FT2-F (U-Value)"""

    __symbol__ = "BTU/HR-FT2-F"
    __aliases__ = ["U-IP", "BTU/HR-SF-F", "BTU/H-SF-F", "BTU/HRFT²°F"]
    __factors__ = {
        "W/M2K": "{}*5.678264134",
        "M2K/W": "1/({}*5.678264134)",
        "BTU/HR-FT2-F": "{}*1",
        "HR-FT2-F/BTU": "(1/{})",
    }


class MeterSquaredKelvinPerWatt(Base_UnitType):
    """M2K/W (R-Value)"""

    __symbol__ = "M2K/W"
    __aliases__ = ["R-SI", "M²K/W"]
    __factors__ = {
        "M2K/W": "{}*1",
        "W/M2K": "(1/{})",
        "HR-FT2-F/BTU": "{}*5.678264134",
        "BTU/HR-FT2-F": "1/({}*5.678264134)",
    }


class HourFootSquaredFahrenheitPerBtu(Base_UnitType):
    """HR-FT2-F/BTU (R-Value)"""

    __symbol__ = "HR-FT2-F/BTU"
    __aliases__ = ["R-IP", "H-SF-F/BTU", "HR-SF-F/BTU"]
    __factors__ = {
        "M2K/W": "1/((1/{})*5.678264134)",
        "W/M2K": "(1/{})*5.678264134",
        "HR-FT2-F/BTU": "{}*1",
        "BTU/HR-FT2-F": "(1/{})",
    }


class HourFootSquaredFahrenheitPerBtuInch(Base_UnitType):
    """HR-FT2-F/BTU-IN (R-per-inch)"""

    __symbol__ = "HR-FT2-F/BTU-IN"
    __aliases__ = ["R/IN", "R-IN", "H-SF-F/BTU-IN"]
    __factors__ = {
        "W/MK": "(1/({}*12))*1.730734908",
        "BTU/HR-FT-F": "1/({}*12)",
    }


class WattsPerMeterKelvin(Base_UnitType):
    """W/MK (Psi-Value)"""

    __symbol__ = "W/MK"
    __aliases__ = []
    __factors__ = {
        "W/MK": "{}*1",
        "HR-FT2-F/BTU-IN": "{}**-1*0.144227909",
        "BTU/HR-FT-F": "{}*0.577789236",
    }


class BtuPerHourFootFahrenheit(Base_UnitType):
    """BTU/HR-FT-F (Psi-Value)"""

    __symbol__ = "BTU/HR-FT-F"
    __aliases__ = ["BTU/HRFT°F"]
    __factors__ = {
        "W/MK": "{}*1.730734908",
        "HR-FT2-F/BTU-IN": "1/({}*12)",
        "BTU/HR-FT-F": "{}*1",
    }


class WattsPerKelvin(Base_UnitType):
    """W/K (Chi-Value)"""

    __symbol__ = "W/K"
    __aliases__ = []
    __factors__ = {"W/K": "{}*1", "BTU/HR-F": "{}*1.895633976"}


class BtuPerHourFahrenheit(Base_UnitType):
    """BTU/HR-F (Chi-Value)"""

    __symbol__ = "BTU/HR-F"
    __aliases__ = ["BTU/HRF", "BTU/HR-F", "BTU/HR-F", "BTU/HR°F", "BTU/HR-°F"]
    __factors__ = {"W/K": "{}*0.527528", "BTU/HR-F": "{}*1"}
