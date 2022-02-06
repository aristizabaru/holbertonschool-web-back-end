#!/usr/bin/python3
"""0-basic_cache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """creates a basic cache system without limit

   methods:
        put(key, item): adds a key/value pair to cache
        get(key): gets the key value from cache
    """

    def put(self, key, item):
        if(key is None or item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        if(key is None or key not in self.cache_data.keys()):
            return
        return self.cache_data.get(key)
