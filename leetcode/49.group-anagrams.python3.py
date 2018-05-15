# TAGS map, partition, equivalence classes, pythonic

import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for s in strs:
            ss = str(sorted(s))
            m[ss].append(s)
        return list(m.values())
