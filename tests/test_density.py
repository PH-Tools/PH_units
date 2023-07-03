# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_mg_per_m3():
    assert convert(1, "MG/M3", "MG/M3") == 1
    assert convert(1, "MG/M3", "G/M3") == 0.001
    assert convert(1, "MG/M3", "KG/M3") == 0.000001
    assert convert(1, "MG/M3", "LB/FT3") == pytest.approx(0.000000062428)


def test_gram_per_m3():
    assert convert(1, "G/M3", "G/M3") == 1
    assert convert(1, "G/M3", "MG/M3") == 1000
    assert convert(1, "G/M3", "KG/M3") == 0.001
    assert convert(1, "G/M3", "LB/FT3") == pytest.approx(0.000062428)


def test_kilogram_per_m3():
    assert convert(1, "KG/M3", "KG/M3") == 1
    assert convert(1, "KG/M3", "MG/M3") == 1000000
    assert convert(1, "KG/M3", "G/M3") == 1000
    assert convert(1, "KG/M3", "LB/FT3") == pytest.approx(0.062428)


def test_lb_per_ft3():
    assert convert(1, "LB/FT3", "LB/FT3") == 1
    assert convert(1, "LB/FT3", "MG/M3") == pytest.approx(16018463.4)
    assert convert(1, "LB/FT3", "G/M3") == pytest.approx(16018.4634)
    assert convert(1, "LB/FT3", "KG/M3") == pytest.approx(16.0184634)
