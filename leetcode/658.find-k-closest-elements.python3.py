# TAGS binary search, cool
#
# Naive = use heap O(n + k.log(n))
#
# This solution, use binary search
# To find the closest element and start from there (kind of a merge sort)
# O(log(n) + k) = O(n)
#
# Note that we don't need to construct the resulting array
# We just compute the bounds, and extract the answer from the initial
# array

import bisect


def d(a, b):
    return abs(a - b)


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        i = bisect.bisect_left(arr, x)
        l = i - 1
        r = i
        res = []
        for _ in range(k):
            if l == -1:
                r += 1
            elif r == n:
                l -= 1
            else:
                a, b = arr[l], arr[r]
                if (d(a, x), a) <= (d(b, x), b):
                    l -= 1
                else:
                    r += 1
        return arr[l + 1 : r]
