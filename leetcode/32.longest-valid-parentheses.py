#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.23%)
# Likes:    2778
# Dislikes: 120
# Total Accepted:    249.4K
# Total Submissions: 913.4K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#

# @lc code=start
# Simple solution O(n^2)
# TAGS dp
# memo[i] is the longest valid substring ending in i
# if s[i] is '(', then it is 0
# else s[i] is ')'  we look for the further '('
#
# TODO try a different implementation (monotonic stack?)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        memo = [ None ] * len(s)
        best = 0
        for i, v in enumerate(s):
            if v == '(' or i == 0:
                res = 0
            else:
                j = i - 1 - memo[i-1]
                if j < 0 or s[j] == ')':
                    res = 0
                else: 
                    res = i - j + 1
                    if j - 1 >= 0:
                        res += memo[j-1]
            best = max(best, res)
            memo[i] = res
        return best
# @lc code=end

