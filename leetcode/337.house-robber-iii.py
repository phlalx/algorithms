# TAGS tree, walk
#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (48.81%)
# Likes:    1747
# Dislikes: 35
# Total Accepted:    115.4K
# Total Submissions: 236.3K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# 
# Input: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# quite interesting
# my  initial solution was to compute
# f(node, robbed) with robbed == True if and only parent  was robbed
# but this led to an exponential solution, or sub-optimal when using memoization
# the right solution is that f(node) returns values when robbed, and not robbed

class Solution:
    def rob(self, root: TreeNode) -> int:
        #  return (a, b) where a is best value if parent was robbed
        #                and b is best value if parent wasn't robbed
        def f(node):
            if node is None:
                return 0, 0
            a, b = f(node.left)
            aa, bb = f(node.right)
            return b + bb, max(node.val + a  +  aa, b +  bb)
        a, b = f(root)
        return max(a, b)
# @lc code=end

