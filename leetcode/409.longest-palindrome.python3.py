# TAGS palindrome

from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        res = 0
        single = False

        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                single = True

        return res + single
