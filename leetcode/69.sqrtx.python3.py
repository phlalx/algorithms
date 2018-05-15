# TAGS binary search


class Square:
    def __getitem__(self, i):
        return i * i


import bisect


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = bisect.bisect_left(Square(), x, 0, x + 1)
        if res * res == x:
            return res
        else:
            return res - 1
