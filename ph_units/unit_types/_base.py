# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

""""""

try:
    from typing import Dict, List
except ImportError:
    pass  # Python 2.7


class Base_UnitType(object):
    """Protocol (base class) for all Unit-Type conversion factor classes"""

    __symbol__ = ""  # type: str
    __aliases__ = []  # type: List[str]
    __factors__ = {}  # type: Dict[str, str]
