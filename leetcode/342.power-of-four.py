#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (40.68%)
# Likes:    385
# Dislikes: 173
# Total Accepted:    132K
# Total Submissions: 321.7K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         l = { 2 ** (2 * n) for n in range(16) }
#         return num in l

#TAGS binary, trick
        
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        one_bit = (num - 1) & num  == 0
        odd_bit = num & (0x55555555) != 0
        return one_bit and odd_bit


# @lc code=end

