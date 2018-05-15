# TAGS string


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            res = res + ((x % 2) != (y % 2))
            x = x // 2
            y = y // 2
        return res
