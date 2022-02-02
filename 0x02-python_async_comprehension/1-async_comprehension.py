#!/usr/bin/env python3
"""1-async_comprehension"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers

    Returns:
        List[float]: 10 random numbers from 0 to 10
    """
    return [i async for i in async_generator()]
