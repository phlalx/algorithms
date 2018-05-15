#TAGS grid, cool, multisource BFS
# see 200
#
# Let N = n * p
#
# Bellman ford runs in N^2
# Optimal solution in N

INF = 2147483647

# Solution 1: Bellman-ford, TLE ...  
#
# class Solution:
#     def wallsAndGates(self, rooms):
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         if not rooms or not rooms[0]:
#             return

#         n = len(rooms)
#         p = len(rooms[0])
#         wall = sum(l.count(-1) for l in rooms)
#         print(n*p, wall)

#         def neighs(i, j):
#             for u, v in zip([0,1,0,-1], [1,0,-1,0]):
#                 ii = i + u
#                 jj = j + v
#                 if 0 <= ii < n and 0 <= jj < p and rooms[ii][jj] != -1:
#                     yield ii, jj

#         for _ in range(n*p-wall):
#             for i in range(n):
#                 for j in range(p):
#                     if rooms[i][j] == -1:
#                         continue
#                     for ii, jj in neighs(i, j):
#                         rooms[i][j] = min(rooms[i][j], 1 + rooms[ii][jj])

# Solution 2: Multisource BFS
#

from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        n = len(rooms)
        p = len(rooms[0])

        gates = []
        for i in range(n):
            for j in range(p):
                if rooms[i][j] == 0:
                    gates.append((i, j))

        def neighs(i, j):
            for u, v in zip([0,1,0,-1], [1,0,-1,0]):
                ii = i + u
                jj = j + v
                if 0 <= ii < n and 0 <= jj < p and rooms[ii][jj] != -1:
                    yield ii, jj

        q = deque(gates)
        while q:
            i, j = q.popleft()
            for ii, jj in neighs(i, j):
                if rooms[ii][jj] == INF:
                    rooms[ii][jj] = rooms[i][j] + 1
                    q.append((ii, jj))

