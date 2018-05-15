# TAGS adhoc

import collections


class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = collections.Counter()
        for l in wall:
            cur_sum = 0
            for i in l[:-1]:
                cur_sum += i
                edges[cur_sum] += 1
        return len(wall) - max(edges.values(), default=0)


def test():
    l = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(Solution().leastBricks(l))
