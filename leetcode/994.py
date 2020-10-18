#TAGS multisource bfs
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multisource bfs
        if not grid or not grid[0]:
            return -1

        n = len(grid)
        p = len(grid[0])

        def neigh(i, j):
            for di, dj in zip([0,1,-1,0], [1,0,0,-1]):
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < p and grid[ii][jj]:
                    yield ii, jj

        dq = deque([])
        dist = [[None for j in range(p)] for i in range(n)]
        fresh = []
        for i in range(n):
            for j in range(p):
                if grid[i][j] == 2:
                    dq.append((i, j))
                    dist[i][j] = 0
                elif grid[i][j] == 1:
                    fresh.append((i,j))
        while dq:
            i, j = dq.popleft()
            for (ii, jj) in neigh(i, j):
                if dist[ii][jj] is not None:
                    continue
                dq.append((ii, jj))
                dist[ii][jj] = dist[i][j] + 1
        res = 0
        for i, j in fresh:
            if dist[i][j] is None:
                return -1
            res = max(res, dist[i][j])
        return res

