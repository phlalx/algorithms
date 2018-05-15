#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (35.94%)
# Likes:    1191
# Dislikes: 43
# Total Accepted:    65.3K
# Total Submissions: 175.8K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
#
#
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
#
# Note:
#
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
#
#
#

# TAGS bellman, graph, 2d optimization
# @lc code=start
# Path length, think Bellman Ford! however, we need to adapt BF. It's not
# enough to change the loop constants as some node distance may be updated
# "faster" than others.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, K: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        trips = K + 1  # K stops means K + 1 trip
        new_dist = [None] * n
        for _ in range(trips):
            # TRICK need to upgrade distances simultaneously
            # initialize new_dist with the best distances known for k
            new_dist[:] = dist[:]
            # we relax new_dist[s'] for each edge s -w-> s'
            for x, y, w in flights:
                new_dist[y] = min(new_dist[y], dist[x] + w)
                # TRICK this is not equivalent to
                # new_dist[y] = min(dist[y], dist[x] + w]
            dist[:] = new_dist[:]
        return dist[dst] if dist[dst] != float('inf') else -1
# @lc code=end
