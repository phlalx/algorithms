#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.28%)
# Likes:    533
# Dislikes: 2121
# Total Accepted:    337.1K
# Total Submissions: 1M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start

def lex(s):
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            while i < n and s[i] == ' ':
                i += 1
        else:
            res = 0
            while i < n and s[i] != ' ':
                res += 1
                i += 1
            yield res

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = None
        for w in lex(s):
            last_len = w
        return last_len if last_len is not None else 0
        
# @lc code=end

