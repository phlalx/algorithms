# TAGS array cool
# See "two-sum"

from collections import Counter


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter()
        res = 0
        cur = 0
        c[0] = 1
        for v in nums:
            cur += v
            res += c[cur - k]
            c[cur] += 1
        return res
