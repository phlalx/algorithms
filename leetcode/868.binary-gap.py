#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
# https://leetcode.com/problems/binary-gap/description/
#
# algorithms
# Easy (59.77%)
# Likes:    170
# Dislikes: 412
# Total Accepted:    30.8K
# Total Submissions: 51.2K
# Testcase Example:  '22'
#
# Given a positive integer N, find and return the longest distance between two
# consecutive 1's in the binary representation of N.
# 
# If there aren't two consecutive 1's, return 0.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 22
# Output: 2
# Explanation: 
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive
# pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: 2
# Explanation: 
# 5 in binary is 0b101.
# 
# 
# 
# Example 3:
# 
# 
# Input: 6
# Output: 1
# Explanation: 
# 6 in binary is 0b110.
# 
# 
# 
# Example 4:
# 
# 
# Input: 8
# Output: 0
# Explanation: 
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8,
# so we return 0.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
#TAGS array

# @lc code=start
class Solution:
    def binaryGap(self, N: int) -> int:
        res = 0
        first = False
        streak = 0
        while N > 0:
            d = N % 2
            if d == 1:
                if not first:
                    first = True
                else:
                    res = max(res, streak)
                streak = 1
            else:
                streak += 1
            N //= 2
        return res






        
# @lc code=end

