# -*- coding: utf-8 -*-

import unittest

from lrucache_interview import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_cold_evict_lru(self):
        """
        When no key has been used, and therefore no particular key
        is the least recently used key, evict the oldest insert.
        """
        cache = LRUCache(capacity=2)

        cache.insert(key="a", value=1234)
        cache.insert(key="b", value=123)
        cache.insert(key="c", value=12)

        assert cache.get("a") is None
        assert cache.get("b") == 123
        assert cache.get("c") == 12

    def test_warm_evict_lru(self):
        """
        Evict the least recently used key
        """
        cache = LRUCache(capacity=3)
        cache.insert(key="a", value=1234)
        cache.insert(key="b", value=123)
        cache.insert(key="c", value=12)

        cache.get("c")
        cache.get("b")
        cache.get("a")

        cache.insert(key="d", value=1)

        assert cache.get("c") is None

        assert cache.get("d") == 1
        assert cache.get("b") == 123
        assert cache.get("a") == 1234
