# TAGS datastructure, cool
import collections

# Since put and get are in O(1), we need a hashtable
# Then it has to be augmented with something else in order to implement
# Cache eviction in constant time.
#
# We don't store directly values in the cache, but Node containing values.
# The nodes are chained in a double-link list, so as to reflect the
# order of use.

# We need to data structures to define a deque
# A `Node` (value + two pointers), and the `Deque` itself
#
# For simplicity, we don't define a class `Deque`. A `Deque` is just
# a `Node`


class Node:
    def __init__(self, k=None, v=None, prev=None, next=None):
        self.k = k
        self.v = v
        self.prev = prev
        self.next = next


def create_deque():
    # an empty dequeue is a sentinel node that points to itself
    dq = Node()
    dq.next = dq
    dq.prev = dq
    return dq


def move_front(dq, n):
    n.prev.next = n.next
    n.next.prev = n.prev
    n.next = dq.next
    n.next.prev = n
    dq.next = n
    n.prev = dq


def push(dq, k, v):
    assert dq.v is None
    n = Node(k, v, dq, dq.next)
    dq.next = n
    n.next.prev = n
    return n


def back(dq):
    return dq.prev


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.m = dict()
        self.dq = create_deque()
        self.capacity = capacity
        self.num = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self.m.get(key)
        if n is None:
            return -1
        v = n.v
        move_front(self.dq, n)
        assert self.m.get(key)
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        n = self.m.get(key)
        if n is not None:
            n.v = value
            move_front(self.dq, n)
        elif self.num == self.capacity:
            n = back(self.dq)
            del self.m[n.k]
            n.k = key
            n.v = value
            move_front(self.dq, n)
            self.m[key] = n
        else:
            self.num += 1
            self.m[key] = push(self.dq, key, value)


# Based on ordered dict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.m = OrderedDict()
        self.capacity = capacity
        self.num = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        v = self.m.get(key)
        if v is None:
            return -1
        self.m.move_to_end(key)
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        v = self.m.get(key)
        if v is not None:
            self.m[key] = value
            self.m.move_to_end(key)
        elif self.num == self.capacity:
            first = next(iter(self.m.keys()))
            del self.m[first]
            self.m[key] = value
        else:
            self.num += 1
            self.m[key] = value

