# BFS

import parse
from collections import deque

def bfs(graph, source):
    print('--- bfs')
    N = len(graph)
    # we use this list both to keep track of the distance, and of the
    # visited nodes.
    # We could also enqueue the distance together with the node, if we don't
    # need to store them (but we need a visited set anyway)
    dist = [None] * N
    queue = deque([source])
    dist[source] = 0 # distance from source to itself is 0
    while queue:
        s = queue.popleft()
        print(s, ' ', end='')
        assert dist[s] is not None
        for n, _ in graph[s]:
            if dist[n] is None:
                # we mark nodes before pushing them to the queue so we can
                # make sure we don't push twice the same node
                # We also keep track of the distance
                dist[n] = dist[s] + 1
                # if we want to build the traversal tree, we would do it here
                # adding a tree edge parent[n] = s
                queue.append(n)

graph = parse.parse()
bfs(graph, 0)

