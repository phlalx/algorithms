#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (45.54%)
# Likes:    396
# Dislikes: 32
# Total Accepted:    54.1K
# Total Submissions: 118.6K
# Testcase Example:  '[-2,0,1,3]\n2'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
#
# Example:
#
#
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than
# 2:
# [-2,0,1]
# ⁠            [-2,0,3]
#
#
# Follow up: Could you solve it in O(n^2) runtime?
#
#

# Solution 1: n.log(n)
#
# from bisect import bisect_left

# class Solution:
#     def threeSumSmaller(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 v = nums[i] + nums[j]
#                 k = bisect_left(nums, target - v, 0, i)
#                 count += k
#         return count


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        # def count(i, j, t):
        #     if i > j:
        #         return 0
        #     elif nums[i] + nums[j] < t:
        #         return j - i + count(i+1, j, t)
        #     else:
        #         return count(i, j-1, t)
        # think recursively
        def count(i, j, t):
            res = 0
            while i <= j:
                if nums[i] + nums[j] < t:
                    res += j - i
                    i += 1
                else:
                    j -= 1
            return res
        for k, v in enumerate(nums):
            res += count(k+1, n-1, target - v)
        return res




