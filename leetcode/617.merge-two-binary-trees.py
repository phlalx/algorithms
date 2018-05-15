#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (71.08%)
# Likes:    2170
# Dislikes: 147
# Total Accepted:    222.5K
# Total Submissions: 310.6K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
#
# Input:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# Output:
# Merged tree:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
#
#
# Note: The merging process must start from the root nodes of both trees.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def add(t1, t2):
    if t1 is None:
        return t2
    elif t2 is None:
        return t1
    else:
        res = TreeNode(t1.val + t2.val)
        res.left = add(t1.left, t2.left)
        res.right = add(t1.right, t2.right)
        return res

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return add(t1, t2)


# @lc code=end

