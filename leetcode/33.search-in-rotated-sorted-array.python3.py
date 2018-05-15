# TAGS binary search


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            middle = (i + j) // 2
            assert 0 <= i <= middle < middle + 1 <= j <= n - 1
            if nums[i] < nums[middle]:
                if nums[i] <= target <= nums[middle]:
                    j = middle
                else:
                    i = middle + 1
            else:
                # assert nums[middle+1] < nums[j]
                if nums[middle + 1] <= target <= nums[j]:
                    i = middle + 1
                else:
                    j = middle

        return i if nums[i] == target else -1
