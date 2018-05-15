# TAGS binary search, cool, pythonic

# Just a slightly modified binary search


def is_peak(nums, i):
    a = nums[i - 1]
    b = nums[i]
    c = nums[i + 1]
    if b > max(a, c):
        return 0
    if b < c:
        return 1
    if b < a:
        return -1


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert nums
        n = len(nums)
        nums.append(float("-inf"))
        # sentinel, works will with python because nums[-1] = nums[n]!
        # trick

        i = 0
        j = n - 1

        while i != j:
            m = (i + j) // 2
            assert i <= m < m + 1 <= j
            ip = is_peak(nums, m)
            if ip <= 0:
                j = m
            else:
                i = m + 1
        return i
