#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (33.21%)
# Likes:    777
# Dislikes: 27
# Total Accepted:    34.2K
# Total Submissions: 102.4K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#
# TAGS parenthesis

# @lc code=start
# trick isValid(cur, i):
#   cur is the number of open parenthesis
# TODO maybe a different dp relation
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = {}
        def isValid(cur, i):
            res  = memo.get((cur,i))
            if res is not None:
                return res
            if i == n:
                res = cur == 0
            elif cur < 0:
                res = False
            elif s[i] == '(':   
                res = isValid(cur+1, i+1)
            elif s[i] == ')':
                res = isValid(cur-1, i+1)
            else: # s[i] == '*':
                res = isValid(cur-1, i+1) or isValid(cur+1, i+1) or isValid(cur, i+1)
            memo[(cur, i )] = res
            return res
        return isValid(0, 0)
            

# @lc code=end

