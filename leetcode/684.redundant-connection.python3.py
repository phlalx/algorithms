# TAGS cycles, union find, kruskaw, classic


class UF:
    def __init__(self, n):
        self.p = list(range(n))  # pythonic
        self.r = [0] * n


def find(uf, i):
    if i == uf.p[i]:
        return i
    res = find(uf, uf.p[i])
    uf.p[i] = res
    return res


def union(uf, i, j):
    i, j = find(uf, i), find(uf, j)
    if i == j:
        return True
    if uf.r[i] > uf.r[j]:
        uf.p[j] = i
    else:
        uf.p[i] = j
        uf.r[j] = max(uf.r[j], 1 + uf.r[i])
    return False


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        uf = UF(n)
        for e1, e2 in edges:
            if union(uf, e1 - 1, e2 - 1):
                return [e1, e2]


# Naive implem, running DFS for every edge
# class Cycle(Exception):

#     def __init__(self, e):
#         self.e = e

# def has_cycle(adj):

#     seen = [ False ] * len(adj)

#     def dfs(i, father):

#         for j in adj[i]:
#             if j == father:
#                 continue
#             if seen[j]:
#                 raise Cycle(sorted([i+1, j+1]))
#             seen[j] = True
#             dfs(j, i)

#     for i in range(len(seen)):
#         if seen[i]:
#             continue
#         seen[i] = True
#         dfs(i, None)

# class Solution:
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         # idée, supprimer une arête qui peut être enlevée
#         # sans baisser le nombre de composantes connexes

#         n = len(edges)

#         adj = [ [] for _ in range(n)]
#         for e1, e2 in edges:
#             adj[e1-1].append(e2-1)
#             adj[e2-1].append(e1-1)
#             try:
#                 has_cycle(adj)
#             except Cycle:
#                 return [e1, e2]
