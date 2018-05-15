# TAGS geometry, classic, cool, monotonic stack

# This a convex hull algorithm based on monotonic stacks.
# O(n.log(n)) complexity
#
# Implementation is simple but tricky.
# Note that there is only one for loop
# First we "normalize" the list of points, then we append
# the last element may break the invariant, but it doesn't
# master because it belongs to the result anyway

import collections


Point = collections.namedtuple("Point", ["x", "y"])


def turn(a, b, c):
    return (a.x - b.x) * (a.y - c.y) - (a.y - b.y) * (a.x - c.x)


class Solution:
    def outerTrees(self, points):
        points = [Point(point[0], point[1]) for point in points]
        points.sort(key=lambda p: (p.x, p.y))
        top = []
        bot = []
        for p in points:
            while len(top) >= 2 and turn(top[-2], top[-1], p) > 0:
                top.pop()
            top.append(p)
            while len(bot) >= 2 and turn(bot[-2], bot[-1], p) < 0:
                bot.pop()
            bot.append(p)
        # set because top and bot share the first and last element
        return list(set(top + bot))
