# TAGS dp, knapsack
# TLE in python3

# Recursive solution
#
# class Solution:
#     def findMaxForm(self, strs, m, n):
#         """
#         :type strs: List[str]
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         strs = [ (w.count('0'), w.count('1')) for w in strs ]
#         N = len(strs)

#         memo = {}

#         def f(i, m, n):
#             tmp = memo.get((i,m,n))
#             if tmp is not None:
#                 return tmp
#             if i == N or (m == 0 and n == 0):
#                 res = 0
#             else:
#                 res = f(i+1, m, n)
#                 a, b = strs[i]
#                 if a <= m and b <= n:
#                     res = max(res, 1 + f(i+1, m - a, n - b))
#             memo[i,m,n] = res
#             return res

#         return f(0, m, n)

# iterative DP, space optimization (similar to floyd warshall)
class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs = [(w.count("0"), w.count("1")) for w in strs]
        N = len(strs)

        # memo[m][n]
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for i in reversed(range(N)):
            for a in reversed(range(m + 1)):  # be careful to loop in the right order
                for b in reversed(range(n + 1)):
                    aa, bb = strs[i]
                    if aa <= a and bb <= b:
                        memo[a][b] = max(memo[a][b], 1 + memo[a - aa][b - bb])
        return memo[m][n]
