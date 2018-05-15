# FLOYD

# Dijkstra = single source shortest path SSSP, non-negative edges
# compute distance from source to every other point
# can stop when we find a given point, or compute a spanning tree
# O(n log(p))
# = BFS if no weight

# Floyd Warshall = all pairs shortest path O(n^3), negative edges?

# Bellman Ford = single source, similar to FW but can handle negative weights

# All pair shortest path
# REMEMBER
# 0. Dynamic programming algorithm
# 1. f(i, j, k) = path from i to j using only [0..k) as intermediary points
# Don't confuse with bellman ford
# 2. This can be computed IN PLACE, the values needed in the recursive
#    formula aren't updated for a given k

inf = float('inf')
m = [ [inf, 2, 10], [inf, inf, 1], [inf, inf, inf] ]

def fw(m):
    n = len(m)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                m[i][j] = min(m[i][j], m[i][k] + m[k][j])
    return m

print('input', m)
print('output', fw(m))

# It is a DP algorithm
# Careful to choose the right recurrence relation
# 1 - dist(i,j,k) : best distance to go from i to j in at most k step
#   dist(i,j,k) = if k == 1, then M[i][j], else min(dist(i,j,k-1),  min( dist(i,p,k-1) + M[p][j] for all p)
# This leads to an O(n^4) algorithm.
# The correct algorithm is based on :
# 2 - dist(i,j,k) : best distance from i to j using at most {0,…,k-1} as intermediary steps
#  dist(i,j,k) = M[i][j] if k == 0 else float('inf')
#                else min(dist(i,j,k-1), dist(i,k-1,k-1) + dist(k-1,j,k-1)
