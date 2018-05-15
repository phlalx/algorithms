#TAGS sliding window

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        distinct = 0
        i = 0
        n = len(s)
        counter = Counter()
        res = 0
        for j in range(n):
            if counter[s[j]] == 0:
                distinct += 1
            counter[s[j]] += 1
            while distinct > k:
                if counter[s[i]] == 1:
                    distinct -= 1
                counter[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

