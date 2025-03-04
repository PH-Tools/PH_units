# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


# -- SI
def test_M3_per_second():
    assert convert(0.02, "M3/S", "M3/S") == 0.02
    assert convert(0.02, "M3/S", "M3/M") == 1.2
    assert convert(0.02, "M3/S", "M3/HR") == 72
    assert convert(0.02, "M3/S", "CFM") == pytest.approx(42.37760007)
    assert convert(0.02, "M3/S", "CFH") == pytest.approx(2542.656004)


def test_M3_per_minute():
    assert convert(1.2, "M3/M", "M3/S") == 0.02
    assert convert(1.2, "M3/M", "M3/M") == 1.2
    assert convert(1.2, "M3/M", "M3/HR") == 72
    assert convert(1.2, "M3/M", "CFM") == pytest.approx(42.37760007)
    assert convert(1.2, "M3/M", "CFH") == pytest.approx(2542.656004)


def test_M3_per_hour():
    assert convert(72, "M3/HR", "M3/S") == 0.02
    assert convert(72, "M3/HR", "M3/M") == 1.2
    assert convert(72, "M3/HR", "M3/HR") == 72
    assert convert(72, "M3/HR", "CFM") == pytest.approx(42.37760007)
    assert convert(72, "M3/HR", "CFH") == pytest.approx(2542.656004)


def test_M3_per_hour_per_square_meter():
    assert convert(72, "M3/HR-M2", "M3/HR-M2") == 72
    assert convert(43_200, "M3/HR-M2", "M3/S-M2") == 12
    assert convert(72, "M3/HR-M2", "CFM/FT2") == pytest.approx(3.937007874)


def test_M3_per_second_per_square_meter():
    assert convert(212.5, "M3/S-M2", "M3/HR-M2") == 765_000
    assert convert(43200, "M3/S-M2", "M3/S-M2") == 43200
    assert convert(72, "M3/S-M2", "CFM/FT2") == pytest.approx(14_173.228368)


def test_FT3_per_minute():
    assert convert(50, "CFM", "M3/S") == pytest.approx(0.023597372)
    assert convert(50, "CFM", "M3/M") == pytest.approx(1.41584233)
    assert convert(50, "CFM", "M3/HR") == pytest.approx(84.95053978)
    assert convert(50, "CFM", "CFM") == 50
    assert convert(50, "CFM", "CFH") == 3000


def test_FT3_per_hour():
    assert convert(3000, "CFH", "M3/S") == pytest.approx(0.023597372)
    assert convert(3000, "CFH", "M3/M") == pytest.approx(1.41584233)
    assert convert(3000, "CFH", "M3/HR") == pytest.approx(84.95053978)
    assert convert(3000, "CFH", "CFM") == 50
    assert convert(3000, "CFH", "CFH") == 3000


def test_FT3_per_minute_per_FT2():
    assert convert(72, "CFM/FT2", "CFM/FT2") == 72
    assert convert(500, "CFM/FT2", "M3/S-M2") == pytest.approx(2.54)
    assert convert(72, "CFM/FT2", "M3/HR-M2") == pytest.approx(1_316.736)
