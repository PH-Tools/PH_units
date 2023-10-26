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
    assert parse_input("1,000 ft2") == ("1000", "FT2")
    assert parse_input("124,456,678.95 ft3") == ("124456678.95", "FT3")


def test_parse_string_no_units():
    assert parse_input("4") == ("4", None)
    assert parse_input(4) == ("4", None)
    assert parse_input("-4") == ("-4", None)
    assert parse_input(-4) == ("-4", None)

    assert parse_input("4.0") == ("4.0", None)
    assert parse_input(4.0) == ("4.0", None)
    assert parse_input("-4.0") == ("-4.0", None)
    assert parse_input(-4.0) == ("-4.0", None)

    assert parse_input("1,000") == ("1000", None)


def test_parse_string_with_units():
    assert parse_input("4 BTU/HR-FT-F") == ("4", "BTU/HR-FT-F")
    assert parse_input("4 BTU/HR-FT-F") == ("4", "BTU/HR-FT-F")
    assert parse_input("4BTU/HR-FT-F") == ("4", "BTU/HR-FT-F")
    assert parse_input("-4 BTU/HR-FT-F") == ("-4", "BTU/HR-FT-F")

    assert parse_input("4.0 BTU/HR-FT-F") == ("4.0", "BTU/HR-FT-F")
    assert parse_input("4.0BTU/HR-FT-F") == ("4.0", "BTU/HR-FT-F")
    assert parse_input("-4.0 BTU/HR-FT-F") == ("-4.0", "BTU/HR-FT-F")

    assert parse_input("-456,678.0 BTU/HR-FT-F") == ("-456678.0", "BTU/HR-FT-F")



def test_parse_string_no_value():
    assert parse_input("Missing Value") == ("", "MISSING VALUE")
