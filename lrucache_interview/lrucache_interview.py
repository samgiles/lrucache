# -*- coding: utf-8 -*-


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
        self.current_size = 0
        self.cache = {}
        self.most_recent_list = DoublyLinkedList()

    def insert(self, key, value):
        if key not in self.cache:
            if self.current_size == self.capacity:
                self.evict_least_recent()
            else:
                self.current_size += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
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
        self.most_recent_list.set_head(list_node)

    def evict_least_recent(self):
        key_to_remove = self.most_recent_list.tail.key
        self.most_recent_list.remove_tail()
        del self.cache[key_to_remove]


class DoublyLinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.previous = None
        self.next = None

    def remove(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous

        self.next = None
        self.previous = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.previous = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove()
            self.head.previous = node
            node.next = self.head
            self.head = node

    def remove_head(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.previous = None

    def remove_tail(self):
        if self.tail is None:
            return

        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.previous
        self.tail.next = None
