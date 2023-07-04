# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

"""Unit-Type Conversion Factors."""

try:
    from typing import Dict, Tuple
    from types import ModuleType
except ImportError:
    pass  # Python 2.7

from ph_units.unit_types._base import Base_UnitType
from ph_units.unit_types import area
from ph_units.unit_types import energy
from ph_units.unit_types import envelope
from ph_units.unit_types import length
from ph_units.unit_types import power
from ph_units.unit_types import speed
from ph_units.unit_types import temperature
from ph_units.unit_types import volume_flow
from ph_units.unit_types import volume
from ph_units.unit_types import density
from ph_units.unit_types import emissions_factors
from ph_units.unit_types import moisture_vapor_resistance


UNIT_TYPE_MODULES = (
    area,
    energy,
    envelope,
    length,
    power,
    speed,
    temperature,
    volume_flow,
    volume,
    density,
    emissions_factors,
    moisture_vapor_resistance,
)


def _is_unit_class(cls):
    # type: (type) -> bool
    """Return True if the type is a Unit."""
    return hasattr(cls, "__symbol__") and hasattr(cls, "__factors__")


def _build_alias_dict(_module):
    # type: (ModuleType) -> Dict[str, str]
    """Create a dict of all the unit-type class's aliases. ie: {"F": "F", "DEG-F": "F", ...}

    Arguments:
    ----------
        * _module (ModuleType): The module to read the classes of.

    Returns:
    --------
        * (Dict[str, str]): A dict of all the unit-type aliases.
    """
    d = {}
    for unit_class in _module.__dict__.values():
        if not _is_unit_class(unit_class):
            continue

        d[unit_class.__symbol__] = unit_class.__symbol__
        for alias in unit_class.__aliases__:
            d[alias] = unit_class.__symbol__
    return d


def build_unit_type_dicts():
    # type: () -> Tuple[Dict[str, Base_UnitType], Dict[str, str]]
    """Returns dicts of all the unit-type conversion factor classes and aliases.

    Arguments:
    ----------
        * (None):

    Returns:
    --------
        * Tuple
            * (Dict[str, Base_UnitType]): A dict of all the unit-types, organized
                by the class's __symbol__ as the key.
            * (Dict[str, str]): A dict of all the unit-type alias values.
    """

    unit_type_dict = {}  # type: Dict[str, Base_UnitType]
    unit_type_alias_dict = {}  # type: Dict[str, str]

    for unit_module in UNIT_TYPE_MODULES:
        d = {}
        for unit_class in unit_module.__dict__.values():
            if not _is_unit_class(unit_class):
                continue

            # -- Add the base unit-type class to the dict.
            d[unit_class.__symbol__] = unit_class

            # -- Add the type's aliases to the dict as well.
            for alias in unit_class.__aliases__:
                d[alias] = unit_class

        unit_type_dict.update(d)
        unit_type_alias_dict.update(_build_alias_dict(unit_module))

    return (unit_type_dict, unit_type_alias_dict)
