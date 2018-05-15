#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (32.48%)
# Likes:    928
# Dislikes: 609
# Total Accepted:    94.7K
# Total Submissions: 290.8K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
#
# Note:
#
#
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
#
#
# Example 1:
#
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#
# Example 2:
#
#
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
#
#
#

# @lc code=start
# TAGS eulerian path, classic
# Simple but hard.
# Trick:
#   a connected graph has an euler cycle iff #in(v) = #out(v) for every vertice
#   it has an open euler walk iff there is exactly two vertices with odd degree
#     (in(v) = out(v) + 1 for one vertice, out(v) = in(v) + 1 for the other
#
#   Idea: To find a path, walk greedily, by consuming edges from start,
#   necessarily reach finish, then add missing cycles

#   This idea doesn't lead directly to an algorithm, but we get the same
#   result with simple DFS, the trick is to construct the path backward
#
#   looks very much like a topological sort, except that we don't use
#   a `seen` set

# LEARN THIS ALGORITHM
# - *almost post-order dfs* print backward the visited nodes
# - unlike dfs, we don't mark visited nodes, as we may visited them more
#   than once
# - in order not too loop, visit each edge once (simply remove it from the adjacency list)

#

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for u, v in tickets:
            d[u].append(v)

        res = []
        def f(n):
            while d[n]:
                f(d[n].pop())
            res.append(n)
        f('JFK')

        # Normal DFS doesn't work
        #  because we don't visit twice the same node
        # seen = {'JFK'}
        # res = []
        # def f(x):
        #     for v in d[x]:
        #         if v not in seen:
        #             seen.add(v)
        #             f(v)
        #     res.append(x)
        # f('JFK')

        return res[::-1]  # pythonic

# @lc code=end

