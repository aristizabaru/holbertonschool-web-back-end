#!/usr/bin/env python3
"""exercise module"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """init cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data to redis using a uuid4 as key

        Args:
            data (Union[str, bytes, int, float]): data to be stored

        Returns:
            str: uuid generated as key for the data
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
