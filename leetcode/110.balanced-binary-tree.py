#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.66%)
# Likes:    1655
# Dislikes: 143
# Total Accepted:    385.1K
# Total Submissions: 910.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Error(Exception):
    pass

def f(root):
    if root is None:
        return 0
    a = f(root.left)
    b = f(root.right)
    if abs(a - b) > 1:
        raise Error
    return max(a, b) + 1

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        try:
            f(root)
            return True
        except Error:
            return False
        

# @lc code=end

