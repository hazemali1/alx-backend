#!/usr/bin/python3
"""import class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic"""
    def put(self, key, item):
        """put data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return sself.cache_data.get(key)
