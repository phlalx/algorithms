#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (40.35%)
# Likes:    513
# Dislikes: 114
# Total Accepted:    124.1K
# Total Submissions: 307.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
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
# Input: 14
# Output: false
#
#
#
#
#TAGS TODO check solution

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        sq = 0
        while sq < num:
            sq += 2 * i + 1
            i += 1
        return sq == num




# @lc code=end

