# TAGS priority queue
# tricky TODO too slow... see how it relates to k-list merge
# TODO see 378 too
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/209985/python-heap-solution-with-detail-explanation

import heapq
import itertools


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        h = [(i + j, (i, j)) for i in nums1[:k] for j in nums2[:k]]
        heapq.heapify(h)
        res = []
        for _ in range(min(k, len(h))):
            res.append(heapq.heappop(h)[1])
        return res
