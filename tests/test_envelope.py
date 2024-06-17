# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


# -- SI
def test_SI_U_value():
    assert convert(0.1, "W/M2K", "W/M2K") == 0.1
    assert convert(0.1, "W/M2K", "M2K/W") == 10
    assert convert(0.1, "W/M²K", "M2K/W") == 10
    # SI U-Value:
    assert convert(0.1, "W/M2K", "BTU/HR-FT2-F") == pytest.approx(0.017611016)
    assert convert(2.0, "W/M2K", "BTU/HR-FT2-F") == pytest.approx(0.352220318)
    # SI R-Value:
    assert convert(0.1, "W/M2K", "HR-FT2-F/BTU") == pytest.approx(56.78264134)
    assert convert(2.0, "W/M2K", "HR-FT2-F/BTU") == pytest.approx(2.839132067)


def test_SI_R_value():
    assert convert(2, "M2K/W", "W/M2K") == 0.5
    assert convert(2, "M²K/W", "M2K/W") == 2
    assert convert(2, "M2K/W", "M2K/W") == 2
    # To U-IP Value:
    assert convert(0.5, "M2K/W", "BTU/HR-FT2-F") == pytest.approx(0.352220318)
    assert convert(2, "M2K/W", "BTU/HR-FT2-F") == pytest.approx(0.08805508)
    # TO R-IP Value:
    assert convert(0.5, "M2K/W", "HR-FT2-F/BTU") == pytest.approx(2.839132067)
    assert convert(2, "M2K/W", "HR-FT2-F/BTU") == pytest.approx(11.35652827)


def test_SI_Psi_Value():
    assert convert(0.2, "W/MK", "W/MK") == 0.2
    assert convert(0.2, "W/MK", "BTU/HR-FT-F") == pytest.approx(0.115557847)
    assert convert(0.2, "W/MK", "HR-FT2-F/BTU-IN") == pytest.approx(0.721139545)


def test_SI_Chi_Value():
    assert convert(0.2, "W/K", "W/K") == 0.2
    assert convert(0.2, "W/K", "BTU/HR-F") == pytest.approx(0.379126795)


# -- IP
def test_IP_U_value():
    assert convert(0.2, "BTU/HR-FT2-F", "W/M2K") == pytest.approx(1.135652827)
    assert convert(0.2, "BTU/HR-FT2-F", "M2K/W") == pytest.approx(0.880550795)
    assert convert(0.2, "BTU/HRFT²°F", "M2K/W") == pytest.approx(0.880550795)
    assert convert(0.2, "BTU/HR-FT2-F", "BTU/HR-FT2-F") == 0.2
    assert convert(0.2, "BTU/HR-FT2-F", "HR-FT2-F/BTU") == 5


def test_IP_R_value():
    assert convert(4, "HR-FT2-F/BTU", "W/M2K") == pytest.approx(1.419566034)
    assert convert(4, "HR-FT2-F/BTU", "M2K/W") == pytest.approx(0.704440636)
    assert convert(4, "HR-FT2-F/BTU", "BTU/HR-FT2-F") == 0.25
    assert convert(4, "HR-FT2-F/BTU", "HR-FT2-F/BTU") == 4


def test_IP_R_per_inch():
    assert convert(5, "HR-FT2-F/BTU-IN", "W/MK") == pytest.approx(0.028845582)
    assert convert(5, "HR-FT2-F/BTU-IN", "BTU/HR-FT-F") == pytest.approx(0.016666667)


def test_IP_Psi_Value():
    assert convert(0.2, "BTU/HR-FT-F", "W/MK") == pytest.approx(0.346146982)
    assert convert(0.2, "BTU/HR-FT-F", "BTU/HR-FT-F") == 0.2
    assert convert(0.2, "BTU/HR-FT-F", "HR-FT2-F/BTU-IN") == pytest.approx(0.416666667)


def test_IP_Chi_Value():
    assert convert(1.0, "BTU/HR-F", "W/K") == pytest.approx(0.527528)
    assert convert(0.2, "BTU/HR-F", "BTU/HR-F") == 0.2
