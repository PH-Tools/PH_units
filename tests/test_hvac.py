# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_MEF():
    assert convert(2.2, "MEF", "IMEF") == pytest.approx(2.593)
    assert convert(2.2, "MEF", "MEF") == 2.2


def test_IMEF():
    assert convert(2.593, "IMEF", "IMEF") == 2.593
    assert convert(2.593, "IMEF", "MEF") == pytest.approx(2.2)
