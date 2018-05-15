# TAGS integer
# Corner case: sign

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        res = 0
        while x:
            # invariant
            res = res * 10 + (x % 10)
            x = x // 10
        res = sign * res
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0
