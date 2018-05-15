# TAGS bst, cool, todo broken
# also see 426

# idea, walk tree while maintaining prev seen value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def walk(t):
    global prev, cur_min
    if t is None:
        return
    walk(t.left)
    if t.val - prev < cur_min:
        cur_min = t.val - prev
    prev = t.val
    walk(t.right)


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global cur_min, prev
        cur_min = float("inf")
        prev = -float("inf")
        walk(root)
        return cur_min


# Solution 2, without global variables
#
# not sure it can work this way, we don't get the right value
# for prev when unstacking the recursive calls
#
# def walk(prev, t):  # prev is the last value seen
#     res = t.val - prev
#     if t.left:
#         # careful not to walk 'None',
#         # not sure how to define the base case
#         # for None
#         res = min(res, walk(prev, t.left))
#     if t.right:
#         res = min(res, walk(t.val, t.right))
#     return res


# class Solution:
#     def getMinimumDifference(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         prev = float("-inf")
#         return walk(prev, root)
