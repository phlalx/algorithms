#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (24.37%)
# Likes:    1826
# Dislikes: 101
# Total Accepted:    236.8K
# Total Submissions: 971.3K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#

# @lc code=start
#TAGS dp
#TODO there are better solutions, check discussions

import functools

class Solution:

    def isMatch(self, s: str, pat: str) -> bool:
        n = len(s)
        p = len(pat)
        @functools.lru_cache()
        def f(i, j):
            if i == n and j == p:
                return True
            elif j == p:
                return False
            elif i == n:
                return pat[j] == '*' and f(i, j+1)
            elif pat[j] == '*':
                return f(i+1, j) or f(i, j+1)
            else:
                return (pat[j] in {s[i], '?'}) and f(i+1, j+1)

        return f(0, 0)
# @lc code=end

