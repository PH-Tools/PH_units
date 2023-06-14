# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_wh_m3():
    assert convert(1, "WH/M3", "WH/M3") == 1
    assert convert(1, "WH/M3", "W/CFM") == pytest.approx(1.699010796)


def test_wh_kilometer_squared():
    assert convert(1, "WH/KM2", "WH/KM2") == 1
    assert convert(1, "WH/KM2", "BTU/FT2") == pytest.approx(0.000000317)


def test_wh_meter_squared():
    assert convert(1, "WH/M2", "WH/M2") == 1
    assert convert(1, "WH/M2", "WH/FT2") == 0.092903
    assert convert(1, "WH/M2", "KWH/M2") == 0.001
    assert convert(1, "WH/M2", "KWH/FT2") == 0.000092903
    assert convert(1, "WH/M2", "BTU/FT2") == pytest.approx(0.316998)
    assert convert(1, "WH/M2", "KBTU/FT2") == pytest.approx(0.000316998)


def test_kwh_meter_squared():
    assert convert(1, "KWH/M2", "WH/M2") == 1000
    assert convert(1, "KWH/M2", "WH/FT2") == 92.903
    assert convert(1, "KWH/M2", "KWH/M2") == 1
    assert convert(1, "KWH/M2", "KWH/FT2") == 0.092903040
    assert convert(1, "KWH/M2", "BTU/FT2") == 316.998
    assert convert(1, "KWH/M2", "KBTU/FT2") == 0.316998286


def test_kBtu_foot_squared():
    assert convert(1, "KBTU/FT2", "WH/M2") == 3154.59
    assert convert(1, "KBTU/FT2", "WH/FT2") == 293.071
    assert convert(1, "KBTU/FT2", "KWH/M2") == 3.15459
    assert convert(1, "KBTU/FT2", "KWH/FT2") == 0.293071
    assert convert(1, "KBTU/FT2", "BTU/FT2") == 1000
    assert convert(1, "KBTU/FT2", "KBTU/FT2") == 1


def test_Btu_foot_squared():
    assert convert(1, "BTU/FT2", "WH/M2") == 3.15459
    assert convert(1, "BTU/FT2", "WH/FT2") == 0.293071
    assert convert(1, "BTU/FT2", "KWH/M2") == 0.00315459
    assert convert(1, "BTU/FT2", "KWH/FT2") == 0.000293071
    assert convert(1, "BTU/FT2", "BTU/FT2") == 1
    assert convert(1, "BTU/FT2", "KBTU/FT2") == 0.001


def test_wh():
    assert convert(1, "WH", "WH") == 1
    assert convert(1, "WH", "BTU") == pytest.approx(3.41214)
    assert convert(1, "WH", "KWH") == 0.001
    assert convert(1, "WH", "KBTU") == pytest.approx(0.003412141633)
    assert convert(1, "WH", "MJ") == pytest.approx(0.0036)
    assert convert(1, "WH", "KJ") == pytest.approx(3.6)


def test_KWH():
    assert convert(1, "KWH", "WH") == 1000
    assert convert(1, "KWH", "BTU") == pytest.approx(3412.141633)
    assert convert(1, "KWH", "KWH") == 1
    assert convert(1, "KWH", "KBTU") == pytest.approx(3.412141633)
    assert convert(1, "KWH", "MJ") == pytest.approx(3.6)
    assert convert(1, "KWH", "KJ") == pytest.approx(3600)


def test_BTU():
    assert convert(1, "BTU", "WH") == pytest.approx(0.293071)
    assert convert(1, "BTU", "BTU") == 1
    assert convert(1, "BTU", "KWH") == pytest.approx(0.000293071)
    assert convert(1, "BTU", "KBTU") == pytest.approx(0.001)
    assert convert(1, "BTU", "MJ") == pytest.approx(0.00105506)
    assert convert(1, "BTU", "KJ") == pytest.approx(1.05506)


def test_KBTU():
    assert convert(1, "KBTU", "WH") == pytest.approx(293.071)
    assert convert(1, "KBTU", "BTU") == 1000
    assert convert(1, "KBTU", "KWH") == pytest.approx(0.293071)
    assert convert(1, "KBTU", "KBTU") == 1
    assert convert(1, "KBTU", "MJ") == pytest.approx(1.05506)
    assert convert(1, "KBTU", "KJ") == pytest.approx(1055.06)


def test_MegaJoule():
    assert convert(1, "MJ", "WH") == pytest.approx(277.778)
    assert convert(1, "MJ", "BTU") == pytest.approx(947.817)
    assert convert(1, "MJ", "KWH") == pytest.approx(0.277778)
    assert convert(1, "MJ", "KBTU") == pytest.approx(0.947817)
    assert convert(1, "MJ", "MJ") == 1
    assert convert(1, "MJ", "KJ") == pytest.approx(1000)


def test_KiloJoule():
    assert convert(1, "KJ", "WH") == pytest.approx(0.277778)
    assert convert(1, "KJ", "BTU") == pytest.approx(0.947817)
    assert convert(1, "KJ", "KWH") == pytest.approx(0.000277778)
    assert convert(1, "KJ", "KBTU") == pytest.approx(0.000947817)
    assert convert(1, "KJ", "MJ") == pytest.approx(0.001)
    assert convert(1, "KJ", "KJ") == 1
