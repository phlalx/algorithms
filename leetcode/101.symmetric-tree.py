# TODO iterative
#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.30%)
# Likes:    2782
# Dislikes: 61
# Total Accepted:    484.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def mirror(a, b):
    if a is None and b is None:
        return True
    elif a is not None and b is not None and a.val == b.val:
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    else:
        return False

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return mirror(root.left, root.right)

# @lc code=end

