# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-
import pytest

from ph_units.converter import (
    UnitTypeNameNotFound,
    _standardize_unit_name,
    unit_type_alias_dict,
    unit_type_dict,
    validate_unit_type,
)


def test_standardize_unit_name_simple() -> None:
    assert _standardize_unit_name("FT", unit_type_alias_dict) == "FT"
    assert _standardize_unit_name("FT", unit_type_alias_dict) == "FT"


def test_standardize_unit_name_percent() -> None:
    assert _standardize_unit_name("%", unit_type_alias_dict) == "%"


def test_standardize_unit_name_alias() -> None:
    assert _standardize_unit_name("FT3/M", unit_type_alias_dict) == "CFM"
    assert _standardize_unit_name("CFM", unit_type_alias_dict) == "CFM"


def test_standardize_gives_error() -> None:
    with pytest.raises(UnitTypeNameNotFound):
        _standardize_unit_name("Not/A-Unit", unit_type_alias_dict)


def test_validate_unit_type() -> None:
    assert validate_unit_type("FT") == "FT"
    assert validate_unit_type("ft") == "FT"
    assert validate_unit_type("Btu/hr-ft2-F") == "BTU/HR-FT2-F"
    with pytest.raises(UnitTypeNameNotFound):
        validate_unit_type("Not/A-Unit")
