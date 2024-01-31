#!/usr/bin/python3
"""import BaseCaching class"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache caching implementation"""
    dic = {}
    def put(self, key, item):
        """put data into the cache"""
        if key and item and len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
        elif key and item and key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.dic.pop(key)
            self.dic[key] = 1
            self.cache_data[key] = item
        elif key and item:
            self.dic = dict(sorted(self.dic.items(), key=lambda item: item[1]))
            r = list(self.dic.keys())[0]
            self.cache_data.pop(r)
            self.dic.pop(r)
            print("DISCARD: {}".format(r))
            self.cache_data[key] = item
        if key in self.dic:
            self.dic[key] += 1
        else:
            self.dic[key] = 1

    def get(self, key):
        """get data from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        v = self.cache_data[key]
        self.cache_data.pop(key)
        self.cache_data[key] = v
        self.dic[key] += 1
        return self.cache_data[key]
