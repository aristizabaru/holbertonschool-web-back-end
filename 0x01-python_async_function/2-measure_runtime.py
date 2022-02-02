#!/usr/bin/env python3
"""2-measure_runtime"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time of wait_n execution

    Args:
        n (int): number of task to create
        max_delay (int): max delay in seconds

    Returns:
        float: time elapse per task
    """
    s = time.perf_counter()
    # run program and wait for its execution
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed/n
