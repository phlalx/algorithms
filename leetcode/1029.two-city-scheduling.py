#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (54.27%)
# Likes:    632
# Dislikes: 89
# Total Accepted:    27.1K
# Total Submissions: 48.6K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
#
#
#
# Example 1:
#
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
#
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
#
#
#
#
# Note:
#
#
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000
#
#

#TAGS dp

# @lc code=start
class Solution:
    
    # recursive sollution
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = {}
        def f(i, a):  # place `a` passengers in city 0,  for cities in [i:]
            if (i, a) in memo:
                return memo[(i, a)]
            if i == n:
                res = 0 if a == 0 else float('inf')
            else:
                res = costs[i][1] + f(i+1, a)
                if a > 0:
                    res = min(res,costs[i][0] + f(i+1, a - 1))
            memo[(i, a)] = res
            return res
        a = n // 2
        return f(0, a)

    # same things + iterative MUCH more tedious
    # still not the right solution, 5.8%
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        cities = n // 2
        memo = [[0] + cities * [ float('inf') ] for i in range(n+1)]
        for i in range(1, n+1):
            memo[i][0] = memo[i-1][0] + costs[i-1][1]
        for i in range(1, n+1):
            for a in range(1, min(i+1, cities+1)):
                memo[i][a] = min(memo[i-1][a] + costs[i-1][1], memo[i-1][a-1] + costs[i-1][0])
        return memo[n][cities]


            
            

# @lc code=end

