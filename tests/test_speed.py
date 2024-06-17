# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_meters_per_day():
    assert convert(1, "M/DAY", "M/DAY") == 1
    assert convert(1, "M/DAY", "FT/DAY") == 3.280839895
    assert convert(10, "M/DAY", "M/S") == pytest.approx(0.000115740740740741)


def test_meters_per_second():
    assert convert(1, "M/S", "M/S") == 1
    assert convert(1, "M/S", "M/DAY") == 86400
    assert convert(1, "M/S", "FT/S") == pytest.approx(3.28084)
    assert convert(1, "M/S", "FT/DAY") == pytest.approx(283_464.566928000)
    assert convert(1, "M/S", "MPH") == pytest.approx(2.2369362920544)


def test_miles_per_hour():
    assert convert(1, "MPH", "M/S") == pytest.approx(0.44704)
    assert convert(1, "MPH", "M/DAY") == pytest.approx(38624.255999999994)
    assert convert(1, "MPH", "FT/S") == pytest.approx(1.466666667)
    assert convert(1, "MPH", "FT/DAY") == pytest.approx(126_720)


def test_feet_per_second() -> None:
    assert convert(1, "FT/S", "M/S") == pytest.approx(0.3048)
    assert convert(1, "FT/S", "M/DAY") == pytest.approx(26_334.7)


def test_feet_per_day():
    assert convert(1, "FT/DAY", "M/DAY") == pytest.approx(0.3048)
    assert convert(1, "FT/DAY", "M/S") == pytest.approx(3.52778e-6)
    assert convert(1, "FT/DAY", "FT/DAY") == 1
    assert convert(1, "FT/DAY", "FT/S") == pytest.approx(1.1574074074074073e-05)
