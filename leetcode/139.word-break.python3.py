# TAGS dp

import functools


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        @functools.lru_cache(maxsize=None)
        def can_decode(i):
            if i == len(s):
                return True
            for w in wordDict:
                if s.startswith(w, i) and can_decode(i + len(w)):
                    return True
            return False

        return can_decode(0)

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        memo = [ None ] * (n + 1)

        memo[n] = True
        for i in reversed(range(n)):

            res = False
            for w in wordDict:
                if s.startswith(w, i) and memo[i + len(w)]:
                    res = True
                    continue
            memo[i] = res

        return memo[0]
