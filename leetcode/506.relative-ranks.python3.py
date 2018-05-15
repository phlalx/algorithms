# TAGS sort cool


def s(r):
    if r < 3:
        return ["Gold Medal", "Silver Medal", "Bronze Medal"][r]
    else:
        return str(r + 1)


def f(scores):
    n = len(scores)
    ranks = sorted(range(n), key=scores.__getitem__, reverse=True)
    res = [None] * n
    for i, r in enumerate(ranks):
        res[r] = s(i)
    return res


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        return f(nums)
