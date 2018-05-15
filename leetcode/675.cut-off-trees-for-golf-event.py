# TAGS bfs, grid, implem

from collections import defaultdict, deque

def bfs(u, v, adj):
    q = deque()
    q.append(u)
    seen = {u : 0}
    while q:
        a = q.popleft()
        if a == v:
            return seen[a]
        for b in adj[a]:
            if b in seen:
                continue
            seen[b] = seen[a] + 1
            q.append(b)
    return -1

class Solution:

    def cutOffTree(self, forest):
        assert forest and forest[0]
        adj = defaultdict(list)
        n = len(forest)
        p = len(forest[0])

        def neigh(i, j):
            return ((i + u, j + v) for u, v in zip([-1, 1, 0, 0], [0, 0, -1, 1]) if (0 <= i + u < n and 0 <= j + v < p))

        to_visit = []
        for i in range(n):
            for j in range(p):
                if forest[i][j] == 0:
                    continue
                if forest[i][j] > 1:
                    to_visit.append((forest[i][j], (i,j)))
                for (u, v) in neigh(i, j):
                    if forest[u][v] >= 1:
                        adj[(i,j)].append((u, v))

        to_visit.sort()
        to_visit = [(0, 0)] + [b for (a, b) in to_visit]

        res = 0
        for a, b in zip(to_visit, to_visit[1:]):
            d =  bfs(a, b, adj)
            if d == -1:
                return -1
            res += d
        return res
