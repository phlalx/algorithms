# TAGS array, danish flag


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            a = nums[j]
            if a == 1:
                j += 1
            elif a == 2:
                nums[j] = nums[k]
                nums[k] = 2
                k -= 1
            else:  # a == 0
                nums[i] = 0
                i += 1
                j += 1
                if j != i:
                    nums[j - 1] = 1


# Solution().sortColors([1,2,2,2,2,0,0,0,1,1])
