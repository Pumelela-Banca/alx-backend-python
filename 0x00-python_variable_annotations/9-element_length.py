#!/usr/bin/env python3
"""
multiple annotations
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns multiple annotations
    """
    return [(i, len(i)) for i in lst]
