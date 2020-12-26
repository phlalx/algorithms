# TAGS bfs
# First idea is dp with storing result (see combination sum)
# But it seem tedious
# Solution here is BFS
# Just remove parenthesis until reaching a final step
# This is a variant of BFS, there maybe be several solution
#
# Complexity: 2^n * n (number of substrings * time to check if it is balanced)
# TODO too slow

# check https://leetcode.com/problems/remove-invalid-parentheses/discuss/75028/Short-Python-BFS

from collections import deque


def neigh(s):
    res = []
    for i, c in enumerate(s):
        if c == "(" or c == ")":
            res.append(s[:i] + s[i + 1 :])
    return res


def isbalanced(s):
    count = 0
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0


def bfs(s):

    next = deque([s])
    seen = set([s])
    res = []

    maximum = float("-inf")

    while next:
        s = next.pop()

        if isbalanced(s):
            if len(s) >= maximum:
                res.append(s)
                maximum = len(s)
            else:
                break

        for n in neigh(s):
            if n not in seen:
                seen.add(n)
                next.appendleft(n)

    return res


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return bfs(s)
