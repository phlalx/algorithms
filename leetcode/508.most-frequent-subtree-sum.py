# TAGS tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        count = Counter()

        def walk(tree):
            res1 = 0
            res2 = 0
            if tree.left is not None:
                res1 = walk(tree.left)
            if tree.right is not None:
                res2 = walk(tree.right)
            res = tree.val + res1 + res2
            count[res] += 1
            return res

        walk(root)

        m = max(count.values())
        return [ k for k, v in count.items() if v == m ]
