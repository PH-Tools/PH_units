# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-
# T
from ph_units.unit_types._base import Base_UnitType


class MeterSquare(Base_UnitType):
    """Meter Square"""

    __symbol__ = "M2"
    __aliases__ = ["SM", "SQM", "SQ.M", "SQ-M", "SQ-METER", "SQ-METERS", "M²", "m²"]
    __factors__ = {
        "M2": "{}*1",
        "CM2": "{}*10_000",
        "MM2": "{}*1_000_000",
        "FT2": "{}*10.76391042",
        "IN2": "{}*1550.0031",
    }


class CentimeterSquare(Base_UnitType):
    """Centimeter Square"""

    __symbol__ = "CM2"
    __aliases__ = [
        "SQCM",
        "SQ.CM",
        "SQ-CM",
        "SQ-CENTIMETER",
        "SQ-CENTIMETERS",
        "CM²",
        "cm²",
    ]
    __factors__ = {
        "MM2": "{}*100",
        "CM2": "{}*1",
        "M2": "{}*0.0001",
        "FT2": "{}*0.001076391042",
        "IN2": "{}*0.15500031",
    }


class MillimeterSquare(Base_UnitType):
    """Millimeter Square"""

    __symbol__ = "MM2"
    __aliases__ = [
        "SQMM",
        "SQ.MM",
        "SQ-MM",
        "SQ-MILLIMETER",
        "SQ-MILLIMETERS",
        "MM²",
        "mm²",
    ]
    __factors__ = {
        "MM2": "{}*1",
        "CM2": "{}*0.01",
        "M2": "{}*0.000001",
        "FT2": "{}*0.000010764",
        "IN2": "{}*0.0015500031",
    }


class FootSquare(Base_UnitType):
    """Foot Square"""

    __symbol__ = "FT2"
    __aliases__ = [
        "SFT",
        "SF",
        "SQFT",
        "SQ.FT",
        "SQ-FT",
        "SQ-FOOT",
        "FT²",
        "ft²",
        "SQ-FEET",
    ]
    __factors__ = {
        "M2": "{}*0.092903",
        "CM2": "{}*929.0304",
        "MM2": "{}*92_903.04",
        "FT2": "{}*1",
        "IN2": "{}*144",
    }


class InchSquare(Base_UnitType):
    """Inch Square"""

    __symbol__ = "IN2"
    __aliases__ = [
        "SIN",
        "SI",
        "SQIN",
        "SQ.IN",
        "SQ-IN",
        "SQ-INCH",
        "IN²",
        "in²",
        "SQ-INCHES",
    ]
    __factors__ = {
        "M2": "{}*0.00064516",
        "CM2": "{}*6.4516",
        "MM2": "{}*645.16",
        "FT2": "{}*0.00694444",
        "IN2": "{}*1",
    }


# --- Concentrations ----------------------------------------------------------


class FootSquarePerPerson(Base_UnitType):
    """Foot Square Per Person"""

    __symbol__ = "FT2/PERSON"
    __aliases__ = [
        "FT2-PERSON",
        "FT²/PERSON",
    ]
    __factors__ = {"M2/PERSON": "{}*0.09290304", "FT2/PERSON": "{}*1"}


class CostPerFootSquared(Base_UnitType):
    """Cost Per Foot Squared"""

    __symbol__ = "COST/FT2"
    __aliases__ = [
        "COST-FT2",
        "COST/FT²",
    ]
    __factors__ = {"COST/M2": "{}*10.76391042", "COST/FT2": "{}*1"}


class CostPerMeterSquared(Base_UnitType):
    """Cost Per Meter Squared"""

    __symbol__ = "COST/M2"
    __aliases__ = [
        "COST-M2",
        "COST/M²",
    ]
    __factors__ = {"COST/M2": "{}*1", "COST/FT2": "{}*0.09290304"}
