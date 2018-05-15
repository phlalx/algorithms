#TAGS easy, dfs, deep copy

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):

        seen = {}

        def copy(node):
            if node is None:
                return None
            cnode = seen.get(id(node))
            if cnode is not None:
                return cnode
            res = Node(node.val, None, None)
            seen[id(node)] = res  # memoize BEFORE recursive call
            res.next = copy(node.next)
            res.random = copy(node.random)
            return res

        return copy(head)
