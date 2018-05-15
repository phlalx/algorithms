# TAGS interval pythonic
# based on solution 56. We don't sort the initial array, but insert
# in the right place the new interval.
# TODO see why it's hard


def it(interval, intervals):
    n = len(intervals)
    i = 0
    while i < n and intervals[i][0] < interval[0]:
        yield intervals[i]
        i += 1
    yield interval
    while i < n:
        yield intervals[i]
        i += 1


class Solution:
    def insert(self, intervals, newInterval):
        iterator = iter(it(newInterval, intervals))
        cur = next(iterator)
        res = []
        for interv in iterator:
            if cur[1] >= interv[0]:  # if overlap, merge
                cur[1] = max(cur[1], interv[1])
            else:
                res.append(cur)
                cur = interv
        res.append(cur)
        return res
