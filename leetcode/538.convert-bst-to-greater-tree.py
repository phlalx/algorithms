# TAGS bst
#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (52.21%)
# Likes:    1520
# Dislikes: 98
# Total Accepted:    97.1K
# Total Submissions: 184.4K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
#
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def f(tree):
            nonlocal cur_sum
            if tree is not None:
                f(tree.right)
                tree.val += cur_sum
                cur_sum = tree.val
                f(tree.left)
        f(root)
        return root

# @lc code=end

