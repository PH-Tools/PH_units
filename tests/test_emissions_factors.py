# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_gram_per_kWh():
    assert convert(1, "G/KWH", "G/KWH") == 1
    assert convert(1, "G/KWH", "G/BTU") == pytest.approx(0.000293071)
    assert convert(1, "G/KWH", "G/KBTU") == pytest.approx(0.293071)


def test_gram_per_btu():
    assert convert(1, "G/BTU", "G/KWH") == pytest.approx(3412.14)
    assert convert(1, "G/BTU", "G/BTU") == 1
    assert convert(1, "G/BTU", "G/KBTU") == pytest.approx(1000)


def test_gram_per_kBtu():
    assert convert(1, "G/KBTU", "G/KWH") == pytest.approx(3.4121416)
    assert convert(1, "G/KBTU", "G/BTU") == pytest.approx(0.001)
    assert convert(1, "G/KBTU", "G/KBTU") == 1


# --- CO2 per Area ------------------------------------------------------------


def test_metric_ton_per_meter_squared():
    assert convert(1, "MT/M2", "MT/M2") == 1
    assert convert(1, "MT/M²", "MT/M²") == 1
    assert convert(1, "MT/M2", "KG/M2") == 1000
    assert convert(1, "MT/M2", "G/M2") == 1_000_000


def test_kilogram_per_meter_squared():
    assert convert(1, "KG/M2", "MT/M2") == pytest.approx(0.001)
    assert convert(1, "KG/M²", "KG/M²") == 1
    assert convert(1, "KG/M2", "KG/M2") == 1
    assert convert(1, "KG/M2", "G/M2") == pytest.approx(1000)


def test_gram_per_meter_squared():
    assert convert(1, "G/M2", "MT/M2") == pytest.approx(0.000001)
    assert convert(1, "G/M2", "KG/M2") == pytest.approx(0.001)
    assert convert(1, "G/M2", "G/M2") == 1
    assert convert(1, "G/M²", "G/M²") == 1
