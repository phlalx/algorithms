#TAGS graph, classic, bipartite

class NotBipartite(Exception):
    pass

def f(graph):

    n = len(graph)
    seen = [None] * n

    def dfs(s, side):
        seen[s] = side

        for t in graph[s]:
            if seen[t] is None :
                dfs(t, not side)
            elif seen[t] == side:
                raise NotBipartite()

    for i in range(n):
        if seen[i] is None:
            dfs(i, True)

class Solution:
    def isBipartite(self, graph):

        try:
            f(graph)
            return True
        except NotBipartite:
            return False

# Solution 2, without exceptions (prolly better to use exceptions)

def g(graph):

    n = len(graph)
    seen = [None] * n

    def dfs(s, side):
        seen[s] = side

        for t in graph[s]:
            if seen[t] is None :
                if not dfs(t, not side):
                    return False
            elif seen[t] == side:
                return False
        return True

    for i in range(n):
        if seen[i] is None:
            if not dfs(i, True):
                return False
    return True

class Solution:
    def isBipartite(self, graph):

        return g(graph)
