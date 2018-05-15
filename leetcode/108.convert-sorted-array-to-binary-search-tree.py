#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (52.49%)
# Likes:    1846
# Dislikes: 180
# Total Accepted:    350.3K
# Total Submissions: 634.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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

#TAGS bst
# 109

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def f(i, j):
            if i == j:
                return TreeNode(nums[i])
            elif i > j:
                return None
            else:
                m = (i + j) // 2
                res = TreeNode(nums[m], f(i, m-1), f(m+1, j))
                return res

        return f(0, len(nums) - 1)
        

# @lc code=end

