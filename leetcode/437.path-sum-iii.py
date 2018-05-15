#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (43.60%)
# Likes:    2340
# Dislikes: 147
# Total Accepted:    131.9K
# Total Submissions: 299K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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

#TAGS cool, classic
# go through all paths of the tree
# TODO can we do without "nonlocal res" here?
# Complexity n * height(tree)
# Generalize target sum for a list

class Solution:

    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0
        prefix = [0]
        res = 0
        # invariant: prefix contains the prefix sums below node
        def walk(node, prefix):
            if node is not None:
                nonlocal res
                cur_sum = prefix[-1] + node.val
                res += prefix.count(cur_sum - target)
                prefix.append(cur_sum)
                walk(node.left, prefix)
                walk(node.right, prefix)
                prefix.pop()
        walk(root, prefix)
        return res

# @lc code=end

