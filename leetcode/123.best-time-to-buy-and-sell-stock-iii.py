#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (34.68%)
# Likes:    1378
# Dislikes: 58
# Total Accepted:    169.9K
# Total Submissions: 485.3K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
#
# Example 2:
#
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
#
#
# Example 3:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#

# tags dp
#
# 1. idea generalize to k transaction
# 2. write dp formula O(k.n^2)
#
# Let f(i, k) be the best score at i with at most k transactions
#
# f(i, k) = max( f(i-1, k),
#                max(prices[i] - prices[j] + f(j, k-1)),  j < i)
# f(0, k) = 0
# f(i, 0) = 0
#
# 3. Optimize the formula (trick)
#
# One can rewrite the formula
#
# f(i, k) = max( f(i-1, k),
#                prices[i] - min(prices[j] - f(j, k-1)),  j < i)
#
# And we realize that the min can be incrementally computed. This is the
# Same optimization we have in the case with only one transaction.
#
# 4. Space optimization TODO


# @lc code=start
#
# Non-optimized solution TLE
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         memo = [[ 0 for _ in range(3) ] for _ in range(n) ]
#         for k in range(1, 3):
#             for i in range(1, n):
#                 res = max(prices[i] - prices[j] + memo[j][k-1] for j in range(i))
#                 res = max(res, memo[i-1][k])
#                 memo[i][k] = res
#         return memo[n-1][2]

# Time complexity is now O(k.n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        memo = [[ 0 for _ in range(3) ] for _ in range(n) ]
        for k in range(1, 3):
            cur_min = prices[0]
            for i in range(1, n):
                cur_min = min(cur_min, prices[i-1] - memo[i-1][k-1])
                memo[i][k] = max(prices[i] - cur_min, memo[i-1][k])
        return memo[n-1][2]
# @lc code=end

