#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (46.56%)
# Likes:    442
# Dislikes: 203
# Total Accepted:    57.4K
# Total Submissions: 120.6K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#

#TAGS subsequence

# @lc code=start
def issubseq(w, s): # This is quite classics
    # TODO maybe we could build a map to the next letter
    i = 0
    for c in w:
        i = s.find(c, i)
        if i < 0:
            return False
        i += 1
    return True


class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        best = 0
        res = ""
        for w in d:
            if issubseq(w, s) and (len(w) > best or (len(w) == best and w < res)):
                res = w
                best = len(w)
        return res
 
# @lc code=end

