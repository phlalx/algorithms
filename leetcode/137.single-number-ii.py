#TAGS bits
# General explanation https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (47.00%)
# Likes:    1136
# Dislikes: 298
# Total Accepted:    191.4K
# Total Submissions: 397.9K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#
#TAGS bitset
#trick count the number of 1 mod 3 using bitwise operations
#use disjunctive normal form

# @lc code=start
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c0 = 0
        c1 = 0
        for i in nums:
            c0, c1 = (~i & c0) | (i & ~c1 & ~c0), (~i & c1) | (i & ~c1 & c0)
        return c0
# @lc code=end
