#!/usr/bin/env python3
"""takes a float multiplier as argument and returns a
function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """t takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier

    Args:
        multiplier (float): argument to be kept in memmory

    Returns:
        Callable[[float], float]: function with float as argument
        and float as return
    """
    return lambda x: x * multiplier
