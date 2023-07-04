# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest
from ph_units.converter import convert


def test_wufi_mew_to_us_perm_in():
    assert convert(10, "WUFI_MEW", "PERM-IN") == pytest.approx(12.88)
    assert convert(5, "WUFI_MEW", "PERM-IN") == pytest.approx(25.76)
    assert convert(203, "WUFI_MEW", "PERM-IN") == pytest.approx(0.634482771310345)
    assert convert(4, "WUFI_MEW", "PERM-IN") == pytest.approx(32.2)


def test_us_perm_in_to_wufi_mew():
    assert convert(12.88, "PERM-IN", "WUFI_MEW") == pytest.approx(10)
    assert convert(25.76, "PERM-IN", "WUFI_MEW") == pytest.approx(5)
    assert convert(0.634482771310345, "PERM-IN", "WUFI_MEW") == pytest.approx(203)
    assert convert(32.2, "PERM-IN", "WUFI_MEW") == pytest.approx(4)
