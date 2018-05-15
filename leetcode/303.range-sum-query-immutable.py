#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (39.55%)
# Likes:    651
# Dislikes: 909
# Total Accepted:    169.5K
# Total Submissions: 410.8K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#
#
#

import itertools

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.t = list(itertools.accumulate(nums))


    def sumRange(self, i: int, j: int) -> int:
        return self.t[j] - (0 if i == 0 else self.t[i-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

