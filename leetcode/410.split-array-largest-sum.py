#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (42.85%)
# Likes:    1337
# Dislikes: 75
# Total Accepted:    73K
# Total Submissions: 167.6K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
#
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#
#

# @lc code=start

# from itertools import accumulate
# TAGS dp (straightforward), binary search
# TODO can we put the sum computation into the DP?

# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         sums = [0] + list(accumulate(nums))
#         # sums[j] - sums[i] = sum[nums[i:j]]

#         memo = {}
#         def f(i, m):
#             res = memo.get((i,m))
#             if res is not None:
#                 return res
#             if m == 1:
#                 res = sums[n] - sums[i]
#             elif i == n:
#                 res = 0
#             else:
#                 res = min(max(sums[j] - sums[i], f(j, m-1)) for j in range(i, n))
#             memo[(i,m)] = res
#             return res

#         return f(0, m)

# In the dp solution, we didn't rely on the positivenss of the elements
# positive sum => monoticity => binary search
# But how to use binary search in this context?
#   binary search the solution!


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        assert nums
        # this could be an Easy problem, return True iff the array can be
        # split in less than m parts with sum less than x
        def is_sol(x):
            k = 1
            cur_sum = 0
            for v in nums:
                if v > x:
                    return False
                if cur_sum + v > x:
                    k += 1
                    cur_sum = 0
                cur_sum += v
            return k <= m

        i = max(nums)
        j = sum(nums)
        # there is always a solution
        # we don't use bisect because the interface isn't generic enough
        while i < j:
            mid = (i + j) // 2
            if is_sol(mid):
                j = mid
            else:
                i = mid + 1
        return i

# @lc code=end

