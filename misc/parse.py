
def parse():
  V = int(input())
  E = int(input())
  graph = [ [] for _ in range(V) ]
  for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
  return graph

