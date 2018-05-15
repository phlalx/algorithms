# TAGS sort

import collections


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = collections.Counter(s)
        l = list(s)
        l.sort()
        l.sort(key=c.__getitem__, reverse=True)
        return "".join(l)
