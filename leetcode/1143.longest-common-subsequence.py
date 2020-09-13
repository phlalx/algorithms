# TAGS classic dp, easy
# CC: used to implement a diff command
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.51%)
# Likes:    169
# Dislikes: 8
# Total Accepted:    9.1K
# Total Submissions: 15.8K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
#
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
#
#
#
# If there is no common subsequence, return 0.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
#
#
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        p = len(text2)
        memo = [[ None ] * (p+1) for _ in range(n+1)]
        def f(i, j):
            res = memo[i][j]
            if res is not None:
                return res
            res = 0
            if not (i == n or j == p):
                res = max(f(i, j+1), f(i+1, j))
                if text1[i] == text2[j]:
                    res = max(1 + f(i+1, j+1), res)
            memo[i][j] = res
            return res
        return f(0, 0)

