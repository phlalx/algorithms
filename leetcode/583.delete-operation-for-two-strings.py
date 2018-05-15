#TAGS dp, longest common subsequence, edition distance, classic

class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        p = len(word2)
        memo = {}
        def f(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n:
                res = p - j
            elif j == p:
                res = n - i
            elif word1[i] == word2[j]:
                res = f(i+1, j+1)
            else:
                res = 1 + min(f(i+1, j), f(i, j+1))
            memo[(i, j)] = res
            return res
        return f(0, 0)

# iterative solution
class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        p = len(word2)
        memo = [[None] * (p+1) for _ in range(n+1)]
        for i in range(n+1):  # precompute initial values (base case)
            memo[i][p] = n - i
        for j in range(p+1):
            memo[n][j] = p - j
        for i in reversed(range(n)):
            for j in reversed(range(p)):
                #  use res instead of memo[i][j] = every time
                if word1[i] == word2[j]:
                    res = memo[i+1][j+1]
                else:
                    res = 1 + min(memo[i+1][j], memo[i][j+1])
                memo[i][j] = res
        return memo[0][0]

# Note: we could use space optimization. And this reduces to the longest
#       subsequence problem
