#!/usr/bin/env python3
"""0-simple_helper_function module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """calculate the range of indexes to return in a list
    for the given pagination parameters

    Args:
        page (int): number of the page indexes to retrieve
        page_size (int): limit of the page

    Returns:
        Tuple[int, int]: start index and end index
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
