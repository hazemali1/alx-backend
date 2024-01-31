#!/usr/bin/python3
"""import class"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic"""
    def put(self, key, item):
        """put data"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
