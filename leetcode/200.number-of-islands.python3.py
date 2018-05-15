# TAGS dfs, grid
# counting connex components


def neighbors(grid, i, j):
    assert grid[i][j]
    res = []
    m = len(grid)
    n = len(grid[0])
    for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        i0 = i + a
        j0 = j + b
        if 0 <= i0 < m and 0 <= j0 < n and grid[i0][j0]:
            res.append((i0, j0))
    return res


def dfs(grid, i, j, seen):
    seen[i][j] = True
    for a, b in neighbors(grid, i, j):
        if seen[a][b]:
            continue
        dfs(grid, a, b, seen)


def countIsland(grid):
    m = len(grid)
    n = len(grid[0])
    seen = [[False for j in range(n)] for i in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            if seen[i][j] or not grid[i][j]:
                continue
            res = res + 1
            dfs(grid, i, j, seen)
    return res


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        grid = [[grid[i][j] == "1" for j in range(n)] for i in range(m)]
        return countIsland(grid)
