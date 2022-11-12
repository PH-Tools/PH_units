# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_meter():
    assert convert(1, "M", "M") == 1
    assert convert(1, "M", "CM") == 100
    assert convert(1, "M", "MM") == 1000
    assert convert(1, "M", "FT") == pytest.approx(3.280839895)
    assert convert(1, "M", "IN") == pytest.approx(39.37007874)


def test_centimeter():
    assert convert(1, "CM", "M") == 0.01
    assert convert(1, "CM", "CM") == 1
    assert convert(1, "CM", "MM") == 10
    assert convert(1, "CM", "FT") == pytest.approx(0.0328)
    assert convert(1, "CM", "IN") == pytest.approx(0.3937)


def test_millimeter():
    assert convert(1, "MM", "M") == 0.001
    assert convert(1, "MM", "CM") == 0.1
    assert convert(1, "MM", "MM") == 1
    assert convert(1, "MM", "FT") == pytest.approx(0.003280842)
    assert convert(1, "MM", "IN") == pytest.approx(0.039370100)


def test_inch():
    assert convert(1, "IN", "M") == 0.0254
    assert convert(1, "IN", "CM") == 2.54
    assert convert(1, "IN", "MM") == 25.4
    assert convert(1, "IN", "FT") == (1 / 12)
    assert convert(1, "IN", "IN") == 1


def test_foot():
    assert convert(1, "FT", "M") == 0.3048
    assert convert(1, "FT", "CM") == 30.48
    assert convert(1, "FT", "MM") == 304.8
    assert convert(1, "FT", "FT") == 1
    assert convert(1, "FT", "IN") == 12
