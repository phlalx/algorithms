#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (35.18%)
# Likes:    1180
# Dislikes: 189
# Total Accepted:    100.1K
# Total Submissions: 283.6K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#
#
#
# Constraints:
#
#
# 0 <= num.length <= 10
# num only contain digits.
#
#
#

# @lc code=start
#TAGS backtrack, cool
# First idea:
#   using backtracking, build all possible expressions
#   quite easy (but think of corner cases)
# But it is not enough
# Also need to eval the expression. Because an expression
# can end with a product (e.g. '2 + 3 * 4'),
# it's not enough to store the evaluation, but also
# separate the last product (see 227.basic-calculator-ii.py)
#
# Take away: the "state" of the nodes of the search tree
# can be more complex than just "i" and the constructed
# value. Also, depending on how complex the state is,
# it may a global object (thing state of a chess game)
# or it can be passed as a parameter (thing string)
#

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        cur_sum = []
        def f(i, # remaining string to parse
              cur_str,  # expression built so far
             ):
            if i == n:
                if sum(cur_sum) == target:
                    res.append(cur_str)
            else:
                if num[i] == '0':
                    bound = min(i+1, n)
                else:
                    bound = n
                for op in {'+', '-', '*'}:
                    j = i
                    while j < bound:
                        new_cur_str = cur_str + op + num[i:j+1]
                        v = int(num[i:j+1])
                        if op == '+':
                            cur_sum.append(v)
                            f(j+1, new_cur_str)
                            cur_sum.pop()
                        elif op == '-':
                            cur_sum.append(-v)
                            f(j+1, new_cur_str)
                            cur_sum.pop()
                        else:
                            old = cur_sum[-1]
                            cur_sum[-1] *= v
                            f(j+1, new_cur_str)
                            cur_sum[-1] = old
                        j += 1
        for i in range(1, n+1):
            cur_sum = [ int(num[:i]) ]
            f(i, num[:i])
            if num[0] == '0':
                break
        return res

# @lc code=end

