# TAGS graph BFS dp classic
#
# Important to understand why BFS is better than DP. This is a good
# problem to think about differences between BFS and DP.
#
# DP is is more general, we can consider arbitrary recurrence relation
# of the form f(x) = F( f(x') for x -> x' )
#
# BFS is restricted to f(x) = min (1 + f(x') for x -> x')
#
# We can use dp to solve this problem, but for this particular case
# BFS is faster. DP will consider unnecessary paths.

# f(x) = min(f(x - k * k) for k in ...)
#
# memo = {}
# def dp(x):
#     res = memo.get(x)
#     if res is not None:
#         return res
#     k = 1
#     res = float('inf')
#     while k * k <= x:
#         res = min(dp(x - k * k))
#     memo[x] = res
#     return res

# O(n) space complexity, O(n ** 2) time complexity
# memo array reused between calls
# -> TLA


class Solution(object):
    def __init__(self):
        self.memo = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(self.memo):
            return self.memo[n]

        for target in range(len(self.memo), n + 1):
            res = float("inf")
            i = 1
            while i * i <= target:
                res = min(res, 1 + self.memo[target - i * i])
                i += 1
            self.memo.append(res)

        return self.memo[n]


from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([n])
        visited = {n: 0}
        while q:
            s = q.popleft()
            if s == 0:
                return visited[s]
            k = 1
            while k * k <= n:
                t = s - k * k
                d = visited.get(t)
                if d is None:
                    visited[t] = visited[s] + 1
                    q.append(t)
                k += 1
        assert False

# Math solution -> probably not expected solution, but dp doesn't pass
# the judge

def isSquare(n):
    return int(n ** 0.5) ** 2 == n


class Solution(object):

    # Math solution, based on Four Square theorem
    # There are four possible results: 1, 2, 3, 4
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isSquare(n):
            return 1
        # The result is 4 if and only if n can be written in the  form of 4^k*(8*m + 7)
        # Legendre's three-square theorem.
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(int(n ** 0.5) + 1):
            if isSquare(n - i * i):
                return 2
        return 3

