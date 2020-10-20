# -*- coding: utf-8 -*-


class DoublyLinkedListNode(object):
    def __init__(self, key, value, container):
        self.container_reference = container
        self.key = key
        self.value = value

        self.previous = None
        self.next = None

    def remove(self):
        """
        Remove this item from the linked list
        """
        if self.container_reference.head == self:
            self.container_reference.remove_head()
        elif self.container_reference.tail == self:
            self.container_reference.remove_tail()
        else:
            if self.previous is not None:
                self.previous.next = self.next
            if self.next is not None:
                self.next.previous = self.previous

        self.next = None
        self.previous = None

    def __repr__(self):
        return "{{{key}: {value}}}".format(key=self.key, value=self.value)


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def new_list_node(self, key, value):
        return DoublyLinkedListNode(key, value, self)

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

    def __repr__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(node)
            node = node.next
        return values.__repr__()
