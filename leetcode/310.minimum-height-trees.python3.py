# TAGS tree, graph, diameter, khan
#
# Solution 1
#
# Idea:
# 1. find longest path.
#    a. find longest path from arbitrary point.
#       leaf of path is on a longest path (why?)
#    b. find longest path from leaf of previous path
#    c. compute previous path
# 2. return middle element(s)
#
# don't forget corner case

# Solution 2
#
# Based on Khan algorithm for topological sort
# We remove the leaves from the graph
# The one (or two) last leaves removed are the answer

from collections import deque

def solution2(graph):

    q = deque()
    for n, adj in enumerate(graph):
        if len(adj) == 1:
            father = adj[0]
            q.append((n, father))

    res = []
    while q:
        n, father = q.popleft()
        res.append(n)
        if len(graph[father]) == 1:
            q.append((father, graph[father][0]))
        if len(graph[father]) == 0:
            q.append((father, None))

    return res

def longest_path(i, adj, father):
    path_len = 0
    leaf = i
    for j in adj[i]:
        if j == father:
            continue
        pl, l = longest_path(j, adj, i)
        pl += 1
        if pl > path_len:
            path_len = pl
            leaf = l
    return path_len, leaf


def get_path(n1, n2, adj, father, cur):
    for j in adj[n1]:
        if j == father:
            continue
        cur.append(j)
        if j == n2:
            return cur
        lp = get_path(j, n2, adj, n1, cur)
        if lp is not None:
            return lp
        cur.pop()

def solution1(adj):
    # longest path starting from arbitrary node
    _, n1 = longest_path(0, adj, 0)
    # longest path from n1
    _, n2 = longest_path(n1, adj, n1)
    # p = n1 -- ... -- n2 is the diameter of the graph
    p = get_path(n1, n2, adj, n1, [n1])

    n = len(p)
    if n % 2 == 1:
        return [p[n // 2]]
    else:
        return sorted([p[(n // 2) - 1], p[n // 2]])


class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # return solution1(adj)
        return solution1(adj)

