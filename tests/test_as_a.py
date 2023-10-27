from ph_units.unit_type import Unit

def test_basic_use() -> None:
    assert Unit(1.0, "KWH").as_a("KBTU") == Unit(3.41214, "KBTU")


def test_zero_value() -> None:
    assert Unit(0, "KWH").as_a("KBTU") == Unit(0, "KBTU")
