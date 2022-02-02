#!/usr/bin/env python3
"""0-async_generator"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """yield a random number between 0 and 10 asynchronously

    Returns:
        float: float number between 0 and 10

    Yields:
        Iterator[float]: next float number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
