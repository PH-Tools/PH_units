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
