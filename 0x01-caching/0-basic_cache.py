#!/usr/bin/python3
"""import class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic"""
    def put(self, key, item):
        """put data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get data"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
