# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_meter_squared():
    assert convert(1, "M2", "SI") == 1
    assert convert(1, "M2", "M2") == 1
    assert convert(1, "M2", "FT2") == pytest.approx(10.76391042)


def test_foot_squared():
    assert convert(1, "FT2", "SI") == pytest.approx(0.09290304)
    assert convert(1, "FT2", "M2") == pytest.approx(0.09290304)
    assert convert(1, "FT2", "FT2") == 1
