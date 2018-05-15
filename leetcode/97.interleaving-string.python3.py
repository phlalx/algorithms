# TAGS dp

import functools


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        @functools.lru_cache(maxsize=None)
        def is_interleave(i, j, k):
            if i == len(s1):
                res = s2[j:] == s3[k:]
            elif j == len(s2):
                res = s1[i:] == s3[k:]
            else:
                a = s1[i]
                b = s2[j]
                c = s3[k]
                res = False
                if a == c:
                    res = is_interleave(i + 1, j, k + 1)
                if b == c:
                    res = res or is_interleave(i, j + 1, k + 1)
            return res

        if len(s1) + len(s2) != len(s3):
            return False

        return is_interleave(0, 0, 0)
