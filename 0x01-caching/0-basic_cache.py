#!/usr/bin/python3
"""import BaseCaching class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching implementation"""
    def put(self, key, item):
        """put data into the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get data from the cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
