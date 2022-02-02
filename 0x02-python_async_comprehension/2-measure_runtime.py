#!/usr/bin/env python3
"""2-measure_runtime"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
    using asyncio.gather

    Returns:
        float: time elapsed
    """
    start = time.perf_counter()
    tasks = []
    for _ in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    stop = time.perf_counter()
    return stop - start
