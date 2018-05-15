# TAGS dp
# little trick


def ispowerof2(n):
    return n >= 1 and (n & (n - 1)) == 0


class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def f(n):
            res = memo.get(n)
            if res is not None:
                return res
            if n == 0:
                res = 1
            elif n == 1:
                res = 0
            elif n % 2 == 0:
                res = 1 + f(n // 2)
            elif ispowerof2(n - 1):
                res = 1 + f(n - 1)
            else:
                res = 1 + min(f(n + 1), f(n - 1))
            memo[n] = res
            return res

        return f(n)
