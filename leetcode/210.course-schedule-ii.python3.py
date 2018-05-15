# TAGS dfs, topological sort, graph, classic, khan

def build_graph(numCourses, prerequisites):
    res = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        res[a].append(b)
    return res


class Cycle(BaseException):
    pass


def dfs(graph, node, seen, res):
    seen[node] = 1
    for n in graph[node]:
        if seen[n] == 1:
            raise Cycle
        elif seen[n] == 2:
            continue
        dfs(graph, n, seen, res)
    seen[node] = 2
    res.append(node)


from collections import deque

# variant, khan algorithm
def khan(graph):
    res = []
    q = deque()
    # initialize queue with leaves
    for v, adj in enumerate(graph):
        if not adj:
            q.append(v)
    while q:
        s = q.popleft()
        for t, adj in enumerate(graph):
            if s in adj:
                # update node children
                adj.remove(s)
                # when a node becomes a leaf, we add to q 
                if not adj:
                    q.append(t)
        res.append(s)
    if any(graph):
        return []
    return res


class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = build_graph(numCourses, prerequisites)
        seen = [0 for i in range(numCourses)]
        res = []
        try:
            for i in range(numCourses):
                if seen[i]:
                    continue
                dfs(graph, i, seen, res)
            return res
        except Cycle:
            return []


def test():
    s = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    res = s.findOrder(numCourses, prerequisites)
    print(res)


# test()
