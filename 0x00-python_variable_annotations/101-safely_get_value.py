#!/usr/bin/env python3
"""module safely get value"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """return dct[key] if it exists, otherwise return `default`

    Args:
        dct (Mapping): dictionary
        key (Any): any given value
        default (Union[T, None], optional): [description]. Defaults to None.

    Returns:
        Union[Any, T]: returns key or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
