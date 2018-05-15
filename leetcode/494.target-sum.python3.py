# TAGS dp

import functools


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)

        @functools.lru_cache(maxsize=None)
        def target(i, S):
            if i == n:
                return S == 0
            else:
                return target(i + 1, S - nums[i]) + target(i + 1, S + nums[i])

        return target(0, S)
