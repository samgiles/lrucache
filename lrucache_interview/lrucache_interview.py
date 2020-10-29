# -*- coding: utf-8 -*-

from .doubly_linked_list import DoublyLinkedList


class LRUCache(object):
    """
    This Least Recently Used Cache is an in memory key value cache with a fixed
    capacity.

    When the number of items in the cache reaches the capacity, the item that
    was used least recently of all cache items is evicted. This is tracked
    using a DoublyLinkedList. Each node of the list is stored in a map, when
    that index is accessed, the node is moved to the head of the list.
    When the cache is at capacity, the tail of the list is removed.

    `insert`, and `get` will always run in linear time with respect to the
    size of the cache.
    """
    def __init__(self, capacity):
        self.capacity = max(1, capacity)

        self.cache = {}
        self.cache_items = DoublyLinkedList()

    @property
    def current_size(self):
        return len(self.cache)

    def insert(self, key, value):
        if key not in self.cache:
            if self.current_size == self.capacity:
                self.evict_least_recent()
            self.cache[key] = self.cache_items.new_list_node(key, value)
        else:
            self.replace(key, value)
        self.update_most_recent(self.cache[key])

    def get(self, key):
        if key not in self.cache:
            return None

        lru_node = self.cache[key]
        self.update_most_recent(lru_node)

        return lru_node.value

    def replace(self, key, value):
        if key not in self.cache:
            raise Exception("Key not in cache")
        self.cache[key].value = value

    def update_most_recent(self, list_node):
        self.cache_items.set_head(list_node)

    def evict_least_recent(self):
        key_to_remove = self.cache_items.tail.key
        self.cache_items.remove_tail()
        del self.cache[key_to_remove]
