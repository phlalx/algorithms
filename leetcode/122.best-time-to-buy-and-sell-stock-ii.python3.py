# TAGS greedy
import itertools


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for cur, nex in zip(prices, prices[1:]):
            res += max(0, nex - cur)
        return res
