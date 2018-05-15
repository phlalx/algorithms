#TAGS DS, cache
# see 146, 432
# https://leetcode.com/problems/lfu-cache/discuss/312189/Python3-O(1)-solution-using-OrderedDict-(doubly-linked-list-%2B-hashmap)
#
# First idea, augment hashmap with priority queue (just like LRU but PQ
# instead of de list) because we want to be able to compute the min of all
# element frequency, but quite hard do implement
#
# Second idea, we don't need the full power of a priority queue, because we
# always insert at one side, and the key increase is only by one increment.
# We can maintain a sorted de list but there is still a problem, what
# if several elements have the same frequency?
#
# So we keep a dequeue of node, each node is a dequeue of key/values.
#
# In python, we can use OrderedDict for de queue
#
# TODO finish this

class Node:
    def __init__(self, key=None, val=None, l=None, r=None):
        self.key = key
        self.val = val
        self.count = 1
        self.l = l
        self.r = r

# We could define a class Queue

def emptyqueue():
    n = Node()
    n.l = n  # first element of the list
    n.r = n  # last element,  n.l == n.r means the list is empty
    return n

def appendleft(q, n):
    tmp = q.r
    q.r = n
    n.r = tmp
    n.l = q

def popleft(q):
    n = q.r
    q.r = q.r.r
    q.r.l = q
    return n

def increase(q, n):
    succ = n
    n.count += 1
    if succ != q and n.count > succ.count:
        left = n.l
        right = succ.r
        n.r = right
        succ.l = left
        succ.r = n
        n.l = succ
        succ.r = n

class LFUCache:

    def __init__(self, capacity: int):
        self.q = emptyqueue()
        self.capacity = capacity
        self.num = 0
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        increase(self.q, n)
        return n.val

    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:  # weird corner case
            return
        if key in self.d:
            n = self.d[key]
            n.val = val
            increase(self.q, n)
            return
        if self.num >= self.capacity:
            n = popleft(self.q)
            del self.d[n.key]
            self.capacity -= 1
        self.num += 1
        n = Node(key, val)
        appendleft(self.q, n)
        self.d[key] = n


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
