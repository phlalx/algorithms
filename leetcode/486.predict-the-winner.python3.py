# TAGS dp
#

# simplest recursive
# from functools import lru_cache
# class solution:
#     def predictthewinner(self, nums):
#         """
#         :type nums: list[int]
#         :rtype: bool
#         """
#         assert nums
#         @lru_cache(maxsize=none)
#         # returns the score difference between first and second player
#         def f(i, j):
#             if i == j:
#                 res = 0
#             else:
#                 res = max(nums[i] - f(i+1, j), nums[j] - f(i, j-1))
#             return res
#         return f(0, len(nums) - 1) >= 0

# iterative with space optimization
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: list[int]
        :rtype: bool
        """
        assert nums
        # returns the score difference between first and second player
        n = len(nums)
        if n % 2 == 0:  # optim
            return True
        memo = [0] * n
        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                memo[j] = max(nums[i] - memo[j], nums[j] - memo[j - 1])
        return memo[n - 1] >= 0


# My initial version, not optimal
# f(i, j, player) returns best score achievable by player
#  assuming player True (resp. False) tries to maximize (resp. minimize)
#  its score
#         def f(i, j, player):
#             if i == j:
#                 res = 0
#             elif player:
#                 res = max(nums[i] + f(i+1, j, False), nums[j-1] + f(i, j-1, False))
#             else:
#                 res = min(-nums[i] + f(i+1, j, True), -nums[j-1] + f(i, j-1, True))
#             return res
#         return f(0, len(nums), True) >= 0
