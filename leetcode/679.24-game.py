#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (43.68%)
# Likes:    572
# Dislikes: 120
# Total Accepted:    31.6K
# Total Submissions: 70.2K
# Testcase Example:  '[4,1,8,7]'
#
#
# You have 4 cards each containing a number from 1 to 9.  You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of
# 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For
# example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use -
# as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression
# -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2,
# 1, 2], we cannot write this as 12 + 12.
#
#
#
#

# TAGS classic, cool
# Precision: all cards should be used
# I didn't manage to get rid of the floating point operations
# Idea: DFS
# a, b, c, d -> a * b, c ,d
# a, b, c, d -> b, a, c, d
# Trick: We generate all permutations using only two permutations

# pythonic u, *v = x

# You have 4 cards each containing a number from 1 to 9. You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of 24.

from itertools import product

def neighbors(v):
    if len(v) > 1:
        a, b, *c = v
        yield (a + b, *c)
        yield (a - b, *c)
        yield (a * b, *c)
        if b != 0:
            yield (a / b, *c)
        yield (b, a, *c)
        yield v[1:] + (v[0],)

class Solution:
    def judgePoint24(self, nums):
        seen = set()
        eps = 10 ** -8
        def dfs(v):
            res = False
            if len(v) == 1 and abs(v[0] - 24) < eps:
                res = True
            else:
                for vv in neighbors(v):
                    if vv not in seen:
                        seen.add(vv)
                        if dfs(vv):
                            res = True
                            break
            return res
        init = tuple(nums)
        seen.add(init)
        return dfs(init)

# @lc code=end

