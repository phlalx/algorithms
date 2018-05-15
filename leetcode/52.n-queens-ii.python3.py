# TAGS backtrack
# TODO too slow


def solve(N):

    pos = [None] * N

    # check if queens at col i can be captured by previous queens
    def check(i):
        for k in range(i):
            # 2 queens are on the same diagonal if | x' - x | == | y' - y |
            if pos[k] == pos[i] or abs(pos[k] - pos[i]) == abs(k - i):
                return False
        return True

    def f(i):
        if i == N:
            return 1
        res = 0
        for j in range(N):
            pos[i] = j
            if check(i):
                res += f(i + 1)
        return res

    return f(0)


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return solve(n)
