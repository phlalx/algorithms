# TAGS array


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        while True:
            while i < n and nums[i] != 0:
                i += 1
            if i == n:
                return
            j = max(i + 1, j)
            while j < n and nums[j] == 0:
                j += 1
            if j == n:
                return
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1


# other idea, imagine we have two arrays, we copy array (j) by
# to array (i). We skip 0 with j, and increment i by one. Then
# we will up the rest of array (i) with 0
