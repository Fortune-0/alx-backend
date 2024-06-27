#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    
    def __init__(self):
        """initilize BaseCache class
        """
        BaseCaching.__init__(self)
        # self.cache_data = {}
        
    def put(self, key, item):
        """
    Store an item in the cache with the given key.

    Parameters:
    key (str): The unique identifier for the item in the cache.
    item (object): The item to be stored in the cache.

    Returns:
    None
    """
        if key is not None and item is not None:
            self.cache_data[key] = item
            
    def get(self, key):
        """
        Retrieve an item from the cache with the given key.
        parameters.
        key (str): The unique identifier for the item in the cache.
        Returns:
        cache if the key exists, otherwise none
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
