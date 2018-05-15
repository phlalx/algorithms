#TAGS dfs

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = [False] * n
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i):
            for neigh in adj[i]:
                if seen[neigh]:
                    continue
                seen[neigh] = True
                dfs(neigh)
        for i in range(n):
            if seen[i]:
                continue
            seen[i] = True
            dfs(i)
            res += 1
        return res
        
