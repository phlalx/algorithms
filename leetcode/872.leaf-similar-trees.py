#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (63.86%)
# Likes:    533
# Dislikes: 27
# Total Accepted:    65.9K
# Total Submissions: 102.1K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
  '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
#
# Note:
#
#
# Both of the given trees will have between 1 and 100 nodes.
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(root, res):
            if root.left is None and root.right is None:
                res.append(root.val)
            else:
                if root.left is not None:
                    leaves(root.left, res)
                if root.right is not None:
                    leaves(root.right, res)

        res1 = []
        leaves(root1, res1)
        res2 = []
        leaves(root2, res2)
        return res1 == res2


# @lc code=end

