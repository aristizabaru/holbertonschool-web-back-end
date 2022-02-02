#!/usr/bin/env python3
"""3-tasks"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create a routine task from wait_random(max_delay)
    and return it

    Args:
        max_delay (int): max delay in seconds

    Returns:
        asyncio.Task: new task from wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
