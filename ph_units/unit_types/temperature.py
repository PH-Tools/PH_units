# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-
#
from ph_units.unit_types._base import Base_UnitType


class Celsius(Base_UnitType):
    "Celsius"

    __symbol__ = "C"
    __aliases__ = ["DEG C", "DEG. C", "°C"]
    __factors__ = {"SI": "{}*1", "C": "{}*1", "F": "{}*1.8+32"}


class DeltaCelsius(Base_UnitType):
    "Delta-Celsius"

    __symbol__ = "DELTA-C"
    __aliases__ = []
    __factors__ = {"SI": "{}*1", "DELTA-C": "{}*1", "DELTA-F": "{}*1.8"}


class Fahrenheit(Base_UnitType):
    "Fahrenheit"

    __symbol__ = "F"
    __aliases__ = ["DEG F", "DEG. F", "°F"]
    __factors__ = {"SI": "({}-32)/1.8", "C": "({}-32)/1.8"}


class DeltaFahrenheit(Base_UnitType):
    "Delta-Fahrenheit"

    __symbol__ = "DELTA-F"
    __aliases__ = []
    __factors__ = {
        "SI": "{}*0.555555556",
        "DELTA-C": "{}*0.555555556",
        "DELTA-F": "{}*1",
    }
