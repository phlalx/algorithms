# TAGS dp


def numDecode(memo, s, i):
    if memo[i] != -1:
        return memo[i]
    if i == len(s):
        res = 1
    elif i == len(s) - 1:
        res = 1 if s[i] != "0" else 0
    else:
        a, b = s[i : i + 2]
        if a == "0":
            res = 0
        else:
            res = numDecode(memo, s, i + 1)
            if a == "1" or (a == "2" and "0" <= b <= "6"):
                res = res + numDecode(memo, s, i + 2)
    memo[i] = res
    return res


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [-1] * (len(s) + 1)
        if s:
            return numDecode(memo, s, 0)
        else:
            return 0


s = Solution()
assert s.numDecodings("") == 0
assert s.numDecodings("0") == 0
assert s.numDecodings("1") == 1
assert s.numDecodings("11") == 2
