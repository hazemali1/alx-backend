#!/usr/bin/python3
"""import BaseCaching class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache caching implementation"""
    def put(self, key, item):
        """put data into the cache"""
        if key and item and len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
        elif key and item and key in self.cache_data.keys():
            self.cache_data[key] = item
        elif key and item:
            r = list(self.cache_data.keys())[-1]
            self.cache_data.pop(r)
            print("DISCARD: {}".format(r))
            self.cache_data[key] = item

    def get(self, key):
        """get data from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
