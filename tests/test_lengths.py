# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert
from ph_units.parser import parse_input


def test_meter():
    assert convert(1, "M", "M") == 1
    assert convert(1, "M", "METER") == 1
    assert convert(1, "M", "METERS") == 1
    assert convert(1, "METER", "M") == 1
    assert convert(1, "METERS", "M") == 1
    assert convert(1, "M", "CM") == 100
    assert convert(1, "M", "MM") == 1000
    assert convert(1, "M", "FT") == pytest.approx(3.280839895)
    assert convert(1, "M", "IN") == pytest.approx(39.37007874)
    assert convert(1, "M", "INCHES") == pytest.approx(39.37007874)


def test_centimeter():
    assert convert(1, "CM", "M") == 0.01
    assert convert(1, "CENTIMETER", "M") == 0.01
    assert convert(1, "CENTIMETERS", "M") == 0.01
    assert convert(1, "CM", "CM") == 1
    assert convert(1, "CM", "MM") == 10
    assert convert(1, "CM", "FT") == pytest.approx(0.0328)
    assert convert(1, "CM", "IN") == pytest.approx(0.3937)


def test_millimeter():
    assert convert(1, "MM", "M") == 0.001
    assert convert(1, "MILLIMETER", "M") == 0.001
    assert convert(1, "MILLIMETERS", "M") == 0.001
    assert convert(1, "MM", "CM") == 0.1
    assert convert(1, "MM", "MM") == 1
    assert convert(1, "MM", "FT") == pytest.approx(0.003280842)
    assert convert(1, "MM", "IN") == pytest.approx(0.039370100)


def test_inch():
    assert convert(1, "IN", "M") == 0.0254
    assert convert(1, "INCH", "M") == 0.0254
    assert convert(1, "INCHES", "M") == 0.0254
    assert convert(1, "IN", "CM") == 2.54
    assert convert(1, "IN", "MM") == 25.4
    assert convert(1, "IN", "FT") == (1 / 12)
    assert convert(1, "IN", "IN") == 1


def test_positive_inches_parsed_input():
    assert convert(*parse_input("3 IN"), "IN") == 3
    assert convert(*parse_input("3 IN"), "FT") == 0.25
    assert convert(*parse_input("4 IN"), "M") == 0.1016
    assert convert(*parse_input("4 IN"), "CM") == 10.16
    assert convert(*parse_input("4 IN"), "MM") == 101.6


def test_negative_inches_parsed_input():
    assert convert(*parse_input("-3 IN"), "IN") == -3
    assert convert(*parse_input("-3 IN"), "FT") == -0.25
    assert convert(*parse_input("-4 IN"), "M") == -0.1016
    assert convert(*parse_input("-4 IN"), "CM") == -10.16
    assert convert(*parse_input("-4 IN"), "MM") == -101.6


def test_foot():
    assert convert(1, "FT", "M") == 0.3048
    assert convert(1, "FOOT", "M") == 0.3048
    assert convert(1, "FEET", "M") == 0.3048
    assert convert(1, "FT", "CM") == 30.48
    assert convert(1, "FT", "MM") == 304.8
    assert convert(1, "FT", "FT") == 1
    assert convert(1, "FT", "IN") == 12


def test_positive_feet_parsed_input():
    assert convert(*parse_input("3 FT"), "FT") == 3
    assert convert(*parse_input("3 FT"), "IN") == 36
    assert convert(*parse_input("4 FT"), "M") == 1.2192
    assert convert(*parse_input("4 FT"), "CM") == 121.92
    assert convert(*parse_input("4 FT"), "MM") == 1219.2


def test_negative_feet_parsed_input():
    assert convert(*parse_input("-3 FT"), "FT") == -3
    assert convert(*parse_input("-3 FT"), "IN") == -36
    assert convert(*parse_input("-4 FT"), "M") == -1.2192
    assert convert(*parse_input("-4 FT"), "CM") == -121.92
    assert convert(*parse_input("-4 FT"), "MM") == -1219.2


def test_mil():
    assert convert(1, "MIL", "MIL") == 1.0
    assert convert(1, "MIL", "M") == 0.0000254
    assert convert(1, "MIL", "CM") == 0.00254
    assert convert(1, "MIL", "MM") == 0.0254
    assert convert(1, "MIL", "FT") == pytest.approx(0.0000833333)
    assert convert(1, "MIL", "IN") == pytest.approx(0.001)

    assert convert(convert(1, "MIL", "M"), "M", "MIL") == pytest.approx(1)
    assert convert(convert(1, "MIL", "CM"), "CM", "MIL") == pytest.approx(1)
    assert convert(convert(1, "MIL", "MM"), "MM", "MIL") == pytest.approx(1)
    assert convert(convert(1, "MIL", "FT"), "FT", "MIL") == pytest.approx(1)
    assert convert(convert(1, "MIL", "IN"), "IN", "MIL") == pytest.approx(1)
    assert convert(convert(1, "MIL", "MIL"), "MIL", "MIL") == pytest.approx(1)