#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (38.08%)
# Likes:    1038
# Dislikes: 291
# Total Accepted:    253.1K
# Total Submissions: 652.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#
#

# @lc code=start

#TAGS string
# TODO can do better

def normalize(s):
    res = []
    f = {}
    count = 0
    for c in s:
        if c in f:
            res.append(f[c])
        else:
            f[c] = count
            count += 1
            res.append(count)
    return res

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return normalize(s) == normalize(t)

# @lc code=end

