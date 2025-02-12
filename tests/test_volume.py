# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_meter_cubed():
    assert convert(1, "M3", "M3") == 1
    assert convert(1, "M³", "M3") == 1
    assert convert(1, "M3", "FT3") == pytest.approx(35.31466672148859)
    assert convert(1, "M3", "IN3") == pytest.approx(61023.74409473229)
    assert convert(1, "M3", "L") == 1000
    assert convert(1, "M3", "GA") == pytest.approx(264.1720523581484)


def test_liters():
    assert convert(1, "L", "M3") == pytest.approx(0.001)
    assert convert(1, "L", "FT3") == pytest.approx(0.03531466672148859)
    assert convert(1, "L", "IN3") == pytest.approx(61.02374409473229)
    assert convert(1, "L", "L") == 1
    assert convert(1, "L", "GA") == pytest.approx(0.2641720523581484)


def test_gallon():
    assert convert(1, "GA", "M3") == pytest.approx(0.003785411784)
    assert convert(1, "GA", "FT3") == pytest.approx(0.13368055555555556)
    assert convert(1, "GA", "IN3") == pytest.approx(231)
    assert convert(1, "GA", "L") == pytest.approx(3.785411784)
    assert convert(1, "GA", "GA") == 1



def test_foot_cubed():
    assert convert(1, "FT3", "M3") == pytest.approx(0.028316847)
    assert convert(1, "FT3", "FT3") == 1
    assert convert(1, "FT3", "IN3") == pytest.approx(1728)
    assert convert(1, "FT3", "L") == pytest.approx(28.316846592)
    assert convert(1, "FT3", "GA") == pytest.approx(7.48051948051948)

def test_inch_cubed():
    assert convert(1, "IN3", "M3") == pytest.approx(0.000016387064)
    assert convert(1, "IN3", "FT3") == pytest.approx(0.0005787037037037037)
    assert convert(1, "IN3", "IN3") == 1
    assert convert(1, "IN3", "L") == pytest.approx(0.0163871)
    assert convert(1, "IN3", "GA") == pytest.approx(0.00432900432900433)