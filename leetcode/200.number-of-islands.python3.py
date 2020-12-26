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


class UF:
    def __init__(self, n, count):
        self.p = list(range(n))
        self.r = [ 0 ] * n
        self.count = count

def find(uf, i):
    if i == uf.p[i]:
        return i
    res = find(uf, uf.p[i])
    uf.p[i] = res  # optim
    return res

def union(uf, i, j):
    i, j = find(uf, i), find(uf, j)
    if i == j:
        return
    uf.count -= 1
    if uf.r[i] > uf.r[j]: # rank optim
        uf.p[j] = i
    else:  # rank optim
        uf.p[i] = j
        uf.r[j] = max(uf.r[j], 1 + uf.r[i])

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         n = len(grid)
#         p = len(grid[0])
#         count = sum(grid[i][j] == "1" for i in range(n) for j in range(p))
#         uf = UF(n * p, count)
#         f = lambda i, j: i * p + j
#         for i in range(n):
#             for j in range(p):
#                 if grid[i][j] == "1":
#                     if j + 1 < p and grid[i][j+1] == "1":
#                         union(uf, f(i, j), f(i, j+1))
#                     if i + 1 < n and grid[i+1][j] == "1":
#                         union(uf, f(i, j), f(i+1, j))
#         return uf.count
