# TAGS binary, pythonic, cool

from itertools import combinations


def f(num):
    s = list(range(10))
    res = []
    for p in combinations(s, num):
        h = 0
        m = 0
        for i in p:
            if i >= 6:
                h += 1 << (i - 6)
            else:
                m += 1 << i
        if h < 12 and m < 60:
            res.append("{}:{:02}".format(h, m))
            # f"{h}:{m:02}"
    return res


def g(num):
    def num_bit(n):
        return bin(n).count("1")

    res = []
    for hour in range(12):
        for min in range(60):
            if num_bit(hour) + num_bit(min) != num:
                continue
            res.append(str(hour) + ":" + str(min).zfill(2))
    return res


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return f(num)
