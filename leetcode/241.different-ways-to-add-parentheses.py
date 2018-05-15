#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (51.44%)
# Likes:    1344
# Dislikes: 67
# Total Accepted:    91K
# Total Submissions: 171K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#

# @lc code=start

#TAGS recursive
# Straighforward

operators = ['*', '-', '+']

def eval(op, u, v):
    if op == '*':
        return u * v
    elif op == '+':
        return u + v
    else:
        return u - v

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        tokens = []
        i = 0
        n = len(input)
        while i < n:
            if input[i] in operators:
                tokens.append(input[i])
                i += 1
            else:
                res = 0
                while i < n and input[i] not in operators:
                    res = 10 * res + int(input[i])
                    i += 1
                tokens.append(res)

        def f(i, j):
            if i == j:
                res = [ tokens[i] ]
            else:
                res = []
                for k in range(i, j+1):
                    if tokens[k] in operators:
                        res1 = f(i,k-1)
                        res2 = f(k+1,j)
                        for u in res1:
                            for v in res2:
                                res.append(eval(tokens[k], u, v))
            return res
        
        return f(0, len(tokens) - 1)




# @lc code=end

