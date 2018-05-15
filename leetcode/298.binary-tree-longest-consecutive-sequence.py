# TAGS easy, dfs, tree
#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (44.72%)
# Likes:    348
# Dislikes: 86
# Total Accepted:    66K
# Total Submissions: 147.4K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# Given a binary tree, find the length of the longest consecutive sequence
# path.
# 
# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The longest consecutive path
# need to be from parent to child (cannot be the reverse).
# 
# Example 1:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   / \
# ⁠  2   4
# ⁠       \
# ⁠        5
# 
# Output: 3
# 
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# 
# Example 2:
# 
# 
# Input:
# 
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠   / 
# ⁠  2    
# ⁠ / 
# ⁠1
# 
# Output: 2 
# 
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# seq is the longuest sequence ending in root

def f(root, seq):
    if root.left is not None:
        seq_left = 1 if root.left.val != root.val + 1 else seq + 1
        f(root.left, seq_left)
    if root.right is not None:
        seq_right = 1 if root.right.val != root.val + 1 else seq + 1
        f(root.left, seq_right)


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = float('-inf')
        def f(root, seq):
            nonlocal res
            res = max(res, seq)
            if root.left is not None:
                seq_left = 1 if root.left.val != root.val + 1 else seq + 1
                f(root.left, seq_left)
            if root.right is not None:
                seq_right = 1 if root.right.val != root.val + 1 else seq + 1
                f(root.right, seq_right)
        f(root, 1)
        return res

        

