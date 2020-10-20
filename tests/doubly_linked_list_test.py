# -*- coding: utf-8 -*-

import unittest

from lrucache_interview import DoublyLinkedList, DoublyLinkedListNode


class TestDoublyLinkedList(unittest.TestCase):
    def test_remove_item_when_head(self):
        llist = DoublyLinkedList()

        first_node = llist.new_list_node(key="a", value=1234)
        llist.set_head(first_node)

        second_node = llist.new_list_node(key="b", value=1234)
        llist.set_head(second_node)

        # (b -> a -> None)
        assert llist.head == second_node
        assert llist.tail == first_node

        second_node.remove()

        # (a -> None)
        assert llist.head == first_node
        assert llist.tail == first_node
    
    def test_remove_item_when_tail(self):
        llist = DoublyLinkedList()

        first_node = llist.new_list_node(key="a", value=1234)
        llist.set_head(first_node)

        second_node = llist.new_list_node(key="b", value=1234)
        llist.set_head(second_node)

        # (b -> a -> None)
        assert llist.head == second_node
        assert llist.tail == first_node

        first_node.remove()

        # (b -> None)
        assert llist.head == second_node
        assert llist.tail == second_node
    
    def test_remove_item_when_middle(self):
        llist = DoublyLinkedList()

        tail_node = llist.new_list_node(key="a", value=1234)
        llist.set_head(tail_node)

        middle_node = llist.new_list_node(key="b", value=1234)
        llist.set_head(middle_node)

        head_node = llist.new_list_node(key="c", value=1234)
        llist.set_head(head_node)

        # (c -> b -> a -> None)
        assert llist.head == head_node
        assert llist.tail == tail_node
        assert llist.head.next == middle_node

        middle_node.remove()

        # (c -> a -> None)
        assert llist.head == head_node
        assert llist.tail == tail_node
        assert llist.head.next == tail_node
