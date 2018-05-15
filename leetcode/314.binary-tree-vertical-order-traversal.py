# TAGS tree, bfs
# Be careful of order of elements (upper elts are displayed first)
#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (41.80%)
# Likes:    645
# Dislikes: 123
# Total Accepted:    81.8K
# Total Submissions: 195.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the vertical order traversal of its nodes'
# values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to
# right.
#
# Examples 1:
#
#
# Input: [3,9,20,null,null,15,7]
#
# ⁠  3
# ⁠ /\
# ⁠/  \
# ⁠9  20
# ⁠   /\
# ⁠  /  \
# ⁠ 15   7
#
# Output:
#
# [
# ⁠ [9],
# ⁠ [3,15],
# ⁠ [20],
# ⁠ [7]
# ]
#
#
# Examples 2:
#
#
# Input: [3,9,8,4,0,1,7]
#
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
#
# Output:
#
# [
# ⁠ [4],
# ⁠ [9],
# ⁠ [3,0,1],
# ⁠ [8],
# ⁠ [7]
# ]
#
#
# Examples 3:
#
#
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
# child is 5)
#
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
# ⁠   /\
# ⁠  /  \
# ⁠  5   2
#
# Output:
#
# [
# ⁠ [4],
# ⁠ [9,5],
# ⁠ [3,0,1],
# ⁠ [8,2],
# ⁠ [7]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

# BUG
# class Solution:
#     def verticalOrder(self, root: TreeNode) -> List[List[int]]:

#         d = defaultdict(list)
#         def f(node, x, height):
#             if node is None:
#                 return
#             d[x].append((height, node.val))
#             f(node.left, x-1, height+1)
#             f(node.right, x+1, height+1)

#         f(root, 0, 0)
#         res = []
#         for k in sorted(list(d.keys())):
#             l = d[k]
#             l.sort()
#             l = [x[1] for x in l]
#             res.append(l)
#         return res

from collections import deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        d = defaultdict(list)
        s = deque([(root, 0)])

        while s:
            n, shift = s.popleft()
            d[shift].append(n.val)
            if n.left:
                s.append((n.left, shift-1))
            if n.right:
                s.append((n.right, shift+1))

        res = []
        for k in sorted(list(d.keys())):
            l = d[k]
            res.append(l)
        return res
