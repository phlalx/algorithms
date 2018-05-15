# TAGS string, dp
# complexity O(len(s).len(p))
# Initially, I tried all the possible ways to consume the star, leading
# to a suboptimal complexity O(len(s)**2.len(p))


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        M = len(s)
        N = len(p)
        memo = [[False] * (N + 1) for _ in range(M + 1)]
        memo[M][N] = True

        for i in reversed(range(M + 1)):
            for j in reversed(range(N)):
                if j + 1 < N and p[j + 1] == "*":
                    res = memo[i][j + 2]
                    if i < M and (p[j] == s[i] or p[j] == "."):
                        res = res or memo[i + 1][j]  # consume the star once
                elif i == M:
                    res = False
                else:
                    res = (p[j] == s[i] or p[j] == ".") and memo[i + 1][j + 1]
                memo[i][j] = res

        return memo[0][0]
