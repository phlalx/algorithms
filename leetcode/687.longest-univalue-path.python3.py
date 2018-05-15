# TAGS binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# returns couple (a, b, c) where:
#  a is the longest univalue path
#  b is the longest univalue branch from root
#  c is the root value
# def f(tree):
#     if tree is None:
#         return float('-inf'), None, None

#     la, lb, lc = f(tree.left)
#     ra, rb, rc = f(tree.right)

#     a = 0
#     b = 0
#     c = tree.val
#     if lc == tree.val:
#        b = 1 + lb
#        a = 1 + lb
#     if rc == tree.val:
#        b = max(b, 1 + rb)
#        a = a + 1 + rb
#     a = max(a, la, ra)
#     return a, b, c


def f(tree):
    if tree is None:
        return (0, None, 0)
    else:
        a, r1, c = f(tree.left)
        u, r2, w = f(tree.right)
        c1 = 1 + c if tree.val == r1 else 0
        w1 = 1 + w if tree.val == r2 else 0
        l = c1 + w1
        return (max(l, a, u), tree.val, max(c1, w1))


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return f(root)[0]
