# TAGS binary search, cool

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def walk(root, target):
    if root is None:
        return None, float("+inf")
    if target > root.val:
        val, dist = walk(root.right, target)
    else:
        val, dist = walk(root.left, target)
    root_dist = abs(target - root.val)
    if root_dist < dist:
        val = root.val
        dist = root_dist
    return val, dist

# def walk(root, target):
#     cur = root
#     best_delta = float('inf')
#     res = None
#     while cur is not None:
#         delta = abs(target - cur.val)
#         if delta < best_delta:
#             best_delta = delta
#             res = cur.val
#         if target > cur.val:
#             cur = cur.right
#         else:
#             cur = cur.left
#     return res

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return walk(root, target)[0]
