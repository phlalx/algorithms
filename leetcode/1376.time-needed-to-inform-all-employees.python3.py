#TAGS dp
#
# Take away:
#  This would have been an easy top-down recursive problem, but I was caught
#  off-guard with this formulation. I didn't see that it could be solve
#  using DP. My first version was TLE because I didn't use memoization.
#   
#  The same technique could be used to compute "node values" from the leaves
#  to the node.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def numOfMinutes(self, n, headID, manager, informTime):
            time = [None] * n
            def total_inform_time(i):
                res = time[i]
                if res is not None:
                    return res
                if manager[i] == -1:
                    res = 0
                else:
                    res = informTime[manager[i]] + total_inform_time(manager[i])
                time[i] = res
                return res

            return max(total_inform_time(i) for i in range(n))
        
