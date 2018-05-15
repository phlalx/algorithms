#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (48.27%)
# Likes:    1378
# Dislikes: 160
# Total Accepted:    90.4K
# Total Submissions: 180.2K
# Testcase Example:  '"bbbab"'
#
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
#
#
# Example 1:
# Input:
#
# "bbbab"
#
# Output:
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
#
# Example 2:
# Input:
#
# "cbbd"
#
# Output:
#
# 2
#
# One possible longest palindromic subsequence is "bb".
#
#

# @lc code=start
#TAGS dp
# TODO space optimization
# TODO https://leetcode.com/problems/longest-palindromic-subsequence/discuss/222605/DP-Problem-Classifications-Helpful-Notes

import sys

class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        res = [[ None for j in range(n) ] for i in range(n)]

        for i in reversed(range(n)):
            res[i][i] = 1  # TRICK no need for extra loops
            for j in range(i+1, n):
                if s[i] == s[j]:
                    a = 2 + (res[i+1][j-1] if i + 1 <= j - 1 else 0)
                else:
                    a = 0
                res[i][j] = max(a, res[i+1][j], res[i][j-1])
        return res[0][n-1]

# @lc code=end

