#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (36.12%)
# Likes:    534
# Dislikes: 98
# Total Accepted:    22.6K
# Total Submissions: 62K
# Testcase Example:  '1'
#
# Given a positive integer n, return the number of all possible attendance
# records with length n, which will be regarded as rewardable. The answer may
# be very large, return it after mod 10^9 + 7.
#
# A student attendance record is a string that only contains the following
# three characters:
#
#
#
# 'A' : Absent.
# 'L' : Late.
# ⁠'P' : Present.
#
#
#
#
# A record is regarded as rewardable if it doesn't contain more than one 'A'
# (absent) or more than two continuous 'L' (late).
#
# Example 1:
#
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent
# times.
#
#
#
# Note:
# The value of n won't exceed 100,000.
#
#
#
#
#

# @lc code=start
#TAGS dp
# TODO got the idea easily, but struggle to find the proper relation
#      copied from https://leetcode.com/problems/student-attendance-record-ii/discuss/101651/Python-Straightforward-DP-with-Explanation

class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7
        a = b = d = 1
        c = e = f = 0
        for _ in range(n-1):
            a, b, c, d, e, f =  (a+b+c) % MOD, a, b, (a + b + c + d + e + f) % MOD, d, e
        return (a + b + c + d + e + f) % MOD
    # @lc code=end

