#!/usr/bin/env python3
"""
creates a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a new tuple
    """
    return k, v * v
