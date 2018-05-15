#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (40.41%)
# Likes:    719
# Dislikes: 22
# Total Accepted:    97.8K
# Total Submissions: 241.9K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
#
# Example 1:
#
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
#
#

# Check if graph has a cycle
# Solution 1 Union-find
# Solution 2 DFS

# def solution_dfs(n, edges):
#   p = len(edges)
#   if p != n - 1:
#     return False

#   if n == 0:
#     return True

#   parent = [None] * n

#   # build adjacency representation
#   adj = [[] for _ in range(n)]
#   for a, b in edges:
#     adj[a].append(b)
#     adj[b].append(a)

#   parent[0] = -1
#   cycle = False
#   def dfs(i):
#     nonlocal cycle
#     for ii in adj[i]:
#       if parent[ii] is None or ii == parent[i]:
#         parent[ii] = i
#         dfs(ii)
#       else:
#         cycle = True

#   dfs(0)
#   return not cycle

class UF:

    def __init__(self, n):
        self.parents = list(range(n))

    def union(self, i, j):
        self.parents[self.find(i)] = j

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

def solution_uf(n, edges):
    uf = UF(n)
    if len(edges) != n - 1:
             return False
    for a, b in edges:
        if uf.find(a) == uf.find(b):
            return False
        uf.union(a, b)
    return True

class Solution:
    def validTree(self, n, edges):
        return solution_uf(n, edges)
