# TAGS binary search, array
# not expected solution, see greedy

import bisect


def is_sol(houses, heaters, radius):
    i = 0

    for h in heaters:
        while i < len(houses) and h - radius <= houses[i] <= h + radius:
            i += 1

    return i == len(houses)


class wrapper:
    def __init__(self, houses, heaters):
        self.heaters = heaters
        self.houses = houses

    def __getitem__(self, radius):
        return is_sol(self.houses, self.heaters, radius)

    def __len__(self):
        return 10 ** 9 + 1


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        return bisect.bisect_left(wrapper(houses, heaters), 1, 0)
