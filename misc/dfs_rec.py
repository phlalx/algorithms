# DFS

import parse

def dfs(graph):
  print('--- dfs_rec')
  V = len(graph)
  seen = [0] * V
  back_edge = 0
  forward_cross_edge = 0
  tree_edge = 0

  def dfs_visit(i):
    nonlocal forward_cross_edge, back_edge, tree_edge
    # This invariant holds because dfs(n) calls are guarded by
    # the condition seen[n].
    assert not seen[i]
    seen[i] = 1
    print(i, ' ', end = '')
    for n, _ in graph[i]:
      if seen[n] == 2:
        forward_cross_edge += 1
        continue
      if seen[n] == 1:
        back_edge += 1
        continue
      tree_edge += 1
      # if we want to build the traversal tree, we would do it here
      # adding edge i -> n to the tree
      dfs_visit(n)
    seen[i] = 2

  for n in range(len(graph)):
    if not seen[n]:
      dfs_visit(n)
  print()

  print('back edge', back_edge)
  print('forward/cross edge', forward_cross_edge)
  print('tree edge', tree_edge)

# CHECK THIS

# lookup for cycle in non-oriented three

def validTree(self, n, edges):
  p = len(edges)
  if p != n - 1:
    return False

  if n == 0:
    return True

  parent = [None] * n  # we keep the parent here, and not only seen
                       # so we don't confuse visiting our parent with
                       # a cycle

  # build adjacency representation
  adj = [[] for _ in range(n)]
  for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)


  parent[0] = -1
  cycle = False
  def dfs(i):
    nonlocal cycle
    for ii in adj[i]:
      if parent[ii] is None:
        parent[ii] = i
        dfs(ii)
      elif parent[i] != ii:
        cycle = True

  dfs(0)
  return not cycle

