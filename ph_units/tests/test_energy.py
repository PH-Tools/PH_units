# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_wh_m3():
    assert convert(1, "WH/M3", "SI") == 1
    assert convert(1, "WH/M3", "WH/M3") == 1
    assert convert(1, "WH/M3", "W/CFM") == pytest.approx(1.699010796)


def test_wh_kilometer_squared():
    assert convert(1, "WH/KM2", "SI") == 1
    assert convert(1, "WH/KM2", "WH/KM2") == 1
    assert convert(1, "WH/KM2", "BTU/FT2") == pytest.approx(0.000000317)


def test_wh_meter_squared():
    assert convert(1, "WH/M2", "SI") == 1
    assert convert(1, "WH/M2", "WH/M2") == 1
    assert convert(1, "WH/M2", "WH/FT2") == 0.092903
    assert convert(1, "WH/M2", "KWH/M2") == 0.001
    assert convert(1, "WH/M2", "KWH/FT2") == 0.000092903
    assert convert(1, "WH/M2", "BTU/FT2") == pytest.approx(0.316998)
    assert convert(1, "WH/M2", "KBTU/FT2") == pytest.approx(0.000316998)


def test_kwh_meter_squared():
    assert convert(1, "KWH/M2", "SI") == 1
    assert convert(1, "KWH/M2", "WH/M2") == 1000
    assert convert(1, "KWH/M2", "WH/FT2") == 92.903
    assert convert(1, "KWH/M2", "KWH/M2") == 1
    assert convert(1, "KWH/M2", "KWH/FT2") == 0.092903040
    assert convert(1, "KWH/M2", "BTU/FT2") == 316.998
    assert convert(1, "KWH/M2", "KBTU/FT2") == 0.316998286


def test_kBtu_foot_squared():
    assert convert(1, "KBTU/FT2", "SI") == 3.15459
    assert convert(1, "KBTU/FT2", "WH/M2") == 3154.59
    assert convert(1, "KBTU/FT2", "WH/FT2") == 293.071
    assert convert(1, "KBTU/FT2", "KWH/M2") == 3.15459
    assert convert(1, "KBTU/FT2", "KWH/FT2") == 0.293071
    assert convert(1, "KBTU/FT2", "BTU/FT2") == 1000
    assert convert(1, "KBTU/FT2", "KBTU/FT2") == 1


def test_Btu_foot_squared():
    assert convert(1, "BTU/FT2", "SI") == 0.00315459
    assert convert(1, "BTU/FT2", "WH/M2") == 3.15459
    assert convert(1, "BTU/FT2", "WH/FT2") == 0.293071
    assert convert(1, "BTU/FT2", "KWH/M2") == 0.00315459
    assert convert(1, "BTU/FT2", "KWH/FT2") == 0.000293071
    assert convert(1, "BTU/FT2", "BTU/FT2") == 1
    assert convert(1, "BTU/FT2", "KBTU/FT2") == 0.001
