# TAGS cool, corner cases
#
# Intuitve solution
#
# Careful, DP doesn't work. It only works for a palindromic
# subsequence.

# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.85%)
# Likes:    4350
# Dislikes: 397
# Total Accepted:    657.6K
# Total Submissions: 2.4M
# Testcases Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#




class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i, j):
            while 0 <= i and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            i += 1
            j -= 1
            return j - i, (i, j)

        res = (-2, (0, -1))
        for i in range(n):
            res = max(res, expand(i, i), expand(i, i+1)) # pythonic
        _, (i, j) = res
        return s[i:j+1]


