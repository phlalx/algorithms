# TAGS binary tree, hashtable

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


def walk(tree, cur, l):
    if tree is None:
        return
    l[cur].append(tree.val)
    walk(tree.left, cur + 1, l)
    walk(tree.right, cur + 1, l)


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        l = collections.defaultdict(list)
        walk(root, 0, l)
        return [sum(x) / len(x) for x in l.values()]
