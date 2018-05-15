#TAGS bfs
# idea is straightforward (run BFS from each building)
# maintain hit grid + sum-dist grid
#
# Trick: don't try to be smart by reusing arrays, just make it work
# TODO can be faster by pruning
#

from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        p = len(grid[0])

        ones = [(i, j) for i in range(n) for j in range(p) if grid[i][j] == 1]

        def neigh(i, j):
            for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < p and grid[ii][jj] == 0:
                    yield ii, jj

         
        dist = [[0 for _ in range(p)] for _ in range(n)]
        hit = [[0 for _ in range(p)] for _ in range(n)]
        
        def bfs(i, j):
            seen = [[0 for _ in range(p)] for _ in range(n)]
            queue = deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for ii, jj in neigh(i, j):
                    if seen[ii][jj] > 0:
                        continue
                    hit[ii][jj] += 1
                    seen[ii][jj] = seen[i][j] + 1
                    dist[ii][jj] = dist[ii][jj] + seen[ii][jj]
                    queue.append((ii, jj))

        for i, j in ones:
            bfs(i, j)

        res = float('inf')
        for i in range(n)  :
            for j in range(p):
                num_one = hit[i][j]
                longest_dist = dist[i][j]
                if num_one == len(ones) and longest_dist < res:
                    res = longest_dist
        return -1 if res == float('inf') else res 


