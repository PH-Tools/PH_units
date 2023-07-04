# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

from ph_units.unit_types._base import Base_UnitType


class WUFI_Vapor_Diffusion_Resistance_Factor(Base_UnitType):
    """MNS/G"""

    __symbol__ = "WUFI_MEW"
    __aliases__ = []
    __factors__ = {
        "WUFI_MEW": "{}*1",
        "-": "{}*1",
        "PERM-IN": "(1/{})/0.007763975",
    }


class Perm_Inch(Base_UnitType):
    """PERM-IN"""

    __symbol__ = "PERM-IN"
    __aliases__ = ["PERMIN", "PERM-INCH", "PERM-INCHES"]
    __factors__ = {
        "WUFI_MEW": "1/({}*0.007763975)",
        "PERM-IN": "{}*1",
    }
