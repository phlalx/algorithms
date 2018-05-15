# TAGS dict

import collections


class Solution:
    def numberOfBoomerangs(self, point):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        dist = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        n = len(point)
        counters = [collections.Counter() for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                tmp = dist(point[i], point[j])
                counters[i][tmp] += 1
                counters[j][tmp] += 1

        res = 0
        for i in range(n):
            for x in counters[i].values():
                res += x * (x - 1)
        return res
