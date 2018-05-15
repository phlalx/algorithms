#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (36.45%)
# Likes:    443
# Dislikes: 47
# Total Accepted:    31.1K
# Total Submissions: 84.3K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
#
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
#
# Example 1:
#
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
#
# Example 2:
#
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Note:
#
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
#
#
#

# @lc code=start
# split array in 4 equal parts
# Brute force using masks TLE
# TAGS
# particular case of 698

# class Solution:
#     def makesquare(self, nums: List[int]) -> bool:
#         if not nums:
#             return False
#         l, r = divmod(sum(nums), 4)
#         if r != 0:
#             return False
#         n = len(nums)
#         ALL = 2 ** n - 1
#         def sum_sticks(x):
#             res = 0
#             for i in range(n):
#                 if x % 2 == 1:
#                     res += nums[i]
#                 x //= 2
#             return res
#         memo = {}
#         def f(stick_avail, num):
#             res = memo.get((stick_avail, num))
#             if res is not None:
#                 return res
#             res = False
#             if num == 1:
#                 res = sum_sticks(stick_avail) == l
#             else:
#                 for x in range(ALL + 1):
#                     s = sum_sticks(x & stick_avail)
#                     if s == l and f((~x) & stick_avail, num - 1):
#                         # print(stick_avail, num)
#                         res = True
#                         break
#             memo[(stick_avail, num)] = res
#             return res
#         return f(ALL, 4)

#TAGS dp
# quite similar to zero-sum-subset (or 2-partition)
#  

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        k = 4
        l, r = divmod(sum(nums), k)
        if r != 0:
            return False
        n = len(nums)
        memo = {}
        def f(i, x):
            res = memo.get((i, x))
            if res is not None:
                return res
            if i == n:
                res = all(y == l for y in x)
            else:
                res = False
                for j in range(k):
                    if x[j] + nums[i] <= l:
                        xx = list(x)
                        xx[j] += + nums[i]
                        if f(i+1, tuple(xx)):
                            res = True
                            break
            memo[(i, x)] = res
            return res
        return f(0, (0,) * k)

# @lc code=end

