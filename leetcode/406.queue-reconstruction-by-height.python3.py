# TAGS tricky, ds

from collections import deque


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [None] * len(people)
        people.sort(key=lambda k: (k[0], -k[1]))
        d = deque(range(len(res)))
        for (h, r) in people:
            i = d[r]
            res[i] = h, r
            del d[r]

        return res

        # idea: fix one parameter
        #
        # The rank is relative to the taller guys, so we place the guys
        # by decreasing size.
        #
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        #
        # First the taller guy,     [7, 0]
        # Then [7,1] comes behind   [7, 1], [7, 0]
        #      [6,1]                [7, 1], [6, 1], [7, 0]
        #      [5,0]                [7, 1], [6, 1], [7, 0], [5, 0]
        #      [5,2]                [7, 1], [6, 1], [5, 2], [7, 0], [5, 0]
        #      [4,4]                [7, 1], [4, 4], [6, 1] ....
        #
        