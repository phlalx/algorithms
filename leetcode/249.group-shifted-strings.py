#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (49.81%)
# Likes:    302
# Dislikes: 52
# Total Accepted:    53.1K
# Total Submissions: 106.6K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the
# sequence:
# 
# 
# "abc" -> "bcd" -> ... -> "xyz"
# 
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
# 
# Example:
# 
# 
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
# 
# 
#

from collections import defaultdict

def key(w):
    res = []
    for a, b in zip(w, w[1:]):
        res.append( (ord(b) - ord(a)) % 26 )
    return tuple(res)

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strings:
            d[key(w)].append(w)
        return list(d.values())

