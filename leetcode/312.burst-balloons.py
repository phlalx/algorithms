#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (50.88%)
# Likes:    2203
# Dislikes: 61
# Total Accepted:    92.5K
# Total Submissions: 181.6K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
#TAGS dp
# this is the classic matrix-chain problem, stated in a different way
#
# The trick here is to think of the *last* burst balloon, and not the first
# one (otherwise we don't know what to use for right and left
#
# TAGS dp
# TODO iterative

# @lc code=start

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def f(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            res = 0
            if i <= j:
                for k in range(i, j+1):
                    res = max(res, f(i, k-1) + f(k+1, j) + nums[i-1] * nums[k] * nums[j+1])
            memo[(i,j)] = res
            return res
        return f(1, len(nums) - 2)


# @lc code=end

