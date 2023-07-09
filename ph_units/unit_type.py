# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

"""Class to manage numeric values with a unit-type (ie: 0.5 IN)."""

try:
    from typing import Any, Iterable, Union, Dict
except ImportError:
    pass  # Python 2.7

from ph_units.converter import convert


class Unit(object):
    """A numeric value with a unit-type."""

    _frozen = False

    def __init__(self, value=0.0, unit="-"):
        # type: (Union[float, str, None], str) -> None
        self._value = float(str(value or 0).replace(",", ""))
        self._unit = unit
        self._frozen = True

    @property
    def value(self):
        # type: () -> float
        return self._value

    @property
    def unit(self):
        # type: () -> str
        return self._unit

    def as_a(self, unit):
        # type: (str) -> Unit
        """Return a new Unit in the specified unit-type."""
        new_value = convert(self.value, self.unit, unit)
        if not new_value:
            raise ValueError(
                "Cannot convert from '{}' to '{}'.".format(self.unit, unit)
            )
        return Unit(new_value, unit)

    @classmethod
    def from_dict(cls, data):
        # type: (Dict) -> Unit
        """Update the value and unit-type from a dictionary."""
        return cls(data["value"], data["unit"])

    def to_dict(self):
        # type: () -> Dict[str, Any]
        """Return a dictionary representation of the object."""
        return {"value": self.value, "unit": self.unit}

    def __sub__(self, other):
        # type: (Union[Unit, int, float]) -> Unit
        if not isinstance(other, (Unit, int, float)):
            raise TypeError(
                "Cannot subtract '{}' from '{}'.".format(
                    type(other), self.__class__.__name__
                )
            )
        if isinstance(other, Unit):
            if self.unit != other.unit:
                raise TypeError(
                    "Error: Cannot add '{}' to '{}'.".format(self.unit, other.unit)
                )
            else:
                return Unit(self.value - other.value, self.unit)
        return Unit(self.value - other, self.unit)

    def __add__(self, other):
        # type: (Union[Unit, int, float]) -> Unit
        if not isinstance(other, (Unit, int, float)):
            raise TypeError(
                "Error: Cannot add '{}' to '{}'.".format(type(other), self.__class__.__name__)
            )
        if isinstance(other, Unit):
            if self.unit != other.unit:
                raise TypeError(
                    "Error: Cannot add '{}' to '{}'.".format(self.unit, other.unit)
                )
            else:
                return Unit(self.value + other.value, self.unit)
        return Unit(self.value + other, self.unit)

    def __radd__(self, other):
        # type: (Union[Unit, int, float]) -> Unit  
        if not isinstance(other, Unit):
            return self
        return self.__add__(other)

    def __mul__(self, other):
        # type: (Union[Unit, int, float]) -> Unit
        if not isinstance(other, (Unit, float, int)):
            raise TypeError(
                "Error: Cannot multiply '{}' by '{}'.".format(type(other), self.__class__.__name__)
            )
        if isinstance(other, Unit):
            if self.unit != other.unit:
                raise TypeError(
                    "Error: Cannot multiply '{}' by '{}'.".format(self.unit, other.unit)
                )
            else:
                return Unit(self.value * other.value, self.unit)
        return Unit(self.value * other, self.unit)

    def __bool__(self):
        # type: () -> bool
        return True

    def __nonzero__(self):
        # type: () -> bool
        return True

    def __iter__(self):
        # type: () -> Iterable
        return iter([self])

    def __len__(self):
        # type: () -> int
        return 1

    def __eq__(self, other):
        # type: (Unit) -> bool
        if not isinstance(other, Unit):
            return False
        return self.value == other.value and self.unit == other.unit

    def __le__(self, other):
        # type: (Unit) -> bool
        if not isinstance(other, Unit):
            return False
        if not self.unit == other.unit:
            raise TypeError("Cannot compare '{}' to '{}'.".format(self.unit, other.unit))
        return self.value <= other.value

    def __lt__(self, other):
        # type: (Unit) -> bool
        if not isinstance(other, Unit):
            return False
        if not self.unit == other.unit:
            raise TypeError("Cannot compare '{}' to '{}'.".format(self.unit, other.unit))
        return self.value < other.value

    def __setattr__(self, name, value):
        # type: (str, Any) -> None
        if self._frozen and hasattr(self, name):
            raise AttributeError(
                "Modifying '{}' of '{}' is not allowed.".format(name,self.__class__.__name__)
            )
        super().__setattr__(name, value)

    def __repr__(self):
        # type: () -> str
        return "{} ({})".format(self.value, self.unit)

    def __str__(self):
        # type: () -> str
        return "{:,.3f}".format(self.value)
