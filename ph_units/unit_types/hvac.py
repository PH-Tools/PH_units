# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class ModifiedEnergyFactor(Base_UnitType):
    """MEF (Clothes Washers)
    
    A metric used to measure the energy efficiency of residential clothes washers,
    accounting for energy consumption during washing, drying (by considering moisture
    retention in clothes).
    A higher MEF indicates a more energy-efficient washer.

    The key difference between MEF and IMEF (Integrated Modified Energy Factor) is that IMEF is
    a more comprehensive metric, as it also includes standby and off-mode power consumption,
    making it a better representation of real-world energy use. IMEF replaced MEF
    as the primary efficiency metric in updated federal standards.
    """

    __symbol__ = "MEF"
    __aliases__ = []
    __factors__ = {
        "MEF": "{}*1",
        "IMEF": "0.503+{}*0.95",
    }


class IntegratedModifiedEnergyFactor(Base_UnitType):
    """IMEF (Clothes Washers)
    
    A metric used to measure the energy efficiency of residential clothes washers,
    accounting for energy consumption during washing, drying (by considering moisture
    retention in clothes), and standby/off-mode power usage.
    A higher IMEF indicates a more energy-efficient washer.

    The key difference between MEF and IMEF (Integrated Modified Energy Factor) is that IMEF is
    a more comprehensive metric, as it also includes standby and off-mode power consumption,
    making it a better representation of real-world energy use. IMEF replaced MEF
    as the primary efficiency metric in updated federal standards.
    """

    __symbol__ = "IMEF"
    __aliases__ = []
    __factors__ = {
        "MEF": "({}-0.503)/0.95",
        "IMEF": "{}*1",
    }
