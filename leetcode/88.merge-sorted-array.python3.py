# TAGS array
# TODO: insert at the end instead


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0  # pointer on first list
        j = 0  # pointer on second list

        while j < n:
            a = nums2[j]
            j = j + 1
            # insert in first list
            while i < m and nums1[i] <= a:
                i = i + 1
            # i is the index where we want to insert a
            nums1[i + 1 : m + 1] = nums1[i:m]
            nums1[i] = a
            i = i + 1
            m = m + 1
