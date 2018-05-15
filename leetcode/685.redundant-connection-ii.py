#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (31.14%)
# Likes:    619
# Dislikes: 184
# Total Accepted:    30.3K
# Total Submissions: 94.9K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
#
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
#
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
#
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# Example 2:
#
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4
#
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
#
#
# https://leetcode.com/problems/redundant-connection-ii/discuss/254733/Python-Union-Find-Clear-Logic
# TAGS super hard

# As the problem states, there is one and only one edge that violates the definition of tree. Therefore, there are three possible cases:
# a. There is no cycle in the graph, but there exist two edges pointing to the same node;
# b. There is a cycle, but there do not exist two edges pointing to the same node;
# c. There is a cycle, and there exist two edges pointing to the same node.

# Use UF on the undirected graph + case analysis based on which node has two parents

# @lc code=start

class UF:
    def __init__(self, n):
        self.p = list(range(n))
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

from collections import defaultdict

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = defaultdict(list)
        cand1 = None
        cand2 = None
        for v1, v2 in edges:
            parent[v2].append(v1)
        for u, v in parent.items():
            if len(v) == 2:
                cand1 = [v[0], u]
                cand2 = [v[1], u]
        print(cand1, cand2)

        # Three cases

        # Case 1 - No cycle
        # return e1

        # Case 2 - Cycle - two parents
        # return edge in cycle

        # Case 3 - Cycle - no two parents
        # return first edge that forms cycle (like 684)

        uf = UF(n)
        if cand2 is None:   # Case 3
            for v1, v2 in edges:
                if union(uf, v1 - 1, v2 - 1):
                    return [v1, v2]
        else:
            for v1, v2 in edges:
                if [v1, v2] == cand2:
                    continue
                if union(uf, v1 - 1, v2 - 1):
                    # Case 1
                    return cand1
            # Case 2
            return cand2


# @lc code=end

