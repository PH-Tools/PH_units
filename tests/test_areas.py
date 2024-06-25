# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_meter_squared():
    assert convert(1, "M2", "M2") == 1
    assert convert(1, "M²", "M2") == 1
    assert convert(1, "M2", "CM2") == 10_000
    assert convert(1, "M2", "MM2") == 1_000_000
    assert convert(00.0553, "M2", "MM2") == 55_300
    assert convert(1, "M2", "FT2") == pytest.approx(10.76391042)


def test_centimeter_squared():
    assert convert(1, "CM2", "CM2") == 1
    assert convert(1, "CM²", "CM2") == 1
    assert convert(1, "CM2", "M2") == 0.0001
    assert convert(1, "CM2", "MM2") == 100


def test_millimeter_squared():
    assert convert(1, "MM2", "MM2") == 1
    assert convert(1, "MM²", "MM2") == 1
    assert convert(1, "MM2", "M2") == 0.000001
    assert convert(34_565_678, "MM2", "M2") == 34.565678
    assert convert(1, "MM2", "CM2") == 0.01


def test_foot_squared():
    assert convert(1, "FT2", "M2") == pytest.approx(0.09290304)
    assert convert(1, "FT²", "M2") == pytest.approx(0.09290304)
    assert convert(1, "FT2", "FT2") == 1
