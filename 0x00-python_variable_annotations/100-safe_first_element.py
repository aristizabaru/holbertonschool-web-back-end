#!/usr/bin/env python3
"""safe first element module"""
from typing import Sequence, Any, Union

# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element of the list if there's any

    Args:
        lst (Sequence[Any]): a list with any value

    Returns:
        Union[Any, None]: any object or none
    """
    if lst:
        return lst[0]
    else:
        return None
