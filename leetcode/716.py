#TAGS datastructure
# TODO figure out this solution https://leetcode.com/problems/max-stack/discuss/108962/C%2B%2B-O(logN)-for-write-ops-O(1)-for-reads

# can be seen as an stack + popmax (O(n))
# or a heapq of double-linked nodes
#   pop implemented as lazy removal

import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.deleted = False
    
def insert_after(node, n):
    n.left = node
    n.right = node.right
    node.right = n
    n.right.left = n

def delete(node):
    node.right.left = node.left
    node.left.right = node.right
    node.deleted = True
        
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hp = []
        self.dq = Node(None)
        self.dq.left = self.dq
        self.dq.right = self.dq
        self.counter = 0
        
    def _gc_heap(self):
      hp = self.hp
      while hp and hp[0][2].deleted:
        heapq.heappop(hp)
        
    def push(self, x: int) -> None:
      v = Node(x)
      insert_after(self.dq.left, v)  # insert after last
      heapq.heappush(self.hp, (-x, -self.counter, v))
      self.counter += 1

    def pop(self) -> int:
      v = self.dq.left
      res = v.val
      delete(v)
      return res

    def top(self) -> int:
      v = self.dq.left
      res = v.val
      return res
        
    def peekMax(self) -> int:
      self._gc_heap()
      v, _, _  = self.hp[0]
      return -v

    def popMax(self) -> int:
      self._gc_heap()
      _, _, v  = heapq.heappop(self.hp)
      res = v.val
      delete(v)
      return res
