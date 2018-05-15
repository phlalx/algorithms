#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (48.08%)
# Likes:    1574
# Dislikes: 360
# Total Accepted:    125.4K
# Total Submissions: 255.7K
# Testcase Example:  '[0,0,0,0]'
#
#
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
#
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
#
#
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
#
#
#
# Note:
#
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
#
#
#
#TAGS simple dp

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a = cost[n-1]
        b = 0
        for i in reversed(range(n-1)):
            a, b = cost[i] + min(a, b), a
        return min(a, b)

# @lc code=end

