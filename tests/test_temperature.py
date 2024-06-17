# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert, unit_type_dict


def test_Celsius_to_Fahrenheit() -> None:
    assert convert(0, "C", "C") == 0
    assert convert(0, "C", "F") == 32
    assert convert(100, "°C", "F") == 212
    assert convert(112, "DEG C", "F") == 233.6


def test_delta_Celsius_to_delta_Farenheit():
    assert convert(0, "DELTA-C", "DELTA-F") == 0
    assert convert(10, "DELTA-C", "DELTA-K") == 10
    assert convert(10, "DELTA-C", "DELTA-F") == 18


def test_delta_Farenheit_to_delta_Celsius():
    assert convert(1, "DELTA-F", "DELTA-C") == 0.555555556
    assert convert(2, "DELTA-F", "DELTA-K") == 1.111111112
    assert convert(3, "DELTA-F", "DELTA-C") == 1.666666668


def test_delta_Farnheit_to_delta_Kelvin():
    assert convert(1, "DELTA-F", "DELTA-K") == 0.555555556
    assert convert(2, "DELTA-F", "DELTA-K") == 1.111111112
    assert convert(3, "DELTA-F", "DELTA-K") == 1.666666668


# --
def test_Farenheit_to_Celsius():
    assert convert(0, "F", "C") == -17.77777777777778
    assert convert(32, "F", "C") == 0
    assert convert(212, "F", "C") == 100
    assert convert(233.6, "F", "C") == 112

    assert convert(0, "°F", "C") == -17.77777777777778
    assert convert(32, "DEG.F", "C") == 0
    assert convert(212, "DEGF", "C") == 100
