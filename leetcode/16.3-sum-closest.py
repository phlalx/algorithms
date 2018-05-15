#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.75%)
# Likes:    1776
# Dislikes: 124
# Total Accepted:    441.1K
# Total Submissions: 964.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#

# @lc code=start
#TAGS sum bisect

from bisect import bisect_left

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = float('inf')
        res = None
        for i in range(1, n):
            for j in range(i+1, n):
                u = nums[i]
                v = nums[j]
                x = target - u - v
                k = bisect_left(nums, x, 0, i)
                if k == i:
                    k = i - 1
                elif nums[k] == x:
                    return target
                elif k > 0 and nums[k] - x > x - nums[k-1]:
                    k = k - 1
                w = nums[k]
                if abs(u + v + w - target) < best:
                    best = abs(u + v + w - target)
                    res = u + v + w

        return res



# @lc code=end

