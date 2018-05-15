#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (58.07%)
# Likes:    1176
# Dislikes: 90
# Total Accepted:    126K
# Total Submissions: 211.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
# Example:
#
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
#
# Note:
#
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#
#

# @lc code=start

# Trick: think xor

from collections import Counter

def xor_all(nums):
    res = 0
    for x in nums:
        res ^= x
    return res

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        uxorv = xor_all(nums)
        # call u, v the numbers we are looking for
        # here we know u ^ v
        # We would like to divide nums in two groups, so that we can
        # find u and v (reduce to the case where we have only one singleton in
        # the group
        #
        # because u and v are distinct, they differ on one bit
        # let's find such a bit
        #
        b = uxorv & (- uxorv)  #  LSB, think femwick (x and -x are identical up
                               #  to the least significant bit
        # now we know u is in g1, v is in g2
        g1 = [v for v in nums if v & b]
        u = xor_all(g1)
        v = uxorv ^ u
        return [u, v]

# @lc code=end

