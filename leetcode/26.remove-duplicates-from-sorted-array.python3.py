# TAGS array


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        i = 1  # position of next element to write in the array
        j = 1  # position of next element to consider for writing
        while j < n:
            if nums[j - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# Other simple idea, copy array (j) to new array (i). We can use
# the same array since i <= j
