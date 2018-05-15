# TAGS dp
# TODO generalize to any cooldown k

# O(n^2) dp, TLE
#
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
#         memo = {}
#         def f(i, j):
#             if (i, j) in memo:
#                 return memo[i,j]
#             res = 0
#             if i >= j:
#                 res = 0
#             else:
#                 res = max(prices[j] - prices[i], 0)
#                 for k in range(i, j+1): # cooldown
#                     res = max(res, f(i,k-1) + f(k+1,j))
#             memo[i,j] = res
#             return res
#         return f(0, len(prices)-1)


class Solution:
    def maxProfit(self, prices):
        own = float("-inf")
        not_own = 0
        cooldown = 0
        for p in prices:
            own1 = max(cooldown - p, own)
            not_own1 = max(not_own, own + p)
            cooldown1 = max(cooldown, not_own)
            own, not_own, cooldown = own1, not_own1, cooldown1
        return max(not_own, cooldown)
