#!/usr/bin/python3
"""4-mru_cache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """creates a MRUCache cache system without limit

   methods:
        put(key, item): adds a key/value pair to cache
        get(key): gets the key value from cache
    """

    def __init__(self):
        """init object"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if(key is None or item is None):
            return
        if(len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = list(self.cache_data.keys())[
                BaseCaching.MAX_ITEMS - 1]
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))
        if(key in self.cache_data.keys()):
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if(key is None or key not in self.cache_data.keys()):
            return
        item = self.cache_data[key]
        self.put(key, item)
        return self.cache_data.get(key)
