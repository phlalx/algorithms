# TAG dp


class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        memo = [[(0, 0, 0)] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    sq, _, _ = memo[i + 1][j + 1]
                    _, _, lin = memo[i][j + 1]
                    _, col, _ = memo[i + 1][j]
                    x = min(sq + 1, lin + 1, col + 1), col + 1, lin + 1
                    memo[i][j] = x
                    res = max(res, x[0])

        return res ** 2
