# TAGS array

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n log(n)) solution
        n = len(nums)
        sorted_nums = sorted(nums)
        i = next((i for i in range(n) if sorted_nums[i] != nums[i]), 0)
        j = next((i for i in reversed(range(n)) if sorted_nums[i] != nums[i]),
                -1)
        return j - i + 1

