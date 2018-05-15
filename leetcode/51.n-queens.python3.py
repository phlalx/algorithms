# TAGS backtracking, complete search
# TODO too slow :( use DFS


def solve(N):

    pos = [None] * N

    def check(i):
        for k in range(i):
            # 2 queens are on the same diagonal if | x' - x | == | y' - y |
            if pos[k] == pos[i] or abs(pos[k] - pos[i]) == abs(k - i):
                return False
        return True

    def to_board(pos):
        l = [["."] * N for _ in range(N)]
        for i, j in enumerate(pos):
            l[i][j] = "Q"
        return ["".join(u) for u in l]

    res = []

    def f(i):
        if i == N:
            res.append(to_board(pos))
        else:
            for j in range(N):
                pos[i] = j
                if check(i):
                    f(i + 1)

    f(0)
    return res


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return solve(n)
