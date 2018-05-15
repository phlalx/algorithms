#TAGS easy, binomial

class Solution:
    def uniquePaths(self, m, n):
        memo = {}
        def f(n, p):
            assert 0 <= p <= n
            if (n, p) in memo:
                return memo[(n, p)]
            if p == 0 or n == p:
                res = 1
            else:
                res = f(n-1, p) + f(n-1, p-1)
            memo[(n, p)] = res
            return res
        return f(n+m-2, m-1)

