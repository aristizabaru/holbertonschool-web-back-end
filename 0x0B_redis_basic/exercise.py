#!/usr/bin/env python3
"""exercise module"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts how many times a function has been called
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs for a particular function
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper  """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function"""
    r = redis.Redis()
    function_name = fn.__qualname__
    number_calls = r.get(function_name)
    try:
        number_calls = number_calls.decode('utf-8')
    except Exception:
        number_calls = 0
    print('{} was called {} times:'.format(function_name, number_calls))

    inputs = r.lrange(function_name + ":inputs", 0, -1)
    outputs = r.lrange(function_name + ":outputs", 0, -1)

    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode('utf-8')
        except Exception:
            inp = ""
        try:
            outp = outp.decode('utf-8')
        except Exception:
            outp = ""

        print('{}(*{}) -> {}'.format(function_name, inp, outp))


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """init cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get value from redis"

        Args:
            key (str): key to get value from
            fn (Optional[Callable], optional): callable to convert
            the data back to the desired format. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: value from redis
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """get string value from redis

        Args:
            key (str): key to get value from

        Returns:
            str: value from redis
        """
        value = self._redis.get(key)

        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """"get int value from redis

        Args:
            key (str): key to get value from

        Returns:
            int: value from redis
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0

        return value
