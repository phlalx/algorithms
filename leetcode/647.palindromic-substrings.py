#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (57.80%)
# Likes:    2172
# Dislikes: 104
# Total Accepted:    160.8K
# Total Submissions: 269.9K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
# TODO dp, string, palindrome, cool

# return true iff s[i:j+1] is a pal
def ps(s, i, j, memo):
    res = memo[i][j]
    if res:
        return res
    if i >= j:
        res = True
    else:
        res = s[i] == s[j] and ps(s, i + 1, j - 1, memo)
    memo[i][j] = res
    return res


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[None] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, n):
                res = res + ps(s, i, j, memo)
        return res

# @lc code=end

