# DIKSTRA

from heapq import heappush, heappop

# as with other graph traversal, we always add edges one
# at a time. Here we greedily choose the edge that connect
# to the closest point not explored yet.

def dijkstra(graph):
  dist = [ None ] * len(graph) # min dist from 0 to node of index i
  heap = [] # no need for a heap constructor, just a list
  init_node = 0
  init_dist = 0
  # lexicographic order, so put distance first
  heappush(heap, (init_dist, init_node))
  while heap:
    # heappop and heappush are functions, since a heap is just a list
    d, n = heappop(heap)
    if dist[n] is None:
      dist[n] = d
    else:
      assert dist[n] < d
      continue
    for nn, dd in graph[n]:
      # important difference with dfs and bfs. We may add
      # an edge to an already seen point. We don't know
      # at that stage which of these points is the closest,
      # they are still in the queue.
      if dist[nn] is not None:
        continue
      heappush(heap, (d + dd, nn))
  print('--- dijkstra')
  print(dist)

# Notes on SSSP (single source shortest path)