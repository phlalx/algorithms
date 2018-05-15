# TAGS greedy, cool

# We can find the minimum radius recursively
# suppose we place n - 1 houses
# for the n-th house, we use the closest heater
# Solution is max(best for n - 1 houses, radius for n-th house)
#
# suppose we have n houses, and p heaters

# Solution 1
# O(n * log(p))
#
# from bisect import bisect_left

# def d(x, y):
#   return abs(x - y)

# # t is a non-empty sorted array
# # return closest element to x
# def closest(t, x):
#   n = len(t)
#   i = bisect_left(t, x)
#   if i == n:
#     return t[i-1]
#   elif i == 0:
#     return t[i]
#   elif d(x, t[i]) <= d(x, t[i-1]):
#     return t[i]
#   else:
#     return t[i-1]
#
# assert closest([1,4,4,7], 2) == 1
#
# def f(houses, heaters):
#   assert heaters
#   houses.sort()
#   heaters.sort()
#   return max((d(closest(heaters, house), house) for house in houses),
#              default=0)

# Solution 2
# O(n + p)
#


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        dist = lambda i, j: abs(houses[i] - heaters[j])
        i = 0
        best_j = 0
        res = 0

        for i in range(len(houses)):
            j = best_j
            best = float("inf")
            while j < len(heaters) and dist(i, j) <= best:
                best = dist(i, j)
                best_j = j
                j += 1
            res = max(res, best)
        return res
