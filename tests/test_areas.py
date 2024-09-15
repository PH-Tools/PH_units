# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert
from ph_units.unit_type import Unit


def test_meter_squared():
    assert convert(1, "M2", "M2") == 1
    assert convert(1, "M²", "M2") == 1
    assert convert(1, "M2", "CM2") == 10_000
    assert convert(1, "M2", "MM2") == 1_000_000
    assert convert(00.0553, "M2", "MM2") == 55_300
    assert convert(1, "M2", "FT2") == pytest.approx(10.76391042)
    assert convert(1, "M2", "IN2") == pytest.approx(1550.0031)


def test_centimeter_squared():
    assert convert(1, "CM2", "CM2") == 1
    assert convert(1, "CM²", "CM2") == 1
    assert convert(1, "CM2", "M2") == 0.0001
    assert convert(1, "CM2", "MM2") == 100
    assert convert(1, "CM2", "FT2") == pytest.approx(0.001076391042)
    assert convert(1, "CM2", "IN2") == pytest.approx(0.15500031)


def test_millimeter_squared():
    assert convert(1, "MM2", "MM2") == 1
    assert convert(1, "MM²", "MM2") == 1
    assert convert(1, "MM2", "M2") == 0.000001
    assert convert(34_565_678, "MM2", "M2") == 34.565678
    assert convert(1, "MM2", "CM2") == 0.01
    assert convert(1, "MM2", "FT2") == pytest.approx(0.000010764)
    assert convert(1, "MM2", "IN2") == pytest.approx(0.0015500031)


def test_foot_squared():
    assert convert(1, "FT2", "IN2") == pytest.approx(144)
    assert convert(1, "FT2", "FT2") == 1
    assert convert(1, "FT2", "MM2") == pytest.approx(92903.04)
    assert convert(1, "FT2", "CM2") == pytest.approx(929.0304)
    assert convert(1, "FT2", "M2") == pytest.approx(0.09290304)


def test_inch_squared():
    assert convert(1, "IN2", "IN2") == 1
    assert convert(1, "IN2", "FT2") == pytest.approx(0.00694444)
    assert convert(1, "IN2", "MM2") == pytest.approx(645.16)
    assert convert(1, "IN2", "CM2") == pytest.approx(6.4516)
    assert convert(1, "IN2", "M2") == pytest.approx(0.00064516)


# --- Concentrations ----------------------------------------------------------


def test_cost_per_meter_squared():
    assert convert(1, "COST/M2", "COST/M2") == 1
    assert convert(1, "COST/M2", "COST/FT2") == pytest.approx(0.09290304)
    assert Unit(1, "COST/M2").as_a("COST/FT2") == pytest.approx(0.09290304)


def test_cost_per_foot_squared():
    assert convert(1, "COST/FT2", "COST/M2") == pytest.approx(10.76391042)
    assert convert(1, "COST/FT2", "COST/FT2") == 1
    assert Unit(1, "COST/FT2").as_a("COST/M2") == pytest.approx(10.76391042)
