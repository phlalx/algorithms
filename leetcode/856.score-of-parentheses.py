#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (59.54%)
# Likes:    1031
# Dislikes: 35
# Total Accepted:    35.4K
# Total Submissions: 59.2K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
#
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
#
#
#
# Example 1:
#
#
# Input: "()"
# Output: 1
#
#
#
# Example 2:
#
#
# Input: "(())"
# Output: 2
#
#
#
# Example 3:
#
#
# Input: "()()"
# Output: 2
#
#
#
# Example 4:
#
#
# Input: "(()(()))"
# Output: 6
#
#
#
#
# Note:
#
#
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
#
#
#
#
#
#
#
#TAGS stack, parenthesis
# TODO do we need to put the value on the stack or can we compute it
# #    outside? 

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st = []
        for c in S:
            if c == '(':
                st.append(c)
            else:
                tmp_res = 0
                while st[-1] != '(':
                    tmp_res += st[-1]
                    st.pop()
                st[-1] = tmp_res * 2 if tmp_res else 1
        return sum(st)


# @lc code=end

