
from collections import Counter

class Solution:
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        p = len(grid[0])
        seen = [[ False ] * p for  _  in  range(n)]

        def neigh(i, j):
            for u, v in zip([0,1,0,-1],[1,0,-1,0]):
                if 0 <= i + u < n and 0 <= j +  v < p and grid[i+u][j+v]  ==  1:
                    yield  i+u, j+v

        def dfs(i, j, or_i, or_j, res):
            assert  grid[i][j]  == 1
            res.append((i - or_i, j - or_j))
            for u, v in neigh(i, j):
                if seen[u][v]:
                    continue
                seen[u][v] = True
                dfs(u, v, or_i, or_j, res)

        count = Counter()

        for i in range(n):
            for j in range(p):
                if seen[i][j] or not grid[i][j]:
                    continue
                seen[i][j] = True
                res = []
                dfs(i, j, i, j, res)
                count[tuple(res)] += 1

        return len(count)
