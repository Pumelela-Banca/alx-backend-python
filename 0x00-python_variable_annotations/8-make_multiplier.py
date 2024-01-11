#!/usr/bin/python3
"""
makes a multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ Return a function """
    def func(n: float) -> float:
        """ Return the multiplication of a float with multiplier """
        return n * multiplier

    return func
