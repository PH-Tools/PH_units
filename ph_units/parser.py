# -*- coding: utf-8 -*-
# -*- Python Version: 2.7 -*-

"""Function to parse input string from the user in numeric and 'unit' parts."""

try:
    from typing import Union, Optional, Tuple
except ImportError:
    pass  # IronPython 2.7

import re


def parse_input(_input_string):
    # type: (Union[str, int, float]) -> Tuple[str, Optional[str]]
    """Parse an input string into the 'value part' and the 'units part'.

    examples:
        '0.5 in' returns -> ('0.5', 'IN')
        '0.5" '  returns -> ('0.5', 'IN')
        '0.5'    returns -> ('0.5', None)
        0.5      returns -> ('0.5', None)
        '0.5Btu/hr-Ft2-F' returns -> ('0.5', 'BTU/HR-FT2-F')
    """

    # -- First, try and split the input string at the first alpha-character found
    # -- ie: the input string: "0.5 HR-FT2-F/BTU-IN" will get split at index=4
    # --                           ^
    # -- You can't just look for the numbers, since some units have numbers in them ('FT2', ...)
    # -- Exclude the '.' and '-' characters from the find so that float and
    # -- negative values don't cause an error.
    # --
    # -- https://regex101.com/

    input_string_cleaned = str(_input_string).strip().upper()
    input_string_cleaned = input_string_cleaned.replace("'", "FT").replace('"', "IN")

    # -------------------------------------------------------------------------
    # -- Find the alpha and the numeric parts
    rx = re.compile(r"[^\d.-]", re.IGNORECASE)
    match = rx.search(input_string_cleaned)
    if not match:
        # -- No alpha part, just return the numeric part
        return (input_string_cleaned, None)
    found_span = match.span()

    # -------------------------------------------------------------------------
    # -- Cleanup
    alpha_part = input_string_cleaned[found_span[0] :].strip()
    numeric_part = input_string_cleaned[: found_span[0]].strip()

    return numeric_part, alpha_part
