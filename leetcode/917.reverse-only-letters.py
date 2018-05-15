#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.03%)
# Likes:    372
# Dislikes: 30
# Total Accepted:    42.6K
# Total Submissions: 75.1K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#
#TAGS TODO seems complicated for easy 56%

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        def bla(s):
            i = 0
            while i < len(s):
                while i < len(s) and not s[i].isalpha():
                    i += 1
                yield i
                i += 1
            yield None

        res = list(S)
        it = bla(S)
        i = next(it)
        for c in reversed(S):
            if c.isalpha():
                res[i] = c
                i = next(it)
        return ''.join(res)

        
# @lc code=end

