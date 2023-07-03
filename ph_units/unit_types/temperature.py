# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-
#
from ph_units.unit_types._base import Base_UnitType


class Celsius(Base_UnitType):
    "Celsius"

    __symbol__ = "C"
    __aliases__ = ["DEGC", "DEG.C", "°C"]
    __factors__ = {"C": "{}*1", "F": "{}*1.8+32"}


class DeltaCelsius(Base_UnitType):
    "Delta-Celsius"

    __symbol__ = "DELTA-C"
    __aliases__ = []
    __factors__ = {"DELTA-C": "{}*1", "DELTA-K": "{}*1", "DELTA-F": "{}*1.8"}


class DeltaKelvin(Base_UnitType):
    "Delta-Kelvin"

    __symbol__ = "DELTA-K"
    __aliases__ = []
    __factors__ = {"DELTA-K": "{}*1", "DELTA-C": "{}*1", "DELTA-F": "{}*1.8"}


class Fahrenheit(Base_UnitType):
    "Fahrenheit"

    __symbol__ = "F"
    __aliases__ = ["DEGF", "DEG.F", "°F"]
    __factors__ = {"C": "({}-32)/1.8"}


class DeltaFahrenheit(Base_UnitType):
    "Delta-Fahrenheit"

    __symbol__ = "DELTA-F"
    __aliases__ = []
    __factors__ = {
        "DELTA-C": "{}*0.555555556",
        "DELTA-K": "{}*0.555555556",
        "DELTA-F": "{}*1",
    }
