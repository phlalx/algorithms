# TAGS easy
#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (31.91%)
# Likes:    438
# Dislikes: 87
# Total Accepted:    84.8K
# Total Submissions: 265.5K
# Testcase Example:  '"ab"\n"acb"'
#
# Given two strings s and t, determine if they are both one edit distance
# apart.
# 
# Note: 
# 
# There are 3 possiblities to satisify one edit distance apart:
# 
# 
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# 
# 
# Example 1:
# 
# 
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# 
# 
# Example 2:
# 
# 
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# 
# Example 3:
# 
# 
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
# 
#
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        assert len(s) <= len(t)
        if len(t) > len(s) + 1:
            return False
        if len(t) == len(s):
            n = sum(c != d for c, d in zip(s, t))
            return n == 1
        else:
            i = 0
            while i < len(s) and s[i] == t[i]:
                i += 1
            if i == len(s):
                return True
            else:
                return s[i:] == t[i+1:]

