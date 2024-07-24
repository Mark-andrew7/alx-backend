#!/usr/bin/python3
"""
class LRUCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache caching system that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.stack.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data[key]
