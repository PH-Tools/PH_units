# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

import pytest

from ph_units.converter import convert


def test_wh_m3():
    assert convert(1, "WH/M³", "WH/M3") == 1
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
    assert convert(1, "KWH/M²", "WH/M2") == 1000
    assert convert(1, "KWH/M2", "WH/FT2") == 92.903
    assert convert(1, "KWH/M2", "KWH/M2") == 1
    assert convert(1, "KWH/M2", "KWH/IN2") == 0.0006451600000025807
    assert convert(1, "KWH/M2", "KWH/FT2") == 0.092903040
    assert convert(1, "KWH/M2", "BTU/FT2") == 316.998330628
    assert convert(1, "KWH/M2", "KBTU/FT2") == 0.316998286


def test_kWh_per_in2():
    assert convert(1, "KWH/IN2", "WH/M2") == 1_550_003.1000062001
    assert convert(1, "KWH/IN2", "WH/FT2") == 144_000
    assert convert(1, "KWH/IN2", "KWH/M2") == 1_550.0031000062001
    assert convert(1, "KWH/IN2", "KWH/IN2") == 1
    assert convert(1, "KWH/IN2", "KWH/FT2") == 144
    assert convert(1, "KWH/IN2", "BTU/FT2") == 491_348.448
    assert convert(1, "KWH/IN2", "KBTU/FT2") == 491.34844799999996


def test_kBtu_foot_squared():
    assert convert(1, "KBTU/FT2", "WH/M2") == 3154.59
    assert convert(1, "KBTU/FT²", "WH/M2") == 3154.59
    assert convert(1, "KBTU/FT2", "WH/FT2") == 293.071
    assert convert(1, "KBTU/FT2", "KWH/M2") == 3.15459
    assert convert(1, "KBTU/FT2", "KWH/FT2") == 0.293071
    assert convert(1, "KBTU/FT2", "BTU/FT2") == 1000
    assert convert(1, "KBTU/FT2", "KBTU/FT2") == 1


def test_Btu_foot_squared():
    assert convert(1, "BTU/FT²", "WH/M2") == 3.15459
    assert convert(1, "BTU/FT2", "WH/M2") == 3.15459
    assert convert(1, "BTU/FT2", "WH/FT2") == 0.293071
    assert convert(1, "BTU/FT2", "KWH/M2") == 0.00315459
    assert convert(1, "BTU/FT2", "KWH/FT2") == 0.000293071
    assert convert(1, "BTU/FT2", "BTU/FT2") == 1
    assert convert(1, "BTU/FT2", "KBTU/FT2") == 0.001


def test_therm():
    assert convert(1, "THERM", "THERM") == 1
    assert convert(convert(1, "THERM", "BTU"), "BTU", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "KBTU"), "KBTU", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "WH"), "WH", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "KWH"), "KWH", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "J"), "J", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "KJ"), "KJ", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "MJ"), "MJ", "THERM") == pytest.approx(1)
    assert convert(convert(1, "THERM", "GJ"), "GJ", "THERM") == pytest.approx(1)


def test_wh():
    assert convert(1, "WH", "BTU") == pytest.approx(3.41214)
    assert convert(1, "WH", "KBTU") == pytest.approx(0.003412141633)
    assert convert(1, "WH", "WH") == 1
    assert convert(1, "WH", "KWH") == 0.001
    assert convert(1, "WH", "J") == 3600
    assert convert(1, "WH", "KJ") == pytest.approx(3.6)
    assert convert(1, "WH", "MJ") == pytest.approx(0.0036)
    assert convert(1, "WH", "GJ") == pytest.approx(0.0000036)


def test_KWH():
    assert convert(1, "KWH", "BTU") == pytest.approx(3412.141633)
    assert convert(1, "KWH", "KBTU") == pytest.approx(3.412141633)
    assert convert(1, "KWH", "WH") == 1000
    assert convert(1, "KWH", "KWH") == 1
    assert convert(1, "KWH", "J") == pytest.approx(3600000)
    assert convert(1, "KWH", "KJ") == pytest.approx(3600)
    assert convert(1, "KWH", "MJ") == pytest.approx(3.6)
    assert convert(1, "KWH", "GJ") == pytest.approx(0.0036)


def test_BTU():
    assert convert(1, "BTU", "BTU") == 1
    assert convert(1, "BTU", "KBTU") == pytest.approx(0.001)
    assert convert(1, "BTU", "WH") == pytest.approx(0.293071)
    assert convert(1, "BTU", "KWH") == pytest.approx(0.000293071)
    assert convert(1, "BTU", "J") == pytest.approx(1055.06)
    assert convert(1, "BTU", "KJ") == pytest.approx(1.05506)
    assert convert(1, "BTU", "MJ") == pytest.approx(0.00105506)
    assert convert(1, "BTU", "GJ") == pytest.approx(0.00000105506)


def test_KBTU():
    assert convert(1, "KBTU", "BTU") == 1000
    assert convert(1, "KBTU", "KBTU") == 1
    assert convert(1, "KBTU", "WH") == pytest.approx(293.071)
    assert convert(1, "KBTU", "KWH") == pytest.approx(0.293071)
    assert convert(1, "KBTU", "J") == pytest.approx(1055060)
    assert convert(1, "KBTU", "KJ") == pytest.approx(1055.06)
    assert convert(1, "KBTU", "MJ") == pytest.approx(1.05506)
    assert convert(1, "KBTU", "GJ") == pytest.approx(0.00105506)


def test_Joule():
    assert convert(1, "J", "BTU") == pytest.approx(0.000947817)
    assert convert(1, "J", "KBTU") == pytest.approx(0.000000947817)
    assert convert(1, "J", "WH") == pytest.approx(0.000277778)
    assert convert(1, "J", "KWH") == pytest.approx(0.00000027778)
    assert convert(1, "J", "J") == 1
    assert convert(1, "J", "KJ") == pytest.approx(0.001)
    assert convert(1, "J", "MJ") == pytest.approx(0.000001)
    assert convert(1, "J", "GJ") == pytest.approx(0.000000001)


def test_KiloJoule():
    assert convert(1, "KJ", "BTU") == pytest.approx(0.947817)
    assert convert(1, "KJ", "KBTU") == pytest.approx(0.000947817)
    assert convert(1, "KJ", "WH") == pytest.approx(0.277778)
    assert convert(1, "KJ", "KWH") == pytest.approx(0.000277778)
    assert convert(1, "KJ", "J") == 1000
    assert convert(1, "KJ", "MJ") == pytest.approx(0.001)
    assert convert(1, "KJ", "KJ") == 1
    assert convert(1, "KJ", "GJ") == pytest.approx(0.000001)


def test_MegaJoule():
    assert convert(1, "MJ", "BTU") == pytest.approx(947.817)
    assert convert(1, "MJ", "KBTU") == pytest.approx(0.947817)
    assert convert(1, "MJ", "WH") == pytest.approx(277.778)
    assert convert(1, "MJ", "KWH") == pytest.approx(0.277778)
    assert convert(1, "MJ", "J") == pytest.approx(1000000)
    assert convert(1, "MJ", "KJ") == pytest.approx(1000)
    assert convert(1, "MJ", "MJ") == 1
    assert convert(1, "MJ", "GJ") == pytest.approx(0.001)


def test_GigaJoule():
    assert convert(1, "GJ", "BTU") == pytest.approx(947817)
    assert convert(1, "GJ", "KBTU") == pytest.approx(947.817)
    assert convert(1, "GJ", "WH") == pytest.approx(277778)
    assert convert(1, "GJ", "KWH") == pytest.approx(277.778)
    assert convert(1, "GJ", "J") == pytest.approx(1000000000)
    assert convert(1, "GJ", "KJ") == pytest.approx(1000000)
    assert convert(1, "GJ", "MJ") == pytest.approx(1000)
    assert convert(1, "GJ", "GJ") == 1


def test_MegaJoule_per_m3_DegreeKelvin():
    assert convert(1, "MJ/M3K", "MJ/M3K") == 1
    assert convert(1, "MJ/M3K", "BTU/FT3F") == pytest.approx(14.91066014)


def test_Btu_per_ft3_DegreeFarenheit():
    assert convert(1, "BTU/FT3F", "BTU/FT3F") == 1
    assert convert(1, "BTU/FT3F", "MJ/M3K") == pytest.approx(0.067066112)


def test_Joule_per_Kilogram_DegreeKelvin():
    assert convert(1, "J/KGK", "J/KGK") == 1
    assert convert(1, "J/KGK", "BTU/LBF") == pytest.approx(0.000238846)


def test_Btu_per_Pound_degree_Farenheit() -> None:
    assert convert(1, "BTU/LBF", "BTU/LBF") == 1
    assert convert(1, "BTU/LBF", "J/KGK") == pytest.approx(4186.8)


def test_wattHour_per_m2_per_degree_Kelvin() -> None:
    assert convert(1, "WH/M2K", "WH/M2K") == 1
    assert convert(1, "WH/M2K", "WH/M²K") == 1
    assert convert(1, "WH/M2K", "BTU/FT2F") == pytest.approx(0.1761102)
    assert convert(1, "WH/M2K", "WH/FT2F") == pytest.approx(0.0516128)


def test_wattHour_per_ft2_per_degree_Farenheit():
    assert convert(1, "WH/FT2F", "WH/FT2F") == 1
    assert convert(1, "WH/FT2F", "WH/M2K") == pytest.approx(19.37503875)
    assert convert(1, "WH/FT2F", "BTU/FT2F") == pytest.approx(3.412141156)


def test_Btu_per_ft2_per_degree_Farenheit():
    assert convert(1, "BTU/FT2F", "BTU/FT2F") == 1
    assert convert(1, "BTU/FT2F", "WH/M2K") == pytest.approx(5.678264134)
    assert convert(1, "BTU/FT2F", "WH/FT2F") == pytest.approx(0.293071111)


def test_kWh_per_kWh():
    assert convert(1, "KWH/KWH", "KWH/KWH") == 1
    assert convert(1, "KWH/KWH", "BTU/BTU") == 1


def test_Btu_per_Btu():
    assert convert(1, "BTU/BTU", "BTU/BTU") == 1
    assert convert(1, "BTU/BTU", "KWH/KWH") == 1


def test_cost_per_kwh():
    assert convert(1, "COST/KWH", "COST/KWH") == 1
    assert convert(0.0423, "COST/KWH", "COST/THERM") == pytest.approx(1.239690799999995)
    assert convert(
        convert(1, "COST/KWH", "COST/THERM"), "COST/THERM", "COST/KWH"
    ) == pytest.approx(1)


def test_cost_per_THERM():
    assert convert(1, "COST/THERM", "COST/THERM") == 1
    assert convert(1, "COST/THERM", "COST/KWH") == pytest.approx(0.034121411564883894)
    assert convert(1.24, "COST/THERM", "COST/KWH") == pytest.approx(0.04231055034045603)
    assert convert(
        convert(1, "COST/THERM", "COST/KWH"), "COST/KWH", "COST/THERM"
    ) == pytest.approx(1)
