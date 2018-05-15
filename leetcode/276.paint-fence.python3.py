# TAGS combinatorics
# TODO too slow...  could compute fast exponential of the matrix but probably
#     not the expected solution


class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        eq = k
        neq = k * (k - 1)
        for _ in range(2, n):
            eq, neq = neq, (k - 1) * (eq + neq)
        return eq + neq
