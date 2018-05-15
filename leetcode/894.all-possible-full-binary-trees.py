#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (74.13%)
# Likes:    810
# Dislikes: 79
# Total Accepted:    34.2K
# Total Submissions: 46.1K
# Testcase Example:  '7'
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
#
# Return a list of all possible full binary trees with N nodes.  Each element
# of the answer is the root node of one possible tree.
#
# Each node of each tree in the answer must have node.val = 0.
#
# You may return the final list of trees in any order.
#
#
#
# Example 1:
#
#
# Input: 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
#
#
#
#
#
# Note:
#
#
# 1 <= N <= 20
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = [ [] for i in range(N+1) ]
        res[1].append(TreeNode())
        for i in range(2, N+1):
            for j in range(1, i):
                for e1 in res[j]:
                    for e2 in res[i - 1 - j]:
                        t = TreeNode(left=e1, right=e2)
                        res[i].append(t)
        return res[N]


# @lc code=end

