# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.parser import parse_input


def test_parse_input():
    assert parse_input("0.5 in") == ("0.5", "IN")
    assert parse_input('0.5"') == ("0.5", "IN")
    assert parse_input("0.5'") == ("0.5", "FT")
    assert parse_input("0.5") == ("0.5", None)
    assert parse_input("-0.5") == ("-0.5", None)
    assert parse_input(0.5) == ("0.5", None)
    assert parse_input(-0.5) == ("-0.5", None)
    assert parse_input("0.5Btu/hr-Ft2-F") == ("0.5", "BTU/HR-FT2-F")
