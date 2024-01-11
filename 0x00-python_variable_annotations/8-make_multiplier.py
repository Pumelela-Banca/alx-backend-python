#!/usr/bin/python3
"""
makes a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function """
    def func(n: float) -> float:
        """ Return the multiplication of a float with multiplier """
        return n * multiplier

    return func
