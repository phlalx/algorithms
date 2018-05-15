# TAGS transitive closure, dfs
#
# build undirected graph, adjacency list
#   a - x -> b
#   b - 1/x -> b
#
#  We dfs each connected component of the graph. The graph is direct
#  but we can always travel in both direction.
#
#  We compute the variable value for each connected component.
#
#  The query answer exists only if both variables belong to the same
#  component.
#
# Corner case: a variable may not be defined

from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        adjacency = defaultdict(list)

        for (left, right), v in zip(equations, values):
            adjacency[left].append((right, 1 / v))
            adjacency[right].append((left, v))

        component = {}
        values = {}  # we compute the value for each node, supposing the first element
                     # has value 1.

        for variable in adjacency.keys():
            
            if variable in values:
                continue

            values[variable] = 1
            component[variable] = variable

            to_visit = [variable]

            while to_visit:
                node = to_visit.pop()
                for n, r in adjacency[node]:
                    if n in values:
                        continue
                    values[n] = values[node] * r
                    component[n] = variable
                    to_visit.append(n)

        res = []
        for q1, q2 in queries:
            if component.get(q1, 1) == component.get(q2, 2):
                x = values[q1] / values[q2]
            else:
                x = -1
            res.append(x)
        return res