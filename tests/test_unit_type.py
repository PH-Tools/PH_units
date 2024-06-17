from functools import reduce

import pytest

from ph_units.unit_type import Unit


def test_default_Unit():
    u = Unit()
    assert u.value == 0.0
    assert u.unit == "-"


def test_percent_Unit():
    u = Unit(1.0, "%")
    assert u.value == 1.0
    assert u.unit == "%"


def test_add_percent_unit():
    u1 = Unit(1.0, "%")
    u2 = Unit(1.0, "%")
    u3 = u1 + u2
    assert u3.value == 2.0
    assert u3.unit == "%"


def test_Unit_is_frozen():
    u = Unit()

    with pytest.raises(AttributeError):
        u._value = 1.0

    with pytest.raises(AttributeError):
        u._unit = "m"


def test_add_two_of_the_same_Units():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "m")
    u3 = u1 + u2
    assert u3.value == 3.0
    assert u3.unit == "m"


def test_add_one_unit_one_float():
    u1 = Unit(1.0, "m")
    u2 = 2.0
    u3 = u1 + u2
    assert u3.value == 3.0
    assert u3.unit == "m"


def test_add_two_different_units():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "s")
    with pytest.raises(TypeError):
        u3 = u1 + u2


def test_sum_list_of_units():
    units_list = [
        Unit(1.0, "m"),
        Unit(2.0, "m"),
        Unit(3.0, "m"),
    ]

    u = sum(units_list, Unit(0.0, "m"))
    assert u.value == 6.0


def test_reduce_list_of_units():
    units_list = [
        Unit(1.0, "m"),
        Unit(2.0, "m"),
        Unit(3.0, "m"),
    ]

    u = reduce(lambda x, y: x + y, units_list)
    assert u.value == 6.0


def test_subtract_two_same_units():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "m")
    u3 = u2 - u1
    assert u3.value == 1.0
    assert u3.unit == "m"


def test_subtract_one_unit_one_float():
    u1 = Unit(1.0, "m")
    u2 = 2.0
    u3 = u1 - u2
    assert u3.value == -1.0
    assert u3.unit == "m"


def test_subtract_two_different_units():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "s")
    with pytest.raises(TypeError):
        u3 = u1 - u2


def test_multiply_two_units():
    u1 = Unit(2.0, "m")
    u2 = Unit(2.0, "m")
    u3 = u1 * u2
    assert u3.value == 4.0
    assert u3.unit == "m"


def test_multiply_one_unit_one_float():
    u1 = Unit(2.0, "m")
    u2 = 2.0
    u3 = u1 * u2
    assert u3.value == 4.0
    assert u3.unit == "m"


def test_multiply_two_different_units():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "s")
    with pytest.raises(TypeError):
        u3 = u1 * u2


def test_units_equal():
    u1 = Unit(1.0, "m")
    u2 = Unit(1.0, "m")
    assert u1 == u2


def test_units_not_equal():
    u1 = Unit(1.0, "m")
    u2 = Unit(2.0, "m")
    assert u1 != u2


def test_sort_list_of_units():
    units_list = [
        Unit(3.0, "m"),
        Unit(1.0, "m"),
        Unit(2.0, "m"),
    ]
    assert sorted(units_list) == [
        Unit(1.0, "m"),
        Unit(2.0, "m"),
        Unit(3.0, "m"),
    ]


def test_unit_dict_round_trip():
    u = Unit(1.0, "m")
    u_dict = u.to_dict()
    u2 = Unit.from_dict(u_dict)
    assert u == u2


def test_unit_conversion():
    u1 = Unit(1.0, "m")
    u2 = u1.as_a("cm")
    assert u2.value == 100.0


def test_invert_unit_conversion():
    u1 = Unit(100.0, "W/M2K").inverse()

    assert u1.unit == "M2K/W"
    assert u1.value == 0.01


def test_invert_unit_IP_UValue():
    u1 = Unit(0.2, "BTU/HR-FT2-F").inverse()

    assert u1.unit == "HR-FT2-F/BTU"
    assert u1.value == 5.0


def test_divide_unit_SI():
    u1 = Unit(100.0, "M")
    u2 = Unit(10.0, "M")
    u3 = u1 / u2
    assert u3.value == 10.0
    assert u3.unit == "-"


def test_cannot_divide_different_units():
    u1 = Unit(100.0, "M")
    u2 = Unit(10.0, "S")
    with pytest.raises(TypeError):
        u3 = u1 / u2


def test_divide_unit_by_float():
    u1 = Unit(100.0, "M")
    u2 = 10.0
    u3 = u1 / u2
    assert u3.value == 10.0
    assert u3.unit == "M"


def test_lt_unit_and_float():
    u1 = Unit(1.0, "M")
    u2 = 2.0
    assert u1 < u2


def test_lt_two_units():
    u1 = Unit(1.0, "M")
    u2 = Unit(2.0, "M")
    assert u1 < u2


def test_cant_lt_two_different_units():
    u1 = Unit(1.0, "M")
    u2 = Unit(2.0, "S")
    with pytest.raises(TypeError):
        assert u1 < u2


def test_eq_unit_and_int():
    u1 = Unit(1.0, "M")
    u2 = 1
    assert u1 == u2
