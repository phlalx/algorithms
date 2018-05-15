# DFS ITER
def dfs(graph):
  print('--- dfs_iter')
  seen = [0] * len(graph)
  back_edge = 0
  forward_cross_edge = 0
  tree_edge = 0

  def dfs_visit(node):
    nonlocal seen, back_edge, forward_cross_edge, tree_edge
    next = [node]
    seen[node] = 1
    while next:
      s = next.pop()
      print(s, ' ', end = '')
      assert seen[s] == 1
      for n, _ in graph[s]:
        if seen[n] == 1:
          forward_cross_edge += 1
          continue
        if seen[n] == 2:
          back_edge += 1
          continue
        # we mark nodes before pushing them to next so we can make sure
        # we don't push twice the same node
        seen[n] = 1
        # if we want to build the traversal tree, we would do it here
        # adding edge node -> n to the tree
        tree_edge += 1
        next.append(n)
      seen[s] = 2

  for n in range(len(graph)):
    if not seen[n]:
      dfs_visit(n)
  print()

  print('back edge', back_edge)
  print('forward/cross edge', forward_cross_edge)
  print('tree edge', tree_edge)

# If we don't care about edge classification, one color is enough.
# However, we need to set the color *before* pushing nodes to the next stack.
# This let us make sure we don't push twice the same node to the stack.
# In other words, we only use the color grey

def dfs_simple(graph):
  seen = [False] * len(graph)
  next = [0]
  seen[0] = True
  while next:
    s = next.pop()
    assert seen[s]
    for n, _ in graph[s]:
      if seen[n]:
        continue
      seen[n] = True
      next.append(n)

# Wrong implementations of dfs_simple
# Note that it's easy to make mistakes if not paying attention

# In this first wrong version, we may traverse the same node more than once
# Example:
# 0 -> 1, 1 -> 2, 0 -> 2
# We'll visit nodes 0, 1, 2, 2
def dfs_wrong1(graph):
  seen = [False] * len(graph)
  next = [0]
  while next:
    s = next.pop()
    seen[s] = True
    for n, _ in graph[s]:
      if seen[n]:
        continue
      next.append(n)

# this is correct although less efficient than dfs_simple
# we may add the same node several times to next
# it will be ignore the second time it is traversed but we could have
# ignored it before pushing it to next
def dfs_wrong2(graph):
  seen = [False] * len(graph)
  next = [0]
  while next:
    s = next.pop()
    if seen[s]:
      continue
    print(s)
    seen[s] = True
    for n, _ in graph[s]:
      if seen[n]:
        continue
      next.append(n)