#!/usr/bin/env python3
"""web module"""
import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def counter(method: Callable) -> Callable:
    """ count how many request have been made
    """

    @wraps(method)
    def wrapper(url):
        """ Wrapper """
        r.incr("count:{}".format(url))
        cached_html = r.get("cached:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex("cached:{}".format(url), 10, html)
        return html

    return wrapper


@counter
def get_page(url: str) -> str:
    """ requests an URL and returns it.
    """
    req = requests.get(url)
    return req.text
