# TAGS dp

N = 10 ** 9 + 7


def decode_iterative(s):
    memo = [-1] * (len(s) + 1)
    n = len(s)
    assert n >= 1
    memo[n] = 1
    if s[n - 1] == "*":
        memo[n - 1] = 9
    elif s[n - 1] == "0":
        memo[n - 1] = 0
    else:
        memo[n - 1] = 1
    i = n - 2
    while i >= 0:
        a, b = s[i : i + 2]
        if a == "0":
            res = 0
        elif a == "*" and b == "*":
            res = 9 * memo[i + 1] + 15 * memo[i + 2]
        elif a != "*" and b != "*":
            res = memo[i + 1]
            if a == "1" or (a == "2" and b <= "6"):
                res = res + memo[i + 2]
        elif a == "*" and b != "*":
            res = 9 * memo[i + 1]
            if b <= "6":
                res = res + 2 * memo[i + 2]
            else:
                res = res + memo[i + 2]
        elif a != "*" and b == "*":
            res = memo[i + 1]
            if a == "2":
                res = res + 6 * memo[i + 2]
            elif a == "1":
                res = res + 9 * memo[i + 2]
        else:
            assert False
        memo[i] = res % N
        i = i - 1
    return memo[0]


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return decode_iterative(s)


s = Solution()
# print(s.numDecodings("*0"))
