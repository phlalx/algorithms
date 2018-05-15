#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.09%)
# Likes:    1904
# Dislikes: 1618
# Total Accepted:    617K
# Total Submissions: 1.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
from collections import deque

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pr = []
        w = strs[0]
        i = 0
        for c in w:
            if all(len(str) > i and str[i] == c for str in strs):
                pr.append(c)
            else:
                break
            i += 1
        return ''.join(pr)

        






        
# @lc code=end

