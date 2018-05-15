# TAGS dp, backtrack, parenthesis
# Take away:
#   this is a generation problem. There are two classes of solution
#   1. backtracking
#   2. build the solution incrementally
#
#  1 is more general. 2 is possible if there is a recurrence relation.
#  Here the recurrence relation is the one for catalan numbers.
#

# Version 1, backtracking

# This would be a dumb backtracking generation of all parenthesis expressions
# *without* the parenthesis matching constraint. The trick is to adapt it
# to add the constraint
class Solution:
    def generateParenthesis(self, n):
        cur = []  # the string being built
        res = []

        def f(i):
            if i == 2 * n:
                cur.append(''.join(cur))
            else:
                cur.append('(')
                f(i+1)
                cur.pop()
                cur.append(')')
                f(i+1)
                cur.pop()

        f(0)
        return res

class Solution:
    def generateParenthesis(self, n):
        cur = []  # the string being built
        open_par = 0
        res = []

        def f(i):
            nonlocal open_par
            if i == 2 * n:
                assert open_par == 0
                res.append(''.join(cur))
            else:
                if 2 * n - i > open_par:
                    cur.append('(')
                    open_par += 1
                    f(i+1)
                    open_par -= 1
                    cur.pop()

                if open_par > 0:
                    cur.append(')')
                    open_par -= 1
                    f(i+1)
                    open_par += 1
                    cur.pop()

        f(0)
        return res

class Solution:
    def generateParenthesis(self, n):
        cur = []  # the string being built
        res = []

        def f(i, open_par):
            if i == 2 * n:
                assert open_par == 0
                res.append(''.join(cur))
            else:
                if 2 * n - i > open_par:
                    cur.append('(')
                    f(i+1, open_par+1)
                    cur.pop()

                if open_par > 0:
                    cur.append(')')
                    f(i+1, open_par-1)
                    cur.pop()

        f(0, 0)
        return res

#   Recursive generation
#
#    the right way to see it is to partition expressions in
#    Cn =
#       (  C_n-1 ) C_0
#       ( C_n-2 )  C_1
#       ( C_n-3 )  C_2


class Solution:
    def generateParenthesis(self, n):
        res = [ None ] * (n+1)
        res[0] = ['']
        res[1] = [ '()' ]
        for i in range(2, n+1):
            s = []
            for j in range(i):
                for exp1 in res[j]:
                    for exp2 in res[i - 1 - j]:
                        s.append( '(' +  exp1 + ')' + exp2)
            res[i] = s
        return res[n]
