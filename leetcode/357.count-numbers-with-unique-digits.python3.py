# TAGS combinatorics
# TODO backtrack

# f(i) = number of unique numbers with length i
# f(0) = 1
# f(1) = 9
# f(2) = 9 * (10 - 1)
# f(3) = f(2) * (10 - 2)


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        # n is the number of digits to consider
        n = min(n, 9)
        unique = 9
        res = 10
        for i in range(2, n + 1):
            unique = unique * (11 - i)
            res += unique
        return res
