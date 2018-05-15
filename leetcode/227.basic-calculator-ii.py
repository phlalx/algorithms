#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (34.40%)
# Likes:    1089
# Dislikes: 198
# Total Accepted:    153K
# Total Submissions: 428.6K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#
#
#

#TAGS lexer, parser
#see 726, 227, 394
#
# the "hard" thing in this exercise is to not start with the general solution
# (lexer + parser), but think about a more ad-hoc solution.
#
# A*B*C + X*Y*Z + U*V*W (think +|- and *|/)
# Try to build the current factor, and add it to the cur res as soon as it
# is "validated"

# @lc code=start



def lexer(s):
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] in {'+', '-', '*', '/'}:
            yield s[i]
            i += 1
        else:
            num = 0
            while i < n and s[i] in "0123456789":
                num = num * 10 + int(s[i])
                i += 1
            yield num

# Solution 1:
# recursive descent parser
# Very general, but overkill for this problem
#
# S = A (+ A) *
# A = N (* N) *

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        it = lexer(s)
        cur = next(it, None)
        def S():
            nonlocal cur
            res = A()
            while cur is not None:
                op = cur
                cur = next(it, None)
                if op == '+':
                    res += A()
                elif op == '-':
                    res -= A()
                else:
                    assert 0
            return res
        def A():
            nonlocal cur
            res = cur
            cur = next(it, None)
            while cur not in {None, '+', '-'}:
                op = cur
                cur = next(it, None)
                if op == '*':
                    res *= cur
                elif op == '/':
                    res //= cur
                else:
                    assert 0
                cur = next(it, None)
            return res
        return S()

# Solution 2
# Use a stack
# we modify lexer so that it ends with a sentinel '+'

def lexer(s):
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] in {'+', '-', '*', '/'}:
            yield s[i]
            i += 1
        else:
            num = 0
            while i < n and s[i] in "0123456789":
                num = num * 10 + int(s[i])
                i += 1
            yield num
    yield '+'

class Solution:
    def calculate(self, s: str) -> int:
        it = iter(lexer(s))
        st = [next(it)]
        for x in it:
            if x in {'+', '-'}:
                # we compute what's on the stack (one or three elements)
                if len(st) > 1:
                    if st[-2] == '+':
                        st[-3] += st[-1]
                    if st[-2] == '-':
                        st[-3] -= st[-1]
                    st.pop()
                    st.pop()
                st.append(x)
            elif x in {'*', '/'}:
                st.append(x)
            else:  # a number
                if st[-1] == '*':
                    st[-2] = st[-2] * x
                    st.pop()
                elif st[-1] == '/':
                    st[-2] = st[-2] // x
                    st.pop()
                else:
                    st.append(x)
        return st[0]

# Solution 3
# The correct solution
# There's no need for a stack since it doesn't grow more than 3 elements
# Let's keep the same idea but with variable.

def lexer(s):
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] in {'+', '-', '*', '/'}:
            yield s[i]
            i += 1
        else:
            num = 0
            while i < n and s[i] in "0123456789":
                num = num * 10 + int(s[i])
                i += 1
            yield num
    yield '+'

class Solution:
    def calculate(self, s: str) -> int:
        it = iter(lexer(s))
        res = 0
        cur_op = '+'
        cur_prod_op = '*'
        factor = 1
        for x in it:
            if x in {'+', '-'}:
                res += factor if cur_op == '+' else -factor
                cur_op = x
                cur_prod_op = '*'
                factor = 1
            elif x in {'*', '/'}:
                cur_prod_op = x
            else:
                if cur_prod_op == '*':
                    factor *= x
                else:
                    factor //= x
        return res

# @lc code=end

