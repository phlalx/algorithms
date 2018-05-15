# TAGS intervals, greedy


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort()
        res = []
        for inter in intervals:
            if res and res[-1][1] >= inter[0]:
                res[-1][1] = max(inter[1], res[-1][1])
            else:
                res.append(inter)
        return res
