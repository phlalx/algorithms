#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (29.39%)
# Likes:    1094
# Dislikes: 115
# Total Accepted:    96.1K
# Total Submissions: 325.6K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
#
# Example 1:
#
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "dcbabcd"
#

# @lc code=start
# TAGS kmp, palindrome, string
#
# Idea: find the largest palindromic prefix v
#       we then have s = u.v
#       and the result is reversed(v) + s
#
#       we find the largest palindromic suffix by using the kmp prefix table
#       on s + '#' + s[::-1]
#
#       the largest palindromic prefix is the longest PSP of s + '#' + s[::-1]
#       given by the last element of the psp tables

class Solution:
    def shortestPalindrome(self, s):
        x = s + '#' + s[::-1]
        kmp = [ 0 ] * len(x)
        res = 0
        for i in range(1, len(x)):
            j = i - 1
            while j >= 0 and x[kmp[j]] != x[i]:
                j = kmp[j] - 1
            kmp[i] = 0 if j == -1 else kmp[j] + 1
        res = kmp[-1]
        ss = s[res:]
        return ss[::-1] + s

# @lc code=end

