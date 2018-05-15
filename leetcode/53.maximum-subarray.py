# TAGS kadane, divide and conquer
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.45%)
# Likes:    5229
# Dislikes: 208
# Total Accepted:    651K
# Total Submissions: 1.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start

# Version 1: Kadane

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert nums
        cur_sum = 0
        cur_min_sum = 0
        res = float('-inf')
        for v in nums:
            cur_sum += v
            res = max(res, cur_sum - cur_min_sum)
            cur_min_sum = min(cur_min_sum, cur_sum)
        return res

# Version 2: Divide and Conquer
# Trick: prefix sum, then it's obvious
#        just look for biggest difference using divide/conquer
#
#        Note: when we compute the prefix sums, it looks like the stock
#              problem

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n  = len(nums)
        ps = [0] * (n+1)
        for i in range(n):
            ps[i+1] = ps[i] + nums[i]


        def f(i, j):
            # best subarray with  bounds in [i,j]
            # min
            # max
            if i == j:
                return nums[i], ps[i], ps[i+1]
            else:
                m = (i + j) // 2
                best1, mi1, ma1 = f(i, m)
                best2, mi2, ma2 = f(m+1, j)
                return  max(best1, best2, ma2 - mi1),  min(mi1, mi2), max(ma1,  ma2)

        res, _, _ = f(0, n-1)

        return res


# The right way of seeing it
# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert nums
        res = float('-inf')
        cur = 0
        for v in nums:
            cur = max(v, cur + v)
            res = max(res, cur)
        return res

# @lc code=end

