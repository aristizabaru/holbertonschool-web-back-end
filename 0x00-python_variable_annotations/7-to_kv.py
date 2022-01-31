#!/usr/bin/env python3
"""takes a 'str' and a number and returns a tuple of both"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a 'str' and a number and returns a tuple of both

    Args:
        k (str): string argument
        v (Union[int, float]): int or float argument

    Returns:
        Tuple[str, float]: tuple with the str and the square of v
    """
    return (k, v ** 2)
