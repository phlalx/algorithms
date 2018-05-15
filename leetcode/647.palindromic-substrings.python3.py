# TODO dfs, string, palindrome, cool

# return true iff s[i:j+1] is a pal
def ps(s, i, j, memo):
    res = memo[i][j]
    if res:
        return res
    if i >= j:
        res = True
    else:
        res = s[i] == s[j] and ps(s, i + 1, j - 1, memo)
    memo[i][j] = res
    return res


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[None] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, n):
                res = res + ps(s, i, j, memo)
        return res
