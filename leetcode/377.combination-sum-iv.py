#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (43.88%)
# Likes:    912
# Dislikes: 107
# Total Accepted:    94.1K
# Total Submissions: 214.3K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
#
#

# TAGS dp, bfs
# simple, I didn't see the solution right away

import functools

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int
        """

        @functools.lru_cache(maxsize=None)
        def combin_sum(target):
            if target < 0:
                return 0
            elif target == 0:
                return 1
            else:
                return sum(combin_sum(target - n) for n in nums)

        return combin_sum(target)

