# TAGS multi-source dfs
# TODO rewrite


class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        if n == 0:
            return []

        p = len(matrix[0])
        if p == 0:
            return []

        seen = [[0] * p for _ in range(n)]
        res = []

        def neighbors(i, j):
            res = []
            for u, v in zip([0, 1, -1, 0], [1, 0, 0, -1]):
                if (
                    0 <= i + u < n
                    and 0 <= j + v < p
                    and matrix[i + u][j + v] >= matrix[i][j]
                ):
                    res.append([i + u, j + v])
            return res

        def dfs_1(i, j):
            seen[i][j] = 1
            for u, v in neighbors(i, j):
                if seen[u][v]:
                    continue
                dfs_1(u, v)

        def dfs_2(i, j):
            if seen[i][j] == 1:
                seen[i][j] = 3
                res.append([i, j])
            else:
                seen[i][j] = 2
            for u, v in neighbors(i, j):
                if seen[u][v] >= 2:
                    continue
                dfs_2(u, v)

        for j in range(p):
            if not seen[0][j]:
                dfs_1(0, j)

        for i in range(n):
            if not seen[i][0]:
                dfs_1(i, 0)

        for i in range(n):
            if seen[i][p - 1] < 2:
                dfs_2(i, p - 1)

        for j in range(p):
            if seen[n - 1][j] < 2:
                dfs_2(n - 1, j)

        return res
